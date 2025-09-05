# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

此文件为 Claude Code (claude.ai/code) 提供在操作此代码仓库时的指导信息。

## 项目概述
这是一个使用 PaperMod 主题的 Hugo 静态网站项目。项目结构遵循标准 Hugo 规范，并通过 PaperMod 主题进行了定制。

### 部署架构
- **Hugo 版本**: 0.146.0 (在 GitHub Actions 中指定)
- **主题**: PaperMod 主题作为 Git 子模块集成 (`themes/PaperMod/`)
- **自动部署**: 通过 GitHub Actions (`.github/workflows/hugo.yml`) 自动部署到 GitHub Pages
- **部署触发**: 推送到 `main` 分支自动触发部署

## 核心开发命令

### Hugo 基础命令
- `hugo server` - 启动本地开发服务器，实时重载，访问 localhost:1313
- `hugo server -D` - 开发模式包含草稿文章
- `hugo` - 构建静态站点到 `public/` 目录
- `hugo --minify` - 生产环境构建，包含代码压缩
- `hugo new posts/文章标题.md` - 在 content/posts/ 创建新博客文章
- `hugo new 页面标题.md` - 创建新的独立页面
- **项目记忆**：每次操作完成后，**不要自动启动项目**，**不要执行 `hugo server -D`**

### Git 子模块管理
- **主题更新**: `git submodule update --remote themes/PaperMod` - 更新 PaperMod 主题到最新版本
- **初始化子模块**: `git submodule update --init --recursive` - 克隆项目后初始化子模块
- **检查子模块状态**: `git submodule status` - 查看当前子模块状态

### 项目目录结构
- **content/** - 网站内容（文章、页面等）
- **static/** - 静态资源（图片、CSS、JS 等）
- **data/** - 网站数据文件
- **i18n/** - 国际化文件
- **layouts/** - 自定义模板（覆盖主题层）
- **archetypes/** - 新内容的模板文件
- **assets/** - 处理的静态资源（CSS、SCSS、JS）
- **themes/PaperMod/** - PaperMod 主题文件（Git 子模块）
- **static/images/** - 图片目录，图片目录和**content**目录层级一致

## 配置文件
- **hugo.toml** - 主站点配置文件
  - 使用中文 (`zh-CN`) 作为主要语言
  - 配置了代码高亮 (`github` 风格)
  - 启用代码复制按钮和 TOC (目录)
- **config/** - 环境特定配置（如存在）
- **config/_default/** - 默认配置
- **config/production/** - 生产环境覆盖配置

## 自定义架构
- **layouts/index.html** - 自定义首页布局，包含个人介绍页面样式
- **archetypes/default.md** - 新内容创建模板，默认为草稿状态
- **static/images/** - 图片资源目录，结构与 content 目录层级一致

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

## 部署流程
项目使用 GitHub Actions 自动部署，无需手动构建：
1. 推送代码到 `main` 分支自动触发构建
2. GitHub Actions 使用 Hugo 0.146.0 Extended 版本构建
3. 构建过程包含 `--gc --minify` 优化
4. 自动部署到 GitHub Pages
5. 支持 Dart Sass 和 Node.js 依赖处理

## 重要注意事项
- PaperMod 主题是 Git 子模块，更新时需要使用子模块命令
- 首页使用自定义布局 (`layouts/index.html`) 显示个人介绍
- 图片资源放在 `static/images/` 目录，路径结构与内容目录对应
- 所有新创建的内容默认为草稿状态，需要设置 `draft: false` 才会显示