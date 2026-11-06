#!/usr/bin/env python3
"""Writes nb Docs' launcher icon from nb-web's logo (graphics/nw-logo.svg, a copy of nb-web's).

    python3 graphics/nb-docs-icon.py            # writes the two vectors below
    python3 graphics/nb-docs-icon.py --preview out.svg   # the same layout as one SVG, to look at

app/src/main/res/drawable/ic_launcher_foreground.xml: the n (teal) and w (gold), each with its
dark outline, centred in the adaptive icon's safe zone. The coloured tile behind them is the
launcher colour (mipmap-anydpi-v26/ic_launcher_*.xml); the default is the logo's own grey.
ic_launcher_monochrome.xml: the same shapes in one colour, for themed icons (Android 13+).

The n draws its outline under its fill (paint-order: stroke fill); a vector drawable always draws
the stroke on top, so the n is drawn twice, outline first. Edit the logo, then run this again.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RES = HERE.parent / 'app' / 'src' / 'main' / 'res'
SVG = (HERE / 'nw-logo.svg').read_text()

LOGO = 112.34027                 # the logo's square (its viewBox)
VISIBLE = 72 / 108               # an adaptive icon shows the middle 72 of its 108 dp
FIT = 0.88                       # so the n's serifs stay inside the safe circle (66 dp)
VIEW = LOGO / (VISIBLE * FIT)    # viewport: the logo's square fills that much of the visible part
OFF = (VIEW - LOGO) / 2


def _attr(tag, name):
    m = re.search(rf'\b{name}="([^"]*)"', tag)
    return m.group(1) if m else None


def _style(tag, key):
    m = re.search(rf'{key}:([^;"]+)', _attr(tag, 'style') or '')
    return m.group(1).strip() if m else None


# the parts, by their labels in the SVG
n_tag = re.search(r'<path[^>]*inkscape:label="n"[^>]*>', SVG).group(0)
n_d, n_fill, n_stroke = _attr(n_tag, 'd'), _style(n_tag, 'fill'), _style(n_tag, 'stroke')
stroke_w = float(_style(n_tag, 'stroke-width'))
outer = re.search(r'<g transform="translate\(([-\d.]+),([-\d.]+)\)">', SVG)
tx, ty = float(outer.group(1)), float(outer.group(2))
w_tag = re.search(r'<g inkscape:label="w" transform="matrix\(([^)]*)\)">', SVG)
a, _, _, d, e, f = (float(v) for v in w_tag.group(1).split(','))
w_body = SVG[w_tag.end():]
outline = re.search(r'<g inkscape:label="outline" style="([^"]*)">(.*?)</g>', w_body, re.S)
fillg = re.search(r'<g inkscape:label="fill" style="([^"]*)">(.*?)</g>', w_body, re.S)
w_outline_d = re.findall(r' d="([^"]*)"', outline.group(2))
w_fill_d = re.findall(r' d="([^"]*)"', fillg.group(2))
w_dark = re.search(r'fill:(#[0-9a-fA-F]{6})', outline.group(1)).group(1)
w_gold = re.search(r'fill:(#[0-9a-fA-F]{6})', fillg.group(1)).group(1)


def _vector(paths_xml):
    return (f'<?xml version="1.0" encoding="utf-8"?>\n'
            f'<!-- Written by graphics/nb-docs-icon.py from graphics/nw-logo.svg: edit those, not this. -->\n'
            f'<vector xmlns:android="http://schemas.android.com/apk/res/android"\n'
            f'    android:width="108dp"\n    android:height="108dp"\n'
            f'    android:viewportWidth="{VIEW:.4f}"\n    android:viewportHeight="{VIEW:.4f}">\n'
            f'  <group android:translateX="{OFF:.4f}" android:translateY="{OFF:.4f}">\n'
            f'    <group android:translateX="{tx}" android:translateY="{ty}">\n'
            f'{paths_xml}'
            f'    </group>\n  </group>\n</vector>\n')


def _path(d, fill=None, stroke=None, width=None, evenodd=False, ind='      '):
    out = f'{ind}<path android:pathData="{d}"'
    if fill:
        out += f'\n{ind}    android:fillColor="{fill}"'
    if evenodd:
        out += f'\n{ind}    android:fillType="evenOdd"'
    if stroke:
        out += (f'\n{ind}    android:strokeColor="{stroke}"\n{ind}    android:strokeWidth="{width}"'
                f'\n{ind}    android:strokeLineJoin="round"')
    return out + ' />\n'


def foreground(mono=None):
    dark, teal, gold = (mono, mono, mono) if mono else (n_stroke, n_fill, w_gold)
    xml = _path(n_d, stroke=dark, width=stroke_w)                      # the n's outline, first
    xml += _path(n_d, fill=teal, evenodd=True)                          # then its fill
    xml += (f'      <group android:scaleX="{a}" android:scaleY="{d}"'
            f' android:translateX="{e}" android:translateY="{f}">\n')
    for p in w_outline_d:
        xml += _path(p, fill=mono or w_dark, stroke=mono or w_dark, width=stroke_w, ind='        ')
    for p in w_fill_d:
        xml += _path(p, fill=gold, ind='        ')
    return _vector(xml + '      </group>\n')


def preview(out):
    body = re.sub(r'<rect[^>]*/>', '', SVG.split('<g id="nw">', 1)[1].rsplit('</svg>', 1)[0])
    Path(out).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"'
        f' viewBox="0 0 {VIEW} {VIEW}" width="432" height="432">'
        f'<rect width="{VIEW}" height="{VIEW}" fill="#c8cbd0"/>'
        f'<circle cx="{VIEW/2}" cy="{VIEW/2}" r="{VIEW*33/108}" fill="none" stroke="#d00" stroke-width="0.4"/>'
        f'<g transform="translate({OFF},{OFF})"><g id="nw">{body}</svg>')


if __name__ == '__main__':
    if sys.argv[1:2] == ['--preview']:
        preview(sys.argv[2])
    else:
        (RES / 'drawable' / 'ic_launcher_foreground.xml').write_text(foreground())
        (RES / 'drawable' / 'ic_launcher_monochrome.xml').write_text(foreground(mono='#ffffff'))
        print('wrote ic_launcher_foreground.xml, ic_launcher_monochrome.xml')
