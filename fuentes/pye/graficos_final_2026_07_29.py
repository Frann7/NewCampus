"""Gráficos del Final 29/07/2026 de PyE (app/contenido/pye/evaluacion/finales/2026-07-29-final/).

Ej. 1: la densidad triangular f(x) = (4 − x)/8, armada paso a paso (tabla → ejes → puntos →
recta → área), y las áreas del inciso d.
Rellena el <svg> que está dentro de cada <div class="pd-grafico" data-g="NOMBRE"> (el pie no se toca).
Uso, desde la raíz del repo:  python fuentes/pye/graficos_final_2026_07_29.py
"""
import glob
import re
from fractions import Fraction

CARPETA = "app/contenido/pye/evaluacion/finales/2026-07-29-final"


def num(v):
    s = f"{float(v):.4f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


# ---------------------------------------------------------------- Ej. 1: f(x) = (4 − x)/8

def f(x):
    return Fraction(4 - x, 8) if 0 <= x <= 4 else Fraction(0)


BASE, X0PX, PX_X, PX_Y = 205, 80, 100, 300     # 1 hora = 100 px; 0,1 de altura = 30 px


def px(x):
    return X0PX + PX_X * x


def py(y):
    return BASE - PX_Y * float(y)


TABLA = [0, 2, 4]


def ejes(aria, extra_alto=0):
    s = [f'<svg viewBox="0 0 620 {250 + extra_alto}" role="img" aria-label="{aria}" style="max-width:100%;height:auto">',
         f'  <line class="eje" x1="30" y1="{BASE}" x2="590" y2="{BASE}"/>',
         f'  <line class="eje" x1="{X0PX}" y1="30" x2="{X0PX}" y2="215"/>']
    for x in range(5):
        s.append(f'  <line class="eje" x1="{px(x)}" y1="{BASE}" x2="{px(x)}" y2="{BASE + 6}"/>')
        s.append(f'  <text class="rotulo" x="{px(x)}" y="228" text-anchor="middle">{x}</text>')
    for y in (Fraction(1, 4), Fraction(1, 2)):
        s.append(f'  <line class="eje" x1="{X0PX - 6}" y1="{py(y)}" x2="{X0PX}" y2="{py(y)}"/>')
        s.append(f'  <text class="rotulo" x="{X0PX - 10}" y="{py(y) + 4}" text-anchor="end">{num(y)}</text>')
    s.append(f'  <text class="rotulo" x="580" y="228" text-anchor="middle">x (h)</text>')
    s.append(f'  <text class="rotulo" x="{X0PX + 10}" y="38">f(x)</text>')
    return s


def puntos(con_rotulos=True):
    s = []
    for x in TABLA:
        y = f(x)
        s.append(f'  <circle class="punto" cx="{px(x)}" cy="{py(y)}" r="5"/>')
        if con_rotulos:
            # el de x = 0 va al costado: arriba esta el rotulo f(x) del eje
            dx, ancla, dy = {0: (12, "start", 5), 4: (0, "middle", -14)}.get(x, (12, "start", -10))
            s.append(f'  <text class="valor" x="{px(x) + dx}" y="{py(y) + dy}" text-anchor="{ancla}">'
                     f'({x} ; {num(y)})</text>')
    return s


def guias_del_medio():
    x, y = 2, f(2)
    return [f'  <line class="guia" x1="{X0PX}" y1="{py(y)}" x2="{px(x)}" y2="{py(y)}"/>',
            f'  <line class="guia" x1="{px(x)}" y1="{py(y)}" x2="{px(x)}" y2="{BASE}"/>']


def recta_y_afuera():
    return [f'  <line class="campana" x1="30" y1="{BASE}" x2="{px(0)}" y2="{BASE}"/>',
            f'  <line class="campana" x1="{px(0)}" y1="{py(f(0))}" x2="{px(4)}" y2="{py(f(4))}"/>',
            f'  <line class="campana" x1="{px(4)}" y1="{BASE}" x2="580" y2="{BASE}"/>']


def triangulo():
    return [f'  <path class="area suave" d="M {px(0)},{BASE} L {px(0)},{py(f(0))} L {px(4)},{BASE} Z"/>']


def paso_ejes():
    s = ejes("Paso 2: los ejes. Horizontal x en horas, marcado de 0 a 4; vertical f(x), marcado en 0,25 y 0,5")
    s.append("</svg>")
    return "\n".join(s)


