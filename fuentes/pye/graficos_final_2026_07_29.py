"""Gráficos del Final 29/07/2026 de PyE (app/contenido/pye/evaluacion/finales/2026-07-29-final/).

Ej. 1: la densidad triangular f(x) = (4 − x)/8, armada paso a paso (tabla → ejes → puntos →
recta → área), y las áreas del inciso d.
Ej. 2: la campana N(355; 4) armada paso a paso (eje → campana → cortes → área) y las de b, c y e.
Ej. 3: el diagrama de caja del consumo, paso a paso (eje → caja → vallas y bigotes → atípico).
Ej. 4: el árbol del filtro antispam, nivel por nivel.
Rellena el <svg> que está dentro de cada <div class="pd-grafico" data-g="NOMBRE"> (el pie no se toca).
Uso, desde la raíz del repo:  python fuentes/pye/graficos_final_2026_07_29.py
"""
import glob
import re
from fractions import Fraction

from scipy import stats

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


# ---------------------------------------------------------------- Ej. 2: X ~ N(355; 4)

MU2, SIG2 = 355, 4
C2, PXS2, BASE2, PICO2 = 310, 67.5, 205, 50     # 67,5 px por desvío: de 339 (40 px) a 371 (580 px)
FILA_X, FILA_Z = 224, 242                       # renglones de los rótulos: x arriba, z abajo


def coma(v, dec=2):
    s = f"{v:.{dec}f}".replace(".", ",").replace("-", "−")
    return s


def x2(x):
    return C2 + (x - MU2) / SIG2 * PXS2


def y2(x):
    return BASE2 - stats.norm.pdf((x - MU2) / SIG2) / stats.norm.pdf(0) * (BASE2 - PICO2)


def trazo2(a, b, pasos=120):
    xs = [a + (b - a) * i / pasos for i in range(pasos + 1)]
    return " ".join(f"L {x2(x):.1f},{y2(x):.1f}" for x in xs)


def curva2():
    a, b = MU2 - 4 * SIG2, MU2 + 4 * SIG2
    return f'  <path class="campana" d="M {x2(a):.1f},{y2(a):.1f} {trazo2(a, b)}"/>'


def area2(a, b, clase="area"):
    return (f'  <path class="{clase}" d="M {x2(a):.1f},{BASE2} L {x2(a):.1f},{y2(a):.1f} '
            f'{trazo2(a, b, 80)} L {x2(b):.1f},{BASE2} Z"/>')


def eje2(con_numeros):
    """Eje horizontal con una rayita en cada desvío (343 a 367); con_numeros escribe x y z de cada una."""
    s = [f'  <line class="eje" x1="30" y1="{BASE2}" x2="595" y2="{BASE2}"/>']
    for k in range(-3, 4):
        x = MU2 + k * SIG2
        s.append(f'  <line class="eje" x1="{x2(x):.1f}" y1="{BASE2}" x2="{x2(x):.1f}" y2="{BASE2 + 6}"/>')
        if con_numeros:
            s.append(f'  <text class="rotulo" x="{x2(x):.1f}" y="{FILA_X}" text-anchor="middle">{x}</text>')
            s.append(f'  <text class="rotulo" x="{x2(x):.1f}" y="{FILA_Z}" text-anchor="middle">{coma(k, 0)}</text>')
    if con_numeros:
        s += [f'  <text class="rotulo" x="62" y="{FILA_X}" text-anchor="middle">x (ml)</text>',
              f'  <text class="rotulo" x="62" y="{FILA_Z}" text-anchor="middle">z</text>']
    return s


def guia_mu2():
    return f'  <line class="guia" x1="{C2}" y1="{PICO2}" x2="{C2}" y2="{BASE2}"/>'


def corte2(x, txt_x, txt_z):
    return [f'  <line class="corte" x1="{x2(x):.1f}" y1="{y2(x):.1f}" x2="{x2(x):.1f}" y2="{BASE2}"/>',
            f'  <text class="rotulo" x="{x2(x):.1f}" y="{FILA_X}" text-anchor="middle">{txt_x}</text>',
            f'  <text class="rotulo" x="{x2(x):.1f}" y="{FILA_Z}" text-anchor="middle">{txt_z}</text>']


