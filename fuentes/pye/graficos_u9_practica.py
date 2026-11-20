"""Gráficos de la Práctica de la Unidad 9 de PyE (app/contenido/pye/u9/practica/).

Cada prueba de hipótesis lleva su campana (Z o t) con la región de rechazo sombreada, el valor
crítico marcado y el estadístico calculado como un punto sobre el eje.
Rellena el <svg> que está dentro de cada <div class="pd-grafico" data-g="NOMBRE"> (lo que venga
después del </svg>, como el pie, no se toca).
Uso, desde la raíz del repo:  python fuentes/pye/graficos_u9_practica.py
"""
import glob
import re

from scipy import stats

CARPETA = "app/contenido/pye/u9/practica"
X0, X1, CENTRO = 40, 580, 310
BASE, PICO = 205, 50


def num(v, dec=2):
    return f"{v:.{dec}f}".replace(".", ",").replace("-", "−")


def campana(nombre, dist, df, cola, critico, est, alfa, letra, rango=4.0, dec_est=2, dec_crit=3):
    """cola: 'izq', 'der' o 'dos'. critico: el valor positivo de tabla (z_α, t_α o el de α/2)."""
    pdf = (lambda x: stats.norm.pdf(x)) if dist == "z" else (lambda x: stats.t.pdf(x, df))
    escala = (BASE - PICO) / pdf(0)
    px = lambda x: CENTRO + x * (X1 - CENTRO) / rango
    py = lambda x: BASE - pdf(x) * escala
    pasos = 96
    puntos = [(-rango + 2 * rango * i / pasos) for i in range(pasos + 1)]
    trazo = " ".join(f"L {px(x):.1f},{py(x):.1f}" for x in puntos)
    d = f"M {X0},{BASE} {trazo} L {X1},{BASE} Z"
    clip = f"c-{nombre}"
    rects = []
    if cola in ("izq", "dos"):
        rects.append(f'<rect x="{X0}" y="0" width="{px(-critico) - X0:.1f}" height="{BASE}"/>')
    if cola in ("der", "dos"):
        rects.append(f'<rect x="{px(critico):.1f}" y="0" width="{X1 - px(critico):.1f}" height="{BASE}"/>')
    tipo = {"izq": "cola izquierda", "der": "cola derecha", "dos": "las dos colas"}[cola]
    curva = "normal estándar Z" if dist == "z" else f"t de Student con {df} grados de libertad"
    borde = {"izq": num(-critico, dec_crit), "der": num(critico, dec_crit), "dos": "±" + num(critico, dec_crit)}[cola]
    aria = (f"Campana {curva}; región de rechazo en {tipo} desde {borde}; "
            f"el estadístico {letra} = {num(est, dec_est)} marcado sobre el eje")
    s = [f'<svg viewBox="0 0 620 255" role="img" aria-label="{aria}">',
         f'  <defs><clipPath id="{clip}">{"".join(rects)}</clipPath></defs>',
         f'  <path class="campana" d="{d}"/>',
         f'  <path class="area" clip-path="url(#{clip})" d="{d}"/>',
         f'  <line class="eje" x1="30" y1="{BASE}" x2="595" y2="{BASE}"/>',
         f'  <line class="guia" x1="{CENTRO}" y1="{PICO}" x2="{CENTRO}" y2="{BASE}"/>',
         f'  <text class="rotulo" x="{CENTRO}" y="228" text-anchor="middle">0</text>']
    area = {0.1: "0,10", 0.05: "0,05", 0.025: "0,025", 0.01: "0,01", 0.005: "0,005"}[round(alfa / 2 if cola == "dos" else alfa, 4)]
    lados = []
    if cola in ("izq", "dos"):
        lados.append(-critico)
    if cola in ("der", "dos"):
        lados.append(critico)
    for c in lados:
        x = px(c)
        s.append(f'  <line class="corte" x1="{x:.1f}" y1="{py(c):.1f}" x2="{x:.1f}" y2="{BASE}"/>')
        s.append(f'  <text class="rotulo" x="{x:.1f}" y="228" text-anchor="middle">{num(c, dec_crit)}</text>')
        tx = max(85, min(535, x - 62 if c < 0 else x + 62))
        s.append(f'  <text class="valor" x="{tx:.1f}" y="168" text-anchor="middle">rechazo</text>')
        s.append(f'  <text class="rotulo" x="{tx:.1f}" y="148" text-anchor="middle">área {area}</text>')
    # zona de no rechazo, rotulada arriba
    izq = px(-critico) if cola in ("izq", "dos") else X0
    der = px(critico) if cola in ("der", "dos") else X1
    s.append(f'  <text class="rotulo" x="{(izq + der) / 2:.1f}" y="28" text-anchor="middle">zona de no rechazo de H₀</text>')
    # el estadístico
    rotulo = f"{letra} = {num(est, dec_est)}"
    if est < -rango:
        s.append(f'  <circle class="punto" cx="{X0}" cy="{BASE}" r="5"/>')
        s.append(f'  <text class="rotulo" x="{X0}" y="246" text-anchor="start">← {rotulo} (mucho más a la izquierda)</text>')
    elif est > rango:
        s.append(f'  <circle class="punto" cx="{X1}" cy="{BASE}" r="5"/>')
        s.append(f'  <text class="rotulo" x="{X1}" y="246" text-anchor="end">{rotulo} (mucho más a la derecha) →</text>')
    else:
        x = px(est)
        ancla = "middle" if 90 < x < 530 else ("start" if x <= 90 else "end")
        s.append(f'  <circle class="punto" cx="{x:.1f}" cy="{BASE}" r="5"/>')
        s.append(f'  <text class="rotulo" x="{x:.1f}" y="246" text-anchor="{ancla}">{rotulo}</text>')
    s.append("</svg>")
    return "\n".join(s)


GRAFICOS = {
    "u9p-ej1": lambda: campana("u9p-ej1", "z", None, "izq", 1.645, -9.0, 0.05, "z"),
    "u9p-ej2": lambda: campana("u9p-ej2", "z", None, "der", 1.645, -2.76, 0.05, "z"),
    "u9p-ej3": lambda: campana("u9p-ej3", "z", None, "dos", 1.96, -7.5, 0.05, "z", dec_crit=2),
    "u9p-ej4": lambda: campana("u9p-ej4", "t", 19, "der", 1.729, 4.3809, 0.05, "t", rango=5.0, dec_est=4),
    "u9p-ej5": lambda: campana("u9p-ej5", "t", 7, "izq", 1.895, -2.7221, 0.05, "t", dec_est=4),
    "u9p-ej6": lambda: campana("u9p-ej6", "t", 5, "der", 1.476, 1.3156, 0.10, "t", dec_est=4),
    "u9p-ej7": lambda: campana("u9p-ej7", "t", 9, "dos", 3.250, 0.7717, 0.01, "t", rango=4.5, dec_est=4),
    "u9p-f1126": lambda: campana("u9p-f1126", "t", 14, "dos", 2.145, -0.3714, 0.05, "t", dec_est=4),
    "u9p-f1210": lambda: campana("u9p-f1210", "z", None, "dos", 1.96, -0.51, 0.05, "z", dec_crit=2),
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
