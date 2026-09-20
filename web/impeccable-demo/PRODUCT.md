# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: developers and sysadmins who live in the terminal and resent alt-tabbing to Electron note apps. Specifically:

- Vim/Helix users who want notes with the same modal muscle memory.
- People burned by Notion/Obsidian sprawl who want *fewer* features, not more.
- Anyone who wants their notes to outlive the app — plain files, git-friendly.

The job: capture and revisit thoughts fast, without leaving the terminal or trusting a proprietary service.

## Product Purpose

Temple is a terminal note-taking app for people who think in plain text. Open it, write, close it. Notes are just Markdown files in a folder the user owns (`~/notes/*.md`). Success is measured by staying out of the way: under 200ms to first keystroke, no accounts, no daemon, no telemetry.

This landing page's purpose is to make a terminal-dweller trust the restraint and run the install command.

## Positioning

A deliberate counter-position to the "second brain" category (databases, backlinks, sync services, AI summaries, subscriptions). Temple's differentiator is subtraction: a quiet, single-purpose tool whose value is what it refuses to add. The name carries the metaphor — a place you *enter* to focus, with nothing on the walls. This is a stance a feature-maximizing competitor cannot truthfully copy without abandoning its own model.

## Operating Context

- Runs in the terminal as a single binary; no GUI, no browser, no online mode.
- Notes are ordinary Markdown files on disk, meant to be grepped, git-committed, and synced by whatever the user already uses (git, Syncthing, Dropbox).
- Modal (Vim-style) editing by default; optional plain-editor mode.
- Instant-capture usage patterns: `temple` opens today's daily note; `temple "buy milk"` appends a line without opening the UI.

## Capabilities and Constraints

Five features, held to five on purpose (restraint is the pitch):

1. Plain Markdown files — no database, no proprietary format.
2. Instant capture — daily note on launch; one-line append without opening the UI.
3. Fuzzy find across all notes' titles and content in milliseconds (`/`).
4. Modal editing — Vim-style keys out of the box, optional plain mode.
5. Zero config — single binary, no accounts, no daemon, no telemetry, works offline.

Deliberate non-features (stated openly as part of the pitch): no sync service, no backlinks graph, no plugins, no AI, no subscription.

Distribution facts: single binary; install via `brew install temple`, `cargo install temple`, or direct download. MIT-licensed, open source. Free.

Keyboard vocabulary worth preserving in UI: `n` new, `/` search, `d` delete, `t` today; movement `j/k`, `i` to write, `Esc` to leave, `q` to quit.

Vibe stats (illustrative, drawn from the brief): "1 binary · 0 dependencies · ~3 MB · <200ms to first keystroke."

## Brand Commitments

- **Name:** Temple. The "quiet room / place you enter to focus" metaphor is load-bearing.
- **Voice & tone:** short sentences, lowercase-comfortable, dry and a little wry, never salesy. States what it *doesn't* do as confidently as what it does. Reference point: the READMEs of good CLI tools, not SaaS marketing.
- **Tagline candidates** (not yet chosen): "Enter. Write. Leave." · "Notes, without the noise." · "A quiet room for your thoughts. In your terminal."

## Evidence on Hand

Temple is a **concept / demo** — it is not a shipping product. The landing page is the deliverable. This constrains what may appear as fact:

- **No real GitHub repository, star count, contributors, or user base exists.** Any social proof, star counts, or community numbers on the page are placeholders to be replaced before a real launch, and must not be presented as genuine metrics.
- **No real testimonials.** Any quotes are invented terminal-dweller personas and must read as illustrative, never as real endorsements.
- **Install commands and downloads are not live.** `brew install temple` / `cargo install temple` illustrate the intended experience; they do not resolve today.
- **Real source material:** [product-details/temple.md](product-details/temple.md) — the authored product brief, including feature copy, non-features, voice, and page-structure intent.

## Product Principles

1. **Subtraction is the feature.** Every "no" (no sync, no AI, no plugins, no subscription) is a selling point; never dilute the non-features to seem more capable.
2. **The page should feel like the app** — sparse, calm, fast. Restraint in the product implies restraint in the marketing.
3. **Trust through ownership.** Plain files in a folder you own, MIT, offline-by-default; lead with durability, not lock-in.
4. **Speak to terminal-dwellers as peers** — dry, precise, unhyped. The audience distrusts marketing gloss.
5. **Don't fabricate traction.** Proof stays honestly illustrative until it's real.

## Accessibility & Inclusion

Target WCAG 2.1 AA. The dark-by-default direction must still meet AA contrast for text and interactive elements; the page must be keyboard-navigable and respect `prefers-reduced-motion` for any cursor/typing animation.
