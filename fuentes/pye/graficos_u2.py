"""Gráficos de la Unidad 2 de PyE (Estadística descriptiva): app/contenido/pye/u2/.

Rellena cada <div class="pd-grafico" data-g="NOMBRE"> de esos archivos con el SVG calculado acá
(histogramas, polígonos, ojivas, diagramas de caja, tallo y hoja, bastones y escalonados).
Todo sale de los datos: nada se dibuja a ojo. Un mismo gráfico puede aparecer en varios lugares.
Uso, desde la raíz del repo:  python fuentes/pye/graficos_u2.py
"""
import glob
import math
import re

CARPETA = "app/contenido/pye/u2"

# ---------------------------------------------------------------- datos

NICOTINA = [1.24, 2.08, 1.79, 1.58, 1.67, 1.69, 0.72, 2.31, 1.51, 2.55, 1.88, 1.75, 1.37, 1.63,
            1.09, 2.46, 1.47, 1.40, 2.03, 2.09, 0.85, 1.92, 1.70, 1.93, 1.68, 1.64, 1.85, 2.37,
            1.79, 1.82, 2.11, 1.86, 1.64, 1.69, 1.97, 2.17, 1.74, 1.75, 2.28, 1.90]
PARCIAL = [558, 619, 629, 647, 655, 655, 678, 700, 719, 646,
           644, 655, 678, 671, 697, 709, 711, 723, 590, 646]
API = [121, 127, 132, 135, 136, 139, 141, 143, 144, 146, 147, 149, 150, 151, 152, 154, 155, 157,
       158, 159, 161, 163, 164, 166, 168, 172, 175, 178, 183, 189]
PESOS = [84, 99, 71, 64, 65, 80, 70, 70, 56, 66, 89, 60, 65, 79]
ESTATURAS = [185, 180, 173, 168, 175, 183, 184, 174, 164, 169, 205, 161, 177, 174]
NOTAS = [75, 89, 66, 52, 90, 68, 83, 94, 77, 60, 63, 77, 31, 88, 74, 37, 85, 76, 74, 63, 38, 47,
         87, 65, 97, 49, 65, 72, 73, 81, 69, 72, 91, 87, 76, 58, 63, 70, 72, 65]
ERRATAS = [2, 3, 5, 0, 1, 4, 0, 6, 2, 1, 1, 0, 2, 4, 5, 3, 1, 2, 3, 2, 3, 1, 2, 4, 4, 2, 5, 4, 1, 3,
           2, 6, 8, 2, 0, 1, 0, 2, 3, 1, 5, 10, 2, 1, 3, 6, 2, 0, 1, 3]
FALLAS = {0: 4, 1: 7, 2: 5, 3: 3, 4: 1}          # ejemplo de la teoría: fallas por día en 20 días
AUTOS = {0: 20, 1: 40, 2: 30, 3: 10, 4: 5, 5: 1}  # ejercicio 10 de la guía


def num(v, dec=None):
    """Número con coma decimal. dec=None: hasta 4 cifras significativas."""
    t = f"{v:.4g}" if dec is None else f"{v:.{dec}f}"
    return t.replace(".", ",")


def cuartil(datos, k, den=4):
    """Convención de la cátedra (hoja de fórmulas y Resultados de la guía).

    n impar: lugar k(n+1)/den; n par: lugar kn/den y, si es entero, el promedio con el siguiente.
    Si el lugar da con coma, se toma el dato del lugar siguiente (redondeo para arriba)."""
    d = sorted(datos)
    n = len(d)
    p = k * (n + 1) / den if n % 2 else k * n / den
    if abs(p - round(p)) < 1e-9:
        p = int(round(p))
        return d[p - 1] if n % 2 else (d[p - 1] + d[p]) / 2
    return d[math.ceil(p) - 1]


def frecuencias(datos, lims):
    k = len(lims) - 1
    return [sum(1 for x in datos if lims[i] <= x < lims[i + 1] or (i == k - 1 and x == lims[-1]))
            for i in range(k)]


# ---------------------------------------------------------------- piezas

def eje_y(s, x, y0, y1, vmax, paso, Y, sufijo=""):
    s.append(f'  <line class="eje" x1="{x}" y1="{y0}" x2="{x}" y2="{y1}"/>')
    v = 0
    while v <= vmax + 1e-9:
        s.append(f'  <line class="eje" x1="{x - 5}" y1="{Y(v):.1f}" x2="{x}" y2="{Y(v):.1f}"/>')
        s.append(f'  <text class="rotulo" x="{x - 9}" y="{Y(v) + 4:.1f}" text-anchor="end">{num(v)}{sufijo}</text>')
        v += paso


