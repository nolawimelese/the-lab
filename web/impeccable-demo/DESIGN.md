---
name: Temple
description: The card catalog that "second brain" databases replaced — restraint is the product.
colors:
  oak: "#1e1712"
  oak-2: "#261d16"
  oak-3: "#322619"
  oak-line: "#3d2f20"
  manila: "#e7d8b6"
  manila-2: "#dccba4"
  manila-edge: "#cbb98f"
  ink: "#26201a"
  ink-soft: "#5a4f42"
  ink-faint: "#665a4b"
  paper: "#ecdfc2"
  paper-soft: "#c3b092"
  paper-faint: "#a3927a"
  stamp: "#a63a50"
  stamp-ink: "#9a3145"
  stamp-bright: "#c65068"
  brass: "#b08d57"
  brass-dim: "#8a6d40"
  rule-blue: "#7089a8"
  rule-red: "#c07a72"
  scrim-soft: "rgba(0,0,0,0.35)"
  scrim-mid: "rgba(0,0,0,0.5)"
  scrim-deep: "rgba(0,0,0,0.8)"
typography:
  # Enumerated ramp recorded from the shipped build. Heading sizes live in the
  # named roles below; this map records the body/command band and the small
  # mono label-caption band (steps ~0.68–1.02rem) the interface uses for tabs,
  # stamps, keycaps, metadata and disclaimers, plus the 18/16px root steps.
  scale:
    root: "18px"
    root-sm: "16px"
    numeral: "2.4rem"
    wordmark: "1.4rem"
    title-lg: "1.18rem"
    title: "1.14rem"
    command-md-a: "1.12rem"
    command-md-b: "1.1rem"
    command-md-c: "1.08rem"
    command-md-d: "1.06rem"
    command-md-e: "1.02rem"
    body: "1rem"
    label-98: "0.98rem"
    label-96: "0.96rem"
    label-92: "0.92rem"
    label-90: "0.9rem"
    label-88: "0.88rem"
    label-86: "0.86rem"
    label-84: "0.84rem"
    label-82: "0.82rem"
    label-80: "0.8rem"
    label-78: "0.78rem"
    label-76: "0.76rem"
    label-74: "0.74rem"
    label-72: "0.72rem"
    label-70: "0.7rem"
    label-68: "0.68rem"
  display:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "clamp(2.7rem, 7.2vw, 5.3rem)"
    fontWeight: 700
    lineHeight: 0.98
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "clamp(1.9rem, 3.6vw, 2.9rem)"
    fontWeight: 700
    lineHeight: 1.06
    letterSpacing: "-0.01em"
  title-cta:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "clamp(2.1rem, 4.5vw, 3.2rem)"
    fontWeight: 700
    lineHeight: 1.06
  numeral:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "2.4rem"
    fontWeight: 700
    lineHeight: 1
  wordmark:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "1.4rem"
    fontWeight: 700
    letterSpacing: "0.36em"
  title-lg:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "1.18rem"
    fontWeight: 700
    lineHeight: 1.15
  title:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "1.14rem"
    fontWeight: 700
    lineHeight: 1.15
  command-lg:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "1.1rem"
    fontWeight: 700
    lineHeight: 1.5
  command:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "1.06rem"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Public Sans, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
  caption:
    fontFamily: "Public Sans, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: "0.96rem"
    fontWeight: 400
    lineHeight: 1.5
  label-lg:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "0.88rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.09em"
  meta:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "0.84rem"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.04em"
  label:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "0.8rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.14em"
  label-sm:
    fontFamily: "Courier Prime, ui-monospace, 'Courier New', monospace"
    fontSize: "0.68rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.12em"
rounded:
  stamp: "2px"
  card: "3px"
  tab: "4px"
  pill: "8px"
spacing:
  xs: "4px"
  sm: "10px"
  md: "16px"
  lg: "24px"
  xl: "48px"
  section: "96px"
components:
  button-primary:
    backgroundColor: "{colors.stamp}"
    textColor: "{colors.manila}"
    typography: "{typography.command}"
    rounded: "{rounded.stamp}"
    padding: "0 20px"
  button-primary-hover:
    backgroundColor: "{colors.stamp-ink}"
    textColor: "{colors.manila}"
  nav-cta:
    backgroundColor: "transparent"
    textColor: "{colors.stamp-bright}"
    rounded: "{rounded.stamp}"
    padding: "7px 16px"
  nav-cta-hover:
    backgroundColor: "{colors.stamp}"
    textColor: "{colors.manila}"
  card:
    backgroundColor: "{colors.manila}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "40px 48px 72px"
  install-line:
    backgroundColor: "rgba(38, 32, 26, 0.06)"
    textColor: "{colors.ink}"
    typography: "{typography.command}"
    rounded: "{rounded.stamp}"
    padding: "14px 16px"
  datestamp:
    backgroundColor: "transparent"
    textColor: "{colors.stamp-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.card}"
    padding: "7px 13px"
