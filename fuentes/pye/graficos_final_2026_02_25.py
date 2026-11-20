"""Gráficos del Final 25/02/2026 de PyE (app/contenido/pye/evaluacion/finales/2026-02-25-final/).

Ej. 2: bastones de f(x) y escalera de F(x), armados paso a paso (ejes → bastones; ejes → tramos →
puntos). Ej. 3: la campana N(200; 25) armada paso a paso (escala → campana → corte del inciso a), la
cola del 20 % (inciso b) y las dos campanas con σ = 25 y σ = 35 (inciso c). Ej. 4: la campana Z de
la prueba de hipótesis, paso a paso (campana → región de rechazo → z calculado).
Rellena el <svg> que está dentro de cada <div class="pd-grafico" data-g="NOMBRE"> (el pie no se toca).
Uso, desde la raíz del repo:  python fuentes/pye/graficos_final_2026_02_25.py
"""
import glob
import math
import re

CARPETA = "app/contenido/pye/evaluacion/finales/2026-02-25-final"


def num(v, dec=2):
    return f"{v:.{dec}f}".replace(".", ",").replace("-", "−")


def abrir(alto, aria):
    return [f'<svg viewBox="0 0 620 {alto}" role="img" aria-label="{aria}">']


# ---------------------------------------------------------------- Ej. 2: f(x) y F(x)

F_X = [0.05, 0.15, 0.25, 0.35, 0.15, 0.05]
ACUM = [round(sum(F_X[:i + 1]), 2) for i in range(6)]      # 0,05 0,20 0,45 0,80 0,95 1
B2 = 215                                                   # base de los dos gráficos


def bx(x):          # bastones: x = 0 en 100 px, 90 px por unidad
    return 100 + 90 * x


def by(p):          # bastones: 0,1 de altura = 45 px
    return B2 - 450 * p


def ejes_f(aria):
    s = abrir(260, aria)
    s += [f'  <line class="eje" x1="50" y1="{B2}" x2="590" y2="{B2}"/>',
          f'  <line class="eje" x1="50" y1="{B2}" x2="50" y2="30"/>']
    for p in (0.1, 0.2, 0.3):
        s += [f'  <line class="guia" x1="50" y1="{by(p):g}" x2="580" y2="{by(p):g}"/>',
              f'  <text class="rotulo" x="42" y="{by(p) + 4:g}" text-anchor="end">{num(p, 1)}</text>']
    s.append('  <text class="rotulo" x="42" y="36" text-anchor="end">f(x)</text>')
    for x in range(6):
        s += [f'  <line class="eje" x1="{bx(x)}" y1="{B2}" x2="{bx(x)}" y2="{B2 + 6}"/>',
              f'  <text class="rotulo" x="{bx(x)}" y="236" text-anchor="middle">{x}</text>']
    s.append('  <text class="rotulo" x="600" y="236" text-anchor="middle">x</text>')
    return s


def f_ejes():
    s = ejes_f("Paso 2: los ejes del gráfico de f(x). Horizontal x de 0 a 5; vertical f(x) marcado en 0,1, "
               "0,2 y 0,3, con líneas punteadas para leer la altura")
    s.append("</svg>")
    return "\n".join(s)


def f_bastones():
    s = ejes_f("Gráfico de bastones de f(x): alturas 0,05; 0,15; 0,25; 0,35; 0,15; 0,05 en x de 0 a 5")
    for x, p in enumerate(F_X):
        s.append(f'  <line class="corte" style="stroke-width:6" x1="{bx(x)}" y1="{B2}" x2="{bx(x)}" y2="{by(p):g}"/>')
    for x, p in enumerate(F_X):
        s.append(f'  <text class="valor" x="{bx(x)}" y="{by(p) - 8.5:g}" text-anchor="middle">{num(p)}</text>')
    s.append("</svg>")
    return "\n".join(s)


def ax(x):          # escalera: x = 0 en 100 px, 80 px por unidad
    return 100 + 80 * x


def ay(p):          # escalera: F = 1 a 170 px de la base
    return B2 - 170 * p


