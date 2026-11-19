"""Gráficos del Primer Parcial 2025 de PyE (app/contenido/pye/evaluacion/parciales/2025-primer-parcial/).

Rellena cada <div class="pd-grafico" data-g="NOMBRE"> de esos archivos con el SVG calculado acá.
Uso, desde la raíz del repo:  python fuentes/pye/graficos_parcial1_2025.py
"""
import glob
import re

CARPETA = "app/contenido/pye/evaluacion/parciales/2025-primer-parcial"


def num(v):
    return f"{v:.4g}".replace(".", ",")


def caja():
    """Diagrama de caja vertical, como el del parcial (eje de 550 a 725)."""
    datos = sorted([558, 619, 629, 647, 655, 655, 678, 700, 719, 646,
                    644, 655, 678, 671, 697, 709, 711, 723, 590, 646])
    n = len(datos)
    q1 = (datos[4] + datos[5]) / 2
    q2 = (datos[9] + datos[10]) / 2
    q3 = (datos[14] + datos[15]) / 2
    iq = q3 - q1
    li, ls = q1 - 1.5 * iq, q3 + 1.5 * iq
    adentro = [x for x in datos if li <= x <= ls]
    bmin, bmax = min(adentro), max(adentro)
    atip = [x for x in datos if x < li or x > ls]
    y0, y1, v0, v1 = 280, 30, 550, 725
    Y = lambda v: y0 - (v - v0) / (v1 - v0) * (y0 - y1)
    cx, w = 330, 110
    s = ['<svg viewBox="0 0 620 310" role="img" aria-label="Diagrama de caja del nivel de contaminante, '
         'redibujado del parcial">']
    s.append(f'  <line class="eje" x1="120" y1="{y0}" x2="120" y2="{y1 - 6}"/>')
    for v in range(550, 726, 25):
        s.append(f'  <line class="eje" x1="114" y1="{Y(v):.1f}" x2="120" y2="{Y(v):.1f}"/>')
        s.append(f'  <text class="rotulo" x="108" y="{Y(v) + 4:.1f}" text-anchor="end">{v}</text>')
    s.append(f'  <text class="rotulo" x="40" y="{(y0 + y1) / 2:.0f}" text-anchor="middle" '
             f'transform="rotate(-90 40 {(y0 + y1) / 2:.0f})">ppm</text>')
    s.append(f'  <line class="eje" x1="{cx}" y1="{Y(bmin):.1f}" x2="{cx}" y2="{Y(q1):.1f}"/>')
    s.append(f'  <line class="eje" x1="{cx}" y1="{Y(q3):.1f}" x2="{cx}" y2="{Y(bmax):.1f}"/>')
    for v in (bmin, bmax):
        s.append(f'  <line class="eje" x1="{cx - 25}" y1="{Y(v):.1f}" x2="{cx + 25}" y2="{Y(v):.1f}"/>')
    s.append(f'  <rect class="barra" x="{cx - w / 2}" y="{Y(q3):.1f}" width="{w}" height="{Y(q1) - Y(q3):.1f}"/>')
    s.append(f'  <line class="corte" x1="{cx - w / 2}" y1="{Y(q2):.1f}" x2="{cx + w / 2}" y2="{Y(q2):.1f}"/>')
    for v in atip:
        s.append(f'  <circle class="punto" cx="{cx}" cy="{Y(v):.1f}" r="4"/>')
    rot = [(bmax, f"máximo sin atípicos: {bmax}"), (q3, f"Q3 = {num(q3)}"), (q2, f"mediana = {num(q2)}"),
           (q1, f"Q1 = {num(q1)}"), (bmin, f"mínimo sin atípicos: {bmin}")]
    ys = []
    for v, t in rot:  # de arriba hacia abajo, con 17 px como mínimo entre rótulos
        y = Y(v) + 4
        if ys and y - ys[-1] < 17:
            y = ys[-1] + 17
        ys.append(y)
        s.append(f'  <text class="rotulo" x="{cx + w / 2 + 18}" y="{y:.1f}">{t}</text>')
    for v in atip:
        s.append(f'  <text class="valor" x="{cx + 18}" y="{Y(v) + 5:.1f}">{v}: atípico</text>')
    s.append('</svg>')
    return "\n".join(s)


