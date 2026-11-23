"""Front page of Sunday 22 November 2026, drawn with Pillow.

One page, one day: 38 dated stories of 22 Nov 2026 in a broadsheet
layout built to stay readable at a glance and at 300 px across.
Run it to (re)create entry.png beside this file.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 36
CW = W - 2 * MARGIN

PAPER = (248, 243, 230)
INK = (24, 24, 24)
FAINT = (104, 97, 83)
RED = (172, 32, 28)
NAVY = (28, 56, 94)
GOLD = (172, 124, 30)
SKY = (214, 226, 238)
SEA = (196, 216, 224)
SAND = (233, 224, 198)

REGION_COLOURS = {
    "EUROPE": (36, 84, 158),
    "MIDEAST": (14, 124, 110),
    "AFRICA": (200, 110, 26),
    "N.AMERICA": (44, 128, 60),
    "ASIA": (146, 50, 136),
    "WORLD": (110, 110, 110),
    "CYBER": (92, 72, 168),
}

FD = "/usr/share/fonts/truetype/dejavu/"
FL = "/usr/share/fonts/truetype/liberation/"


def serif_b(size):
    return ImageFont.truetype(FD + "DejaVuSerif-Bold.ttf", size)


def sans_b(size):
    return ImageFont.truetype(FL + "LiberationSans-Bold.ttf", size)


def sans(size):
    return ImageFont.truetype(FL + "LiberationSans-Regular.ttf", size)


def serif_i(size):
    return ImageFont.truetype(FL + "LiberationSerif-Italic.ttf", size)


def wrap(d, text, font, maxw):
    """Greedy word wrap: the lines of text that fit maxw."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def tracked(d, cx, y, text, font, tracking, fill):
    """Draw text centred at cx with extra letter spacing."""
    widths = [d.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        d.text((x, y), ch, font=font, fill=fill)
        x += w + tracking
    return total


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 6], fill=INK)
tracked(d, W // 2, 16, "THE WORLD IN ONE DAY", serif_b(54), 2, INK)
d.line([MARGIN, 84, W - MARGIN, 84], fill=INK, width=2)
d.text((MARGIN, 94), "22 NOVEMBER 2026", font=sans_b(56), fill=RED)
right1 = "SUNDAY"
right2 = "38 STORIES · 17 COUNTRIES"
d.text((W - MARGIN - d.textlength(right1, font=sans_b(20)), 100),
       right1, font=sans_b(20), fill=INK)
d.text((W - MARGIN - d.textlength(right2, font=sans_b(15)), 128),
       right2, font=sans_b(15), fill=NAVY)
d.line([MARGIN, 158, W - MARGIN, 158], fill=INK, width=1)

# ---------------------------------------------------------------- stat strip
STATS = [
    ("190+", "nations at COP31 in Antalya"),
    ("258", "House seats held by Democrats"),
    ("1.52M", "people in the KEPCO breach"),
    ("84,000", "9/11 records released in NYC"),
    ("$50.1B", "US transport funding request"),
]
sy = 166
colw = CW // len(STATS)
for i, (num, label) in enumerate(STATS):
    x = MARGIN + i * colw
    if i:
        d.line([x - 8, sy + 2, x - 8, sy + 40], fill=(205, 196, 172), width=1)
    d.text((x, sy), num, font=sans_b(29), fill=NAVY)
    for j, ln in enumerate(wrap(d, label, sans(11), colw - 16)[:1]):
        d.text((x, sy + 36), ln, font=sans(11), fill=FAINT)
d.line([MARGIN, 214, W - MARGIN, 214], fill=INK, width=1)

# ---------------------------------------------------------------- timeline
TIMELINE = [
    ("01:00", "AFRICA", "Khartoum drone hit"),
    ("05:30", "MIDEAST", "Tanker seized, Oman"),
    ("09:00", "EUROPE", "COP31 ends, no deal"),
    ("13:00", "N.AMERICA", "Arizona screwworm"),
    ("17:30", "CYBER", "SonicWall hack out"),
    ("21:00", "EUROPE", "Manchester gig shut"),
]
d.text((MARGIN, 222), "THE DAY IN UTC", font=sans_b(12), fill=INK)
line_y = 258
tl_x0, tl_x1 = MARGIN + 70, W - MARGIN - 70
d.line([tl_x0, line_y, tl_x1, line_y], fill=FAINT, width=2)
step = (tl_x1 - tl_x0) // (len(TIMELINE) - 1)
for i, (clock, region, label) in enumerate(TIMELINE):
    x = tl_x0 + i * step
    col = REGION_COLOURS[region]
    d.ellipse([x - 6, line_y - 6, x + 6, line_y + 6], fill=col)
    d.text((x, line_y - 16), clock, font=sans_b(11), fill=col, anchor="mm")
    anchor = "lm" if i == 0 else ("rm" if i == len(TIMELINE) - 1 else "mm")
    ly = line_y + 14 + (i % 2) * 14
    d.text((x, ly), label, font=sans(10), fill=INK, anchor=anchor)
d.line([MARGIN, 296, W - MARGIN, 296], fill=INK, width=2)

# ---------------------------------------------------------------- leads
LEADS = [
    {
        "kicker": "CLIMATE · ANTALYA, TÜRKIYE",
        "head": "COP31 ENDS WITH NO CLIMATE DEAL",
        "body": ("Over 190 nations left Antalya with no pact on fossil "
                 "fuels or climate finance. Guterres called the "
                 "result deeply disappointing."),
        "tag": "NO DEAL",
        "art": "globe",
    },
    {
        "kicker": "SECURITY · CHELM, POLAND",
        "head": "RUSSIAN MISSILE LANDS IN POLAND",
        "body": ("A Russian Kh-101 cruise missile struck near Chelm "
                 "during an allied exercise. Britain and France sent "
                 "jets; NATO weighed its response."),
        "tag": "NATO ON ALERT",
        "art": "missile",
    },
    {
        "kicker": "WAR AT SEA · BENGHAZI, LIBYA",
        "head": "RUSSIAN WARSHIP BURNS IN LIBYA",
        "body": ("An explosion wrecked the Russian corvette Merkury "
                 "at Benghazi base. Suspected Ukrainian sea drones "
                 "were blamed; a merchant ship was hit."),
        "tag": "CAUSE DISPUTED",
        "art": "ship",
    },
]


def art_globe(x, y, w, h):
    """COP31: a cracked globe over an Antalya minaret skyline."""
    d.rectangle([x, y, x + w, y + h], fill=SAND)
    cx, cy, r = x + w // 2, y + h // 2 - 4, 38
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(120, 170, 205))
    d.ellipse([cx - 29, cy - 25, cx - 8, cy - 8], fill=(96, 150, 92))
    d.ellipse([cx + 4, cy - 17, cx + 29, cy + 2], fill=(96, 150, 92))
    d.ellipse([cx - 15, cy + 8, cx + 11, cy + 28], fill=(96, 150, 92))
    d.line([cx - 25, cy - 28, cx - 8, cy - 11, cx + 3, cy - 19,
            cx - 2, cy - 2, cx + 11, cy + 13, cx + 5, cy + 27],
           fill=RED, width=4)
    for bx, bh in ((x + 18, 20), (x + 46, 30), (x + w - 60, 26),
                   (x + w - 34, 16)):
        d.rectangle([bx, y + h - bh, bx + 7, y + h], fill=INK)
        d.ellipse([bx - 1, y + h - bh - 7, bx + 8, y + h - bh + 2], fill=INK)
    d.line([x, y + h - 1, x + w, y + h - 1], fill=INK, width=2)


