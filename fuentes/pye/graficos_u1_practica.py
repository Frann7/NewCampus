"""Gráficos de la Práctica de la Unidad 1 de PyE (app/contenido/pye/u1/practica/).

Rellena cada <div class="pd-grafico" data-g="NOMBRE"> de esos archivos con el SVG calculado acá:
árboles (espacios muestrales, probabilidad total y Bayes), diagramas de Venn y una recta.
Uso, desde la raíz del repo:  python fuentes/pye/graficos_u1_practica.py
"""
import glob
import re
from fractions import Fraction

CARPETA = "app/contenido/pye/u1/practica"
NO = "̄"  # raya de "no" (complemento) arriba de la letra anterior


def num(v):
    if isinstance(v, Fraction):
        return f"{v.numerator}/{v.denominator}" if v.denominator != 1 else str(v.numerator)
    return f"{round(v, 4):.4f}".rstrip("0").rstrip(",.").replace(".", ",")


def esc(t):
    """Escapa el texto; una letra seguida de NO sale con la raya arriba (complemento)."""
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub("(.)" + NO, lambda m: f'<tspan style="text-decoration:overline">{m.group(1)}</tspan>', t)


# ---------------------------------------------------------------- árboles

def nodo(et, p=None, hijos=None):
    return {"et": et, "p": p, "hijos": hijos or []}


def arbol(aria, hijos, cols, paso=26, marcar=(), resultado=None, ancho=620):
    """Árbol acostado. Cada nodo: etiqueta y, si tiene, la probabilidad de su rama.
    En cada hoja se anota el producto de la rama (si hay probabilidades) o el resultado."""
    hojas = []

    def recorrer(n, camino):
        n["camino"] = camino + [n]
        if not n["hijos"]:
            hojas.append(n)
        for h in n["hijos"]:
            recorrer(h, n["camino"])

    for h in hijos:
        recorrer(h, [])
    for i, h in enumerate(hojas):
        h["y"] = 24 + i * paso

    def ubicar(n, prof):
        n["x"] = cols[prof]
        if n["hijos"]:
            for h in n["hijos"]:
                ubicar(h, prof + 1)
            n["y"] = (n["hijos"][0]["y"] + n["hijos"][-1]["y"]) / 2

    for h in hijos:
        ubicar(h, 1)
    alto = int(hojas[-1]["y"] + 24)
    y0 = (hijos[0]["y"] + hijos[-1]["y"]) / 2
    s = [f'<svg viewBox="0 0 {ancho} {alto}" role="img" aria-label="{esc(aria)}">']
    s.append(f'  <circle class="punto" cx="{cols[0]}" cy="{y0:.1f}" r="4"/>')
    largo = lambda t: len(t.replace(NO, ""))
    xa = max(h["x"] + 9 * largo(h["et"]) for h in hojas) + 18

    def dibujar(n, px, py, plen=0):
        x1 = px + (6 if plen == 0 else 9 * plen + 8)
        x2 = n["x"] - 6
        s.append(f'  <line class="eje" x1="{x1}" y1="{py:.1f}" x2="{x2}" y2="{n["y"]:.1f}"/>')
        if n["p"] is not None:
            mx, my = (x1 + x2) / 2, (py + n["y"]) / 2
            dy = -6 if n["y"] <= py else 14
            s.append(f'  <text class="rotulo" x="{mx:.1f}" y="{my + dy:.1f}" text-anchor="middle">{num(n["p"])}</text>')
        s.append(f'  <text class="valor" x="{n["x"]}" y="{n["y"] + 5:.1f}">{esc(n["et"])}</text>')
        for h in n["hijos"]:
            dibujar(h, n["x"], n["y"], largo(n["et"]))

    for h in hijos:
        dibujar(h, cols[0], y0)
    for h in hojas:
        cam = h["camino"]
        clave = tuple(c["et"] for c in cam)
        cls = "valor" if clave in marcar else "rotulo"
        if resultado == "texto":
            t = "".join(c["et"] for c in cam)
        else:
            ps = [c["p"] for c in cam]
            prod = ps[0]
            for p in ps[1:]:
                prod = prod * p
            t = " · ".join(num(p) for p in ps) + " = " + num(prod)
        s.append(f'  <text class="{cls}" x="{xa}" y="{h["y"] + 5:.1f}">{esc(t)}</text>')
    s.append('</svg>')
    return "\n".join(s)


