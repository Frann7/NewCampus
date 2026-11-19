"""Gráficos de la teoría de la Unidad 1 de PyE (app/contenido/pye/u1/teoria/).

Rellena cada <div class="pd-grafico" data-g="u1-..."> de esos archivos con el SVG calculado acá
(deja intacto el <p class="pd-pie"> que va después del SVG). Un mismo nombre puede aparecer en
varios archivos: así cada ejemplo repite su diagrama.
Uso, desde la raíz del repo:  python fuentes/pye/graficos_u1.py
"""
import glob
import math
import re

CARPETA = "app/contenido/pye/u1/teoria"

COL_A = "var(--teoria)"
COL_B = "var(--practica)"
COL_C = "var(--ok)"


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------------------------------------------------------------- árboles

def arbol(raiz, ancho_nivel, alto_hoja, x_hojas_texto=None, rotulo_raiz=None, aria="", cabeceras=None):
    """Árbol horizontal. Cada nodo es un dict: {"t": texto, "p": prob. de la rama, "h": [hijos],
    "hoja": texto al final, "marca": True si la hoja se destaca}."""
    hojas = []

    def contar(n, nivel):
        if not n.get("h"):
            hojas.append(n)
            n["_nivel"] = nivel
            return
        for h in n["h"]:
            contar(h, nivel + 1)
    contar(raiz, 0)
    niveles = max(h["_nivel"] for h in hojas)
    arriba = 38 if cabeceras else 18
    alto = arriba + alto_hoja * len(hojas) + 10
    x0 = 30 if not rotulo_raiz else 30 + 8 * len(rotulo_raiz)
    xs = [x0 + i * ancho_nivel for i in range(niveles + 1)]
    x_txt = x_hojas_texto or xs[-1] + 36
    s = [f'<svg viewBox="0 0 620 {alto}" role="img" aria-label="{esc(aria)}">']
    if cabeceras:
        for x, c in zip(xs[1:] + [x_txt], cabeceras):
            if c:
                anchor = "start" if x == x_txt else "middle"
                s.append(f'  <text class="rotulo" x="{x}" y="18" text-anchor="{anchor}">{esc(c)}</text>')
    contador = [0]

    def pos(n, nivel):
        if not n.get("h"):
            y = arriba + alto_hoja * contador[0] + alto_hoja / 2
            contador[0] += 1
        else:
            ys = [pos(h, nivel + 1) for h in n["h"]]
            y = sum(ys) / len(ys)
        n["_y"], n["_x"] = y, xs[nivel]
        return y
    pos(raiz, 0)

    def dibujar(n, nivel):
        x, y = n["_x"], n["_y"]
        for h in n.get("h", []):
            hx, hy = h["_x"], h["_y"]
            xa = x + (10 if nivel > 0 else 4)
            s.append(f'  <line class="eje" x1="{xa}" y1="{y:.1f}" x2="{hx - 14}" y2="{hy:.1f}"/>')
            if h.get("p"):
                mx, my = (xa + hx - 14) / 2, (y + hy) / 2
                dy = -7 if hy <= y else 15
                s.append(f'  <text class="rotulo" x="{mx:.1f}" y="{my + dy:.1f}" text-anchor="middle">{esc(h["p"])}</text>')
            s.append(f'  <text class="valor" x="{hx - 4}" y="{hy + 5:.1f}">{esc(h["t"])}</text>')
            dibujar(h, nivel + 1)
        if not n.get("h") and n.get("hoja"):
            cls = "valor" if n.get("marca") else "rotulo"
            s.append(f'  <text class="{cls}" x="{x_txt}" y="{y + 5:.1f}">{esc(n["hoja"])}</text>')
    if rotulo_raiz:
        s.append(f'  <text class="rotulo" x="{x0 - 8}" y="{raiz["_y"] + 5:.1f}" text-anchor="end">{esc(rotulo_raiz)}</text>')
    else:
        s.append(f'  <circle class="punto" cx="{x0}" cy="{raiz["_y"]:.1f}" r="4"/>')
    dibujar(raiz, 0)
    s.append("</svg>")
    return "\n".join(s)


