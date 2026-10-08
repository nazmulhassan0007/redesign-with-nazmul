# Prism Dashboard UI Kit — HR Dashboard Patterns

Source: Hassan's Figma file "Prism Dashboard UI Kit – Desktop", page **HR** (fileKey `d5PebFT1ihU7rZs68Jvse0`, page `0:3163`). Values below were read directly from the file (styles, fills, fonts, frame sizes). 9 screens at 1440px: HR Dashboard, Company, Report, Department, Employee's List, Employee's Box (grid), Payroll, Time off, Calendar.

Use Prism when the product is **HR, ATS, people-ops, enterprise back-office, or the user wants a friendly blue SaaS look** instead of the monochrome shadcn kit. Tokens: `assets/tokens-prism.css`.

## Contents
1. The look
2. Tokens (exact)
3. App shell (exact sizes)
4. Page header patterns
5. Screen recipes (9 screens)
6. Component details
7. Redesign upgrades to apply on top of Prism

---

## 1. The look
Light grey canvas (`#F6F6F6`), white cards with a barely-there shadow (`0 1px 3px rgba(0,0,0,.08)`) and **small radius (4–8px)**, one strong blue (`#1F7BF4`) for primary buttons, active nav, links, and the main chart series, with light blue (`#00AAFF`) as the second series. Status uses 8%-opacity tinted pills. Everything Inter. Calm, enterprise, highly scannable.

## 2. Tokens (exact, from Figma styles)
**Brand**: Primary `#1F7BF4` · Secondary light blue `#00AAFF` · Secondary dark blue `#0B438D`
**Neutrals ("Dark")**: 1 `#202020` (headings/body) · 2 `#484848` (secondary text) · 3 `#84818A` (muted text, icons, dotted lines) · 4 `#E8E8E8` (borders/lines) · 5 `#F6F6F6` (canvas) · 6 `#FFFFFF` (cards)
**Signals**: Success `#0AA630` · Alert `#FC0000` · Orange `#FFA043` · Pink `#FA699D` · (Rating gold `#D8A049`, silver `#919191`, bronze `#955D3E`)
**Faded (tint backgrounds)**: each brand/signal color at **8% opacity** behind its full-color text → status pills, active nav row, highlighted list item, icon circles.
**Type** (Inter):
- H1 Semi Bold 36/46 — page titles ("Payroll", "Good morning, Justin")
- H2 Semi Bold 24 · H3 Semi Bold 18/24 — card titles
- H4 16/20 Regular & Medium — list titles, nav items
- H5 14 Regular/Medium/Semi Bold — body, table cells (14/24 for paragraphs)
- H6 12 Regular/Medium/Semi Bold — meta, table headers, emails, dates
- Numbers: Big Bold 32 · Medium Bold 24 · Small Semi Bold 14
- Delta text: Medium 14 in success/alert color
**Radius**: 2 (pills/badges, small tags), 4 (buttons, inputs, cards), 8 (larger cards/panels). Avatars round.
**Shadow**: Shadow/1 `0 1px 3px rgba(0,0,0,.08)` on cards. No heavy shadows.
**Lines**: 1px `#E8E8E8` row dividers; dotted `#84818A` timeline line.

## 3. App shell (exact sizes)
- **Sidebar 250px**, white, right border `#E8E8E8`. Top: ☰ menu icon + logo mark + "Prism" wordmark (72px tall row, aligned with header). Nav items ~46px tall, 24px icon + 16px label, grouped with extra gap: [Dashboard, Department, Employees] · [Calendar, Payroll, Time off, Report, Company] · [Settings]. **Active**: `#1F7BF4` 8% background + 4px left blue bar + blue icon & text. Bottom: "Light mode" label + sun/moon segmented toggle.
- **Header 72px**, white, bottom border: search (icon + "Search…") left; right: bell with red dot, mail icon, avatar 32–36px + name (Medium 16) + role line ("Admin – Designspace", 12 muted).
- **Content**: starts at x=290 → **40px gutter**, right margin 40px, max width 1110px at 1440. Card gap **24px**. Card inner padding **24px**.

## 4. Page header patterns
- **Greeting**: "Good morning, Justin" (H1) + muted subline "Here's what's going on with your team Designspace"; right: weekday (Semi Bold 18) over date (16 regular).
- **Title + actions**: H1 left; right: view toggle (grid/list segmented, outline) + primary button ("Add Employee", "Print Report", "Create time-off", "Add Task"), sometimes an outline secondary ("Assign to..").
- **Department tabs** under the title: All Employee · Marketing · Accounting · Cs. Support · Finance · Human Resource · IT Support — text tabs, active = dark text + 2px blue underline, full-width 1px divider.

