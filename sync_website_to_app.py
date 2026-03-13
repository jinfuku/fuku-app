#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网站和APP内容同步工具
自动从网站内容生成APP的文章列表
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

# 配置
WEBSITE_DIR = Path(__file__).parent.parent / "fuku-psychology-website"
APP_DIR = Path(__file__).parent
SYNC_REPORT_FILE = APP_DIR / "sync_report.md"

# 网站基础URL
WEBSITE_BASE_URL = "https://jinfuku.github.io/fukuxinli"

# 分类映射
CATEGORY_MAP = {
    "身": "body",
    "心": "mind",
    "神": "spirit",
    "伴侣关系": "relationship",
    "AI": "ai"
}

def extract_articles_from_content():
    """从网站content目录提取文章信息"""
    articles = []
    content_dir = WEBSITE_DIR / "content"
    
    if not content_dir.exists():
        print(f"警告：content目录不存在: {content_dir}")
        return articles
    
    # 遍历所有分类目录
    for category_dir in content_dir.iterdir():
        if not category_dir.is_dir():
            continue
        
        category_name = category_dir.name
        # 映射分类名称
        chinese_category = None
        for cn, en in CATEGORY_MAP.items():
            if en == category_name:
                chinese_category = cn
                break
        
        if not chinese_category:
            continue
        
        # 遍历分类下的所有markdown文件
        for md_file in category_dir.glob("*.md"):
            article_info = parse_markdown_article(md_file, chinese_category, category_name)
            if article_info:
                articles.append(article_info)
    
    return articles

def parse_markdown_article(md_file, chinese_category, category_dir):
    """解析markdown文件，提取文章信息"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取front matter
        front_matter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not front_matter_match:
            return None
        
        front_matter = front_matter_match.group(1)
        
        # 提取标题
        title_match = re.search(r'title:\s*[\'"](.+?)[\'"]', front_matter)
        title = title_match.group(1) if title_match else md_file.stem
        
        # 提取日期
        date_match = re.search(r'date:\s*(.+)', front_matter)
        date = date_match.group(1).strip() if date_match else "2024-01-01"
        
        # 提取密码（付费文章）
        password_match = re.search(r'password:\s*[\'"](.+?)[\'"]', front_matter)
        is_premium = password_match is not None
        password = password_match.group(1) if password_match else None
        
        # 生成URL
        # 对于付费文章，使用content目录下的md文件
        # 对于免费文章，使用生成的HTML目录
        if is_premium:
            # 付费文章链接到md文件
            relative_path = md_file.relative_to(WEBSITE_DIR)
            url = f"{WEBSITE_BASE_URL}/{relative_path.as_posix()}"
        else:
            # 免费文章使用标题编码的URL
            # 需要找到对应的HTML目录
            html_dir = WEBSITE_DIR / category_dir / md_file.stem
            if html_dir.exists() and (html_dir / "index.html").exists():
                url = f"{WEBSITE_BASE_URL}/{category_dir}/{md_file.stem}/"
            else:
                # 如果HTML目录不存在，使用md文件
                relative_path = md_file.relative_to(WEBSITE_DIR)
                url = f"{WEBSITE_BASE_URL}/{relative_path.as_posix()}"
        
        # 提取摘要（第一段内容）
        body_content = re.sub(r'^---.*?---', '', content, flags=re.DOTALL).strip()
        # 提取第一段
        first_para_match = re.search(r'## (.+?)(?:\n|$)', body_content)
        summary = ""
        if first_para_match:
            summary = first_para_match.group(1).strip()
        else:
            # 如果没有二级标题，提取第一段文本
            lines = [line.strip() for line in body_content.split('\n') if line.strip() and not line.startswith('#')]
            if lines:
                summary = lines[0][:100]  # 限制摘要长度
        
        return {
            "id": generate_article_id(),
            "title": title,
            "category": chinese_category,
            "summary": summary + "..." if len(summary) > 80 else summary,
            "date": date,
            "isPremium": is_premium,
            "url": url,
            "password": password if is_premium else None
        }
    except Exception as e:
        print(f"解析文件失败 {md_file}: {e}")
        return None

def generate_article_id():
    """生成文章ID（简单实现）"""
    return int(datetime.now().timestamp())

def generate_app_html(articles):
    """生成APP的HTML文件"""
    # 按日期排序
    sorted_articles = sorted(articles, key=lambda x: x['date'], reverse=True)
    
    # 读取APP模板
    app_template_path = APP_DIR / "index.html"
    with open(app_template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 生成文章数组的JavaScript代码
    articles_js = "        const articles = [\n"
    for article in sorted_articles:
        articles_js += f"            {{\n"
        articles_js += f"                id: {article['id']},\n"
        articles_js += f"                title: '{escape_js_string(article['title'])}',\n"
        articles_js += f"                category: '{article['category']}',\n"
        articles_js += f"                summary: '{escape_js_string(article['summary'])}',\n"
        articles_js += f"                date: '{article['date']}',\n"
        articles_js += f"                isPremium: {str(article['isPremium']).lower()},\n"
        articles_js += f"                url: '{article['url']}'\n"
        if article['password']:
            articles_js += f"                price: '199元'\n"
        articles_js += f"            }},\n"
    articles_js += "        ];"
    
    # 替换模板中的文章数组
    new_template = re.sub(
        r'// 文章数据\s*const articles = \[.*?\];',
        articles_js,
        template,
        flags=re.DOTALL
    )
    
    # 写入新的APP HTML文件
    output_path = APP_DIR / "index-synced.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_template)
    
    return output_path

def escape_js_string(s):
    """转义JavaScript字符串"""
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('"', '\\"').replace('\n', '\\n')

def generate_sync_report(articles):
    """生成同步报告"""
    report = f"""# 网站和APP内容同步报告

生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 同步统计

- 总文章数: {len(articles)}
- 免费文章: {len([a for a in articles if not a['isPremium']])}
- 付费文章: {len([a for a in articles if a['isPremium']])}

## 文章列表

| ID | 标题 | 分类 | 日期 | 类型 | URL |
|----|------|------|------|------|-----|
"""
    for article in articles:
        article_type = "🔒 付费" if article['isPremium'] else "✅ 免费"
        report += f"| {article['id']} | {article['title']} | {article['category']} | {article['date']} | {article_type} | [查看]({article['url']}) |\n"
    
    return report

def main():
    """主函数"""
    print("=" * 60)
    print("网站和APP内容同步工具")
    print("=" * 60)
    print()
    
    # 提取文章
    print("正在从网站提取文章...")
    articles = extract_articles_from_content()
    print(f"找到 {len(articles)} 篇文章")
    print()
    
    # 生成APP HTML
    print("正在生成APP HTML文件...")
    app_html_path = generate_app_html(articles)
    print(f"已生成: {app_html_path}")
    print()
    
    # 生成同步报告
    print("正在生成同步报告...")
    report = generate_sync_report(articles)
    with open(SYNC_REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"已生成: {SYNC_REPORT_FILE}")
    print()
    
    print("=" * 60)
    print("同步完成!")
    print("=" * 60)
    print()
    print("下一步操作:")
    print("1. 检查生成的同步报告")
    print("2. 用生成的 index-synced.html 替换原有的 index.html")
    print("3. 提交更改到Git仓库")
    print()

if __name__ == "__main__":
    main()
