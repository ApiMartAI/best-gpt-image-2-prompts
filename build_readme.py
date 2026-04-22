"""
构建 README 家族：从原版 README 解析 case，结合 locales.py 里的翻译，
生成 11 种语言的画廊版 README（README.md + README_<locale>.md）。

用法：
    python3 build_readme.py
"""

import re
from pathlib import Path
from dataclasses import dataclass
from urllib.parse import quote

from locales import LOCALES, LOCALE_ORDER, LOCALE_SLUGS, readme_filename

# === 配置 ===
ROOT = Path(__file__).parent
SOURCE_README = Path("/Users/xiwu/Downloads/awesome-gpt-image-2-prompts-main/README.md")
GALLERY_COLUMNS = 4       # 画廊每行列数
THUMB_WIDTH = 200         # 缩略图宽度 (px)

# === APIMart 营销链接 ===
APIMART_BASE = "https://apimart.ai"
APIMART_DOCS = "https://docs.apimart.ai"
CHANNEL = "github-best-gpt-image-2-prompts"  # 所有外链的 sourceChannel 参数


# prompt URL 参数长度上限（字符数），控制最终 README 文件大小避免超 GitHub 渲染上限
PROMPT_URL_MAX_LEN = 1000


def _locale_path(locale: str) -> str:
    """返回 locale 对应的路径前缀段，如 'zh/'、'ja/'；英文空 slug 返回空串。"""
    slug = LOCALE_SLUGS.get(locale, "")
    return f"{slug}/" if slug else ""


def apimart_try_url(locale: str, prompt: str = "") -> str:
    """GPT-Image-2 在线试用页 URL。带 sourceChannel，prompt 非空时带 URL 编码的 prompt。
    过长的 prompt 会被截断到 PROMPT_URL_MAX_LEN，用户到页面后可继续编辑。"""
    url = f"{APIMART_BASE}/{_locale_path(locale)}model/gpt-image-2?sourceChannel={CHANNEL}"
    if prompt:
        trimmed = prompt[:PROMPT_URL_MAX_LEN]
        url += f"&prompt={quote(trimmed, safe='')}"
    return url


def apimart_marketplace_url(locale: str) -> str:
    """图像模型市场页。"""
    return f"{APIMART_BASE}/{_locale_path(locale)}model?type=image&sourceChannel={CHANNEL}"


def apimart_home_url() -> str:
    return f"{APIMART_BASE}?sourceChannel={CHANNEL}"


def apimart_docs_url() -> str:
    return f"{APIMART_DOCS}?sourceChannel={CHANNEL}"

# 原版 README 里的英文分类顺序（固定）
CATEGORIES = [
    "Portrait & Photography Cases",
    "Poster & Illustration Cases",
    "Character Design Cases",
    "UI & Social Media Mockup Cases",
    "Comparison & Community Examples",
]

# 分类对应本地化 key（在 locales 字典中）
CATEGORY_KEY = {
    "Portrait & Photography Cases": "section_portrait",
    "Poster & Illustration Cases": "section_poster",
    "Character Design Cases": "section_character",
    "UI & Social Media Mockup Cases": "section_ui",
    "Comparison & Community Examples": "section_comparison",
}

# 分类对应的 emoji，仅用于视觉区分
CATEGORY_EMOJI = {
    "Portrait & Photography Cases": "📸",
    "Poster & Illustration Cases": "🎨",
    "Character Design Cases": "🧝",
    "UI & Social Media Mockup Cases": "📱",
    "Comparison & Community Examples": "🔬",
}


# ===================== Case 解析 =====================

@dataclass
class Case:
    """单个 case 的结构化信息。"""
    category: str
    case_num: str
    title: str
    tweet_url: str
    author: str
    author_url: str
    image_path: str
    prompt: str
    anchor: str


def parse_readme(text: str) -> list[Case]:
    """从原版 README 解析所有 case。"""
    cases: list[Case] = []
    section_pattern = re.compile(r"^## (?P<cat>.+?)\s*$", re.MULTILINE)
    matches = list(section_pattern.finditer(text))
    for i, m in enumerate(matches):
        cat_name = m.group("cat").strip()
        if cat_name not in CATEGORIES:
            continue
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        cases.extend(parse_cases_in_section(cat_name, text[start:end]))
    return cases


def parse_cases_in_section(category: str, section_text: str) -> list[Case]:
    case_pattern = re.compile(
        r"^### Case (?P<num>\d+): \[(?P<title>.+?)\]\((?P<tweet>https?://[^)]+)\) \(by \[@(?P<author>[^\]]+)\]\((?P<author_url>https?://[^)]+)\)\)",
        re.MULTILINE,
    )
    results: list[Case] = []
    case_matches = list(case_pattern.finditer(section_text))
    for i, cm in enumerate(case_matches):
        cs, ce = cm.end(), (case_matches[i + 1].start() if i + 1 < len(case_matches) else len(section_text))
        body = section_text[cs:ce]
        img = re.search(r'<img\s+src="(\.\/images\/[^"]+)"', body)
        prm = re.search(r"```\s*\n(.+?)```", body, re.DOTALL)
        num, title, author = cm.group("num"), cm.group("title").strip(), cm.group("author").strip()
        results.append(Case(
            category=category, case_num=num, title=title,
            tweet_url=cm.group("tweet").strip(), author=author,
            author_url=cm.group("author_url").strip(),
            image_path=img.group(1) if img else "",
            prompt=prm.group(1).rstrip() if prm else "",
            anchor=make_anchor(category, num, title, author),
        ))
    return results


