# INFRASTRUCTURE.md — Kanonisk oversigt over alle services
_Opdateres af Kira når nye services tilføjes. Læses af alle agenter FØR de tager arkitekturbeslutninger._

---

## ⚠️ VIGTIG REGEL FOR AGENTER
**Inden du vælger en database, storage eller API:**
1. Læs denne fil
2. Brug en eksisterende service hvis den passer
3. Spørg Kira/Henrik inden du opretter noget nyt

---

## Databaser

### Neon (PostgreSQL) — PRIMÆR DATABASE
- **Hvad:** Managed PostgreSQL med PostGIS
- **Bruges til:** MaxBuddy V4 (MB4) — stores, products, reports, prices
- **Også egnet til:** Alle nye projekter der behøver en rigtig relationel database
- **Creds:** `/home/slambert/.openclaw/workspace/credentials/neon-database-url.txt`
- **Org:** `[se workspace/INFRASTRUCTURE.md]`
- **Brug det til:** Alt nyt der behøver persistent storage og ikke er et spil

### Turso (LibSQL/SQLite) — LEGACY
- **Hvad:** Edge SQLite database
- **Bruges til:** MaxBuddy V3 (gammelt, kørende produktionssite)
- **BRUG IKKE til nyt** — vi migrerede til Neon i Sprint 2
- **Creds:** se `credentials/mb4-services.md`

