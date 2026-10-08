# shadcn UI Kit — Component Catalog & When to Use

From github.com/bundui/shadcn-ui-kit (`components/ui`, `contents/components`, `contents/blocks`). Numbers = how many variants the kit ships, so you know rich options exist. Install any with the shadcn CLI (`npx shadcn@latest add <name>`); if output must be plain HTML, recreate the same classes.

## Primitives (components/ui)
accordion, alert, alert-dialog, attachment, autocomplete, avatar, badge, breadcrumb, bubble (chat bubble), button, button-group, calendar, card, carousel, chart, checkbox, collapsible, command, context-menu, dialog, drawer, dropdown-menu, empty, field, form, highlighter, hover-card, image-zoom, infinite-slider, input, input-group, item, kbd, label, menubar, native-select, navigation-menu, pagination, popover, progress, radio-group, resizable, scroll-area, select, separator, sheet, sidebar, skeleton, slider, sonner, spinner, switch, table, tabs, textarea, toggle, toggle-group, tooltip.

## Variant library (contents/components)
button 27 · input 26 · avatar 21 · button-group 20 · badge 17 · alert-dialog 16 · separator 16 · alert 15 · calendar 15 · radio-group 15 · select 15 · tabs 15 · spinner 14 · carousel 13 · checkbox 13 · slider 13 · accordion 12 · combobox 12 · dropdown-menu 12 · pagination 12 · sonner-toast 12 · table 12 · field 10 · item 10 · progress 10 · switch 10 · card 9 · native-select 9 · collapsible 8 · command 8 · empty 8 · toggle 8 · tooltip 8 · bubble 7 · file-upload 7 · sheet 7 · skeleton 7 · breadcrumb 6 · data-table 6 · drawer 6 · popover 6 · scroll-area 6 · attachment 5 · autocomplete 5 · navigation-menu 4 · hover-card 3

## Blocks (contents/blocks)
- dashboard-ui: stat-cards, tables (7), sign-in-forms, modal-dialogs (16+)
- application-ui: todo-app
- marketing: hero-sections, how-it-works, faqs, newsletter-sections
Admin template (`components/admin`): app-sidebar, nav-main, nav-secondary, nav-user, site-header, section-cards, chart-area-interactive, data-table. Admin pages: dashboard, users (TanStack table), settings (sidebar-nav + profile-form), login, register, 404, 500.

## Picking the right component (redesign swaps)
| Old pattern | Replace with |
|---|---|
| Plain `<select>` with many options | Combobox (searchable) or Select; NativeSelect on mobile forms |
| Long list of checkboxes for one choice | RadioGroup as selectable cards |
| On/off checkbox setting | Switch inside an Item row (title + description + control) |
| Confirm with `alert()` | AlertDialog (destructive action soft-red) |
| Detail page for a row | Sheet (right drawer) or Drawer on mobile |
| Toolbar of loose buttons | ButtonGroup / ToggleGroup |
| Search box in header | Command palette (⌘K) with Kbd hint |
| "No data" text | Empty (icon + title + description + action) |
| Spinners for page load | Skeleton matching layout; Spinner only inside buttons |
| Raw label + input stacks | Field (label, description, error) + InputGroup for addons/icons |
| Upload input | File-upload dropzone + Attachment chips |
| Chat UI | Bubble + Avatar + InputGroup composer |
| Flash messages | Sonner toast |
| Long settings page | Tabs or settings sidebar-nav + Cards |
| Logo row | InfiniteSlider (marquee) |
| Product image | ImageZoom |
| Plain list rows | Item (media + title + description + actions) |
| Key metric | Card with CardAction badge (see dashboard patterns §5) |
