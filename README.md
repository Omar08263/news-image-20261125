# Wednesday, 25 November 2026 — The Day in News

One image summing up the world's news of Wednesday 25 November 2026,
built for the make.fun competition
[`news-image-20261125`](https://make.fun/bounty/news-image-20261125).

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Omar08263/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Omar08263/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

## The poster

- **Pacific — Security:** Australia and Solomon Islands sign a security
  pact; Canberra becomes Honiara's defence partner of choice as the
  Solomons ends its 2022 security deal with China (Reuters, SYDNEY
  Nov 25; The Straits Times, 25 Nov; ABC News, 25 Nov).
- **Japan — Economy:** Japan's services inflation hits a 36-year high;
  prices charged by service firms rose 4.2% in October, the fastest
  since 1990 (Reuters, TOKYO Nov 25; Bank of Japan SPPI release list:
  October 2026 data released Nov. 25, 2026).
- **Moscow — Diplomacy:** Putin meets Brunei's Sultan Hassanal Bolkiah
  in Moscow on a state visit; talks on Russia–Brunei ties and a joint
  declaration (Kremlin announcement, talks on 25 Nov; TASS, MOSCOW
  November 25).

Every story on the poster took place, or was first reported, on
Wednesday 25 November 2026. Stories the morning digests date
25 November but which happened on 24 November were checked and left
out: Huawei's US conviction (Nov 24), the CAS ruling reinstating
Senegal as AFCON winners (Nov 24), Nvidia CEO Jensen Huang's apology
to staff (Nov 24), and Dell's Q3 results (press release Nov 24,
4:05pm EST).

## How it is built

`entry.png` (1024×1024 PNG, 117,279 bytes) is drawn from scratch by
`compose.py` (Python + PIL, DejaVu Sans): masthead with the full date,
three story panels with flat icons, and a footer naming the sources.
Two runs of `compose.py` write byte-identical files (sha256
`68eb2aa1ff2daf3a53af47515e9576032c56d24bf3cb89911a992935fe074b54`).
`main.ts` (Node 22, standard library only) checks the poster is a
whole 1024×1024 PNG under 1 MiB with an IEND chunk, then copies
`entry.png` to the output directory byte for byte, so both graded
runs write identical bytes. No network is used at run time.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
