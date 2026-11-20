"""Dibujos de la teoría de la Unidad 3 de Matemática Discreta (álgebras de Boole).

Uso (desde la raíz del repo):  python fuentes/md/u3_boole.py
Mete cada SVG dentro de su <div class="pd-grafico" data-g="u3t-..."></div> en
app/contenido/md/u3/teoria/. Los diagramas de Hasse se arman con la relación de
orden (un segmento entre dos elementos si uno cubre al otro), no a ojo.
"""
import os
import re
from itertools import combinations
from math import gcd

RAIZ = "app/contenido/md/u3/teoria"
ALTO_LETRA = 14


def ancho_texto(t):
    return 8.2 * len(t)


def hasse(elementos, cubre, niveles, x0, ancho, y_base, paso_y, titulo):
    """elementos: lista de rótulos; cubre(a, b): b cubre a a (a debajo de b);
    niveles: dict rótulo -> nivel (0 abajo)."""
    por_nivel = {}
    for e in elementos:
        por_nivel.setdefault(niveles[e], []).append(e)
    pos = {}
    for nivel, fila in por_nivel.items():
        k = len(fila)
        for i, e in enumerate(fila):
            x = x0 + ancho * (i + 1) / (k + 1)
            y = y_base - nivel * paso_y
            pos[e] = (x, y)
    partes = []
    for a in elementos:
        for b in elementos:
            if cubre(a, b):
                (xa, ya), (xb, yb) = pos[a], pos[b]
                # el segmento arranca arriba del rótulo de abajo y termina abajo del de arriba
                partes.append(
                    f'<line class="flecha" x1="{xa:.1f}" y1="{ya - ALTO_LETRA:.1f}" '
                    f'x2="{xb:.1f}" y2="{yb + 6:.1f}"/>'
                )
    for e, (x, y) in pos.items():
        partes.append(f'<text class="valor" x="{x:.1f}" y="{y:.1f}" text-anchor="middle">{e}</text>')
    partes.append(
        f'<text class="rotulo" x="{x0 + ancho / 2:.1f}" y="{y_base + 30:.1f}" '
        f'text-anchor="middle">{titulo}</text>'
    )
    return partes


def partes_de(letras):
    subs = []
    for k in range(len(letras) + 1):
        for c in combinations(letras, k):
            subs.append(frozenset(c))
    return subs


def rotulo_conj(s, letras, total):
    if not s:
        return "∅"
    if len(s) == len(letras) and total:
        return total
    return "{" + ", ".join(sorted(s)) + "}"


def svg_hasse_partes():
    partes = []
    conjuntos = [("a",), ("a", "b"), ("a", "b", "c")]
    xs = [(0, 150), (150, 200), (350, 250)]
    for letras, (x0, w) in zip(conjuntos, xs):
        subs = partes_de(letras)
        rot = {s: rotulo_conj(s, letras, None) for s in subs}
        elementos = [rot[s] for s in subs]
        inv = {v: k for k, v in rot.items()}
        niveles = {rot[s]: len(s) for s in subs}
        cubre = lambda a, b, inv=inv: inv[a] < inv[b] and len(inv[b]) == len(inv[a]) + 1
        titulo = "P({" + ", ".join(letras) + "})"
        partes += hasse(elementos, cubre, niveles, x0, w, 230, 62, titulo)
    return f'<svg viewBox="0 0 600 275" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagramas de Hasse de los conjuntos de partes">\n' + "\n".join(partes) + "\n</svg>"


def svg_hasse_d30():
    partes = []
    # D(30) ordenado por divisibilidad
    divs = [1, 2, 3, 5, 6, 10, 15, 30]
    nivel = {1: 0, 2: 1, 3: 1, 5: 1, 6: 2, 10: 2, 15: 2, 30: 3}
    elementos = [str(d) for d in divs]
    niveles = {str(d): nivel[d] for d in divs}

    def cubre(a, b):
        a, b = int(a), int(b)
        return b % a == 0 and b != a and nivel[b] == nivel[a] + 1

    partes += hasse(elementos, cubre, niveles, 20, 250, 230, 62, "D(30), ordenado por divisibilidad")
    # P({2, 3, 5}): el mismo dibujo
    letras = ("2", "3", "5")
    subs = partes_de(letras)
    rot = {s: rotulo_conj(s, letras, None) for s in subs}
    inv = {v: k for k, v in rot.items()}
    cubre2 = lambda a, b: inv[a] < inv[b] and len(inv[b]) == len(inv[a]) + 1
    partes += hasse([rot[s] for s in subs], cubre2, {rot[s]: len(s) for s in subs}, 320, 270, 230, 62,
                    "P({2, 3, 5}), ordenado por inclusión")
    return f'<svg viewBox="0 0 600 275" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="D(30) y P de 2, 3, 5 tienen el mismo diagrama de Hasse">\n' + "\n".join(partes) + "\n</svg>"


