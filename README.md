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
- **Claude Code**: clone the repo straight into your skills folder.
  ```bash
  git clone https://github.com/nazmulhassan0007/redesign-with-nazmul.git ~/.claude/skills/redesign-with-nazmul
  ```
  Use your project's `.claude/skills/` instead to install it for one project only. Run `git pull` in that folder to update.
- **Claude.ai**: click **Code → Download ZIP** on this page, then upload the zip in Settings → Capabilities → Skills.

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
├── CREDITS.md                sources and licenses
├── references/               design knowledge loaded on demand
├── assets/                   tokens.css, tokens-prism.css, licenses
└── tools/
    ├── ui-ux-pro-max/        local search engine (python3, no deps)
    └── hugeicons/            offline icon lookup (python3, no deps)
```

## Credits
See `CREDITS.md`. Bundled third-party material is MIT / Apache-2.0 licensed; their license files are in `assets/`, `tools/ui-ux-pro-max/LICENSE` and `tools/hugeicons/LICENSE.md`.