## 5. Screen recipes
- **HR Dashboard (home)**: greeting header → onboarding banner card (blue 1px border, icon in light-blue circle, title + description, "Get Started" primary right) → 2 columns: **Things to do** (vertical timeline: dotted line + dots, active item highlighted blue 8% bg with 4px left bar, date top-right, "View All Things to do →" link) 732px | **Suggested** 354px (dismissible suggestion card with blue border + close ✕ + text link; "Upcoming" list rows with date, description, optional avatar; "Add reminder to your calendar" icon link).
- **Report**: greeting → **4 KPI cards** (259×118: label 14 → value Bold 24 + delta "−9.98%" with red/green square arrow icon) → "Mancount per Department" wide card (donut with "Total Employee 350.5k" center + 2-column legend table with color dots, New, Total) → 2×2 grid: horizontal bar chart (Average Performance), grouped vertical bars (Overtime: This week vs Last week), bar chart + side stats ($3,575 Avg Salary / 85.0% Salary Payed / $24,500 Total Payout), Bonus Performance table with "View All →" link. Card headers have a "This month ▾" muted dropdown on the right.
- **Company**: Total Sales grouped bar chart (2/3) + Employee Satisfaction donut (1/3, % in center, legend list with counts) → MRR and Net Revenue area-line cards (big value + delta + "in selected period") → Announcement list (red dots, relative time) + Files list (file-type icons, `⋯`).
- **Department**: tabs → department summary strip (icon circle, name, "76 Total employee" with people icon; 4 inline mini KPIs with arrow badges) → Avg KPI's Index two-line area chart (2/3) + On-Time Accuracy ring (1/3) with a feedback footer row (smiley icon + "It's good enough / But we think it can be better") → Overtime grouped bars (Hire/Resign) + Team Performance table with small circular progress indicator per row (85%, 75%, 40%).
- **Employee's List**: title + view toggle + "Add Employee" → tabs → table card: ID · Name (avatar + name + email) · Position · Department (colored dot + name) · Phone (phone icon) · Status pill (Contract light-blue, Full time green, Intern red; 8% tint) · `⋯`. Sortable "Name ↓".
- **Employee's Box**: same header; 3-column card grid: avatar + name + email + status pill on top, divider, then key–value rows (ID, Position, Department with dot, Phone) label muted left / value right → pagination.
- **Payroll**: "Print Report" → **Information card** (circular progress ring with info icon, "Your payment status for this month is paid in 65%" with the % in orange; right: Total Payroll $120,630, Deadline 25 March 2021) → tabs → table: ID, Name, Position, Gross pay, Tax, Total (coin icon), Status (Complete green / Pending dark-blue / Failed red), `⋯` → footer "Show 11 from 36 employee's" + pagination (‹ Previous · 1 (boxed) 2 3 4 … 12 · Next › in blue).
- **Time off**: tabs → timeline/Gantt card: left column employee list with search (avatar, name, role), right a day grid grouped by month (March / April), today column shaded light blue; leave bars = white chips with a 3–4px colored left border (blue Time-off, green Holiday, red Sick) spanning days.
- **Calendar**: card with "March 2021 ‹ ›" + view select (Week ▾) + ‹ Today › segmented; week grid with hour labels; events = tinted blocks (8–15% color) with a 3px top border in the category color, time range in color, title, and a small white department tag with dot at the bottom.

## 6. Component details
- **Buttons**: primary blue fill, white Medium 14, radius 4, height 40; outline secondary white with `#E8E8E8` border + icon; text links blue with → arrow.
- **Status pill**: radius 2, 12px Medium, padding 2×8, text in color, background same color 8%.
- **Department dot**: 6–8px circle in a category color (Marketing light blue, Accounting green, Cs. Support red, Finance grey, HR orange, IT pink).
- **KPI delta**: number in success/alert + 14px square icon tile with diagonal arrow.
- **Charts**: thin bars (8–12px) with rounded tops, two-series in blue + light blue, horizontal grid lines `#E8E8E8`, 12px muted axis labels, area charts with 8–15% blue fill, donuts with thick stroke (~12px) + rounded segment gaps.
- **Table**: header 12px muted (no background), rows ~46px with 1px dividers, 14px cells, avatar 32px.
- **Icon circles**: 40–48px circle, brand color 8% background, 20–24px icon in brand color.

## 7. Redesign upgrades to apply on top of Prism
Keep Prism's palette and structure, but fix these when redesigning with it:
- Use `tabular-nums` and right-align money columns (Prism left-aligns them).
- Replace pure `#FC0000` red text/pills with a slightly deeper red (e.g., `#D92D20`) for AA contrast on white; same for `#00AAFF` text (use `#0B438D` text on the 8% light-blue pill).
- Consistent number formatting (Prism mixes "75,5%" and "85.45%"); pick one locale.
- Replace lorem ipsum with real task copy; fix typos ("Finnish", "Mancount", "Speciaist").
- Add hover/focus states, empty states, and skeletons; make the department tabs scroll horizontally on small screens.
- On narrow screens collapse the 250px sidebar to icons (72px) and stack 2-column rows.
