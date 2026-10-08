#!/usr/bin/env python3
"""Hugeicons Free (stroke-rounded, MIT) — offline SVG lookup for redesign-with-nazmul.

Usage:
  python3 icon.py search <words...>            # find icon names, e.g. search user add
  python3 icon.py svg <name> [--size 20] [--stroke 1.5] [--class cls]
  python3 icon.py svg <name1> <name2> ...      # several at once
  python3 icon.py sprite <name...> > sprite.svg # <symbol> sprite, use <svg><use href="#hi-name"/></svg>
Icons use currentColor, so color comes from CSS.
"""
import gzip, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
with gzip.open(os.path.join(HERE, "icons.json.gz"), "rt") as f:
    DB = json.load(f)

def els(name):
    v = DB.get(name)
    if isinstance(v, str) and v.startswith("@"):
        v = DB[v[1:]]
    return v

def inner(name, stroke):
    parts = []
    for tag, attrs in els(name):
        a = dict(attrs)
        if stroke and "stroke-width" in a:
            a["stroke-width"] = str(stroke)
        parts.append("<%s %s/>" % (tag, " ".join('%s="%s"' % (k, v) for k, v in a.items())))
    return "".join(parts)

def svg(name, size=20, stroke=None, cls=None):
    c = ' class="%s"' % cls if cls else ""
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s" viewBox="0 0 24 24" fill="none" aria-hidden="true"%s>%s</svg>'
            % (size, size, c, inner(name, stroke)))

def search(words):
    words = [w.lower() for w in words]
    hits = [n for n in DB if all(w in n for w in words)]
    return sorted(hits, key=len)[:40]

def main(argv):
    if len(argv) < 2 or argv[1] not in ("search", "svg", "sprite"):
        print(__doc__); return 1
    cmd, rest = argv[1], argv[2:]
    opts = {"--size": "20", "--stroke": None, "--class": None}
    names = []
    i = 0
    while i < len(rest):
        if rest[i] in opts: opts[rest[i]] = rest[i + 1]; i += 2
        else: names.append(rest[i]); i += 1
    if cmd == "search":
        res = search(names); print("\n".join(res) if res else "no match - try fewer/shorter words"); return 0
    missing = [n for n in names if n not in DB]
    for n in missing:
        print("<!-- not found: %s ; try: %s -->" % (n, ", ".join(search(n.split("-"))[:5])), file=sys.stderr)
    names = [n for n in names if n in DB]
    if cmd == "svg":
        for n in names:
            print("<!-- %s -->\n%s" % (n, svg(n, opts["--size"], opts["--stroke"], opts["--class"])))
    else:
        print('<svg xmlns="http://www.w3.org/2000/svg" style="display:none">')
        for n in names:
            print('<symbol id="hi-%s" viewBox="0 0 24 24" fill="none">%s</symbol>' % (n, inner(n, opts["--stroke"])))
        print("</svg>")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
