"""Gráficos de la Unidad 3 de PyE (Variables Aleatorias), calculados y no a ojo.

Uso (desde la raíz del repo):
    python fuentes/pye/graficos_u3.py

En cada fragmento de app/contenido/pye/u3/, el <svg> que está dentro de
<div class="pd-grafico" data-g="nombre"> se reemplaza por el que arma G["nombre"].
El resto del div (el pie, <p class="pd-pie">) no se toca. Las clases (.barra,
.campana, .area, .eje, .guia, .corte, .punto, .rotulo, .valor) están en
app/assets/estilos.css y siguen el tema claro/oscuro.
"""
import glob
import os
import re
from fractions import Fraction as Fr

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CARPETA = os.path.join(RAIZ, "app", "contenido", "pye", "u3")

ANCHO, ALTO = 620, 250
X0, X1 = 60, 590      # zona de dibujo en x
Y0, Y1 = 200, 34      # y del eje (abajo) y del tope


def n(v):
    """Número corto para SVG."""
    s = ("%.1f" % v).rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def coma(v, dec=2):
    s = ("%." + str(dec) + "f") % v
    return s.replace(".", ",")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Lienzo:
    def __init__(self, etiqueta, alto=ALTO, ancho=ANCHO):
        self.p = []
        self.etiqueta = etiqueta
        self.alto = alto
        self.ancho = ancho

    def add(self, s):
        self.p.append("  " + s)

    def linea(self, x1, y1, x2, y2, clase="eje"):
        self.add('<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (clase, n(x1), n(y1), n(x2), n(y2)))

    def camino(self, pts, clase="campana", cerrar=False):
        d = "M " + " L ".join("%s,%s" % (n(a), n(b)) for a, b in pts)
        if cerrar:
            d += " Z"
        relleno = "" if clase.startswith("area") else ' fill="none"'
        self.add('<path class="%s"%s d="%s"/>' % (clase, relleno, d))

    def texto(self, x, y, s, clase="rotulo", ancla="middle"):
        # "M" + raya combinante (U+0304) se dibuja como M con raya arriba (la combinante sola se ve corrida)
        t = esc(s).replace("M̄", '<tspan text-decoration="overline">M</tspan>')
        self.add('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (clase, n(x), n(y), ancla, t))

    def punto(self, x, y, lleno=True, r=4.5):
        if lleno:
            self.add('<circle class="punto" cx="%s" cy="%s" r="%s"/>' % (n(x), n(y), r))
        else:
            self.add('<circle class="corte" fill="none" cx="%s" cy="%s" r="%s"/>' % (n(x), n(y), r))

    def rect(self, x, y, w, h, clase="barra"):
        self.add('<rect class="%s" x="%s" y="%s" width="%s" height="%s"/>' % (clase, n(x), n(y), n(w), n(h)))

    def svg(self):
        return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s">\n' % (self.ancho, self.alto, esc(self.etiqueta))
                + "\n".join(self.p) + "\n</svg>")


def escala(a, b, c, d):
    return lambda v: c + (v - a) * (d - c) / (b - a)


def eje_y(L, sy, marcas, fmt=lambda v: coma(v, 1), x=X0, guias=True, x_fin=X1):
    L.linea(x, Y0, x, Y1 - 10)
    for v in marcas:
        yy = sy(v)
        if guias and v != 0:
            L.linea(x, yy, x_fin, yy, "guia")
        L.texto(x - 8, yy + 4, fmt(v), "rotulo", "end")


# ---------------------------------------------------------------- discretas

def bastones(etiqueta, xs, ps, rotulos_p, eje_x, titulo, marcados=(), ymax=None, xmin=None, xmax=None,
             marcas_y=None):
    L = Lienzo(etiqueta)
    xmin = min(xs) - (max(xs) - min(xs)) * 0.12 if xmin is None else xmin
    xmax = max(xs) + (max(xs) - min(xs)) * 0.12 if xmax is None else xmax
    sx = escala(xmin, xmax, X0 + 10, X1)
    top = ymax or max(ps) * 1.25
    sy = escala(0, top, Y0, Y1)
    eje_y(L, sy, marcas_y or [0, top / 2, top], fmt=lambda v: coma(v, 2))
    L.linea(X0, Y0, X1, Y0)
    for x, p, r in zip(xs, ps, rotulos_p):
        cx = sx(x)
        clase = "barra marcada" if x in marcados else "barra"
        L.rect(cx - 5, sy(p), 10, Y0 - sy(p), clase)
        L.punto(cx, sy(p), True, 4)
        L.texto(cx, sy(p) - 10, r, "valor")
        L.texto(cx, Y0 + 20, n(x) if isinstance(x, (int, float)) else str(x))
    L.texto((X0 + X1) / 2, Y0 + 42, eje_x)
    L.texto(X0 - 4, 18, titulo, "rotulo", "start")
    L.alto = 250
    return L.svg()


def escalonada(etiqueta, xs, Fs, eje_x, rotulos=None, xmin=None, xmax=None, marcar=None):
    """F(x) de una discreta: escalones con punto lleno a la izquierda y vacío a la derecha."""
    L = Lienzo(etiqueta)
    paso = (max(xs) - min(xs)) / max(len(xs) - 1, 1)
    xmin = min(xs) - paso if xmin is None else xmin
    xmax = max(xs) + paso if xmax is None else xmax
    sx = escala(xmin, xmax, X0 + 10, X1)
    sy = escala(0, 1.12, Y0, Y1)
    eje_y(L, sy, [0, 0.5, 1], fmt=lambda v: coma(v, 1))
    L.linea(X0, Y0, X1, Y0)
    # tramo en 0 antes del primer valor
    L.linea(sx(xmin), sy(0), sx(xs[0]), sy(0), "campana")
    L.punto(sx(xs[0]), sy(0), False)
    rotulos = rotulos or [coma(F, 2) for F in Fs]
    for i, (x, F) in enumerate(zip(xs, Fs)):
        x_sig = xs[i + 1] if i + 1 < len(xs) else xmax
        L.linea(sx(x), sy(F), sx(x_sig), sy(F), "campana")
        L.linea(sx(x), sy(0), sx(x), sy(F), "guia")
        L.punto(sx(x), sy(F), True)
        if i + 1 < len(xs):
            L.punto(sx(x_sig), sy(F), False)
        L.texto((sx(x) + sx(x_sig)) / 2, sy(F) - 9, rotulos[i], "valor")
        L.texto(sx(x), Y0 + 20, n(x))
    L.texto((X0 + X1) / 2, Y0 + 42, eje_x)
    L.texto(X0 - 4, 18, "F(x)", "rotulo", "start")
    return L.svg()


# ---------------------------------------------------------------- continuas

def densidad(etiqueta, f, a, b, xmin, xmax, marcas_x, sombra=None, textos=(), ymax=None, marcas_y=None,
             fmt_y=lambda v: coma(v, 2), tramos=None, puntos_y=()):
    """f vale f(x) en [a, b] y 0 afuera. sombra = (lo, hi) se pinta. tramos: lista de (a, b, f) si es por partes."""
    L = Lienzo(etiqueta)
    sx = escala(xmin, xmax, X0 + 10, X1)
    tramos = tramos or [(a, b, f)]
    N = 120
    pts_todos = []
    for ta, tb, tf in tramos:
        pts_todos += [(ta + (tb - ta) * i / N, tf(ta + (tb - ta) * i / N)) for i in range(N + 1)]
    top = ymax or max(v for _, v in pts_todos) * 1.25
    sy = escala(0, top, Y0, Y1)
    eje_y(L, sy, marcas_y or [0, top / 2], fmt=fmt_y)
    L.linea(X0, Y0, X1, Y0)
    if sombra:
        lo, hi = sombra
        poli = [(sx(lo), sy(0))]
        for ta, tb, tf in tramos:
            for i in range(N + 1):
                xv = ta + (tb - ta) * i / N
                if lo <= xv <= hi:
                    poli.append((sx(xv), sy(tf(xv))))
        poli.append((sx(hi), sy(0)))
        L.camino(poli, "area", True)
        for v in (lo, hi):
            if a < v < b:
                yv = next(tf(v) for ta, tb, tf in tramos if ta <= v <= tb)
                L.linea(sx(v), sy(0), sx(v), sy(yv), "corte")
    # cero afuera
    L.linea(sx(xmin), sy(0), sx(a), sy(0), "campana")
    L.linea(sx(b), sy(0), sx(xmax), sy(0), "campana")
    for ta, tb, tf in tramos:
        L.camino([(sx(ta + (tb - ta) * i / N), sy(tf(ta + (tb - ta) * i / N))) for i in range(N + 1)])
    fa, fb = tramos[0][2](a), tramos[-1][2](b)
    if abs(fa) > 1e-12:
        L.linea(sx(a), sy(0), sx(a), sy(fa), "guia")
    if abs(fb) > 1e-12:
        L.linea(sx(b), sy(0), sx(b), sy(fb), "guia")
    for xv, yv in puntos_y:
        L.punto(sx(xv), sy(yv), True, 4)
    for m in marcas_x:
        L.texto(sx(m), Y0 + 20, coma(m, 2).rstrip("0").rstrip(",") if m != int(m) else str(int(m)))
    for (tx, ty, s, clase, ancla) in textos:
        L.texto(sx(tx), sy(ty) if ty is not None else 18, s, clase, ancla)
    return L.svg()


def acumulada(etiqueta, F, a, b, xmin, xmax, marcas_x, puntos=(), textos=()):
    L = Lienzo(etiqueta)
    sx = escala(xmin, xmax, X0 + 10, X1)
    sy = escala(0, 1.12, Y0, Y1)
    eje_y(L, sy, [0, 0.5, 1], fmt=lambda v: coma(v, 1))
    L.linea(X0, Y0, X1, Y0)
    N = 120
    L.linea(sx(xmin), sy(0), sx(a), sy(0), "campana")
    L.camino([(sx(a + (b - a) * i / N), sy(F(a + (b - a) * i / N))) for i in range(N + 1)])
    L.linea(sx(b), sy(1), sx(xmax), sy(1), "campana")
    for xv in puntos:
        L.linea(sx(xv), sy(0), sx(xv), sy(F(xv)), "guia")
        L.punto(sx(xv), sy(F(xv)), True, 4)
    for m in marcas_x:
        L.texto(sx(m), Y0 + 20, coma(m, 2).rstrip("0").rstrip(",") if m != int(m) else str(int(m)))
    for (tx, ty, s, clase, ancla) in textos:
        L.texto(sx(tx), sy(ty) if ty is not None else 18, s, clase, ancla)
    return L.svg()


def region(etiqueta, sop, xr, yr, marcas_x, marcas_y, sombra=None, poligono=None, punteada=None, textos=()):
    """Plano x-y. sop = (x1, x2, y1, y2) el rectángulo donde f > 0. sombra = rectángulo pintado,
    poligono = lista de puntos pintados, punteada = rectángulo con borde punteado (zona fuera de la base)."""
    alto = 300
    L = Lienzo(etiqueta, alto=alto)
    yb, yt = 255, 25
    # misma escala en los dos ejes
    ux = (X1 - 170 - 90) / (xr[1] - xr[0])
    uy = (yb - yt) / (yr[1] - yr[0])
    u = min(ux, uy)
    ox = 150
    sx = lambda v: ox + (v - xr[0]) * u
    sy = lambda v: yb - (v - yr[0]) * u
    x0, x1_, y0, y1_ = sop
    L.add('<rect class="area suave" x="%s" y="%s" width="%s" height="%s"/>' % (
        n(sx(x0)), n(sy(y1_)), n(sx(x1_) - sx(x0)), n(sy(y0) - sy(y1_))))
    L.camino([(sx(x0), sy(y0)), (sx(x1_), sy(y0)), (sx(x1_), sy(y1_)), (sx(x0), sy(y1_))], "corte", True)
    if sombra:
        a1, a2, b1, b2 = sombra
        L.add('<rect class="area" x="%s" y="%s" width="%s" height="%s"/>' % (
            n(sx(a1)), n(sy(b2)), n(sx(a2) - sx(a1)), n(sy(b1) - sy(b2))))
    if poligono:
        L.camino([(sx(a), sy(b)) for a, b in poligono], "area", True)
    if punteada:
        a1, a2, b1, b2 = punteada
        L.camino([(sx(a1), sy(b1)), (sx(a2), sy(b1)), (sx(a2), sy(b2)), (sx(a1), sy(b2))], "guia", True)
    # ejes
    L.linea(sx(xr[0]), sy(0) if yr[0] <= 0 else sy(yr[0]), sx(xr[1]), sy(0) if yr[0] <= 0 else sy(yr[0]))
    L.linea(sx(0) if xr[0] <= 0 else sx(xr[0]), sy(yr[0]), sx(0) if xr[0] <= 0 else sx(xr[0]), sy(yr[1]))
    ybase = sy(0) if yr[0] <= 0 else sy(yr[0])
    xbase = sx(0) if xr[0] <= 0 else sx(xr[0])
    for m in marcas_x:
        L.linea(sx(m), ybase - 4, sx(m), ybase + 4)
        L.texto(sx(m), ybase + 20, fmtm(m))
    for m in marcas_y:
        L.linea(xbase - 4, sy(m), xbase + 4, sy(m))
        L.texto(xbase - 9, sy(m) + 4, fmtm(m), "rotulo", "end")
    L.texto(sx(xr[1]) + 6, ybase + 4, "x", "rotulo", "start")
    L.texto(xbase, sy(yr[1]) - 8, "y", "rotulo", "middle")
    for (tx, ty, s, clase, ancla) in textos:
        L.texto(sx(tx), sy(ty), s, clase, ancla)
    return L.svg()


def fmtm(m):
    fr = Fr(m).limit_denominator(8)
    if fr.denominator == 1:
        return str(fr.numerator)
    return coma(m, 2).rstrip("0")


# ---------------------------------------------------------------- árbol

def arbol(etiqueta, l1, l2, l3, letra_x, hojas_texto):
    """l1: [(rama, prob)], l2: {rama1: [(rama, prob)]}, l3: {rama1+rama2: [(rama, prob)]}.
    hojas_texto: función(camino) -> texto de la hoja."""
    hojas = []
    for r1, _ in l1:
        for r2, _ in l2[r1]:
            for r3, _ in l3[r1 + r2]:
                hojas.append(r1 + r2 + r3)
    alto = 40 + 34 * len(hojas)
    L = Lienzo(etiqueta, alto=alto)
    xs = [24, 150, 280, 410]
    ypos = {}
    for i, h in enumerate(hojas):
        ypos[h] = 30 + 34 * i
    def y_de(pref):
        ys = [ypos[h] for h in hojas if h.startswith(pref)]
        return sum(ys) / len(ys)
    raiz = (xs[0], y_de(""))
    def rama(xa, ya, xb, yb, letra, prob):
        L.linea(xa + 8, ya, xb - 14, yb, "corte")
        mx, my = xa + (xb - xa) * 0.55, ya + (yb - ya) * 0.55
        dy = 15 if yb > ya else -7
        L.texto(mx, my + dy, prob, "rotulo", "middle")
        L.texto(xb, yb + 5, letra, "valor", "middle")
    L.punto(raiz[0], raiz[1], True, 4)
    for r1, p1 in l1:
        y1 = y_de(r1)
        rama(xs[0], raiz[1], xs[1], y1, letra_x(r1), p1)
        for r2, p2 in l2[r1]:
            y2 = y_de(r1 + r2)
            rama(xs[1], y1, xs[2], y2, letra_x(r2), p2)
            for r3, p3 in l3[r1 + r2]:
                y3 = ypos[r1 + r2 + r3]
                rama(xs[2], y2, xs[3], y3, letra_x(r3), p3)
                L.texto(xs[3] + 22, y3 + 5, hojas_texto(r1 + r2 + r3), "rotulo", "start")
    return L.svg()


def letra_m(c):
    return "M" if c == "M" else "M̄"


# ---------------------------------------------------------------- los gráficos

G = {}

# Teoría 2 y 3: computadoras de la cátedra (8, 3 defectuosas, se compran 2)
G["u3-bastones-defectuosos"] = bastones(
    "Gráfico de bastones: f(0) = 10/28, f(1) = 15/28, f(2) = 3/28",
    [0, 1, 2], [10 / 28, 15 / 28, 3 / 28], ["10/28 ≈ 0,357", "15/28 ≈ 0,536", "3/28 ≈ 0,107"],
    "x = computadoras defectuosas compradas", "f(x)", ymax=0.7, xmin=-0.7, xmax=2.7, marcas_y=[0, 0.25, 0.5])
G["u3-F-defectuosos"] = escalonada(
    "Acumulada escalonada: F vale 0 antes de 0, 10/28 desde 0, 25/28 desde 1 y 1 desde 2",
    [0, 1, 2], [10 / 28, 25 / 28, 1], "x = computadoras defectuosas compradas",
    rotulos=["10/28", "25/28", "1"], xmin=-1, xmax=3)

# Parcial 1 2025, ej. 4: publicaciones
pub_x = [0, 1, 2, 3, 4, 5]
pub_p = [0.20, 0.25, 0.18, 0.15, 0.10, 0.12]
pub_F = [0.20, 0.45, 0.63, 0.78, 0.88, 1.00]
G["u3-bastones-publicaciones"] = bastones(
    "Bastones de las publicaciones: 0,20; 0,25; 0,18; 0,15; 0,10; 0,12",
    pub_x, pub_p, [coma(p) for p in pub_p], "x = publicaciones de un usuario en un día", "f(x)",
    ymax=0.32, xmin=-0.6, xmax=5.6, marcas_y=[0, 0.1, 0.2, 0.3])
G["u3-F-publicaciones"] = escalonada(
    "Acumulada escalonada de las publicaciones: 0,20; 0,45; 0,63; 0,78; 0,88; 1",
    pub_x, pub_F, "x = publicaciones de un usuario en un día", xmin=-1, xmax=6)

# Final 25/02/2026, ej. 2: solicitudes con k
sol_x = [0, 1, 2, 3, 4, 5]
sol_p = [0.05, 0.15, 0.25, 0.35, 0.15, 0.05]
G["u3-bastones-solicitudes"] = bastones(
    "Bastones de las solicitudes: 0,05; 0,15; 0,25; 0,35; 0,15; 0,05",
    sol_x, sol_p, ["0,05", "0,15", "0,25", "k = 0,35", "0,15", "0,05"],
    "x = solicitudes que van a la base de datos", "f(x)", ymax=0.45, xmin=-0.6, xmax=5.6,
    marcas_y=[0, 0.2, 0.4])
G["u3-F-solicitudes"] = escalonada(
    "Acumulada de las solicitudes: 0,05; 0,20; 0,45; 0,80; 0,95; 1",
    sol_x, [0.05, 0.20, 0.45, 0.80, 0.95, 1.0], "x = solicitudes que van a la base de datos", xmin=-1, xmax=6)

# Teoría 4: integral = área
G["u3-area-integral"] = densidad(
    "La recta f(x) = x entre 0 y 2: el área pintada es un triángulo de base 2 y altura 2, vale 2",
    lambda x: x, 0, 2, -0.5, 2.6, [0, 1, 2], sombra=(0, 2), ymax=2.5, marcas_y=[0, 1, 2],
    fmt_y=lambda v: n(v),
    textos=[(1.35, 0.35, "área = 2 × 2 / 2 = 2", "valor", "middle"),
            (1.9, 2.25, "f(x) = x", "rotulo", "end")])

# Teoría 5: la de la cátedra x²/3 en (−1; 2)
G["u3-densidad-catedra"] = densidad(
    "Densidad x²/3 entre −1 y 2, con el área entre −1 y 1 pintada: vale 2/9",
    lambda x: x * x / 3, -1, 2, -1.8, 2.8, [-1, 0, 1, 1.5, 2], sombra=(-1, 1), ymax=1.6,
    marcas_y=[0, 0.5, 1, 1.5], fmt_y=lambda v: coma(v, 1),
    textos=[(0, 0.5, "P(−1 < X < 1) = 2/9", "valor", "middle"),
            (2.05, 1.38, "f(x) = x²/3", "rotulo", "start")])
G["u3-densidad-3x2"] = densidad(
    "Densidad 3x²/8 entre 0 y 2, con el área entre 0,5 y 1,5 pintada: vale 13/32",
    lambda x: 3 * x * x / 8, 0, 2, -0.5, 2.6, [0, 0.5, 1, 1.5, 2], sombra=(0.5, 1.5), ymax=1.8,
    marcas_y=[0, 0.5, 1, 1.5], fmt_y=lambda v: coma(v, 1),
    textos=[(0.55, 0.9, "P(0,5 < X < 1,5) = 13/32", "valor", "middle"),
            (2.05, 1.55, "f(x) = 3x²/8", "rotulo", "start")])

# Teoría 6: hallar k
G["u3-densidad-kx2"] = densidad(
    "Densidad x²/9 entre 0 y 3: el área total vale 1",
    lambda x: x * x / 9, 0, 3, -0.5, 3.7, [0, 1, 2, 3], sombra=(0, 3), ymax=1.3, marcas_y=[0, 0.5, 1],
    fmt_y=lambda v: coma(v, 1),
    textos=[(2.3, 0.15, "área total = 1", "valor", "middle"),
            (3.05, 1.08, "f(x) = x²/9", "rotulo", "start")])
G["u3-densidad-ingresos"] = densidad(
    "Densidad (2/15)(x/5 + 1) entre 0 y 5, con el área de 3 a 5 pintada: vale 0,48",
    lambda x: Fr(2, 15) * (x / 5 + 1), 0, 5, -0.7, 6, [0, 1, 2, 3, 4, 5], sombra=(3, 5), ymax=0.36,
    marcas_y=[0, 0.1, 0.2, 0.3], fmt_y=lambda v: coma(v, 1),
    textos=[(4, 0.05, "P(X > 3) = 0,48", "valor", "middle"),
            (0.1, 0.165, "f(0) = 2/15", "rotulo", "start"),
            (5.05, 0.29, "f(5) = 4/15", "rotulo", "start")])

# Teoría 7: F continua
G["u3-F-catedra"] = acumulada(
    "Acumulada (x³ + 1)/9: vale 0 antes de −1, sube como curva y vale 1 desde 2",
    lambda x: (x ** 3 + 1) / 9, -1, 2, -1.8, 2.8, [-1, 0, 1, 1.5, 2], puntos=[1, 1.5],
    textos=[(1, 0.32, "F(1) = 2/9", "valor", "end"),
            (1.45, 0.6, "F(1,5) = 35/72", "valor", "end")])
G["u3-densidad-tickets"] = densidad(
    "Densidad (4 − x)/8 entre 0 y 4, con el área de 1 a 3 pintada: vale 0,5",
    lambda x: (4 - x) / 8, 0, 4, -0.7, 4.8, [0, 1, 2, 3, 4], sombra=(1, 3), ymax=0.62,
    marcas_y=[0, 0.25, 0.5], fmt_y=lambda v: coma(v, 2),
    textos=[(2, 0.04, "P(1 < X ≤ 3) = 0,5", "valor", "middle"),
            (0.1, 0.55, "f(x) = (4 − x)/8", "rotulo", "start")])
G["u3-F-tickets"] = acumulada(
    "Acumulada x/2 − x²/16 entre 0 y 4: F(1) = 7/16 y F(3) = 15/16",
    lambda x: x / 2 - x * x / 16, 0, 4, -0.7, 4.8, [0, 1, 2, 3, 4], puntos=[1, 3],
    textos=[(1.1, 0.33, "F(1) = 7/16", "valor", "start"),
            (2.9, 0.98, "F(3) = 15/16", "valor", "end")])

# Teoría 10 y 11: regiones de la conjunta continua
G["u3-region-kxy"] = region(
    "Cuadrado de 0 a 1 en x y en y; pintado el rectángulo 0 < x < 0,5 y 0,25 < y < 0,5",
    (0, 1, 0, 1), (0, 1.25), (0, 1.2), [0, 0.5, 1], [0.25, 0.5, 1], sombra=(0, 0.5, 0.25, 0.5),
    textos=[(0.75, 0.85, "f(x,y) = 4xy", "rotulo", "middle"),
            (0.25, 0.6, "la región pedida", "valor", "middle")])
G["u3-region-triangulo"] = region(
    "Cuadrado de 0 a 1; pintado el triángulo debajo de la diagonal y = x",
    (0, 1, 0, 1), (0, 1.25), (0, 1.2), [0, 1], [1], poligono=[(0, 0), (1, 0), (1, 1)],
    textos=[(0.7, 0.25, "y < x", "valor", "middle"),
            (0.3, 0.85, "y > x", "rotulo", "middle")])
G["u3-region-parcial-base"] = region(
    "Rectángulo 0 ≤ x ≤ 2, 1 ≤ y ≤ 3: es la única zona donde f(x,y) no vale 0",
    (0, 2, 1, 3), (0, 3), (0, 3.6), [0, 1, 2, 3], [1, 2, 3],
    textos=[(1, 2, "f(x,y) = (x + 2y)/20", "valor", "middle"),
            (2.5, 0.4, "afuera: f = 0", "rotulo", "middle")])
G["u3-region-parcial-c"] = region(
    "La zona x > 2 y y < 1 (punteada) queda toda afuera del rectángulo donde f no vale 0",
    (0, 2, 1, 3), (0, 3), (0, 3.6), [0, 1, 2, 3], [1, 2, 3], punteada=(2, 2.95, 0.02, 0.98),
    textos=[(1, 2, "acá f > 0", "rotulo", "middle"),
            (2.47, 0.45, "x > 2, y < 1", "valor", "middle")])
G["u3-region-parcial-d"] = region(
    "La franja y < 1 (punteada) queda toda debajo del rectángulo donde f no vale 0",
    (0, 2, 1, 3), (0, 3), (0, 3.6), [0, 1, 2, 3], [1, 2, 3], punteada=(0.02, 2.95, 0.02, 0.98),
    textos=[(1, 2, "acá f > 0", "rotulo", "middle"),
            (1.5, 0.45, "y < 1: acá f = 0", "valor", "middle")])
G["u3-region-parcial-e"] = region(
    "Rectángulo 0 ≤ x ≤ 2, 1 ≤ y ≤ 3; pintado el pedazo 0 ≤ x < 1, 1 ≤ y < 2",
    (0, 2, 1, 3), (0, 3), (0, 3.6), [0, 1, 2, 3], [1, 2, 3], sombra=(0, 1, 1, 2),
    textos=[(0.5, 1.5, "pedida", "valor", "middle"),
            (1.5, 2.5, "f > 0", "rotulo", "middle")])

# ---------------------------------------------------------------- práctica

# Ej. 1: autos manchados (5 autos, 2 manchados, se reciben 3)
G["u3-p-arbol-autos"] = arbol(
    "Árbol de los tres autos: cada rama M (manchado) o M con barra (no manchado), con su probabilidad",
    [("M", "2/5"), ("N", "3/5")],
    {"M": [("M", "1/4"), ("N", "3/4")], "N": [("M", "2/4"), ("N", "2/4")]},
    {"MM": [("N", "3/3")], "MN": [("M", "1/3"), ("N", "2/3")],
     "NM": [("M", "1/3"), ("N", "2/3")], "NN": [("M", "2/3"), ("N", "1/3")]},
    letra_m,
    lambda h: "".join(letra_m(c) for c in h) + " · x = %d · %s" % (
        h.count("M"), {"MMN": "6/60", "MNM": "6/60", "MNN": "12/60", "NMM": "6/60", "NMN": "12/60",
                       "NNM": "12/60", "NNN": "6/60"}[h]))
G["u3-p-bastones-autos"] = bastones(
    "Bastones de los autos manchados: 1/10, 6/10, 3/10",
    [0, 1, 2], [0.1, 0.6, 0.3], ["1/10", "6/10", "3/10"], "x = autos manchados recibidos", "f(x)",
    ymax=0.75, xmin=-0.7, xmax=2.7, marcas_y=[0, 0.25, 0.5])

# Ej. 2: computadoras (7, 2 defectuosas, se compran 3)
G["u3-p-arbol-computadoras"] = arbol(
    "Árbol de las tres computadoras: cada rama D (defectuosa) o N (no defectuosa), con su probabilidad",
    [("D", "2/7"), ("N", "5/7")],
    {"D": [("D", "1/6"), ("N", "5/6")], "N": [("D", "2/6"), ("N", "4/6")]},
    {"DD": [("N", "5/5")], "DN": [("D", "1/5"), ("N", "4/5")],
     "ND": [("D", "1/5"), ("N", "4/5")], "NN": [("D", "2/5"), ("N", "3/5")]},
    lambda c: c,
    lambda h: h + " · x = %d · %s" % (
        h.count("D"), {"DDN": "10/210", "DND": "10/210", "DNN": "40/210", "NDD": "10/210", "NDN": "40/210",
                       "NND": "40/210", "NNN": "60/210"}[h]))
G["u3-p-bastones-computadoras"] = bastones(
    "Bastones de las computadoras defectuosas: 6/21, 12/21, 3/21",
    [0, 1, 2], [6 / 21, 12 / 21, 3 / 21], ["6/21", "12/21", "3/21"], "x = computadoras defectuosas recibidas",
    "f(x)", ymax=0.75, xmin=-0.7, xmax=2.7, marcas_y=[0, 0.25, 0.5])

# Ej. 3: temperatura (4 − x²)/9 en [−1; 2]
G["u3-p-ej3-densidad"] = densidad(
    "Densidad (4 − x²)/9 entre −1 y 2, con el área hasta 0 pintada: vale 11/27",
    lambda x: (4 - x * x) / 9, -1, 2, -1.8, 2.8, [-1, 0, 1, 2], sombra=(-1, 0), ymax=0.6,
    marcas_y=[0, 0.25, 0.5], fmt_y=lambda v: coma(v, 2),
    textos=[(-0.5, 0.12, "11/27", "valor", "middle"),
            (0.5, 0.53, "f(x) = (4 − x²)/9", "rotulo", "start")])
G["u3-p-ej3-entre"] = densidad(
    "Densidad (4 − x²)/9 con el área entre 0 y 1 pintada: vale 11/27",
    lambda x: (4 - x * x) / 9, -1, 2, -1.8, 2.8, [-1, 0, 1, 2], sombra=(0, 1), ymax=0.6,
    marcas_y=[0, 0.25, 0.5], fmt_y=lambda v: coma(v, 2),
    textos=[(0.5, 0.12, "11/27", "valor", "middle"),
            (-1.7, 0.53, "f(x) = (4 − x²)/9", "rotulo", "start")])

# Ej. 4: libro, kx en [0; 2]
G["u3-p-ej4-densidad"] = densidad(
    "Densidad x/2 entre 0 y 2: una recta que sube de 0 a 1; el área hasta 1,5 pintada",
    lambda x: x / 2, 0, 2, -0.6, 2.7, [0, 0.5, 1, 1.5, 2], sombra=(0, 1.5), ymax=1.25, marcas_y=[0, 0.5, 1],
    fmt_y=lambda v: coma(v, 1),
    textos=[(1.1, 0.12, "P(X < 1,5) = 0,5625", "valor", "middle"),
            (2.05, 1.08, "f(x) = x/2", "rotulo", "start")])
G["u3-p-ej4-F"] = acumulada(
    "Acumulada x²/4: 0 antes de 0, curva entre 0 y 2, 1 desde 2",
    lambda x: x * x / 4, 0, 2, -0.6, 2.7, [0, 0.5, 1, 1.5, 2], puntos=[1.5],
    textos=[(1.45, 0.62, "F(1,5) = 0,5625", "valor", "end")])

# Ej. 5: ganancias MRA
mra_x = [-100, 0, 50, 100, 150, 200]
mra_p = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]
G["u3-p-ej5-bastones"] = bastones(
    "Bastones de las ganancias: 0,10; 0,20; 0,30; 0,25; 0,10; 0,05 (marcados 150 y 200)",
    mra_x, mra_p, [coma(p) for p in mra_p], "x = ganancia en miles de dólares", "f(x)", marcados=(150, 200),
    ymax=0.38, xmin=-130, xmax=230, marcas_y=[0, 0.1, 0.2, 0.3])