def n(t, p=None, h=None, hoja=None, marca=False):
    d = {"t": t}
    if p:
        d["p"] = p
    if h:
        d["h"] = h
    if hoja:
        d["hoja"] = hoja
    d["marca"] = marca
    return d


def arbol_moneda_dado():
    raiz = n("", h=[n("C", h=[n("C", hoja="CC"), n("X", hoja="CX")]),
                   n("X", h=[n(str(i), hoja=f"X{i}") for i in range(1, 7)])])
    return arbol(raiz, 150, 30, aria="Diagrama de tallo y hojas: moneda; si sale cara, otra moneda; "
                 "si sale cruz, un dado", cabeceras=["Suceso 1", "Suceso 2", "E. M."])


def arbol_tres(letras, raiz_txt, aria, probs=None, marca=None):
    """Tres pasos con dos opciones cada uno (artículos D/N, casos de prueba P/F)."""
    def rama(prefijo, nivel):
        hijos = []
        for l in letras:
            p = probs[l] if probs else None
            camino = prefijo + l
            if nivel == 3:
                hoja = camino
                if probs:
                    fac = " · ".join(probs[c] for c in camino)
                    val = 1.0
                    for c in camino:
                        val *= float(probs[c].replace(",", "."))
                    hoja = f"{camino}:  {fac} = {val:.3f}".replace(".", ",")
                hijos.append(n(l, p, hoja=hoja, marca=bool(marca and marca(camino))))
            else:
                hijos.append(n(l, p, h=rama(camino, nivel + 1)))
        return hijos
    raiz = n("", h=rama("", 1))
    return arbol(raiz, 105 if probs else 120, 32, rotulo_raiz=raiz_txt, aria=aria,
                 cabeceras=["1.º", "2.º", "3.º", "Resultado"])


def arbol_articulos():
    return arbol_tres("DN", "Fabricación", "Diagrama de árbol de tres artículos, cada uno D o N")


def arbol_casos():
    return arbol_tres("PF", "3 casos", "Diagrama de árbol de tres casos de prueba, cada uno pasa (P) o falla (F)")


def arbol_casos_p():
    return arbol_tres("PF", "3 casos", "Árbol de tres casos de prueba con probabilidad 0,9 de pasar y 0,1 de fallar",
                      probs={"P": "0,9", "F": "0,1"}, marca=lambda c: c.count("F") == 2)


def arbol_dos_niveles(primeros, segundo, aria, x_txt=352):
    """primeros: [(nombre, prob, [(nombre2, prob2, texto hoja, marca), ...]), ...]"""
    raiz = n("", h=[n(a, p, h=[n(b, q, hoja=t, marca=m) for b, q, t, m in hijos]) for a, p, hijos in primeros])
    return arbol(raiz, 140, 36, x_hojas_texto=x_txt, aria=aria, cabeceras=segundo)


def arbol_general():
    prim = []
    for i in ("₁", "₂", "₃"):
        prim.append((f"B{i}", f"P(B{i})", [("A", f"P(A/B{i})", f"P(B{i})·P(A/B{i}) = P(B{i} ∩ A)", True),
                                            ("Ā", f"P(Ā/B{i})", f"P(B{i})·P(Ā/B{i}) = P(B{i} ∩ Ā)", False)]))
    return arbol_dos_niveles(prim, ["Partición", "Evento", "Producto de las ramas"],
                             "Árbol general: partición B1, B2, B3 y después A o no A")