---

# Design System: Temple

## Overview

**Creative North Star: "The Catalog Room"**

Temple is a terminal note-taking app dressed as a library card catalog: a warm, dim wooden drawer room where every content plane is a glowing manila index card and the only ink that raises its voice is an oxblood rubber stamp. The system exists to prove a thesis by restraint — it deliberately refuses the near-black terminal-window mockup with a single neon accent that every dev tool and AI-generated page ships. Where that anti-reference is cold, screen-lit, and monospaced-all-the-way-down, Temple is warm, paper-lit, and quiet. The product's promise (your plain files outlive the app) is carried by the material itself: cards look older and more durable than software.

Density is generous and physical. Cards sit at slight rotations, cast soft warm shadows onto the oak, and are threaded with brass rod hardware and drawer tabs. Nothing is pure flat design and nothing is glassy; every surface reads as a real object under pooled tungsten light. The mono voice (Courier Prime) is reserved for anything typed, stamped, filed, or commanded — headlines, labels, install commands, catalog numbers — while a humanist sans (Public Sans) carries readable prose. That split is the grammar: mono is the machine and the archive; sans is the human explaining.

The accent discipline is the whole point. Oxblood stamp ink appears only where a real rubber stamp would land — the headline, the primary action, date-stamp specs, "withdrawn" marks — and never as a general-purpose highlight. Warmth, ruled card lines, and brass hardware do the decorative work so the accent can stay rare.

**Key Characteristics:**
- Warm dark oak ground, never near-black; every surface is a lit paper object.
- Manila index cards as the universal container, faintly rotated and softly shadowed.
- A single oxblood accent, spent only where a stamp would physically fall.
- Two-voice type: Courier Prime for typed/stamped/filed voices, Public Sans for prose.
- Diegetic library hardware — drawer tabs, punched holes, brass rod, keycaps, date stamps.

## Colors

A warm archival palette built from three material families — oak (the room), manila (the cards), and oxblood (the ink) — with brass and ruled-line supporting hues. No cool greys and no pure black anywhere.

### Primary
- **Oxblood Stamp Ink** (`#a63a50`, deepened to `#9a3145` for pressed ink, brightened to `#c65068` for focus rings and CTA labels): The sole accent. Used only where a rubber stamp lands — the stamped headline, the copy button, date-stamp spec chips, "withdrawn" marks, prompts, and section links. `stamp-wash` (`rgba(166,58,80,0.12)`) tints feature entry chips.

### Neutral
- **Deep Warm Oak** (`#1e1712`, with `#261d16` / `#322619` layering steps and `#3d2f20` hairlines): The ground — body background, dark section bands, footer drawer front, and all borders on dark surfaces. The room, never a screen.
- **Glowing Manila** (`#e7d8b6`, aged variant `#dccba4`, edge `#cbb98f`): The card stock. Every content container. The aged variant backs "withdrawn" non-feature cards.
- **Card Ink** (`#26201a`, soft `#5a4f42`, faint `#665a4b`): Text on manila. Ink for headings and commands, soft for body prose, faint for small mono labels (holds AA ~4.8:1 on manila).
- **Paper on Oak** (`#ecdfc2`, soft `#c3b092`, faint `#a3927a`): Text on the dark ground — nav, section titles/subs on dark bands, footer, honesty copy (faint holds AA ~5.9:1 on oak).

### Tertiary (hardware & ruled lines)
- **Brass** (`#b08d57`, dim `#8a6d40`): Rod through the punched hole, drawer pull, nav mark glyph, link underlines. The only metal.
- **Ruled Blue** (`#7089a8`) and **Ruled Red** (`#c07a72`): Notebook rule lines — blue baseline rules and the install line's underline; red the header rule across cards. Structural, never text.

### Elevation Scrims (recorded from the shipped build)
These are not palette hues; they are the neutral black alphas the shadow vocabulary composites with, recorded here so the elevation system reads as documented tokens rather than off-palette literals. Used only inside `box-shadow` drop layers, never as fills or text.
- **Scrim Soft** (`rgba(0,0,0,0.35)`): Brass-rod and hover-drop softening.
- **Scrim Mid** (`rgba(0,0,0,0.5)`): Standard card/tab drop and hole inset.
- **Scrim Deep** (`rgba(0,0,0,0.8)`): Deepest footer drawer-label drop.