def paso_puntos():
    s = ejes("Paso 3: los tres puntos de la tabla marcados, (0 ; 0,5), (2 ; 0,25) y (4 ; 0), con líneas "
             "punteadas que muestran cómo se ubica el del medio")
    s += guias_del_medio() + puntos()
    s.append("</svg>")
    return "\n".join(s)


def paso_recta():
    s = ejes("Paso 4: la recta que une los tres puntos, de (0 ; 0,5) a (4 ; 0), y la densidad en 0 "
             "sobre el eje a la izquierda de 0 y a la derecha de 4")
    s += recta_y_afuera() + puntos(con_rotulos=False)
    s += [f'  <text class="rotulo" x="55" y="{BASE - 10}" text-anchor="middle">f = 0</text>',
          f'  <text class="rotulo" x="530" y="{BASE - 10}" text-anchor="middle">f = 0</text>']
    s.append("</svg>")
    return "\n".join(s)


def grafico_final(aria="Densidad triangular que baja en línea recta desde 0,5 en x igual a 0 hasta 0 en "
                       "x igual a 4; el área debajo vale 1"):
    s = ejes(aria)
    s = s[:1] + triangulo() + s[1:]
    s += recta_y_afuera() + guias_del_medio() + puntos(con_rotulos=False)
    s.append(f'  <text class="valor" x="{px(1.2)}" y="180" text-anchor="middle">área = 1</text>')
    s.append("</svg>")
    return "\n".join(s)


def paso_area():
    s = ejes("Paso 5: el triángulo debajo de la recta sombreado, con la base de 0 a 4 y la altura 0,5 "
             "marcadas; su área vale 1")
    s = s[:1] + triangulo() + s[1:]
    s += recta_y_afuera() + puntos(con_rotulos=False)
    s += [f'  <line class="flecha" x1="{px(0)}" y1="{BASE + 36}" x2="{px(4)}" y2="{BASE + 36}"/>',
          f'  <line class="flecha" x1="{px(0)}" y1="{BASE + 31}" x2="{px(0)}" y2="{BASE + 41}"/>',
          f'  <line class="flecha" x1="{px(4)}" y1="{BASE + 31}" x2="{px(4)}" y2="{BASE + 41}"/>',
          f'  <text class="valor" x="{px(2)}" y="{BASE + 56}" text-anchor="middle">base = 4 (de 0 a 4)</text>',
          f'  <text class="valor" x="{px(0) + 14}" y="{py(f(0)) + 5}">altura = 0,5 (la de x = 0)</text>',
          f'  <text class="valor" x="{px(1.2)}" y="180" text-anchor="middle">área = 1</text>']
    s[0] = s[0].replace('viewBox="0 0 620 250"', 'viewBox="0 0 620 270"')
    s.append("</svg>")
    return "\n".join(s)


def areas_d():
    a, b = 1, 3
    s = ejes("Densidad triangular con el tramo de 0 a 1 sombreado fuerte, P(X ≤ 1) = 0,4375, y el de 1 a 3 "
             "sombreado suave, P(1 < X ≤ 3) = 0,5; las alturas en 1 y 3 son 0,375 y 0,125")
    zonas = [f'  <path class="area" d="M {px(0)},{BASE} L {px(0)},{py(f(0))} L {px(a)},{py(f(a))} L {px(a)},{BASE} Z"/>',
             f'  <path class="area suave" d="M {px(a)},{BASE} L {px(a)},{py(f(a))} L {px(b)},{py(f(b))} L {px(b)},{BASE} Z"/>']
    s = s[:1] + zonas + s[1:]
    s += recta_y_afuera()
    for x in (a, b):
        s += [f'  <line class="corte" x1="{px(x)}" y1="{py(f(x))}" x2="{px(x)}" y2="{BASE}"/>',
              f'  <circle class="punto" cx="{px(x)}" cy="{py(f(x))}" r="4"/>',
              f'  <text class="rotulo" x="{px(x) + 8}" y="{py(f(x)) - 8}">f({x}) = {num(f(x))}</text>']
    s += [f'  <text class="valor" x="{px(0.5)}" y="175" text-anchor="middle">0,4375</text>',
          f'  <text class="valor" x="{px(1.9)}" y="185" text-anchor="middle">0,5</text>',
          "</svg>"]
    return "\n".join(s)


GRAFICOS = {
    "f0729-ej1-b": grafico_final,
    "f0729-ej1-ejes": paso_ejes,
    "f0729-ej1-puntos": paso_puntos,
    "f0729-ej1-recta": paso_recta,
    "f0729-ej1-area": paso_area,
    "f0729-ej1-d": areas_d,
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
