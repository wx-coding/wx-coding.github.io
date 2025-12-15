#!/usr/bin/env python3
"""
下载 Markdown 文章中的远程图片到本地，并替换 URL 为相对路径

使用方式:
    python .claude/skills/download-images/download_images.py <markdown文件路径>

示例:
    python .claude/skills/download-images/download_images.py content/posts/文章名.md
"""

import os
import re
import sys
import hashlib
import urllib.request
import urllib.error
import uuid
from pathlib import Path


def get_file_extension(url: str, content_type: str = None) -> str:
    """从 URL 或 Content-Type 获取文件扩展名"""
    # 优先从 URL 获取扩展名
    url_path = url.split('?')[0]  # 移除查询参数
    ext = os.path.splitext(url_path)[1].lower()

    if ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.bmp', '.ico']:
        return ext

    # 从 Content-Type 推断
    if content_type:
        content_type = content_type.lower()
        type_map = {
            'image/png': '.png',
            'image/jpeg': '.jpg',
            'image/gif': '.gif',
            'image/webp': '.webp',
            'image/svg+xml': '.svg',
            'image/bmp': '.bmp',
            'image/x-icon': '.ico',
        }
        for mime, extension in type_map.items():
            if mime in content_type:
                return extension

    return '.png'  # 默认扩展名


def generate_filename(url: str, index: int) -> str:
    """生成唯一的文件名"""
    # 使用 URL 的 hash 作为文件名的一部分，确保唯一性
    url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    return f"img_{index:02d}_{url_hash}"


def download_image(url: str, save_path: Path) -> bool:
    """下载图片到指定路径"""
    try:
        print(f"  下载: {url[:80]}...")

        # 创建请求，添加 User-Agent 避免被拒绝
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        request = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(request, timeout=30) as response:
            content_type = response.headers.get('Content-Type', '')
            data = response.read()

            # 获取扩展名并更新保存路径
            ext = get_file_extension(url, content_type)
            final_path = save_path.with_suffix(ext)

            # 确保目录存在
            final_path.parent.mkdir(parents=True, exist_ok=True)

            # 写入文件
            with open(final_path, 'wb') as f:
                f.write(data)

            print(f"  保存: {final_path.name}")
            return True, final_path

    except urllib.error.URLError as e:
        print(f"  失败: {e.reason}")
        return False, None
    except Exception as e:
        print(f"  错误: {e}")
        return False, None


def process_markdown(md_path: str) -> dict:
    """
    处理 Markdown 文件
    返回: {
        'success': bool,
        'downloaded': int,
        'failed': int,
        'skipped': int,
        'replacements': list
    }
    """
    md_path = Path(md_path)

    if not md_path.exists():
        print(f"错误: 文件不存在 - {md_path}")
        return {'success': False, 'error': '文件不存在'}

    if not md_path.suffix.lower() == '.md':
        print(f"错误: 不是 Markdown 文件 - {md_path}")
        return {'success': False, 'error': '不是 Markdown 文件'}

    # 读取文件内容
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配 Markdown 图片语法: ![alt](url)
    # 只匹配 http/https 开头的 URL
    pattern = r'!\[([^\]]*)\]\((https?://[^)]+)\)'
    matches = list(re.finditer(pattern, content))

    if not matches:
        print("未找到需要下载的远程图片")
        return {'success': True, 'downloaded': 0, 'failed': 0, 'skipped': 0}

    print(f"找到 {len(matches)} 个远程图片")

    # 计算保存目录
    # 使用 UUID 生成随机目录名，避免特殊字符问题
    folder_name = uuid.uuid4().hex[:12]

    # 获取项目根目录（脚本在 .claude/skills/download-images/ 下，需向上4级）
    project_root = Path(__file__).parent.parent.parent.parent
    if not (project_root / 'hugo.toml').exists():
        # 尝试使用当前工作目录
        project_root = Path.cwd()

    save_dir = project_root / 'static' / 'images' / 'posts' / folder_name
    save_dir.mkdir(parents=True, exist_ok=True)

    print(f"图片保存目录: {save_dir}")

    # 下载图片并收集替换信息
    downloaded = 0
    failed = 0
    skipped = 0
    replacements = []

    for i, match in enumerate(matches, 1):
        alt_text = match.group(1)
        url = match.group(2)
        original_text = match.group(0)

        # 生成文件名
        filename = generate_filename(url, i)
        save_path = save_dir / filename

        # 下载图片
        success, final_path = download_image(url, save_path)

        if success:
            # 构建相对路径（Hugo 中使用 /images/... 形式）
            relative_path = f"/images/posts/{folder_name}/{final_path.name}"
            new_text = f"![{alt_text}]({relative_path})"
            replacements.append((original_text, new_text))
            downloaded += 1
        else:
            failed += 1

    # 执行替换
    if replacements:
        new_content = content
        for old, new in replacements:
            new_content = new_content.replace(old, new)

        # 写回文件
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"\n完成! 成功: {downloaded}, 失败: {failed}")

    return {
        'success': True,
        'downloaded': downloaded,
        'failed': failed,
        'skipped': skipped,
        'replacements': replacements
    }


def main():
    if len(sys.argv) < 2:
        print("使用方式: python download_images.py <markdown文件路径>")
        print("示例: python download_images.py content/posts/文章名.md")
        sys.exit(1)

    md_path = sys.argv[1]
    result = process_markdown(md_path)

    if not result['success']:
        sys.exit(1)


if __name__ == '__main__':
    main()
