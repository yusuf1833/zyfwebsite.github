import os

class Config:
    # 飞书应用配置
    FEISHU_APP_ID = os.environ.get("FEISHU_APP_ID", "cli_a76c243cb9f0d00b")
    FEISHU_APP_SECRET = os.environ.get("FEISHU_APP_SECRET", "NiFzCMPVTMHC75LVj9fWLYikpFyGbmSK")
    
    # 多维表格配置
    BASE_ID = os.environ.get("BASE_ID", "VS3zbdBAVa4eMKsF1oncLLFRnIc")
    TABLE_ID = os.environ.get("TABLE_ID", "tblYwz3x8qr2oWBz")
    
    # 应用配置
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DEBUG = os.environ.get("DEBUG", "True").lower() in ("true", "1", "t")
    
    # 缓存配置
    CACHE_TIMEOUT = 300  # 5分钟缓存刷新
    
    # 网站配置
    SITE_TITLE = "个人网站导航"
    
    # 分类列表
    CATEGORIES = [
        "全部", 
        "AI应用", 
        "AI模型", 
        "AI社区", 
        "IOT应用", 
        "工作应用", 
        "AI办公", 
        "AI编程", 
        "AI产品经理", 
        "AI写作", 
        "其他"
    ] 