def arbol_ej20():
    datos = [("B₁", "0,30", "0,02", "0,98"), ("B₂", "0,45", "0,03", "0,97"), ("B₃", "0,25", "0,02", "0,98")]
    prim = []
    for b, p, d, nd in datos:
        pa = float(p.replace(",", ".")) * float(d.replace(",", "."))
        pn = float(p.replace(",", ".")) * float(nd.replace(",", "."))
        prim.append((b, p, [("A", d, f"{p} · {d} = {pa:.4f}".replace(".", ","), True),
                            ("Ā", nd, f"{p} · {nd} = {pn:.4f}".replace(".", ","), False)]))
    return arbol_dos_niveles(prim, ["Máquina", "Defectuoso", "Producto de las ramas"],
                             "Árbol de las tres máquinas y producto defectuoso o no")


def arbol_motores():
    prim = [("A", "0,90", [("D", "0,05", "0,90 · 0,05 = 0,045", True), ("D̄", "0,95", "0,90 · 0,95 = 0,855", False)]),
            ("B", "0,10", [("D", "0,03", "0,10 · 0,03 = 0,003", True), ("D̄", "0,97", "0,10 · 0,97 = 0,097", False)])]
    return arbol_dos_niveles(prim, ["Proveedor", "Motor", "Producto de las ramas"],
                             "Árbol de los motores: proveedor A o B y motor defectuoso o no")


def arbol_urnas(marca_roja=False):
    prim = [("U₁", "1/2", [("Bl", "3/5", "1/2 · 3/5 = 3/10", not marca_roja), ("R", "2/5", "1/2 · 2/5 = 2/10", marca_roja)]),
            ("U₂", "1/2", [("Bl", "4/6", "1/2 · 4/6 = 4/12", not marca_roja), ("R", "2/6", "1/2 · 2/6 = 2/12", marca_roja)])]
    return arbol_dos_niveles(prim, ["Moneda → urna", "Bola", "Producto de las ramas"],
                             "Árbol de las dos urnas: cara a la urna 1, cruz a la urna 2, y bola blanca o roja")


def arbol_urnas_roja():
    return arbol_urnas(True)


def arbol_scripts(con=False):
    if con:
        prim = [("Py", "7/12", [("Py", "7/12", "7/12 · 7/12 = 49/144", False), ("JS", "5/12", "7/12 · 5/12 = 35/144", True)]),
                ("JS", "5/12", [("Py", "7/12", "5/12 · 7/12 = 35/144", False), ("JS", "5/12", "5/12 · 5/12 = 25/144", False)])]
    else:
        prim = [("Py", "7/12", [("Py", "6/11", "7/12 · 6/11 = 42/132", False), ("JS", "5/11", "7/12 · 5/11 = 35/132", True)]),
                ("JS", "5/12", [("Py", "7/11", "5/12 · 7/11 = 35/132", False), ("JS", "4/11", "5/12 · 4/11 = 20/132", False)])]
    return arbol_dos_niveles(prim, ["1.er script", "2.º script", "Producto de las ramas"],
                             "Árbol de dos scripts sacados " + ("con" if con else "sin") + " reposición")


def arbol_scripts_con():
    return arbol_scripts(True)


# ---------------------------------------------------------------- Venn

def rect_s(x, y, w, h, rot="S"):
    return [f'  <rect class="eje" x="{x}" y="{y}" width="{w}" height="{h}" fill="none"/>',
            f'  <text class="valor" x="{x + 10}" y="{y + 20}">{rot}</text>']


def circ(cx, cy, r, color=COL_A, rx=None):
    if rx:
        return f'  <ellipse class="campana" cx="{cx}" cy="{cy}" rx="{rx}" ry="{r}" style="stroke:{color}"/>'
    return f'  <circle class="campana" cx="{cx}" cy="{cy}" r="{r}" style="stroke:{color}"/>'


def txt(x, y, t, cls="rotulo", anchor="middle", color=None):
    st = f' style="fill:{color}"' if color else ""
    return f'  <text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}"{st}>{esc(t)}</text>'


def dentro(p, c):
    (x, y), (cx, cy, r) = p, c
    return (x - cx) ** 2 + (y - cy) ** 2 < r * r


def comprobar(puntos, circulos, conjuntos):
    """Verifica que cada número caiga exactamente en los círculos que dice su conjunto."""
    for num, p in puntos.items():
        for nombre, c in circulos.items():
            assert dentro(p, c) == (num in conjuntos[nombre]), (num, nombre)


