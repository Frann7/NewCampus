"""Dibuja diagramas de clases UML en SVG y los mete en los fragmentos.

Uso (desde la raíz del repo):
    python fuentes/uml.py fuentes/ing2/diagramas/base.py [app/contenido/ing2]

El primer argumento es un archivo de diagramas: Python que arma un diccionario
`D` con un diagrama por nombre. El segundo, la carpeta de fragmentos donde
buscar (por defecto, `app/contenido/ing2`). En cada fragmento, el contenido de
`<div class="pd-grafico uml" data-g="nombre">...</div>` se reemplaza por el SVG
de `D["nombre"]`. Los estilos (`.uml ...`) están en `app/assets/estilos.css`.

Un diagrama:
    D["animales"] = dict(
        clases=[
            dict(id="Animal", x=120, y=0, estereo="abstract", abstracta=True,
                 attrs=["# nombre: string"], mets=["a:+ hablar(): void"]),
            dict(id="Perro", x=0, y=150, mets=["+ hablar(): void"]),
        ],
        rel=[("Perro", "Animal", "herencia")],
    )

Clase: `id`, `x`, `y` (esquina de arriba a la izquierda, en px), y opcionales
`nombre` (si no es el id), `estereo` (interface, abstract...), `abstracta`
(nombre en cursiva), `destacada` (color), `attrs`, `mets`, `w` (ancho mínimo).
Un miembro que empieza con `s:` es estático (subrayado); con `a:`, abstracto
(cursiva).

Relación: (de, a, tipo[, opciones]). Tipos: herencia, realiza, asociacion
(flecha abierta hacia `a`), enlace (sin punta), dependencia, agregacion y
composicion (el rombo va en `de`, que es el todo). Opciones: `rot` (texto al
medio), `m1` y `m2` (multiplicidad en cada punta), `sal` y `lle` (lado por el
que sale y llega: arriba, abajo, izq, der), `d1` y `d2` (correr la punta a lo
largo del lado), `medio` (dónde dobla, de 0 a 1).
"""
import os
import re
import sys

ALTO_LINEA = 19
ANCHO_CHAR = 7.6      # miembros, monoespaciado de 12.5px
ANCHO_NOMBRE = 8.6    # nombre de la clase, negrita de 14px
MARGEN = 14


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def medir(c):
    nombre = c.get("nombre", c["id"])
    attrs, mets = c.get("attrs", []), c.get("mets", [])
    limpio = [re.sub(r"^[sa]:", "", m) for m in attrs + mets]
    ancho = max([len(nombre) * ANCHO_NOMBRE]
                + [len(m) * ANCHO_CHAR for m in limpio]
                + [(len(c["estereo"]) + 2) * 7 if c.get("estereo") else 0]) + 24
    c["w"] = max(round(ancho), c.get("w", 0), 90)
    cab = 30 + (16 if c.get("estereo") else 0)
    c["cab"] = cab
    c["h"] = cab + sum(len(g) * ALTO_LINEA + 10 for g in (attrs, mets) if g)


def dibujar_clase(c):
    x, y, w, h = c["x"], c["y"], c["w"], c["h"]
    o = [f'<rect class="caja{" destacada" if c.get("destacada") else ""}" x="{x}" y="{y}" width="{w}" height="{h}" rx="3"/>']
    ty = y + 20
    if c.get("estereo"):
        o.append(f'<text class="estereo" x="{x + w / 2:g}" y="{y + 16}">&#171;{esc(c["estereo"])}&#187;</text>')
        ty = y + 35
    cls = "nombre abstracta" if c.get("abstracta") else "nombre"
    o.append(f'<text class="{cls}" x="{x + w / 2:g}" y="{ty}">{esc(c.get("nombre", c["id"]))}</text>')
    cy = y + c["cab"]
    for grupo in (c.get("attrs", []), c.get("mets", [])):
        if not grupo:
            continue
        o.append(f'<line class="div" x1="{x}" y1="{cy}" x2="{x + w}" y2="{cy}"/>')
        for i, m in enumerate(grupo):
            extra = {"s:": " estatico", "a:": " abstracto"}.get(m[:2], "")
            if extra:
                m = m[2:]
            o.append(f'<text class="miembro{extra}" x="{x + 10}" y="{cy + 18 + i * ALTO_LINEA}">{esc(m)}</text>')
        cy += len(grupo) * ALTO_LINEA + 10
    return o