def arbol_dos_niveles(aria, ramas, hoja_si, hoja_no, marcar=(), ancho=620):
    """Causas con su probabilidad y, en cada una, el suceso que interesa y su contrario."""
    hijos = [nodo(c, p, [nodo(hoja_si, q), nodo(hoja_no, 1 - q if not isinstance(q, Fraction) else 1 - q)])
             for c, p, q in ramas]
    for h in hijos:
        for n in h["hijos"]:
            if not isinstance(n["p"], Fraction):
                n["p"] = round(n["p"], 4)
    return arbol(aria, hijos, [30, 190, 330], paso=34, marcar=marcar, ancho=ancho)


# --- Guía 1A

def a1_ej3():
    hijos = []
    for d in range(1, 7):
        if d % 2 == 0:
            hijos.append(nodo(str(d), None, [nodo("C"), nodo("X")]))
        else:
            hijos.append(nodo(str(d), None, [nodo("C", None, [nodo("C"), nodo("X")]),
                                              nodo("X", None, [nodo("C"), nodo("X")])]))
    return arbol("Árbol: primero el dado (1 a 6); si sale par, una moneda; si sale impar, dos monedas. "
                 "18 resultados", hijos, [30, 140, 270, 390], paso=21, resultado="texto")


def a1_bolsa(a, b, na, nb):
    """Se sacan 3 de un lote con na de la clase a y nb de la clase b, sin reposición."""
    def rama(quedan_a, quedan_b, nivel):
        if nivel == 3:
            return []
        out = []
        if quedan_a > 0:
            out.append(nodo(a, None, rama(quedan_a - 1, quedan_b, nivel + 1)))
        if quedan_b > 0:
            out.append(nodo(b, None, rama(quedan_a, quedan_b - 1, nivel + 1)))
        return out
    return rama(na, nb, 0)


def a1_ej5():
    return arbol("Árbol de los tres autos: en cada uno, manchado (M) o no manchado; como hay solo dos "
                 "manchados, después de dos M el tercero no puede ser M. 7 resultados",
                 a1_bolsa("M", "M" + NO, 2, 3), [30, 160, 290, 420], paso=30, resultado="texto")


def a1_ej6():
    return arbol("Árbol de las tres computadoras: en cada una, defectuosa (D) o no defectuosa (N); "
                 "como hay solo dos defectuosas, después de dos D la tercera es N. 7 resultados",
                 a1_bolsa("D", "N", 2, 5), [30, 160, 290, 420], paso=30, resultado="texto")


def a1_ej7():
    def cadena(k):
        if k == 0:
            return [nodo("C"), nodo("X", None, [nodo("…")])]
        return [nodo("C"), nodo("X", None, cadena(k - 1))]
    hijos = cadena(3)
    svg = arbol("Árbol de la moneda que se tira hasta que sale cara: en cada tiro, cara (termina) o "
                "cruz (sigue); no tiene fin", hijos, [30, 130, 230, 330, 430, 520], paso=34,
                resultado="texto")
    return svg.replace("XXXX…", "y así sigue")


def a1_ej8():
    hijos = []
    for m1 in "CX":
        hijos2 = []
        for m2 in "CX":
            if m1 == m2:
                hijos2.append(nodo(m2, None, [nodo(str(d)) for d in range(1, 7)]))
            else:
                hijos2.append(nodo(m2, None, [nodo(c) for c in ("B", "R", "N")]))
        hijos.append(nodo(m1, None, hijos2))
    return arbol("Árbol: dos monedas; si salen iguales se tira un dado, si salen distintas se saca una "
                 "bolilla blanca, roja o negra. 18 resultados", hijos, [30, 150, 290, 420], paso=21,
                 resultado="texto")


# --- Guía Probabilidad: total y Bayes

RADAR = [("L1", 0.2, 0.4), ("L2", 0.1, 0.3), ("L3", 0.5, 0.2), ("L4", 0.2, 0.3)]


def ej16():
    return arbol_dos_niveles("Árbol: lugar por el que pasa (L1 a L4) y si lo multan (M) o no",
                             RADAR, "M", "M" + NO, marcar={(l, "M") for l, _, _ in RADAR})


def ej17():
    return arbol_dos_niveles("Árbol: lugar por el que pasa (L1 a L4) y si lo multan (M) o no; "
                             "resaltada la rama L2 y M", RADAR, "M", "M" + NO, marcar={("L2", "M")})


CONSULT = [("A", 0.40, 0.05), ("B", 0.35, 0.03), ("C", 0.25, 0.15)]


