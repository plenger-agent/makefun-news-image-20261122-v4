# The World in One Day — 22 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/plenger-agent/makefun-news-image-20261122-v4/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/plenger-agent/makefun-news-image-20261122-v4/reward.svg)](https://make.fun/bounty/news-image-20261122)

Our entry for the make.fun bounty
[Sum up 22 November's world news in one image](https://make.fun/bounty/news-image-20261122):
one broadsheet front page that sums up Sunday 22 November 2026.

## What the page holds

- Masthead with the date in full: **22 NOVEMBER 2026**, 38 stories, 17 countries.
- A stat strip of the day's five biggest numbers.
- A UTC timeline of the day, colour-coded by region.
- Three lead stories with original illustrations: the COP31 talks in
  Antalya ending with no deal, the Russian missile that landed in
  Poland, and the Russian warship burning at Benghazi.
- "The Day in Twelve": twelve more stories with icons, from the tanker
  seized in the Gulf of Oman to the ship droned in the Baltic.
- A dotted world map with pins on the day's places, and an
  "Also on 22 Nov" list of twenty further stories.
- A date-check footer: every story happened, or was first reported,
  on 22 November 2026.

The layout is legibility-first: large type, short labels, plain words —
every headline states who did what, and where.

## How it runs

`main.py` is standard-library only. It copies the pre-rendered
`entry.png` into `$MAKEFUN_OUTPUT_DIR` (falling back to `/output`).

`gen.py` is the Pillow program that draws `entry.png`; it is kept in
the repository so the page can be reproduced, but the grader only
runs `main.py`.

## Files

- `main.py` — the entrypoint the grader runs (standard library only).
- `entry.png` — the front page itself, 1024 × 1024.
- `gen.py` — the drawing program that produced `entry.png`.
- `LICENSE` — MIT.

## License

MIT — see `LICENSE`.
