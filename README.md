[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/epanpai/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/epanpai/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

# The World in One Day — Thursday, 26 November 2026

My entry for the make.fun bounty
[news-image-20261126](https://make.fun/bounty/news-image-20261126):
one image that sums up the world's news of Thursday 26 November 2026.

## The image

A newspaper front page, drawn from scratch with Pillow
(`gen_image.py`, no photo and no download):

- **Lead — North Korea:** Kim Jong Un inspects nuclear sites and
  orders a wider deployment of tactical nuclear weapons, calling the
  North's status as a nuclear-weapons state "absolutely inviolable".
- **Space:** Pakistan's first astronaut, Muhammad Zeeshan Ali, joins
  China's Tiangong station aboard Shenzhou-24.
- **Trade war:** the US unveils new tariffs on 14 trading partners;
  China is hit hardest, Taiwan faces 15%, and markets slide.
- **Ukraine:** a strike on a Russian air base damages five planes.
- **Science:** the first close-ups of the asteroid deliberately
  struck to test Earth's defences.
- **Work:** Bangladesh raises garment workers' minimum wage by 36%.
- **Also today:** Colombia marks 10 years since its peace deal,
  Lebanon plans a second international airport, North Korea tells
  Switzerland to shut its Pyongyang office, Russia's own figures put
  its Ukraine war losses near 500,000, Gukesh faces Sindarov for the
  world chess crown, and India marks Constitution Day.

## How it runs

`main.py` (Python 3.13, standard library only) validates
`assets/entry.png` — PNG signature, every chunk's CRC, size and
dimensions — then copies it to `/output/entry.png` and verifies the
copy is byte-identical. No network, no randomness — two runs write the
same bytes.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`gen_image.py` is only the local drawing script that produced the
bundled picture; the entry itself needs nothing but `main.py` and
`assets/entry.png`.

## Files

- `main.py` — the entry program
- `assets/entry.png` — the front page, 1024×1024, 114,758 bytes
- `gen_image.py` — the script that drew the front page
- `BUILD_LOG.md` — how this entry was built
- `LICENSE` — MIT