def histograma(lims, fa, titulo_x, poligono=True, paso_y=5, marcar=None, cruz=False, aria=""):
    """Histograma de frecuencias absolutas (eje izq.) con fr a la derecha y el polígono."""
    n, k = sum(fa), len(fa)
    A = lims[1] - lims[0]
    x0, x1, y0, y1 = 70, 560, 220, 40
    lo, hi = lims[0] - A, lims[-1] + A
    X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    vmax = math.ceil(max(fa) / paso_y) * paso_y
    Y = lambda v: y0 - v / vmax * (y0 - y1)
    s = [f'<svg viewBox="0 0 620 280" role="img" aria-label="{aria}">']
    for i in range(k):
        clase = "barra marcada" if marcar == i else "barra"
        s.append(f'  <rect class="{clase}" x="{X(lims[i]):.1f}" y="{Y(fa[i]):.1f}" '
                 f'width="{X(lims[i + 1]) - X(lims[i]):.1f}" height="{y0 - Y(fa[i]):.1f}"/>')
        s.append(f'  <text class="valor" x="{(X(lims[i]) + X(lims[i + 1])) / 2:.1f}" y="{Y(fa[i]) - 6:.1f}" '
                 f'text-anchor="middle">{fa[i]}</text>')
    if cruz and marcar is not None:
        i = marcar
        fp = fa[i - 1] if i > 0 else 0
        fs = fa[i + 1] if i < k - 1 else 0
        xa, xb = X(lims[i]), X(lims[i + 1])
        s.append(f'  <line class="corte" x1="{xa:.1f}" y1="{Y(fa[i]):.1f}" x2="{xb:.1f}" y2="{Y(fs):.1f}"/>')
        s.append(f'  <line class="corte" x1="{xb:.1f}" y1="{Y(fa[i]):.1f}" x2="{xa:.1f}" y2="{Y(fp):.1f}"/>')
        d1, d2 = fa[i] - fp, fa[i] - fs
        mo = lims[i] + A * d1 / (d1 + d2)
        ycr = Y(fa[i]) + (Y(fs) - Y(fa[i])) * (X(mo) - xa) / (xb - xa)
        s.append(f'  <line class="guia" x1="{X(mo):.1f}" y1="{ycr:.1f}" x2="{X(mo):.1f}" y2="{y0}"/>')
        s.append(f'  <text class="valor" x="{X(mo):.1f}" y="{y0 + 34}" text-anchor="middle">Mo = {num(mo)}</text>')
    if poligono:
        pts = [(lims[0] - A / 2, 0)] + [((lims[i] + lims[i + 1]) / 2, fa[i]) for i in range(k)] + [(lims[-1] + A / 2, 0)]
        s.append('  <polyline class="campana" points="' + " ".join(f"{X(a):.1f},{Y(b):.1f}" for a, b in pts) + '"/>')
        for a, b in pts:
            s.append(f'  <circle class="punto" cx="{X(a):.1f}" cy="{Y(b):.1f}" r="3.5"/>')
    s.append(f'  <line class="eje" x1="{x0}" y1="{y0}" x2="{x1 + 10}" y2="{y0}"/>')
    eje_y(s, x0, y0, y1 - 10, vmax, paso_y, Y)
    s.append(f'  <text class="rotulo" x="{x0 - 30}" y="{y1 - 18}" text-anchor="middle">fa</text>')
    # escala de fr a la derecha
    s.append(f'  <line class="eje" x1="{x1 + 10}" y1="{y0}" x2="{x1 + 10}" y2="{y1 - 10}"/>')
    v = 0
    while v <= vmax + 1e-9:
        s.append(f'  <text class="rotulo" x="{x1 + 16}" y="{Y(v) + 4:.1f}">{num(v / n, 3)}</text>')
        v += paso_y
    s.append(f'  <text class="rotulo" x="{x1 + 30}" y="{y1 - 18}" text-anchor="middle">fr</text>')
    for v in lims:
        s.append(f'  <text class="rotulo" x="{X(v):.1f}" y="{y0 + 17}" text-anchor="middle">{num(v)}</text>')
    s.append(f'  <text class="rotulo" x="{(x0 + x1) / 2:.0f}" y="{y0 + 54}" text-anchor="middle">{titulo_x}</text>')
    s.append('</svg>')
    return "\n".join(s)