### Named Rules
**The One Stamp Rule.** Oxblood is spent only where a physical rubber stamp would land — a headline, a stamped spec, a "declined" mark, the one primary button. It is never a generic highlight, hover fill for prose links, or decorative tint. Its rarity is what makes it read as ink.

**The No-Near-Black Rule.** The darkest *surface* is warm oak (`#1e1712`), never `#000` or a blue-black terminal grey. Pure-black alphas appear only inside shadow scrims (above), never as a fill, ground, or text color. If a surface looks like an unlit screen, it is wrong for this world.

## Typography

**Display / Label / Mono Font:** Courier Prime (with `ui-monospace, 'Courier New', Consolas, monospace`)
**Body Font:** Public Sans (with `system-ui, 'Segoe UI', Roboto, sans-serif`)

**Character:** A typewriter mono doing the work of a headline face is the signature — Courier Prime stamped large reads as a rubber-stamped catalog entry, not a code block. Public Sans keeps explanatory prose plain and legible so the mono never has to be read in paragraphs.

### Hierarchy
- **Display** (Courier Prime 700, `clamp(2.7rem, 7.2vw, 5.3rem)`, line-height 0.98, letter-spacing -0.02em): The one hero headline, rubber-stamped in oxblood with per-word rotation and a faint multiply text-shadow.
- **Headline** (Courier Prime 700, `clamp(1.9rem, 3.6vw, 2.9rem)`, line-height 1.06): Section titles ("What it does", "Borrower's slips").
- **CTA Title** (Courier Prime 700, `clamp(2.1rem, 4.5vw, 3.2rem)`, line-height 1.06): The final call-to-action headline; a hair smaller than Display, larger than section Headlines.
- **Numeral** (Courier Prime 700, 2.4rem, line-height 1): The oversized step numbers (01 / 02 / 03) in manila-edge tint.
- **Wordmark** (Courier Prime 700, 1.4rem, letter-spacing 0.36em): The engraved footer drawer-label "TEMPLE".
- **Title** (Courier Prime 700, 1.14–1.18rem, line-height 1.15): Feature card titles (1.14rem) and non-feature card titles (1.18rem, `title-lg`).
- **Command** (Courier Prime, 1.06rem regular for typed install lines; 1.1rem 700 `command-lg` for step commands): oxblood `$` prompt, ink command text.
- **Body** (Public Sans 400, 1rem on an 18px root / 16px under 720px, line-height 1.55–1.6): Ledes, quotes. Ledes cap at ~46ch, section subs at ~52ch.
- **Caption** (Public Sans 400, 0.96rem, line-height 1.5): Feature and non-feature card body copy.
- **Label** (Courier Prime 700, uppercase, tracked): the small mono label band — see Recorded Type Scale.

### Recorded Type Scale (from the shipped build)
Every mono/prose size the page actually ships, recorded so none reads as off-ramp. All are legitimate documented steps; the label/caption band clusters tightly on purpose because stamped labels come in many small physical sizes.

- **Display / heading band (rem):** 5.3 (display max), 3.2 & 2.1 (CTA title clamp endpoints, `clamp(2.1rem, 4.5vw, 3.2rem)`), 2.9 & 1.9 (headline clamp endpoints), 2.4 (step numeral), 1.4 (footer wordmark), 1.18 (non-feature title), 1.14 (feature title).
- **Command / body band (rem):** 1.12 (hero lede), 1.1 (step command), 1.08 (CTA lede / section sub), 1.06 (install line), 1.0 (body root).
- **Label / caption band (rem):** 0.98, 0.96 (card body), 0.92, 0.9 (copy button), 0.88 (date-stamp), 0.86, 0.84 (meta), 0.82, 0.8, 0.78, 0.76, 0.74, 0.72, 0.68 (catalog number). Mono here is uppercase, weight 700, letter-spacing 0.09em–0.36em.

### Named Rules
**The Two-Voice Rule.** Courier Prime carries anything typed, stamped, filed, or commanded (headlines, labels, catalog numbers, install lines). Public Sans carries anything a human reads as prose. Never set a paragraph in mono; never set a stamp or command in sans.