def make_anchor(category: str, num: str, title: str, author: str) -> str:
    """生成稳定的锚点 id，带分类前缀避免跨类 case 编号冲突。"""
    cat_short = category.split(" & ")[0].lower().replace(" ", "-")
    def slug(s: str) -> str:
        s = re.sub(r"[^a-z0-9\s-]", "", s.lower())
        return re.sub(r"\s+", "-", s).strip("-")
    return f"{cat_short}-case-{num}-{slug(title)}-by-{slug(author)}"


# ===================== 渲染各部分 =====================

def render_cta_badges(locale: str) -> str:
    """Hero CTA 徽章组（4 个，所有语言通用英文标签，URL 按 locale 本地化）。"""
    try_url = apimart_try_url(locale)
    models_url = apimart_marketplace_url(locale)
    docs_url = apimart_docs_url()
    home_url = apimart_home_url()
    return "\n".join([
        f"[![🚀 Try on APIMart](https://img.shields.io/badge/🚀_Try_on-APIMart-000000?style=for-the-badge)]({try_url})",
        f"[![🧩 ALL Models](https://img.shields.io/badge/🧩_ALL-Models-3a86ff?style=for-the-badge)]({models_url})",
        f"[![📘 API Docs](https://img.shields.io/badge/📘_API-Docs-06d6a0?style=for-the-badge)]({docs_url})",
        f"[![🌐 Website](https://img.shields.io/badge/🌐-apimart.ai-ffd166?style=for-the-badge)]({home_url})",
    ])


def render_language_badges(active_locale: str) -> str:
    """顶部语言切换徽章行。当前语言徽章替换成 Default 样式。"""
    lines: list[str] = []
    for loc in LOCALE_ORDER:
        cfg = LOCALES[loc]
        flag = cfg["badge_flag"]
        label = cfg["badge_label"]
        # 当前语言显示 "Current"，其他显示配置的 verb
        verb = "Current" if loc == active_locale else cfg["badge_verb"]
        color = cfg["badge_color"]
        # shields.io 的 URL 里空格用下划线
        badge_label = f"{flag}_{label}".replace(" ", "_")
        badge_verb = verb.replace(" ", "_")
        url = f"https://img.shields.io/badge/{badge_label}-{badge_verb}-{color}"
        target = readme_filename(loc)
        lines.append(f"[![{flag} {label}]({url})]({target})")
    return "\n".join(lines)


def render_gallery(cases_by_cat: dict[str, list[Case]], cfg: dict, locale: str) -> str:
    """渲染画廊区：每分类一个 table 网格。
    图片 → APIMart 试用页（带 prompt）；标题 → 站内详情锚点；作者 → 原推文。"""
    parts: list[str] = []
    cell_width = 100 // GALLERY_COLUMNS
    by_label = cfg["by_label"]
    for cat in CATEGORIES:
        cat_cases = cases_by_cat.get(cat, [])
        if not cat_cases:
            continue
        emoji = CATEGORY_EMOJI.get(cat, "")
        cat_label = cfg[CATEGORY_KEY[cat]]
        parts.append(f"### {emoji} {cat_label}\n")
        parts.append("<table>")
        for i in range(0, len(cat_cases), GALLERY_COLUMNS):
            row = cat_cases[i : i + GALLERY_COLUMNS]
            parts.append("  <tr>")
            for c in row:
                try_url = apimart_try_url(locale, c.prompt)
                cell = (
                    f'    <td align="center" width="{cell_width}%" valign="top">'
                    f'<a href="{try_url}" target="_blank" rel="noopener">'
                    f'<img src="{c.image_path}" width="{THUMB_WIDTH}" alt="{c.title}">'
                    f'</a><br>'
                    f'<a href="#{c.anchor}"><sub><b>Case {c.case_num}: {c.title}</b></sub></a><br>'
                    f'<sub>{by_label} <a href="{c.author_url}">@{c.author}</a></sub>'
                    f'</td>'
                )
                parts.append(cell)
            for _ in range(GALLERY_COLUMNS - len(row)):
                parts.append(f'    <td width="{cell_width}%"></td>')
            parts.append("  </tr>")
        parts.append("</table>\n")
    return "\n".join(parts)


