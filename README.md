# 小六英文拼字 · p6english

Cute, colourful **Primary 6 English spelling game** for Hong Kong kids — mobile & iPad friendly.

**Live:** https://p6english.chanplanet.workers.dev/

## Features

- **每日 10 個字** — same words for everyone on the same Hong Kong calendar day (`Asia/Hong_Kong`)
- Each word hides **2–5 letters**; fill the blanks with an on-screen keyboard
- **8 hearts** · **繁體中文（香港）** · QWERTY · examples + exampleZh
- Gradient answer reveal · report-image (3/IP/day) · share card
- **Edge TTS** — word + example audio pre-generated with Microsoft `edge-tts` (`en-GB-SoniaNeural`) under `/audio/w/` and `/audio/e/` (no Cloudflare Workers AI at runtime)

## Vocabulary source (EDB honesty)

Hong Kong’s Education Bureau does **not** publish a separate Primary 6–only English wordlist. Official indicative targets are about **1,000 words by end of KS1** and **2,000 by end of primary (KS2)**. This app uses a **curated P6-appropriate pool** (~720 spelling words, length 5–14) aligned with EDB upper KS2 / end-of-primary themes (environment, science, society, school academic language, feelings, describing). Slightly harder / longer than the sibling P5 pool. **Not an official EDB dump**.

References: [EDB primary vocabulary](https://www.edb.gov.hk/en/curriculum-development/kla/eng-edu/references-resources/resource%20pri_vocab.html) · [Primary ELCG 2025](https://www.edb.gov.hk/attachment/en/curriculum-development/kla/eng-edu/Curriculum%20Document/Pri_ELCG_Primary_1-6_2025.pdf)

## Develop / Deploy

```bash
npm install
python3 -m venv .venv && .venv/bin/pip install edge-tts
.venv/bin/python scripts/generate_static_tts.py
npm run build && npx wrangler deploy
```

Daily seed key: `p6english-daily-YYYY-MM-DD`.
