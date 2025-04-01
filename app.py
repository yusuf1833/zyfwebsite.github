from flask import Flask, render_template, request, jsonify
from config import Config
from utils.feishu import feishu_api
import os
import datetime

app = Flask(__name__)
app.config.from_object(Config)

# 添加时间上下文处理器
@app.context_processor
def inject_now():
    return {'now': datetime.datetime.now()}

@app.route('/')
def index():
    """网站首页"""
    try:
        # 获取数据
        sites = feishu_api.get_table_records()
        
        # 获取分类列表（从配置中获取）
        categories = Config.CATEGORIES
        
        # 渲染模板
        return render_template(
            'index.html', 
            sites=sites, 
            categories=categories,
            site_title=Config.SITE_TITLE
        )
    except Exception as e:
        app.logger.error(f"首页加载错误: {str(e)}")
        return render_template(
            'error.html',
            error_title="加载失败",
            error_message="无法从飞书获取数据，请检查网络连接和飞书配置。",
            site_title=Config.SITE_TITLE
        )

@app.route('/api/sites')
def get_sites():
    """API接口，获取网站数据"""
    try:
        # 获取查询参数
        category = request.args.get('category', '')
        search = request.args.get('search', '')
        
        # 获取数据
        sites = feishu_api.get_table_records()
        
        # 筛选数据
        if category and category != "全部":
            sites = [site for site in sites if site.get('category') == category]
        
        if search:
            search = search.lower()
            sites = [
                site for site in sites 
                if search in site.get('title', '').lower() 
                or search in site.get('description', '').lower()
                or any(search in tag.lower() for tag in site.get('tags', []))
            ]
        
        # 返回JSON数据
        return jsonify(sites)
    except Exception as e:
        app.logger.error(f"API错误: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/refresh', methods=['POST'])
def refresh_data():
    """强制刷新数据缓存"""
    try:
        feishu_api.get_table_records(force_refresh=True)
        return jsonify({"success": True, "message": "数据刷新成功"})
    except Exception as e:
        app.logger.error(f"刷新数据错误: {str(e)}")
        return jsonify({"error": str(e)}), 500

# 错误处理
@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        'error.html',
        error_title="页面未找到",
        error_message="您请求的页面不存在。",
        site_title=Config.SITE_TITLE
    ), 404

@app.errorhandler(500)
def server_error(e):
    return render_template(
        'error.html',
        error_title="服务器错误",
        error_message="服务器遇到了一个错误，请稍后再试。",
        site_title=Config.SITE_TITLE
    ), 500

if __name__ == '__main__':
    # 设置主机和端口（优先从环境变量获取）
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    
    # 启动应用
    app.run(host=host, port=port, debug=Config.DEBUG) 