### Cloudflare D1 (SQLite) — KUN TIL SLAMBERT.COM SPIL
- **Hvad:** SQLite database koblet til Cloudflare Pages
- **Bruges KUN til:** slambert.com spil-leaderboards (papirklipsjagt, Clippy's Revenge)
- **BRUG IKKE til:** noget andet — det er en spil-database
- **Database ID prod:** `[se workspace/INFRASTRUCTURE.md]`
- **Database ID staging:** `[se workspace/INFRASTRUCTURE.md]`

---

## Hosting & Deployment

### Vercel — MB4
- **Hvad:** Hosting for MaxBuddy V4
- **Project ID:** `[se workspace/INFRASTRUCTURE.md]`
- **URL:** `maxbuddy-v4.vercel.app`
- **Token:** `/home/slambert/.openclaw/workspace/credentials/vercel-token.txt`
- **Vigtigt:** Brug Henriks token — kira-agent har ikke Vercel team-adgang

### Cloudflare — Account
- **Account ID:** `[se workspace/INFRASTRUCTURE.md]`

### Cloudflare API Tokens — KOMPLET OVERSIGT

| Token | Værdi | Permissions | Bruges til |
|---|---|---|---|
| **Primært (bred adgang)** | `[se workspace/INFRASTRUCTURE.md]` | Pages, Workers, DNS, D1, mm. | **Brug dette som default** |
| Tunnel/DNS/ZeroTrust | `[se workspace/INFRASTRUCTURE.md]` | Tunnel Edit, DNS Edit, Zero Trust | Kira tunnel |
| Browser Rendering | `[se workspace/INFRASTRUCTURE.md]` | Browser Rendering Edit | MB4 catalog crawler |

**Regel:** Prøv altid det primære token først. Brug specialiserede tokens kun hvis det primære ikke har den specifikke permission.

### Cloudflare Pages — slambert.com
- **Repo:** `SlambertDK/slambert-com`
- **URL:** `slambert.com`
- **Deploy:** Automatisk fra main branch
- **API til Pages env vars:** Primært token

### ⚠️ Cloudflare Pages Functions — storage regler
**VIGTIGT — dette gælder for ALT der kører i Pages Functions (edge runtime):**
- ✅ **KV** — native, virker altid. Brug til key-value storage
- ✅ **R2** — native, virker til filer/blobs
- ✅ **D1** — native, virker til SQLite (kun slambert.com spil)
- ❌ **Neon/Postgres** — kræver `@neondatabase/serverless` npm pakke + bundler. Virker IKKE i Pages Functions uden bundling. Brug Vercel/Node til Neon-kald.
- ❌ **Rå HTTP til Neon** — Neons HTTP API kræver deres driver. Virker ikke med fetch direkte.

**Tommelfingerregel:** slambert.com Pages Functions = KV/R2/D1. Neon = kun fra Vercel (MB4) eller Node scripts.

### Cloudflare Pages — alle projekter
| Projekt | URL |
|---|---|
| slambert-com | slambert.com |
| pepsimax-index-git | (V3 legacy) |
| maxbuddy-playground | playground |

### Cloudflare Tunnel — Kira
- **URL:** `kira.slambert.com` → localhost:18789
- **Tunnel navn:** kira
- **Zero Trust:** beskyttet

---

## Auth

### Clerk — MB4
- **Bruges til:** MaxBuddy V4 bruger-auth
- **Publishable key:** se `credentials/mb4-services.md`
- **BRUG IKKE til:** slambert.com eller andre projekter

---

## AI / LLM

### Azure Anthropic — PRIMÆR LLM
- **Hvad:** Claude via Henriks Azure AI Foundry konto (gratis via arbejde)
- **Hostname:** `henla-mm2bob76-eastus2.services.ai.azure.com`
- **Auth:** `Authorization: Bearer <key>` (IKKE `api-key` header)
- **Model:** `claude-sonnet-4-6`
- **API path:** `/anthropic/v1/messages?api-version=2025-01-01-preview`
- **Key:** `[se workspace/INFRASTRUCTURE.md]`
- **Creds fil:** `/home/slambert/.openclaw/workspace/credentials/azure-openai.json`

### Azure OpenAI (GPT + Audio)
- **Hvad:** GPT-4o vision + audio via samme Azure konto
- **Bruges til:** Catalog crawler (GPT-4o vision), TTS (morgenbrief)
- **Deployment:** `gpt-audio-1.5` (audio), `gpt-4o` (vision)

---

## GitHub

### SlambertDK (Henrik)
- **Token:** `/home/slambert/.openclaw/workspace/github-token.txt`
- **Brug til:** Alt der kræver Henrik som author — merges, releases

### kira-agent (Kira)
- **Token:** `/home/slambert/.openclaw/workspace/github-kira-token.txt`
- **Brug til:** Issues, kommentarer, branches
- **Kan IKKE:** Pushe til Vercel (ikke på teamet)

---

## Projekter og deres services

| Projekt | Database | Hosting | Auth | Repo |
|---|---|---|---|---|
| MaxBuddy V4 (MB4) | Neon | Vercel | Clerk | `SlambertDK/maxbuddy-v4` |
| MaxBuddy V3 (live) | Turso | (legacy) | — | `SlambertDK/maxbuddy` |
| slambert.com | D1 (spil only) | Cloudflare Pages | — | `SlambertDK/slambert-com` |
| diplom-ledelse | — | — | — | `SlambertDK/diplom-ledelse` |
| energinet-ai | — | — | — | `SlambertDK/energinet-ai` |
| exodraft-analysis | — | — | — | `SlambertDK/exotraft-analysis` |

---

## Præsentationer og tools (slambert.com/kira)

| Titel | URL | Projekt | Dato |
|---|---|---|---|
| Exodraft — Produktvisualisering | https://slambert.com/exodraft | exodraft-analysis | 2026-03-18 |
| Exodraft — Transform præsentation | https://slambert.com/exotraft | exodraft-analysis | 2026-03-18 |
| MaxBuddy Pitch | https://slambert.com/pitch | maxbuddy-v4 | 2026-03-15 |
| MB4 Live App | https://maxbuddy-v4.vercel.app | maxbuddy-v4 | 2026-03-18 |
| Kira Hub (drop/pickup/links) | https://slambert.com/kira | slambert-com | 2026-03-19 |
| Drop filer til Kira | https://kira.slambert.com/drop | openclaw | 2026-03-01 |

_Tilføj nye links her + i `src/kira/links.json` i slambert-com repoen_

---

## Regler for agenter

1. **Ny database?** Brug Neon. Spørg inden du bruger noget andet.
2. **Ny hosting?** Brug Vercel (MB4) eller Cloudflare Pages (slambert.com). Ikke begge til samme projekt.
3. **D1?** Kun til slambert.com spil. Aldrig til noget andet.
4. **Turso?** Kun til at vedligeholde V3. Aldrig til nyt.
5. **Ny præsentation/tool deployet?** Tilføj til tabellen her OG til `src/kira/links.json`.
6. **Usikker?** Stop og spørg Kira i stedet for at gætte.