def venn_dado():
    circulos = {"A": (190, 150, 82), "B": (300, 175, 75), "C": (420, 75, 42)}
    conj = {"A": {1, 3, 5}, "B": {5, 6}, "C": {2}}
    puntos = {1: (170, 110), 3: (160, 190), 5: (250, 165), 6: (340, 190), 2: (420, 82), 4: (510, 200)}
    comprobar(puntos, circulos, conj)
    s = ['<svg viewBox="0 0 620 270" role="img" aria-label="Diagrama de Venn del dado: A impar, B mayor que 4, C igual a 2">']
    s += rect_s(60, 15, 500, 240)
    for (k, (cx, cy, r)), col in zip(circulos.items(), (COL_A, COL_B, COL_C)):
        s.append(circ(cx, cy, r, col))
    s.append(txt(140, 85, "A", "valor", color=COL_A))
    s.append(txt(375, 115, "B", "valor", color=COL_B))
    s.append(txt(470, 50, "C", "valor", color=COL_C))
    for k, (x, y) in puntos.items():
        s.append(txt(x, y + 5, str(k), "valor"))
    s.append("</svg>")
    return "\n".join(s)


def lente(c1, c2):
    """Path de la intersección de dos círculos del mismo radio."""
    (x1, y1, r), (x2, y2, _) = c1, c2
    d = math.hypot(x2 - x1, y2 - y1)
    a = d / 2
    h = math.sqrt(r * r - a * a)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    p1 = (mx - uy * h, my + ux * h)
    p2 = (mx + uy * h, my - ux * h)
    return (f"M {p1[0]:.1f},{p1[1]:.1f} A {r},{r} 0 0 1 {p2[0]:.1f},{p2[1]:.1f} "
            f"A {r},{r} 0 0 1 {p1[0]:.1f},{p1[1]:.1f} Z")


def circ_path(cx, cy, r):
    return f"M {cx - r},{cy} a {r},{r} 0 1 0 {2 * r},0 a {r},{r} 0 1 0 {-2 * r},0 Z"


def venn_operaciones():
    """Cuatro paneles: complemento, intersección, unión, excluyentes."""
    s = ['<svg viewBox="0 0 620 400" role="img" aria-label="Cuatro diagramas de Venn: complemento de A, '
         'A intersección B, A unión B, y A y B excluyentes">']
    paneles = [(15, 15, "Complemento: Ā"), (320, 15, "Intersección: A ∩ B"),
               (15, 210, "Unión: A ∪ B"), (320, 210, "Excluyentes: A ∩ B = ∅")]
    for i, (x, y, tit) in enumerate(paneles):
        w, h = 285, 165
        cy = y + 95
        if i == 0:
            ca = (x + 142, cy, 50)
            s.append(f'  <path class="area" fill-rule="evenodd" d="M {x},{y + 25} h {w} v {h - 25} h {-w} Z {circ_path(*ca)}"/>')
            s += rect_s(x, y + 25, w, h - 25)
            s.append(circ(*ca))
            s.append(txt(ca[0], cy + 5, "A", "valor", color=COL_A))
        else:
            if i == 3:
                ca, cb = (x + 85, cy, 45), (x + 200, cy, 45)
            else:
                ca, cb = (x + 115, cy, 55), (x + 170, cy, 55)
            if i == 1:
                s.append(f'  <path class="area" d="{lente(ca, cb)}"/>')
            if i == 2:
                s.append(f'  <g style="opacity:.35"><circle class="area" style="opacity:1" cx="{ca[0]}" cy="{ca[1]}" r="{ca[2]}"/>'
                         f'<circle class="area" style="opacity:1" cx="{cb[0]}" cy="{cb[1]}" r="{cb[2]}"/></g>')
            s += rect_s(x, y + 25, w, h - 25)
            s.append(circ(*ca))
            s.append(circ(*cb[:3], color=COL_B))
            s.append(txt(ca[0] - (20 if i != 3 else 0), cy + 5, "A", "valor", color=COL_A))
            s.append(txt(cb[0] + (20 if i != 3 else 0), cy + 5, "B", "valor", color=COL_B))
        s.append(txt(x + w / 2, y + 14, tit, "valor"))
    s.append("</svg>")
    return "\n".join(s)


