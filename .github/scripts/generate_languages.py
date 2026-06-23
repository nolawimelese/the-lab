import requests
import sys

REPO = "nolawimelese/the-lab"
OUTPUT = ".github/assets/languages.svg"

LANG_COLORS = {
    "Python":            "#3572A5",
    "TypeScript":        "#3178c6",
    "JavaScript":        "#f1e05a",
    "HTML":              "#e34c26",
    "CSS":               "#563d7c",
    "SCSS":              "#c6538c",
    "Shell":             "#89e051",
    "Jupyter Notebook":  "#DA5B0B",
    "Markdown":          "#083fa1",
    "JSON":              "#292929",
    "YAML":              "#cb171e",
    "Dockerfile":        "#384d54",
    "R":                 "#198CE7",
    "SQL":               "#e38c00",
    "C":                 "#555555",
    "C++":               "#f34b7d",
    "Java":              "#b07219",
    "Rust":              "#dea584",
    "Go":                "#00ADD8",
    "Ruby":              "#701516",
    "Vue":               "#41b883",
    "Svelte":            "#ff3e00",
}

FALLBACK_PALETTE = [
    "#8b5cf6","#06b6d4","#10b981","#f59e0b",
    "#ef4444","#ec4899","#a78bfa","#34d399",
]

EXT_MAP = {
    ".py": "Python", ".pyw": "Python",
    ".ts": "TypeScript", ".tsx": "TypeScript",
    ".js": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript", ".jsx": "JavaScript",
    ".html": "HTML", ".htm": "HTML",
    ".css": "CSS", ".scss": "SCSS", ".sass": "SCSS", ".less": "CSS",
    ".sh": "Shell", ".bash": "Shell", ".zsh": "Shell",
    ".ipynb": "Jupyter Notebook",
    ".md": "Markdown", ".mdx": "Markdown",
    ".json": "JSON",
    ".yaml": "YAML", ".yml": "YAML",
    ".r": "R", ".rmd": "R",
    ".sql": "SQL",
    ".c": "C", ".h": "C",
    ".cpp": "C++", ".cc": "C++", ".cxx": "C++", ".hpp": "C++",
    ".java": "Java",
    ".rs": "Rust",
    ".go": "Go",
    ".rb": "Ruby",
    ".vue": "Vue",
    ".svelte": "Svelte",
    ".toml": "TOML",
}


def get_color(lang, idx):
    return LANG_COLORS.get(lang, FALLBACK_PALETTE[idx % len(FALLBACK_PALETTE)])


def format_bytes(b):
    if b >= 1_000_000:
        return f"{b/1_000_000:.2f} MB"
    if b >= 1_000:
        return f"{b/1_000:.1f} KB"
    return f"{b} B"


def count_files(tree):
    counts = {}
    for item in tree:
        if item["type"] != "blob":
            continue
        fname = item["path"].split("/")[-1].lower()
        if fname == "dockerfile":
            counts["Dockerfile"] = counts.get("Dockerfile", 0) + 1
            continue
        ext = "." + fname.rsplit(".", 1)[-1] if "." in fname else None
        if ext:
            lang = EXT_MAP.get(ext)
            if lang:
                counts[lang] = counts.get(lang, 0) + 1
    return counts


