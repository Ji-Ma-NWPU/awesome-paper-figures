"""Generate README.md, papers/*.md and gallery/*.md from papers.yaml."""

from pathlib import Path

import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent

TYPES = {
    "teaser": "Teaser / 概念示意图",
    "framework": "方法框架图 / Pipeline",
    "plot": "实验结果图",
    "visualization": "可视化 / 定性结果",
    "table": "表格",
}

TLDR = {"motivation": "动机", "method": "方法", "result": "效果"}

GRID_COLS = 3
MAX_WIDTH = 800
SMALL = 420  # figures at most this wide are shown two per row


def paper_links(p):
    links = [f"[Paper]({p['paper']})"]
    if p.get("code"):
        links.append(f"[Code]({p['code']})")
    return " · ".join(links)


def short(p):
    return p.get("short") or p["title"]


def fig_anchor(fig):
    return fig["caption"].lower().replace(" ", "-")


def load():
    data = yaml.safe_load((ROOT / "papers.yaml").read_text(encoding="utf-8")) or {}
    papers = sorted(data.get("papers") or [], key=lambda p: str(p.get("added", "")), reverse=True)
    for p in papers:
        for fig in p.get("figures") or []:
            if fig.get("type") not in TYPES:
                raise SystemExit(f"{p['id']}: unknown figure type {fig.get('type')!r}")
            if fig.get("file") and not (ROOT / "figures" / p["id"] / fig["file"]).exists():
                raise SystemExit(f"{p['id']}: missing figures/{p['id']}/{fig['file']}")
    return papers


def write(path, lines):
    path.parent.mkdir(exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_paper_page(p):
    out = [f"# {p['title']}\n", "[← 返回目录](../README.md)\n"]
    out.append(f"- **作者**：{p.get('authors', '')}")
    out.append(f"- **发表**：{p.get('venue', '')}")
    out.append(f"- **链接**：{paper_links(p)}")
    out.append(f"- **收录日期**：{p.get('added', '')}\n")
    tldr = [(label, p[key]) for key, label in TLDR.items() if p.get(key)]
    if tldr:
        out.append("## TL;DR\n")
        out += [f"- **{label}**：{text}" for label, text in tldr]
        out.append("")
    out.append("## Figures\n")
    figs = p.get("figures") or []
    i = 0
    while i < len(figs):
        fig = figs[i]
        nxt = figs[i + 1] if i + 1 < len(figs) else None
        if nxt and display_width(p, fig) <= SMALL and display_width(p, nxt) <= SMALL:
            out.append('<table><tr>')
            out += [f'<td width="50%" valign="top">{fig_html(p, f)}</td>' for f in (fig, nxt)]
            out.append('</tr></table>\n')
            i += 2
        else:
            out.append(fig_html(p, fig) + "\n")
            i += 1
    write(ROOT / "papers" / f"{p['id']}.md", out)


def display_width(p, fig):
    """Show figures at their natural size (crops are 200 dpi) instead of stretching small ones."""
    if not fig.get("file"):
        return MAX_WIDTH
    with Image.open(ROOT / "figures" / p["id"] / fig["file"]) as im:
        return min(MAX_WIDTH, round(im.width * 0.6))


def fig_html(p, fig):
    label = TYPES[fig["type"]]
    parts = [f'<a id="{fig_anchor(fig)}"></a><b>{fig["caption"]}</b> · '
             f'<a href="../gallery/{fig["type"]}.md">{label}</a><br>']
    if fig.get("file"):
        parts.append(f'<img src="../figures/{p["id"]}/{fig["file"]}" width="{display_width(p, fig)}"><br>')
    else:
        parts.append("📷 <i>截图待补</i><br>")
    if fig.get("comment"):
        parts.append(f"💡 {fig['comment']}")
    return "".join(parts)


def build_gallery_page(t, items):
    out = [f"# {TYPES[t]}\n", f"[← 返回目录](../README.md) · 共 {len(items)} 张\n"]
    if not items:
        out.append("_暂无_")
    else:
        out.append("| " + " | ".join([" "] * GRID_COLS) + " |")
        out.append("|" + "---|" * GRID_COLS)
        for i in range(0, len(items), GRID_COLS):
            cells = []
            for p, fig in items[i:i + GRID_COLS]:
                link = f"../papers/{p['id']}.md#{fig_anchor(fig)}"
                img = (f'<img src="../figures/{p["id"]}/{fig["file"]}" width="260">'
                       if fig.get("file") else "📷 待补")
                cells.append(f"[{img}]({link})<br>**{short(p)}** · {fig['caption']}")
            cells += [" "] * (GRID_COLS - len(cells))
            out.append("| " + " | ".join(cells) + " |")
    write(ROOT / "gallery" / f"{t}.md", out)


def build_readme(papers, by_type):
    n_figs = sum(map(len, by_type.values()))
    out = [
        "# Awesome Paper Figures\n",
        "个人收藏：图画得好的论文，方便画图时找参考。\n",
        "- 数据源：[`papers.yaml`](papers.yaml)，图片存放在 `figures/<paper-id>/`",
        "- 修改后运行 `python3 scripts/build_readme.py` 重新生成 README、论文页和画廊页（依赖 `pyyaml`、`pillow`；请勿手动编辑生成的文件）\n",
        f"共收录 **{len(papers)}** 篇论文，**{n_figs}** 张图。\n",
        "## 按图类型浏览\n",
    ]
    out.append(" · ".join(f"[{label}](gallery/{t}.md) ({len(by_type[t])})" for t, label in TYPES.items()))
    out.append("\n## 按论文浏览\n")
    out.append("| 预览 | 论文 | 发表 | 图 | 链接 |")
    out.append("|---|---|---|---|---|")
    for p in papers:
        first = next((f for f in p.get("figures") or [] if f.get("file")), None)
        thumb = f'<img src="figures/{p["id"]}/{first["file"]}" width="200">' if first else ""
        out.append(
            f"| {thumb} | [{p['title'].replace('|', '&#124;')}](papers/{p['id']}.md) | {p.get('venue', '')} "
            f"| {len(p.get('figures') or [])} | {paper_links(p)} |"
        )
    write(ROOT / "README.md", out)


def main():
    papers = load()
    by_type = {t: [] for t in TYPES}
    for p in papers:
        for fig in p.get("figures") or []:
            by_type[fig["type"]].append((p, fig))

    for d in ("papers", "gallery"):
        for old in (ROOT / d).glob("*.md"):
            old.unlink()
    for p in papers:
        build_paper_page(p)
    for t, items in by_type.items():
        build_gallery_page(t, items)
    build_readme(papers, by_type)
    print(f"Generated README, {len(papers)} paper pages, {len(TYPES)} gallery pages")


if __name__ == "__main__":
    main()
