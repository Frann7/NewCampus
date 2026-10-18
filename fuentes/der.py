"""Dibuja diagramas entidad-relación (DER) en SVG y los mete en los fragmentos.

Uso (desde la raíz del repo):
    python fuentes/der.py fuentes/bd/diagramas/der.py [app/contenido/bd]

El primer argumento es un archivo de diagramas: Python que arma un diccionario
`D` con un diagrama por nombre. El segundo, la carpeta de fragmentos (por
defecto, `app/contenido/bd`). En cada fragmento, el contenido de
`<div class="pd-grafico der" data-g="nombre">...</div>` se reemplaza por el SVG
de `D["nombre"]`. Los estilos (`.der ...`) están en `app/assets/estilos.css`.

La notación es la de la cátedra: entidades en rectángulos, interrelaciones en
rombos, la cardinalidad (mín, máx) junto a cada entidad, y los atributos como
"chupetines": círculo lleno el identificador, círculo vacío el resto.

Un diagrama:
    D["zoo"] = dict(
        ent=[dict(id="Zona", x=300, y=200, attrs=["*Codigo", "Nombre"], lado="der")],
        rel=[dict(id="R3", x=450, y=200, une=[("Zona", "(1,n)"), ("Especie", "(1,1)")],
                  attrs=["FechaDesde"], lado="arriba")],
        gen=[dict(padre="Empleado", hijos=["Guia", "Cuidador"], rotulo="(p,s)")],
    )

Entidad: `id` (y `nombre` si se lee distinto), `x`, `y` (el centro), `attrs`
(un `*` adelante marca el identificador), `lado` de los atributos (der, izq,
arriba, abajo) y `w` (ancho mínimo).
Interrelación: `id`, `x`, `y`, `nombre` (por defecto el id), `une` = lista de
(entidad, cardinalidad) o (entidad, cardinalidad, [puntos intermedios]) para
una línea con codos, `attrs` y `lado` como en la entidad.
La cardinalidad va sola junto a la entidad; con un cuarto elemento (dx, dy)
se corre de lugar.
"""
import math
import os
import re
import sys

ALTO_E = 36          # alto de una entidad
MEDIO_R = (46, 21)   # medio ancho y medio alto de un rombo
PASO_A = 15          # distancia entre atributos


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def ancho_texto(s, px=12.5):
    return sum(px * (0.33 if c in "ilI.,;:()'|" else 0.62 if c.isupper() else 0.55) for c in s)


class Lienzo:
    def __init__(self):
        self.partes = []
        self.caja = [math.inf, math.inf, -math.inf, -math.inf]

    def ver(self, x, y):
        c = self.caja
        c[0], c[1], c[2], c[3] = min(c[0], x), min(c[1], y), max(c[2], x), max(c[3], y)

    def texto(self, x, y, s, clase, ancla="middle"):
        w = ancho_texto(s)
        x0 = x - w / 2 if ancla == "middle" else x - w if ancla == "end" else x
        self.ver(x0, y - 8)
        self.ver(x0 + w, y + 8)
        self.partes.append(f'<text class="{clase}" x="{x:.1f}" y="{y:.1f}" text-anchor="{ancla}" '
                           f'dominant-baseline="central">{esc(s)}</text>')

    def linea(self, puntos, clase="lin"):
        for x, y in puntos:
            self.ver(x, y)
        d = " L".join(f"{x:.1f},{y:.1f}" for x, y in puntos)
        self.partes.append(f'<path class="{clase}" d="M{d}"/>')


def borde_rect(cx, cy, mw, mh, hacia):
    dx, dy = hacia[0] - cx, hacia[1] - cy
    if dx == dy == 0:
        return cx, cy
    t = min(mw / abs(dx) if dx else math.inf, mh / abs(dy) if dy else math.inf)
    return cx + dx * t, cy + dy * t


def borde_rombo(cx, cy, mw, mh, hacia):
    dx, dy = hacia[0] - cx, hacia[1] - cy
    if dx == dy == 0:
        return cx, cy
    t = 1 / (abs(dx) / mw + abs(dy) / mh)
    return cx + dx * t, cy + dy * t


def atributos(L, cx, cy, mw, mh, attrs, lado):
    """Chupetines: una línea del borde a cada círculo, y el nombre al lado."""
    n = len(attrs)
    for k, a in enumerate(attrs):
        clave = a.startswith("*")
        nombre = a.lstrip("*")
        if lado in ("der", "izq"):
            s = 1 if lado == "der" else -1
            yi = cy + (k - (n - 1) / 2) * PASO_A
            x0 = cx + s * mw
            xc = x0 + s * 30
            L.linea([(x0, cy + (yi - cy) * 0.25), (xc - s * 4, yi)])
            tx, ty, ancla = xc + s * 8, yi, "start" if s > 0 else "end"
        else:
            s = -1 if lado == "arriba" else 1
            xi = cx + mw * 0.75
            yi = cy + s * (mh + 16 + (n - 1 - k if s < 0 else k) * PASO_A)
            L.linea([(cx + mw * 0.55, cy + s * mh), (xi - 4, yi)])
            xc = xi
            tx, ty, ancla = xi + 8, yi, "start"
        L.partes.append(f'<circle class="{"id" if clave else "noid"}" cx="{xc:.1f}" cy="{yi:.1f}" r="3.6"/>')
        L.ver(xc - 4, yi - 4)
        L.texto(tx, ty, nombre, "att" + (" pk" if clave else ""), ancla)