def ojiva(lims, fa, titulo_x, marcas=((0.25, "Q1"), (0.5, "Me"), (0.75, "Q3")), aria="", dec=3):
    """Histograma de Fr y la ojiva (une los límites superiores con su Fr)."""
    n, k = sum(fa), len(fa)
    A = lims[1] - lims[0]
    Fr, c = [], 0
    for f in fa:
        c += f
        Fr.append(c / n)
    x0, x1, y0, y1 = 70, 560, 230, 40
    lo, hi = lims[0] - A / 2, lims[-1] + A / 2
    X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    Y = lambda v: y0 - v * (y0 - y1)
    s = [f'<svg viewBox="0 0 620 290" role="img" aria-label="{aria}">']
    for i in range(k):
        s.append(f'  <rect class="barra" x="{X(lims[i]):.1f}" y="{Y(Fr[i]):.1f}" '
                 f'width="{X(lims[i + 1]) - X(lims[i]):.1f}" height="{y0 - Y(Fr[i]):.1f}"/>')
    pts = [(lims[0], 0)] + [(lims[i + 1], Fr[i]) for i in range(k)]
    for p, rot in marcas:
        i = next(i for i in range(k) if Fr[i] >= p - 1e-12)
        Fp = Fr[i - 1] if i > 0 else 0
        v = lims[i] + (p - Fp) / (Fr[i] - Fp) * A
        s.append(f'  <line class="guia" x1="{x0}" y1="{Y(p):.1f}" x2="{X(v):.1f}" y2="{Y(p):.1f}"/>')
        s.append(f'  <line class="guia" x1="{X(v):.1f}" y1="{Y(p):.1f}" x2="{X(v):.1f}" y2="{y0}"/>')
        s.append(f'  <text class="valor" x="{X(v):.1f}" y="{y0 + 36}" text-anchor="middle">{rot}</text>')
        s.append(f'  <text class="rotulo" x="{X(v):.1f}" y="{y0 + 52}" text-anchor="middle">{num(v, dec)}</text>')
    s.append('  <polyline class="campana" points="' + " ".join(f"{X(a):.1f},{Y(b):.1f}" for a, b in pts) + '"/>')
    for a, b in pts:
        s.append(f'  <circle class="punto" cx="{X(a):.1f}" cy="{Y(b):.1f}" r="3.5"/>')
    s.append(f'  <line class="eje" x1="{x0}" y1="{y0}" x2="{x1 + 10}" y2="{y0}"/>')
    s.append(f'  <line class="eje" x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1 - 10}"/>')
    for v in (0, 0.25, 0.5, 0.75, 1):
        s.append(f'  <line class="eje" x1="{x0 - 5}" y1="{Y(v):.1f}" x2="{x0}" y2="{Y(v):.1f}"/>')
        s.append(f'  <text class="rotulo" x="{x0 - 9}" y="{Y(v) + 4:.1f}" text-anchor="end">{num(v)}</text>')
    s.append(f'  <text class="rotulo" x="{x0 - 30}" y="{y1 - 18}" text-anchor="middle">Fr</text>')
    for v in lims:
        s.append(f'  <text class="rotulo" x="{X(v):.1f}" y="{y0 + 17}" text-anchor="middle">{num(v)}</text>')
    s.append(f'  <text class="rotulo" x="{x1 + 10}" y="{y0 + 52}" text-anchor="end">{titulo_x}</text>')
    s.append('</svg>')
    return "\n".join(s)


def caja(datos, lo, hi, paso, unidad, aria="", dec=None, media=True):
    """Diagrama de caja horizontal, como el de la cátedra: bigotes hasta el último dato dentro de
    las vallas, atípicos con una cruz y la media con una x dentro de la caja."""
    d = sorted(datos)
    q1, q2, q3 = cuartil(d, 1), cuartil(d, 2), cuartil(d, 3)
    iq = q3 - q1
    vi, vs = q1 - 1.5 * iq, q3 + 1.5 * iq
    adentro = [x for x in d if vi <= x <= vs]
    atip = [x for x in d if x < vi or x > vs]
    m = sum(d) / len(d)
    x0, x1 = 50, 570
    X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    yc, h = 105, 56
    s = [f'<svg viewBox="0 0 620 250" role="img" aria-label="{aria}">']
    for v in (vi, vs):
        if lo <= v <= hi:
            s.append(f'  <line class="guia" x1="{X(v):.1f}" y1="{yc - 62}" x2="{X(v):.1f}" y2="{yc + 62}"/>')
            s.append(f'  <text class="rotulo" x="{X(v):.1f}" y="{yc - 68}" text-anchor="middle">valla {f"{v:.6g}".replace(".", ",")}</text>')
    s.append(f'  <rect class="area suave" x="{X(q1):.1f}" y="{yc - h / 2}" width="{X(q3) - X(q1):.1f}" height="{h}"/>')
    s.append(f'  <rect x="{X(q1):.1f}" y="{yc - h / 2}" width="{X(q3) - X(q1):.1f}" height="{h}" fill="none" stroke="currentColor" stroke-width="2"/>')
    s.append(f'  <line x1="{X(q2):.1f}" y1="{yc - h / 2}" x2="{X(q2):.1f}" y2="{yc + h / 2}" stroke="currentColor" stroke-width="3"/>')
    for a, b in ((adentro[0], q1), (q3, adentro[-1])):
        s.append(f'  <line x1="{X(a):.1f}" y1="{yc}" x2="{X(b):.1f}" y2="{yc}" stroke="currentColor" stroke-width="2"/>')
    for v in (adentro[0], adentro[-1]):
        s.append(f'  <line x1="{X(v):.1f}" y1="{yc - 14}" x2="{X(v):.1f}" y2="{yc + 14}" stroke="currentColor" stroke-width="2"/>')
    if media:
        xm = X(m)
        s.append(f'  <line class="corte" x1="{xm - 6:.1f}" y1="{yc - 6}" x2="{xm + 6:.1f}" y2="{yc + 6}"/>')
        s.append(f'  <line class="corte" x1="{xm + 6:.1f}" y1="{yc - 6}" x2="{xm - 6:.1f}" y2="{yc + 6}"/>')
    vistos = {}
    for v in atip:
        k = vistos.get(v, 0)
        vistos[v] = k + 1
        xa, ya = X(v), yc - 14 * k
        s.append(f'  <line class="corte" x1="{xa - 6:.1f}" y1="{ya - 6}" x2="{xa + 6:.1f}" y2="{ya + 6}"/>')
        s.append(f'  <line class="corte" x1="{xa + 6:.1f}" y1="{ya - 6}" x2="{xa - 6:.1f}" y2="{ya + 6}"/>')
    for j, v in enumerate(sorted(set(atip))):
        s.append(f'  <text class="valor" x="{X(v):.1f}" y="{yc + 30 + (j % 2) * 18}" text-anchor="middle">{num(v, dec)}</text>')
    abajo = [(q1, f"Q1 = {num(q1, dec)}", "end", -4), (q3, f"Q3 = {num(q3, dec)}", "start", 4)]
    for v, t, anc, dx in abajo:
        s.append(f'  <text class="rotulo" x="{X(v) + dx:.1f}" y="{yc + h / 2 + 17}" text-anchor="{anc}">{t}</text>')
    s.append(f'  <text class="rotulo" x="{X(q2):.1f}" y="{yc - h / 2 - 6}" text-anchor="middle">Me = {num(q2, dec)}</text>')
    for v in (adentro[0], adentro[-1]):
        s.append(f'  <text class="rotulo" x="{X(v):.1f}" y="{yc - 20}" text-anchor="middle">{num(v, dec)}</text>')
    ye = 205
    s.append(f'  <line class="eje" x1="{x0}" y1="{ye}" x2="{x1}" y2="{ye}"/>')
    v = lo
    while v <= hi + 1e-9:
        s.append(f'  <line class="eje" x1="{X(v):.1f}" y1="{ye - 5}" x2="{X(v):.1f}" y2="{ye + 5}"/>')
        s.append(f'  <text class="rotulo" x="{X(v):.1f}" y="{ye + 21}" text-anchor="middle">{num(v)}</text>')
        v += paso
    s.append(f'  <text class="rotulo" x="{x1}" y="{ye + 40}" text-anchor="end">{unidad}</text>')
    s.append('</svg>')
    return "\n".join(s)


