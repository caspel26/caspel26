"""Generate the animated SVGs used by the profile README (assets/*.svg).

Usage (standard library only):

    python3 scripts/make_profile.py

Each image is written twice, `-dark` and `-light`, and the README picks one
with a <picture> element. GitHub renders SVGs through <img>, so only CSS
animation is used: no scripts, no external fonts, no network.
"""

from __future__ import annotations

import json
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
# Glyph paths (24x24) extracted from simple-icons, CC0. Names without a glyph get a lettered dot.
BRAND_ICONS: dict[str, str] = json.loads((Path(__file__).with_name("brand_icons.json")).read_text())
CONNECT = ["Portfolio", "LinkedIn", "Email", "GitHub"]
SANS = "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

THEMES = {
    "dark": {
        "bg": "#100e24", "bg2": "#1e1b4b", "card": "#17142e", "edge": "#2b2650",
        "text": "#f1eeff", "muted": "#9d98c8", "accent": "#b9a4ff",
        "violet": "#8b6cf0", "ochre": "#e8c39e", "chip": "#241f4a",
        "blob": 0.55,
    },
    "light": {
        "bg": "#faf8ff", "bg2": "#ece6ff", "card": "#ffffff", "edge": "#ddd5f5",
        "text": "#1d1a24", "muted": "#625c85", "accent": "#6d4fc2",
        "violet": "#7a55c4", "ochre": "#a8742f", "chip": "#efeaff",
        "blob": 0.35,
    },
}

ROLES = [
    "Backend · APIs · developer tools",
    "Python · Go · TypeScript",
    "AI-first · agentic programming",
    "Building Hinoki: Python APIs with a Rust core",
]

PROJECTS = [
    ("hinoki", "Typed Python APIs with a Rust core,", "and architecture rules you can check.",
     ["PYTHON", "RUST", "PRE-ALPHA"], True),
    ("django-ninja-aio-crud", "Async CRUD framework for Django Ninja,", "with an MCP server for AI agents.",
     ["PYTHON", "DJANGO NINJA", "MCP"], False),
    ("goninja", "Code-first CRUD REST APIs for Go,", "generated from annotated structs.",
     ["GO", "CODEGEN", "GORM"], False),
    ("shimwire", "Mock and test an API from one", "OpenAPI spec. A Bun and TypeScript CLI.",
     ["TYPESCRIPT", "BUN", "MCP"], False),
    ("lilac-nights", "A dark VS Code theme with a lilac spine,", "built to be read for eight hours.",
     ["THEME", "VS CODE", "WCAG AA"], False),
    ("Shiori", "Anime discovery and tracking,", "built end to end and in public beta.",
     ["GO", "POSTGRESQL", "PRODUCT"], False),
]

STACK = [
    ("LANGUAGES", ["Python", "Go", "TypeScript", "JavaScript", "Rust", "SQL"]),
    ("BACKEND AND FRONTEND", ["Django", "DRF", "FastAPI", "Django Ninja", "Gin", "Echo", "Huma",
                              "GORM", "Node.js", "Bun", "Vue", "Next.js", "Tailwind CSS"]),
    ("DATA AND DELIVERY", ["PostgreSQL", "MySQL", "SQLite", "Redis", "Docker", "Linux", "Nginx",
                           "HAProxy", "GitHub Actions", "GitLab", "Jenkins", "Cloudflare", "AWS"]),
    ("TESTING AND AI", ["Pytest", "Playwright", "Anthropic", "OpenAI", "Gemini", "Perplexity"]),
]


def write(name: str, theme: str, body: str) -> None:
    (OUT / f"{name}-{theme}.svg").write_text(body)


