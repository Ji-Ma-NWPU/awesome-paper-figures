"""Generate README.md from papers.yaml."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

TYPES = {
    "teaser": "Teaser / Figure 1",
    "framework": "方法框架图 / Pipeline",
    "concept": "概念示意图 / Motivation",
    "plot": "实验结果图",
    "visualization": "可视化 / 定性结果",
    "table": "表格",
}

HEADER = """# Awesome Paper Figures

个人收藏：图画得好的论文，方便画图时找参考。

- 数据源：[`papers.yaml`](papers.yaml)，图片存放在 `figures/<paper-id>/`
- 修改后运行 `python3 scripts/build_readme.py` 重新生成本文件（请勿手动编辑 README）

"""


def anchor(text):
    return "".join(c for c in text.lower().replace(" ", "-") if c.isalnum() or c in "-_")


def paper_link(p):
    links = [f"[Paper]({p['paper']})"]
    if p.get("code"):
        links.append(f"[Code]({p['code']})")
    return " · ".join(links)


def main():
    data = yaml.safe_load((ROOT / "papers.yaml").read_text(encoding="utf-8")) or {}
    papers = data.get("papers") or []

    by_type = {t: [] for t in TYPES}
    for p in papers:
        for fig in p.get("figures") or []:
            t = fig.get("type")
            if t not in TYPES:
                raise SystemExit(f"{p['id']}: unknown figure type {t!r}")
            if fig.get("file") and not (ROOT / "figures" / p["id"] / fig["file"]).exists():
                raise SystemExit(f"{p['id']}: missing figures/{p['id']}/{fig['file']}")
            by_type[t].append((p, fig))

    out = [HEADER, f"共收录 **{len(papers)}** 篇论文，**{sum(map(len, by_type.values()))}** 张图。\n"]

    out.append("## 目录\n")
    out.append("- [按论文浏览](#按论文浏览)")
    for t, label in TYPES.items():
        out.append(f"- [{label}](#{anchor(label)}) ({len(by_type[t])})")
    out.append("")

    out.append("## 按论文浏览\n")
    out.append("| 论文 | 作者 | 发表 | 链接 | 收录日期 |")
    out.append("|---|---|---|---|---|")
    for p in sorted(papers, key=lambda p: str(p.get("added", "")), reverse=True):
        out.append(
            f"| {p['title']} | {p.get('authors', '')} | {p.get('venue', '')} "
            f"| {paper_link(p)} | {p.get('added', '')} |"
        )
    out.append("")

    for t, label in TYPES.items():
        out.append(f"## {label}\n")
        if not by_type[t]:
            out.append("_暂无_\n")
            continue
        for p, fig in by_type[t]:
            out.append(f"### {p['title']} — {fig.get('caption', '')}\n")
            out.append(f"*{p.get('venue', '')}* · {paper_link(p)}\n")
            if fig.get("file"):
                out.append(f'<img src="figures/{p["id"]}/{fig["file"]}" width="800">\n')
            else:
                out.append("📷 _截图待补_\n")
            if fig.get("comment"):
                out.append(f"> 💡 {fig['comment']}\n")

    (ROOT / "README.md").write_text("\n".join(out), encoding="utf-8")
    print(f"README.md updated: {len(papers)} papers")


if __name__ == "__main__":
    main()
