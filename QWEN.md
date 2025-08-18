# Qwen Context for wx-coding.github.io

## 项目概述

这是一个使用 [Hugo](https://gohugo.io/) 静态网站生成器构建的个人博客网站。该网站托管在 GitHub Pages 上。

*   **网站名称**: wx-coding
*   **主题**: PaperMod (一个快速、简洁、响应式的 Hugo 主题)
*   **主要技术**: Hugo, Markdown, HTML/CSS/JavaScript (通过主题)
*   **内容类型**: 技术分享、个人介绍、博客文章。
*   **默认语言**: 中文 (zh-CN)。

网站结构遵循标准的 Hugo 项目布局。

## 重要文件和目录

*   `hugo.toml`: 网站的主要配置文件，定义了标题、主题、菜单、分页、多语言等设置。
*   `content/`:
    *   `about.md`: 关于页面的内容，包含个人信息、技术栈、项目经验和联系方式。
    *   `posts/`: 存放博客文章的目录。示例文章 `my-first-post.md` 已存在。
*   `themes/`: 存放 Hugo 主题。当前使用的是 `PaperMod` 主题。
*   `archetypes/`: Hugo 内容模板。`default.md` 定义了新文章的默认 front matter。
*   `static/`: 存放静态文件，如 `favicon.ico`。
*   `layouts/`: (当前为空) 可用于存放自定义布局模板，覆盖主题默认模板。
*   `public/`: Hugo 构建后生成的静态网站文件存放在此目录。

## 构建和运行

*   **启动本地开发服务器**:
    ```bash
    hugo server -D
    ```
    此命令会在本地启动一个开发服务器（通常在 `http://localhost:1313`），并实时重新加载页面以方便预览。`-D` 参数用于包含草稿文章。

*   **构建静态网站**:
    ```bash
    hugo
    ```
    此命令会根据 `hugo.toml` 中的配置，将 `content/` 目录中的 Markdown 文件等内容，结合 `themes/` 中的主题，生成静态 HTML 文件，并输出到 `public/` 目录。

## 开发约定

*   **内容创建**:
    *   博客文章应创建在 `content/posts/` 目录下，使用 Markdown 格式。
    *   可以使用 `hugo new posts/your-post-name.md` 命令来创建新文章，它会自动使用 `archetypes/default.md` 模板。
    *   文章文件的 front matter (如 `date`, `draft`, `title`) 应根据需要进行调整。
*   **配置**:
    *   主要配置集中在 `hugo.toml` 文件中。
*   **主题**:
    *   当前使用 `PaperMod` 主题。有关主题的配置和自定义选项，请参考 [PaperMod 主题文档](https://github.com/adityatelange/hugo-PaperMod)。
    *   自定义布局或覆盖主题默认行为时，应在 `layouts/` 目录下创建相应的模板文件。
*   **静态文件**:
    *   所有需要直接访问的静态资源（如图片、图标、CSS/JS 文件）应放在 `static/` 目录下。它们在构建后的网站中会相对于网站根目录进行访问。