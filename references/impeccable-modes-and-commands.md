# Visitor Modes, Craft Floor & Refine Commands (Impeccable)

Distilled from github.com/pbakaus/impeccable (Apache-2.0 © Paul Bakaus), skill v4.6. Ideas paraphrased; no code or binary bundled.

## 1. Visitor mode (pick from the surface, not the product)
| Mode | Visitor succeeds by | Surfaces | Ambition shows as |
|---|---|---|---|
| **Persuade** | deciding and acting | landing, marketing, campaign, pricing | bold, distinct, point of view, real imagery |
| **Operate** | completing a task | dashboards, admin, editors, settings, tools | precision, consistency, scanability; brand in details |
| **Read** | understanding | docs, articles, guides, changelogs | structure for comprehension, comfortable reading |
| **Experience** | being inside the work | portfolios, galleries, showcases | the artifact leads from the first viewport; UI recedes |
A tool's landing page is still Persuade; a docs index is Read. Map to this skill: Website/Section → Persuade or Experience; Dashboard/App → Operate; docs/blog → Read.

## 2. Refinement vs redesign
- **Refinement** keeps identity, behavior, copy, and everything out of scope. Polish inside the existing look.
- **Redesign** keeps product truth (content, function, constraints) but treats the old look as evidence of what to leave behind; commit to a new visual world. Never split the difference by polishing the discarded look.
- **The brief wins**: pinned fonts, palettes, eras, or brand rules override every default and ban in this skill.
- Ask before replacing factual copy or adding claims. No loaded symbols (hate, militarism) as decoration.

## 3. Craft floor — verify on the built result
- Contrast: body and placeholder ≥ 4.5:1, large ≥ 3:1; on colored surfaces tint secondary text from that hue, never grey.
- Depth: shadows have offset + soft blur; zero-offset colored halos are decoration.
- Spacing: tight groups, generous separation, more space above a heading than below.
- Type: measure 65–75ch, display ≤ 6rem, tracking ≥ −0.04em, balanced headings, obvious scale steps; run real copy at every breakpoint.
- Motion: one authored moment per page, not the same entrance on every section; exponential ease-out from an already-visible default.
- States: hover, disabled, loading, error, empty, keyboard focus, real content, responsive composition.
- **Browser surfaces**: theme `::selection`, `caret-color`, scrollbars, focus rings, `text-underline-offset`, and tabular numerals from the palette. Cheapest signal that a page was built, not assembled.
- Copy in the product's own language; controls name actions; errors name problem + recovery.
- Coverage: every brief requirement present and findable within seconds.

## 4. Refuse by default (Persuade / Read / Experience)
- Same-size icon+heading+text cards as page structure; nested cards (always wrong).
- Hero-metric template (big number, small label, supporting stats, accent) as a hero.
- **Kicker/eyebrow labels above headings: banned outright.** Section numbers only when sequence is real information.
- Gradient text; glass/blur as decoration; colored `border-left/right` > 1px on cards, list items, callouts, alerts; hard offset block shadows outside a real neobrutalist world.
- Sparklines, progress rings, or soft rounded rectangles standing in for content.
- Monospace as a "technical" costume (only for code, data, measurements).
- System fonts (Arial Black, Impact, platform sans) as the display voice.
- Emoji or unicode glyphs as icons (use Hugeicons / a real library).
- Geometric masks faking organic photo cut-outs.
- Light vs dark chosen by category instead of by the use scene (who, where, what light).
**Operate exception**: a user's own kit conventions that encode information (Prism's active-nav bar, category bars on calendar/time-off events, KPI cards, progress rings that show real values) are allowed.

## 5. Refine commands (user can say these directly)
| Say | Do |
|---|---|
| **polish** | Final pass: classify each issue (missing token / one-off implementation / conceptual mismatch / local defect), fix the whole path: flow, layout & type, color & icons, states, content & code. |
| **bolder** | Amplify what the system already owns (its motif, its type scale at full strength). One decisive move, quiet everything around it; make the section a peak in the scroll rhythm. Keep claims true. |
| **quieter** | Find intensity sources; desaturate to ~70–85%, neutrals dominate (color ≈10%), keep very few bold elements, remove what can go, gentler contrast except where it matters. |
| **distill** | Find the ONE purpose; cut secondary actions and redundancy; progressive disclosure; 1–2 colors + neutrals, one family, 3–4 sizes, 2–3 weights; one primary action. |
| **harden** | Production edge cases: 100+ char names, emoji, RTL (Arabic) and CJK text, Bangla text, empty/huge data, network and permission errors, validation, offline, slow states. |
| **colorize** | Persuade: color may own regions and carry the voice. Operate/Read: color encodes action, selection, status, wayfinding; rarity gives the accent force. |
| **typeset** | Persuade: decisive display contrast. Operate/Read: one well-tuned family, fixed role scale, measure first. |
| **delight** | One delight thesis at meaningful moments (first use, success, recovery, mastery); success scaled to effort; never fake waiting; no jokes about money, loss, privacy. |
| **overdrive** | Propose 2–3 ambitious directions with trade-offs and get a pick before building; toolkit: View Transitions, `@starting-style`, springs, scroll-driven animations (`animation-timeline`) with static fallback, WebGL (Three.js/OGL). |
| **layout** / **adapt** / **clarify** / **onboard** | Fix spacing & hierarchy / adapt to devices / rewrite UX copy & errors / design first-run, empty states, activation. |
| **critique** / **audit** | UX heuristic review / technical check (a11y, performance, responsive). Use the report formats in `product-ui-polish.md` §10. |