def ancla(c, lado, corr):
    x, y, w, h = c["x"], c["y"], c["w"], c["h"]
    return {"arriba": (x + w / 2 + corr, y), "abajo": (x + w / 2 + corr, y + h),
            "izq": (x, y + h / 2 + corr), "der": (x + w, y + h / 2 + corr)}[lado]


DIR = {"arriba": (0, -1), "abajo": (0, 1), "izq": (-1, 0), "der": (1, 0)}


def lados(a, b):
    """Por qué lado sale de `a` y por cuál llega a `b`."""
    if b["y"] + b["h"] <= a["y"]:
        return "arriba", "abajo"
    if a["y"] + a["h"] <= b["y"]:
        return "abajo", "arriba"
    if b["x"] >= a["x"] + a["w"]:
        return "der", "izq"
    return "izq", "der"


def punta(tipo, p, d):
    """La figura en la punta `p`; `d` apunta hacia afuera de la línea.
    Devuelve (svg, cuánto se acorta la línea)."""
    (x, y), (dx, dy) = p, d
    nx, ny = -dy, dx
    if tipo in ("herencia", "realiza"):
        bx, by = x - dx * 13, y - dy * 13
        pts = f"{x:g},{y:g} {bx + nx * 7:g},{by + ny * 7:g} {bx - nx * 7:g},{by - ny * 7:g}"
        return f'<polygon class="hueca" points="{pts}"/>', 13
    if tipo in ("asociacion", "dependencia"):
        bx, by = x - dx * 10, y - dy * 10
        return (f'<polyline class="linea" points="{bx + nx * 5:g},{by + ny * 5:g} {x:g},{y:g} '
                f'{bx - nx * 5:g},{by - ny * 5:g}"/>'), 0
    if tipo in ("agregacion", "composicion"):
        mx, my, fx, fy = x - dx * 9, y - dy * 9, x - dx * 18, y - dy * 18
        pts = f"{x:g},{y:g} {mx + nx * 6:g},{my + ny * 6:g} {fx:g},{fy:g} {mx - nx * 6:g},{my - ny * 6:g}"
        return f'<polygon class="{"hueca" if tipo == "agregacion" else "llena"}" points="{pts}"/>', 18
    return "", 0


def dibujar_rel(clases, r):
    de, a, tipo = clases[r[0]], clases[r[1]], r[2]
    op = r[3] if len(r) > 3 else {}
    sal, lle = lados(de, a)
    sal, lle = op.get("sal", sal), op.get("lle", lle)
    p1, p2 = ancla(de, sal, op.get("d1", 0)), ancla(a, lle, op.get("d2", 0))
    d1, d2 = DIR[sal], DIR[lle]
    if d1[1] == 0 and d2[1] == 0 and "d1" not in op and "d2" not in op:
        # dos cajas lado a lado: si se superponen en altura, la línea va derecha
        arriba, abajo = max(de["y"], a["y"]), min(de["y"] + de["h"], a["y"] + a["h"])
        if abajo - arriba > 16:
            p1, p2 = (p1[0], (arriba + abajo) / 2), (p2[0], (arriba + abajo) / 2)
    o = []
    # el rombo va en el origen (el todo); el resto de las puntas, en el destino
    fig1, corte1 = punta(tipo, p1, (-d1[0], -d1[1])) if tipo in ("agregacion", "composicion") else ("", 0)
    fig2, corte2 = punta(tipo, p2, (-d2[0], -d2[1])) if tipo not in ("agregacion", "composicion", "enlace") else ("", 0)
    q1 = (p1[0] + d1[0] * corte1, p1[1] + d1[1] * corte1)
    q2 = (p2[0] + d2[0] * corte2, p2[1] + d2[1] * corte2)
    medio = op.get("medio", 0.5)
    if d1[0] == 0 and d2[0] == 0:        # vertical - horizontal - vertical
        my = q1[1] + (q2[1] - q1[1]) * medio
        pts = [q1, (q1[0], my), (q2[0], my), q2]
    elif d1[1] == 0 and d2[1] == 0:      # horizontal - vertical - horizontal
        mx = q1[0] + (q2[0] - q1[0]) * medio
        pts = [q1, (mx, q1[1]), (mx, q2[1]), q2]
    elif d1[0] == 0:                     # sale vertical, llega horizontal
        pts = [q1, (q1[0], q2[1]), q2]
    else:
        pts = [q1, (q2[0], q1[1]), q2]
    cls = "linea punteada" if tipo in ("realiza", "dependencia") else "linea"
    o.append(f'<polyline class="{cls}" points="{" ".join(f"{x:g},{y:g}" for x, y in pts)}"/>')
    o += [f for f in (fig1, fig2) if f]
    if op.get("rot"):
        i = len(pts) // 2 - 1
        (ax, ay), (bx, by) = pts[i], pts[i + 1]
        horizontal = ay == by
        o.append(f'<text class="rotulo" x="{(ax + bx) / 2 + (0 if horizontal else 6):g}" '
                 f'y="{(ay + by) / 2 - (6 if horizontal else 0):g}" '
                 f'text-anchor="{"middle" if horizontal else "start"}">{esc(op["rot"])}</text>')
    for clave, p, d in (("m1", p1, d1), ("m2", p2, d2)):
        if op.get(clave):
            x = p[0] + d[0] * 22 + (8 if d[0] == 0 else 0)
            y = p[1] + d[1] * 22 + (-6 if d[1] == 0 else 4)
            o.append(f'<text class="rotulo" x="{x:g}" y="{y:g}" text-anchor="middle">{esc(op[clave])}</text>')
    return o, pts