def media2():
    return [f'  <text class="rotulo" x="{C2}" y="{FILA_X}" text-anchor="middle">μ = 355</text>',
            f'  <text class="rotulo" x="{C2}" y="{FILA_Z}" text-anchor="middle">z = 0</text>']


def svg2(aria, cuerpo):
    return "\n".join([f'<svg viewBox="0 0 620 250" role="img" aria-label="{aria}" style="max-width:100%;height:auto">']
                     + cuerpo + ["</svg>"])


def ej2_ejes():
    return svg2("Paso 1: el eje horizontal con una marca en cada desvío: 343, 347, 351, 355, 359, 363 y 367 ml, "
                "y debajo su z: de −3 a 3", eje2(True))


def ej2_campana():
    s = [curva2()] + eje2(True) + [guia_mu2()]
    for x in (MU2 - SIG2, MU2, MU2 + SIG2):
        s.append(f'  <circle class="punto" cx="{x2(x):.1f}" cy="{y2(x):.1f}" r="5"/>')
    yi = y2(MU2 + SIG2)
    s += [f'  <text class="rotulo" x="{C2 + 10}" y="{PICO2 - 2}" text-anchor="start">máximo en 355</text>',
          f'  <text class="rotulo" x="{x2(MU2 + SIG2) + 10:.1f}" y="{yi - 6:.1f}" text-anchor="start">inflexión en 359</text>',
          f'  <text class="rotulo" x="{x2(MU2 - SIG2) - 10:.1f}" y="{yi - 6:.1f}" text-anchor="end">inflexión en 351</text>']
    return svg2("Paso 2: la campana, con el máximo en 355, los puntos de inflexión en 351 y 359 y la línea "
                "punteada de simetría en 355; en 343 y 367 ya casi toca el eje", s)


def ej2_cortes():
    s = [curva2()] + eje2(False) + [guia_mu2()] + media2()
    s += corte2(350, "350", "z = −1,25") + corte2(360, "360", "z = 1,25")
    return svg2("Paso 3: la campana con dos líneas verticales en 350 (z = −1,25) y en 360 (z = 1,25)", s)


def ej2_a(con_colas=False):
    s = [area2(350, 360), curva2()] + eje2(False) + [guia_mu2()] + media2()
    s += corte2(350, "350", "z = −1,25") + corte2(360, "360", "z = 1,25")
    s.append(f'  <text class="valor" x="{C2}" y="160" text-anchor="middle">0,7888</text>')
    if con_colas:
        s += ['  <text class="rotulo" x="150" y="178" text-anchor="middle">0,1056</text>',
              '  <text class="rotulo" x="470" y="178" text-anchor="middle">0,1056</text>']
        aria = ("Paso 4: el tramo entre 350 y 360 sombreado, con área 0,7888; en cada cola, afuera del tramo, "
                "queda 0,1056")
    else:
        aria = "Campana normal con el tramo entre 350 y 360 ml sombreado: área 0,7888"
    return svg2(aria, s)


def ej2_b():
    s = [area2(MU2 - 4 * SIG2, 348), curva2()] + eje2(False) + [guia_mu2()] + media2()
    s += corte2(348, "348", "z = −1,75")
    s.append('  <text class="valor" x="140" y="178" text-anchor="middle">0,0401</text>')
    return svg2("Campana normal con la cola izquierda sombreada por debajo de 348 ml (z = −1,75): área 0,0401", s)


def ej2_c():
    s = [area2(363.2, MU2 + 4 * SIG2), curva2()] + eje2(False) + [guia_mu2()] + media2()
    s += corte2(363.2, "363,2", "z = 2,05")
    s += ['  <text class="valor" x="250" y="170" text-anchor="middle">0,98</text>',
          '  <text class="valor" x="520" y="180" text-anchor="middle">0,02</text>']
    return svg2("Campana normal con el corte en 363,2 ml (z = 2,05): a la izquierda queda 0,98 y la cola derecha "
                "sombreada, 0,02, son las sobrellenadas", s)