def arbol():
    """Árbol de los motores: proveedor y después defectuoso o no."""
    ramas = [("A", 0.90, [("D", 0.05), ("D'", 0.95)]), ("B", 0.10, [("D", 0.03), ("D'", 0.97)])]
    s = ['<svg viewBox="0 0 620 260" role="img" aria-label="Diagrama de árbol: proveedor A o B y '
         'motor defectuoso o no">']
    x0, y0 = 40, 130
    s.append(f'  <circle class="punto" cx="{x0}" cy="{y0}" r="4"/>')
    ys1 = [65, 195]
    for (n1, p1, hijos), y1 in zip(ramas, ys1):
        s.append(f'  <line class="eje" x1="{x0}" y1="{y0}" x2="200" y2="{y1}"/>')
        s.append(f'  <text class="rotulo" x="{(x0 + 200) / 2 - 10}" y="{(y0 + y1) / 2 - 8}">{num(p1)}</text>')
        s.append(f'  <text class="valor" x="208" y="{y1 + 5}">{n1}</text>')
        for (n2, p2), dy in zip(hijos, (-32, 32)):
            y2 = y1 + dy
            s.append(f'  <line class="eje" x1="228" y1="{y1}" x2="360" y2="{y2}"/>')
            s.append(f'  <text class="rotulo" x="{(228 + 360) / 2 - 8}" y="{(y1 + y2) / 2 - 7}">{num(p2)}</text>')
            s.append(f'  <text class="valor" x="368" y="{y2 + 5}">{n2}</text>')
            cls = "valor" if n2 == "D" else "rotulo"
            s.append(f'  <text class="{cls}" x="410" y="{y2 + 5}">{num(p1)} · {num(p2)} = {num(round(p1 * p2, 4))}</text>')
    s.append('</svg>')
    return "\n".join(s)


F_PUB = [0.20, 0.25, 0.18, 0.15, 0.10, 0.12]


def bastones():
    s = ['<svg viewBox="0 0 620 250" role="img" aria-label="Gráfico de bastones de f(x) para las publicaciones">']
    y0, esc = 210, 600
    X = lambda x: 90 + x * 90
    s.append(f'  <line class="eje" x1="60" y1="{y0}" x2="590" y2="{y0}"/>')
    s.append(f'  <line class="eje" x1="60" y1="{y0}" x2="60" y2="30"/>')
    for v in (0.05, 0.10, 0.15, 0.20, 0.25):
        yy = y0 - v * esc
        s.append(f'  <line class="guia" x1="60" y1="{yy:.1f}" x2="590" y2="{yy:.1f}"/>')
        s.append(f'  <text class="rotulo" x="52" y="{yy + 4:.1f}" text-anchor="end">{num(v)}</text>')
    for x, p in enumerate(F_PUB):
        yy = y0 - p * esc
        s.append(f'  <line class="corte" x1="{X(x)}" y1="{y0}" x2="{X(x)}" y2="{yy:.1f}" style="stroke-width:4"/>')
        s.append(f'  <circle class="punto" cx="{X(x)}" cy="{yy:.1f}" r="5"/>')
        s.append(f'  <text class="valor" x="{X(x)}" y="{yy - 10:.1f}" text-anchor="middle">{num(p)}</text>')
        s.append(f'  <text class="rotulo" x="{X(x)}" y="{y0 + 20}" text-anchor="middle">{x}</text>')
    s.append(f'  <text class="rotulo" x="590" y="{y0 + 38}" text-anchor="end">x = publicaciones</text>')
    s.append('</svg>')
    return "\n".join(s)


