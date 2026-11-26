#!/usr/bin/env python3
"""Draw the front page for Thursday 26 November 2026 (PIL, build-time only).

The entry itself is main.py + assets/entry.png; this script only produced
the bundled picture. Layout: masthead, North-Korea nuclear lead (missile
+ mushroom cloud), right column (Tiangong space / US tariffs), three
middle panels (Ukraine air base / asteroid close-ups / Bangladesh wages),
and an "also today" ticker.
"""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 232)
INK = (22, 22, 22)
RED = (176, 32, 26)
DARKRED = (58, 14, 14)
NAVY = (16, 34, 64)
BLUE = (30, 70, 130)
TEAL = (16, 104, 104)
ORANGE = (208, 92, 18)
GOLD = (198, 148, 42)
GREY = (96, 94, 86)
LIGHT = (233, 227, 211)
WHITE = (248, 246, 240)
SMOKE = (120, 116, 108)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / name), size)


def serif_b(s: int):
    return font("DejaVuSerif-Bold.ttf", s)


def serif(s: int):
    return font("DejaVuSerif.ttf", s)


def sans_b(s: int):
    return font("DejaVuSans-Bold.ttf", s)


def sans(s: int):
    return font("DejaVuSans.ttf", s)


def wrap(d: ImageDraw.ImageDraw, text: str, fnt, width: int) -> list[str]:
    out, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if d.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                out.append(line)
            line = word
    if line:
        out.append(line)
    return out


def para(d, x, y, text, fnt, width, leading, color=INK):
    for ln in wrap(d, text, fnt, width):
        d.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


def kicker(d, x, y, text, color=RED):
    d.text((x, y), text, font=sans_b(15), fill=color)
    return y + 22


def rule(d, x0, y, x1, color=INK, w=2):
    d.line([(x0, y), (x1, y)], fill=color, width=w)


def panel(d, x0, y0, x1, y1, fill=None, outline=INK, w=2):
    d.rectangle([x0, y0, x1, y1], fill=fill, outline=outline, width=w)


# ---------------------------------------------------------------- visuals

def draw_mushroom(d, cx, base_y, scale=1.0):
    """Mushroom cloud: stacked circles, orange-red glow on dark ground."""
    glow = (214, 110, 30)
    d.ellipse([cx - 118 * scale, base_y - 150 * scale,
               cx + 118 * scale, base_y - 30 * scale], fill=(96, 30, 18))
    d.ellipse([cx - 88 * scale, base_y - 190 * scale,
               cx + 88 * scale, base_y - 70 * scale], fill=glow)
    d.ellipse([cx - 58 * scale, base_y - 214 * scale,
               cx + 58 * scale, base_y - 110 * scale], fill=(232, 150, 60))
    d.ellipse([cx - 26 * scale, base_y - 228 * scale,
               cx + 26 * scale, base_y - 160 * scale], fill=(248, 196, 110))
    # stem
    d.polygon([(cx - 22 * scale, base_y - 120 * scale),
               (cx + 22 * scale, base_y - 120 * scale),
               (cx + 34 * scale, base_y),
               (cx - 34 * scale, base_y)], fill=(150, 82, 34))
    d.polygon([(cx - 12 * scale, base_y - 120 * scale),
               (cx + 12 * scale, base_y - 120 * scale),
               (cx + 18 * scale, base_y),
               (cx - 18 * scale, base_y)], fill=(214, 130, 50))


def draw_missile(d, x, y, length=210, angle=-38):
    """Slim missile silhouette angled up-right, with exhaust flame."""
    a = math.radians(angle)
    dx, dy = math.cos(a), math.sin(a)
    px, py = -dy, dx  # perpendicular
    bx, by = x, y
    tx, ty = x + dx * length, y + dy * length
    hw = 9
    body = [(bx + px * hw, by + py * hw), (tx + px * hw, ty + py * hw),
            (tx + dx * 26, ty + dy * 26),
            (tx - px * hw, ty - py * hw), (bx - px * hw, by - py * hw)]
    d.polygon(body, fill=(210, 208, 200))
    # fins near the tail
    d.polygon([(bx, by), (bx - dx * 26 + px * 22, by - dy * 26 + py * 22),
               (bx - dx * 8 + px * 22, by - dy * 8 + py * 22)], fill=(176, 32, 26))
    d.polygon([(bx, by), (bx - dx * 26 - px * 22, by - dy * 26 - py * 22),
               (bx - dx * 8 - px * 22, by - dy * 8 - py * 22)], fill=(176, 32, 26))
    # flame
    fx, fy = bx - dx * 20, by - dy * 20
    d.polygon([(fx + px * 10, fy + py * 10), (fx - px * 10, fy - py * 10),
               (fx - dx * 44, fy - dy * 44)], fill=(240, 160, 40))
    d.polygon([(fx + px * 5, fy + py * 5), (fx - px * 5, fy - py * 5),
               (fx - dx * 30, fy - dy * 30)], fill=(250, 220, 120))