G["u3-p-ej5-F"] = escalonada(
    "Acumulada de las ganancias: 0,10; 0,30; 0,60; 0,85; 0,95; 1",
    mra_x, [0.10, 0.30, 0.60, 0.85, 0.95, 1.0], "x = ganancia en miles de dólares", xmin=-150, xmax=250)

# Ej. 6: la F dada
G["u3-p-ej6-F"] = escalonada(
    "La acumulada dada: 0 antes de 1; 0,1 desde 1; 0,5 desde 2; 0,7 desde 3; 1 desde 4",
    [1, 2, 3, 4], [0.1, 0.5, 0.7, 1.0], "x", rotulos=["0,1", "0,5", "0,7", "1"], xmin=-1, xmax=5)

# Ej. 7: aspiradora, triangular
G["u3-p-ej7-densidad"] = densidad(
    "Densidad triangular: x entre 0 y 1, 2 − x entre 1 y 2; el área hasta 1,2 pintada: vale 0,68",
    None, 0, 2, -0.5, 2.6, [0, 0.5, 1, 1.2, 2], sombra=(0, 1.2), ymax=1.3, marcas_y=[0, 0.5, 1],
    fmt_y=lambda v: coma(v, 1),
    tramos=[(0, 1, lambda x: x), (1, 2, lambda x: 2 - x)],
    textos=[(0.75, 0.2, "0,68", "valor", "middle"),
            (0.05, 1.1, "f(x) = x", "rotulo", "start"),
            (1.55, 0.75, "f(x) = 2 − x", "rotulo", "start")])