def ejes_F(aria):
    s = abrir(260, aria)
    s += [f'  <line class="eje" x1="30" y1="{B2}" x2="600" y2="{B2}"/>',
          f'  <line class="eje" x1="{ax(0)}" y1="222" x2="{ax(0)}" y2="30"/>',
          f'  <line class="guia" x1="{ax(0)}" y1="{ay(1):g}" x2="590" y2="{ay(1):g}"/>',
          f'  <text class="rotulo" x="92" y="{ay(1) + 4:g}" text-anchor="end">1</text>',
          '  <text class="rotulo" x="108" y="34">F(x)</text>']
    for x in range(6):
        s.append(f'  <text class="rotulo" x="{ax(x)}" y="238" text-anchor="middle">{x}</text>')
    s.append('  <text class="rotulo" x="605" y="238" text-anchor="middle">x</text>')
    return s


def tramos():
    s = [f'  <line class="corte" style="stroke-width:3" x1="30" y1="{B2}" x2="{ax(0)}" y2="{B2}"/>']
    for x in range(6):
        fin = ax(x + 1) if x < 5 else 590
        s.append(f'  <line class="corte" style="stroke-width:3" x1="{ax(x)}" y1="{ay(ACUM[x]):g}" '
                 f'x2="{fin}" y2="{ay(ACUM[x]):g}"/>')
    for x in range(5):
        # el de 0,95 va debajo del escalón: arriba está la guía del 1
        dy = 18.5 if x == 4 else -8.5
        s.append(f'  <text class="valor" x="{ax(x) + 40}" y="{ay(ACUM[x]) + dy:g}" text-anchor="middle">'
                 f'{num(ACUM[x])}</text>')
    return s


def F_ejes():
    s = ejes_F("Paso 2: los ejes del gráfico de F(x). Horizontal x de 0 a 5; vertical F(x) hasta 1, con una "
               "línea punteada en altura 1")
    s.append("</svg>")
    return "\n".join(s)


def F_tramos():
    s = ejes_F("Paso 3: los tramos horizontales de F(x): 0 antes de 0, luego 0,05; 0,20; 0,45; 0,80; 0,95 "
               "y 1 desde x = 5")
    s += tramos()
    s.append("</svg>")
    return "\n".join(s)


def F_escalera():
    s = ejes_F("Gráfico en escalera de F(x): 0 antes de 0, luego 0,05; 0,20; 0,45; 0,80; 0,95 y 1 desde x = 5")
    s += tramos()
    previo = [0] + ACUM[:5]
    for x in range(6):
        s.append(f'  <circle class="campana" style="stroke-width:2" cx="{ax(x)}" cy="{ay(previo[x]):g}" r="4"/>')
    for x in range(6):
        s.append(f'  <circle class="punto" cx="{ax(x)}" cy="{ay(ACUM[x]):g}" r="4.5"/>')
    s.append("</svg>")
    return "\n".join(s)


# ---------------------------------------------------------------- Campanas (ej. 3 y 4)

BASE, CENTRO, ALTO = 205, 310, 155      # el pico de la campana de referencia sube 155 px
PX_SIGMA = 56                           # 56 px por desvío de la campana de referencia
X0, X1 = 40, 580


class Campana:
    """Normal de media mu dibujada con 56 px por cada 'ref' unidades (el desvío de referencia)."""

    def __init__(self, mu, ref, sigma=None):
        self.mu, self.ref, self.sigma = mu, ref, sigma or ref

    def px(self, x):
        return CENTRO + (x - self.mu) / self.ref * PX_SIGMA

    def x_de_px(self, p):
        return self.mu + (p - CENTRO) / PX_SIGMA * self.ref

    def py(self, x):
        # la altura es proporcional a la densidad: con un desvío mayor, el pico baja (ref / sigma)
        z = (x - self.mu) / self.sigma
        return BASE - ALTO * self.ref / self.sigma * math.exp(-z * z / 2)

    def trazo(self, a, b, pasos=120):
        xs = [a + (b - a) * i / pasos for i in range(pasos + 1)]
        return " ".join(f"L {self.px(x):.1f},{self.py(x):.1f}" for x in xs)

    def curva(self, clase="campana"):
        a, b = self.x_de_px(X0), self.x_de_px(X1)
        return f'  <path class="{clase}" d="M {X0},{self.py(a):.1f} {self.trazo(a, b)}"/>'

    def area(self, a, b, clase="area"):
        a, b = max(a, self.x_de_px(X0)), min(b, self.x_de_px(X1))
        return (f'  <path class="{clase}" d="M {self.px(a):.1f},{BASE} L {self.px(a):.1f},{self.py(a):.1f} '
                f'{self.trazo(a, b, 60)} L {self.px(b):.1f},{BASE} Z"/>')

    def corte(self, x, clase="corte"):
        return (f'  <line class="{clase}" x1="{self.px(x):.1f}" y1="{self.py(x):.1f}" '
                f'x2="{self.px(x):.1f}" y2="{BASE}"/>')

    def simetria(self, arriba=None):
        return (f'  <line class="guia" x1="{CENTRO}" y1="{arriba or self.py(self.mu):.1f}" '
                f'x2="{CENTRO}" y2="{BASE}"/>')


