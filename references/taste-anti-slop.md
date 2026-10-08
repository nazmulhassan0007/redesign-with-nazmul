# Taste Dials, Anti-Slop Rules & Redesign Audit

Distilled from github.com/leonxlnx/taste-skill (MIT © Leonxlnx: taste-skill, redesign-skill) and google-labs-code/stitch-skills (Apache-2.0: taste-design, design-md). Use on every **website / section** redesign; use the "Dashboards" exceptions for product UI.

## 1. Three dials (set them in the Direction line)
`VARIANCE` 1 symmetric → 10 artsy · `MOTION` 1 static → 10 cinematic · `DENSITY` 1 airy → 10 cockpit.
| Brief | V | M | D |
|---|---|---|---|
| Minimal / calm / editorial | 5-6 | 3-4 | 2-3 |
| Premium consumer / luxury | 7-8 | 5-7 | 3-4 |
| Awwwards / agency / experimental | 9-10 | 8-10 | 3-4 |
| SaaS landing (default marketing) | 7 | 6 | 4 |
| Trust-first / public sector / education admissions | 3-4 | 2-3 | 4-5 |
| Dashboard / admin | 3-4 | 2-3 | 7-9 |
| Redesign, preserve | match | +1 | match |
| Redesign, overhaul | +2 | +2 | match |
Variance > 4 → no centered hero. Density > 7 → numbers in mono/tabular.

## 2. Redesign fix priority (biggest impact, lowest risk first)
1. Font swap → 2. Color cleanup → 3. Hover/active/focus states → 4. Layout & spacing (grid, max-width, padding) → 5. Replace generic components → 6. Loading/empty/error states → 7. Type scale polish.
Work with the existing stack; never break functionality; no framework migrations.

## 3. AI tells to remove (marketing sites)
**Visual**: purple/blue "AI gradient" heroes, neon glows, pure `#000`, oversaturated or multiple accents, gradient text on big headlines, warm+cool greys mixed, untinted generic shadows, random single dark section inside a light page, custom cursors (default off).
**Type**: Inter-everywhere on premium/creative sites (prefer Geist, Satoshi, Outfit, Cabinet Grotesk, General Sans; serif only Fraunces / Instrument Serif / Editorial New for editorial), screaming H1s, Title Case Everywhere (use sentence case), orphans (`text-wrap: balance`).
**Layout**: three equal feature cards, everything centered, `h-screen` (use `min-h-[100dvh]`), uniform radius on everything, CTAs not bottom-aligned in card rows, pricing features starting at different heights.
**Decoration clichés (banned by default)**: section-number eyebrows (`01 / Services`, `(02) —`), `01 / 4` image counters, scroll cues ("Scroll to explore", bouncing chevrons), rotated vertical text, decorative hairline grids, decorative status dots everywhere, locale/time/weather strips, version labels (`V2.0`, `BETA`) in hero, mono-caps word strips (`DESIGN · BUILD · SHIP`), pills overlaid on photos, fake photo credits, div-built fake product screenshots, "Step 1 / Step 2" labels, em-dash as decoration.
**Content**: lorem ipsum, "John Doe", "Acme/Nexus", fake-perfect numbers (99.99%), filler verbs (Elevate, Seamless, Unleash, Next-Gen, Revolutionize), "Oops!", exclamation marks in success messages.
**Components**: modals for everything (prefer inline / slide-over), sun/moon toggle as the only theme control, 4-column footer link farms, 3-card dot carousels for testimonials, generic border+shadow+white cards when spacing would do.

## 4. Do instead
- Hero: asymmetric split or left-aligned; one primary CTA; optional inline images between headline words; real product screenshot or none.
- Features: 2-column zig-zag, bento with mixed spans, horizontal scroll, sticky-stack.
- Surfaces: tinted shadows, subtle grain, radial/mesh gradients in brand hues, 1px inner border for glass.
- Data: organic numbers (47.2%, +1 (312) 847-1928), believable locale-appropriate names (e.g., Bangladeshi/UK names for Hassan's clients).
- Images: `https://picsum.photos/seed/{descriptive}/{w}/{h}` when no assets.
- Full-height sections `min-h-[100dvh]`; CSS Grid over flex math; max-width 1200–1440px.
- Always ship states: hover, active (`scale(0.98)`), focus ring, skeleton loading, composed empty state, inline errors.
- Meta: title, description, og:image, favicon, skip-link, legal links in footer.

## 5. Dashboards / product UI exceptions
Inter is fine when the product kit uses it (Prism). Left sidebar is fine. Status dots are fine when they encode real state (department, live status). shadcn components allowed but never left in pure default state: tune radius, color, shadow, type to the product.

## 6. DESIGN.md (when the user wants a reusable design system doc)
Write `DESIGN.md` with: 1 Visual theme & atmosphere (adjectives + dial values) · 2 Color palette & roles (descriptive name + hex + role) · 3 Typography rules · 4 Component stylings (buttons, cards, inputs, states) · 5 Layout principles (grid, spacing, responsive) · 6 Motion · 7 Anti-patterns. Describe geometry in words ("pill-shaped", "subtly rounded") alongside exact values.