G["u3-p-ej7-entre"] = densidad(
    "La misma densidad triangular, con el área entre 0,5 y 1 pintada: vale 3/8",
    None, 0, 2, -0.5, 2.6, [0, 0.5, 1, 2], sombra=(0.5, 1), ymax=1.3, marcas_y=[0, 0.5, 1],
    fmt_y=lambda v: coma(v, 1),
    tramos=[(0, 1, lambda x: x), (1, 2, lambda x: 2 - x)],
    textos=[(0.75, 0.25, "3/8", "valor", "middle"),
            (1.55, 0.75, "f(x) = 2 − x", "rotulo", "start")])

# Ej. 8: fichas USB, (6 + 2x)/7 en [0; 1]
G["u3-p-ej8-densidad"] = densidad(
    "Densidad (6 + 2x)/7 entre 0 y 1, con el área entre 0,1 y 0,5 pintada: vale 0,3771",
    lambda x: (6 + 2 * x) / 7, 0, 1, -0.3, 1.35, [0, 0.1, 0.5, 1], sombra=(0.1, 0.5), ymax=1.45,
    marcas_y=[0, 0.5, 1], fmt_y=lambda v: coma(v, 1),
    textos=[(0.3, 0.45, "0,3771", "valor", "middle"),
            (0.55, 1.3, "f(x) = (6 + 2x)/7", "rotulo", "start")])

