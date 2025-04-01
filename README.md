# 个人网站导航（飞书多维表格驱动）

这是一个基于Flask的网址导航网站，数据来源于飞书多维表格。采用Linear app的简约现代设计风格，提供简洁优雅的阅读体验。

## 功能特点

- 动态导航菜单管理
- 网站内容分类卡片式显示：标题、分类、描述等
- 深色/浅色主题切换
- 响应式设计，适配移动设备和桌面设备
- 搜索功能，快速查找所需网站
- 分类筛选："全部"，"AI应用", "AI模型", "AI社区", "IOT应用", "工作应用", "AI办公", "AI编程", "AI产品经理", "AI写作", "其他"
- 标签系统

## 技术栈

- 后端：Python Flask
- 前端：HTML + CSS + JavaScript
- UI框架：Tailwind CSS
- 图标库：Font Awesome
- 字体：Google Fonts (Noto Sans SC, Noto Serif SC)
- 数据源：飞书多维表格

## 安装与运行

### 环境要求

- Python 3.8+
- Node.js和npm（用于Tailwind CSS构建）

### 安装步骤

1. 克隆仓库
```bash
git clone [仓库地址]
cd [项目文件夹]
```

2. 安装Python依赖
```bash
pip install -r requirements.txt
```

3. 配置飞书应用信息
在 `config.py` 中填入您的飞书应用信息，或者设置环境变量：
```
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret
BASE_ID=your_base_id
TABLE_ID=your_table_id
```

4. 运行应用
```bash
python app.py
```

5. 访问应用
浏览器访问 http://localhost:5000

## 飞书配置指南

### 创建飞书应用

1. 登录[飞书开发者平台](https://open.feishu.cn/)
2. 创建一个新应用
3. 获取应用凭证（App ID 和 App Secret）
4. 在"权限管理"中，开启多维表格权限：`bitable:record:read`

### 创建多维表格

1. 在飞书中创建一个多维表格
2. 创建一个表，包含以下字段：
   - 标题（文本类型）
   - 分类（单选类型，设置选项为：AI应用、AI模型、AI社区、IOT应用、工作应用、AI办公、AI编程、AI产品经理、AI写作、其他）
   - 链接地址（链接类型）
   - 标签（多选类型，根据需要设置选项）
   - 描述（文本类型，可选）
   - 图标（附件类型，可选）
3. 获取多维表格的Base ID和Table ID

## 部署到Vercel

1. 确保项目根目录有 `vercel.json` 文件
2. 在Vercel中导入项目
3. 设置环境变量（FEISHU_APP_ID, FEISHU_APP_SECRET, BASE_ID, TABLE_ID）
4. 完成部署

## 使用指南

### 管理网站内容

1. 通过飞书多维表格添加、编辑或删除网站信息
2. 网站会自动同步飞书中的数据（刷新间隔为5分钟）

### 主题切换

- 点击导航栏右侧的主题图标切换深色/浅色模式

### 搜索和筛选

- 使用顶部搜索框搜索网站
- 使用分类筛选栏按类别筛选网站

## 常见问题

1. **数据没有显示或更新**
   - 检查飞书应用权限是否正确开启
   - 验证多维表格的字段名称是否与代码中一致
   - 确认表格中已添加数据

2. **主题切换不生效**
   - 清除浏览器缓存并刷新页面

3. **部署到Vercel后无法访问飞书API**
   - 检查环境变量是否正确设置
   - 确认飞书应用的权限配置

## 开发与贡献

欢迎贡献代码或提交问题！请参考以下步骤：

1. Fork 仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建Pull Request

## 许可

[MIT License](LICENSE) 