def ej2_e():
    zx = lambda z: C2 + z * PXS2
    zy = lambda z: BASE2 - stats.norm.pdf(z) / stats.norm.pdf(0) * (BASE2 - PICO2)
    zs = [-4 + 8 * i / 160 for i in range(161)]
    curva = f'  <path class="campana" d="M 40,{zy(-4):.1f} ' + " ".join(f"L {zx(z):.1f},{zy(z):.1f}" for z in zs) + '"/>'
    zc = -1.645
    cola = [-4 + (zc + 4) * i / 80 for i in range(81)]
    area = (f'  <path class="area" d="M 40,{BASE2} ' + " ".join(f"L {zx(z):.1f},{zy(z):.1f}" for z in cola)
            + f' L {zx(zc):.1f},{BASE2} Z"/>')
    s = [area, curva,
         f'  <line class="eje" x1="30" y1="{BASE2}" x2="595" y2="{BASE2}"/>',
         guia_mu2(),
         f'  <text class="rotulo" x="{C2}" y="{FILA_X}" text-anchor="middle">0</text>',
         f'  <line class="corte" x1="{zx(zc):.1f}" y1="{zy(zc):.1f}" x2="{zx(zc):.1f}" y2="{BASE2}"/>',
         f'  <text class="rotulo" x="{zx(zc):.1f}" y="{FILA_X}" text-anchor="middle">−1,645</text>',
         f'  <circle class="punto" cx="{zx(-2.25):.1f}" cy="{BASE2}" r="5"/>',
         f'  <text class="rotulo" x="{zx(-2.25):.1f}" y="{FILA_Z}" text-anchor="middle">z = −2,25</text>',
         '  <text class="valor" x="110" y="148" text-anchor="middle">rechazo</text>',
         '  <text class="valor" x="110" y="168" text-anchor="middle">α = 0,05</text>']
    return svg2("Campana normal estándar con la región de rechazo a la izquierda de −1,645 (área 0,05) y el "
                "estadístico z = −2,25 marcado adentro", s)


# ---------------------------------------------------------------- Ej. 3: diagrama de caja

DATOS3 = [2.1, 2.5, 2.8, 3.0, 3.2, 3.4, 3.5, 3.6, 3.8, 3.9, 4.0, 4.1, 4.3, 4.5, 4.7, 5.0, 5.3, 5.8, 6.5, 9.8]
Q1_3, ME_3, Q3_3 = 3.30, 3.95, 4.85
MEDIA_3 = sum(DATOS3) / len(DATOS3)                       # 4,29
VI_3, VS_3 = Q1_3 - 1.5 * (Q3_3 - Q1_3), Q3_3 + 1.5 * (Q3_3 - Q1_3)   # 0,975 y 7,175
X0_3, PX_3, YC_3, H_3, YE_3 = 50, 52, 110, 56, 200     # 1 GB = 52 px, de 0 a 10


def gx(v):
    return X0_3 + PX_3 * v


def c3(v):
    return f"{v:.6g}".replace(".", ",")


def eje3():
    s = [f'  <line class="eje" x1="{X0_3 - 10}" y1="{YE_3}" x2="{gx(10) + 10}" y2="{YE_3}"/>']
    for v in range(11):
        s += [f'  <line class="eje" x1="{gx(v)}" y1="{YE_3 - 5}" x2="{gx(v)}" y2="{YE_3 + 5}"/>',
              f'  <text class="rotulo" x="{gx(v)}" y="{YE_3 + 20}" text-anchor="middle">{v}</text>']
    s.append(f'  <text class="rotulo" x="{gx(10) + 10}" y="{YE_3 + 40}" text-anchor="end">GB</text>')
    return s


def cruz3(v, y):
    x = gx(v)
    return [f'  <line class="corte" x1="{x - 6:.1f}" y1="{y - 6}" x2="{x + 6:.1f}" y2="{y + 6}"/>',
            f'  <line class="corte" x1="{x + 6:.1f}" y1="{y - 6}" x2="{x - 6:.1f}" y2="{y + 6}"/>']


