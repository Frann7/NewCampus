"""Gráficos del Final 10/12/2025 de PyE (app/contenido/pye/evaluacion/finales/2025-12-10-final/).

Ej. 1: árbol de las dos urnas, armado por niveles (moneda → bola → producto). Ej. 3: la campana de la
glucosa armada paso a paso (ejes → puntos → curva), el 25 % más alto y sus propiedades. Ej. 4: la campana
Z de la prueba de hipótesis en tres pasos (campana → región de rechazo → estadístico).
Rellena el <svg> que está dentro de cada <div class="pd-grafico" data-g="NOMBRE"> (el pie no se toca).
Uso, desde la raíz del repo:  python fuentes/pye/graficos_final_2025_12_10.py
"""
import glob
import re
from fractions import Fraction

from scipy import stats

CARPETA = "app/contenido/pye/evaluacion/finales/2025-12-10-final"


def num(v, dec=2):
    if isinstance(v, Fraction):
        return f"{v.numerator}/{v.denominator}" if v.denominator != 1 else str(v.numerator)
    return f"{v:.{dec}f}".replace(".", ",").replace("-", "−")


# ---------------------------------------------------------------- Ej. 1: árbol

def arbol(nivel=3):
    """nivel 1: la moneda; 2: más el color de la bola; 3: más el producto de cada camino."""
    # fracciones sin simplificar, como salen de contar bolas (4/6, no 2/3)
    ramas = [("U₁", (1, 2), [("Bl", (3, 5)), ("R", (2, 5))]),
             ("U₂", (1, 2), [("Bl", (4, 6)), ("R", (2, 6))])]
    fr = lambda p: f"{p[0]}/{p[1]}"
    cols, paso, y0hoja = [30, 170, 310], 36, 56
    aria = {1: "Paso 1 del árbol: de la raíz salen dos ramas, cara (1/2) a la urna 1 y cruz (1/2) a la urna 2",
            2: "Paso 2 del árbol: de la urna 1 salen blanca 3/5 y roja 2/5; de la urna 2, blanca 4/6 y roja 2/6",
            3: "Árbol de las dos urnas: cara (1/2) a la urna 1 y cruz (1/2) a la urna 2; de la urna 1 blanca 3/5 "
               "y roja 2/5; de la urna 2 blanca 4/6 y roja 2/6"}[nivel]
    s = [f'<svg viewBox="0 0 620 192" role="img" aria-label="{aria}">',
         f'  <text class="rotulo" x="{cols[1]}" y="18" text-anchor="middle">Moneda → urna</text>']
    if nivel >= 2:
        s.append(f'  <text class="rotulo" x="{cols[2]}" y="18" text-anchor="middle">Bola</text>')
    if nivel >= 3:
        s.append('  <text class="rotulo" x="352" y="18" text-anchor="start">Producto de las ramas</text>')
    hojas_y = [y0hoja + i * paso for i in range(4)]
    urnas_y = [(hojas_y[0] + hojas_y[1]) / 2, (hojas_y[2] + hojas_y[3]) / 2]
    raiz_y = sum(urnas_y) / 2
    s.append(f'  <circle class="punto" cx="{cols[0]}" cy="{raiz_y:.1f}" r="4"/>')
    for i, (urna, pu, bolas) in enumerate(ramas):
        uy = urnas_y[i]
        x1, x2 = cols[0] + 4, cols[1] - 14
        s.append(f'  <line class="eje" x1="{x1}" y1="{raiz_y:.1f}" x2="{x2}" y2="{uy:.1f}"/>')
        dy = -6 if uy < raiz_y else 14
        s.append(f'  <text class="rotulo" x="{(x1 + x2) / 2:.1f}" y="{(raiz_y + uy) / 2 + dy:.1f}" '
                 f'text-anchor="middle">{fr(pu)}</text>')
        s.append(f'  <text class="valor" x="{cols[1] - 4}" y="{uy + 5:.1f}">{urna}</text>')
        if nivel < 2:
            continue
        for j, (bola, pb) in enumerate(bolas):
            hy = hojas_y[2 * i + j]
            x1, x2 = cols[1] + 10, cols[2] - 14
            s.append(f'  <line class="eje" x1="{x1}" y1="{uy:.1f}" x2="{x2}" y2="{hy:.1f}"/>')
            dy = -6 if hy < uy else 14
            s.append(f'  <text class="rotulo" x="{(x1 + x2) / 2:.1f}" y="{(uy + hy) / 2 + dy:.1f}" '
                     f'text-anchor="middle">{fr(pb)}</text>')
            s.append(f'  <text class="valor" x="{cols[2] - 4}" y="{hy + 5:.1f}">{bola}</text>')
            if nivel < 3:
                continue
            prod = (pu[0] * pb[0], pu[1] * pb[1])
            cls = "valor" if bola == "Bl" else "rotulo"
            s.append(f'  <text class="{cls}" x="352" y="{hy + 5:.1f}">{fr(pu)} · {fr(pb)} = {fr(prod)} '
                     f'= {num(prod[0] / prod[1], 4)}</text>')
    s.append("</svg>")
    return "\n".join(s)