def header(theme: str, c: dict) -> str:
    roles = "".join(
        f'<text class="role" style="animation-delay:{i * 3}s" x="80" y="214">{escape(r)}</text>'
        for i, r in enumerate(ROLES)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300" role="img" aria-label="Hi, I'm Giuseppe. Backend engineer: frameworks, APIs and developer tools.">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c['bg2']}"/><stop offset="1" stop-color="{c['bg']}"/></linearGradient>
<linearGradient id="rule" x1="0" x2="1"><stop offset="0" stop-color="{c['violet']}"/><stop offset=".5" stop-color="{c['accent']}"/><stop offset="1" stop-color="{c['ochre']}"/></linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="46"/></filter>
<clipPath id="clip"><rect width="1200" height="300" rx="22"/></clipPath>
</defs>
<style>
text{{font-family:{SANS}}}
.hi{{font-size:60px;font-weight:700;fill:{c['text']};letter-spacing:-1.5px}}
.sub{{font-size:22px;fill:{c['muted']}}}
.role{{font-family:{MONO};font-size:20px;fill:{c['accent']};opacity:0;animation:role 12s infinite}}
.blob{{filter:url(#blur);opacity:{c['blob']}}}
.b1{{animation:drift1 14s ease-in-out infinite alternate}}
.b2{{animation:drift2 17s ease-in-out infinite alternate}}
.b3{{animation:drift1 19s ease-in-out infinite alternate-reverse}}
.sweep{{transform-box:fill-box;transform-origin:left;animation:sweep 5s ease-in-out infinite alternate}}
@keyframes role{{0%{{opacity:0;transform:translateY(8px)}}4%,22%{{opacity:1;transform:none}}26%,100%{{opacity:0;transform:translateY(-6px)}}}}
@keyframes drift1{{to{{transform:translate(120px,40px)}}}}
@keyframes drift2{{to{{transform:translate(-140px,-30px)}}}}
@keyframes sweep{{from{{transform:scaleX(.25)}}to{{transform:scaleX(1)}}}}
@media (prefers-reduced-motion:reduce){{.role,.b1,.b2,.b3,.sweep{{animation:none}}.role:first-of-type{{opacity:1}}}}
</style>
<g clip-path="url(#clip)">
<rect width="1200" height="300" fill="url(#bg)"/>
<circle class="blob b1" cx="260" cy="60" r="150" fill="{c['violet']}"/>
<circle class="blob b2" cx="900" cy="250" r="170" fill="{c['accent']}"/>
<circle class="blob b3" cx="1080" cy="40" r="110" fill="{c['ochre']}"/>
<text class="hi" x="80" y="120">Hi, I'm Giuseppe</text>
<text class="sub" x="80" y="164">Backend engineer · building Hinoki, goninja and django-ninja-aio-crud</text>
{roles}
<rect class="sweep" x="80" y="240" width="220" height="3" rx="1.5" fill="url(#rule)"/>
</g>
<rect x=".75" y=".75" width="1198.5" height="298.5" rx="21.5" fill="none" stroke="{c['edge']}" stroke-width="1.5"/>
</svg>
"""


def card(index: int, project: tuple, theme: str, c: dict) -> str:
    name, line1, line2, tags, featured = project
    chips, x = [], 28
    for tag in tags:
        w = len(tag) * 7.4 + 22
        tone = c["ochre"] if tag == "PRE-ALPHA" else c["accent"]
        chips.append(
            f'<rect x="{x}" y="138" width="{w:.0f}" height="26" rx="13" fill="{c["chip"]}"/>'
            f'<text class="tag" x="{x + w / 2:.0f}" y="155.5" text-anchor="middle" fill="{tone}">{tag}</text>'
        )
        x += w + 8
    glow = c["ochre"] if featured else c["violet"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 190" width="580" height="190" role="img" aria-label="{escape(name)}: {escape(line1)} {escape(line2)}">
<defs>
<linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{c['violet']}"/><stop offset="1" stop-color="{glow}"/></linearGradient>
<radialGradient id="glow" cx="1" cy="0" r="1"><stop offset="0" stop-color="{glow}" stop-opacity=".28"/><stop offset="1" stop-color="{glow}" stop-opacity="0"/></radialGradient>
<clipPath id="clip"><rect x="1" y="1" width="578" height="188" rx="18"/></clipPath>
</defs>
<style>
text{{font-family:{SANS}}}
.name{{font-size:26px;font-weight:700;fill:{c['text']};letter-spacing:-.4px}}
.desc{{font-size:15px;fill:{c['muted']}}}
.tag{{font-family:{MONO};font-size:11px;font-weight:600;letter-spacing:.6px}}
.num{{font-family:{MONO};font-size:12px;fill:{c['muted']}}}
.arrow{{fill:none;stroke:{c['accent']};stroke-width:2;stroke-linecap:round;stroke-linejoin:round;animation:nudge 2.4s ease-in-out infinite}}
.bar{{transform-box:fill-box;transform-origin:left;animation:bar 4.5s ease-in-out {index * .35:.2f}s infinite alternate}}
.glow{{animation:pulse 5s ease-in-out {index * .5:.1f}s infinite alternate}}
@keyframes nudge{{50%{{transform:translate(3px,-3px)}}}}
@keyframes bar{{from{{transform:scaleX(.18)}}to{{transform:scaleX(1)}}}}
@keyframes pulse{{from{{opacity:.55}}to{{opacity:1}}}}
@media (prefers-reduced-motion:reduce){{.arrow,.bar,.glow{{animation:none}}}}
</style>
<g clip-path="url(#clip)">
<rect width="580" height="190" fill="{c['card']}"/>
<rect class="glow" width="580" height="190" fill="url(#glow)"/>
<rect class="bar" x="0" y="0" width="580" height="3" fill="url(#bar)"/>
</g>
<rect x="1" y="1" width="578" height="188" rx="18" fill="none" stroke="{c['edge']}" stroke-width="1.5"/>
<text class="num" x="28" y="38">{index + 1:02d}</text>
<text class="name" x="28" y="76">{escape(name)}</text>
<text class="desc" x="28" y="102">{escape(line1)}</text>
<text class="desc" x="28" y="122">{escape(line2)}</text>
{''.join(chips)}
<path class="arrow" d="M534 38 L552 20 M538 20 H552 V34"/>
</svg>
"""


# LinkedIn is no longer in simple-icons; this is the same mark used on the portfolio site.
LINKEDIN_PATH = (
    "M20.45 0H3.55A3.55 3.55 0 0 0 0 3.55v16.9A3.55 3.55 0 0 0 3.55 24h16.9A3.55 3.55 0 0 0 24 20.45V3.55A3.55 3.55 0 0 0 20.45 0ZM7.1 20.45H3.56V9H7.1ZM5.33 7.44a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12ZM20.45 20.45h-3.54v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.13 1.45-2.13 2.94v5.67H9.39V9h3.4v1.56h.05c.47-.9 1.63-1.85 3.35-1.85 3.58 0 4.26 2.36 4.26 5.43Z"
)


def portfolio_mark(x: float, y: float, c: dict) -> str:
    """The portfolio favicon (arc and bar) without its tile, fitted to 16px."""
    return (
        f'<g transform="translate({x - 9.5:.1f} {y - 5.7:.1f}) scale(.72)">'
        f'<path d="M22.5 13.5A8.5 8.5 0 1 0 22.5 25.5" fill="none" stroke="{c["accent"]}" stroke-width="4.2" stroke-linecap="round"/>'
        f'<rect x="26.5" y="26" width="9" height="4.4" rx="1.2" fill="{c["ochre"]}"/></g>'
    )


def glyph(name: str, x: float, y: float, c: dict) -> str:
    """A 16px brand glyph from simple-icons (CC0), or a lettered dot when there is none."""
    if name == "Portfolio":
        return portfolio_mark(x, y, c)
    path = LINKEDIN_PATH if name == "LinkedIn" else BRAND_ICONS.get(name)
    if path:
        return f'<path transform="translate({x:.0f} {y:.0f}) scale(.667)" fill="{c["accent"]}" d="{path}"/>'
    return (
        f'<circle cx="{x + 8:.0f}" cy="{y + 8:.0f}" r="8" fill="none" stroke="{c["accent"]}" stroke-width="1.5"/>'
        f'<text class="mono" x="{x + 8:.0f}" y="{y + 11.5:.0f}" text-anchor="middle" fill="{c["accent"]}">{escape(name[0])}</text>'
    )


def pill_row(names: list[str], c: dict) -> tuple[str, int]:
    pills, x = [], 0
    for name in names:
        w = len(name) * 7.7 + 54
        pills.append(
            f'<rect x="{x:.0f}" y="0" width="{w:.0f}" height="38" rx="19" fill="{c["chip"]}" stroke="{c["edge"]}"/>'
            f'{glyph(name, x + 14, 11, c)}'
            f'<text class="pill" x="{x + 38}" y="24.5">{escape(name)}</text>'
        )
        x += w + 10
    return "".join(pills), int(x)


def stack(theme: str, c: dict) -> str:
    labels, rows, rules, y = [], [], [], 0
    for i, (label, names) in enumerate(STACK):
        pills, width = pill_row(names, c)
        speed = max(24, width // 38)
        direction = "reverse" if i % 2 else "normal"
        labels.append(f'<text class="label" x="20" y="{y + 20}">{label}</text>')
        rules.append(f".t{i}{{--w:-{width}px;animation-duration:{speed}s;animation-direction:{direction}}}")
        rows.append(
            f'<g transform="translate(0 {y + 32})"><g class="track t{i}">'
            f'{pills}<g transform="translate({width} 0)">{pills}</g></g></g>'
        )
        y += 86
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {y}" width="1200" height="{y}" role="img" aria-label="Languages, frameworks, data, delivery, testing and AI tools I work with">
<defs>
<linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".06" stop-color="#fff"/><stop offset=".94" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="m"><rect width="1200" height="{y}" fill="url(#fade)"/></mask>
</defs>
<style>
.label{{font-family:{MONO};font-size:11px;font-weight:600;letter-spacing:1.6px;fill:{c['muted']}}}
.pill{{font-family:{SANS};font-size:14px;font-weight:600;fill:{c['text']}}}
.mono{{font-family:{MONO};font-size:10px;font-weight:700}}
.track{{animation-name:marquee;animation-timing-function:linear;animation-iteration-count:infinite}}
@keyframes marquee{{to{{transform:translateX(var(--w))}}}}
{''.join(rules)}
@media (prefers-reduced-motion:reduce){{.track{{animation:none}}}}
</style>
<g mask="url(#m)">{''.join(rows)}</g>
{''.join(labels)}
</svg>
"""


def footer(theme: str, c: dict) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="1200" height="120" role="presentation">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{c['violet']}"/><stop offset=".5" stop-color="{c['accent']}"/><stop offset="1" stop-color="{c['ochre']}"/></linearGradient></defs>
<style>
.w1{{animation:slide 14s linear infinite}}
.w2{{animation:slide 22s linear infinite reverse}}
@keyframes slide{{to{{transform:translateX(-600px)}}}}
@media (prefers-reduced-motion:reduce){{.w1,.w2{{animation:none}}}}
</style>
<g fill="url(#g)">
<path class="w2" opacity=".35" d="M0 70 Q150 20 300 70 T600 70 T900 70 T1200 70 T1500 70 T1800 70 V120 H0Z"/>
<path class="w1" opacity=".6" d="M0 86 Q150 46 300 86 T600 86 T900 86 T1200 86 T1500 86 T1800 86 V120 H0Z"/>
</g>
</svg>
"""


def connect(label: str, c: dict) -> str:
    w = int(len(label) * 8.2 + 62)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 44" width="{w}" height="44" role="img" aria-label="{label}">
<style>
.t{{font-family:{SANS};font-size:15px;font-weight:600;fill:{c['text']}}}
.mono{{font-family:{MONO};font-size:11px;font-weight:700}}
</style>
<rect x=".75" y=".75" width="{w - 1.5}" height="42.5" rx="21.25" fill="{c['chip']}" stroke="{c['edge']}" stroke-width="1.5"/>
{glyph(label, 20, 14, c)}
<text class="t" x="46" y="28">{escape(label)}</text>
</svg>
"""


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for theme, c in THEMES.items():
        write("header", theme, header(theme, c))
        write("stack", theme, stack(theme, c))
        write("footer", theme, footer(theme, c))
        for label in CONNECT:
            write(f"connect-{label.lower()}", theme, connect(label, c))
        for i, project in enumerate(PROJECTS):
            write(f"card-{project[0].lower()}", theme, card(i, project, theme, c))
    print(f"wrote {len(list(OUT.glob('*.svg')))} SVGs to {OUT}")


if __name__ == "__main__":
    main()
