# Awwwards Section Idea Library

Organized like Awwwards "Collections" (curated by element type). Pick 1 idea per section; never stack more than one signature effect per viewport. Each entry: idea → how to build → when to use.

## Contents
Preloaders · Navigation & menus · Heroes · Text & type animation · Scroll storytelling · Galleries & showcases · Features · Cards & hover · Testimonials & social proof · Pricing · CTA · Footers · Cursors · Page transitions · 404 / micro pages · Forms

## Preloaders
- **Counter 0→100** in huge digits, then the panel slides up revealing the hero (GSAP timeline, ≤ 1.5s).
- **Logo stroke draw** (SVG `stroke-dashoffset`) then scale-out.
- **Image stack shuffle**: 4–6 project images flash in a small frame, last one scales to full-bleed hero.
Use only on portfolio/brand sites; skip for SaaS and dashboards.

## Navigation & menus
- **Minimal bar**: logo left, 3–4 links center/right, pill CTA; becomes blurred translucent (`backdrop-blur bg-background/70`) after scroll; hides on scroll-down, shows on scroll-up.
- **Fullscreen overlay menu**: huge stacked links (64–120px), hover swaps a preview image on the side, staggered line reveal on open, menu button morphs ☰→✕.
- **Floating dock/pill nav** centered at the bottom or top.
- **Mega menu** with image cards for product-rich sites.
- Active-section indicator (underline slides between links).

## Heroes
- **Oversized wordmark**: brand name spans 100vw, bottom-aligned, small intro text top-left.
- **Split headline + media**: words of the headline interleaved with small inline images/videos ("We build [img] digital [video] products").
- **Video mask**: headline text acts as a mask for a video (`background-clip: text`).
- **Scroll-scale media**: small centered video grows to full screen as you scroll (pinned).
- **3D / WebGL object** reacting to cursor (Three.js / Spline) — only if it means something.
- **Marquee headline**: infinite horizontal running text behind the content.
- **Grid of tiles** that assemble into the hero on load.

## Text & type animation
- Line-by-line mask reveal (SplitText, `overflow:hidden` lines, y 100%→0).
- Scroll-scrubbed word highlight: paragraph from 20% opacity to 100% word by word.
- Variable-font weight change on hover/scroll.
- Scramble/decode text effect for tech brands.
- Kinetic marquee that speeds up/reverses with scroll velocity.

## Scroll storytelling
- **Sticky split**: left title pinned, right steps scroll; images crossfade in a pinned frame.
- **Horizontal pinned scroll** for process/case studies.
- **Stacking cards**: cards pin and stack on top of each other with slight scale-down.
- **Zoom-through**: scroll zooms into an image to reveal the next section.
- **Progress line** drawing along a timeline/roadmap.
- **Number counters** triggered in view.

## Galleries & showcases
- Work index as **list with hover image follow** (image follows cursor over rows).
- **Asymmetric masonry** with parallax at different speeds per column.
- **Infinite draggable canvas** of projects.
- **Fullscreen slider** with clip-path transitions and a minimal prev/next control.
- Before/after comparison slider.

## Features
- **Bento grid** (mixed spans) with one live/animated cell (mini UI, chart, video).
- **Tabbed feature**: tabs on the left, product UI swaps on the right with progress bar per tab (auto-advance).
- **Feature + live UI mock** built in HTML instead of screenshots.
- Icon lists replaced with editorial rows: bold topic word + one-line description, separated by a single hairline.

## Cards & hover
- Image zoom 1.04 + overlay reveal of meta.
- Tilt / 3D perspective on hover (subtle, ≤ 6°).
- Border gradient spotlight following the cursor.
- Card expands into a detail view (shared-element / FLIP transition).

## Testimonials & social proof
- One big quote (36–48px) with portrait and name, arrows to switch.
- Two-row opposite-direction marquee of short quotes.
- Logo wall: grayscale → color on hover; or infinite slider with edge fade mask.
- Big stats band: 3–4 numbers 64–96px with rule lines.

## Pricing
- 3 tiers, middle highlighted (dark card in a light page or vice versa), monthly/yearly toggle with "save 20%" badge, animated price number change.
- Comparison table below with sticky header.

## CTA
- Full-width dark band, giant headline, magnetic round button.
- CTA with background video/gradient mesh and noise.
- Email capture inline in the headline sentence.

## Footers
- **Giant brand wordmark** across the full width at the bottom.
- Big "Let's talk" link/email as the main element, with link columns small.
- Reveal footer: content scrolls up to uncover a fixed footer underneath.
- Local time + location + socials + back-to-top.

## Cursors
- Off by default. Only for explicit agency/Awwwards briefs: small dot + lagging ring that grows with a label ("View", "Drag") over media; hide on touch and reduced-motion.

## Page transitions
- Panel wipe (color block slides across), clip-path circle reveal, or fade+translate of content. Keep ≤ 700ms. (Barba.js / View Transitions API.)

## 404 / micro pages
- Playful interactive 404 (draggable letters, physics), with a clear way home.

## Forms
- Large conversational form ("Hi, my name is ____ and I need help with ____").
- Selectable pill chips for services/budget instead of dropdowns.

## Guardrails
- Every effect respects `prefers-reduced-motion`.
- Content first: effects must not hide the value proposition or CTA.
- Mobile: replace pinned/horizontal scroll with vertical stacking; disable custom cursor.
