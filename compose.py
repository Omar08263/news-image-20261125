#!/usr/bin/env python3
"""Compose the news-image-20261125 poster: one 1024x1024 PNG summing up
Wednesday 25 November 2026, drawn from scratch with PIL (no network,
no downloaded images, no timestamps) so every run writes identical bytes.

Stories (each verified against two primary sources, all dated 25 Nov 2026):
  1. Australia & Solomon Islands sign a security pact (Reuters, SYDNEY
     Nov 25; The Straits Times, Nov 25; ABC News, 25 Nov).
  2. Japan's services inflation hits a 36-year high: +4.2% in October,
     fastest since 1990 (Reuters, TOKYO Nov 25; Bank of Japan SPPI
     release list: October 2026 data released Nov. 25, 2026).
  3. Putin meets Brunei's Sultan Hassanal Bolkiah in Moscow (Kremlin
     announcement, talks on 25 Nov; TASS, MOSCOW November 25).
"""
import hashlib
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (16, 38, 63)
GOLD = (201, 162, 39)
PAPER = (251, 248, 241)
INK = (24, 32, 44)
GREY = (84, 94, 108)
CARD = (255, 255, 255)
BORDER = (214, 206, 190)
TEAL = (14, 116, 110)
AMBER = (180, 110, 8)
SLATE = (71, 85, 105)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_shield(d, cx, cy, r, color):
    pts = [
        (cx, cy - r),
        (cx + r * 0.85, cy - r * 0.45),
        (cx + r * 0.85, cy + r * 0.25),
        (cx, cy + r),
        (cx - r * 0.85, cy + r * 0.25),
        (cx - r * 0.85, cy - r * 0.45),
    ]
    d.polygon(pts, fill=color)
    d.line([(cx - r * 0.45, cy), (cx - r * 0.1, cy + r * 0.35),
            (cx + r * 0.5, cy - r * 0.35)], fill=(255, 255, 255), width=9)


def draw_chart(d, cx, cy, r, color):
    x0, y0, x1, y1 = cx - r, cy - r, cx + r, cy + r
    bars = [0.35, 0.55, 0.7, 1.0]
    bw = (x1 - x0) // 6
    for i, f in enumerate(bars):
        bx = x0 + i * (bw + 8)
        bh = int((y1 - y0) * f)
        d.rectangle([bx, y1 - bh, bx + bw, y1], fill=color)
    d.line([(x0 + 4, y1 - int((y1 - y0) * 0.32)),
            (x1 - 6, y0 + 14)], fill=(255, 255, 255), width=7)
    # arrowhead at the top-right end of the trend line
    ax, ay = x1 - 6, y0 + 14
    d.polygon([(ax, ay), (ax - 20, ay + 2), (ax - 4, ay + 20)],
              fill=(255, 255, 255))


def draw_globe(d, cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=7)
    d.ellipse([cx - int(r * 0.45), cy - r, cx + int(r * 0.45), cy + r],
              outline=color, width=5)
    d.line([(cx - r, cy), (cx + r, cy)], fill=color, width=5)
    d.line([(cx - int(r * 0.85), cy - int(r * 0.55)),
            (cx + int(r * 0.85), cy - int(r * 0.55))], fill=color, width=4)
    d.line([(cx - int(r * 0.85), cy + int(r * 0.55)),
            (cx + int(r * 0.85), cy + int(r * 0.55))], fill=color, width=4)


def panel(d, y0, y1, accent, kicker, headline, sub, icon):
    d.rounded_rectangle([36, y0, 988, y1], radius=18, fill=CARD,
                        outline=BORDER, width=2)
    d.rounded_rectangle([36, y0, 52, y1], radius=9, fill=accent)
    tx = 84
    d.text((tx, y0 + 22), kicker, font=font(BOLD, 23), fill=accent)
    hf = font(BOLD, 40)
    lines = wrap(d, headline, hf, 700)
    ly = y0 + 58
    for ln in lines:
        d.text((tx, ly), ln, font=hf, fill=INK)
        ly += 48
    sf = font(REG, 23)
    slines = wrap(d, sub, sf, 700)
    for ln in slines:
        d.text((tx, ly + 4), ln, font=sf, fill=GREY)
        ly += 31
    icon(d, 905, (y0 + y1) // 2, 62, accent)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # Masthead
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.text((512, 26), "THE WORLD IN ONE IMAGE", font=font(BOLD, 30),
           fill=(255, 255, 255), anchor="ma")
    d.text((512, 66), "WEDNESDAY, 25 NOVEMBER 2026", font=font(BOLD, 52),
           fill=(255, 255, 255), anchor="ma")
    d.rectangle([0, 148, W, 154], fill=GOLD)

    panel(d, 172, 424, TEAL, "PACIFIC  ·  SECURITY",
          "Australia and Solomon Islands sign security pact",
          "Canberra becomes Honiara's defence partner of choice as the "
          "Solomons ends its 2022 security deal with China. — Reuters, 25 Nov",
          draw_shield)
    panel(d, 440, 692, AMBER, "JAPAN  ·  ECONOMY",
          "Japan's services inflation hits a 36-year high",
          "Prices charged by service firms rose 4.2% in October — the "
          "fastest since 1990, Bank of Japan data show. — Reuters / BOJ, 25 Nov",
          draw_chart)
    panel(d, 708, 936, SLATE, "MOSCOW  ·  DIPLOMACY",
          "Putin meets Brunei's Sultan in Moscow",
          "Hassanal Bolkiah on a state visit; talks on Russia–Brunei ties "
          "and a joint declaration. — Kremlin / TASS, 25 Nov",
          draw_globe)

    d.line([(36, 958), (988, 958)], fill=BORDER, width=2)
    d.text((512, 970), "All events took place or were first reported on "
           "Wednesday, 25 November 2026.",
           font=font(REG, 20), fill=GREY, anchor="ma")
    d.text((512, 994), "Sources: Reuters · The Straits Times · Bank of Japan "
           "· Kremlin · TASS",
           font=font(REG, 19), fill=GREY, anchor="ma")
    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png",
          hashlib.sha256(open("entry.png", "rb").read()).hexdigest())


if __name__ == "__main__":
    main()
