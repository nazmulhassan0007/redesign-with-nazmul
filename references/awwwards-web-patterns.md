# Awwwards-Level Website & Section Patterns

What makes a site feel award-worthy: a strong concept, confident typography, intentional motion, and craft in the details — still built on Refactoring UI fundamentals.

## Contents
1. Concept first
2. Typography
3. Layout & grid
4. Hero patterns
5. Section patterns
6. Motion
7. Color & texture
8. Anti-generic rules
9. Performance & accessibility

---

## 1. Concept first
Before building, define in one line: **audience + feeling + one signature idea**. E.g. "Study-abroad platform, optimistic and global, signature: a scroll-driven globe that pins and rotates to each destination." Every section should support that signature.

## 2. Typography
- Display type is the hero. Headlines 56–120px desktop (`clamp(2.75rem, 7vw, 7.5rem)`), line-height 0.95–1.05, letter-spacing −0.03 to −0.05em.
- Pairings: grotesk display + clean sans body (General Sans / Satoshi / Geist), editorial serif display + sans body (Instrument Serif / Fraunces + Inter), or a mono accent for labels (Geist Mono / JetBrains Mono).
- Section eyebrows name the topic in plain words (12px, +0.08em tracking), e.g. `Services`. No numbered eyebrows like `(01)` or `01 /`.
- Mix weights or italic serif words inside a sans headline for emphasis.
- Keep headlines to 2–4 lines; avoid single orphan words.

## 3. Layout & grid
- 12-column grid with generous outer margins (`px-6 md:px-10 xl:px-16`), max content ~1440px.
- Asymmetry: offset columns (text in cols 1–7, image in 8–12 shifted down), not everything centered.
- Section spacing large: 96–160px vertical on desktop, 64–96px mobile.
- Use rule lines (1px borders) only where they organize real content.
- Break the grid deliberately once per page (full-bleed image, oversized type overflowing).

## 4. Hero patterns (pick one, vary per project)
- **Giant type hero**: headline fills width, small supporting copy + CTA at bottom corners, subtle background media.
- **Split editorial**: left headline + copy + CTAs, right tall image/video with rounded corners or masked shape.
- **Full-bleed media**: video/image background, dark overlay gradient, headline bottom-left.
- **Minimal centered**: small headline, lots of whitespace, one product visual below with perspective/tilt.
- **Interactive**: cursor-reactive element, 3D object, or scroll-scrubbed sequence.
Always include: clear value proposition, one primary CTA + one secondary, trust signal (logos, rating, numbers) near the fold.

## 5. Section patterns
- **Logo marquee**: grayscale logos, infinite horizontal scroll, edges faded with mask gradient.
- **Features**: bento grid with mixed spans (1 large visual cell + smaller cells), not 3 identical icon cards.
- **Sticky storytelling**: left column sticky title, right column scrolling steps/images.
- **Horizontal scroll gallery**: pinned section scrolling cards sideways (GSAP ScrollTrigger).
- **Stats**: huge numbers (64–96px) with count-up, short muted labels, divided by rule lines.
- **Testimonials**: one large quote with portrait, or masonry of short quotes; avoid tiny carousels.
- **Pricing**: 3 tiers, middle highlighted (border-primary + badge), monthly/yearly toggle, feature lists with checks, compare table below.
- **FAQ**: two-column (title left, accordion right).
- **CTA band**: high-contrast block, big headline, single button.
- **Footer**: oversized brand wordmark, organized link columns, newsletter input, small legal row.

## 6. Motion
- Libraries: GSAP + ScrollTrigger, Lenis smooth scroll, or CSS-only for sections.
- Entrance: fade + translateY(24–40px), 0.6–0.9s, ease `power3.out` / `cubic-bezier(0.22,1,0.36,1)`, stagger 0.06–0.1s.
- Headline reveal: split lines/words, mask-up from overflow hidden.
- Scroll: parallax images (±10–15%), pinned sections, scale-on-scroll media.
- Micro: magnetic buttons, link underline draw, image zoom on hover (scale 1.04). Custom cursors off by default (see taste-anti-slop.md).
- Respect `prefers-reduced-motion`: disable transforms, keep opacity fades.

## 7. Color & texture
- Restrained palette: near-black/off-white base + one bold accent (lime, orange, electric blue, etc.).
- Dark themes: #0A0A0A–#111 bases, not pure black; light: #FAFAF9 warm off-white.
- Texture: subtle noise/grain overlay (opacity 0.03–0.06), soft radial glows, gradient meshes in brand hues.
- Imagery: consistent treatment (same crop ratio, grade, rounded radius).

## 8. Anti-generic rules
- No default purple-to-blue gradient hero.
- No three identical icon cards as the main features section.
- No centered everything; no stock-photo handshake.
- No lorem ipsum — write real, specific copy.
- Vary section rhythm: alternate dense/airy, light/dark, left/right.
- Give each project one memorable signature interaction.

## 9. Performance & accessibility
- Semantic HTML (header, nav, main, section, footer), one h1.
- Images with width/height, `loading="lazy"` below the fold.
- Contrast AA, visible focus states, keyboard-accessible menus.
- Animate only transform and opacity.
