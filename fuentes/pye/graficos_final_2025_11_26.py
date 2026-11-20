"""Gráficos del Final 26/11/2025 de PyE (app/contenido/pye/evaluacion/finales/2025-11-26-final/).

Ej. 2: la campana del colesterol, N(200; 30), armada paso a paso (eje → puntos → curva →
propiedades), y las áreas de los incisos b y c.
Ej. 3: diagrama de caja de las 15 baterías, paso a paso (eje → caja → bigotes → media), y la
campana t (14 grados de libertad) de la prueba.
Ej. 4: árbol de los traductores A, B y C con error (E) o sin error, por niveles.
Rellena cada <div class="pd-grafico" data-g="NOMBRE"> de esos archivos con el SVG calculado acá
(un mismo gráfico puede estar en Resultados y en la Explicación).
Uso, desde la raíz del repo:  python fuentes/pye/graficos_final_2025_11_26.py
"""
import glob
import os
import re
import sys

from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graficos_u1_practica import NO, arbol_dos_niveles  # noqa: E402
from graficos_u2 import caja  # noqa: E402
from graficos_u9_practica import campana  # noqa: E402

CARPETA = "app/contenido/pye/evaluacion/finales/2025-11-26-final"
MU, SIGMA = 200, 30
X0, X1, BASE, PICO = 40, 580, 195, 50
BATERIAS = [440, 452, 468, 480, 495, 505, 508, 511, 522, 530, 545, 550, 565, 575, 590]


def num(v, dec=2):
    t = f"{v:.{dec}f}".replace(".", ",")
    return t.rstrip("0").rstrip(",") if "," in t else t


# ---------------------------------------------------------------- ej. 2: la normal

def px(x):
    return X0 + (x - (MU - 3.6 * SIGMA)) / (7.2 * SIGMA) * (X1 - X0)


def py(x):
    pdf = stats.norm.pdf(x, MU, SIGMA)
    return BASE - pdf / stats.norm.pdf(MU, MU, SIGMA) * (BASE - PICO)


def trazo(a, b, pasos=120):
    xs = [a + (b - a) * i / pasos for i in range(pasos + 1)]
    return " ".join(f"L {px(x):.1f},{py(x):.1f}" for x in xs)


def curva():
    a, b = MU - 3.6 * SIGMA, MU + 3.6 * SIGMA
    return f'  <path class="campana" d="M {px(a):.1f},{py(a):.1f} {trazo(a, b)}"/>'


def marcas(valores, y=217):
    s = []
    for v in valores:
        s.append(f'  <line class="eje" x1="{px(v):.1f}" y1="{BASE - 4}" x2="{px(v):.1f}" y2="{BASE + 4}"/>')
        s.append(f'  <text class="rotulo" x="{px(v):.1f}" y="{y}" text-anchor="middle">{num(v)}</text>')
    return s


def normal_propiedades():
    i1, i2 = MU - SIGMA, MU + SIGMA
    s = ['<svg viewBox="0 0 620 255" role="img" aria-label="Campana normal del colesterol con media 200 y '
         'desvío 30: pico en 200, eje de simetría en 200, puntos de inflexión en 170 y 230, colas que se '
         'acercan al eje sin tocarlo y área total 1">',
         curva(),
         f'  <line class="eje" x1="34" y1="{BASE}" x2="586" y2="{BASE}"/>',
         f'  <line class="guia" x1="{px(MU):.1f}" y1="{PICO}" x2="{px(MU):.1f}" y2="25"/>',
         f'  <line class="guia" x1="{px(i1):.1f}" y1="{py(i1):.1f}" x2="{px(i1):.1f}" y2="{BASE}"/>',
         f'  <line class="guia" x1="{px(i2):.1f}" y1="{py(i2):.1f}" x2="{px(i2):.1f}" y2="{BASE}"/>',
         f'  <circle class="punto" cx="{px(MU):.1f}" cy="{PICO}" r="5"/>',
         f'  <circle class="punto" cx="{px(i1):.1f}" cy="{py(i1):.1f}" r="5"/>',
         f'  <circle class="punto" cx="{px(i2):.1f}" cy="{py(i2):.1f}" r="5"/>']
    s += marcas([MU + k * SIGMA for k in range(-3, 4)])
    s += [f'  <text class="rotulo" x="{px(MU) + 9:.1f}" y="{PICO - 4}" text-anchor="start">① moda: el pico está en 200</text>',
          f'  <text class="rotulo" x="{px(MU):.1f}" y="19" text-anchor="middle">② eje de simetría x = 200</text>',
          f'  <text class="rotulo" x="{px(i2) + 9:.1f}" y="{py(i2) - 4:.1f}" text-anchor="start">③ inflexión en 230</text>',
          f'  <text class="rotulo" x="{px(i1) - 9:.1f}" y="{py(i1) - 4:.1f}" text-anchor="end">③ inflexión en 170</text>',
          f'  <text class="rotulo" x="{px(MU):.1f}" y="{(PICO + BASE) / 2 + 30:.1f}" text-anchor="middle">⑤ cóncava hacia abajo</text>',
          f'  <text class="rotulo" x="{px(MU - 2.4 * SIGMA):.1f}" y="160" text-anchor="middle">⑤ hacia arriba</text>',
          f'  <text class="rotulo" x="{px(MU + 2.4 * SIGMA):.1f}" y="160" text-anchor="middle">⑤ hacia arriba</text>',
          f'  <text class="rotulo" x="{X0 + 6}" y="{BASE - 10}" text-anchor="start">④ se acerca al eje</text>',
          f'  <text class="rotulo" x="{X1 - 6}" y="{BASE - 10}" text-anchor="end">sin tocarlo ④</text>',
          '  <text class="rotulo" x="310" y="243" text-anchor="middle">⑥ el área total bajo la curva vale 1</text>',
          '</svg>']
    return "\n".join(s)