def ej18():
    return arbol_dos_niveles("Árbol: consultora A, B o C y si hay exceso de costos (E) o no",
                             CONSULT, "E", "E" + NO, marcar={(c, "E") for c, _, _ in CONSULT})


def ej19():
    r = [("I1", 0.7, 0.02), ("I2", 0.3, 0.04)]
    return arbol_dos_niveles("Árbol: ingeniero 1 o 2 y si comete error (E) o no", r, "E", "E" + NO,
                             marcar={("I1", "E"), ("I2", "E")})


def ej20():
    r = [("A", 0.7, 0.2), ("B", 0.3, 0.1)]
    return arbol_dos_niveles("Árbol: método A o B y si la persona no aprende (N) o aprende", r, "N",
                             "N" + NO, marcar={("A", "N"), ("B", "N")})


def ej21():
    r = [("I", 0.5, 0.04), ("II", 0.3, 0.06), ("III", 0.2, 0.02)]
    return arbol_dos_niveles("Árbol: línea I, II o III y si el componente es defectuoso (D) o no", r,
                             "D", "D" + NO, marcar={("I", "D"), ("II", "D"), ("III", "D")})


def ej22b():
    F = Fraction
    r = [("Urna A", F(1, 2), F(2, 3)), ("Urna B", F(1, 2), F(1, 3))]
    return arbol_dos_niveles("Árbol: se elige la urna A o la B (mitad y mitad) y después la bola, "
                             "blanca (Bl) o negra (Ne)", r, "Bl", "Ne",
                             marcar={("Urna A", "Bl"), ("Urna B", "Bl")})


def ej22c():
    F = Fraction
    r = [("Bl de A", F(2, 3), F(2, 4)), ("Ne de A", F(1, 3), F(1, 4))]
    return arbol_dos_niveles("Árbol: primero la bola que pasa de A a B (blanca o negra) y después la "
                             "que se saca de B", r, "Bl de B", "Ne de B",
                             marcar={("Bl de A", "Bl de B"), ("Ne de A", "Bl de B")})


# ---------------------------------------------------------------- Venn

def venn(aria, na, nb, solo_a, ambos, solo_b, fuera, separados=False):
    s = [f'<svg viewBox="0 0 620 260" role="img" aria-label="{esc(aria)}">']
    s.append('  <rect class="eje" x="20" y="16" width="580" height="228" rx="6" style="fill:none"/>')
    s.append('  <text class="rotulo" x="34" y="38">S</text>')
    if separados:
        (ca, cb, r) = (200, 420, 85)
    else:
        (ca, cb, r) = (245, 375, 100)
    for c, cls in ((ca, "area suave"), (cb, "area b suave")):
        s.append(f'  <circle class="{cls}" cx="{c}" cy="132" r="{r}"/>')
        s.append(f'  <circle class="corte" cx="{c}" cy="132" r="{r}" style="fill:none"/>')
    s.append(f'  <text class="valor" x="{ca - r + 6}" y="{132 - r + 12}" text-anchor="end">{esc(na)}</text>')
    s.append(f'  <text class="valor" x="{cb + r - 6}" y="{132 - r + 12}">{esc(nb)}</text>')
    if separados:
        s.append(f'  <text class="valor" x="{ca}" y="137" text-anchor="middle">{num(solo_a)}</text>')
        s.append(f'  <text class="valor" x="{cb}" y="137" text-anchor="middle">{num(solo_b)}</text>')
    else:
        s.append(f'  <text class="valor" x="{ca - 50}" y="137" text-anchor="middle">{num(solo_a)}</text>')
        s.append(f'  <text class="valor" x="{(ca + cb) / 2}" y="137" text-anchor="middle">{num(ambos)}</text>')
        s.append(f'  <text class="valor" x="{cb + 50}" y="137" text-anchor="middle">{num(solo_b)}</text>')
    s.append(f'  <text class="valor" x="585" y="232" text-anchor="end">afuera: {num(fuera)}</text>')
    s.append('</svg>')
    return "\n".join(s)


