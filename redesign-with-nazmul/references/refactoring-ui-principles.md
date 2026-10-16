# Refactoring UI — Working Principles

Actionable rules distilled (in our own words) from the ideas in *Refactoring UI*. Use as an audit checklist and a build guide.

## Contents
1. Start with the feature, not the layout
2. Hierarchy
3. Layout & spacing
4. Typography
5. Color
6. Depth
7. Images & icons
8. Finishing touches

---

## 1. Start with the feature
- Design the actual functionality first (the form, the table, the card), not the app shell/nav.
- Work in greyscale first; add color last. This forces hierarchy through spacing, weight, and contrast.
- Don't design every edge case up front, but always design empty states.
- Pick a personality early: rounded + playful vs sharp + serious; this drives radius, font, and color.
- Limit choices with systems: a fixed spacing scale, type scale, color palette, shadow scale.

## 2. Hierarchy
- Not everything is equally important. Decide primary / secondary / tertiary for every element.
- Size isn't the only lever. Use **font weight** (400 vs 600) and **color** (foreground vs muted) first.
- Use 2–3 text colors: dark for primary, grey for secondary, lighter grey for tertiary.
- Use 2 weights in UI: normal (400/500) and bold (600/700). Avoid weights <400 for UI text.
- Emphasize by de-emphasizing: if the active item doesn't pop, make the inactive items quieter instead of making the active one louder.
- Labels are a last resort. Prefer "12 left in stock" over "Stock: 12". When a label is needed, make it secondary (small, muted) and the value primary.
- Separate visual hierarchy from document hierarchy: an h1 can be visually small (e.g., a page title in an app).
- Balance weight and contrast: heavy icons next to text should get a softer color; thin borders may need more contrast.
- Semantic ≠ visual: a destructive action that's secondary on the page should be a secondary/ghost button, red only on the confirm step.
- Buttons: primary = solid, secondary = outline or soft fill, tertiary = link style.

## 3. Layout & spacing
- **Start with too much white space, then remove.** Dense UIs are a deliberate choice, not a default.
- Use a constrained spacing scale (4px base): 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Neighboring values should differ by ≥ ~25%.
- More space between groups than within groups. Ambiguous spacing is the #1 cause of "messy" UIs.
- You don't need to fill the screen. Give components the width they need (forms ~ 400–600px), not 100%.
- Grids are overrated for components: fixed-width sidebars + flexible content beats a rigid 12-col percentage grid.
- Relative sizing doesn't scale: large elements shrink faster than small ones on mobile; set sizes per breakpoint.

## 4. Typography
- Use a hand-picked type scale, e.g. 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72.
- Use px/rem, not em, for scale steps (avoids compounding).
- Good UI fonts: neutral sans with many weights (Inter, Geist, Manrope, Plus Jakarta Sans, General Sans). Avoid fonts with < 5 weights for UI.
- Line length 45–75 characters for paragraphs (`max-width: 65ch`).
- Line height is inverse to size: body 1.5–1.7, headings 1.1–1.25, big display 1.0–1.05.
- Tighten letter-spacing on large headlines (−0.02 to −0.04em); add tracking to small all-caps labels (+0.05em).
- Baseline-align mixed font sizes on one line, not center-align.
- Not every link needs a color; in dense nav, use weight/darker color and underline on hover.
- Left-align body text; center only short blocks (≤ 2–3 lines). Right-align numbers in tables.

## 5. Color
- Use HSL/OKLCH thinking, not hex guessing.
- You need more colors than you think: greys (8–10 shades), a primary (5–10 shades), and semantic accents (red, amber, green, blue) each with shades.
- Define shades up front: pick the base (500), the darkest (900, for text on light tint), the lightest (50, for tinted backgrounds), then fill gaps.
- Greys don't have to be pure grey: tint slightly cool (blue) or warm (yellow/orange) to match the brand.
- As lightness moves toward the extremes, increase saturation so colors don't look washed out.
- Don't use grey text on colored backgrounds; use a lighter/darker tint of the background hue instead.
- Accessibility: 4.5:1 for normal text, 3:1 for large text. If white-on-color fails, flip to dark-on-light-tint.
- Never rely on color alone — pair with icons, text, or shape.

## 6. Depth
- Light comes from above: raised elements get a lighter top edge and a shadow below; inset elements get a darker top.
- Use a shadow elevation scale (5 levels: xs for buttons, sm for cards, md for dropdowns, lg for popovers, xl for modals).
- Good shadows have two parts: a tight, darker one (direct light) + a large, soft one (ambient).
- Flat designs can show depth with color: lighter = closer, darker = farther.
- Overlap elements (cards crossing section boundaries, avatars overlapping) to create layers.
- Fewer borders. Instead: box shadow, a different background tone, or extra spacing.

## 7. Images & icons
- Use good photos or none. Text over images needs an overlay, lowered contrast image, or text shadow.
- Don't scale up small icons (24px icons at 64px look clunky): wrap them in a tinted shape instead.
- Don't scale down screenshots; crop to the relevant part or redraw a simplified version.
- User-uploaded images: fix aspect ratio with `object-fit: cover`; add a subtle inner shadow/ring to prevent background bleed.

## 8. Finishing touches
- Supercharge defaults: replace bullets with icons/checks, style blockquotes, use custom checkboxes/radios in brand color.
- Add accent borders (a 3–4px colored top border on cards, a left border on alerts, an underline on active nav).
- Decorate backgrounds subtly: a slight color shift between sections, a faint pattern, or a gradient of two close hues.
- Design empty states with an illustration/icon + one clear CTA.
- Think outside the obvious: tables don't have to be plain text (combine columns, add avatars, badges); radio buttons can be selectable cards.