# ---------------------------------------------------------------- Ej. 3: normal de la glucosa

MU, SIGMA = 106, 8
X0, X1, CENTRO, PXS = 40, 580, 310, 75      # 75 px por cada desvío
BASE, PICO = 195, 50


def px(x):
    return CENTRO + (x - MU) / SIGMA * PXS


def py(x):
    return BASE - stats.norm.pdf((x - MU) / SIGMA) / stats.norm.pdf(0) * (BASE - PICO)


def trazo(a, b, pasos=120):
    xs = [a + (b - a) * i / pasos for i in range(pasos + 1)]
    return " ".join(f"L {px(x):.1f},{py(x):.1f}" for x in xs)


def x_de_px(p):
    return MU + (p - CENTRO) / PXS * SIGMA


def marcas(s, valores, y=217):
    for v in valores:
        s.append(f'  <text class="rotulo" x="{px(v):.1f}" y="{y}" text-anchor="middle">{num(v, 0) if v == int(v) else num(v)}</text>')


def ejes_glucosa(aria):
    s = [f'<svg viewBox="0 0 620 250" role="img" aria-label="{aria}">',
         f'  <line class="eje" x1="34" y1="{BASE}" x2="586" y2="{BASE}"/>']
    for k in range(-3, 4):
        x = px(MU + k * SIGMA)
        s.append(f'  <line class="eje" x1="{x:.1f}" y1="{BASE}" x2="{x:.1f}" y2="{BASE + 6}"/>')
    marcas(s, [MU + k * SIGMA for k in range(-3, 4)])
    return s


ALTURAS = [(0, "0,0499"), (1, "0,0302"), (2, "0,0067"), (3, "0,0006")]   # f(x) en z = 0, ±1, ±2, ±3


def puntos_glucosa(s, con_valores=True):
    for k, txt in ALTURAS:
        for signo in ((1,) if k == 0 else (-1, 1)):
            x = MU + signo * k * SIGMA
            s.append(f'  <circle class="punto" cx="{px(x):.1f}" cy="{py(x):.1f}" r="4"/>')
            if not con_valores:
                continue
            if k == 0:
                s.append(f'  <text class="valor" x="{px(x) + 9:.1f}" y="{py(x) - 2:.1f}" text-anchor="start">{txt}</text>')
            else:
                dx, ancla = (9, "start") if signo > 0 else (-9, "end")
                s.append(f'  <text class="valor" x="{px(x) + dx:.1f}" y="{py(x) - 8:.1f}" text-anchor="{ancla}">{txt}</text>')