def eje():
    return f'  <line class="eje" x1="30" y1="{BASE}" x2="595" y2="{BASE}"/>'


def rot(x, y, texto, ancla="middle", clase="rotulo"):
    return f'  <text class="{clase}" x="{x:.1f}" y="{y}" text-anchor="{ancla}">{texto}</text>'


def marca(x):
    return f'  <line class="eje" x1="{x:.1f}" y1="{BASE}" x2="{x:.1f}" y2="{BASE + 6}"/>'


# ---------------------------------------------------------------- Ej. 3: N(200; 25)

API = Campana(200, 25)
MARCAS_API = [200 + k * 25 for k in range(-3, 4)]          # 125 ... 275


def escala_api():
    s = [eje()]
    for k, x in zip(range(-3, 4), MARCAS_API):
        s += [marca(API.px(x)), rot(API.px(x), 222, x), rot(API.px(x), 242, num(k, 0))]
    s += [rot(20, 222, "x (ms)", "start"), rot(20, 242, "z", "start")]
    return s


def api_escala():
    s = abrir(250, "Paso 1: el eje horizontal con los tiempos de 125 a 275 ms, de a un desvío (25 ms), y "
                   "debajo el z de cada marca, de −3 a 3")
    s += escala_api() + ["</svg>"]
    return "\n".join(s)


def campana_api():
    yi = API.py(175)
    return [API.curva(), API.simetria(API.py(200) - 12),
            f'  <circle class="punto" cx="{CENTRO}" cy="{API.py(200):.1f}" r="5"/>',
            f'  <circle class="punto" cx="{API.px(175):.1f}" cy="{yi:.1f}" r="5"/>',
            f'  <circle class="punto" cx="{API.px(225):.1f}" cy="{yi:.1f}" r="5"/>']


def api_campana():
    s = abrir(250, "Paso 2: la campana con el pico sobre 200, simétrica respecto de la línea punteada en 200, "
                   "con los puntos de inflexión en 175 y 225 y casi pegada al eje desde 125 y desde 275")
    yi = API.py(175)
    s += campana_api() + escala_api()
    s += [rot(CENTRO + 12, f"{API.py(200) - 2:.1f}", "pico en 200", "start"),
          rot(API.px(175) - 10, f"{yi - 4:.1f}", "inflexión", "end"),
          rot(API.px(225) + 10, f"{yi - 4:.1f}", "inflexión", "start"),
          "</svg>"]
    return "\n".join(s)


def api_a():
    s = abrir(250, "Paso 3: la campana con el tramo entre 175 y 225 ms (z de −1 a 1) sombreado; el área "
                   "sombreada vale 0,6826")
    s += [API.area(175, 225)] + campana_api()[:2] + escala_api()
    s += [API.corte(175), API.corte(225),
          rot(CENTRO, 160, "0,6826", clase="valor"),
          "</svg>"]
    return "\n".join(s)