def normal_area(a, b, aria, rotulo_area, marcar, rotulo_z):
    """Sombrea el área entre a y b (a o b pueden ser los extremos del dibujo)."""
    izq, der = max(a, MU - 3.6 * SIGMA), min(b, MU + 3.6 * SIGMA)
    area = f'M {px(izq):.1f},{BASE} {trazo(izq, der, 80)} L {px(der):.1f},{BASE} Z'
    s = [f'<svg viewBox="0 0 620 255" role="img" aria-label="{aria}">',
         f'  <path class="area" d="{area}"/>',
         curva(),
         f'  <line class="eje" x1="34" y1="{BASE}" x2="586" y2="{BASE}"/>']
    for v in marcar:
        s.append(f'  <line class="corte" x1="{px(v):.1f}" y1="{py(v):.1f}" x2="{px(v):.1f}" y2="{BASE}"/>')
    s += marcas(marcar)
    for v, t in rotulo_z:
        s.append(f'  <text class="rotulo" x="{px(v):.1f}" y="238" text-anchor="middle">{t}</text>')
    xt, yt, t = rotulo_area
    s.append(f'  <text class="valor" x="{xt}" y="{yt}" text-anchor="middle">{t}</text>')
    s.append('</svg>')
    return "\n".join(s)


# los pasos del inciso d: eje → puntos → curva (el cuarto es normal_propiedades)

def altura(k):
    """Altura de la densidad a k desvíos de la media."""
    return stats.norm.pdf(MU + k * SIGMA, MU, SIGMA)


def eje_campana():
    return [f'  <line class="eje" x1="34" y1="{BASE}" x2="586" y2="{BASE}"/>'] + marcas([MU + k * SIGMA for k in range(-3, 4)])


def puntos_campana(con_rotulos):
    s = []
    for k in range(-3, 4):
        x = MU + k * SIGMA
        s.append(f'  <circle class="punto" cx="{px(x):.1f}" cy="{py(x):.1f}" r="5"/>')
        if con_rotulos:
            t = num(altura(k), 5 if abs(k) == 3 else 4)
            if k == 0:
                s.append(f'  <text class="valor" x="{px(x):.1f}" y="{PICO - 10}" text-anchor="middle">{t}</text>')
            elif abs(k) == 1:
                dx, anc = (-9, "end") if k < 0 else (9, "start")
                s.append(f'  <text class="valor" x="{px(x) + dx:.1f}" y="{py(x) - 4:.1f}" text-anchor="{anc}">{t}</text>')
            else:
                s.append(f'  <text class="valor" x="{px(x):.1f}" y="{py(x) - 12:.1f}" text-anchor="middle">{t}</text>')
    return s


def campana_ejes():
    s = ['<svg viewBox="0 0 620 255" role="img" aria-label="Paso 2: el eje horizontal del colesterol con las '
         'marcas de 30 en 30: 110, 140, 170, 200, 230, 260 y 290">']
    s += eje_campana() + ['</svg>']
    return "\n".join(s)


def campana_puntos():
    s = ['<svg viewBox="0 0 620 255" role="img" aria-label="Paso 3: los siete puntos de la tabla, cada uno arriba '
         'de su marca a su altura: 0,0133 en 200, 0,0081 en 170 y 230, 0,0018 en 140 y 260, 0,00015 en 110 y 290; '
         'líneas punteadas desde cada punto hasta el eje">']
    s += eje_campana()
    for k in range(-3, 4):
        x = MU + k * SIGMA
        s.append(f'  <line class="guia" x1="{px(x):.1f}" y1="{py(x):.1f}" x2="{px(x):.1f}" y2="{BASE}"/>')
    s += puntos_campana(True) + ['</svg>']
    return "\n".join(s)


