# redesign with nazmul

A fast, opinionated UI redesign skill for Claude by **Md. Nazmul Hassan (naz)**. Give it a screenshot, code, Figma link, or description and say "redesign koro". It returns a production-ready redesign of websites (Awwwards-level), single sections, modern dashboards, and app screens.

## What's inside
- **Refactoring UI** principles as the design foundation
- **shadcn UI Kit** + official **shadcn/ui** rules for dashboards and components
- **Prism Dashboard UI Kit** theme (HR / ATS / payroll) with exact Figma tokens
- **Awwwards** section library and website patterns
- **Taste / anti-slop** dials and AI-tell blacklist
- **Motion polish** (Emil Kowalski) and exact **product UI polish** values (ibelick, Jakub Krehel)
- **UI UX Pro Max** design-intelligence search engine (palettes, fonts, styles, UX rules)
- **Hugeicons Free** icon pack (6,000+ SVGs, offline lookup)
- 18 real-world **DESIGN.md** examples

## Install
- **Claude.ai**: download `redesign-with-nazmul.skill` from Releases (or zip the `redesign-with-nazmul/` folder) and upload it in Settings → Skills.
- **Claude Code**: copy `redesign-with-nazmul/` into `~/.claude/skills/` (or your project's `.claude/skills/`).

## Usage
```
eta redesign koro            (with a screenshot or code)
Redesign this ATS candidate list page
Build an Awwwards-level hero for a study-abroad platform
Review this component's motion
```

## Structure
```
redesign-with-nazmul/
├── SKILL.md                  workflow, speed rules, pre-flight check
├── references/               design knowledge loaded on demand
├── assets/                   tokens.css, tokens-prism.css, licenses
└── tools/ui-ux-pro-max/      local search engine (python3, no deps)
```

## Credits
See `redesign-with-nazmul/CREDITS.md`. Bundled third-party material is MIT / Apache-2.0 licensed; their license files are in `redesign-with-nazmul/assets/` and `tools/ui-ux-pro-max/LICENSE`.
