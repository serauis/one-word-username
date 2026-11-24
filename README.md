# One Word, One Username, One Reward

[![Bounty](https://img.shields.io/badge/bounty-make.fun-blue)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/serauis/one-word-username/blob/main/LICENSE)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://github.com/serauis/one-word-username)

An entry for the [make.fun bounty](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae) that asks for exactly one word: a username. One word is all a judge ever sees.

## Entry

The single word is our own make.fun username:

```
serauis
```

No explanation, no link, no pitch — just the username.

## How it works

Running `main.py` writes that word, with no trailing newline, to
`entry.txt` inside `$MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

The output file is exactly 7 bytes long — the word `serauis` and
nothing else, not even a newline.