**The Widely-Tracked-Caps Rule.** Mono labels are uppercase with generous letter-spacing (0.09em–0.36em, widest on wordmarks). This is how a typed label reads as "stamped on a card" rather than as UI chrome.

## Layout

Centered single-column reading measure inside a 1180px max-width container, gutters of 24px (18px under 720px). Vertical rhythm is a 96px section pad (68px under 720px). The spacing scale in use runs roughly 4 / 10 / 16 / 24 / 48px. Sections alternate between the plain oak ground and darker inset bands (`section--dark`, oak-2 with a top radial glow and hairline borders top and bottom) to pace the page like drawers in a cabinet.

Multi-card zones are explicit grids: features are a 5-column "tray" (5 held on purpose), non-features an `auto-fit minmax(230px)` stack, steps and voices 3-column, the cheatsheet a 2-column definition grid. Responsive collapse is staged: the tray goes `auto-fit minmax(200px)` at 1080px, voices/steps/cheat drop to one column at 900px, and at 720px everything stacks to a single column, all card rotations flatten, and the install command goes vertical.

## Elevation & Depth

A physical, warm-shadow system — the opposite of flat design. Depth is conveyed by real object cues: soft directional drop shadows on manila cards, an inset top highlight simulating lit paper edges, an inset shadow inside the punched hole, and a sticky nav with a blurred oak backdrop. Shadows are warm and low-contrast (tinted with `manila-shadow` `rgba(10,6,2,0.55)` and the neutral scrim alphas recorded in Colors), never a hard neutral wall of black. Layering also uses tonal oak steps (oak → oak-2 → oak-3) for section bands and the footer.

### Shadow Vocabulary
- **Card at rest** (`box-shadow: 0 1px 0 rgba(255,250,235,0.5) inset, 0 18px 34px -20px var(--manila-shadow), 0 3px 8px -4px rgba(0,0,0,0.4)`): Every manila card. Inset highlight = lit top edge; the two drops = paper lifted off oak.
- **Card on hover** (`0 30px 44px -22px var(--manila-shadow), 0 6px 12px -6px scrim-soft` + inset highlight): Feature cards lift and rotate to level on hover.
- **Keycap** (`0 1px 0 rgba(255,252,242,0.9) inset, 0 2px 0 var(--manila-edge), 0 3px 4px -2px scrim-soft`): A hard 2px offset base plus soft drop — a pressable physical key. A skeuomorphic material cue, not a decorative offset shadow.
- **Brass rod / hole inset** (uses `scrim-soft` and `scrim-mid`): The rod carries a `scrim-soft` drop; the punched hole an inset `rgba(0,0,0,0.7)` well.
- **Footer drawer label** (`0 14px 30px -20px scrim-deep`): The deepest drop on the page — the engraved oak plate reads as recessed into the drawer front.

### Named Rules
**The Lit-Paper Rule.** Every card carries the inset top highlight plus a warm double drop. Cards are objects resting on wood; they are never flat fills and never cast a cold grey shadow. The neutral scrim alphas (`0.35 / 0.5 / 0.8`) are shadow-only tokens — soft for hover and hardware, mid for standard drops and the hole well, deep for the footer plate.

## Shapes

Small, restrained radii throughout — this is paper and hardware, not soft plastic. Cards are 3px (`--card-radius`), stamps/buttons/install lines 2px, drawer tabs and keycaps 4px, and the brass drawer-pull pill is 8px (`rounded.pill`, the single largest radius, reserved for the rounded metal hardware). Brass rod is 3px; the punched hole is a full circle. The signature geometry is subtle rotation: cards, stamps, and date chips sit at fractional degrees (-2.4deg to +2.2deg) so the surface reads as hand-filed, all flattening to 0 under 720px. Borders are hairline and material-matched: `manila-edge` on cards, `oak-line` on dark surfaces, ruled red/blue lines for notebook structure, dashed manila for spec dividers, dashed oxblood for feature-entry chips.

## Components

### Buttons
- **Shape:** Sharp, near-square (2px radius).
- **Primary (copy / install):** Oxblood `stamp` fill, manila text, `stamp-ink` border, mono 0.9rem, padding `0 20px`. On success it swaps the word "copy" for a rotated "copied" rubber-stamp overlay (-8deg, scale settle). Hover deepens to `stamp-ink`; active nudges down 1px.
- **Nav CTA ("install"):** Ghost variant — transparent with a `stamp` border and `stamp-bright` text; hover fills `stamp` with manila text. The only outlined button.