def recta():
    """Ej. 10: la vida del componente sobre una recta de horas."""
    X = lambda h: 60 + h / 10000 * 500
    s = ['<svg viewBox="0 0 620 250" role="img" aria-label="Recta de horas de vida: B es de 0 a 4000, '
         'A es más de 6000; sus contrarios son más de 4000 y hasta 6000">']
    filas = [(40, 0, 4000, "B: no dura más de 4000 h · 0,04", True),
             (80, 6000, 10000, "A: más de 6000 h · 0,42", True),
             (175, 0, 6000, "A" + NO + ": 6000 h o menos · 0,58", False),
             (215, 4000, 10000, "B" + NO + ": más de 4000 h · 0,96", False)]
    yeje = 128
    s.append(f'  <line class="eje" x1="40" y1="{yeje}" x2="600" y2="{yeje}"/>')
    s.append(f'  <line class="eje" x1="600" y1="{yeje}" x2="590" y2="{yeje - 5}"/>')
    s.append(f'  <line class="eje" x1="600" y1="{yeje}" x2="590" y2="{yeje + 5}"/>')
    for h in (0, 4000, 6000):
        s.append(f'  <line class="eje" x1="{X(h)}" y1="{yeje - 6}" x2="{X(h)}" y2="{yeje + 6}"/>')
        s.append(f'  <text class="rotulo" x="{X(h)}" y="{yeje + 22}" text-anchor="middle">{h}</text>')
        s.append(f'  <line class="guia" x1="{X(h)}" y1="30" x2="{X(h)}" y2="225"/>')
    s.append(f'  <text class="rotulo" x="600" y="{yeje + 22}" text-anchor="end">horas</text>')
    for y, a, b, t, arriba in filas:
        cls = "corte" if arriba else "corte"
        estilo = "stroke-width:5" if arriba else "stroke-width:5;stroke:var(--practica)"
        s.append(f'  <line class="{cls}" x1="{X(a)}" y1="{y}" x2="{min(X(b), 595)}" y2="{y}" style="{estilo}"/>')
        tx = X(a) + 6 if a > 0 else X(0) + 6
        s.append(f'  <text class="valor" x="{tx}" y="{y - 9}">{esc(t)}</text>')
    s.append('</svg>')
    return "\n".join(s)


GRAFICOS = {
    "u1p-1a-ej3-arbol": a1_ej3,
    "u1p-1a-ej5-arbol": a1_ej5,
    "u1p-1a-ej6-arbol": a1_ej6,
    "u1p-1a-ej7-arbol": a1_ej7,
    "u1p-1a-ej8-arbol": a1_ej8,
    "u1p-ej1-venn": lambda: venn("Venn: Buenos Aires y Córdoba", "A: Buenos Aires", "B: Córdoba", 0.4, 0.3, 0.1, 0.2),
    "u1p-ej2-venn": lambda: venn("Venn: bonos y fondos", "B", "F", 0.45, 0.15, 0.15, 0.25),
    "u1p-ej4-venn": lambda: venn("Venn: frenos y combustible", "F", "C", 0.10, 0.15, 0.02, 0.73),
    "u1p-ej10-recta": recta,
    "u1p-ej11-venn": lambda: venn("Venn: falla y se deforma sin fallar, separados", "A", "B", 0.20, 0, 0.35,
                                  0.45, separados=True),
    "u1p-ej12-venn": lambda: venn("Venn: aceite y filtro", "A", "F", 0.11, 0.14, 0.26, 0.49),
    "u1p-ej13-venn": lambda: venn("Venn: esposo y esposa", "H", "M", 0.05, 0.35, 0.15, 0.45),
    "u1p-ej16-arbol": ej16,
    "u1p-ej17-arbol": ej17,
    "u1p-ej18-arbol": ej18,
    "u1p-ej19-arbol": ej19,
    "u1p-ej20-arbol": ej20,
    "u1p-ej21-arbol": ej21,
    "u1p-ej22b-arbol": ej22b,
    "u1p-ej22c-arbol": ej22c,
}


def main():
    usados = set()
    for ruta in glob.glob(f"{CARPETA}/*.html"):
        texto = open(ruta, encoding="utf-8").read()
        nuevo = texto
        for nombre, fn in GRAFICOS.items():
            patron = re.compile(r'(<div class="pd-grafico" data-g="' + nombre + r'">)(.*?)(</div>)', re.S)
            if patron.search(nuevo):
                usados.add(nombre)
            nuevo = patron.sub(lambda m: m.group(1) + "\n" + fn() + "\n" + m.group(3), nuevo)
        if nuevo != texto:
            open(ruta, "w", encoding="utf-8", newline="\n").write(nuevo)
            print("actualizado", ruta)
    for nombre in GRAFICOS:
        if nombre not in usados:
            print("sin usar:", nombre)


if __name__ == "__main__":
    main()