def art_missile(x, y, w, h):
    """A cruise missile streaks over fields; two jets climb to meet it."""
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    d.polygon([(x + 96, y + 56), (x + 172, y + 10), (x + 190, y + 23),
               (x + 114, y + 70)], fill=INK)
    d.polygon([(x + 172, y + 10), (x + 199, y + 4), (x + 190, y + 23)],
              fill=RED)
    d.polygon([(x + 100, y + 52), (x + 85, y + 65), (x + 102, y + 67)],
              fill=INK)
    for t in range(5):
        sx, sy2 = x + 88 - t * 15, y + 63 + t * 3
        d.ellipse([sx - 7, sy2 - 5, sx + 7, sy2 + 5], outline=FAINT, width=2)
    for jx, jy in ((x + 218, y + 52), (x + 246, y + 30)):
        d.polygon([(jx, jy), (jx + 26, jy + 6), (jx + 4, jy + 10)], fill=NAVY)
        d.polygon([(jx + 2, jy + 2), (jx - 8, jy + 12), (jx + 8, jy + 10)],
                  fill=NAVY)
    base = y + h - 11
    d.line([x, base, x + w, base], fill=INK, width=2)
    for gx in range(x + 12, x + w - 8, 30):
        d.line([gx, base, gx + 8, base - 8], fill=(96, 150, 92), width=3)


