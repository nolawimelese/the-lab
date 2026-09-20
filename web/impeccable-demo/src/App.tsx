import { useEffect, useRef, useState } from 'react'
import './App.css'

/* ------------------------------------------------------------------ *
 * Temple — a terminal note-taking app, filed as a library card catalog.
 * Every content plane is a manila card; the accent is rubber-stamp ink.
 * ------------------------------------------------------------------ */

/* --- authored icon set: one consistent 1.6 stroke, currentColor --- */
function IconCatalog() {
  return (
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <rect x="3.5" y="4.5" width="17" height="15" rx="1.5" stroke="currentColor" strokeWidth="1.6" />
      <line x1="3.5" y1="9.2" x2="20.5" y2="9.2" stroke="currentColor" strokeWidth="1.6" />
      <line x1="7" y1="13" x2="17" y2="13" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
      <line x1="7" y1="16" x2="13" y2="16" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
    </svg>
  )
}
function IconArrow() {
  return (
    <svg width="12" height="12" viewBox="0 0 16 16" fill="none" aria-hidden="true">
      <path
        d="M4.5 11.5L11.5 4.5M11.5 4.5H6M11.5 4.5V10"
        stroke="currentColor"
        strokeWidth="1.6"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  )
}
function IconStar() {
  return (
    <svg width="13" height="13" viewBox="0 0 16 16" fill="none" aria-hidden="true">
      <path
        d="M8 2.2V13.8M3.1 5.1L12.9 10.9M12.9 5.1L3.1 10.9"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
      />
    </svg>
  )
}

const STATS = ['1 binary', '0 deps', '≈3 MB', '<200ms']

const FEATURES = [
  {
    call: 'MD',
    title: 'Plain Markdown files',
    body: 'No database, no proprietary format. Grep them, git them, sync them however you like.',
    entry: '~/notes/2026-09-17.md',
  },
  {
    call: 'CAP',
    title: 'Instant capture',
    body: 'Launch opens today’s daily note. Or append a line without opening the UI at all.',
    entry: 'temple "buy milk"',
  },
  {
    call: 'FND',
    title: 'Fuzzy find everything',
    body: 'One key searches titles and content across every note. Results in milliseconds.',
    entry: '/  raku firing notes',
  },
  {
    call: 'MOD',
    title: 'Modal editing',
    body: 'Vim keys out of the box — j/k, i, Esc. Or a plain-editor mode for everyone else.',
    entry: 'i  … Esc',
  },
  {
    call: 'CFG',
    title: 'Zero config',
    body: 'One binary. No accounts, no daemon, no telemetry. Offline because there is no “online.”',
    entry: '$ temple   # the whole setup',
  },
]

const NON_FEATURES = [
  {
    title: 'No sync service',
    stamp: 'OUT OF SCOPE',
    body: 'Use git, Syncthing, Dropbox — your call. Your files, your pipes.',
  },
  {
    title: 'No backlinks graph',
    stamp: 'NOT HELD',
    body: 'You came to write a note, not to garden a knowledge graph at 1 a.m.',
  },
  {
    title: 'No plugins',
    stamp: 'WITHDRAWN',
    body: 'Nothing to install, break, or audit. The surface stays flat on purpose.',
  },
  {
    title: 'No AI',
    stamp: 'DECLINED',
    body: 'It will not summarize, autocomplete, or form opinions about your grocery list.',
  },
  {
    title: 'No subscription',
    stamp: 'NO CHARGE',
    body: 'It never phones home for rent. Install it once and forget the invoice.',
  },
]

const STEPS = [
  {
    n: '01',
    cmd: 'brew install temple',
    body: 'A single binary. Or cargo install temple, or grab the download. No account, no wizard.',
  },
  {
    n: '02',
    cmd: 'temple',
    body: 'You’re writing within 200ms. Today’s note opens straight to the cursor.',
  },
  {
    n: '03',
    cmd: 'Esc  q',
    body: 'Your note is already saved. It was a plain file on your disk the whole time.',
  },
]

const KEYS = [
  { k: 'n', d: 'new' },
  { k: '/', d: 'search' },
  { k: 'd', d: 'delete' },
  { k: 't', d: 'today' },
  { k: 'j k', d: 'move' },
  { k: 'i', d: 'write' },
  { k: 'Esc', d: 'leave' },
  { k: 'q', d: 'quit' },
]

const VOICES = [
  {
    quote: 'I aliased my second brain to /dev/null and haven’t missed it once.',
    who: 'rc_dotfiles',
    role: 'sysadmin · runs it in tmux',
  },
  {
    quote:
      'It opens before I finish exhaling, and every note is grep-able. That is the entire review.',
    who: 'Priya N.',
    role: 'backend engineer',
  },
  {
    quote: 'Finally, a notes app that does not want a relationship.',
    who: 'mx-helix',
    role: 'terminal gremlin',
  },
]

/* --- respects prefers-reduced-motion --- */
function usePrefersReducedMotion() {
  const [reduced, setReduced] = useState(
    () =>
      typeof window !== 'undefined' &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches,
  )
  useEffect(() => {
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)')
    const on = (e: MediaQueryListEvent) => setReduced(e.matches)
    mq.addEventListener('change', on)
    return () => mq.removeEventListener('change', on)
  }, [])
  return reduced
}