def venn_ej6():
    circulos = {"A": (230, 115, 80), "B": (340, 115, 80), "C": (285, 205, 80)}
    conj = {"A": {7, 2, 1, 4}, "B": {2, 6, 1, 3}, "C": {4, 1, 3, 5}}
    puntos = {7: (195, 95), 2: (285, 85), 6: (375, 95), 1: (285, 150), 4: (240, 170), 3: (330, 170), 5: (285, 240)}
    comprobar(puntos, circulos, conj)
    s = ['<svg viewBox="0 0 620 310" role="img" aria-label="Diagrama de Venn con tres eventos A, B y C y los elementos 1 a 7">']
    s += rect_s(120, 15, 330, 290)
    for (k, (cx, cy, r)), col in zip(circulos.items(), (COL_A, COL_B, COL_C)):
        s.append(circ(cx, cy, r, col))
    s.append(txt(175, 45, "A", "valor", color=COL_A))
    s.append(txt(400, 45, "B", "valor", color=COL_B))
    s.append(txt(355, 290, "C", "valor", color=COL_C))
    for k, (x, y) in puntos.items():
        s.append(txt(x, y + 5, str(k), "valor"))
    s.append("</svg>")
    return "\n".join(s)


def venn_ej16():
    # A = {4, 5, 6} (elipse), B = {2, 4, 6} (círculo)
    s = ['<svg viewBox="0 0 620 270" role="img" aria-label="Diagrama de Venn del dado: A mayor que 3 y B par">']
    ea = (340, 165, 60, 160)  # cx, cy, ry, rx
    cb = (450, 120, 78)
    puntos = {1: (150, 70), 3: (150, 220), 5: (255, 170), 4: (430, 180), 6: (480, 168), 2: (465, 72)}
    for k, (x, y) in puntos.items():
        en_a = ((x - ea[0]) / ea[3]) ** 2 + ((y - ea[1]) / ea[2]) ** 2 < 1
        assert en_a == (k in {4, 5, 6}), k
        assert dentro((x, y), cb) == (k in {2, 4, 6}), k
    s += rect_s(60, 15, 500, 240)
    s.append(circ(ea[0], ea[1], ea[2], COL_A, rx=ea[3]))
    s.append(circ(*cb, color=COL_B))
    s.append(txt(225, 125, "A", "valor", color=COL_A))
    s.append(txt(515, 70, "B", "valor", color=COL_B))
    for k, (x, y) in puntos.items():
        s.append(txt(x, y + 5, str(k), "valor"))
    s.append("</svg>")
    return "\n".join(s)


def venn_ej18():
    circulos = {"A": (320, 140, 105), "B": (310, 165, 62)}
    conj = {"A": {2, 3, 4, 5, 6}, "B": {2, 4, 6}}
    puntos = {1: (150, 60), 5: (330, 65), 3: (395, 115), 2: (300, 130), 4: (285, 195), 6: (340, 190)}
    comprobar(puntos, circulos, conj)
    s = ['<svg viewBox="0 0 620 270" role="img" aria-label="Diagrama de Venn del dado: A mayor que 1 y B par, con B dentro de A">']
    s += rect_s(110, 15, 400, 245)
    s.append(circ(*circulos["A"]))
    s.append(circ(*circulos["B"], color=COL_B))
    s.append(txt(410, 55, "A", "valor", color=COL_A))
    s.append(txt(238, 150, "B", "valor", color=COL_B))
    for k, (x, y) in puntos.items():
        s.append(txt(x, y + 5, str(k), "valor"))
    s.append("</svg>")
    return "\n".join(s)