def caja3():
    top, bot = YC_3 - H_3 / 2, YC_3 + H_3 / 2
    s = [f'  <rect class="area suave" x="{gx(Q1_3):.1f}" y="{top}" width="{gx(Q3_3) - gx(Q1_3):.1f}" height="{H_3}"/>',
         f'  <rect x="{gx(Q1_3):.1f}" y="{top}" width="{gx(Q3_3) - gx(Q1_3):.1f}" height="{H_3}" fill="none" stroke="currentColor" stroke-width="2"/>',
         f'  <line x1="{gx(ME_3):.1f}" y1="{top}" x2="{gx(ME_3):.1f}" y2="{bot}" stroke="currentColor" stroke-width="3"/>']
    s += cruz3(MEDIA_3, YC_3)
    s += [f'  <text class="rotulo" x="{gx(ME_3):.1f}" y="{top - 6}" text-anchor="middle">Me = 3,95</text>',
          f'  <text class="rotulo" x="{gx(Q1_3) - 4:.1f}" y="{bot + 17}" text-anchor="end">Q1 = 3,3</text>',
          f'  <text class="rotulo" x="{gx(Q3_3) + 4:.1f}" y="{bot + 17}" text-anchor="start">Q3 = 4,85</text>',
          f'  <text class="rotulo" x="{gx(MEDIA_3):.1f}" y="{bot + 34}" text-anchor="middle">x̄ = 4,29</text>']
    return s


def bigotes3():
    s = []
    for v in (VI_3, VS_3):
        s += [f'  <line class="guia" x1="{gx(v):.1f}" y1="{YC_3 - 62}" x2="{gx(v):.1f}" y2="{YC_3 + 62}"/>',
              f'  <text class="rotulo" x="{gx(v):.1f}" y="{YC_3 - 68}" text-anchor="middle">valla {c3(v)}</text>']
    for a, b in ((2.1, Q1_3), (Q3_3, 6.5)):
        s.append(f'  <line x1="{gx(a):.1f}" y1="{YC_3}" x2="{gx(b):.1f}" y2="{YC_3}" stroke="currentColor" stroke-width="2"/>')
    for v in (2.1, 6.5):
        s += [f'  <line x1="{gx(v):.1f}" y1="{YC_3 - 14}" x2="{gx(v):.1f}" y2="{YC_3 + 14}" stroke="currentColor" stroke-width="2"/>',
              f'  <text class="rotulo" x="{gx(v):.1f}" y="{YC_3 - 20}" text-anchor="middle">{c3(v)}</text>']
    return s


def svg3(aria, cuerpo):
    return "\n".join([f'<svg viewBox="0 0 620 250" role="img" aria-label="{aria}" style="max-width:100%;height:auto">']
                     + cuerpo + ["</svg>"])


def ej3_eje():
    return svg3("Paso 2: el eje horizontal del consumo, de 0 a 10 GB, marcado de a 1", eje3())


def ej3_caja():
    return svg3("Paso 3: la caja de Q1 = 3,3 a Q3 = 4,85, con una raya en la mediana 3,95 y una cruz en la "
                "media 4,29", caja3() + eje3())


def ej3_bigotes():
    return svg3("Paso 4: las vallas punteadas en 0,975 y 7,175 y los bigotes desde la caja hasta 2,1 y 6,5, "
                "el último dato de cada lado que queda dentro de las vallas", bigotes3() + caja3() + eje3())


def ej3_final():
    s = bigotes3() + caja3() + cruz3(9.8, YC_3)
    s.append(f'  <text class="valor" x="{gx(9.8):.1f}" y="{YC_3 + 30}" text-anchor="middle">9,8</text>')
    return svg3("Diagrama de caja del consumo: caja de 3,3 a 4,85 con mediana 3,95 y media 4,29, bigotes hasta "
                "2,1 y 6,5, vallas en 0,975 y 7,175 y el atípico 9,8 marcado suelto con una cruz", s + eje3())


# ---------------------------------------------------------------- Ej. 4: árbol del filtro antispam