def escalera():
    s = ['<svg viewBox="0 0 620 260" role="img" aria-label="Gráfico escalonado de F(x) para las publicaciones">']
    y0, esc = 220, 180
    X = lambda x: 90 + x * 85
    s.append(f'  <line class="eje" x1="40" y1="{y0}" x2="600" y2="{y0}"/>')
    s.append(f'  <line class="eje" x1="60" y1="{y0}" x2="60" y2="25"/>')
    for v in (0.2, 0.45, 0.63, 0.78, 0.88, 1.0):
        yy = y0 - v * esc
        s.append(f'  <line class="guia" x1="60" y1="{yy:.1f}" x2="595" y2="{yy:.1f}"/>')
        s.append(f'  <text class="rotulo" x="54" y="{yy + 4:.1f}" text-anchor="end">{num(v)}</text>')
    acum = 0
    s.append(f'  <line class="corte" x1="40" y1="{y0}" x2="{X(0)}" y2="{y0}" style="stroke-width:3"/>')
    for x, p in enumerate(F_PUB):
        acum = round(acum + p, 2)
        yy = y0 - acum * esc
        fin = X(x + 1) if x < 5 else 600
        s.append(f'  <line class="corte" x1="{X(x)}" y1="{yy:.1f}" x2="{fin}" y2="{yy:.1f}" style="stroke-width:3"/>')
        s.append(f'  <circle class="punto" cx="{X(x)}" cy="{yy:.1f}" r="4.5"/>')
        s.append(f'  <text class="rotulo" x="{X(x)}" y="{y0 + 20}" text-anchor="middle">{x}</text>')
    s.append('</svg>')
    return "\n".join(s)


def region():
    """Rectángulo donde vive la densidad conjunta y las zonas que piden c) y d)."""
    s = ['<svg viewBox="0 0 620 300" role="img" aria-label="Región 0 ≤ x ≤ 2, 1 ≤ y ≤ 3 y las zonas '
         'x mayor que 2 e y menor que 1, que quedan afuera">']
    ox, oy, u = 90, 260, 60
    X = lambda x: ox + x * u
    Y = lambda y: oy - y * u
    s.append(f'  <rect class="area" x="{X(0)}" y="{Y(3)}" width="{2 * u}" height="{2 * u}"/>')
    s.append(f'  <rect class="area suave" x="{X(0)}" y="{Y(1)}" width="{4 * u}" height="{u}" style="fill:var(--practica)"/>')
    s.append(f'  <rect class="area suave" x="{X(2)}" y="{Y(3.6)}" width="{2 * u}" height="{3.6 * u}" style="fill:var(--practica)"/>')
    s.append(f'  <line class="eje" x1="{ox - 10}" y1="{oy}" x2="{X(4.6)}" y2="{oy}"/>')
    s.append(f'  <line class="eje" x1="{ox}" y1="{oy + 10}" x2="{ox}" y2="{Y(3.9)}"/>')
    for x in range(0, 5):
        s.append(f'  <text class="rotulo" x="{X(x)}" y="{oy + 20}" text-anchor="middle">{x}</text>')
    for y in range(1, 4):
        s.append(f'  <text class="rotulo" x="{ox - 10}" y="{Y(y) + 4}" text-anchor="end">{y}</text>')
        s.append(f'  <line class="guia" x1="{ox}" y1="{Y(y)}" x2="{X(4.5)}" y2="{Y(y)}"/>')
    s.append(f'  <text class="rotulo" x="{X(4.6)}" y="{oy + 20}" text-anchor="end">x (núcleos)</text>')
    s.append(f'  <text class="rotulo" x="{ox + 8}" y="{Y(3.9) + 4}">y (GB)</text>')
    s.append(f'  <text class="valor" x="{X(1)}" y="{Y(2) + 5}" text-anchor="middle">f &gt; 0</text>')
    s.append(f'  <text class="rotulo" x="{X(3)}" y="{Y(0.5) + 5}" text-anchor="middle">y &lt; 1: f = 0</text>')
    s.append(f'  <text class="rotulo" x="{X(3)}" y="{Y(2.5)}" text-anchor="middle">x &gt; 2: f = 0</text>')
    s.append('</svg>')
    return "\n".join(s)


GRAFICOS = {
    "p1-2025-caja": caja,
    "p1-2025-arbol": arbol,
    "p1-2025-bastones": bastones,
    "p1-2025-escalera": escalera,
    "p1-2025-region": region,
}


def main():
    for ruta in glob.glob(f"{CARPETA}/*.html"):
        texto = open(ruta, encoding="utf-8").read()
        nuevo = texto
        for nombre, fn in GRAFICOS.items():
            patron = re.compile(r'(<div class="pd-grafico" data-g="' + nombre + r'">)(.*?)(</div>)', re.S)
            nuevo = patron.sub(lambda m: m.group(1) + "\n" + fn() + "\n" + m.group(3), nuevo)
        if nuevo != texto:
            open(ruta, "w", encoding="utf-8", newline="\n").write(nuevo)
            print("actualizado", ruta)


if __name__ == "__main__":
    main()