def particion(rotulos, centro_a, porcentajes_a=None, aria=""):
    """S partido en tres regiones (B1 arriba a la izquierda, B2 a la derecha, B3 abajo a la izquierda)
    con el evento A en el medio, como en el apunte."""
    x0, y0, x1, y1 = 60, 15, 560, 285
    cx, cy = 320, 155
    s = [f'<svg viewBox="0 0 620 300" role="img" aria-label="{esc(aria)}">']
    s.append(f'  <circle class="area suave" cx="{cx}" cy="{cy}" r="75"/>')
    s += rect_s(x0, y0, x1 - x0, y1 - y0)
    for (xa, ya) in ((x0, 170), (370, y0), (430, y1)):
        s.append(f'  <line class="corte" x1="{xa}" y1="{ya}" x2="{cx}" y2="{cy}" style="stroke:{COL_B};stroke-width:2"/>')
    s.append(circ(cx, cy, 75))
    s.append(txt(cx + 52, cy - 62, "A", "valor", color=COL_A))
    (r1, r2, r3) = rotulos
    s.append(txt(150, 70, r1, "valor", color=COL_B))
    s.append(txt(480, 120, r2, "valor", color=COL_B))
    s.append(txt(150, 250, r3, "valor", color=COL_B))
    if porcentajes_a:
        p1, p2, p3 = porcentajes_a
        s.append(txt(282, 135, p1, "rotulo"))
        s.append(txt(355, 165, p2, "rotulo"))
        s.append(txt(300, 200, p3, "rotulo"))
    s.append("</svg>")
    return "\n".join(s)


def particion_general():
    return particion(("B₁", "B₂", "B₃"), None, ("B₁ ∩ A", "B₂ ∩ A", "B₃ ∩ A"),
                     aria="Espacio muestral partido en B1, B2 y B3, con el evento A repartido entre los tres")


def particion_ej20():
    return particion(("B₁ 30 %", "B₂ 45 %", "B₃ 25 %"), None, ("2 %", "3 %", "2 %"),
                     aria="Espacio muestral partido en las tres máquinas, con el evento A defectuoso repartido entre las tres")


GRAFICOS = {
    "u1-arbol-moneda-dado": arbol_moneda_dado,
    "u1-arbol-articulos": arbol_articulos,
    "u1-arbol-casos": arbol_casos,
    "u1-arbol-casos-p": arbol_casos_p,
    "u1-venn-dado": venn_dado,
    "u1-venn-operaciones": venn_operaciones,
    "u1-venn-ej6": venn_ej6,
    "u1-venn-ej16": venn_ej16,
    "u1-venn-ej18": venn_ej18,
    "u1-particion-general": particion_general,
    "u1-particion-ej20": particion_ej20,
    "u1-arbol-general": arbol_general,
    "u1-arbol-ej20": arbol_ej20,
    "u1-arbol-motores": arbol_motores,
    "u1-arbol-urnas": arbol_urnas,
    "u1-arbol-urnas-roja": arbol_urnas_roja,
    "u1-arbol-scripts": arbol_scripts,
    "u1-arbol-scripts-con": arbol_scripts_con,
}


def main():
    usados = set()
    patron = re.compile(r'(<div class="pd-grafico" data-g="(u1-[\w-]+)">)(\s*<svg.*?</svg>)?', re.S)
    for ruta in sorted(glob.glob(f"{CARPETA}/*.html")):
        texto = open(ruta, encoding="utf-8").read()

        def poner(m):
            nombre = m.group(2)
            usados.add(nombre)
            return m.group(1) + "\n" + GRAFICOS[nombre]()
        nuevo = patron.sub(poner, texto)
        if nuevo != texto:
            open(ruta, "w", encoding="utf-8", newline="\n").write(nuevo)
            print("actualizado", ruta)
    sobran = set(GRAFICOS) - usados
    if sobran:
        print("sin usar:", ", ".join(sorted(sobran)))


if __name__ == "__main__":
    main()
