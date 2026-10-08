---
name: redesign-with-nazmul
description: Fast, opinionated UI redesign system by Nazmul (Hassan) built on Refactoring UI principles and shadcn/ui-kit style dashboards. Use this skill whenever the user asks to redesign, restyle, polish, modernize, "make it look better/premium/Awwwards-level", or rebuild any website, landing page, single section (hero, pricing, features, footer, testimonials), admin/SaaS dashboard, or web/mobile app screen — from a screenshot, code, URL, Figma link, or plain description. Also trigger on Bangla/Banglish requests like "redesign koro", "eta sundor kore dao", "modern kore dao", "dashboard ta redesign", even if the word "skill" or "nazmul" is never mentioned.
---

# Redesign with Nazmul

Goal: take whatever the user gives you and return a noticeably better, production-ready redesign **fast** — one pass, no long interviews. Two design sources drive every decision:

- **Refactoring UI** (Wathan & Schoger) — the rules for hierarchy, spacing, type, color, depth. See `references/refactoring-ui-principles.md`.
- **shadcn UI Kit** (shadcnuikit.com, source: github.com/bundui/shadcn-ui-kit) — the visual language for dashboards and apps: monochrome neutral tokens, near-black primary, pill buttons, ringed rounded cards, inset sidebar shell, container-query grids. See `references/shadcn-dashboard-patterns.md` and the component catalog `references/shadcn-ui-kit-components.md`.

For marketing websites and sections, layer on the Awwwards playbook in `references/awwwards-web-patterns.md` and pick section ideas from `references/awwwards-section-library.md` (organized like Awwwards Collections). Hassan's favorite inspiration sites (Awwwards, HorizonX, Framify) and how to use a shared reference are in `references/inspiration-sources.md`. For product/mobile app screens, read `references/app-patterns.md`.

More toolkits are built in:
- **Taste & anti-slop** (`references/taste-anti-slop.md`): the Variance/Motion/Density dials, the redesign fix-priority order, and the AI-tell blacklist. Read it for every website/section job.
- **Motion polish** (`references/motion-emil.md`): Emil Kowalski's rules for whether/how/how fast to animate. Read it whenever you add states or animation.
- **Product UI polish** (`references/product-ui-polish.md`): exact values for surfaces, motion, typography, layout, color, UI copy, accessibility and metadata, plus audit/review report formats. Run it on every dashboard/app output.
- **shadcn official rules** (`references/shadcn-official-rules.md`): how correct shadcn/ui code is composed (FieldGroup, gap not space-y, Card anatomy, semantic tokens). Read it whenever output is React + shadcn.
- **DESIGN.md library** (`references/design-md-examples/`): 18 real design systems (Vercel, Atlassian, Clerk, Mintlify, Culture Amp…) for structure and "feel like X" directions. Never copy their brand.
- **Design intelligence engine** (`tools/ui-ux-pro-max/`): a local searchable database of 79 styles, 192 product palettes, 74 font pairings, 119 UX guidelines, landing patterns and chart types. Use it when there is no brand direction yet (see step 3).