def art_ship(x, y, w, h):
    """A corvette burns at its berth; a sea drone marks the sky."""
    d.rectangle([x, y, x + w, y + h], fill=SEA)
    base = y + h - 30
    d.polygon([(x + 44, base), (x + w - 36, base), (x + w - 58, base + 15),
               (x + 60, base + 15)], fill=INK)
    d.rectangle([x + 118, base - 24, x + 198, base], fill=INK)
    d.rectangle([x + 146, base - 41, x + 174, base - 24], fill=INK)
    d.line([x + 160, base - 41, x + 160, base - 53], fill=INK, width=3)
    d.rectangle([x + 82, base - 13, x + 106, base], fill=INK)
    for fx, fh in ((x + 136, 26), (x + 158, 38), (x + 180, 23)):
        d.polygon([(fx - 9, base - 22), (fx + 9, base - 22),
                   (fx, base - 22 - fh)], fill=RED)
        d.polygon([(fx - 5, base - 22), (fx + 5, base - 22),
                   (fx, base - 22 - fh + 11)], fill=GOLD)
    for sx, sy2, sr in ((x + 172, y + 21, 12), (x + 195, y + 13, 15),
                        (x + 220, y + 8, 19)):
        d.ellipse([sx - sr, sy2 - sr // 2, sx + sr, sy2 + sr // 2],
                  outline=FAINT, width=2)
    dx, dy = x + w - 42, y + 18
    d.line([dx - 11, dy - 7, dx + 11, dy + 7], fill=RED, width=3)
    d.line([dx - 11, dy + 7, dx + 11, dy - 7], fill=RED, width=3)
    d.ellipse([dx - 4, dy - 4, dx + 4, dy + 4], fill=RED)
    for wx in range(x + 10, x + w - 16, 30):
        d.arc([wx, base + 16, wx + 18, base + 23], 0, 180, fill=NAVY, width=2)


ARTS = {"globe": art_globe, "missile": art_missile, "ship": art_ship}

lead_y, lead_h = 304, 230
lead_w = (CW - 24) // 3
for i, lead in enumerate(LEADS):
    x = MARGIN + i * (lead_w + 12)
    d.rectangle([x, lead_y, x + lead_w, lead_y + lead_h], outline=INK, width=2)
    ARTS[lead["art"]](x + 6, lead_y + 6, lead_w - 12, 88)
    ky = lead_y + 102
    d.text((x + 10, ky), lead["kicker"], font=sans_b(11), fill=RED)
    lines = wrap(d, lead["head"], sans_b(18), lead_w - 20)
    for j, ln in enumerate(lines):
        d.text((x + 10, ky + 18 + j * 20), ln, font=sans_b(18), fill=INK)
    by = ky + 18 + len(lines) * 20 + 4
    for ln in wrap(d, lead["body"], sans(12), lead_w - 20)[:3]:
        d.text((x + 10, by), ln, font=sans(12), fill=INK)
        by += 13
    tag = lead["tag"]
    tw = d.textlength(tag, font=sans_b(10)) + 12
    d.rectangle([x + 10, lead_y + lead_h - 26, x + 10 + tw,
                 lead_y + lead_h - 9], fill=INK)
    d.text((x + 16, lead_y + lead_h - 23), tag, font=sans_b(10), fill=PAPER)

# ---------------------------------------------------------------- the twelve
GRID = [
    ("ship", "IRAN SEIZES TANKER IN GULF OF OMAN", "Stena Imperative taken by force"),
    ("shield", "FBI PROBES HACK OF CRIME DATABASE", "US NCIC records system breached"),
    ("ballot", "DEMOCRATS REACH 258 HOUSE SEATS", "NC recount flips one more seat"),
    ("plane", "DELTA GLITCH SNARLS US FLIGHTS", "Atlanta hub hit, holiday rush on"),
    ("target", "MEXICO CAPTURES TOP-10 FUGITIVE", "'Chapo Isidro' held in Sinaloa"),
    ("globe", "DRONE HIT DAMAGES UN BUILDING", "Four killed in Khartoum, Sudan"),
    ("server", "NSA SECRET NETWORK GOES DOWN", "No sign of a cyberattack found"),
    ("rocket", "IRAN SHOWS TWIN-MISSILE LAUNCHER", "Display amid Hormuz blockade"),
    ("flame", "DRONE STRIKE HITS KYIV REGION", "3 killed, 30 hurt in Ukraine"),
    ("flag", "UN FORCE HANDS POSTS TO LEBANON", "UNIFIL pullout begins in south"),
    ("storm", "STORMS BATTER BOTH US COASTS", "Thanksgiving travel snarled"),
    ("drone", "RUSSIAN SHIP DRONED IN BALTIC", "NATO meets on Poland airspace"),
]


def icon(kind, x, y):
    """A bold 26x26 pictogram, top-left at x, y."""
    if kind == "ship":
        d.polygon([(x + 2, y + 16), (x + 24, y + 16), (x + 21, y + 23),
                   (x + 5, y + 23)], fill=NAVY)
        d.rectangle([x + 10, y + 8, x + 16, y + 16], fill=NAVY)
        d.line([x + 13, y + 2, x + 13, y + 8], fill=NAVY, width=2)
    elif kind == "shield":
        d.polygon([(x + 13, y + 2), (x + 23, y + 5), (x + 23, y + 13),
                   (x + 13, y + 24), (x + 3, y + 13), (x + 3, y + 5)],
                  outline=NAVY, width=2)
        d.line([x + 8, y + 13, x + 12, y + 17], fill=RED, width=2)
        d.line([x + 12, y + 17, x + 19, y + 8], fill=RED, width=2)
    elif kind == "ballot":
        d.rectangle([x + 4, y + 9, x + 22, y + 23], outline=NAVY, width=2)
        d.rectangle([x + 9, y + 3, x + 17, y + 9], fill=NAVY)
        d.line([x + 7, y + 16, x + 19, y + 16], fill=RED, width=2)
    elif kind == "plane":
        d.polygon([(x + 13, y + 2), (x + 16, y + 12), (x + 24, y + 18),
                   (x + 24, y + 21), (x + 16, y + 18), (x + 15, y + 24),
                   (x + 11, y + 24), (x + 10, y + 18), (x + 2, y + 21),
                   (x + 2, y + 18), (x + 10, y + 12)], fill=NAVY)
    elif kind == "target":
        d.ellipse([x + 3, y + 3, x + 23, y + 23], outline=RED, width=2)
        d.ellipse([x + 10, y + 10, x + 16, y + 16], fill=RED)
        d.line([x + 13, y, x + 13, y + 5], fill=RED, width=2)
        d.line([x + 13, y + 21, x + 13, y + 26], fill=RED, width=2)
    elif kind == "globe":
        d.ellipse([x + 3, y + 3, x + 23, y + 23], outline=NAVY, width=2)
        d.ellipse([x + 8, y + 3, x + 18, y + 23], outline=NAVY, width=1)
        d.line([x + 3, y + 13, x + 23, y + 13], fill=NAVY, width=1)
    elif kind == "server":
        for r in range(2):
            d.rectangle([x + 4, y + 3 + r * 11, x + 22, y + 12 + r * 11],
                        outline=NAVY, width=2)
            d.ellipse([x + 6, y + 6 + r * 11, x + 9, y + 9 + r * 11], fill=RED)
    elif kind == "rocket":
        d.polygon([(x + 13, y + 1), (x + 17, y + 7), (x + 17, y + 16),
                   (x + 9, y + 16), (x + 9, y + 7)], outline=NAVY, width=2)
        d.polygon([(x + 9, y + 13), (x + 4, y + 19), (x + 9, y + 18)],
                  fill=NAVY)
        d.polygon([(x + 17, y + 13), (x + 22, y + 19), (x + 17, y + 18)],
                  fill=NAVY)
        d.polygon([(x + 11, y + 18), (x + 15, y + 18), (x + 13, y + 25)],
                  fill=RED)
    elif kind == "flame":
        d.polygon([(x + 13, y + 1), (x + 18, y + 9), (x + 20, y + 15),
                   (x + 17, y + 23), (x + 9, y + 23), (x + 5, y + 15),
                   (x + 8, y + 8)], fill=RED)
        d.polygon([(x + 13, y + 11), (x + 16, y + 16), (x + 14, y + 22),
                   (x + 11, y + 22), (x + 10, y + 16)], fill=GOLD)
    elif kind == "flag":
        d.line([x + 6, y + 2, x + 6, y + 24], fill=NAVY, width=2)
        d.polygon([(x + 6, y + 3), (x + 22, y + 7), (x + 6, y + 11)],
                  fill=REGION_COLOURS["MIDEAST"])
    elif kind == "storm":
        d.arc([x + 2, y + 3, x + 17, y + 16], 90, 360, fill=NAVY, width=2)
        d.arc([x + 9, y + 2, x + 24, y + 15], 90, 360, fill=NAVY, width=2)
        d.line([x + 3, y + 14, x + 23, y + 14], fill=NAVY, width=2)
        d.polygon([(x + 13, y + 14), (x + 9, y + 20), (x + 13, y + 20),
                   (x + 11, y + 26), (x + 17, y + 18), (x + 13, y + 18)],
                  fill=GOLD)
    elif kind == "drone":
        d.line([x + 4, y + 4, x + 22, y + 22], fill=RED, width=2)
        d.line([x + 4, y + 22, x + 22, y + 4], fill=RED, width=2)
        for ex, ey in ((4, 4), (22, 4), (4, 22), (22, 22)):
            d.ellipse([x + ex - 3, y + ey - 3, x + ex + 3, y + ey + 3],
                      outline=RED, width=2)
        d.ellipse([x + 11, y + 11, x + 15, y + 15], fill=RED)


gh_y = lead_y + lead_h + 14
tracked(d, MARGIN + 130, gh_y, "THE DAY IN TWELVE", sans_b(17), 1, INK)
d.line([MARGIN, gh_y + 26, W - MARGIN, gh_y + 26], fill=INK, width=1)
cell_w, cell_h = CW // 4, 50
grid_y = gh_y + 34
for i, (kind, head, sub) in enumerate(GRID):
    cx = MARGIN + (i % 4) * cell_w
    cy = grid_y + (i // 4) * cell_h
    if i % 4:
        d.line([cx - 5, cy + 2, cx - 5, cy + cell_h - 8],
               fill=(205, 196, 172), width=1)
    icon(kind, cx + 2, cy + 3)
    tx = cx + 34
    lines = wrap(d, head, sans_b(12), cell_w - 40)
    for j, ln in enumerate(lines[:2]):
        d.text((tx, cy + 1 + j * 14), ln, font=sans_b(12), fill=INK)
    sy2 = cy + 1 + len(lines[:2]) * 14 + 2
    for ln in wrap(d, sub, sans(11), cell_w - 40)[:1]:
        d.text((tx, sy2), ln, font=sans(11), fill=FAINT)

# ---------------------------------------------------------------- map strip
map_y = grid_y + 3 * cell_h + 8
d.line([MARGIN, map_y, W - MARGIN, map_y], fill=INK, width=1)
d.text((MARGIN, map_y + 5), "WHERE IT HAPPENED", font=sans_b(11), fill=INK)
legend = ("Red pins: Washington · Mexico City · Chelm · Antalya · "
          "Benghazi · Hormuz · Khartoum · Seoul")
d.text((W - MARGIN - d.textlength(legend, font=sans(10)), map_y + 6),
       legend, font=sans(10), fill=FAINT)
LAND = [
    [(8, 26), (64, 98)],
    [(5, 30), (48, 55), (62, 99)],
    [(4, 33), (47, 60), (61, 99)],
    [(6, 34), (48, 61), (62, 97)],
    [(8, 33), (49, 60), (63, 95)],
    [(10, 31), (46, 63), (64, 92)],
    [(13, 29), (46, 64), (66, 90)],
    [(16, 27), (47, 64), (68, 88)],
    [(24, 33), (48, 63), (70, 84)],
    [(26, 36), (50, 62), (82, 91)],
    [(28, 37), (52, 60), (81, 92)],
    [(30, 36), (54, 58), (83, 90)],
]
PINS = [  # (col, row) on the dot grid
    (18, 3), (15, 6), (52, 2), (56, 3), (54, 5), (62, 4), (56, 7), (86, 3),
]
mx, my = MARGIN + 120, map_y + 18
for r, spans in enumerate(LAND):
    for c0, c1 in spans:
        for c in range(c0, c1 + 1):
            x, y = mx + c * 8, my + r * 5
            d.ellipse([x, y, x + 3, y + 3], fill=(178, 168, 140))
for c, r in PINS:
    x, y = mx + c * 8, my + r * 5
    d.ellipse([x - 4, y - 4, x + 5, y + 5], fill=RED)
    d.ellipse([x - 1, y - 1, x + 2, y + 2], fill=PAPER)

# ---------------------------------------------------------------- also on 22 nov
ALSO = [
    ("US", "Trump vows a 'permanent' Iran deal to bar a nuclear path"),
    ("US", "Trump backs a 10% cap on credit-card interest rates"),
    ("US", "Court: 2022 funding law passed without a House quorum"),
    ("US", "PhD student detained at Reagan National airport"),
    ("NYC", "Mamdani releases 84,000 more 9/11 records"),
    ("US", "ICE detains 121 people in a Memphis bar raid"),
    ("KOREA", "KEPCO data breach exposes 1.52 million people"),
    ("KOREA", "Exports more than double in November's first 20 days"),
    ("MARKETS", "Tech sell-off pushes US stocks into correction"),
    ("US", "Transport chief seeks $50.1B after flight outages"),
    ("US", "Virginia child dies of measles, the state's first of 2026"),
    ("US", "California prosecutors sue Newsom over death-row clemency"),
    ("US", "Georgia man charged over alleged ISIS money laundering"),
    ("TECH", "OpenAI's chief scientist urges shared limits on AI"),
    ("WORLD", "Guterres, in Barbados, calls for global AI rules"),
    ("LIBYA", "US signs aviation and rare-minerals deals with Libya"),
    ("ETHIOPIA", "Polio drive aims to protect 11 million children"),
    ("AFGHAN.", "Women sent back from Iran struggle to rebuild"),
    ("FOOTBALL", "Liverpool rout Manchester United 4-0"),
    ("MUSIC", "Ateez tops the Billboard 200 with 'Golden Hour: Part. 6'"),
]
also_y = my + len(LAND) * 5 + 12
d.line([MARGIN, also_y, W - MARGIN, also_y], fill=INK, width=2)
d.text((MARGIN, also_y + 6), "ALSO ON 22 NOV", font=sans_b(16), fill=INK)
d.text((MARGIN + 196, also_y + 9), "twenty more stories of the day",
       font=serif_i(12), fill=FAINT)
item_y = also_y + 32
col_w2 = CW // 2
for i, (tag, text) in enumerate(ALSO):
    cx = MARGIN + (i // 10) * col_w2
    cy = item_y + (i % 10) * 13
    d.text((cx, cy), tag, font=sans_b(9), fill=RED)
    tw = d.textlength(tag, font=sans_b(9))
    d.text((cx + tw + 5, cy), text, font=sans(11), fill=INK)

# ---------------------------------------------------------------- footer
foot_y = item_y + 10 * 13 + 6
d.line([MARGIN, foot_y, W - MARGIN, foot_y], fill=INK, width=2)
d.text((MARGIN, foot_y + 8),
       "DATE CHECK: every story on this page happened, or was first reported, on Sunday 22 November 2026.",
       font=sans_b(11), fill=INK)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size, "also_y", also_y, "foot_y", foot_y)