def draw_rocket_station(d, x0, y0, x1, y1):
    """Rocket rising past a small space station, on navy."""
    # stars
    for sx, sy, r in [(x0 + 30, y0 + 26, 2), (x0 + 90, y0 + 60, 1),
                      (x0 + 170, y0 + 22, 2), (x0 + 230, y0 + 70, 1),
                      (x0 + 60, y0 + 110, 1), (x0 + 250, y0 + 120, 2),
                      (x0 + 140, y0 + 96, 1)]:
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=WHITE)
    # small moon, top right
    d.ellipse([x1 - 52, y0 + 18, x1 - 22, y0 + 48], fill=(220, 222, 210))
    d.ellipse([x1 - 44, y0 + 26, x1 - 36, y0 + 34], fill=(190, 192, 180))
    # station: central module + solar panels (compact)
    mx, my = x0 + 168, y0 + 52
    d.rectangle([mx - 44, my - 8, mx + 44, my + 8], fill=(190, 196, 208))
    d.rectangle([mx - 44, my - 8, mx + 44, my - 8 + 4], fill=(120, 128, 150))
    d.rectangle([mx - 92, my - 14, mx - 48, my + 14], fill=(52, 96, 168))
    d.rectangle([mx + 48, my - 14, mx + 92, my + 14], fill=(52, 96, 168))
    d.ellipse([mx - 12, my - 12, mx + 12, my + 12], fill=(210, 214, 222))
    # small rocket, left
    rx, ry = x0 + 46, y0 + 62
    d.polygon([(rx - 9, ry + 28), (rx + 9, ry + 28), (rx + 9, ry - 20),
               (rx, ry - 34), (rx - 9, ry - 20)], fill=(236, 236, 230))
    d.rectangle([rx - 9, ry - 4, rx + 9, ry + 2], fill=(176, 32, 26))
    d.polygon([(rx - 9, ry + 28), (rx - 19, ry + 42), (rx - 9, ry + 36)],
              fill=(176, 32, 26))
    d.polygon([(rx + 9, ry + 28), (rx + 19, ry + 42), (rx + 9, ry + 36)],
              fill=(176, 32, 26))
    d.polygon([(rx - 5, ry + 28), (rx + 5, ry + 28), (rx, ry + 40)],
              fill=(250, 200, 80))


def draw_chart_down(d, x0, y0, x1, y1):
    """Falling market line with red arrow, inside its own box."""
    top = y0 + 2
    pts = [(x0 + 10, top + 2), (x0 + 60, top + 8), (x0 + 105, top + 6),
           (x0 + 155, top + 22), (x0 + 205, top + 18), (x0 + 252, top + 34)]
    for gx in range(x0 + 10, x1 - 10, 28):
        d.line([(gx, top), (gx, y1 - 4)], fill=(214, 208, 192), width=1)
    d.line(pts, fill=RED, width=5, joint="curve")
    ex, ey = pts[-1]
    d.polygon([(ex, ey + 12), (ex - 13, ey - 4), (ex + 2, ey - 2)], fill=RED)