def api_b():
    x = 200 - 0.84 * 25                                     # 179
    s = abrir(250, "Campana normal con la cola izquierda sombreada hasta 179 ms (z = −0,84), de área 0,20; "
                   "a la derecha queda 0,80")
    s += [API.area(API.x_de_px(X0), x), API.curva(), eje(), API.simetria(), API.corte(x),
          marca(API.px(x)), marca(CENTRO),
          rot(API.px(x), 222, "179"), rot(CENTRO, 222, "200"),
          rot(API.px(x), 242, "−0,84"), rot(CENTRO, 242, "0"),
          rot(20, 222, "x (ms)", "start"), rot(20, 242, "z", "start"),
          rot(232, 194, "0,20", clase="valor"),
          rot(345, 150, "0,80"),
          "</svg>"]
    return "\n".join(s)


def api_c():
    ancha = Campana(200, 25, 35)
    s = abrir(250, "Dos campanas con la misma media 200: la de desvío 25, punteada, más alta (0,0160) y "
                   "angosta; la de desvío 35, llena, más baja (0,0114) y ancha. Líneas en 175 y 225")
    s += [API.curva("campana angosta"), ancha.curva(), eje(), API.simetria(30),
          API.corte(175), API.corte(225),
          f'  <circle class="punto" cx="{CENTRO}" cy="{API.py(200):.1f}" r="5"/>',
          f'  <circle class="punto" cx="{CENTRO}" cy="{ancha.py(200):.1f}" r="5"/>']
    for x in (175, 200, 225):
        s += [marca(API.px(x)), rot(API.px(x), 224, x)]
    s += [rot(CENTRO + 12, f"{API.py(200) - 2:.1f}", "σ = 25: altura 0,0160", "start", "valor"),
          rot(445, 165, "σ = 35: altura 0,0114", "start", "valor"),
          "</svg>"]
    return "\n".join(s)


# ---------------------------------------------------------------- Ej. 4: prueba de hipótesis

Z = Campana(0, 1)
CRIT, EST = -1.645, -0.3 / (0.6 / math.sqrt(30))           # −1,645 y −2,74


def z_base(rotular_enteros):
    s = [eje()]
    for k in range(-3, 4):
        s.append(marca(Z.px(k)))
        if rotular_enteros or k == 0:
            s.append(rot(Z.px(k), 224, num(k, 0)))
    s.append(rot(20, 224, "z", "start"))
    return s


def ph_campana():
    s = abrir(240, "Paso 1: la campana de Z si H₀ es cierta, centrada en 0, con el eje marcado de −3 a 3")
    s += [Z.curva(), Z.simetria()] + z_base(True) + ["</svg>"]
    return "\n".join(s)


def region():
    return [Z.area(Z.x_de_px(X0), CRIT), Z.curva(), Z.simetria(), Z.corte(CRIT),
            rot(Z.px(CRIT), 224, "−1,645"),
            rot(150, 175, "rechazo", clase="valor"),
            rot(140, 152, "área 0,05"),
            rot(340, 150, "0,95"),
            rot(CENTRO, 32, "zona de no rechazo de H₀")]


def ph_region():
    s = abrir(240, "Paso 2: la región de rechazo, la cola izquierda desde −1,645, sombreada con área 0,05; "
                   "a la derecha queda 0,95")
    s += region() + z_base(False) + ["</svg>"]
    return "\n".join(s)


def ph_final():
    s = abrir(240, "Campana normal con la región de rechazo en la cola izquierda desde −1,645 y el "
                   "estadístico −2,74 dentro de ella")
    s += region() + z_base(False)
    s += [f'  <circle class="punto" cx="{Z.px(EST):.1f}" cy="{BASE}" r="5"/>',
          rot(Z.px(EST), 224, num(EST)),
          "</svg>"]
    return "\n".join(s)


GRAFICOS = {
    "f0225-ej2-f-ejes": f_ejes,
    "f0225-ej2-f": f_bastones,
    "f0225-ej2-F-ejes": F_ejes,
    "f0225-ej2-F-tramos": F_tramos,
    "f0225-ej2-F": F_escalera,
    "f0225-ej3-a-escala": api_escala,
    "f0225-ej3-a-campana": api_campana,
    "f0225-ej3-a": api_a,
    "f0225-ej3-b": api_b,
    "f0225-ej3-c": api_c,
    "f0225-ej4-campana": ph_campana,
    "f0225-ej4-region": ph_region,
    "f0225-ej4-d": ph_final,
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
