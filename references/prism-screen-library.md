# Prism Kit — Full Screen Library

All products in Hassan's Figma "Prism Dashboard UI Kit – Desktop" (fileKey `d5PebFT1ihU7rZs68Jvse0`). Every screen shares the Prism shell and tokens (`prism-dashboard-patterns.md`, `assets/tokens-prism.css`). Use this file to pick a proven layout for a domain. If Figma tools are available, open a frame by its node id to see it (`get_screenshot`).

Status: ✅ = recipe captured below · 📋 = frame listed only (layout not yet captured — open it in Figma before copying).

## Shell variations seen across products
- **Workspace card** at the top of the sidebar (avatar/logo + "Designspace · 16 Members" in a rounded `#F6F6F6` box) — team products (Freelance).
- **Profile + progress** sidebar header (avatar, name, "Premium Plan" ▾, then EXP and Level progress bars with numbers) — gamified products (Online Learning).
- **Count badges** on nav items: blue pill for neutral counts (Projects 28, Tasks 16), red pill for urgent (Work Inquiry 12, Inbox 2).
- Expandable nav groups with chevron (Dashboard ▾, Reports ▾).
- Header right: bell (red dot), mail, avatar + name + ▾.

## HR — page `0:3163` ✅
Company `0:3164`, Report `0:3604`, Time off `0:4058`, Payroll `0:4461`, Calendar `0:5056`, Employee's List `0:5428`, Employee's Box `0:5998`, Department `0:6609`, HR Dashboard `0:7057`. Recipes in `prism-dashboard-patterns.md` §5.

## Freelance Tools — page `0:7335`
- ✅ **Dashboard** `0:11175` — "Hi Ibnu," + subline; "Download Report" primary. **4 KPI cards with icon circle left** (value Bold 24, label below, delta top-right green/red). Row 2: Task Progress grouped bar chart (3 series: On Progress blue, Complete green, Waiting for Payment orange; month stepper ‹ Apr ›) 2/3 + Active Projects list 1/3 (app-icon tile with red status dot, name, "2 Members | 24 Tasks", clock "8 Days"; "See All"). Row 3: Top Inquiries donut (center "Top Inquiry 110", legend with sublines "50 Project – 40%", "This Month ▾") + Latest Clients rows (avatar, name, project, status pill Wait Payment orange / Done green, outline "Chat" button).
- ✅ **Accounting** `0:7336` — title + subline + "Yearly ▾" select. Revenue Overview two-series bar chart with "Download" outline button (2/3) + **stacked stat cards** right (icon circle, `⋯`, value Bold 24, label, delta). **Subscription tiles row** (brand icon, name, date, price + "/yearly") ×4. **Gauge** "Project Done Target 80 from 120" semi-circle + encouraging copy. Latest Transaction list (avatar, name, project, amount green +/red −, date-time, attachment icon, `⋯`, "All Transaction ▾").
- ✅ **Projects** `0:10659` — **Kanban**: 4 columns (New Project, On Progress, Wait Payment, Done) each a white card with colored square + title + count; task cards with title, 2-line description, optional cover image, avatar stack (with colored initial avatars), clock duration; "Show More Project" link. Header: "Show: All Category ▾" + "Download Report".
- 📋 Reports `0:7832`, Expense `0:8323`, Contract `0:8867`, Calendar `0:9324`, Clients `0:9776`, Work Inquiry `0:10295`. Extra cards: Card `560:6`, card-bright-playful `561:20`, card-muted-editorial `561:29`.