def svg(diagrama):
    clases = {}
    for c in diagrama["clases"]:
        medir(c)
        clases[c["id"]] = c
    cuerpo, xs, ys = [], [], []
    for r in diagrama.get("rel", []):
        o, pts = dibujar_rel(clases, r)
        cuerpo += o
        xs += [p[0] for p in pts]
        ys += [p[1] for p in pts]
    for c in clases.values():
        cuerpo += dibujar_clase(c)
        xs += [c["x"], c["x"] + c["w"]]
        ys += [c["y"], c["y"] + c["h"]]
    x0, y0 = min(xs) - MARGEN, min(ys) - MARGEN
    w, h = max(xs) + MARGEN - x0, max(ys) + MARGEN - y0
    cabeza = (f'<svg viewBox="{x0:g} {y0:g} {w:g} {h:g}" width="{w:g}" height="{h:g}" '
              f'role="img" aria-label="{esc(diagrama.get("alt", "Diagrama de clases"))}">')
    return "\n".join([cabeza] + ["  " + l for l in cuerpo] + ["</svg>"])


def main():
    espacio = {"D": {}}
    with open(sys.argv[1], encoding="utf-8") as f:
        exec(compile(f.read(), sys.argv[1], "exec"), espacio)
    D = espacio["D"]
    raiz = sys.argv[2] if len(sys.argv) > 2 else "app/contenido/ing2"
    usados = set()
    patron = re.compile(r'(<div class="pd-grafico uml" data-g="([^"]+)">)(.*?)(\n?[ \t]*</div>)', re.S)
    for carpeta, _, archivos in os.walk(raiz):
        for archivo in sorted(archivos):
            if not archivo.endswith(".html"):
                continue
            ruta = os.path.join(carpeta, archivo)
            with open(ruta, encoding="utf-8") as f:
                viejo = f.read()

            def cambiar(m):
                if m.group(2) not in D:
                    return m.group(0)
                usados.add(m.group(2))
                sangria = re.search(r"[ \t]*$", viejo[:m.start()]).group(0) + "  "
                dibujo = "\n".join(sangria + l for l in svg(D[m.group(2)]).splitlines())
                return f"{m.group(1)}\n{dibujo}\n{sangria[:-2]}</div>"

            nuevo = patron.sub(cambiar, viejo)
            if nuevo != viejo:
                with open(ruta, "w", encoding="utf-8", newline="\n") as f:
                    f.write(nuevo)
                print("ok:", os.path.relpath(ruta, raiz))
    for nombre in sorted(set(D) - usados):
        print("SIN USAR:", nombre)


if __name__ == "__main__":
    main()
