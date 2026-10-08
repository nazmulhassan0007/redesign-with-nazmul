# Icons — Hugeicons (default set)

Default icon set for redesign-with-nazmul: **Hugeicons Free, stroke-rounded** (6,000+ icons, MIT © Hugeicons). Bundled offline in `tools/hugeicons/` so HTML outputs get real inline SVGs with no CDN.

## Which library
1. The project already uses an icon library → keep it (one library per surface).
2. Otherwise → Hugeicons Free stroke-rounded.
3. User owns Hugeicons Pro and asks for another style (Soft, Duotone, Solid, Bulk, Twotone…) → use `@hugeicons-pro/*` packages in *their* project; never paste Pro SVGs into this skill or public repos.

## Plain HTML output
```bash
python3 <skill-dir>/tools/hugeicons/icon.py search user add          # find names
python3 <skill-dir>/tools/hugeicons/icon.py svg home-01 search-01 --size 20
python3 <skill-dir>/tools/hugeicons/icon.py sprite home-01 user-add-01 > sprite.svg
```
Inline the SVG (or the sprite + `<svg><use href="#hi-home-01"/></svg>`). Icons use `currentColor`; size via width/height. If bash is unavailable, write the icon name in a comment and use a simple placeholder shape.

## React output
```bash
npm i @hugeicons/react @hugeicons/core-free-icons
```
```tsx
import { HugeiconsIcon } from "@hugeicons/react";
import { Home01Icon, Search01Icon } from "@hugeicons/core-free-icons";
<HugeiconsIcon icon={Home01Icon} size={20} strokeWidth={1.5} />
```
With shadcn Buttons: pass `data-icon="inline-start"` and let the component size it (see `shadcn-official-rules.md`).

## Sizing & stroke
| Context | Size | Stroke |
|---|---|---|
| Buttons, inputs, nav, table actions | 16–20px | 1.5 |
| Sidebar nav (Prism style) | 20–24px | 1.5 |
| Feature/empty-state icon in a tinted circle | 24px inside a 40–48px circle | 1.5 |
| Next to bold text (600–700) | match text | 2 |
Outline = default, filled/colored = active state. Recolor with CSS (`currentColor`), never separate assets. Decorative icons `aria-hidden="true"`; icon-only buttons get `aria-label` naming the action.

## Common names (stroke-rounded)
home-01 · dashboard-square-01 · search-01 · notification-01 · mail-01 · settings-01 · user · user-add-01 · user-group · calendar-03 · clock-01 · file-01 · folder-01 · chart-line-data-01 · analytics-01 · money-01 · credit-card · shopping-cart-01 · filter · sort-by-down-01 · more-horizontal · more-vertical · plus-sign · cancel-01 · tick-02 · edit-02 · delete-02 · download-01 · upload-01 · share-08 · link-01 · arrow-right-01 · arrow-left-01 · arrow-down-01 · arrow-up-right-01 · logout-01 · menu-01 · sun-03 · moon-02 · star · favourite · location-01 · call · message-01 · bubble-chat · briefcase-01 · school · mortarboard-01 · globe-02 · airplane-01 · building-03 · task-01 · checklist · alert-02 · information-circle · help-circle · lock · eye · image-01 · video-01 · play · pause
Names change between versions; always confirm with `icon.py search`.