### Chips / Stamps
- **Date-stamp spec** (`.dstamp`): Oxblood outline (1.5px) with faint oxblood glow, `stamp-ink` uppercase mono 0.88rem, ~0.86 opacity, each rotated a few degrees — vibe-stats presented as stamped issue specs.
- **Withdrawn stamp** (`.nonfeature__stamp`): Absolutely positioned oxblood outline mark ("OUT OF SCOPE", "DECLINED") rotated 9deg over the card corner, ~0.62 opacity — a rejection stamp.
- **Feature entry** (`.feature__entry`): Dashed oxblood border on `stamp-wash`, mono, truncating — a filed catalog line.

### Cards / Containers
- **Corner Style:** 3px.
- **Background:** Manila with a layered warm vignette + faint fiber-tooth gradient (aged variant desaturated for "withdrawn" cards).
- **Shadow Strategy:** The Lit-Paper Rule (see Elevation).
- **Border:** 1px `manila-edge`.
- **Internal Padding:** Generous, 30–52px; hero and CTA reserve extra bottom pad (66–76px) for the punched-hole brass strip.
- **Card furniture:** Optional red header rule with faint blue baseline rules (`card__rulered`), blue divider (`card__ruleblue`), and a bottom `PunchStrip` (punched hole + brass rod).

### Inputs / Command line
- **Install line** (`.install__line`): Reads as a ruled notebook line, not a form field — faint ink tint background, `manila-edge` border with a 2px `rule-blue` underline, 2px radius, mono. Carries an oxblood `$` prompt, ink command text, and a blinking oxblood block cursor (steps animation; reduced to static 0.55 opacity under reduced-motion).

### Navigation
- **Style:** Sticky, translucent oak gradient with a 6px backdrop blur and an `oak-line` bottom border. Wordmark = brass authored-SVG glyph + widely-tracked "TEMPLE" + faint "cat. no. 001" catalog number (0.68rem `label-sm`). Links are mono `paper-soft`, hover to `paper`. Under 720px the catalog number and the features/non-features links drop, leaving GitHub + install.

### Signature Components
- **Drawer tabs** (`.hero__tab`): Manila alphabetical index tabs (A–G / H–N / O–Z) peeking behind the hero card, the middle one lifted and inked oxblood.
- **Punch strip** (`.punch`): A brass rod threaded through a punched hole at the card foot — the catalog rod made literal.
- **Keycaps** (`.keycap`): Physical two-tone manila key caps for the shortcut cheatsheet.
- **Footer drawer label** (`.foot__label`): The wordmark set as an engraved oak drawer-front plate with an 8px-radius brass pull.

## Do's and Don'ts

### Do:
- **Do** put every content plane on a manila card (3px radius, lit-paper shadow, hairline `manila-edge`) resting on the warm oak ground.
- **Do** reserve oxblood (`#a63a50`/`#9a3145`) for stamped moments only — headline, primary button, spec/withdrawn stamps, prompts, section links.
- **Do** split the type voices: Courier Prime for anything typed/stamped/filed/commanded, Public Sans for prose. Keep mono labels uppercase and widely tracked.
- **Do** draw small mono labels from the recorded label/caption band (0.68–0.98rem) and headings from the display/heading band; both are documented steps, not free values.
- **Do** confine pure-black to the shadow scrim tokens (`0.35 / 0.5 / 0.8`) inside `box-shadow` only.
- **Do** use diegetic library hardware (drawer tabs, punched holes, brass rod, keycaps, date stamps, ruled red/blue lines) as the decorative vocabulary instead of generic UI ornament.
- **Do** give cards subtle fractional rotation at rest and flatten all rotation, and stack to one column, under 720px.
- **Do** honor reduced-motion: no typewriter reveal, static cursor, no hover lift dependence.

### Don't:
- **Don't** use near-black, cool grey, or a terminal-window mockup as a *surface* — the darkest surface is warm oak. This is the confirmed anti-reference.
- **Don't** introduce a second accent hue or spend oxblood as a general highlight; brass, ruled lines, and warmth carry secondary emphasis.
- **Don't** set prose in mono or a stamp/command in sans.
- **Don't** flatten the material into cold flat design or glassy surfaces — cards are lit paper objects with warm shadows.
- **Don't** add large radii beyond the 8px hardware pill; keep corners small (2–4px) so surfaces read as paper and hardware.

<!-- not-canonized: the manila fiber, oak wood-grain, and brass are rendered as CSS gradients/repeating-linear-gradients as a stand-in; real raster manila/brass textures are a deferred future enhancement (blocked on image generation), not a system rule to reproduce in code. -->