**Dashboard theme choice**: default to the monochrome shadcn UI Kit look (`assets/tokens.css`). Use the **Prism** theme (`references/prism-dashboard-patterns.md` + `assets/tokens-prism.css`, from Hassan's own Figma kit) when the product is HR, ATS, recruitment, people-ops, payroll, or enterprise back-office, or when the user asks for a friendly blue SaaS look. The user's brand always wins over both. For a domain-specific layout (freelance, e-learning, job search/ATS, crypto, SaaS metrics, social planner, onboarding, auth, settings) check `references/prism-screen-library.md` first.

## Speed rules

Speed is the point of this skill, so:

1. **Don't ask questions unless something truly blocks you** (e.g., an attached file is missing). Make a sensible assumption, state it in one line, and build.
2. **Keep all content and functionality.** Redesign = same information and actions, better presentation. Never drop fields, links, or data. You may reorder, regroup, and rewrite microcopy for clarity.
3. **Read only the references you need** for the mode (below). Don't load all of them.
4. **Deliver the redesign, not an essay.** The diagnosis is short; the output is the work.

## Workflow

### 1. Detect input and mode

| Input | What to do |
|---|---|
| Screenshot / image | Read the layout, content, and hierarchy from it |
| Code (HTML/JSX/Vue/CSS) | Keep structure & logic, rewrite markup/styles |
| Figma link (and Figma tools available) | Pull design context/screenshot first, then redesign |
| URL or description only | Infer content; use realistic placeholder copy (never lorem ipsum) |

| Mode | Triggers | Read |
|---|---|---|
| **Website** | landing page, full site, portfolio, "Awwwards" | awwwards-web-patterns.md + awwwards-section-library.md + refactoring-ui |
| **Section** | hero, pricing, features, CTA, footer, FAQ, nav, preloader | awwwards-section-library.md (that section only) + refactoring-ui |
| **Dashboard** | admin, analytics, SaaS, CRM, table-heavy | shadcn-dashboard-patterns.md (or prism-dashboard-patterns.md for HR/ATS/payroll) + shadcn-ui-kit-components.md + refactoring-ui |
| **App** | mobile screen, onboarding, settings, product UI | app-patterns.md + shadcn-ui-kit-components.md |

### 2. Quick audit (max 5 bullets)

Scan the original against the Refactoring UI checklist and name the **top 3–5 problems** only, each with its fix. Example:
- Everything is the same weight → primary metric 30px/600, labels 13px muted.
- Spacing is random → snap to 4/8px scale, 24px card padding, 48px section gaps.

### 3. Pick a direction (one line)

State the direction in one sentence including the dials: surface tone, accent, type pairing, and `V/M/D`. E.g. "Warm off-white, single deep-teal accent, Satoshi + Geist Mono, V7 M6 D4."

- User's brand colors/fonts known → use them.
- Dashboard → `assets/tokens.css` (monochrome) or `assets/tokens-prism.css` (HR/ATS/payroll).
- Website/section with no brand → run the engine for a starting palette + font pairing + landing pattern, then filter it through the anti-slop rules (reject purple AI gradients, generic fonts on premium briefs):
```bash
python3 <skill-dir>/tools/ui-ux-pro-max/scripts/search.py "<product> <industry> <mood>" --design-system -p "<Name>" --variance <V> --motion <M> --density <D>
python3 <skill-dir>/tools/ui-ux-pro-max/scripts/search.py "<keywords>" --domain landing|typography|color|chart|ux -n 3
```
Treat engine output as suggestions, not orders. If bash isn't available, skip it and decide from the references.

### 4. Build

- **Default stack**: a single self-contained HTML file with Tailwind (play CDN) and the CSS-variable tokens from `assets/tokens.css`, so it previews instantly. If the user gave React/shadcn code, return React + shadcn/ui components instead. If they asked for Figma, build in Figma.
- In dashboards/apps, swap weak patterns for the right kit component (see the swap table in `shadcn-ui-kit-components.md`).
- Use the token variables (`--background`, `--foreground`, `--muted`, `--primary`, `--border`, `--radius`…) — never hard-code random hex values.
- Include light **and** dark mode via tokens.
- Responsive: mobile-first, test mentally at 375 / 768 / 1280 / 1536.
- Real states: hover, focus-visible ring, active (`scale(0.97)`), disabled, empty, skeleton loading, inline errors.
- Motion: **websites/sections** follow `motion-emil.md` (custom ease-out curves, expressive entrances allowed). **Dashboards/apps** follow `product-ui-polish.md` §3 (feedback ≤ 200ms, no motion on high-frequency actions, Tailwind easing). Both: press `scale(0.96)`, only transform/opacity, nothing from `scale(0)`, reduced-motion respected.
- Content: real copy, believable names and organic numbers, no lorem ipsum.
- Icons: Lucide (kit default), 16px in buttons/nav, stroke 2, consistent.

### 5. Pre-flight check (do it silently, fix before delivering)

- [ ] One clear primary action per view; secondary actions visually quieter
- [ ] Hierarchy uses weight + color, not just size
- [ ] Every spacing value is on the 4/8 scale; more space between groups than within
- [ ] Body text ≥ 16px on marketing, ≥ 14px in dashboards; line length 45–75ch
- [ ] Text contrast ≥ 4.5:1 (WCAG AA); no grey text on colored backgrounds
- [ ] Monochrome base; max 1 brand accent + semantic colors (success/warning/destructive, soft-tinted)
- [ ] No cards-inside-cards-inside-cards; borders OR shadow, rarely both
- [ ] Numbers in tables right-aligned with tabular-nums
- [ ] No AI tells from `taste-anti-slop.md` §3 (purple gradient, 3 equal cards, numbered eyebrows, scroll cues, fake div screenshots, filler verbs, em-dash decoration)
- [ ] Full-height sections use `min-h-[100dvh]`; no horizontal scroll on mobile; touch targets ≥ 44px
- [ ] All original content and actions still present

### 6. Deliver

Reply format (keep it short, in the user's language):
1. **Problems fixed** — 3–5 bullets from step 2
2. **Direction** — one line
3. **The redesign** — the file/code/Figma frame
4. **Next tweaks** — optional, 1–2 suggestions max

When the user asks for changes, edit the existing output rather than regenerating from scratch.

When the user asks to **review** (not redesign): motion/CSS details → one `| Before | After | Why |` table; an existing screen → the max-3 findings table from `product-ui-polish.md` §10; a PR/branch → Introduced/Regression/Pre-existing findings (same section). When they ask for a reusable design system doc, write a `DESIGN.md` (format in `taste-anti-slop.md` §6).