def paso_glucosa_ejes():
    s = ejes_glucosa("Paso 2: el eje horizontal de la glucosa con 106 en el centro y marcas cada 8 (un desvío), "
                     "de 82 a 130")
    y = BASE - 20
    s += [f'  <line class="flecha" x1="{px(MU):.1f}" y1="{y}" x2="{px(MU + SIGMA):.1f}" y2="{y}"/>',
          f'  <line class="flecha" x1="{px(MU):.1f}" y1="{y - 5}" x2="{px(MU):.1f}" y2="{y + 5}"/>',
          f'  <line class="flecha" x1="{px(MU + SIGMA):.1f}" y1="{y - 5}" x2="{px(MU + SIGMA):.1f}" y2="{y + 5}"/>',
          f'  <text class="valor" x="{px(MU + SIGMA / 2):.1f}" y="{y - 9}" text-anchor="middle">8 = un desvío</text>',
          "</svg>"]
    return "\n".join(s)


def paso_glucosa_puntos():
    s = ejes_glucosa("Paso 3: los siete puntos de la tabla; el más alto en 106 (0,0499), en 98 y 114 a 0,0302, en 90 y "
                     "122 a 0,0067 y en 82 y 130 a 0,0006, casi sobre el eje; líneas punteadas desde cada marca")
    for k in range(-3, 4):
        x = MU + k * SIGMA
        s.append(f'  <line class="guia" x1="{px(x):.1f}" y1="{py(x):.1f}" x2="{px(x):.1f}" y2="{BASE}"/>')
    puntos_glucosa(s)
    s.append("</svg>")
    return "\n".join(s)


def paso_glucosa_campana():
    a, b = x_de_px(X0), x_de_px(X1)
    s = ejes_glucosa("Paso 4: la curva suave que une los siete puntos, una campana con el pico en 106, que a la "
                     "izquierda de 82 y a la derecha de 130 sigue pegada al eje sin tocarlo")
    s.insert(1, f'  <path class="campana" d="M {X0},{py(a):.1f} {trazo(a, b)}"/>')
    puntos_glucosa(s, con_valores=False)
    s += [f'  <text class="rotulo" x="47.5" y="{BASE - 10}" text-anchor="start">no toca el eje</text>',
          f'  <text class="rotulo" x="572.5" y="{BASE - 10}" text-anchor="end">no toca el eje</text>',
          "</svg>"]
    return "\n".join(s)


def normal_propiedades():
    a, b = x_de_px(X0), x_de_px(X1)
    s = ['<svg viewBox="0 0 620 250" role="img" aria-label="Campana normal de la glucosa con media 106 y desvío 8: '
         'pico en 106, simétrica, puntos de inflexión en 98 y 114, se acerca al eje sin tocarlo, área total 1">',
         f'  <path class="campana" d="M {X0},{py(a):.1f} {trazo(a, b)}"/>',
         f'  <line class="eje" x1="34" y1="{BASE}" x2="586" y2="{BASE}"/>',
         f'  <line class="guia" x1="{CENTRO}" y1="{py(MU):.1f}" x2="{CENTRO}" y2="25"/>']
    for x in (MU - SIGMA, MU + SIGMA):
        s.append(f'  <line class="guia" x1="{px(x):.1f}" y1="{py(x):.1f}" x2="{px(x):.1f}" y2="{BASE}"/>')
        s.append(f'  <circle class="punto" cx="{px(x):.1f}" cy="{py(x):.1f}" r="5"/>')
    s.append(f'  <circle class="punto" cx="{CENTRO}" cy="{py(MU):.1f}" r="5"/>')
    marcas(s, [MU + k * SIGMA for k in range(-3, 4)])
    yi = py(MU + SIGMA)
    s += [f'  <text class="rotulo" x="{CENTRO + 9}" y="{py(MU) - 4:.1f}" text-anchor="start">① máximo (moda) en 106</text>',
          f'  <text class="rotulo" x="{CENTRO}" y="19" text-anchor="middle">② eje de simetría x = 106</text>',
          f'  <text class="rotulo" x="{px(MU + SIGMA) + 9:.1f}" y="{yi - 4:.1f}" text-anchor="start">③ inflexión en 114</text>',
          f'  <text class="rotulo" x="{px(MU - SIGMA) - 9:.1f}" y="{yi - 4:.1f}" text-anchor="end">③ inflexión en 98</text>',
          f'  <text class="rotulo" x="{CENTRO}" y="{(yi + BASE) / 2 + 4:.1f}" text-anchor="middle">⑤ cóncava hacia abajo</text>',
          f'  <text class="rotulo" x="115" y="{BASE - 30:.1f}" text-anchor="middle">⑤ hacia arriba</text>',
          f'  <text class="rotulo" x="505" y="{BASE - 30:.1f}" text-anchor="middle">⑤ hacia arriba</text>',
          f'  <text class="rotulo" x="47.5" y="{BASE - 10}" text-anchor="start">④ se acerca al eje</text>',
          f'  <text class="rotulo" x="572.5" y="{BASE - 10}" text-anchor="end">sin tocarlo ④</text>',
          '  <text class="rotulo" x="310" y="243" text-anchor="middle">⑥ el área total encerrada vale 1 (0,5 de cada lado de 106)</text>',
          "</svg>"]
    return "\n".join(s)


