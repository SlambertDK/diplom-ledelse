# INFRASTRUCTURE.md — Kanonisk oversigt over alle services
_Fuld version med credentials: `/home/slambert/.openclaw/workspace/INFRASTRUCTURE.md`_
_Opdateres af Kira. Synces til alle repos. Læses af agenter FØR arkitekturbeslutninger._

---

## ⚠️ VIGTIG REGEL FOR AGENTER
**Inden du vælger en database, storage eller API:**
1. Læs `/home/slambert/.openclaw/workspace/INFRASTRUCTURE.md` for fulde credentials
2. Brug en eksisterende service hvis den passer
3. Spørg Kira/Henrik inden du opretter noget nyt

---

## Cloudflare — Account ID: 101f54029f6aca69592052842e0285fd

### API Tokens (værdier i workspace INFRASTRUCTURE.md)
| Token | Permissions | Bruges til |
|---|---|---|
| **Primært (brug dette som default)** | Pages, Workers, DNS, D1 + mere | Alt Cloudflare-arbejde |
| Tunnel/DNS/ZeroTrust | Tunnel, DNS, Zero Trust | Kira tunnel |
| Browser Rendering | Browser Rendering Edit | MB4 catalog crawler |

**Regel:** Prøv altid det primære token. Find det i workspace INFRASTRUCTURE.md.

### Pages projekter
| Projekt | URL |
|---|---|
| slambert-com | slambert.com |
| pepsimax-index-git | V3 legacy |

---

## Databaser

### Neon (PostgreSQL) — PRIMÆR DATABASE
- **Bruges til:** MaxBuddy V4 + alt nyt
- **Creds:** `/home/slambert/.openclaw/workspace/credentials/neon-database-url.txt`
- **ALDRIG brug D1 eller Turso til nyt**

### Turso (LibSQL) — LEGACY ONLY
- **Bruges KUN til:** MaxBuddy V3 vedligehold
- **Opret ikke nyt her**

### Cloudflare D1 — SPIL ONLY
- **Bruges KUN til:** slambert.com leaderboards (papirklipsspillet)
- **Opret ikke nyt her**

---

## Hosting

### Vercel — MB4
- **Project ID:** `prj_8fDGeYvL4MDLRblnKvu1ZELEydr0`
- **Token:** `/home/slambert/.openclaw/workspace/credentials/vercel-token.txt`
- **Vigtigt:** Brug Henriks token — kira-agent har ikke team-adgang

### Cloudflare Pages — slambert.com
- **Repo:** `SlambertDK/slambert-com` → auto-deploy fra main

---

## AI / LLM

### Azure Anthropic — PRIMÆR
- **Hostname:** `henla-mm2bob76-eastus2.services.ai.azure.com`
- **Auth:** `Authorization: Bearer <key>` (IKKE `api-key` header)
- **Model:** `claude-sonnet-4-6`
- **Path:** `/anthropic/v1/messages?api-version=2025-01-01-preview`
- **Creds:** `/home/slambert/.openclaw/workspace/credentials/azure-openai.json`

---

## GitHub

| Konto | Token-fil | Bruges til |
|---|---|---|
| SlambertDK (Henrik) | `workspace/github-token.txt` | Merges, releases, alt der kræver Henrik |
| kira-agent | `workspace/github-kira-token.txt` | Issues, kommentarer, branches |

---

## Projekter og deres services

| Projekt | Database | Hosting | Repo |
|---|---|---|---|
| MaxBuddy V4 (MB4) | Neon | Vercel | `SlambertDK/maxbuddy-v4` |
| MaxBuddy V3 (live) | Turso | Cloudflare Pages | `SlambertDK/maxbuddy` |
| slambert.com | D1 (spil only) | Cloudflare Pages | `SlambertDK/slambert-com` |
| diplom-ledelse | — | — | `SlambertDK/diplom-ledelse` |

---

## Præsentationer og tools

| Titel | URL | Dato |
|---|---|---|
| Exodraft — Produktvisualisering | https://slambert.com/exodraft | 2026-03-18 |
| Exodraft — Transform | https://slambert.com/exotraft | 2026-03-18 |
| MaxBuddy Pitch | https://slambert.com/pitch | 2026-03-15 |
| MB4 Live App | https://maxbuddy-v4.vercel.app | 2026-03-18 |
| Kira Hub | https://slambert.com/kira | 2026-03-19 |
| Drop til Kira | https://kira.slambert.com/drop | 2026-03-01 |
