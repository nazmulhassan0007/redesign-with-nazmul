# redesign with nazmul

A fast, opinionated UI redesign skill for Claude by **Md. Nazmul Hassan (naz)**. Give it a screenshot, code, Figma link, or description and say "redesign koro". It returns a production-ready redesign of websites (Awwwards-level), single sections, modern dashboards, and app screens.

## What's inside
- **Refactoring UI** principles as the design foundation
- **shadcn UI Kit** + official **shadcn/ui** rules for dashboards and components
- **Prism Dashboard UI Kit** theme (HR / ATS / payroll) with exact Figma tokens
- **Awwwards** section library and website patterns
- **Taste / anti-slop** dials, AI-tell blacklist and full redesign audit checklist
- **Impeccable** visitor modes, craft floor and refine commands (polish, bolder, quieter, distill, harden…)
- **Motion polish** (Emil Kowalski) and exact **product UI polish** values (ibelick, Jakub Krehel)
- **UI UX Pro Max** design-intelligence search engine (palettes, fonts, styles, UX rules)
- **Hugeicons Free** icon pack (6,000+ SVGs, offline lookup)
- 18 real-world **DESIGN.md** examples

## Install
- **Skills CLI** (Claude Code, Cursor and other agents):
  ```bash
  npx skills add nazmulhassan0007/redesign-with-nazmul
  ```
- **Claude Code** (manual):
  ```bash
  git clone https://github.com/nazmulhassan0007/redesign-with-nazmul.git ~/.claude/skills/redesign-with-nazmul
  ```
  (or clone into your project's `.claude/skills/` folder)
- **Claude.ai**: download `redesign-with-nazmul.skill` from Releases (or download this repo as ZIP) and upload it in Settings → Skills.

## Usage
```
eta redesign koro            (with a screenshot or code)
Redesign this ATS candidate list page
Build an Awwwards-level hero for a study-abroad platform
aro bold koro / polish koro / simple koro
Review this component's motion
```

## Structure
```
.
├── SKILL.md                  workflow, speed rules, pre-flight check
├── references/               design knowledge loaded on demand
├── assets/                   tokens.css, tokens-prism.css, licenses
└── tools/
    ├── ui-ux-pro-max/        design-intelligence search engine (python3)
    └── hugeicons/            offline icon lookup (python3)
```

## Credits
See `CREDITS.md`. Bundled third-party material is MIT / Apache-2.0 licensed; license files are in `assets/`, `tools/ui-ux-pro-max/LICENSE` and `tools/hugeicons/LICENSE.md`.
