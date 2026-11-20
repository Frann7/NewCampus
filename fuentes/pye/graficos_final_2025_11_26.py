"""Gráficos del Final 26/11/2025 de PyE (app/contenido/pye/evaluacion/finales/2025-11-26-final/).

Ej. 2: la campana del colesterol, N(200; 30), con sus propiedades y las áreas de los incisos b y c.
Ej. 3: diagrama de caja de las 15 baterías y la campana t (14 grados de libertad) de la prueba.
Ej. 4: árbol de los traductores A, B y C con error (E) o sin error.
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


def ej3_t():
    return campana("f1126-ej3-t", "t", 14, "dos", 2.145, -0.3714, 0.05, "t", dec_est=4)


TRAD = [("A", 0.25, 0.10), ("B", 0.35, 0.05), ("C", 0.40, 0.01)]


def ej4_arbol():
    return arbol_dos_niveles("Árbol: traductor A (0,25), B (0,35) o C (0,40) y si la página tiene error (E) "
                             "o no; resaltadas las tres ramas con error", TRAD, "E", "E" + NO,
                             marcar={(t, "E") for t, _, _ in TRAD})


GRAFICOS = {
    "f1126-ej2-prop": normal_propiedades,
    "f1126-ej2-b": ej2_b,
    "f1126-ej2-c": ej2_c,
    "f1126-ej3-caja": ej3_caja,
    "f1126-ej3-t": ej3_t,
    "f1126-ej4-arbol": ej4_arbol,
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