def render_details(cases_by_cat: dict[str, list[Case]], cfg: dict, locale: str) -> str:
    """渲染详情区。大图同样链接到 APIMart 试用页（带 prompt）。"""
    parts: list[str] = []
    output_label, output_alt, prompt_label = cfg["output_label"], cfg["output_alt"], cfg["prompt_label"]
    by_label = cfg["by_label"]
    for cat in CATEGORIES:
        cat_cases = cases_by_cat.get(cat, [])
        if not cat_cases:
            continue
        emoji = CATEGORY_EMOJI.get(cat, "")
        parts.append(f"## {emoji} {cfg[CATEGORY_KEY[cat]]}\n")
        for c in cat_cases:
            try_url = apimart_try_url(locale, c.prompt)
            parts.append(f'<a id="{c.anchor}"></a>')
            parts.append(
                f"### Case {c.case_num}: [{c.title}]({c.tweet_url}) "
                f"({by_label} [@{c.author}]({c.author_url}))\n"
            )
            parts.append(f"| {output_label} |")
            parts.append("| :----: |")
            parts.append(
                f'| <a href="{try_url}" target="_blank" rel="noopener">'
                f'<img src="{c.image_path}" width="480" alt="{output_alt}">'
                f'</a> |\n'
            )
            parts.append(f"**{prompt_label}:**\n")
            parts.append("```")
            parts.append(c.prompt)
            parts.append("```\n")
        parts.append("")
    return "\n".join(parts)


def build_one(locale: str, cases_by_cat: dict[str, list[Case]], total: int) -> str:
    """生成某个 locale 的完整 README 文本。"""
    cfg = LOCALES[locale]
    cats = len([c for c in CATEGORIES if cases_by_cat.get(c)])

    lang_badges = render_language_badges(locale)
    cta_badges = render_cta_badges(locale)

    # 封面点击 → 图像模型市场页
    cover_url = apimart_marketplace_url(locale)
    # 首屏主 CTA → GPT-Image-2 试用页（不带 prompt，让用户自己输入）
    hero_try_url = apimart_try_url(locale)

    header = f"""<div align="center">

<a href="{cover_url}" target="_blank" rel="noopener"><img src="./images/cover.svg" alt="best-gpt-image-2-prompts" width="100%"></a>

{cta_badges}

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
![Cases](https://img.shields.io/badge/Cases-{total}-ef476f)
![Categories](https://img.shields.io/badge/Categories-{cats}-118ab2)

{lang_badges}

**{cfg["tagline"]}**

</div>

## {cfg["intro_heading"]}

{cfg["intro_body"]}

{cfg["intro_hint"]}

> [!TIP]
> {cfg["note_title"]} — {cfg["apimart_pitch"]}
>
> {cfg["note_body"]} **[{cfg["note_cta"]}]({hero_try_url})**

{cfg["intro_note"]}

## {cfg["news_heading"]}

"""
    news_block = "\n".join(item.format(total=total, cats=cats) for item in cfg["news_items"]) + "\n"

    gallery_section = f"""
## {cfg["gallery_heading"]}

{cfg["gallery_tip"]}

"""

    gallery = render_gallery(cases_by_cat, cfg, locale)
    details_header = f"## {cfg['prompts_heading']}\n"
    details = render_details(cases_by_cat, cfg, locale)

    # 底部 Footer CTA：大字标题 + 主 CTA + 两个副链接
    footer_cta = f"""
---

<div align="center">

### {cfg["footer_heading"]}

{cfg["apimart_pitch"]}

**[{cfg["footer_cta"]}]({hero_try_url})**

[{cfg["footer_link_models"]}]({apimart_marketplace_url(locale)}) · [{cfg["footer_link_docs"]}]({apimart_docs_url()})

</div>

"""

    tail = f"""## {cfg["ack_heading"]}

{cfg["ack_body"]}

## {cfg["license_heading"]}

{cfg["license_body"]}
"""
    return "".join([header, news_block, gallery_section, gallery, "\n---\n\n", details_header, details, footer_cta, tail])


def build_all(cases: list[Case]) -> dict[str, str]:
    """对每个 locale 生成 README 文本，返回 {locale: content}。"""
    # 分组 + 内部按 case_num 数字排序
    cases_by_cat: dict[str, list[Case]] = {c: [] for c in CATEGORIES}
    for c in cases:
        cases_by_cat.setdefault(c.category, []).append(c)
    for cat in cases_by_cat:
        cases_by_cat[cat].sort(key=lambda c: int(c.case_num))

    total = sum(len(v) for v in cases_by_cat.values())
    return {loc: build_one(loc, cases_by_cat, total) for loc in LOCALE_ORDER}


def main():
    text = SOURCE_README.read_text(encoding="utf-8")
    cases = parse_readme(text)

    by_cat: dict[str, int] = {}
    for c in cases:
        by_cat[c.category] = by_cat.get(c.category, 0) + 1
    print(f"共解析 {len(cases)} 个 case：")
    for cat in CATEGORIES:
        print(f"  - {cat}: {by_cat.get(cat, 0)}")

    outputs = build_all(cases)
    for loc, content in outputs.items():
        path = ROOT / readme_filename(loc)
        path.write_text(content, encoding="utf-8")
        print(f"  ✓ {path.name} ({len(content):,} chars)")

    print(f"\n生成完毕，共 {len(outputs)} 份 README。")


if __name__ == "__main__":
    main()