def campana_curva():
    s = ['<svg viewBox="0 0 620 255" role="img" aria-label="Paso 4: la curva suave que pasa por los siete puntos, '
         'con el pico en 200 y las colas pegadas al eje más allá de 110 y 290">',
         curva()]
    s += eje_campana() + puntos_campana(False) + ['</svg>']
    return "\n".join(s)


def ej2_b():
    return normal_area(140, 260, "Campana del colesterol con el área entre 140 y 260 sombreada: 0,9544",
                       (310, 150, "0,9544"), [140, MU, 260], [(140, "z = −2"), (MU, "z = 0"), (260, "z = 2")])


def ej2_c():
    x = MU + 1.645 * SIGMA
    return normal_area(x, 1e9, "Campana del colesterol con la cola derecha de área 0,05 sombreada desde 249,35",
                       (round(px(x) + 62, 1), 165, "área 0,05"), [MU, x], [(MU, "z = 0"), (x, "z = 1,645")])


# ---------------------------------------------------------------- ej. 3 y ej. 4

def ej3_caja():
    return caja(BATERIAS, 420, 620, 20, "horas",
                aria="Diagrama de caja de las 15 duraciones: mínimo 440, Q1 = 480, mediana 511, Q3 = 550, "
                     "máximo 590; la media 515,73 marcada con una x; sin atípicos (vallas 375 y 655)")


# los pasos de la caja: eje → caja → bigotes (el cuarto, con la media, es ej3_caja)

CX0, CX1, CLO, CHI, YC, H = 50, 570, 420, 620, 105, 56
Q1, ME, Q3 = 480, 511, 550


def cx(v):
    return CX0 + (v - CLO) / (CHI - CLO) * (CX1 - CX0)


def eje_caja():
    s = [f'  <line class="eje" x1="{CX0}" y1="205" x2="{CX1}" y2="205"/>']
    for v in range(CLO, CHI + 1, 20):
        s.append(f'  <line class="eje" x1="{cx(v):.1f}" y1="200" x2="{cx(v):.1f}" y2="210"/>')
        s.append(f'  <text class="rotulo" x="{cx(v):.1f}" y="226" text-anchor="middle">{v}</text>')
    s.append(f'  <text class="rotulo" x="{CX1}" y="245" text-anchor="end">horas</text>')
    return s


def la_caja():
    a, w = cx(Q1), cx(Q3) - cx(Q1)
    return [f'  <rect class="area suave" x="{a:.1f}" y="{YC - H / 2}" width="{w:.1f}" height="{H}"/>',
            f'  <rect x="{a:.1f}" y="{YC - H / 2}" width="{w:.1f}" height="{H}" fill="none" stroke="currentColor" stroke-width="2"/>',
            f'  <line x1="{cx(ME):.1f}" y1="{YC - H / 2}" x2="{cx(ME):.1f}" y2="{YC + H / 2}" stroke="currentColor" stroke-width="3"/>',
            f'  <text class="rotulo" x="{cx(Q1) - 4:.1f}" y="{YC + H / 2 + 17}" text-anchor="end">Q1 = {Q1}</text>',
            f'  <text class="rotulo" x="{cx(Q3) + 4:.1f}" y="{YC + H / 2 + 17}" text-anchor="start">Q3 = {Q3}</text>',
            f'  <text class="rotulo" x="{cx(ME):.1f}" y="{YC - H / 2 - 6}" text-anchor="middle">Me = {ME}</text>']


def bigotes():
    mn, mx = BATERIAS[0], BATERIAS[-1]
    s = [f'  <line x1="{cx(mn):.1f}" y1="{YC}" x2="{cx(Q1):.1f}" y2="{YC}" stroke="currentColor" stroke-width="2"/>',
         f'  <line x1="{cx(Q3):.1f}" y1="{YC}" x2="{cx(mx):.1f}" y2="{YC}" stroke="currentColor" stroke-width="2"/>']
    for v in (mn, mx):
        s.append(f'  <line x1="{cx(v):.1f}" y1="{YC - 14}" x2="{cx(v):.1f}" y2="{YC + 14}" stroke="currentColor" stroke-width="2"/>')
        s.append(f'  <text class="rotulo" x="{cx(v):.1f}" y="{YC - 20}" text-anchor="middle">{v}</text>')
    return s