def draw_jet_blast(d, x0, y0, x1, y1):
    """Jet silhouette over a runway blast."""
    cx, cy = (x0 + x1) // 2, y0 + 42
    d.polygon([(cx - 96, cy - 2), (cx + 78, cy - 12), (cx + 124, cy),
               (cx + 78, cy + 12), (cx - 96, cy + 6)], fill=(70, 74, 82))
    d.polygon([(cx - 26, cy - 8), (cx + 8, cy - 40), (cx + 20, cy - 8)],
              fill=(70, 74, 82))
    d.polygon([(cx - 44, cy + 8), (cx - 16, cy + 34), (cx - 2, cy + 8)],
              fill=(70, 74, 82))
    d.polygon([(cx - 96, cy - 2), (cx - 118, cy - 16), (cx - 112, cy + 2)],
              fill=(70, 74, 82))
    # blast below
    bx, by = cx + 10, y1 - 40
    for r, col in [(46, (232, 120, 30)), (34, (244, 170, 60)),
                   (20, (252, 216, 110))]:
        d.ellipse([bx - r, by - r // 2, bx + r, by + r // 2], fill=col)
    d.line([(x0 + 16, y1 - 12), (x1 - 16, y1 - 12)], fill=GREY, width=3)


def draw_asteroid(d, x0, y0, x1, y1):
    """Cratered grey asteroid on black sky with a small probe trail."""
    cx, cy = (x0 + x1) // 2, y0 + 52
    d.ellipse([cx - 44, cy - 34, cx + 44, cy + 34], fill=(150, 146, 138))
    d.ellipse([cx - 44, cy - 34, cx + 44, cy + 34], outline=(96, 92, 84),
              width=2)
    for ox, oy, r in [(-20, -12, 9), (13, 6, 12), (-4, 18, 6),
                      (24, -15, 6), (-27, 11, 4)]:
        d.ellipse([cx + ox - r, cy + oy - r, cx + ox + r, cy + oy + r],
                  fill=(118, 114, 106))
        d.ellipse([cx + ox - r, cy + oy - r, cx + ox + r, cy + oy + r],
                  outline=(88, 84, 76), width=1)
    d.ellipse([cx - 44, cy - 34, cx - 8, cy - 4], fill=(178, 174, 166))
    # impact flash + probe
    d.ellipse([cx + 32, cy - 42, cx + 48, cy - 26], fill=(250, 220, 120))
    d.line([(cx + 56, cy - 46), (x1 - 18, y0 + 12)], fill=GOLD, width=2)


def draw_shirt(d, x0, y0, x1, y1):
    """T-shirt on a hanger line above a factory skyline."""
    cx, cy = (x0 + x1) // 2, y0 + 40
    d.line([(x0 + 20, y0 + 12), (x1 - 20, y0 + 12)], fill=GREY, width=2)
    d.line([(cx, y0 + 12), (cx, y0 + 22)], fill=GREY, width=2)
    d.polygon([(cx - 44, cy - 6), (cx - 66, cy + 10), (cx - 49, cy + 28),
               (cx - 39, cy + 18), (cx - 39, cy + 56), (cx + 39, cy + 56),
               (cx + 39, cy + 18), (cx + 49, cy + 28), (cx + 66, cy + 10),
               (cx + 44, cy - 6), (cx + 17, cy - 6),
               (cx, cy + 7), (cx - 17, cy - 6)], fill=(38, 120, 96))
    d.arc([cx - 17, cy - 6, cx + 17, cy + 12], 0, 180, fill=(22, 90, 70),
          width=3)
    # factory skyline at the bottom
    fy = y1 - 8
    d.rectangle([x0 + 18, fy - 14, x0 + 70, fy], fill=(90, 88, 84))
    d.rectangle([x0 + 78, fy - 22, x0 + 118, fy], fill=(110, 108, 100))
    d.rectangle([x0 + 126, fy - 9, x0 + 190, fy], fill=(90, 88, 84))
    d.rectangle([x0 + 96, fy - 38, x0 + 104, fy - 22], fill=(110, 108, 100))
    d.rectangle([x0 + 196, fy - 17, x0 + 250, fy], fill=(110, 108, 100))


# ---------------------------------------------------------------- page

def build() -> Image.Image:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 26  # margin
    rx = W - mx

    # masthead
    title = "THE WORLD IN ONE DAY"
    tf = serif_b(56)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 16), title, font=tf, fill=INK)
    rule(d, mx, 92, rx, INK, 3)
    date_line = "THURSDAY, 26 NOVEMBER 2026  •  ONE DAY, ONE PICTURE"
    df = sans_b(20)
    dw = d.textlength(date_line, font=df)
    d.text(((W - dw) / 2, 100), date_line, font=df, fill=RED)
    rule(d, mx, 130, rx, INK, 2)

    # ---- lead: North Korea (left, dark panel)
    lx0, ly0, lx1, ly1 = mx, 142, 668, 540
    d.rectangle([lx0, ly0, lx1, ly1], fill=DARKRED)
    d.rectangle([lx0, ly0, lx1, ly1], outline=INK, width=2)
    ix = lx0 + 20
    iy = ly0 + 16
    d.text((ix, iy), "NORTH KOREA", font=sans_b(16), fill=(244, 170, 60))
    d.text((ix + 168, iy), "—  LEAD STORY", font=sans_b(16),
           fill=(200, 190, 180))
    iy += 30
    iy = para(d, ix, iy, "KIM ORDERS WIDER NUCLEAR DEPLOYMENT",
              serif_b(40), lx1 - lx0 - 40, 46, WHITE)
    iy += 4
    iy = para(d, ix, iy,
              "Kim inspects nuclear sites and calls the North's status as a "
              "nuclear-weapons state “absolutely inviolable”.",
              sans(17), lx1 - lx0 - 40, 23, (228, 220, 208))
    # visuals: missile flying low-right, mushroom cloud bottom-left
    draw_missile(d, lx0 + 430, ly0 + 300, length=130, angle=-28)
    draw_mushroom(d, lx0 + 150, ly1 - 14, scale=0.78)
    qy = ly1 - 66
    q = "“Our nuclear capability is now a reality.”"
    d.text((lx0 + 290, qy), q, font=serif(17), fill=(248, 220, 160))
    d.text((lx0 + 290, qy + 24), "— Kim Jong Un, KCNA", font=sans(15),
           fill=(200, 190, 180))

    # ---- right column: space
    cx0, cx1 = 684, rx
    sx0, sy0, sy1 = cx0, 142, 332
    d.rectangle([sx0, sy0, cx1, sy1], fill=NAVY)
    d.rectangle([sx0, sy0, cx1, sy1], outline=INK, width=2)
    draw_rocket_station(d, sx0, sy0, cx1, sy1)
    d.rectangle([sx0, sy1 - 100, cx1, sy1], fill=(12, 26, 52))
    yy = kicker(d, sx0 + 14, sy1 - 96, "SPACE", color=(120, 190, 240))
    yy = para(d, sx0 + 14, yy, "PAKISTAN'S FIRST ASTRONAUT ON TIANGONG",
              sans_b(16), cx1 - sx0 - 28, 20, WHITE)
    para(d, sx0 + 14, yy + 2,
         "Zeeshan Ali aboard Shenzhou-24.",
         sans(14), cx1 - sx0 - 28, 18, (200, 212, 228))

    # ---- right column: tariffs
    tx0, ty0, ty1 = cx0, 346, 540
    panel(d, tx0, ty0, cx1, ty1, fill=WHITE)
    yy = kicker(d, tx0 + 14, ty0 + 10, "TRADE WAR")
    yy = para(d, tx0 + 14, yy, "US UNVEILS NEW TARIFFS ON 14 PARTNERS",
              serif_b(21), cx1 - tx0 - 28, 25, INK)
    d.text((tx0 + 14, yy + 2), "China hit hardest; Taiwan faces 15%.",
           font=sans(15), fill=(60, 58, 52))
    draw_chart_down(d, tx0 + 14, ty1 - 52, cx1 - 14, ty1 - 12)

    # ---- middle row: three panels
    my0, my1 = 556, 826
    pw = (rx - mx - 2 * 16) // 3
    panels = [
        ("UKRAINE", "UKRAINE HITS RUSSIAN AIR BASE",
         "Five planes damaged in a strike deep inside Russia.",
         draw_jet_blast, RED),
        ("SCIENCE", "FIRST CLOSE-UPS OF THE ASTEROID WE HIT",
         "New images of the asteroid struck to test Earth's defences.",
         draw_asteroid, BLUE),
        ("WORK", "BANGLADESH RAISES GARMENT PAY 36%",
         "Minimum-wage rise for millions of garment workers.",
         draw_shirt, TEAL),
    ]
    for i, (kick, head, body, draw_fn, col) in enumerate(panels):
        px0 = mx + i * (pw + 16)
        px1 = px0 + pw
        panel(d, px0, my0, px1, my1, fill=WHITE)
        yy = kicker(d, px0 + 14, my0 + 12, kick, color=col)
        yy = para(d, px0 + 14, yy, head, serif_b(23), px1 - px0 - 28, 27, INK)
        yy += 4
        para(d, px0 + 14, yy, body, sans(15), px1 - px0 - 28, 20,
             (60, 58, 52))
        draw_fn(d, px0 + 8, my1 - 108, px1 - 8, my1 - 12)

    # ---- ticker
    ty0, ty1 = 842, 1000
    d.rectangle([mx, ty0, rx, ty1], fill=INK)
    d.text((mx + 16, ty0 + 12), "ALSO TODAY", font=sans_b(17),
           fill=(244, 170, 60))
    items = [
        ("Colombia marks 10 years since its peace deal",
         "Lebanon to open a second international airport"),
        ("N. Korea tells Switzerland to shut its Pyongyang office",
         "Russia's own toll: nearly 500,000 lost in Ukraine"),
        ("Gukesh faces Sindarov for the world chess crown",
         "India marks Constitution Day"),
    ]
    yy = ty0 + 38
    for a, b in items:
        txt = f"{a}   •   {b}"
        d.text((mx + 16, yy), txt, font=sans(15), fill=(232, 228, 218))
        yy += 26
    rule(d, mx, ty1 - 22, rx, (120, 116, 108), 1)
    foot = "THE WORLD IN ONE DAY  •  THURSDAY 26 NOVEMBER 2026  •  SOURCES: REUTERS / CNN / AP"
    fw = d.textlength(foot, font=sans(13))
    d.text(((W - fw) / 2, ty1 - 18), foot, font=sans(13),
           fill=(170, 166, 156))

    return img


if __name__ == "__main__":
    out = Path(__file__).resolve().parent / "assets" / "entry.png"
    img = build()
    img.save(out, format="PNG", optimize=True)
    print(f"wrote {out} {out.stat().st_size} bytes {img.size}")