/* --- the install command: typed onto a ruled line, with a copy stamp --- */
function InstallCommand({
  command = 'brew install temple',
  size = 'lg',
}: {
  command?: string
  size?: 'lg' | 'sm'
}) {
  const reduced = usePrefersReducedMotion()
  const [typed, setTyped] = useState(reduced ? command : '')
  const [copied, setCopied] = useState(false)
  const ref = useRef<HTMLDivElement>(null)
  const started = useRef(false)

  useEffect(() => {
    // when reduced motion is preferred, initial state already shows the full
    // command — nothing to animate.
    if (reduced) return
    const el = ref.current
    if (!el) return
    const io = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting && !started.current) {
          started.current = true
          let i = 0
          const tick = () => {
            i += 1
            setTyped(command.slice(0, i))
            if (i < command.length) window.setTimeout(tick, 42)
          }
          window.setTimeout(tick, 260)
        }
      },
      { threshold: 0.6 },
    )
    io.observe(el)
    return () => io.disconnect()
  }, [command, reduced])

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(command)
    } catch {
      /* clipboard unavailable — the text is still visible to copy by hand */
    }
    setCopied(true)
    window.setTimeout(() => setCopied(false), 1600)
  }

  const done = typed.length === command.length

  return (
    <div ref={ref} className={`install install--${size}`}>
      <code className="install__line" aria-label={`Install command: ${command}`}>
        <span className="install__prompt" aria-hidden="true">
          $
        </span>
        <span className="install__text">{typed}</span>
        <span
          className={`install__cursor ${done ? 'is-blinking' : ''}`}
          aria-hidden="true"
        />
      </code>
      <button type="button" className="install__copy" onClick={copy}>
        <span className={`install__copyword ${copied ? 'is-hidden' : ''}`}>
          copy
        </span>
        <span className={`install__stamp ${copied ? 'is-shown' : ''}`} aria-hidden={!copied}>
          copied
        </span>
      </button>
    </div>
  )
}

function PunchStrip() {
  return (
    <div className="punch" aria-hidden="true">
      <span className="punch__hole" />
      <span className="punch__rod" />
    </div>
  )
}