def svg(d):
    L = Lienzo()
    ents = {}
    for e in d.get("ent", []):
        nombre = e.get("nombre", e["id"])
        mw = max(e.get("w", 0), ancho_texto(nombre, 14) + 28) / 2
        ents[e["id"]] = (e["x"], e["y"], mw, ALTO_E / 2)

    for g in d.get("gen", []):
        px, py, pw, ph = ents[g["padre"]]
        hijos = [ents[h] for h in g["hijos"]]
        ymed = (py + ph + min(h[1] - h[3] for h in hijos)) / 2
        L.linea([(px, py + ph), (px, ymed)])
        L.linea([(min(h[0] for h in hijos), ymed), (max(h[0] for h in hijos), ymed)])
        for hx, hy, hw, hh in hijos:
            L.linea([(hx, ymed), (hx, hy - hh)])
        if g.get("rotulo"):
            L.texto(px + 8, (py + ph + ymed) / 2, g["rotulo"], "card", "start")

    for r in d.get("rel", []):
        rx, ry = r["x"], r["y"]
        mw, mh = MEDIO_R
        mw = max(mw, ancho_texto(r.get("nombre", r["id"])) / 2 + 22)
        for u in r["une"]:
            eid, card = u[0], u[1]
            via = list(u[2]) if len(u) > 2 and u[2] else []
            ex, ey, ew, eh = ents[eid]
            primero = via[0] if via else (ex, ey)
            ultimo = via[-1] if via else (rx, ry)
            a = borde_rombo(rx, ry, mw, mh, primero)
            b = borde_rect(ex, ey, ew, eh, ultimo)
            L.linea([a] + via + [b])
            if card:
                ux, uy = ultimo[0] - b[0], ultimo[1] - b[1]
                largo = math.hypot(ux, uy) or 1
                ux, uy = ux / largo, uy / largo
                nx, ny = -uy, ux
                if ny > 0 or (ny == 0 and nx < 0):
                    nx, ny = -nx, -ny
                cx, cy = b[0] + ux * 20 + nx * 11, b[1] + uy * 20 + ny * 11
                if len(u) > 3:
                    cx, cy = cx + u[3][0], cy + u[3][1]
                L.texto(cx, cy, card, "card")
        pts = [(rx, ry - mh), (rx + mw, ry), (rx, ry + mh), (rx - mw, ry)]
        for p in pts:
            L.ver(*p)
        L.partes.append('<polygon class="rel" points="%s"/>' % " ".join(f"{x:.1f},{y:.1f}" for x, y in pts))
        L.texto(rx, ry, r.get("nombre", r["id"]), "nrel")
        if r.get("attrs"):
            atributos(L, rx, ry, mw * 0.55, mh * 0.55, r["attrs"], r.get("lado", "abajo"))

    for e in d.get("ent", []):
        x, y, mw, mh = ents[e["id"]]
        L.ver(x - mw, y - mh)
        L.ver(x + mw, y + mh)
        L.partes.append(f'<rect class="ent" x="{x - mw:.1f}" y="{y - mh:.1f}" width="{2 * mw:.1f}" '
                        f'height="{2 * mh:.1f}"/>')
        L.texto(x, y, e.get("nombre", e["id"]), "nent")
        if e.get("attrs"):
            atributos(L, x, y, mw, mh, e["attrs"], e.get("lado", "der"))

    x0, y0, x1, y1 = L.caja
    m = 8
    vb = f"{x0 - m:.0f} {y0 - m:.0f} {x1 - x0 + 2 * m:.0f} {y1 - y0 + 2 * m:.0f}"
    rot = d.get("titulo", "Diagrama entidad-relación")
    cuerpo = "\n".join("  " + p for p in L.partes)
    # Se puede achicar hasta el 80 % (la letra sigue legible); más angosto, se desplaza.
    ancho = x1 - x0 + 2 * m
    return (f'<svg viewBox="{vb}" width="{ancho:.0f}" height="{y1 - y0 + 2 * m:.0f}" '
            f'style="min-width:{ancho * 0.8:.0f}px" role="img" aria-label="{esc(rot)}">\n{cuerpo}\n</svg>')


def main():
    espacio = {"D": {}}
    with open(sys.argv[1], encoding="utf-8") as f:
        exec(compile(f.read(), sys.argv[1], "exec"), espacio)
    D = espacio["D"]
    raiz = sys.argv[2] if len(sys.argv) > 2 else "app/contenido/bd"
    usados = set()
    patron = re.compile(r'(<div class="pd-grafico der" data-g="([^"]+)">)(.*?)(\n?[ \t]*</div>)', re.S)
    for carpeta, _, archivos in os.walk(raiz):
        for archivo in sorted(archivos):
            if not archivo.endswith(".html"):
                continue
            ruta = os.path.join(carpeta, archivo)
            with open(ruta, encoding="utf-8") as fh:
                viejo = fh.read()

            def cambiar(m):
                if m.group(2) not in D:
                    return m.group(0)
                usados.add(m.group(2))
                sangria = re.search(r"[ \t]*$", viejo[:m.start()]).group(0) + "  "
                dibujo = "\n".join(sangria + l for l in svg(D[m.group(2)]).splitlines())
                return f"{m.group(1)}\n{dibujo}\n{sangria[:-2]}</div>"

            nuevo = patron.sub(cambiar, viejo)
            if nuevo != viejo:
                with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(nuevo)
                print("ok:", os.path.relpath(ruta, raiz))
    for nombre in sorted(set(D) - usados):
        print("SIN USAR:", nombre)


if __name__ == "__main__":
    main()