def normal_cuartil():
    a, b = x_de_px(X0), x_de_px(X1)
    corte = MU + 0.67 * SIGMA
    s = ['<svg viewBox="0 0 620 250" role="img" aria-label="Campana normal de la glucosa: el 25 % más alto, '
         'sombreado, empieza en 111,36 (z = 0,67); a la izquierda queda el 75 %">',
         f'  <path class="area" d="M {px(corte):.1f},{BASE} L {px(corte):.1f},{py(corte):.1f} {trazo(corte, b, 60)} L {X1},{BASE} Z"/>',
         f'  <path class="campana" d="M {X0},{py(a):.1f} {trazo(a, b)}"/>',
         f'  <line class="eje" x1="34" y1="{BASE}" x2="586" y2="{BASE}"/>',
         f'  <line class="guia" x1="{CENTRO}" y1="{py(MU):.1f}" x2="{CENTRO}" y2="{BASE}"/>',
         f'  <line class="corte" x1="{px(corte):.1f}" y1="{py(corte):.1f}" x2="{px(corte):.1f}" y2="{BASE}"/>',
         f'  <text class="rotulo" x="{CENTRO}" y="217" text-anchor="middle">106</text>',
         f'  <text class="rotulo" x="{CENTRO}" y="236" text-anchor="middle">z = 0</text>',
         f'  <text class="valor" x="{px(corte) + 4:.1f}" y="217" text-anchor="start">x = 111,36</text>',
         f'  <text class="rotulo" x="{px(corte) + 4:.1f}" y="236" text-anchor="start">z = 0,67</text>',
         f'  <text class="valor" x="{px(corte) + 36:.1f}" y="{BASE - 22}" text-anchor="middle">25 %</text>',
         f'  <text class="rotulo" x="{CENTRO - 60}" y="{BASE - 40}" text-anchor="middle">75 %</text>',
         f'  <text class="rotulo" x="{px(corte):.1f}" y="30" text-anchor="middle">F(0,67) = 0,7486 ≈ 0,75</text>',
         "</svg>"]
    return "\n".join(s)


# ---------------------------------------------------------------- Ej. 4: prueba de hipótesis

