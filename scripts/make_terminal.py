"""Render assets/terminal.gif, the animated terminal at the top of the README.

Usage (needs Pillow and macOS's Menlo; nothing else):

    uv run --with pillow python scripts/make_terminal.py

The session is scripted below, so the project list stays in one place: edit
PROJECTS and re-run. Frames are drawn at 2x and scaled down for smooth text.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "assets" / "terminal.gif"
FONT = "/System/Library/Fonts/Menlo.ttc"
W, H, SCALE = 940, 440, 2
SIZE, LEADING = 21, 34
PAD_X, FIRST_LINE = 56, 94

BG, CARD, EDGE = "#100e24", "#17142e", "#2b2650"
TEXT, MUTED = "#e7e3ff", "#7f7aa8"
LILAC, VIOLET, MINT, OCHRE = "#b9a4ff", "#8b6cf0", "#6ee7b7", "#e8c39e"

Segment = tuple[str, str] | tuple[str, str, bool]
PROMPT: list[Segment] = [("caspel26", LILAC), (" ~ ", MUTED), ("❯ ", VIOLET)]
OTHERS = ["django-ninja-aio-crud", "goninja", "shimwire", "lilac-nights"]
SCRIPT: list[tuple[str, list[list[Segment]]]] = [
    ("whoami", [[("caspel26", TEXT)]]),
    (
        "cat about.txt",
        [
            [("Software Engineer @ Namirial Group", LILAC, True)],
            [("Backend · Python · Go · Async APIs", MUTED)],
        ],
    ),
    (
        "ls projects/",
        [
            [("hinoki/", OCHRE, True), ("  pre-alpha", MUTED)],
            [("  ".join(f"{name}/" for name in OTHERS), VIOLET)],
        ],
    ),
]


def face(bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, SIZE * SCALE, index=1 if bold else 0)


REGULAR, BOLD = face(), face(True)


def draw_line(draw: ImageDraw.ImageDraw, row: int, segments: list[Segment]) -> int:
    x = PAD_X * SCALE
    y = (FIRST_LINE + row * LEADING) * SCALE
    for seg in segments:
        font = BOLD if len(seg) > 2 and seg[2] else REGULAR
        draw.text((x, y), seg[0], fill=seg[1], font=font)
        x += int(draw.textlength(seg[0], font=font))
    return x


def chrome(draw: ImageDraw.ImageDraw) -> None:
    box = (24 * SCALE, 20 * SCALE, (W - 24) * SCALE, (H - 20) * SCALE)
    draw.rounded_rectangle(
        box, radius=18 * SCALE, fill=CARD, outline=EDGE, width=2 * SCALE
    )
    for i, color in enumerate(("#ff5f57", "#febc2e", "#28c840")):
        cx, cy, r = (52 + i * 22) * SCALE, 48 * SCALE, 6 * SCALE
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)
    title = "caspel26 — zsh"
    width = draw.textlength(title, font=REGULAR)
    draw.text(((W * SCALE - width) / 2, 36 * SCALE), title, fill=MUTED, font=REGULAR)
    draw.line(
        (24 * SCALE, 72 * SCALE, (W - 24) * SCALE, 72 * SCALE), fill=EDGE, width=SCALE
    )


def frame(lines: list[list[Segment]], cursor: bool) -> Image.Image:
    img = Image.new("RGB", (W * SCALE, H * SCALE), BG)
    draw = ImageDraw.Draw(img)
    chrome(draw)
    end_x = PAD_X * SCALE
    for row, line in enumerate(lines):
        end_x = draw_line(draw, row, line)
    if cursor:
        top = (FIRST_LINE + (len(lines) - 1) * LEADING + 4) * SCALE
        draw.rectangle(
            (end_x + 2 * SCALE, top, end_x + 14 * SCALE, top + 26 * SCALE), fill=LILAC
        )
    # Crop to the card so it spans the full image width, like the header above it.
    img = img.crop((22 * SCALE, 18 * SCALE, (W - 22) * SCALE, (H - 18) * SCALE))
    return img.resize(((W - 44) * 3 // 2, (H - 36) * 3 // 2), Image.Resampling.LANCZOS)


def build() -> list[tuple[Image.Image, int]]:
    frames: list[tuple[Image.Image, int]] = []
    done: list[list[Segment]] = []

    def add(typing: str | None, cursor: bool, ms: int) -> None:
        shown = list(done)
        if typing is not None:
            shown.append(PROMPT + [(typing, MINT)])
        frames.append((frame(shown, cursor), ms))

    add("", True, 700)
    for command, output in SCRIPT:
        for n in range(1, len(command) + 1):
            add(command[:n], True, 150 if command[n - 1] == " " else 70)
        add(command, True, 350)
        done.append(PROMPT + [(command, MINT)])
        for line in output:
            done.append(line)
            add(None, False, 120)
        add("", True, 650)
    for _ in range(3):
        add("", True, 520)
        add("", False, 520)
    return frames


def palette_from(sample: Image.Image) -> Image.Image:
    """A shared palette: the last frame plus a swatch of every flat colour,
    so small accents (the window dots) are not merged into their neighbours."""
    flat = ["#ff5f57", "#febc2e", "#28c840", BG, CARD, EDGE, TEXT, MUTED]
    flat += [LILAC, VIOLET, MINT, OCHRE]
    swatches = Image.new("RGB", (len(flat) * 40, 40))
    for i, color in enumerate(flat):
        swatches.paste(color, (i * 40, 0, i * 40 + 40, 40))
    sheet = Image.new("RGB", (sample.width, sample.height + 40))
    sheet.paste(sample, (0, 0))
    sheet.paste(swatches, (0, sample.height))
    return sheet.quantize(colors=128, dither=Image.Dither.NONE)


def corner_mask(size: tuple[int, int]) -> Image.Image:
    """White outside the card's rounded corners: those pixels become transparent."""
    mask = Image.new("L", size, 255)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, size[0] - 1, size[1] - 1), radius=27, fill=0
    )
    return mask


def main() -> None:
    built = build()
    palette = palette_from(built[-2][0])
    clear = palette.getpalette() or []
    bg = tuple(int(BG[i : i + 2], 16) for i in (1, 3, 5))
    index = next(i for i in range(0, len(clear), 3) if tuple(clear[i : i + 3]) == bg) // 3
    mask = corner_mask(built[0][0].size)
    images = []
    for image, _ in built:
        quantized = image.quantize(palette=palette, dither=Image.Dither.NONE)
        quantized.paste(index, mask=mask)
        images.append(quantized)
    images[0].save(
        OUT,
        save_all=True,
        append_images=images[1:],
        duration=[ms for _, ms in built],
        loop=0,
        optimize=True,
        transparency=index,
        disposal=2,
    )
    total = sum(ms for _, ms in built) / 1000
    print(f"{OUT}: {len(built)} frames, {total:.1f} s, {OUT.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