def caja_eje():
    s = ['<svg viewBox="0 0 620 250" role="img" aria-label="Paso 2: el eje de las horas, de 420 a 620 marcado de 20 en 20">']
    s += eje_caja() + ['</svg>']
    return "\n".join(s)


def caja_caja():
    s = ['<svg viewBox="0 0 620 250" role="img" aria-label="Paso 3: la caja de Q1 = 480 a Q3 = 550 con la raya de la '
         'mediana en 511; líneas punteadas desde los tres hasta el eje">']
    s += la_caja()
    for v in (Q1, ME, Q3):
        s.append(f'  <line class="guia" x1="{cx(v):.1f}" y1="{YC + H / 2}" x2="{cx(v):.1f}" y2="205"/>')
    s += eje_caja() + ['</svg>']
    return "\n".join(s)


def caja_bigotes():
    s = ['<svg viewBox="0 0 620 250" role="img" aria-label="Paso 4: los bigotes, de 440 hasta la caja y de la caja '
         'hasta 590; líneas punteadas desde sus puntas hasta el eje">']
    s += la_caja() + bigotes()
    for v in (BATERIAS[0], BATERIAS[-1]):
        s.append(f'  <line class="guia" x1="{cx(v):.1f}" y1="{YC + 14}" x2="{cx(v):.1f}" y2="205"/>')
    s += eje_caja() + ['</svg>']
    return "\n".join(s)


def ej3_t():
    return campana("f1126-ej3-t", "t", 14, "dos", 2.145, -0.3714, 0.05, "t", dec_est=4)


TRAD = [("A", 0.25, 0.10), ("B", 0.35, 0.05), ("C", 0.40, 0.01)]


def ej4_arbol():
    return arbol_dos_niveles("Árbol: traductor A (0,25), B (0,35) o C (0,40) y si la página tiene error (E) "
                             "o no; resaltadas las tres ramas con error", TRAD, "E", "E" + NO,
                             marcar={(t, "E") for t, _, _ in TRAD})


def ej4_nivel(nivel, aria):
    """El árbol a medio armar: nivel 1 = solo los traductores; nivel 2 = también error o no (sin las puntas)."""
    lineas = ej4_arbol().split("\n")
    s = [re.sub(r'aria-label="[^"]*"', f'aria-label="{aria}"', lineas[0])]
    for l in lineas[1:-1]:
        punta = 'x="357"' in l
        nivel1 = ('class="punto"' in l or 'x1="36"' in l or 'x="110.0"' in l or 'x="190"' in l)
        if (nivel == 1 and nivel1) or (nivel == 2 and not punta):
            s.append(l)
    s.append("</svg>")
    return "\n".join(s)


GRAFICOS = {
    "f1126-ej2-prop": normal_propiedades,
    "f1126-ej2-ejes": campana_ejes,
    "f1126-ej2-puntos": campana_puntos,
    "f1126-ej2-curva": campana_curva,
    "f1126-ej2-b": ej2_b,
    "f1126-ej2-c": ej2_c,
    "f1126-ej3-caja": ej3_caja,
    "f1126-ej3-caja-eje": caja_eje,
    "f1126-ej3-caja-caja": caja_caja,
    "f1126-ej3-caja-bigotes": caja_bigotes,
    "f1126-ej3-t": ej3_t,
    "f1126-ej4-arbol": ej4_arbol,
    "f1126-ej4-nivel1": lambda: ej4_nivel(1, "Paso 1: el primer nivel del árbol, el traductor: A con 0,25, "
                                             "B con 0,35 y C con 0,40"),
    "f1126-ej4-nivel2": lambda: ej4_nivel(2, "Paso 2: el segundo nivel, de cada traductor sale error (E) o sin "
                                             "error: A 0,1 y 0,9; B 0,05 y 0,95; C 0,01 y 0,99"),
}


def main():
    usados = set()
    for ruta in sorted(glob.glob(f"{CARPETA}/*.html")):
        texto = open(ruta, encoding="utf-8").read()
        nuevo = texto
        for nombre, fn in GRAFICOS.items():
            patron = re.compile(r'(<div class="pd-grafico" data-g="' + nombre + r'">)\s*(?:<svg.*?</svg>\s*)?', re.S)
            if patron.search(nuevo):
                usados.add(nombre)
                svg = fn()
                nuevo = patron.sub(lambda m: m.group(1) + "\n" + svg + "\n    ", nuevo)
        if nuevo != texto:
            open(ruta, "w", encoding="utf-8", newline="\n").write(nuevo)
            print("actualizado", ruta)
    print("sin usar:", sorted(set(GRAFICOS) - usados))


if __name__ == "__main__":
    main()
