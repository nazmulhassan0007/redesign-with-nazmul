# shadcn UI Kit Dashboard Patterns

Source of truth: **github.com/bundui/shadcn-ui-kit** (MIT, © Mohd. Nisab), the free edition of shadcnuikit.com. Stack: Next.js 16, React 19, Tailwind v4, Recharts 3, TanStack Table 8, `motion`, Lucide icons (Tabler icons in admin). shadcn style `radix-luma`, base color **neutral**. Component catalog: `shadcn-ui-kit-components.md`.

## Contents
1. The look in one paragraph
2. Tokens
3. App shell (exact values)
4. Page header
5. KPI / stat cards (two kit variants)
6. Charts
7. Data tables
8. Dashboard recipes (16 kit dashboards)
9. Dark mode & details

---

## 1. The look
Monochrome first. Pure neutral greys (chroma 0), **primary is near-black** (`oklch(0.205 0 0)`), charts in shades of grey/black, color only for meaning (green up / red down, status badges). White cards with a faint ring instead of heavy borders, rounded-full buttons and badges, big rounded cards, generous 24px card padding. Feels calm, editorial, data-first. Add a brand accent only if the user has one — and then only on primary actions, active nav, and chart-1.

## 2. Tokens
Use `assets/tokens.css` (copied from the kit's `globals.css`). Key values:
- `--radius: 0.45rem` → `radius-sm/md/lg/xl` = radius −4 / −2 / 0 / +4px.
- Cards: `rounded-4xl`, `shadow-md ring-1 ring-foreground/5` (dark: `ring-foreground/10`), `--card-spacing: 24px` (sm size: 16px).
- Buttons: `rounded-4xl` (pill). Sizes: xs h-6, sm h-8, default h-9, lg h-10; icon sizes 24/32/36/40. Hover = `primary/80`; press = `translate-y-px`; focus `ring-3 ring-ring/30`.
- Destructive buttons/badges are **soft**: `bg-destructive/10 text-destructive`, never solid red.
- Badges: h-5, `rounded-3xl`, text-xs/500, svg size-3. Variants: default, secondary, destructive (soft), outline, ghost, link.
- Kit also defines a `--base-50 … --base-1000` neutral ramp (zinc-tinted) for custom surfaces.

## 3. App shell (from `app/admin/(dashboard)/layout.tsx`)
```tsx
<SidebarProvider style={{"--sidebar-width":"calc(var(--spacing) * 72)", "--header-height":"calc(var(--spacing) * 12)"}}>
  <AppSidebar variant="inset" collapsible="icon" />
  <SidebarInset>
    <SiteHeader />
    <div className="@container/main flex flex-1 flex-col">
      <div className="flex flex-col gap-4 p-4 md:gap-6 lg:p-6">{children}</div>
    </div>
  </SidebarInset>
</SidebarProvider>
```
- Sidebar **288px**, `variant="inset"` (content floats as a rounded panel on the sidebar-colored canvas), collapses to icons.
- Sidebar parts: logo + product name (size-6 logo) → NavMain groups (Dashboards, Apps, Pages) with collapsible sub-items and "New"/"Coming" badges → NavSecondary (`mt-auto`) → promo card ("Download / Get…" with a dark button) → NavUser (avatar, name, email, menu).
- Header **48px**, `border-b`: SidebarTrigger → vertical Separator (h-4) → page title (text-base/500) or search with `⌘K` kbd → right: notifications (dot), theme toggle, settings, avatar.
- Use **container queries** (`@container/main`, `@xl/main:grid-cols-2 @5xl/main:grid-cols-4`) so grids react to the content width, not the viewport (sidebar open vs collapsed).

## 4. Page header
`h1 text-2xl font-bold tracking-tight` ("Dashboard" or "Welcome Toby") left; right: date-range picker button ("21 Aug 2025 – 17 Sep 2025" with calendar icon, outline) + **Download** (primary, black). Optional Tabs under it.

## 5. KPI / stat cards
**A. Admin "SectionCards"** — grid `grid-cols-1 gap-4 @xl/main:grid-cols-2 @5xl/main:grid-cols-4`, each card `bg-gradient-to-t from-primary/5 to-card shadow-xs`:
- CardHeader: CardDescription (label) → CardTitle `text-2xl font-semibold tabular-nums @[250px]/card:text-3xl` → CardAction: `Badge variant="outline"` with trend icon + "+12.5%".
- CardFooter `flex-col items-start gap-1.5 text-sm`: bold line "Trending up this month ↗" + muted context line.

**B. Stat-cards block** — `shadow-none` cards on a `bg-muted` page; title `text-sm font-medium text-muted-foreground`, CardAction = ghost `⋯` dropdown (Settings, Add Alert, Pin to Dashboard, Share, — Remove destructive); value `text-2xl font-bold tracking-tight` + outline badge colored green/red with ArrowUp/ArrowDown; footer "vs last month: 105,922" muted.

Other KPI styles seen in the kit's dashboards: greeting card ("Congratulations Toby! 🎉" + big value + "View Sales" button), KPI with inline bar sparkline, KPI with progress bar, review score card (4.5 ★ + rating distribution bars), donut with center total ("10.2K").

## 6. Charts (`components/ui/chart.tsx` + Recharts)
- Wrap in `Card @container/card`; header has title + description and a **range switcher**: ToggleGroup (Last 3 months / 30 days / 7 days) shown at `@[767px]/card:flex`, collapsing to a Select below that width.
- Chart container `aspect-auto h-[250px] w-full`, content padding `px-2 pt-4 sm:px-6 sm:pt-6`.
- Monochrome palette: bars black, secondary series light grey; area charts with gradient fill; thin line charts with a second dashed/grey comparison line.
- Minimal axes: no axis lines, 12px muted ticks, horizontal grid only (`vertical={false}`).
- Tooltip `rounded-lg`, indicator dot.

## 7. Data tables (TanStack, `components/admin/data-table.tsx`, `tables/1–7` blocks)
- Toolbar: filter input ("Filter emails…") left; **Columns** dropdown (column visibility) right; optional faceted filters & "Add" primary.
- Header row `hover:bg-transparent`, muted 13px text. Row actions: ghost `⋯` → dropdown.
- Numbers `text-right tabular-nums`; totals `text-base font-semibold`.
- **Responsive trick** from the blocks: secondary columns `hidden sm:table-cell`, and on mobile show that info stacked under the main cell (`text-muted-foreground text-xs sm:hidden`).
- Status badges: soft tinted pills (New Order blue, In Progress amber, Completed green, Cancelled red).
- Summary row inside a nested `rounded-xl border p-3` box for totals.
- Empty: `h-24 text-center text-muted-foreground` "No results."
- Footer: "0 of 68 row(s) selected." + Rows per page select + Page x of y + first/prev/next/last icon buttons.

## 8. Dashboard recipes (kit's 16 dashboards)
- **Classic/Default**: Team members list (avatar, name, email, role select) · Subscriptions (+4850 bar chart) · Total revenue line · Chat card · Exercise minutes line (2 series) · Latest payments table · Payment method selector cards.
- **E-commerce**: Greeting card · KPI row (revenue, sales, users growth) · Total revenue bar chart with 2 mini stats · Returning rate line · Sales by location (progress bars per country) · Store visits by source (donut) · Customer reviews (stars + distribution).
- **Sales**: Revenue bar chart (many thin bars) with Orders/Sales mini KPIs · 4 KPI cards (Total balance, Income, Expense, Tax) · Best selling products (thumbnail list) · Track order status (counts by status + progress + orders table).
- **CRM**: leads KPIs, pipeline/funnel by stage, leads by source, recent deals table, tasks.
- **Project management**: project progress, task summary, team, timeline.
- **File manager**: storage usage, folders grid, recent files table, Upload button.
- **Finance / Payment / Crypto / Analytics / Website Analytics / Hospital / Hotel / Academy-School**: same skeleton — page header + KPI row + 1 wide chart + 1–2 list/donut cards + table.
- **17 web apps**: Kanban, Todo, Calendar, Notes, Chats, Mail, File manager, Social media, etc.
- **Bento rule**: mix spans (`lg:col-span-2`, `xl:col-span-3` of 7 etc.) so rows aren't identical boxes.

## 9. Dark mode & details
- Dark: background `oklch(0.145 0 0)`, card `0.205`, borders `white/10%`, inputs `white/15%`; primary flips to light grey (`0.922`) with dark text. Sidebar primary in dark gets a blue accent (`oklch(0.488 0.243 264)`).
- Menus are `default-translucent` with subtle accent.
- Kbd hints (`⌘K`) in search; skeletons mirror content geometry; Sonner for toasts.
- Base text 14px (`text-sm` everywhere in cards); 12px only for meta/badges.
