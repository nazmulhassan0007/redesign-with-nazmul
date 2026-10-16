# Modern App Screen Patterns (web app + mobile)

## Mobile (iOS/Android-feel, 375–430px)
- Safe areas respected; content padding 16–20px.
- Large title (28–34px/700) that collapses to a 17px nav title on scroll.
- Bottom tab bar: 3–5 items, 24px icons, labels 10–11px, active = primary color + filled icon.
- Touch targets ≥ 44×44px; primary button full width, 48–52px tall, radius 12–14px, pinned above the home indicator for key flows.
- Lists: 56–72px rows, leading icon/avatar, title 16px + subtitle 13–14px muted, trailing value/chevron.
- Grouped inset sections (settings style) on a muted background with white rounded cards.
- Bottom sheets for actions/filters instead of new screens; drag handle 36×4px.
- Cards with 16px radius, soft shadow or 1px border, images edge-to-edge on top.
- Segmented controls for 2–4 views; chips for filters (horizontal scroll).
- Empty, loading (skeleton), error, and success states for every screen.

## Onboarding & auth
- 1 idea per screen, illustration/visual top, headline 24–28px, 1–2 lines body, progress dots, primary CTA bottom.
- Auth: social buttons first if supported, email field, clear "Forgot password", minimal fields.

## Web product app (non-dashboard)
- Reuse the shadcn shell from `shadcn-dashboard-patterns.md`.
- Detail pages: header with title, status badge, meta row (owner, date), actions right; content in tabs; side panel for properties (key-value list, label muted, value foreground).
- Settings: left nav + cards per section, save bar sticky at bottom when dirty.
- Multi-step flows: stepper at top, one focused card max-width 560–640px, Back (ghost) + Continue (primary) aligned right.

## Feel
- Motion: 150–250ms for UI transitions, spring for sheets, fade+scale 0.96→1 for dialogs.
- Haptic-like feedback through pressed states (scale 0.98).
- Consistent icon set (Lucide), consistent radius scale.