def campana_z(nombre, critico, est, rango=4.0, etapa=3):
    """etapa 1: campana y centro; 2: más los cortes y las colas de rechazo; 3: más el estadístico."""
    base, pico, c = 205, 50, 310
    pdf = stats.norm.pdf
    esc = (base - pico) / pdf(0)
    zx = lambda z: c + z * (580 - c) / rango
    zy = lambda z: base - pdf(z) * esc
    pts = [(-rango + 2 * rango * i / 96) for i in range(97)]
    d = f"M 40,{base} " + " ".join(f"L {zx(z):.1f},{zy(z):.1f}" for z in pts) + f" L 580,{base} Z"
    clip = f"c-{nombre}"
    aria = {1: "Paso 1: la campana normal estándar Z, con el pico en 0 y una línea punteada en el centro",
            2: f"Paso 2: la campana Z con los cortes en ±{num(critico)} y las dos colas sombreadas, de área 0,025 "
               f"cada una: la región de rechazo",
            3: f"Campana normal estándar Z; región de rechazo en las dos colas desde ±{num(critico)}; el estadístico "
               f"z = {num(est)} marcado sobre el eje"}[etapa]
    s = [f'<svg viewBox="0 0 620 255" role="img" aria-label="{aria}">',
         f'  <defs><clipPath id="{clip}"><rect x="40" y="0" width="{zx(-critico) - 40:.1f}" height="{base}"/>'
         f'<rect x="{zx(critico):.1f}" y="0" width="{580 - zx(critico):.1f}" height="{base}"/></clipPath></defs>',
         f'  <path class="campana" d="{d}"/>',
         f'  <path class="area" clip-path="url(#{clip})" d="{d}"/>',
         f'  <line class="eje" x1="30" y1="{base}" x2="595" y2="{base}"/>',
         f'  <line class="guia" x1="{c}" y1="{pico}" x2="{c}" y2="{base}"/>',
         f'  <text class="rotulo" x="{c}" y="228" text-anchor="middle">0</text>']
    if etapa == 1:
        s = [l for l in s if "clip" not in l]     # sin colas sombreadas
        s.append("</svg>")
        return "\n".join(s)
    for v in (-critico, critico):
        x = zx(v)
        tx = x - 62 if v < 0 else x + 62
        s += [f'  <line class="corte" x1="{x:.1f}" y1="{zy(v):.1f}" x2="{x:.1f}" y2="{base}"/>',
              f'  <text class="rotulo" x="{x:.1f}" y="228" text-anchor="middle">{num(v)}</text>',
              f'  <text class="valor" x="{tx:.1f}" y="168" text-anchor="middle">rechazo</text>',
              f'  <text class="rotulo" x="{tx:.1f}" y="148" text-anchor="middle">área 0,025</text>']
    s.append(f'  <text class="rotulo" x="{c}" y="28" text-anchor="middle">zona de no rechazo de H₀</text>')
    if etapa == 2:
        s.append("</svg>")
        return "\n".join(s)
    s += [f'  <circle class="punto" cx="{zx(est):.1f}" cy="{base}" r="5"/>',
          f'  <text class="rotulo" x="{zx(est):.1f}" y="246" text-anchor="middle">z = {num(est)}</text>',
          "</svg>"]
    return "\n".join(s)


GRAFICOS = {
    "f1210-arbol-1": lambda: arbol(1),
    "f1210-arbol-2": lambda: arbol(2),
    "f1210-arbol": arbol,
    "f1210-c-ejes": paso_glucosa_ejes,
    "f1210-c-puntos": paso_glucosa_puntos,
    "f1210-c-campana": paso_glucosa_campana,
    "f1210-normal-prop": normal_propiedades,
    "f1210-normal-c": normal_cuartil,
    "f1210-ph-1": lambda: campana_z("f1210-ph-1", 1.96, -0.51, etapa=1),
    "f1210-ph-2": lambda: campana_z("f1210-ph-2", 1.96, -0.51, etapa=2),
    "f1210-ph": lambda: campana_z("f1210-ph", 1.96, -0.51),
}


def main():
    usados = set()
    for ruta in sorted(glob.glob(f"{CARPETA}/*.html")):
        texto = open(ruta, encoding="utf-8").read()
        nuevo = texto
        for nombre, fn in GRAFICOS.items():
            patron = re.compile(r'(<div class="pd-grafico" data-g="' + nombre + r'">\s*)<svg.*?</svg>', re.S)
            if patron.search(nuevo):
                usados.add(nombre)
            nuevo = patron.sub(lambda m: m.group(1) + fn(), nuevo)
        if nuevo != texto:
            open(ruta, "w", encoding="utf-8", newline="\n").write(nuevo)
            print("actualizado", ruta)
    for nombre in GRAFICOS:
        if nombre not in usados:
            print("sin usar:", nombre)


if __name__ == "__main__":
    main()
