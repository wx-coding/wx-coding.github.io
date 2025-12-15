---
name: download-images
description: |
  下载 Hugo 博客文章中的远程图片到本地，并将 URL 替换为相对路径。

  触发场景：
  - 用户说"帮我将xxx文章的图片地址替换一下"
  - 用户说"下载xxx文章中的图片"
  - 用户说"把xxx文章的远程图片本地化"
  - 用户说"处理xxx文章的图片"
  - 用户提到需要将文章中的网络图片下载到本地

  关键词：图片下载、图片替换、图片本地化、远程图片、URL替换
---

# 下载文章图片 Skill

## 概述

这个 Skill 用于将 Hugo 博客文章中的远程图片（如来自 `cdn.nlark.com`、`imgur.com` 等）下载到本地 `static/images/posts/` 目录，并自动将文章中的远程 URL 替换为 Hugo 可识别的相对路径。

## 使用场景

- 从语雀、Notion 等平台导出的文章包含远程图片 URL
- 需要将文章中的图片资源本地化以提高访问速度
- 避免外链图片失效导致文章图片丢失

## 执行步骤

当用户请求处理文章图片时，按以下步骤执行：

### 1. 确认文章路径

如果用户只提供了文章名（如"VibeCoding实践"），在 `content/posts/` 目录下查找匹配的 `.md` 文件：

```bash
# 列出匹配的文章
ls content/posts/ | grep -i "关键词"
```

### 2. 执行 Python 脚本

使用 Skill 目录中的 `download_images.py` 脚本处理：

```bash
python .claude/skills/download-images/download_images.py "content/posts/文章名.md"
```

### 3. 报告执行结果

向用户报告：
- 找到了多少张远程图片
- 成功下载了多少张
- 图片保存到了哪个目录
- 是否有下载失败的图片

## 技术细节

### 图片保存路径规则

```
文章路径: content/posts/文章名.md
图片目录: static/images/posts/文章名/
替换后URL: /images/posts/文章名/img_01_hash.png
```

### 支持的图片格式

- PNG, JPG, JPEG, GIF, WebP, SVG, BMP, ICO

### 图片命名规则

- 格式: `img_序号_hash8位.扩展名`
- 示例: `img_01_5b086d21.png`

## 示例对话

**用户**: 帮我将 VibeCoding实践 文章的图片地址替换一下

**执行**:
1. 查找文章 → `content/posts/VibeCoding实践，Spec+Claude Code小程序开发.md`
2. 运行脚本 → `python .claude/skills/download-images/download_images.py "content/posts/VibeCoding实践，Spec+Claude Code小程序开发.md"`
3. 报告结果 → "已下载 12 张图片到 static/images/posts/VibeCoding实践，Spec+Claude Code小程序开发/"