## Online Learning — page `0:11750`
- ✅ **Dashboard** `0:18152` — "Hi, Justin Fagundez" + "Daily View Track ▾". Learning Overview area-line chart with **dark tooltip** (two metrics "125 task / 100 pts") and header stats (Task Completed 2,357 · Points Earned 22,500) 2/3 + Average Performance **two-tone ring** (orange points / blue tasks, icon in center, legend) 1/3. Row: Skill Developed **radar chart** (2 overlaid series + "See Details"), Study Time green bar chart by hour with Best/Worst Performance split footer, Exercise list with segmented filter (All · Module 1 · Module 2) and letter-avatar circles (L/R/S) + "Points 80/100". Row: Other Students horizontal **carousel** of course cards (avatar, course, mentor link, "24 Module total – 23 hr 34 min") with › arrow.
- ✅ **Course** `0:17534` — "Featured Course" + "Sort by: Recent ▾" + grid/list toggle. 4 **image course cards** (photo, title, orange progress bar, "Booked: 70%", "Days left: 3d"). My Course table with tabs (All Course · On Progress · Archived): mentor avatar + course + teacher, Module count, clock duration, status pill (On Progress orange / Archived grey / Finished green), outline "Details" button (2/3) + "You may like too…" list (thumb, title, 👤 2.3k, ★ 9,0, "Show More Course").
- 📋 Reports `0:11751`, Schedule alt 2 `0:12329`, Schedule alt `0:13032`, Schedule `0:13486`, Inbox `0:13890`, Tasks `0:14317`, Mentors `0:15007`, Student `0:15750`, Resources `0:16164`.

## Job Search — page `0:18652` 📋
Dashboard `0:25992`, Job Search `0:24935`, Job Details `0:24542`, Talent Details `0:23942`, Applicant Review `0:23058`, Message `0:22665`, Message – Video Call `0:22235`, Talent Scouting `0:21524`, Schedule `0:20010`, History `0:19298`, Events `0:18653`; Nav-bar `456:23`, Logo `456:6`. → Best reference for **ATS / recruitment** products.

## Crypto — page `0:26478` 📋
Dashboard `32:8153`, Dashboard – Get Started `32:6667`, – Get Started Minimize `32:7679`, – Send Invitation `32:8614`, Portfolio `32:6265`, Trade `32:5662`, Trade – BTC `32:5208`, BTC Wallet `32:4827`, BTC Receive `32:4493`, BTC Vault `32:4246`.

## SaaS Metrics — page `0:36057` 📋
Overview `33:25803`, Metrics – Revenue `33:24998`, MRR Movement `33:24444`, Active Customers (Compare Plans) `33:23702`, Forecast `33:23275`, Pricing insights `33:22914`, Benchmarks `33:22507`, Recover `33:22051`, Cancellations `33:21560`, Performance `33:21116`.

## Social Media Planner — page `0:31310` 📋
Dashboard `33:18924`, Analytics `33:18159`, Post Performance `33:17740`, Post Performance Details `33:16567`, Media Library `33:17324`, Media Library List `33:16894`, Schedule `33:16241`, Schedule post `33:15984`, Schedule post Calendar `33:15619`, Saved caption `33:15339`.

## Onboarding — page `173:7` 📋
5 variants × steps (Onboarding, #2, #3, #4), 1440×900.

## Auth — page `173:6` 📋
Sign in / Sign up #1–#4, filled states, Forgot password, New Password.

## Settings — page `173:8` 📋
Overview, Basic Information, Sign in method, Connected account, Notifications, Deactivate account, Billing, Referrals, Invite a Friend, 404.

## Styleguide — page `0:41443` 📋
01 Typography `0:41444`, 02 Color `0:41511`, 03 UI Elements `0:41608`.

## Cross-product patterns to reuse
- KPI card variants: plain (label → value → delta), **icon-circle left**, stacked stat card with `⋯`.
- Chart types used: grouped bars (2–3 series), area-line with dark tooltip, donut with center label, two-tone ring, semi-circle gauge, radar, horizontal bars.
- List rows: avatar/app-icon + 2-line text + meta right + action (pill / outline button / `⋯`).
- Kanban columns, course/image cards with progress bars, horizontal card carousels, segmented filters inside card headers.