def tallo_y_hoja(filas, aria="", titulo=""):
    """filas: lista de (tallo, [hojas como texto])."""
    alto = 40 + 26 * len(filas)
    s = [f'<svg viewBox="0 0 620 {alto}" role="img" aria-label="{aria}">']
    if titulo:
        s.append(f'  <text class="rotulo" x="20" y="18">{titulo}</text>')
    y = 44
    xl = 90
    for tallo, hojas in filas:
        s.append(f'  <text class="valor" x="{xl - 14}" y="{y}" text-anchor="end">{tallo}</text>')
        paso = min(22, 500 / max(1, len(hojas)))
        for j, h in enumerate(hojas):
            s.append(f'  <text class="rotulo" x="{xl + 14 + j * paso:.1f}" y="{y}">{h}</text>')
        y += 26
    s.append(f'  <line class="eje" x1="{xl}" y1="26" x2="{xl}" y2="{y - 16}"/>')
    s.append('</svg>')
    return "\n".join(s)


def tallo_nicotina(ordenado):
    datos = sorted(NICOTINA) if ordenado else NICOTINA
    tallos = [("0", 0.0, 0.5), ("0+", 0.5, 1.0), ("1", 1.0, 1.5), ("1+", 1.5, 2.0), ("2", 2.0, 2.5), ("2+", 2.5, 3.0)]
    filas = []
    for t, a, b in tallos:
        filas.append((t, [f"{round(x * 100) % 100:02d}" for x in datos if a <= x < b - 1e-9]))
    tit = "tallo = unidad del mg · hoja = los dos decimales (1+ | 51 es 1,51 mg)"
    return tallo_y_hoja(filas, f"Tallo y hoja {'ordenado' if ordenado else 'original'} de la nicotina", tit)