function App() {
  return (
    <>
      <a href="#install" className="skiplink">
        Skip to install
      </a>

      {/* ---------------- nav: the drawer label rail ---------------- */}
      <header className="nav">
        <div className="nav__inner">
          <a href="#top" className="nav__mark" aria-label="Temple — home">
            <span className="nav__glyph" aria-hidden="true">
              <IconCatalog />
            </span>
            <span className="nav__word">TEMPLE</span>
            <span className="nav__cat" aria-hidden="true">
              cat. no. 001
            </span>
          </a>
          <nav className="nav__links" aria-label="Primary">
            <a href="#does">features</a>
            <a href="#doesnt">non-features</a>
            <a
              href="https://github.com"
              className="nav__gh"
              rel="noreferrer nofollow"
            >
              GitHub
              <IconArrow />
            </a>
            <a href="#install" className="nav__cta">
              install
            </a>
          </nav>
        </div>
      </header>

      <main id="top">
        {/* ---------------------- hero ---------------------- */}
        <section className="hero" aria-labelledby="hero-h">
          <div className="hero__drawer" aria-hidden="true">
            <span className="hero__tab hero__tab--a">A–G</span>
            <span className="hero__tab hero__tab--b">H–N</span>
            <span className="hero__tab hero__tab--c">O–Z</span>
          </div>

          <article className="card hero__card">
            <div className="card__rulered" />
            <div className="hero__cardhead">
              <span className="hero__filed">filed under</span>
              <span className="hero__subject">terminal · plain text · yours</span>
            </div>

            <h1 id="hero-h" className="hero__headline">
              <span className="stamped">notes,</span>{' '}
              <span className="stamped stamped--2">without</span>{' '}
              <span className="stamped stamped--3">the noise.</span>
            </h1>
            <p className="hero__lede">
              Open it, write, close it. Your notes are just Markdown files in a
              folder you own — no accounts, no daemon, no second brain to feed.
            </p>

            <div id="install" className="hero__install">
              <InstallCommand />
            </div>

            <div className="datestamps">
              <span className="datestamps__head">specs — stamped on issue</span>
              <ul className="datestamps__row" aria-label="At a glance">
                {STATS.map((s) => (
                  <li key={s} className="dstamp">
                    {s}
                  </li>
                ))}
              </ul>
            </div>

            <PunchStrip />
          </article>

          <p className="hero__aside">
            <span className="hero__asidemark" aria-hidden="true">
              <IconStar />
            </span>
            The card catalog your note app forgot it was replacing.
          </p>
        </section>

        {/* ------------------- what it does ------------------- */}
        <section id="does" className="section" aria-labelledby="does-h">
          <div className="section__head">            <h2 id="does-h" className="section__title">
              What it does
            </h2>
            <p className="section__sub">
              Five cards. Held to five on purpose — the point is restraint.
            </p>
          </div>

          <div className="tray">
            {FEATURES.map((f, i) => (
              <article className="card feature" key={f.call} style={{ ['--i' as string]: i }}>
                <span className="feature__tab">{f.call}</span>
                <div className="card__ruleblue" />
                <h3 className="feature__title">{f.title}</h3>
                <p className="feature__body">{f.body}</p>
                <code className="feature__entry">{f.entry}</code>
              </article>
            ))}
          </div>
        </section>

        {/* ---------------- what it doesn't do ---------------- */}
        <section id="doesnt" className="section section--dark" aria-labelledby="doesnt-h">
          <div className="section__head">            <h2 id="doesnt-h" className="section__title">
              What it doesn’t do
            </h2>
            <p className="section__sub">
              Deliberately not held. Every “no” below is part of the pitch.
            </p>
          </div>

          <div className="withdrawn">
            {NON_FEATURES.map((nf) => (
              <article className="card card--aged nonfeature" key={nf.title}>
                <span className="nonfeature__stamp" aria-hidden="true">
                  {nf.stamp}
                </span>
                <h3 className="nonfeature__title">{nf.title}</h3>
                <p className="nonfeature__body">{nf.body}</p>
              </article>
            ))}
          </div>
        </section>

        {/* ------------------- how it works ------------------- */}
        <section id="how" className="section" aria-labelledby="how-h">
          <div className="section__head">            <h2 id="how-h" className="section__title">
              From nothing to a saved note
            </h2>
            <p className="section__sub">Three lines. Then you’re out.</p>
          </div>

          <ol className="steps">
            {STEPS.map((s) => (
              <li className="card step" key={s.n}>
                <span className="step__n">{s.n}</span>
                <code className="step__cmd">{s.cmd}</code>
                <p className="step__body">{s.body}</p>
              </li>
            ))}
          </ol>
        </section>

        {/* ------------------- cheatsheet ------------------- */}
        <section id="keys" className="section section--dark" aria-labelledby="keys-h">
          <div className="section__head">            <h2 id="keys-h" className="section__title">
              The whole vocabulary
            </h2>
            <p className="section__sub">
              Circulation rules, printed on the card. That’s all of them.
            </p>
          </div>

          <article className="card cheat">
            <div className="card__rulered" />
            <ul className="cheat__grid" aria-label="Keyboard shortcuts">
              {KEYS.map((row) => (
                <li className="cheat__row" key={row.d}>
                  <span className="cheat__keys">
                    {row.k.split(' ').map((k) => (
                      <kbd className="keycap" key={k}>
                        {k}
                      </kbd>
                    ))}
                  </span>
                  <span className="cheat__dot" aria-hidden="true" />
                  <span className="cheat__def">{row.d}</span>
                </li>
              ))}
            </ul>
          </article>
        </section>

        {/* ------------------- voices ------------------- */}
        <section id="voices" className="section" aria-labelledby="voices-h">
          <div className="section__head">            <h2 id="voices-h" className="section__title">
              Borrower’s slips
            </h2>
            <p className="section__sub">
              Notes left in the back pocket by people who checked it out.
            </p>
          </div>

          <div className="voices">
            {VOICES.map((v) => (
              <figure className="card voice" key={v.who}>
                <blockquote className="voice__quote">“{v.quote}”</blockquote>
                <figcaption className="voice__by">
                  <span className="voice__who">{v.who}</span>
                  <span className="voice__role">{v.role}</span>
                </figcaption>
              </figure>
            ))}
          </div>
          <p className="voices__disclaimer">
            Illustrative personas — Temple is a concept in the open. No real
            endorsements, star counts, or borrowers exist yet.
          </p>
        </section>

        {/* ------------------- final CTA ------------------- */}
        <section id="get" className="cta" aria-labelledby="cta-h">
          <article className="card cta__card">
            <div className="card__rulered" />
            <h2 id="cta-h" className="cta__title">
              It’s free. It’s yours.
            </h2>
            <p className="cta__lede">
              MIT-licensed, open source, and offline by default. Install it once;
              the notes were always going to outlive the app.
            </p>
            <InstallCommand />
            <div className="cta__meta">
              <a href="https://github.com" className="cta__link" rel="noreferrer nofollow">
                Source on GitHub
                <IconArrow />
              </a>
              <span className="cta__dot" aria-hidden="true">
                ·
              </span>
              <span>MIT</span>
              <span className="cta__dot" aria-hidden="true">
                ·
              </span>
              <span>no accounts</span>
              <span className="cta__dot" aria-hidden="true">
                ·
              </span>
              <span>no telemetry</span>
            </div>
            <PunchStrip />
          </article>
        </section>
      </main>

      {/* ------------------- footer: drawer front ------------------- */}
      <footer className="foot">
        <div className="foot__label">
          <span className="foot__word">TEMPLE</span>
          <span className="foot__sub">terminal notes · plain files</span>
          <span className="foot__pull" aria-hidden="true" />
        </div>
        <p className="foot__note">
          Enter. Write. Leave. — A concept landing page; install commands and
          links are illustrative and don’t resolve yet.
        </p>
      </footer>
    </>
  )
}

export default App
