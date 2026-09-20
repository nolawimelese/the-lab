# Temple — product brief

## One-liner

**Temple is a terminal note-taking app for people who think in plain text.** Open it, write, close it. Your notes are just Markdown files in a folder you own.

## Positioning

The note-app market has drifted toward "second brains": databases, backlinks, sync services, AI summaries, subscriptions. Temple is the counter-position — a quiet, single-purpose tool that stays out of the way. The name carries the metaphor: a place you *enter* to focus, with nothing on the walls.

**Tagline candidates:**

- "Enter. Write. Leave."
- "Notes, without the noise."
- "A quiet room for your thoughts. In your terminal."

## Who it's for

- Developers and sysadmins who already live in the terminal and resent alt-tabbing to Electron
- Vim/Helix users who want notes with the same modal muscle memory
- People burned by Notion/Obsidian sprawl who want *fewer* features, not more
- Anyone who wants their notes to outlive the app (plain files, git-friendly)

## Core features

Keep it to five — the point is restraint.

1. **Plain Markdown files** — `~/notes/*.md`. No database, no proprietary format. Grep them, git them, sync them however you like.
2. **Instant capture** — `temple` opens today's daily note; `temple "buy milk"` appends a line without opening the UI at all.
3. **Fuzzy find everything** — `/` searches titles and content across all notes in milliseconds.
4. **Modal editing** — Vim-style keys out of the box (`j/k` to move, `i` to write, `Esc` to leave). Optional plain-editor mode for everyone else.
5. **Zero config** — single binary, no accounts, no daemon, no telemetry. Works offline because there is no "online."

## Deliberate non-features

Worth stating on the page — it's part of the pitch.

- No sync service (use git, Syncthing, Dropbox — your call)
- No backlinks graph
- No plugins
- No AI
- No subscription

## How it works

The "3 steps" section.

1. `brew install temple` / `cargo install temple` / single binary download
2. `temple` — you're writing within 200ms
3. `Esc` `q` — your note is already saved

## Details that give the page texture

- **Install command** with copy-to-clipboard (`brew install temple`)
- **A terminal mockup** in the hero: a two-pane TUI — note list on the left, editor on the right, a `/` search bar at the bottom, one soft accent color for the cursor line
- **Keyboard cheatsheet** as a feature block (`n` new, `/` search, `d` delete, `t` today) — keycaps make a nice visual rhythm
- **Stats that fit the vibe:** "1 binary · 0 dependencies · ~3 MB · <200ms to first keystroke"
- **Open source** — MIT, link to GitHub, "star count" as social proof instead of testimonials (or 2–3 short quotes from fictional terminal-dwellers)
- **Pricing:** free. A single "It's free. It's yours." block, optionally with a "buy me a coffee" link

## Voice & tone

Short sentences. Lowercase-comfortable. Dry, a little wry, never salesy. Says what it *doesn't* do as confidently as what it does. Think the READMEs of good CLI tools, not SaaS marketing.

## Visual direction

Starting point for `/impeccable`.

- **Dark by default**, near-black background with warm off-white text — a terminal, not a "dark mode"
- **One accent color** (amber or muted green) used sparingly: cursor, active line, primary CTA
- **Monospace for the product, a humanist sans for the prose** — the contrast between the two is the whole typographic system
- Generous whitespace; the page itself should feel like the app: sparse, calm, fast
- Subtle motion only: a blinking cursor in the hero, maybe a typed-in command on load

## Page structure

1. Nav (logo, GitHub, Install)
2. Hero — tagline, one-line pitch, install command, terminal mockup
3. "What it does" — five features
4. "What it doesn't do" — the non-features list (the memorable section)
5. How it works — three steps
6. Keyboard cheatsheet
7. Community / open source — stars, contributors, a quote or two
8. Final CTA — install command again, footer
