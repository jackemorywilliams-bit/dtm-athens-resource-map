#!/usr/bin/env python3
"""Regenerate the brand/ asset set (and mirror it into docs/brand/).

Occasional-use tool; NOT part of build.py's critical path. Requires Pillow.
Sources are the raw logo files (see RAW_* paths, override via env).

Outputs (all transparent PNG unless noted):
  brand/dtm-bird.png    red bird mark, red-pixel extraction, ~256px wide
  brand/odb-logo.png    ODB arch, soft-alpha from luminance, bottom 22%
                        cropped (drops the blurry baked-in subtitle; the
                        letterspaced DOWNTOWN MINISTRIES line is rebuilt in
                        type wherever the mark is used). Low-res source:
                        never render above 300px wide.
  brand/dta-logo.png    DTA typographic mark (from supplied raster)
  brand/el-logo.png     PLACEHOLDER: no official Emerging Leaders asset
                        exists; letterspaced text + brick rule. Replace when
                        DTM provides a real mark.
  brand/favicon-32.png  tight bird crop, 32x32
  brand/favicon.ico     16/32/48 bird
  brand/og-card.png     1200x630 social card (paper bg, bird, serif title,
                        brick rule). Not transparent.
"""
import os
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent.parent
BRAND = HERE / "brand"
DOCS_BRAND = HERE / "docs" / "brand"

RAW_BIRD = Path(os.environ.get("RAW_BIRD", "/Users/emorywilliams/Downloads/dtm_bird_logo.png"))
RAW_ODB = Path(os.environ.get("RAW_ODB", "/Users/emorywilliams/Downloads/odb_logo.png"))
RAW_DTA = Path(os.environ.get("RAW_DTA", "/Users/emorywilliams/Downloads/dta_logo.png"))

INK = (28, 28, 28, 255)          # --ink
ACCENT = (139, 58, 43, 255)      # --accent (brick)
PAPER = (250, 250, 247, 255)     # --paper

SERIF_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
    "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
]


def serif(size: int) -> ImageFont.FreeTypeFont:
    for p in SERIF_CANDIDATES:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default(size)


def save(img: Image.Image, name: str, quantize: int = 0, alpha_floor: int = 36) -> None:
    if img.mode == "RGBA" and alpha_floor:
        arr = np.array(img)
        a = arr[:, :, 3].astype(int)
        a[a < alpha_floor] = 0  # low-alpha speckle compresses terribly; drop it
        arr[:, :, 3] = a.astype("uint8")
        img = Image.fromarray(arr)
    if quantize:
        img = img.quantize(quantize, method=Image.FASTOCTREE)
    for d in (BRAND, DOCS_BRAND):
        d.mkdir(parents=True, exist_ok=True)
        img.save(d / name, optimize=True)
    kb = (BRAND / name).stat().st_size // 1024
    print(f"  {name}: {img.size[0]}x{img.size[1]}, {kb}KB")


def bird() -> Image.Image:
    arr = np.array(Image.open(RAW_BIRD).convert("RGBA"))
    r, g, b = arr[:, :, 0].astype(int), arr[:, :, 1].astype(int), arr[:, :, 2].astype(int)
    arr[:, :, 3] = np.where((r > 150) & (g < 100) & (b < 100), 255, 0)
    img = Image.fromarray(arr)
    img = img.crop(img.getbbox())
    img.thumbnail((200, 200), Image.LANCZOS)
    save(img, "dtm-bird.png", quantize=32)
    return img


def odb() -> None:
    src = Image.open(RAW_ODB).convert("RGBA")
    # flatten onto white, then soft alpha from inverted luminance so
    # anti-aliased edges keep partial coverage (no hard threshold mush)
    flat = Image.new("RGBA", src.size, (255, 255, 255, 255))
    flat.alpha_composite(src)
    gray = np.array(flat.convert("L")).astype(float)
    alpha = np.clip((235 - gray) / 235 * 255 * 1.25, 0, 255).astype(np.uint8)
    out = np.zeros((*gray.shape, 4), dtype=np.uint8)
    out[:, :, 0] = INK[0]
    out[:, :, 1] = INK[1]
    out[:, :, 2] = INK[2]
    out[:, :, 3] = alpha
    img = Image.fromarray(out)
    img = img.crop(img.getbbox())
    img = img.crop((0, 0, img.width, int(img.height * 0.78)))  # drop baked subtitle band
    img.thumbnail((300, 300), Image.LANCZOS)  # low-res source: 300px cap
    save(img, "odb-logo.png", quantize=64)


def dta() -> None:
    img = Image.open(RAW_DTA).convert("RGBA")
    px = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            if r > 240 and g > 240 and b > 240:
                px[x, y] = (255, 255, 255, 0)
    img = img.crop(img.getbbox())
    img.thumbnail((320, 320), Image.LANCZOS)
    save(img, "dta-logo.png", quantize=32)


def el_placeholder() -> None:
    # placeholder mark: no official Emerging Leaders asset exists; replace
    # when DTM provides one
    f = serif(34)
    text = "E M E R G I N G   L E A D E R S"
    probe = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(probe)
    w = int(d.textlength(text, font=f))
    pad = 12
    img = Image.new("RGBA", (w + pad * 2, 84), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((pad, 8), text, font=f, fill=INK)
    rule_w = int((w + pad * 2) * 0.6)
    x0 = (img.width - rule_w) // 2
    d.rectangle([x0, 66, x0 + rule_w, 70], fill=ACCENT)
    save(img, "el-logo.png")


def favicons(bird_img: Image.Image) -> None:
    side = max(bird_img.size)
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.alpha_composite(bird_img, ((side - bird_img.width) // 2, (side - bird_img.height) // 2))
    fav = sq.resize((32, 32), Image.LANCZOS)
    save(fav, "favicon-32.png")
    ico = sq.resize((48, 48), Image.LANCZOS)
    for d in (BRAND, DOCS_BRAND):
        ico.save(d / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"  favicon.ico: 16/32/48, {(BRAND / 'favicon.ico').stat().st_size // 1024}KB")


def og_card(bird_img: Image.Image) -> None:
    img = Image.new("RGBA", (1200, 630), PAPER)
    d = ImageDraw.Draw(img)
    b = bird_img.copy()
    b.thumbnail((360, 360), Image.LANCZOS)
    img.alpha_composite(b, ((1200 - b.width) // 2, 130))
    title = "Athens Area Resource Map"
    f = serif(64)
    tw = int(d.textlength(title, font=f))
    d.text(((1200 - tw) // 2, 330), title, font=f, fill=INK)
    sub = "Downtown Ministries"
    f2 = serif(30)
    sw = int(d.textlength(sub, font=f2))
    d.text(((1200 - sw) // 2, 420), sub, font=f2, fill=(74, 74, 74, 255))
    d.rectangle([(1200 - 340) // 2, 480, (1200 + 340) // 2, 486], fill=ACCENT)
    save(img.convert("RGB").convert("RGBA"), "og-card.png")


if __name__ == "__main__":
    print("brand assets:")
    b = bird()
    odb()
    dta()
    el_placeholder()
    favicons(b)
    og_card(b)
    print("done — mirror written to docs/brand/")
