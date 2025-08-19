# CLAUDE.md

此文件为 Claude Code (claude.ai/code) 提供在操作此代码仓库时的指导信息。

## 项目概述
这是一个使用 PaperMod 主题的 Hugo 静态网站项目。项目结构遵循标准 Hugo 规范，并通过 PaperMod 主题进行了定制。

## 核心开发命令

### Hugo 基础命令
- `hugo server` - 启动本地开发服务器，实时重载，访问 localhost:1313
- `hugo server -D` - 开发模式包含草稿文章
- `hugo` - 构建静态站点到 `public/` 目录
- `hugo --minify` - 生产环境构建，包含代码压缩
- `hugo new posts/文章标题.md` - 在 content/posts/ 创建新博客文章
- `hugo new 页面标题.md` - 创建新的独立页面
- **项目记忆**：每次操作完成后，**不要自动启动项目**，**不要执行 `hugo server -D`**

### 项目目录结构
- **content/** - 网站内容（文章、页面等）
- **static/** - 静态资源（图片、CSS、JS 等）
- **data/** - 网站数据文件
- **i18n/** - 国际化文件
- **layouts/** - 自定义模板（覆盖主题层）
- **archetypes/** - 新内容的模板文件
- **assets/** - 处理的静态资源（CSS、SCSS、JS）
- **themes/PaperMod/** - PaperMod 主题文件（Git 子模块）

## 配置文件
- **hugo.toml** - 主站点配置文件
- **config/** - 环境特定配置（如存在）
- **config/_default/** - 默认配置
- **config/production/** - 生产环境覆盖配置

## PaperMod 主题特性
- 浅色/深色模式切换
- 响应式设计
- 搜索功能（集成 Fuse.js）
- 归档和分类支持
- 社交媒体图标和分享按钮
- 个人资料模式 vs 博客模式

## 内容创建规范
文章支持 YAML 前置元数据，主要字段包括：
- `title` - 文章标题
- `date` - 发布日期
- `tags` - 标签数组
- `categories` - 分类数组
- `draft` - 草稿状态（true/false）
- `toc` - 目录显示（true/false）
- `description` - SEO 描述
- `cover.image` - 封面图片路径
- `showReadingTime` - 阅读时间显示（true/false）

## 自定义扩展点
1. **站点配置** - 修改 `hugo.toml` 参数
2. **主题样式** - 添加到 `assets/css/extended/` 目录
3. **自定义模板** - 在 `layouts/` 目录中覆盖主题层
4. **社交图标** - 在 `hugo.toml` 的 `[params.social]` 中配置
5. **导航菜单** - 在 `hugo.toml` 中使用 `[[menu.main]]` 配置