# Ej. 9: pilas con k
G["u3-p-ej9-bastones"] = bastones(
    "Bastones de las pilas defectuosas: 2/5, 1/5, 4/15, 2/15",
    [0, 1, 2, 3], [0.4, 0.2, 4 / 15, 2 / 15], ["2/5", "1/5", "4/15", "2/15"], "x = pilas defectuosas en la linterna",
    "f(x)", ymax=0.5, xmin=-0.7, xmax=3.7, marcas_y=[0, 0.2, 0.4])

# Ej. 10: perno, (3x − 1)/136 en [2; 10]
G["u3-p-ej10-densidad"] = densidad(
    "Densidad (3x − 1)/136 entre 2 y 10, con el área desde 5 pintada: vale 0,7904",
    lambda x: (3 * x - 1) / 136, 2, 10, 0.5, 11.2, [2, 4, 5, 6, 8, 10], sombra=(5, 10), ymax=0.26,
    marcas_y=[0, 0.1, 0.2], fmt_y=lambda v: coma(v, 1),
    textos=[(7.6, 0.03, "P(X ≥ 5) = 0,7904", "valor", "middle"),
            (2.1, 0.22, "f(x) = (3x − 1)/136", "rotulo", "start")])

# Ej. 11: pestañas
pes_x = [1, 2, 3, 4, 5, 6]
pes_p = [0.40, 0.25, 0.20, 0.05, 0.05, 0.05]
G["u3-p-ej11-bastones"] = bastones(
    "Bastones de las pestañas: 0,40; 0,25; 0,20; 0,05; 0,05; 0,05",
    pes_x, pes_p, [coma(p) for p in pes_p], "x = pestañas abiertas a la vez", "f(x)",
    ymax=0.5, xmin=0.4, xmax=6.6, marcas_y=[0, 0.2, 0.4])
G["u3-p-ej11-F"] = escalonada(
    "Acumulada de las pestañas: 0,40; 0,65; 0,85; 0,90; 0,95; 1",
    pes_x, [0.40, 0.65, 0.85, 0.90, 0.95, 1.0], "x = pestañas abiertas a la vez", xmin=0, xmax=7)


def main():
    patron = re.compile(r'(<div class="pd-grafico" data-g="([^"]+)">\s*)<svg.*?</svg>', re.S)
    usados = set()
    faltan = set()
    for ruta in sorted(glob.glob(os.path.join(CARPETA, "**", "*.html"), recursive=True)):
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()

        def cambiar(m):
            nombre = m.group(2)
            if nombre not in G:
                faltan.add(nombre)
                return m.group(0)
            usados.add(nombre)
            return m.group(1) + G[nombre]

        nuevo = patron.sub(cambiar, texto)
        if nuevo != texto:
            with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(nuevo)
    print("Gráficos puestos: %d" % len(usados))
    if faltan:
        print("Sin definir:", ", ".join(sorted(faltan)))
    sobran = set(G) - usados
    if sobran:
        print("Definidos y no usados:", ", ".join(sorted(sobran)))


if __name__ == "__main__":
    main()
