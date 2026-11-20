"""Gráficos de la teoría de la Unidad 9 de PyE (Prueba de hipótesis), calculados y no a ojo.

Uso (desde la raíz del repo):
    python fuentes/pye/graficos_u9.py

En cada fragmento de app/contenido/pye/u9/teoria/, el <svg> que está dentro de
<div class="pd-grafico" data-g="nombre"> se reemplaza por el que arma G["nombre"].
El resto del div (el pie, <p class="pd-pie">) no se toca. Las clases (.campana,
.area, .area.b, .eje, .guia, .corte, .punto, .rotulo, .valor) están en
app/assets/estilos.css y siguen el tema claro/oscuro.

Las curvas: Normal estándar (nu=None) o t de Student con nu grados de libertad,
dibujadas con la misma escala vertical (la t queda un poco más baja y más ancha).
"""
import glob
import math
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CARPETA = os.path.join(RAIZ, "app", "contenido", "pye", "u9", "teoria")

ANCHO, ALTO = 620, 250
XA, XB = 40, 580          # x de la pantalla para z = -4 y z = 4
ZMIN, ZMAX = -4.0, 4.0
YB, ALTURA = 200, 150      # y del eje y alto del pico de la normal


def n(v):
    s = ("%.1f" % v).rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def coma(v, dec=2):
    s = ("%." + str(dec) + "f") % v
    s = s.replace(".", ",").replace("-", "−")
    return s


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def phi(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def tpdf(z, nu):
    c = math.gamma((nu + 1) / 2) / (math.sqrt(nu * math.pi) * math.gamma(nu / 2))
    return c * (1 + z * z / nu) ** (-(nu + 1) / 2)


def dens(z, nu):
    return phi(z) if nu is None else tpdf(z, nu)


def sx(z, zmin=ZMIN, zmax=ZMAX):
    return XA + (z - zmin) / (zmax - zmin) * (XB - XA)


def sy(d):
    return YB - d / phi(0) * ALTURA


class Lienzo:
    def __init__(self, etiqueta, alto=ALTO):
        self.p = []
        self.etiqueta = etiqueta
        self.alto = alto

    def add(self, s):
        self.p.append("  " + s)

    def linea(self, x1, y1, x2, y2, clase="eje"):
        self.add('<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (clase, n(x1), n(y1), n(x2), n(y2)))

    def camino(self, pts, clase="campana", cerrar=False):
        d = "M " + " L ".join("%s,%s" % (n(a), n(b)) for a, b in pts)
        if cerrar:
            d += " Z"
        self.add('<path class="%s" d="%s"/>' % (clase, d))

    def texto(self, x, y, s, clase="rotulo", ancla="middle"):
        self.add('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (clase, n(x), n(y), ancla, esc(s)))

    def punto(self, x, y, r=5):
        self.add('<circle class="punto" cx="%s" cy="%s" r="%s"/>' % (n(x), n(y), n(r)))

    def svg(self):
        cab = '<svg viewBox="0 0 %d %d" role="img" aria-label="%s">' % (ANCHO, self.alto, esc(self.etiqueta))
        return cab + "\n" + "\n".join(self.p) + "\n</svg>"


def curva(nu, a=ZMIN, b=ZMAX, centro=0.0, pasos=160):
    pts = []
    for i in range(pasos + 1):
        z = a + (b - a) * i / pasos
        pts.append((sx(z), sy(dens(z - centro, nu))))
    return pts


def sombra(L, nu, a, b, clase="area", centro=0.0):
    a, b = max(a, ZMIN), min(b, ZMAX)
    if b <= a:
        return
    pts = [(sx(a), YB)] + curva(nu, a, b, centro, 60) + [(sx(b), YB)]
    L.camino(pts, clase, cerrar=True)


def region(etiqueta, nu, tipo, crit, est=None, est_txt=None, crit_txt=None, alfa_txt=None,
           letra="z", centro_txt="0", texto_rech="rechazo"):
    """tipo: 'izq', 'der' o 'bi'. crit: valor crítico positivo. est: estadístico calculado."""
    L = Lienzo(etiqueta)
    if tipo in ("izq", "bi"):
        sombra(L, nu, ZMIN, -crit)
    if tipo in ("der", "bi"):
        sombra(L, nu, crit, ZMAX)
    L.camino(curva(nu))
    L.linea(30, YB, 590, YB)
    L.linea(sx(0), sy(dens(0, nu)), sx(0), YB, "guia")
    L.texto(sx(0), YB + 20, centro_txt)
    cortes = []
    if tipo in ("izq", "bi"):
        cortes.append(-crit)
    if tipo in ("der", "bi"):
        cortes.append(crit)
    for c in cortes:
        L.linea(sx(c), sy(dens(c, nu)) - 12, sx(c), YB, "corte")
        L.texto(sx(c), YB + 20, crit_txt if crit_txt and c > 0 else
                (("−" + crit_txt) if crit_txt and c < 0 else coma(c, 3 if nu else 3).rstrip("0").rstrip(",")))
    # rótulos de las zonas
    if alfa_txt is None:
        alfa_txt = ""
    for c in cortes:
        xz = (ZMIN + c) / 2 - 0.35 if c < 0 else (c + ZMAX) / 2 + 0.35
        xz = max(min(xz, 3.55), -3.55)
        L.texto(sx(xz), YB - 52, texto_rech, "valor")
        if alfa_txt:
            L.texto(sx(xz), YB - 34, alfa_txt)
    L.texto(sx(0), YB - 70, "no se rechaza H₀", "valor")
    if est is not None:
        ev = max(min(est, 3.85), -3.85)
        L.punto(sx(ev), YB)
        txt = est_txt or ("%s = %s" % (letra, coma(est)))
        if ev != est:
            txt += " (más allá)"
        L.texto(sx(ev), YB + 40, txt, "valor")
    return L.svg()


def pvalor(etiqueta, nu, lados, est, p_txt, crit=None, crit_txt=None, letra="z"):
    """Sombrea el área del valor p (clase area b): 'izq', 'der' o 'bi' a partir de est."""
    L = Lienzo(etiqueta)
    a = abs(est)
    if lados == "izq":
        sombra(L, nu, ZMIN, est, "area b")
    elif lados == "der":
        sombra(L, nu, est, ZMAX, "area b")
    else:
        sombra(L, nu, ZMIN, -a, "area b")
        sombra(L, nu, a, ZMAX, "area b")
    L.camino(curva(nu))
    L.linea(30, YB, 590, YB)
    L.linea(sx(0), sy(dens(0, nu)), sx(0), YB, "guia")
    L.texto(sx(0), YB + 20, "0")
    if crit is not None:
        cs = []
        if lados in ("izq", "bi"):
            cs.append(-crit)
        if lados in ("der", "bi"):
            cs.append(crit)
        for c in cs:
            L.linea(sx(c), sy(dens(c, nu)) - 12, sx(c), YB, "guia")
            L.texto(sx(c), YB + 20, ("−" if c < 0 else "") + crit_txt)
    pts = [est] if lados != "bi" else [-a, a]
    for e in pts:
        ev = max(min(e, 3.85), -3.85)
        L.punto(sx(ev), YB)
        L.texto(sx(ev), YB + 40, "%s = %s" % (letra, coma(e)), "valor")
    # rótulo del valor p arriba de la cola
    xs = [max(min((e + (ZMIN if e < 0 else ZMAX)) / 2, 3.4), -3.4) for e in pts]
    for x in xs:
        L.texto(sx(x), YB - 45, p_txt, "valor")
    return L.svg()


def beta(etiqueta):
    """Prueba unilateral izquierda: curva de H0 y curva real corrida 2,4 desvíos a la izquierda."""
    L = Lienzo(etiqueta, alto=285)
    h0 = 0.9              # centro de la curva de H0 (corrida para que entren las dos)
    d = h0 - 2.4          # la media real
    c = h0 - 1.645        # el valor crítico
    sombra(L, None, ZMIN, c, "area", centro=h0)          # alfa
    sombra(L, None, c, ZMAX, "area b", centro=d)         # beta
    L.camino(curva(None, centro=h0))
    L.camino(curva(None, centro=d), "campana angosta")
    L.linea(30, YB, 590, YB)
    L.linea(sx(h0), sy(phi(0)), sx(h0), YB, "guia")
    L.linea(sx(d), sy(phi(0)), sx(d), YB, "guia")
    L.linea(sx(c), sy(phi(0)) - 5, sx(c), YB, "corte")
    L.texto(sx(h0), YB + 20, "μ₀ (lo que dice H₀)")
    L.texto(sx(d), YB + 20, "μ real")
    L.texto(sx(c), YB + 42, "valor crítico")
    L.texto(sx(c) - 22, YB - 8, "α", "valor")
    L.texto(sx(c) + 26, YB - 20, "β", "valor")
    L.texto(sx(h0), sy(phi(0)) - 10, "si H₀ es cierta")
    L.texto(sx(d), sy(phi(0)) - 10, "si la media real es otra")
    L.texto(sx(c) - 10, YB + 70, "← se rechaza H₀", ancla="end")
    L.texto(sx(c) + 10, YB + 70, "no se rechaza H₀ →", ancla="start")
    return L.svg()


def consistente(etiqueta):
    """Distribución de x̄ si H0 es cierta, con un x̄ cerca (consistente) y uno lejos."""
    L = Lienzo(etiqueta, alto=270)
    L.camino(curva(None))
    L.linea(30, YB, 590, YB)
    L.linea(sx(0), sy(phi(0)), sx(0), YB, "guia")
    L.texto(sx(0), YB + 20, "μ₀ = 2000")
    z = 0.53
    L.punto(sx(z), YB)
    L.texto(sx(z) - 6, YB + 42, "x̄ = 2010", ancla="start")
    L.texto(sx(z) - 6, YB + 62, "cerca: consistente", "valor", ancla="start")
    z = 3.2
    L.punto(sx(z), YB)
    L.linea(sx(z), YB - 22, sx(z), YB, "guia")
    L.texto(sx(z) + 8, YB - 50, "x̄ = 2060", ancla="end")
    L.texto(sx(z) + 8, YB - 30, "lejísimos: inconsistente", "valor", ancla="end")
    L.texto(sx(-2.2), sy(phi(1.2)) - 15, "promedios posibles si H₀ es cierta", ancla="middle")
    return L.svg()


def intervalo(etiqueta, li, ls, mu0, xbar, minimo, maximo, marcas, dec=2, unidad=""):
    """Recta con el intervalo [li; ls], la media x̄ y el valor de H0."""
    L = Lienzo(etiqueta, alto=150)
    def X(v):
        return 60 + (v - minimo) / (maximo - minimo) * 500
    y = 80
    L.linea(40, y, 580, y)
    for m in marcas:
        L.linea(X(m), y - 4, X(m), y + 4, "eje")
        L.texto(X(m), y + 22, coma(m, 0) if float(m).is_integer() else coma(m, 1))
    # el intervalo, como una barra gruesa hecha con un área
    L.camino([(X(li), y - 7), (X(ls), y - 7), (X(ls), y + 7), (X(li), y + 7)], "area", cerrar=True)
    L.linea(X(li), y - 18, X(li), y + 18, "corte")
    L.linea(X(ls), y - 18, X(ls), y + 18, "corte")
    L.texto(X(li), y - 26, coma(li, dec))
    L.texto(X(ls), y - 26, coma(ls, dec))
    L.linea(X(xbar), y - 10, X(xbar), y + 10, "guia")
    L.texto(X(xbar), y + 44, "x̄ = " + coma(xbar, dec))
    L.punto(X(mu0), y)
    adentro = li <= mu0 <= ls
    L.texto(X(mu0), y - 46, "μ₀ = %s %s" % (coma(mu0, 0) if float(mu0).is_integer() else coma(mu0, 1),
                                            "(adentro)" if adentro else "(afuera)"), "valor")
    return L.svg()


G = {}

# Sección 1: la idea
G["u9-consistente"] = consistente(
    "Campana de los promedios posibles si H0 es cierta, centrada en 2000; un promedio de 2010 cae cerca y uno de 2060 cae en la punta")

# Sección 2: alfa y beta
G["u9-beta"] = beta(
    "Dos campanas: la de H0 con la cola izquierda alfa sombreada, y la de la media real corrida a la izquierda con el área beta en la zona de no rechazo")

# Sección 3: las tres formas
G["u9-izq"] = region("Prueba unilateral izquierda: región de rechazo a la izquierda de −1,645, con área 0,05",
                     None, "izq", 1.645, crit_txt="1,645", alfa_txt="área α = 0,05")
G["u9-der"] = region("Prueba unilateral derecha: región de rechazo a la derecha de 1,645, con área 0,05",
                     None, "der", 1.645, crit_txt="1,645", alfa_txt="área α = 0,05")
G["u9-bi"] = region("Prueba bilateral: dos regiones de rechazo, a la izquierda de −1,96 y a la derecha de 1,96, con área 0,025 cada una",
                    None, "bi", 1.96, crit_txt="1,96", alfa_txt="α/2 = 0,025")
G["u9-crit-t"] = region("Campana t con 11 grados de libertad: región de rechazo a la izquierda de −2,718, con área 0,01",
                        11, "izq", 2.718, crit_txt="2,718", alfa_txt="área α = 0,01")
G["u9-crit-bi10"] = region("Prueba bilateral al 10 %: regiones de rechazo fuera de −1,645 y 1,645, con 0,05 cada una",
                           None, "bi", 1.645, crit_txt="1,645", alfa_txt="α/2 = 0,05")

# Sección 4: el ejemplo de la cátedra
G["u9-peso"] = region("Prueba bilateral del peso: rechazo fuera de −1,96 y 1,96; el estadístico 3,33 cae en la región de la derecha",
                      None, "bi", 1.96, est=3.33, crit_txt="1,96", alfa_txt="α/2 = 0,025")

# Sección 5: prueba con Z
G["u9-backup"] = region("Prueba unilateral derecha del backup: rechazo a la derecha de 1,645; el estadístico 2 cae adentro",
                        None, "der", 1.645, est=2.0, crit_txt="1,645", alfa_txt="área α = 0,05")
G["u9-f2907"] = region("Prueba unilateral izquierda de las botellas: rechazo a la izquierda de −1,645; el estadístico −2,25 cae adentro",
                       None, "izq", 1.645, est=-2.25, crit_txt="1,645", alfa_txt="área α = 0,05")
G["u9-f1012"] = region("Prueba bilateral de las piezas: rechazo fuera de −1,96 y 1,96; el estadístico −0,51 cae en el medio",
                       None, "bi", 1.96, est=-0.51, crit_txt="1,96", alfa_txt="α/2 = 0,025")
G["u9-f2502"] = region("Prueba unilateral izquierda de la memoria: rechazo a la izquierda de −1,645; el estadístico −2,74 cae adentro",
                       None, "izq", 1.645, est=-2.74, crit_txt="1,645", alfa_txt="área α = 0,05")

# Sección 6: prueba con t
G["u9-baterias"] = region("Campana t con 15 grados de libertad: rechazo fuera de −2,131 y 2,131; el estadístico −2 cae en el medio",
                          15, "bi", 2.131, est=-2.0, crit_txt="2,131", alfa_txt="α/2 = 0,025", letra="t")
G["u9-build"] = region("Campana t con 9 grados de libertad: rechazo a la izquierda de −1,833; el estadístico −2,32 cae adentro",
                       9, "izq", 1.833, est=-2.32, crit_txt="1,833", alfa_txt="área α = 0,05", letra="t")
G["u9-f2611"] = region("Campana t con 14 grados de libertad: rechazo fuera de −2,145 y 2,145; el estadístico −0,37 cae en el medio",
                       14, "bi", 2.145, est=-0.37, crit_txt="2,145", alfa_txt="α/2 = 0,025", letra="t")

# Sección 7: valor p
G["u9-p-backup"] = pvalor("Valor p del backup: el área a la derecha de z = 2, que vale 0,0228",
                          None, "der", 2.0, "p = 0,0228", crit=1.645, crit_txt="1,645")
G["u9-p-peso"] = pvalor("Valor p del peso: las dos colas más allá de −3,33 y 3,33, que suman 0,0008",
                        None, "bi", 3.33, "0,0004", crit=1.96, crit_txt="1,96")
G["u9-p-f2502"] = pvalor("Valor p de la memoria: el área a la izquierda de z = −2,74, que vale 0,0031",
                         None, "izq", -2.74, "p = 0,0031", crit=1.645, crit_txt="1,645")
G["u9-p-baterias"] = pvalor("Valor p de las baterías: las dos colas de la t con 15 grados de libertad más allá de −2 y 2",
                            15, "bi", 2.0, "≈ 0,032", crit=2.131, crit_txt="2,131", letra="t")

# Sección 8: intervalo y prueba bilateral
G["u9-ic-f1012"] = intervalo("Recta con el intervalo de 75,61 a 76,23 y el valor 76 adentro",
                             75.61, 76.23, 76, 75.92, 75.3, 76.5, [75.4, 75.6, 75.8, 76.0, 76.2, 76.4])
G["u9-ic-f2611"] = intervalo("Recta con el intervalo de 491,09 a 540,37 y el valor 520 adentro",
                             491.09, 540.37, 520, 515.73, 480, 550, [480, 490, 500, 510, 520, 530, 540, 550])
G["u9-ic-f2907"] = intervalo("Recta con el intervalo de 352,19 a 354,81 y el valor 355 afuera, a la derecha",
                             352.19, 354.81, 355, 353.5, 351.5, 355.5, [352, 353, 354, 355])
G["u9-ic-peso"] = intervalo("Recta con el intervalo de 68,82 a 71,18 y el valor 68 afuera, a la izquierda",
                            68.82, 71.18, 68, 70, 67.5, 71.5, [68, 69, 70, 71])


def main():
    patron = re.compile(r'(<div class="pd-grafico" data-g="([^"]+)">\s*)<svg.*?</svg>', re.S)
    usados, faltan = set(), set()
    for ruta in sorted(glob.glob(os.path.join(CARPETA, "*.html"))):
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