def interruptor(x, y, nombre):
    """Interruptor abierto dibujado entre x y x + 40 a la altura y."""
    return [
        f'<circle class="punto" cx="{x}" cy="{y}" r="3"/>',
        f'<circle class="punto" cx="{x + 40}" cy="{y}" r="3"/>',
        f'<line class="eje" x1="{x}" y1="{y}" x2="{x + 36}" y2="{y - 16}"/>',
        f'<text class="valor" x="{x + 20}" y="{y - 22}" text-anchor="middle">{nombre}</text>',
    ]


def svg_circuitos():
    p = []
    # serie
    y = 70
    p.append(f'<line class="eje" x1="20" y1="{y}" x2="70" y2="{y}"/>')
    p += interruptor(70, y, "x")
    p.append(f'<line class="eje" x1="110" y1="{y}" x2="160" y2="{y}"/>')
    p += interruptor(160, y, "y")
    p.append(f'<line class="eje" x1="200" y1="{y}" x2="250" y2="{y}"/>')
    p.append(f'<text class="rotulo" x="135" y="{y + 40}" text-anchor="middle">En serie: pasa corriente solo si x = 1 y y = 1</text>')
    p.append(f'<text class="valor" x="135" y="{y + 62}" text-anchor="middle">x · y</text>')
    # paralelo
    y1, y2 = 50, 110
    p.append(f'<line class="eje" x1="330" y1="80" x2="370" y2="80"/>')
    p.append(f'<line class="eje" x1="370" y1="{y1}" x2="370" y2="{y2}"/>')
    p.append(f'<line class="eje" x1="370" y1="{y1}" x2="420" y2="{y1}"/>')
    p.append(f'<line class="eje" x1="370" y1="{y2}" x2="420" y2="{y2}"/>')
    p += interruptor(420, y1, "x")
    p += interruptor(420, y2, "y")
    p.append(f'<line class="eje" x1="460" y1="{y1}" x2="510" y2="{y1}"/>')
    p.append(f'<line class="eje" x1="460" y1="{y2}" x2="510" y2="{y2}"/>')
    p.append(f'<line class="eje" x1="510" y1="{y1}" x2="510" y2="{y2}"/>')
    p.append(f'<line class="eje" x1="510" y1="80" x2="550" y2="80"/>')
    p.append(f'<text class="rotulo" x="440" y="150" text-anchor="middle">En paralelo: pasa si x = 1 o y = 1</text>')
    p.append(f'<text class="valor" x="440" y="172" text-anchor="middle">x + y</text>')
    return '<svg viewBox="0 0 600 190" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Interruptores en serie y en paralelo">\n' + "\n".join(p) + "\n</svg>"


D = {
    "u3t-hasse-partes": svg_hasse_partes,
    "u3t-hasse-d30": svg_hasse_d30,
    "u3t-circuitos": svg_circuitos,
}


def main():
    patron = re.compile(r'(<div class="pd-grafico" data-g="([^"]+)">)(.*?)(\n?[ \t]*</div>)', re.S)
    usados = set()
    for archivo in sorted(os.listdir(RAIZ)):
        if not archivo.endswith(".html"):
            continue
        ruta = os.path.join(RAIZ, archivo)
        with open(ruta, encoding="utf-8") as fh:
            viejo = fh.read()

        def cambiar(m):
            if m.group(2) not in D:
                return m.group(0)
            usados.add(m.group(2))
            sangria = re.search(r"[ \t]*$", viejo[:m.start()]).group(0) + "  "
            dibujo = "\n".join(sangria + l for l in D[m.group(2)]().splitlines())
            return f"{m.group(1)}\n{dibujo}\n{sangria[:-2]}</div>"

        nuevo = patron.sub(cambiar, viejo)
        if nuevo != viejo:
            with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(nuevo)
            print("ok:", archivo)
    for nombre in sorted(set(D) - usados):
        print("SIN USAR:", nombre)


if __name__ == "__main__":
    main()
