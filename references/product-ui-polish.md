# Product UI Polish Pass (exact values)

Distilled from github.com/ibelick/ui-skills (MIT © Julien Thibeaut: baseline-ui, fixing-accessibility, fixing-motion-performance, fixing-metadata, improve-ui) and github.com/jakubkrehel/skills (MIT © Jakub Krehel: better-ui, better-typography, better-layout, better-colors, better-writing, better-accessibility, interface-review). Run this pass on every dashboard/app output, and on the component layer of websites.

## 1. Baseline (product UI)
- Tailwind defaults unless the project has custom values. `cn()` for class logic. `motion/react` for JS animation, `tw-animate-css` for simple entrances.
- Accessible primitives (Base UI / Radix / React Aria) for anything with focus or keyboard; never mix systems in one surface; never hand-roll focus logic.
- `AlertDialog` for destructive actions; errors next to where the action happened; never block paste.
- `h-dvh` / `min-h-dvh`, never `h-screen`; respect `safe-area-inset` (needs `viewport-fit=cover`).
- Fixed z-index scale; `size-*` for squares.
- No gradients, purple/multicolor gradients, or glow affordances in product UI unless asked. One accent per view. Empty states have one clear next action.

## 2. Surfaces & icons (exact)
- **Concentric radius**: outer radius = inner radius + padding (+ border). Past 24px padding treat as separate surfaces.
- **Shadows for elevation, borders for structure**: replace depth-only borders with layered transparent shadows; keep borders on inputs, dividers, table cells, selected states. Under a shadow ring keep `border: 1px solid transparent` (forced-colors).
- **Image outline**: content images get `outline: 1px solid oklch(0 0 0 / 0.1)` (dark: `oklch(1 0 0 / 0.1)`), `outline-offset: -1px`. Never tinted.
- **Optical alignment**: button with icon gets ~2px less padding on the icon side; nudge play triangles toward the point.
- **Icons**: `currentColor`, one library per surface, outline default / filled for active, stroke follows text weight (1.5px at 400 → 2.5px at 700).

## 3. Motion (product UI)
- Press: `scale(0.96)`, 150ms, ease-out; never on `:disabled` (`enabled:active:scale-[0.96]`).
- High-frequency (keystrokes, row hover, tab switch): instant or ≤150ms on opacity/background-color only.
- Interaction feedback ≤ 200ms. Transitions (not keyframes) for interactive state. Name properties, never `transition: all`.
- Staged entrance: chunks (title → description → actions) 100ms apart, each opacity + 4px blur + 12px translateY over 300ms ease-out. Exit: 150ms, -12px, never full height.
- Icon swap (copy→copied, play→pause): scale 0.25→1, opacity 0→1, blur 4px→0; spring `{duration: 0.3, bounce: 0}` or 300ms `cubic-bezier(0.2, 0, 0, 1)`.
- `initial={false}` on AnimatePresence for state swaps. Suppress all transitions during theme switch.
- Hover styles only under `@media (hover: hover)`; `-webkit-tap-highlight-color: transparent` where a control draws its own press state. `overscroll-behavior: contain` on scrollable overlays.
- Every animated change also has a static cue (color/icon/label). Gate movement behind `prefers-reduced-motion: no-preference`; under reduce, cross-fade opacity.
- Performance: animate transform/opacity only; never animate large blur/backdrop-filter surfaces; `will-change` only with the named property during stutter; pause looping animations off-screen.

## 4. Typography (exact)
- Max ~3 fonts. Weight ≥400 below 18px; 100–300 only at 28px+.
- Line-height unitless: display 1.1, headings 1.2–1.3, body 1.5–1.6; anything wrapping 3+ lines ≥1.4.
- Tracking: headings ≥24px −0.01 to −0.02em; uppercase labels ≤14px +0.05em; body 0.
- Measure 60–75ch. `text-wrap: balance` on headings, `pretty` on paragraphs, `overflow-wrap: break-word` for long IDs/links, `nowrap` on badges.
- `tabular-nums` on timers, counters, prices, numeric columns.
- Size floors: long-form body 16px; UI 14px inputs/menus, 13px captions, rarely <12px; set in rem. Inputs 16px on mobile (iOS zoom).
- Natural case in source + `text-transform`; typographic punctuation (curly quotes, en dash, … ellipsis).
- `antialiased` once on root. Set `lang` and `dir`.

## 5. Layout
- Group with space, not lines. Align to shared edges. Order by importance. **One primary (filled) action per view.**
- Controls float, content bleeds; inset buttons from edges; borderless controls need more clearance; hint at hidden/scrollable content.
- Fixes: `minmax(0,1fr)` / `min-width:0` for overflow; `width:100%` not `100vw`; `min-height` not fixed heights on text boxes; `@container` in reusable components; `scroll-padding-top` = sticky header height.

## 6. Color
- Ramps not single colors; every step has a job; primitives named by hue, semantics by role (`--color-accent-solid`, `--color-bg-surface`); components use semantic tokens only.
- Hold hue across a ramp (build in OKLCH); light end steps ~0.04–0.05 L apart.
- One color, one meaning; status hues ≥15° away from the accent hue.
- Fix contrast by changing lightness, not hue. White text on a Tailwind 500 fill usually fails 4.5:1 → use 600.
- Dark mode is not the reversed light ramp: lower accent chroma, re-measure every pair. One switching mechanism (class OR media query).

## 7. Writing (UI copy)
- Address the reader; plain words; one vocabulary and one capitalization policy.
- Buttons verb + object ("Delete project"), never OK/Yes/No. Links name their destination (no "click here").
- Errors say what failed + how to fix, next to the field; no "Oops", no "!", no "successfully" ("Changes saved").
- Undo beats confirmation; "Are you sure" → name the action and object. Toggles describe the ON state.
- Empty states point forward. Placeholders show an example. Dates via `Intl.DateTimeFormat` with locale.

## 8. Accessibility (critical first)
1. Names: every control labeled; icon-only buttons `aria-label` naming the action ("Close dialog"); decorative icons `aria-hidden`.
2. Keyboard: native `<button>`/`<a>`, everything reachable by Tab, no positive tabindex, Escape closes overlays.
3. Focus: visible `focus-visible` ring (never bare `outline-none`); dialogs trap and restore focus.
4. Semantics: native first, no skipped headings, `th` in tables.
5. Forms: errors linked via `aria-describedby`, `aria-invalid`, required announced; keep submit enabled and validate on submit.
6. Announcements: `role="status"` for success, `aria-live` region rendered empty first; `aria-expanded/controls` on disclosures.
7. Contrast 4.5:1 text, 3:1 UI boundaries; never color alone; hit area ≥ 24px (44px touch).
8. Never `user-scalable=no`; nothing essential on a timer; drag has a single-pointer alternative.

## 9. Metadata (websites)
`<title>`, meta description, canonical, Open Graph + Twitter image, favicon set, `lang`, theme-color, structured data where relevant.

## 10. Audit/review output
- **Audit of an existing surface** (improve-ui method): reconstruct the design language first (sources, decisions, exceptions), keep a finding only with contract + runtime + one correction, report max 3:
`| # | Problem | Evidence | Proposed change | Scope | Confidence |` then "Improve first".
- **Review of a change/PR** (interface-review method): review the change not the codebase; read removed lines for regressions (deleted aria-label, outline, reduced-motion); tag each finding `Introduced` / `Regression` / `Pre-existing`; check every new variant has hover, focus, active, disabled, loading, selected, empty, error, narrow states.
