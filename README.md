# The World in One Page — Dense Tabloid, 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Tenguu0/news-image-20261124-v6-dense-tabloid/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Tenguu0/news-image-20261124-v6-dense-tabloid/reward.svg)](https://make.fun/bounty/news-image-20261124)

A make.fun entry for
[news-image-20261124](https://make.fun/bounty/news-image-20261124):
the whole world of Tuesday 24 November 2026 squeezed onto a single
newspaper front page, tabloid-dense. One big lead — Iran says it hit
two U.S. Patriot radars in Bahrain — above a packed two-column grid:
15 dead in the Kyiv region, the COP31 collapse, the ICJ's Myanmar
genocide verdict, the Xi–Trump–Putin trilateral ending with no deal,
Ukraine sinking a Russian warship off Libya, the U.S. naming
Venezuela's Cartel de los Soles a terrorist group, Bolsonaro back in
jail, and Trump's warning to Iran — plus an ALSO TODAY band (Alcaraz
wins the ATP Finals, Huang back at Nvidia, Lagarde resigns from the
ECB) and a ticker of four more stories. Sixteen stories on one page:
density over whitespace, every word still readable at full size.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

It writes `out/entry.png` (1024x1024 PNG). Python 3.12+, standard
library only — no network, no randomness, no clock, so every run
writes the same bytes.

## How it works

`entry.png` is drawn entirely in code by the builder script
(`build_page.py` in the work directory, PIL + DejaVu fonts): a
newsprint masthead, a big bold lead headline with an abstract
radar-sweep panel drawn from shapes (no borrowed photos), a dense
headline grid, an ALSO TODAY band, and a ticker strip. `main.py` is
the entry program: it copies the finished page to the output
directory. Every story on the page is a real event from 24 November
2026, cross-checked in at least two news sources; claims are hedged
as claims ("TEHRAN CLAIMS", "BAHRAIN SAYS").