def build_svg(langs, file_counts):
    total = sum(langs.values())
    entries = sorted(langs.items(), key=lambda x: -x[1])
    entries = [
        {
            "name": name,
            "bytes": b,
            "pct": b / total * 100,
            "color": get_color(name, i),
            "files": file_counts.get(name, 0),
        }
        for i, (name, b) in enumerate(entries)
    ]

    W = 560
    PAD = 28
    BAR_W = W - PAD * 2
    BAR_Y = 60
    BAR_H = 12
    COLS = 2
    ENTRY_H = 46
    ENTRY_START_Y = 102
    ROWS = -(-len(entries) // COLS)  # ceil div
    TOTAL_H = ENTRY_START_Y + ROWS * ENTRY_H + 20

    # stacked bar segments
    bar_x = PAD
    segments = []
    for e in entries:
        w = max((e["bytes"] / total) * BAR_W, 2)
        segments.append({**e, "x": bar_x, "w": w})
        bar_x += w + 2

    seg_els = []
    for i, s in enumerate(segments):
        first, last = i == 0, i == len(segments) - 1
        if first and last:
            rx = 6
        elif first or last:
            rx = 6
        else:
            rx = 0

        if first and not last:
            seg_els.append(
                f'<rect x="{s["x"]}" y="{BAR_Y}" width="{s["w"]}" height="{BAR_H}" rx="{rx}" fill="{s["color"]}"/>'
                f'<rect x="{s["x"] + s["w"] - 6}" y="{BAR_Y}" width="6" height="{BAR_H}" fill="{s["color"]}"/>'
            )
        elif last and not first:
            seg_els.append(
                f'<rect x="{s["x"]}" y="{BAR_Y}" width="{s["w"]}" height="{BAR_H}" rx="{rx}" fill="{s["color"]}"/>'
                f'<rect x="{s["x"]}" y="{BAR_Y}" width="6" height="{BAR_H}" fill="{s["color"]}"/>'
            )
        else:
            seg_els.append(
                f'<rect x="{s["x"]}" y="{BAR_Y}" width="{s["w"]}" height="{BAR_H}" rx="{rx}" fill="{s["color"]}"/>'
            )

    entry_els = []
    for i, e in enumerate(entries):
        col = i % COLS
        row = i // COLS
        ex = PAD + col * ((W - PAD * 2) / COLS)
        ey = ENTRY_START_Y + row * ENTRY_H
        file_str = f" · {e['files']} file{'s' if e['files'] != 1 else ''}" if e["files"] else ""
        entry_els.append(f"""
    <circle cx="{ex+7}" cy="{ey+10}" r="5" fill="{e['color']}"/>
    <text x="{ex+20}" y="{ey+14}" fill="#e6edf3" font-size="12.5" font-weight="500" font-family="'Segoe UI',system-ui,sans-serif">{e['name']}</text>
    <text x="{ex+20}" y="{ey+30}" fill="#8b949e" font-size="10.5" font-family="'Segoe UI',system-ui,sans-serif">{e['pct']:.1f}%  ·  {format_bytes(e['bytes'])}{file_str}</text>""")

    svg = f"""<svg width="{W}" height="{TOTAL_H}" viewBox="0 0 {W} {TOTAL_H}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{W}" height="{TOTAL_H}" rx="14" fill="#0d1117"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{TOTAL_H-1}" rx="13.5" fill="none" stroke="#21262d" stroke-width="1"/>

  <!-- Header -->
  <text x="{PAD}" y="33" fill="#58a6ff" font-size="10" font-weight="700" letter-spacing="2.2" font-family="'Segoe UI',system-ui,sans-serif">LANGUAGES  ·  {REPO}</text>
  <line x1="{PAD}" y1="44" x2="{W-PAD}" y2="44" stroke="#21262d" stroke-width="1"/>

  <!-- Bar bg -->
  <rect x="{PAD}" y="{BAR_Y}" width="{BAR_W}" height="{BAR_H}" rx="6" fill="#161b22"/>
  {''.join(seg_els)}

  <!-- Entries -->
  {''.join(entry_els)}
</svg>"""

    return svg


def main():
    headers = {}
    # token is injected by the workflow via env
    import os
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    lang_res = requests.get(
        f"https://api.github.com/repos/{REPO}/languages", headers=headers
    )
    lang_res.raise_for_status()
    langs = lang_res.json()

    tree_res = requests.get(
        f"https://api.github.com/repos/{REPO}/git/trees/main?recursive=1",
        headers=headers,
    )
    tree_res.raise_for_status()
    tree = tree_res.json().get("tree", [])

    file_counts = count_files(tree)
    svg = build_svg(langs, file_counts)

    import pathlib
    pathlib.Path(OUTPUT).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(OUTPUT).write_text(svg, encoding="utf-8")
    print(f"Written to {OUTPUT}")


if __name__ == "__main__":
    main()
