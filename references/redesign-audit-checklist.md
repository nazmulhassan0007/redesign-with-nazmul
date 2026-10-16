# Redesign Audit Checklist (redesign-existing-projects)

Distilled from the "redesign-existing-projects" skill in github.com/leonxlnx/taste-skill (MIT). Use in step 2 (quick audit): scan every category, then report only the top 3–5 problems. Fix order is in `taste-anti-slop.md` §2.

## Scan
1. Detect the stack (framework, styling, icon library) and the current design language before changing anything.
2. Work inside the existing stack; no migrations; never break functionality; keep all content.

## Audit categories
- **Typography**: generic default font, weak hierarchy (all same weight), headlines without tight tracking, body lines too long, no tabular numbers in data, orphan words.
- **Color & surfaces**: purple/blue AI gradient, pure black, more than one accent, mixed warm/cool greys, untinted black shadows, flat sections with no depth.
- **Layout**: everything centered, three equal cards, uniform spacing between and within groups, `h-screen` heroes, no max-width, misaligned card CTAs.
- **Interactivity & states**: missing hover/active/focus, no loading (skeleton), empty or error states, no transitions, instant layout jumps.
- **Content**: lorem ipsum, generic names (John Doe, Acme), fake-perfect numbers, filler verbs (Elevate, Seamless, Unleash), exclamation marks, "Oops".
- **Component patterns**: default unstyled library components, modals for everything, 3-dot testimonial carousels, 4-column footer link farms.
- **Iconography**: default icon set everywhere (use Hugeicons or the project's own set), cliché metaphors (rocket = launch, shield = security → bolt, fingerprint, spark, vault), mixed stroke widths, missing favicon, uncanny stock "team" photos.
- **Code quality**: div soup (use nav/main/section/article/aside), inline styles mixed with classes, hardcoded pixel widths, missing or useless alt text, `z-index: 9999`, dead commented code, imports not in package.json, missing meta tags.
- **Strategic omissions**: no privacy/terms links, dead-end flows without back navigation, no custom 404, no form validation, no skip-to-content link, no cookie consent where required.

## Upgrade techniques (pick per dials; websites only unless noted)
- **Typography**: variable-font weight/width shift on scroll or hover; outline-to-fill text on entry; text as a mask over video.
- **Layout**: deliberate broken grid / overlap; aggressive whitespace around one focal element; sticky stacking card sections; split-screen opposite-direction scroll.
- **Motion**: inertia smooth scroll (Lenis); staggered entrances (y + opacity); spring physics on interactive elements; scroll-driven mask/wipe/SVG-draw reveals.
- **Surfaces**: real glass (blur + 1px inner border + subtle inner shadow); cursor spotlight borders; fixed pointer-events-none grain overlay; shadows tinted with the background hue (also fine in dashboards).
