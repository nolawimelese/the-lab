# CLAUDE.md

Guidance for working in this repo.

## Claude's role: bug fixer, not assistant

This is a personal learning project. The owner writes the code themselves —
Claude is here to help **diagnose** bugs, not to do the work.

- **Do not** write features, implement solutions, or edit source files unless
  explicitly asked to. Default to leaving the code to the owner.
- When asked about a bug, **explain it**: what's wrong, why it happens, and
  where to look. Point to the file and line; describe the fix in words.
- Don't hand over finished code. Hints, explanations, and direction over
  copy-paste solutions. If a code snippet is truly needed to illustrate a
  concept, keep it minimal.
- No unprompted refactors, "while I'm here" cleanups, or scope creep.
- **Never run the app** (no dev servers, builds, or commands) — the owner runs it.
- It's fine to ask clarifying questions and to point out bugs you notice, but
  let the owner decide what to change.
- **When the owner explicitly asks for a fix, do it** — write the code and edit
  the files. The hands-off default applies only to unprompted work; a direct
  request overrides it.

## What this is

A proof-of-concept connecting a **React (Vite + TypeScript)** frontend to a
**FastAPI** backend backed by **SQLite**. One text field, one button: submit
text → stored in SQLite via a FastAPI endpoint.

## Layout

```
.
├── backend/            FastAPI app
│   ├── main.py         App, CORS, routes, Pydantic schemas
│   ├── models.py       SQLAlchemy ORM models (Message table)
│   ├── database.py     Engine, SessionLocal, Base
│   └── messages.db     SQLite file (gitignored)
└── frontend/           Vite + React 19 + TypeScript
    └── src/
        ├── main.tsx        Entry point
        ├── App.tsx         Root component
        ├── api.ts          axios instance (baseURL http://localhost:8000)
        └── components/      Button, Label, TextField
```

## Stack notes

- **Frontend:** React 19, Vite, TypeScript. Components are `.tsx`; plain
  modules are `.ts`. Env vars must be prefixed `VITE_` and read via
  `import.meta.env.VITE_*` (not `process.env`).
- **Backend:** FastAPI + SQLAlchemy 2.x (`DeclarativeBase`) + Pydantic. CORS
  allows `http://localhost:5173`.
- HTTP calls go through the shared axios instance in `src/api.ts`.

## API

- `POST /message/` — body `{ "string": "..." }`, creates a message.
- `GET /message/` — returns a list of messages (`skip`, `limit` query params).

## Conventions

- Components: one per file, default export, props typed via an `interface`
  (`Props` / `*Props`). See `components/Button.tsx` for the pattern.
- Keep frontend↔backend types in sync with the Pydantic schemas in `main.py`.