def tallo_enteros(datos, div, ordenado=True, tit="", aria=""):
    datos = sorted(datos) if ordenado else datos
    tallos = range(min(datos) // div, max(datos) // div + 1)
    filas = [(str(t), [str(x % div) for x in datos if x // div == t]) for t in tallos]
    return tallo_y_hoja(filas, aria, tit)


def bastones(tabla, titulo_x, relativa=True, aria=""):
    xs = sorted(tabla)
    n = sum(tabla.values())
    x0, x1, y0, y1 = 70, 560, 210, 40
    lo, hi = xs[0] - 1, xs[-1] + 1
    X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    fmax = max(tabla.values()) / n
    top = math.ceil(fmax * 10) / 10 if relativa else max(tabla.values())
    Y = lambda v: y0 - v / top * (y0 - y1)
    s = [f'<svg viewBox="0 0 620 260" role="img" aria-label="{aria}">']
    for x in xs:
        f = tabla[x] / n
        s.append(f'  <line class="corte" x1="{X(x):.1f}" y1="{y0}" x2="{X(x):.1f}" y2="{Y(f):.1f}" stroke-width="3"/>')
        s.append(f'  <circle class="punto" cx="{X(x):.1f}" cy="{Y(f):.1f}" r="4.5"/>')
        s.append(f'  <text class="valor" x="{X(x):.1f}" y="{Y(f) - 9:.1f}" text-anchor="middle">{num(f, 2)}</text>')
    for x in range(lo + 1, hi):
        s.append(f'  <text class="rotulo" x="{X(x):.1f}" y="{y0 + 18}" text-anchor="middle">{x}</text>')
    s.append(f'  <line class="eje" x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}"/>')
    paso = 0.1 if top <= 0.5 else 0.2
    eje_y(s, x0, y0, y1 - 10, top, paso, Y)
    s.append(f'  <text class="rotulo" x="{x0 - 30}" y="{y1 - 18}" text-anchor="middle">fr</text>')
    s.append(f'  <text class="rotulo" x="{(x0 + x1) / 2:.0f}" y="{y0 + 42}" text-anchor="middle">{titulo_x}</text>')
    s.append('</svg>')
    return "\n".join(s)


def escalonado(tabla, titulo_x, aria=""):
    xs = sorted(tabla)
    n = sum(tabla.values())
    x0, x1, y0, y1 = 70, 560, 210, 40
    lo, hi = xs[0] - 1, xs[-1] + 1
    X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    Y = lambda v: y0 - v * (y0 - y1)
    s = [f'<svg viewBox="0 0 620 260" role="img" aria-label="{aria}">']
    c = 0
    s.append(f'  <line class="corte" x1="{x0}" y1="{y0}" x2="{X(xs[0]):.1f}" y2="{y0}" stroke-width="2.5"/>')
    for j, x in enumerate(xs):
        c += tabla[x]
        F = c / n
        fin = X(xs[j + 1]) if j + 1 < len(xs) else x1
        s.append(f'  <line class="corte" x1="{X(x):.1f}" y1="{Y(F):.1f}" x2="{fin:.1f}" y2="{Y(F):.1f}" stroke-width="2.5"/>')
        s.append(f'  <circle class="punto" cx="{X(x):.1f}" cy="{Y(F):.1f}" r="4.5"/>')
        if j + 1 < len(xs):
            s.append(f'  <circle cx="{fin:.1f}" cy="{Y(F):.1f}" r="4.5" fill="none" stroke="currentColor" stroke-width="1.5"/>')
        s.append(f'  <text class="rotulo" x="{X(x) + 4:.1f}" y="{Y(F) - 8:.1f}">{num(F, 2)}</text>')
    for x in range(lo + 1, hi):
        s.append(f'  <text class="rotulo" x="{X(x):.1f}" y="{y0 + 18}" text-anchor="middle">{x}</text>')
    s.append(f'  <line class="eje" x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}"/>')
    eje_y(s, x0, y0, y1 - 10, 1, 0.25, Y)
    s.append(f'  <text class="rotulo" x="{x0 - 30}" y="{y1 - 18}" text-anchor="middle">Fr</text>')
    s.append(f'  <text class="rotulo" x="{(x0 + x1) / 2:.0f}" y="{y0 + 42}" text-anchor="middle">{titulo_x}</text>')
    s.append('</svg>')
    return "\n".join(s)


def recta_chebyshev(m, S, p125, p875, lo, hi, unidad, dec=3, aria=""):
    """Recta con x̄ ± 2S y los percentiles 12,5 y 87,5: si los percentiles quedan adentro, la
    dispersión es pequeña (el 75 % del medio está dentro de los 2 desvíos)."""
    x0, x1 = 50, 570
    X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    y = 120
    s = [f'<svg viewBox="0 0 620 200" role="img" aria-label="{aria}">']
    s.append(f'  <rect class="area suave" x="{X(m - 2 * S):.1f}" y="{y - 34}" width="{X(m + 2 * S) - X(m - 2 * S):.1f}" height="34"/>')
    s.append(f'  <rect class="area b" opacity=".35" x="{X(p125):.1f}" y="{y - 20}" width="{X(p875) - X(p125):.1f}" height="20"/>')
    s.append(f'  <text class="rotulo" x="{(X(p125) + X(p875)) / 2:.1f}" y="{y - 26}" text-anchor="middle">el 75 % del medio</text>')
    s.append(f'  <line class="eje" x1="{x0}" y1="{y}" x2="{x1}" y2="{y}"/>')
    for v, t, cl in ((m - 2 * S, "x̄ − 2S", "rotulo"), (m, "x̄", "rotulo"), (m + 2 * S, "x̄ + 2S", "rotulo")):
        s.append(f'  <line class="eje" x1="{X(v):.1f}" y1="{y - 40}" x2="{X(v):.1f}" y2="{y + 6}"/>')
        s.append(f'  <text class="{cl}" x="{X(v):.1f}" y="{y - 46}" text-anchor="middle">{t} = {num(v, dec)}</text>')
    for v, t in ((p125, "P12,5"), (p875, "P87,5")):
        s.append(f'  <line class="corte" x1="{X(v):.1f}" y1="{y - 20}" x2="{X(v):.1f}" y2="{y + 6}" stroke-width="2.5"/>')
        s.append(f'  <text class="valor" x="{X(v):.1f}" y="{y + 26}" text-anchor="middle">{t}</text>')
        s.append(f'  <text class="rotulo" x="{X(v):.1f}" y="{y + 42}" text-anchor="middle">{num(v, dec)}</text>')
    s.append(f'  <text class="rotulo" x="{x1}" y="{y + 62}" text-anchor="end">{unidad}</text>')
    s.append('</svg>')
    return "\n".join(s)


def curvas_forma(tipo):
    """Tres curvas lado a lado: asimetría (izq., simétrica, der.) o curtosis (platí, meso, lepto)."""
    s = [f'<svg viewBox="0 0 620 220" role="img" aria-label="Formas de una distribución: {tipo}">']
    paneles = [40, 230, 420]
    w, base, alto = 160, 150, 105
    if tipo == "asimetria":
        def dens(a, t):     # beta(a, b) en [0, 1]
            b = 7 - a
            return t ** (a - 1) * (1 - t) ** (b - 1)
        params = [(5, "cola a la izquierda", "SK < 0", "media < mediana < moda"),
                  (3.5, "simétrica", "SK = 0", "media = mediana = moda"),
                  (2, "cola a la derecha", "SK > 0", "moda < mediana < media")]
        for x0, (a, tit, sk, orden) in zip(paneles, params):
            pts = [(i / 200, dens(a, i / 200)) for i in range(201)]
            top = max(p[1] for p in pts)
            P = lambda t, f: (x0 + t * w, base - f / top * alto)
            s.append('  <polyline class="campana" points="' + " ".join(f"{P(t, f)[0]:.1f},{P(t, f)[1]:.1f}" for t, f in pts) + '"/>')
            s.append(f'  <line class="eje" x1="{x0 - 5}" y1="{base}" x2="{x0 + w + 5}" y2="{base}"/>')
            # moda, media de la beta
            moda = (a - 1) / (7 - 2)
            media = a / 7
            for v, cl in ((moda, "guia"), (media, "corte")):
                X, Yv = P(v, dens(a, v))
                s.append(f'  <line class="{cl}" x1="{X:.1f}" y1="{Yv:.1f}" x2="{X:.1f}" y2="{base}"/>')
            s.append(f'  <text class="valor" x="{x0 + w / 2}" y="{base + 22}" text-anchor="middle">{sk}</text>')
            s.append(f'  <text class="rotulo" x="{x0 + w / 2}" y="{base + 40}" text-anchor="middle">{tit}</text>')
            s.append(f'  <text class="rotulo" x="{x0 + w / 2}" y="{base + 58}" text-anchor="middle">{orden}</text>')
        s.append('  <text class="rotulo" x="310" y="22" text-anchor="middle">línea punteada: la moda (el pico) · línea llena: la media</text>')
    else:
        params = [("platicúrtica", "Cu < 0", "achatada"), ("mesocúrtica", "Cu = 0", "como la normal"),
                  ("leptocúrtica", "Cu > 0", "puntiaguda")]
        for x0, (tit, cu, desc) in zip(paneles, params):
            pts = []
            for i in range(201):
                z = -3.2 + 6.4 * i / 200
                if tit == "platicúrtica":
                    f = math.exp(-abs(z / 1.9) ** 4)
                elif tit == "mesocúrtica":
                    f = math.exp(-z * z / 2)
                else:
                    f = math.exp(-abs(z) * 1.7)
                pts.append((x0 + i / 200 * w, base - f * alto))
            s.append('  <polyline class="campana" points="' + " ".join(f"{a:.1f},{b:.1f}" for a, b in pts) + '"/>')
            s.append(f'  <line class="eje" x1="{x0 - 5}" y1="{base}" x2="{x0 + w + 5}" y2="{base}"/>')
            s.append(f'  <text class="valor" x="{x0 + w / 2}" y="{base + 22}" text-anchor="middle">{cu}</text>')
            s.append(f'  <text class="rotulo" x="{x0 + w / 2}" y="{base + 40}" text-anchor="middle">{tit}</text>')
            s.append(f'  <text class="rotulo" x="{x0 + w / 2}" y="{base + 58}" text-anchor="middle">{desc}</text>')
    s.append('</svg>')
    return "\n".join(s)


def cajas_ej9():
    """Las cuatro cajas del ejercicio 9, con los valores leídos del gráfico de Minitab de la guía."""
    grupos = [("arena gruesa", 48, 52, 57, 64.5, 80, []), ("arena fina", 67, 71.5, 74.5, 80, 92, [96]),
              ("grava", 40, 53.5, 56.5, 64, 75, [88, 95]), ("gravilla", 62, 70.5, 79, 85.5, 99, [])]
    y0, y1, v0, v1 = 250, 30, 40, 100
    Y = lambda v: y0 - (v - v0) / (v1 - v0) * (y0 - y1)
    s = ['<svg viewBox="0 0 620 300" role="img" aria-label="Cuatro diagramas de caja de la absorción de humedad por agregado">']
    s.append(f'  <line class="eje" x1="70" y1="{y0}" x2="70" y2="{y1 - 6}"/>')
    for v in range(40, 101, 10):
        s.append(f'  <line class="eje" x1="64" y1="{Y(v):.1f}" x2="70" y2="{Y(v):.1f}"/>')
        s.append(f'  <text class="rotulo" x="58" y="{Y(v) + 4:.1f}" text-anchor="end">{v}</text>')
    s.append(f'  <text class="rotulo" x="22" y="{(y0 + y1) / 2:.0f}" text-anchor="middle" transform="rotate(-90 22 {(y0 + y1) / 2:.0f})">absorción (%)</text>')
    for j, (nom, mn, q1, me, q3, mx, at) in enumerate(grupos):
        cx, w = 145 + j * 125, 54
        s.append(f'  <line x1="{cx}" y1="{Y(mn):.1f}" x2="{cx}" y2="{Y(q1):.1f}" stroke="currentColor" stroke-width="1.5"/>')
        s.append(f'  <line x1="{cx}" y1="{Y(q3):.1f}" x2="{cx}" y2="{Y(mx):.1f}" stroke="currentColor" stroke-width="1.5"/>')
        s.append(f'  <rect class="area suave" x="{cx - w / 2}" y="{Y(q3):.1f}" width="{w}" height="{Y(q1) - Y(q3):.1f}"/>')
        s.append(f'  <rect x="{cx - w / 2}" y="{Y(q3):.1f}" width="{w}" height="{Y(q1) - Y(q3):.1f}" fill="none" stroke="currentColor" stroke-width="1.8"/>')
        s.append(f'  <line x1="{cx - w / 2}" y1="{Y(me):.1f}" x2="{cx + w / 2}" y2="{Y(me):.1f}" stroke="currentColor" stroke-width="3"/>')
        for v in at:
            s.append(f'  <line class="corte" x1="{cx - 5}" y1="{Y(v) - 5:.1f}" x2="{cx + 5}" y2="{Y(v) + 5:.1f}"/>')
            s.append(f'  <line class="corte" x1="{cx + 5}" y1="{Y(v) - 5:.1f}" x2="{cx - 5}" y2="{Y(v) + 5:.1f}"/>')
            s.append(f'  <text class="rotulo" x="{cx + 10}" y="{Y(v) + 4:.1f}">{v}</text>')
        s.append(f'  <text class="rotulo" x="{cx}" y="{y0 + 22}" text-anchor="middle">{nom}</text>')
    s.append('</svg>')
    return "\n".join(s)


# ---------------------------------------------------------------- catálogo

LIM_NIC = [0.7, 1.0, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8]
FA_NIC = frecuencias(NICOTINA, LIM_NIC)
LIM_API = list(range(120, 191, 10))
FA_API = frecuencias(API, LIM_API)
LIM_NOTAS = list(range(30, 101, 10))
FA_NOTAS = frecuencias(NOTAS, LIM_NOTAS)
LIM_GB = [0, 2, 4, 6, 8, 10]
FA_GB = [6, 9, 23, 12, 10]


def _m_s(d):
    n = len(d)
    m = sum(d) / n
    return m, math.sqrt(sum((x - m) ** 2 for x in d) / (n - 1))


def _cheb_nic():
    m, S = _m_s(NICOTINA)
    d = sorted(NICOTINA)
    return recta_chebyshev(m, S, d[4], d[34], 0.8, 2.8, "mg", aria="Chebyshev con la nicotina")


def _cheb_parcial():
    m, S = _m_s(PARCIAL)
    d = sorted(PARCIAL)
    return recta_chebyshev(m, S, d[2], d[17], 560, 760, "ppm", dec=1, aria="Chebyshev con el contaminante")


def _cheb_notas():
    return recta_chebyshev(70.75, math.sqrt(255.8333333), 50, 88.5714, 30, 110, "puntos", dec=2,
                           aria="Chebyshev con las notas agrupadas")


GRAFICOS = {
    "u2-tallo-nicotina-original": lambda: tallo_nicotina(False),
    "u2-tallo-nicotina": lambda: tallo_nicotina(True),
    "u2-tallo-parcial": lambda: tallo_enteros(PARCIAL, 10, tit="tallo = las dos primeras cifras · hoja = la última (64 | 4 es 644 ppm)",
                                              aria="Tallo y hoja del contaminante"),
    "u2-hist-nicotina": lambda: histograma(LIM_NIC, FA_NIC, "contenido de nicotina (mg)",
                                           aria="Histograma y polígono de la nicotina"),
    "u2-moda-nicotina": lambda: histograma(LIM_NIC, FA_NIC, "contenido de nicotina (mg)", poligono=False, marcar=3, cruz=True,
                                           aria="Histograma de la nicotina con la construcción de la moda"),
    "u2-ojiva-nicotina": lambda: ojiva(LIM_NIC, FA_NIC, "mg", aria="Ojiva de la nicotina con Q1, mediana y Q3"),
    "u2-hist-api": lambda: histograma(LIM_API, FA_API, "tiempo de respuesta (ms)", paso_y=2,
                                      aria="Histograma y polígono de los tiempos de respuesta"),
    "u2-moda-api": lambda: histograma(LIM_API, FA_API, "tiempo de respuesta (ms)", poligono=False, paso_y=2, marcar=3, cruz=True,
                                      aria="Histograma de los tiempos con la construcción de la moda"),
    "u2-ojiva-api": lambda: ojiva(LIM_API, FA_API, "ms", aria="Ojiva de los tiempos de respuesta", dec=2),
    "u2-caja-nicotina": lambda: caja(NICOTINA, 0.6, 2.8, 0.2, "mg", aria="Diagrama de caja de la nicotina"),
    "u2-caja-parcial": lambda: caja(PARCIAL, 540, 800, 20, "ppm", aria="Diagrama de caja del contaminante"),
    "u2-bastones-fallas": lambda: bastones(FALLAS, "fallas por día", aria="Diagrama de bastones de las fallas"),
    "u2-escalon-fallas": lambda: escalonado(FALLAS, "fallas por día", aria="Gráfico escalonado de las fallas"),
    "u2-asimetria": lambda: curvas_forma("asimetria"),
    "u2-curtosis": lambda: curvas_forma("curtosis"),
    "u2-cheb-nicotina": _cheb_nic,
    "u2-cheb-parcial": _cheb_parcial,
    # práctica
    "u2-ej1-tallo-pesos": lambda: tallo_enteros(PESOS, 10, tit="tallo = decenas · hoja = unidades (8 | 4 es 84 kg)", aria="Tallo y hoja de los pesos"),
    "u2-ej1-tallo-estaturas": lambda: tallo_enteros(ESTATURAS, 10, tit="tallo = las dos primeras cifras · hoja = la última (18 | 5 es 185 cm)", aria="Tallo y hoja de las estaturas"),
    "u2-ej5-tallo": lambda: tallo_enteros(NOTAS, 10, tit="tallo = decenas · hoja = unidades (7 | 5 es 75 puntos)", aria="Tallo y hoja de los puntajes"),
    "u2-ej5-hist": lambda: histograma(LIM_NOTAS, FA_NOTAS, "puntaje", paso_y=2, aria="Histograma y polígono de los puntajes"),
    "u2-ej5-moda": lambda: histograma(LIM_NOTAS, FA_NOTAS, "puntaje", poligono=False, paso_y=2, marcar=4, cruz=True,
                                      aria="Histograma de los puntajes con la construcción de la moda"),
    "u2-ej5-ojiva": lambda: ojiva(LIM_NOTAS, FA_NOTAS, "puntaje", aria="Histograma de frecuencias acumuladas y ojiva de los puntajes", dec=2),
    "u2-ej5-cheb": _cheb_notas,
    "u2-ej5-caja": lambda: caja(NOTAS, 20, 110, 10, "puntaje", aria="Diagrama de caja de los puntajes"),
    "u2-ej6-hist": lambda: histograma(LIM_GB, FA_GB, "consumo mensual (Gb)", paso_y=5, marcar=2, cruz=True,
                                      aria="Histograma y polígono del consumo de datos, con la moda"),
    "u2-ej7-bastones": lambda: bastones({k: ERRATAS.count(k) for k in set(ERRATAS)}, "erratas por página", aria="Bastones de las erratas"),
    "u2-ej7-escalon": lambda: escalonado({k: ERRATAS.count(k) for k in set(ERRATAS)}, "erratas por página", aria="Escalonado de las erratas"),
    "u2-ej9-cajas": cajas_ej9,
    "u2-ej10-bastones": lambda: bastones(AUTOS, "autos en 10 minutos", aria="Bastones de los autos"),
    "u2-ej10-escalon": lambda: escalonado(AUTOS, "autos en 10 minutos", aria="Escalonado de los autos"),
}


def main():
    usados = set()
    for ruta in glob.glob(f"{CARPETA}/**/*.html", recursive=True):
        texto = open(ruta, encoding="utf-8").read()
        nuevo = texto
        for nombre, fn in GRAFICOS.items():
            patron = re.compile(r'(<div class="pd-grafico" data-g="' + nombre + r'">)\s*(?:<svg.*?</svg>\s*)?', re.S)
            if patron.search(nuevo):
                usados.add(nombre)
                svg = fn()
                nuevo = patron.sub(lambda m: m.group(1) + "\n" + svg + "\n", nuevo)
        if nuevo != texto:
            open(ruta, "w", encoding="utf-8", newline="\n").write(nuevo)
            print("actualizado", ruta)
    for ruta in glob.glob(f"{CARPETA}/**/*.html", recursive=True):
        for g in re.findall(r'data-g="([^"]+)"', open(ruta, encoding="utf-8").read()):
            if g not in GRAFICOS:
                print("SIN GRÁFICO:", g, "en", ruta)
    print("sin usar:", sorted(set(GRAFICOS) - usados))


if __name__ == "__main__":
    main()
