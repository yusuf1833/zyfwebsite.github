import requests
import json
import time
from functools import lru_cache
from config import Config

class FeishuAPI:
    """飞书API工具类，用于获取飞书多维表格数据"""
    
    def __init__(self):
        self.app_id = Config.FEISHU_APP_ID
        self.app_secret = Config.FEISHU_APP_SECRET
        self.base_id = Config.BASE_ID
        self.table_id = Config.TABLE_ID
        self.cache_timeout = Config.CACHE_TIMEOUT
        self.token = None
        self.token_expire_time = 0

    def get_access_token(self):
        """获取飞书访问令牌"""
        # 检查缓存的令牌是否有效
        if self.token and time.time() < self.token_expire_time:
            return self.token
            
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        payload = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        headers = {
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            result = response.json()
            
            if result.get("code") == 0:
                self.token = result.get("tenant_access_token")
                # 设置令牌过期时间（减去60秒的安全边际）
                self.token_expire_time = time.time() + result.get("expire", 7200) - 60
                return self.token
            else:
                print(f"获取飞书令牌失败: {result}")
                return None
        except Exception as e:
            print(f"获取飞书令牌异常: {str(e)}")
            return None

    @lru_cache(maxsize=1)
    def get_table_records(self, force_refresh=False):
        """
        获取多维表格数据
        
        Args:
            force_refresh: 是否强制刷新缓存
            
        Returns:
            格式化后的表格数据列表
        """
        # 如果强制刷新，清除缓存
        if force_refresh:
            self.get_table_records.cache_clear()
            
        token = self.get_access_token()
        if not token:
            return []
            
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.base_id}/tables/{self.table_id}/records"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            result = response.json()
            
            if result.get("code") == 0:
                return self._format_records(result.get("data", {}).get("items", []))
            else:
                print(f"获取表格数据失败: {result}")
                return []
        except Exception as e:
            print(f"获取表格数据异常: {str(e)}")
            return []
    
    def _format_records(self, records):
        """
        格式化表格记录
        
        Args:
            records: 原始记录列表
            
        Returns:
            格式化后的记录列表
        """
        formatted_records = []
        
        for record in records:
            record_id = record.get("record_id")
            fields = record.get("fields", {})
            
            # 提取字段值
            title = fields.get("标题", "")
            category = fields.get("分类", "")
            url = fields.get("链接地址", "")
            tags = fields.get("标签", [])
            description = fields.get("描述", "")
            icon = fields.get("图标", [])
            
            # 如果有图标附件，提取第一个图标的URL
            icon_url = ""
            if icon and isinstance(icon, list) and len(icon) > 0:
                icon_url = icon[0].get("url", "")
            
            # 创建格式化的记录
            formatted_record = {
                "id": record_id,
                "title": title,
                "category": category,
                "url": url,
                "tags": tags,
                "description": description,
                "icon_url": icon_url
            }
            
            formatted_records.append(formatted_record)
        
        return formatted_records

# 创建API实例
feishu_api = FeishuAPI() 