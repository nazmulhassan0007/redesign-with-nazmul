# Motion & Interaction Polish (Emil Kowalski's design-engineering rules)

Distilled from github.com/emilkowalski/skills (MIT © Emil Kowalski): emil-design-eng, animate, improve-animations, review-animations. Use for every interactive state and animation you add.

## 1. Should it animate at all?
| How often users see it | Decision |
|---|---|
| 100+/day (keyboard shortcuts, ⌘K toggle) | No animation |
| Tens/day (hover, list nav) | Remove or reduce drastically |
| Occasional (modals, drawers, toasts) | Standard animation |
| Rare (onboarding, celebrations) | Can add delight |
Never animate keyboard-initiated actions. Every animation needs a purpose: spatial consistency, state change, explanation, feedback, or preventing a jarring jump. "Looks cool" on a frequent element = no.

## 2. Easing
- Entering/exiting → ease-out. Moving/morphing on screen → ease-in-out. Hover/color → ease. Constant motion (marquee, progress) → linear.
- **Never ease-in for UI** (feels sluggish).
- Use strong custom curves:
```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
```

## 3. Duration
Button press 100–160ms · tooltip/small popover 125–200ms · dropdown/select 150–250ms · modal/drawer 200–500ms · marketing can be longer. **UI animations stay under 300ms.** Exit faster than enter. Stagger lists 30–80ms per item.

## 4. Springs
Use for drag with momentum, "alive" elements, interruptible gestures, decorative mouse-follow. Prefer `{ type: "spring", duration: 0.5, bounce: 0.2 }`; keep bounce 0.1–0.3, none in most UI. Springs keep velocity when interrupted.

## 5. Component rules
- Buttons: press to `scale(0.96)` over ~150ms ease-out, never when disabled.
- Never enter from `scale(0)`; start at `scale(0.95)` + `opacity: 0`.
- Popovers/dropdowns scale from their trigger (`transform-origin` at trigger); modals stay centered.
- Tooltips: delay the first one, then show instantly (no delay, no animation) while moving across a toolbar.
- Prefer CSS transitions over keyframes for things triggered rapidly (interruptible).
- A little `filter: blur()` during crossfades hides the double-image look.
- Enter states with `@starting-style` for CSS-only mount animations.
- `clip-path: inset()` for reveals, tabs with perfect color transitions, hold-to-confirm, comparison sliders.
- Height + opacity together for list items entering/leaving (Sonner principle).

## 6. Performance & accessibility
- Animate only `transform` and `opacity` (never width/height/top/left; never `transition: all`).
- Under load, CSS animations beat JS; use WAAPI for programmatic CSS animation.
- Respect `prefers-reduced-motion` (keep fades, drop movement).
- Gate hover effects: `@media (hover: hover) and (pointer: fine)`.

## 7. Review table format
When reviewing someone's UI code/motion, output one table:
| Before | After | Why |
|---|---|---|
| `transition: all 300ms` | `transition: transform 200ms var(--ease-out)` | Exact properties, faster |
| `scale(0)` entry | `scale(0.95); opacity: 0` | Nothing appears from nothing |
| `ease-in` dropdown | `ease-out` custom curve | Instant feedback |
| No `:active` on button | `scale(0.96)` (not when disabled) | Press must feel heard |
| Same enter/exit speed | Exit faster | Get out of the way |
