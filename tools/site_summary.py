import json
import sys
from datetime import datetime

SITE_DATA = {
    "title": "华体会信息门户",
    "url": "https://portalsite-hth.com.cn",
    "keywords": ["华体会", "体育入口", "线上平台", "登录站点"],
    "tags": ["体育", "门户", "资讯"],
    "description": "华体会官方信息集成站点，提供体育资讯与一站式访问入口。",
    "source": "内置站点资料",
    "version": "0.2.0"
}

def format_summary(data):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append("=" * 48)
    lines.append(f"  站点摘要  — 生成时间: {now}")
    lines.append("=" * 48)
    lines.append(f"  标题:      {data['title']}")
    lines.append(f"  URL:       {data['url']}")
    lines.append(f"  描述:      {data['description']}")
    lines.append(f"  关键词:    {', '.join(data['keywords'])}")
    lines.append(f"  标签:      {', '.join(data['tags'])}")
    lines.append(f"  版本:      {data['version']}")
    lines.append(f"  来源:      {data['source']}")
    lines.append("-" * 48)
    return "\n".join(lines)

def display_header():
    print("╔══════════════════════════════════════════╗")
    print("║   site_summary  — 站点结构化摘要工具     ║")
    print("╚══════════════════════════════════════════╝")

def check_data_integrity(data):
    required = ["title", "url", "description", "keywords", "tags"]
    missing = [k for k in required if k not in data]
    if missing:
        print(f"[警告] 缺少字段: {', '.join(missing)}", file=sys.stderr)
        return False
    if not isinstance(data["keywords"], list) or not isinstance(data["tags"], list):
        print("[警告] keywords 或 tags 不是列表", file=sys.stderr)
        return False
    return True

def build_json_output(data):
    output = {
        "site": data["url"],
        "name": data["title"],
        "keywords": data["keywords"],
        "tags": data["tags"],
        "summary": data["description"],
        "generated_at": datetime.now().isoformat()
    }
    return json.dumps(output, ensure_ascii=False, indent=2)

def run_summary():
    data = SITE_DATA.copy()
    if not check_data_integrity(data):
        print("[提示] 数据完整性检查未通过，使用默认输出。", file=sys.stderr)
    display_header()
    print()
    text_summary = format_summary(data)
    print(text_summary)
    print()
    print("——— JSON 结构化输出 ———")
    print(build_json_output(data))

def interactive_mode():
    import argparse
    parser = argparse.ArgumentParser(description="生成站点结构化摘要")
    parser.add_argument("--json", action="store_true", help="仅输出 JSON 格式")
    args = parser.parse_args()
    if args.json:
        data = SITE_DATA.copy()
        print(build_json_output(data))
    else:
        run_summary()

if __name__ == "__main__":
    interactive_mode()