"""Gráficos de la teoría de la Unidad 4 de Matemática Discreta (relaciones de recurrencia).

Uso (desde la raíz del repo):
    python fuentes/md/graficos_u4.py

En cada fragmento de app/contenido/md/u4/teoria/, lo que está dentro de
<div class="pd-grafico" data-g="nombre"> ... </div> hasta el <svg> inclusive se
reemplaza por el que arma G["nombre"]. El pie (<p class="pd-pie">) no se toca.
Las clases (.eje, .guia, .corte, .punto, .rotulo, .valor, .campana) están en
app/assets/estilos.css y siguen el tema claro/oscuro. Todo se calcula, nada a ojo.
"""
import glob
import math
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CARPETA = os.path.join(RAIZ, "app", "contenido", "md", "u4", "teoria")


def n(v):
    s = ("%.1f" % v).rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Lienzo:
    def __init__(self, etiqueta, ancho, alto):
        self.p, self.etiqueta, self.ancho, self.alto = [], etiqueta, ancho, alto

    def add(self, s):
        self.p.append("  " + s)

    def linea(self, x1, y1, x2, y2, clase="eje"):
        self.add('<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (clase, n(x1), n(y1), n(x2), n(y2)))

    def camino(self, d, clase="corte"):
        self.add('<path class="%s" fill="none" d="%s"/>' % (clase, d))

    def texto(self, x, y, s, clase="rotulo", ancla="middle"):
        self.add('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (clase, n(x), n(y), ancla, esc(s)))

    def punto(self, x, y, r=4.5):
        self.add('<circle class="punto" cx="%s" cy="%s" r="%s"/>' % (n(x), n(y), r))

    def flecha(self, x1, y1, x2, y2):
        """Eje con punta de flecha (dos trazos cortos al final)."""
        self.linea(x1, y1, x2, y2)
        ang = math.atan2(y2 - y1, x2 - x1)
        for d in (2.6, -2.6):
            self.linea(x2, y2, x2 - 9 * math.cos(ang + d / 6), y2 - 9 * math.sin(ang + d / 6))

    def svg(self):
        return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s">\n' % (self.ancho, self.alto, esc(self.etiqueta))
                + "\n".join(self.p) + "\n</svg>")


def escala(a, b, c, d):
    return lambda v: c + (v - a) * (d - c) / (b - a)


def sucesion():
    """a_n = n/(n+1): puntos en el plano (n, a_n) y, abajo, los mismos valores sobre la recta."""
    L = Lienzo("Sucesión n/(n+1): puntos en el plano y sobre la recta", 620, 330)
    X0, X1, Y0, Y1 = 70, 590, 200, 30
    N = 14
    sx = escala(0, N + 0.6, X0, X1)
    sy = escala(0, 1.15, Y0, Y1)
    L.flecha(X0, Y0, X1 + 10, Y0)
    L.flecha(X0, Y0, X0, Y1 - 12)
    L.texto(X1 + 6, Y0 + 30, "n")
    L.texto(X0 - 10, Y1 - 16, "aₙ", "rotulo", "end")
    L.texto(X0 - 10, Y0 + 5, "0", "rotulo", "end")
    L.linea(X0, sy(1), X1, sy(1), "guia")
    L.texto(X0 - 10, sy(1) + 5, "1", "rotulo", "end")
    for k in range(1, N + 1):
        L.linea(sx(k), Y0, sx(k), Y0 + 5)
        L.texto(sx(k), Y0 + 20, str(k))
        L.punto(sx(k), sy(k / (k + 1)), 4)
    # a_7 = 7/8
    L.linea(sx(7), Y0, sx(7), sy(7 / 8), "corte")
    L.texto(sx(7) + 10, (Y0 + sy(7 / 8)) / 2 + 5, "a₇ = 7/8", "valor", "start")
    # la recta
    YR = 290
    rx = escala(0, 1.1, X0, X1)
    L.linea(X0 - 20, YR, X1 + 10, YR)
    for v, t in ((0, "0"), (0.5, "1/2"), (1, "1")):
        L.linea(rx(v), YR - 7, rx(v), YR + 7)
        L.texto(rx(v), YR + 26, t)
    for k in range(1, 40):
        L.linea(rx(k / (k + 1)), YR - 5, rx(k / (k + 1)), YR + 5, "corte")
    for k in (1, 2, 3):
        L.texto(rx(k / (k + 1)), YR - 14, "a%s" % "₀₁₂₃"[k])
    L.texto((X0 + X1) / 2, YR - 34, "los mismos valores sobre la recta: se amontonan cerca de 1")
    return L.svg()


def complejo():
    """El número 1 + i en el plano: módulo √2 y argumento 45°; y su conjugado 1 − i."""
    L = Lienzo("El complejo 1 + i: módulo raíz de 2 y argumento 45 grados", 620, 330)
    cx, cy, u = 250, 165, 100  # origen y largo de una unidad
    L.flecha(cx - 1.6 * u, cy, cx + 2.6 * u, cy)
    L.flecha(cx, cy + 1.5 * u, cx, cy - 1.5 * u)
    L.texto(cx + 2.6 * u + 6, cy + 22, "parte real", "rotulo", "end")
    L.texto(cx + 8, cy - 1.5 * u + 4, "parte imaginaria", "rotulo", "start")
    for v in (1, 2):
        L.linea(cx + v * u, cy - 5, cx + v * u, cy + 5)
        L.texto(cx + v * u + 8, cy + 20, str(v), "rotulo", "start")
    L.linea(cx - 5, cy - u, cx + 5, cy - u)
    L.texto(cx - 10, cy - u + 5, "1", "rotulo", "end")
    L.linea(cx - 5, cy + u, cx + 5, cy + u)
    L.texto(cx - 10, cy + u + 5, "−1", "rotulo", "end")
    # 1 + i y 1 - i
    px, py = cx + u, cy - u
    qx, qy = cx + u, cy + u
    L.linea(cx, cy, px, py, "campana")
    L.linea(px, py, px, cy, "guia")
    L.linea(cx, cy, qx, qy, "guia")
    L.punto(px, py, 5)
    L.punto(qx, qy, 5)
    L.texto(px + 12, py - 4, "r₁ = 1 + i", "valor", "start")
    L.texto(qx + 12, qy + 6, "r₂ = 1 − i", "valor", "start")
    L.texto((cx + px) / 2 - 14, (cy + py) / 2 - 8, "|z| = √2", "valor", "end")
    # arco del ángulo de 45°
    R = 42
    a = math.radians(45)
    L.camino("M %s,%s A %s,%s 0 0 0 %s,%s" % (n(cx + R), n(cy), R, R, n(cx + R * math.cos(a)), n(cy - R * math.sin(a))))
    L.texto(cx + R + 10, cy - 12, "θ = 45° = π/4", "rotulo", "start")
    return L.svg()


G = {
    "u4t-sucesion": sucesion,
    "u4t-complejo": complejo,
}


def main():
    patron = re.compile(r'(<div class="pd-grafico" data-g="([^"]+)">)\s*(<svg.*?</svg>)?', re.S)
    for ruta in sorted(glob.glob(os.path.join(CARPETA, "*.html"))):
        with open(ruta, encoding="utf-8") as f:
            txt = f.read()

        def cambiar(m):
            nombre = m.group(2)
            if nombre not in G:
                return m.group(0)
            return m.group(1) + "\n" + G[nombre]()

        nuevo = patron.sub(cambiar, txt)
        if nuevo != txt:
            with open(ruta, "w", encoding="utf-8", newline="\n") as f:
                f.write(nuevo)
            print("actualizado:", os.path.relpath(ruta, RAIZ))


if __name__ == "__main__":
    main()