def arbol4(niveles):
    """niveles = 1 (qué es el correo), 2 (+ qué dice el filtro) o 3 (+ el producto de cada camino)."""
    ramas = [("S", "0,20", [("C", "0,95", "P(S∩C) = 0,20 · 0,95 = 0,19"),
                            ("C'", "0,05", "P(S∩C') = 0,20 · 0,05 = 0,01")]),
             ("S'", "0,80", [("C", "0,03", "P(S'∩C) = 0,80 · 0,03 = 0,024"),
                             ("C'", "0,97", "P(S'∩C') = 0,80 · 0,97 = 0,776")])]
    cols, x_prod = [30, 190, 350], 392
    hojas_y = [56 + 46 * i for i in range(4)]
    nodos_y = [(hojas_y[0] + hojas_y[1]) / 2, (hojas_y[2] + hojas_y[3]) / 2]
    raiz_y = sum(nodos_y) / 2
    s = [f'  <text class="rotulo" x="{cols[1]}" y="18" text-anchor="middle">Correo</text>']
    if niveles >= 2:
        s.append(f'  <text class="rotulo" x="{cols[2]}" y="18" text-anchor="middle">Filtro</text>')
    if niveles >= 3:
        s.append(f'  <text class="rotulo" x="{x_prod}" y="18" text-anchor="start">Producto de las ramas</text>')
    s.append(f'  <circle class="punto" cx="{cols[0]}" cy="{raiz_y:.1f}" r="4"/>')
    for i, (ev, p, hijos) in enumerate(ramas):
        ny = nodos_y[i]
        a, b = cols[0] + 4, cols[1] - 16
        dy = -8 if ny < raiz_y else 18
        s += [f'  <line class="eje" x1="{a}" y1="{raiz_y:.1f}" x2="{b}" y2="{ny:.1f}"/>',
              f'  <text class="rotulo" x="{(a + b) / 2:.1f}" y="{(raiz_y + ny) / 2 + dy:.1f}" text-anchor="middle">{p}</text>',
              f'  <text class="valor" x="{cols[1] - 6}" y="{ny + 5:.1f}">{ev}</text>']
        if niveles < 2:
            continue
        for j, (ev2, p2, prod) in enumerate(hijos):
            hy = hojas_y[2 * i + j]
            a, b = cols[1] + 14, cols[2] - 16
            dy = -6 if hy < ny else 16
            s += [f'  <line class="eje" x1="{a}" y1="{ny:.1f}" x2="{b}" y2="{hy:.1f}"/>',
                  f'  <text class="rotulo" x="{(a + b) / 2:.1f}" y="{(ny + hy) / 2 + dy:.1f}" text-anchor="middle">{p2}</text>',
                  f'  <text class="valor" x="{cols[2] - 6}" y="{hy + 5:.1f}">{ev2}</text>']
            if niveles >= 3:
                s.append(f'  <text class="rotulo" x="{x_prod}" y="{hy + 5:.1f}">{prod}</text>')
    if niveles >= 3:
        s.append(f'  <text class="rotulo" x="{x_prod}" y="{hojas_y[-1] + 34:.1f}">suma: 0,19 + 0,01 + 0,024 + 0,776 = 1</text>')
    alto = 250 if niveles >= 3 else 230
    arias = {1: "Paso 1: el primer nivel del árbol: spam S con 0,20 y legítimo S' con 0,80",
             2: "Paso 2: el árbol con el segundo nivel: de S salen C con 0,95 y C' con 0,05; de S' salen C con "
                "0,03 y C' con 0,97",
             3: "Árbol de probabilidades: spam 0,20 y legítimo 0,80; de spam salen clasificado spam 0,95 y no "
                "spam 0,05; de legítimo, clasificado spam 0,03 y no spam 0,97; a la derecha, el producto de cada "
                "camino: 0,19; 0,01; 0,024 y 0,776, que suman 1"}
    return "\n".join([f'<svg viewBox="0 0 620 {alto}" role="img" aria-label="{arias[niveles]}" '
                      f'style="max-width:100%;height:auto">'] + s + ["</svg>"])


GRAFICOS = {
    "f0729-ej1-b": grafico_final,
    "f0729-ej1-ejes": paso_ejes,
    "f0729-ej1-puntos": paso_puntos,
    "f0729-ej1-recta": paso_recta,
    "f0729-ej1-area": paso_area,
    "f0729-ej1-d": areas_d,
    "f0729-ej2-a": ej2_a,
    "f0729-ej2-ejes": ej2_ejes,
    "f0729-ej2-campana": ej2_campana,
    "f0729-ej2-cortes": ej2_cortes,
    "f0729-ej2-area": lambda: ej2_a(con_colas=True),
    "f0729-ej2-b": ej2_b,
    "f0729-ej2-c": ej2_c,
    "f0729-ej2-e": ej2_e,
    "f0729-ej3-eje": ej3_eje,
    "f0729-ej3-caja": ej3_caja,
    "f0729-ej3-bigotes": ej3_bigotes,
    "f0729-ej3-final": ej3_final,
    "f0729-ej4-n1": lambda: arbol4(1),
    "f0729-ej4-n2": lambda: arbol4(2),
    "f0729-ej4-arbol": lambda: arbol4(3),
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
