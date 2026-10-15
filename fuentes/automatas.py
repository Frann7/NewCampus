"""Autómatas finitos para Paradigmas y Lenguajes: los dibuja en SVG y hace las
cuentas de la cátedra (Thompson, subconjuntos, minimización) para no hacerlas
a mano.

Usos (desde la raíz del repo):

    python fuentes/automatas.py fuentes/pyl/diagramas/u3.py [app/contenido/pyl]
        Mete los dibujos en los fragmentos: el contenido de cada
        `<div class="pd-grafico af" data-g="nombre">...</div>` se reemplaza
        por el SVG de `D["nombre"]`. Los estilos (`.af ...`) están en
        `app/assets/estilos.css`.

    python fuentes/automatas.py --resolver "b(a*|b)|a"
        Imprime Thompson (estados y transiciones), la tabla de subconjuntos,
        las particiones de la minimización y el AFD mínimo. Con `--html` al
        final, también las tablas en HTML para pegar en el fragmento.

    python fuentes/automatas.py --comparar "ER" "ER2" [alfabeto]
        Dice si las dos ER generan las mismas cadenas hasta largo 9.

    python fuentes/automatas.py --verificar fuentes/pyl/diagramas/u2.py
        Cada dibujo que tenga `er` (y `sigma`, el alfabeto) se prueba contra
        esa ER con todas las cadenas hasta largo 8; con `cumple` (una función
        de Python que dice si una cadena está en el lenguaje), contra ella. Las etiquetas pueden ser
        ER (los pasos intermedios de AF -> ER), y "0, 1" es lo mismo que 0|1.

Un dibujo:
    D["par-de-a"] = dict(
        estados={"q0": (0, 0), "q1": (2, 0)},   # centro, en celdas de 80 px
        inicial="q0", finales=["q0"],
        trans=[("q0", "q1", "a"), ("q1", "q0", "a"), ("q0", "q0", "b")],
    )
Opcionales del dibujo: `muertos` (gris y punteado), `marcados` (el estado que
se está por eliminar), `entrada` (de dónde llega la flecha del inicial: izq,
arriba, abajo), `alt`.
Una transición es (de, a, etiqueta[, opciones]). Dos transiciones con el mismo
origen y destino se juntan en una sola etiqueta ("a, b"). Si hay ida y vuelta
entre dos estados, las dos se curvan solas. Opciones: `curva` (px; positivo
dobla hacia la izquierda de quien recorre la flecha), `lazo` (arriba, abajo,
izq, der), `lado` (+1 / -1: de qué lado de la flecha va la etiqueta), `nueva`
(verde: la transición que se acaba de crear), `t` (dónde va la etiqueta, de 0 a 1).

`thompson("ER")` devuelve el dibujo del AFN-ε de Thompson, ya ubicado.
"""
import math
import os
import re
import sys
from itertools import product

CELDA = 80
R = 19          # radio del estado
R2 = 15         # radio del círculo de adentro (estado final)
MARGEN = 12
EPS = "ε"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def ancho_texto(s):
    return len(s) * 7.6


# ----------------------------------------------------------------- dibujo

def _u(x, y):
    n = math.hypot(x, y) or 1
    return x / n, y / n


def _punta(tip, d, clase="punta"):
    ux, uy = d
    bx, by = tip[0] - 9 * ux, tip[1] - 9 * uy
    px, py = -uy * 4.5, ux * 4.5
    return (f'<path class="{clase}" d="M{tip[0]:.1f},{tip[1]:.1f} L{bx + px:.1f},{by + py:.1f} '
            f'L{bx - px:.1f},{by - py:.1f} Z"/>')


def _rotulo(x, y, texto, puntos):
    w = ancho_texto(texto)
    puntos += [(x - w / 2, y - 9), (x + w / 2, y + 9)]
    return (f'<text class="rot" x="{x:.1f}" y="{y:.1f}" text-anchor="middle" '
            f'dominant-baseline="central">{esc(texto)}</text>')


def svg(d):
    pos = {k: (v[0] * CELDA, v[1] * CELDA) for k, v in d["estados"].items()}
    finales, muertos, marcados = set(d.get("finales", [])), set(d.get("muertos", [])), set(d.get("marcados", []))
    # juntar paralelas
    juntas, orden = {}, []
    for t in d.get("trans", []):
        de, a, et = t[0], t[1], t[2]
        op = dict(t[3]) if len(t) > 3 else {}
        if (de, a) in juntas:
            juntas[(de, a)][0].append(et)
            juntas[(de, a)][1].update(op)
        else:
            juntas[(de, a)] = ([et], op)
            orden.append((de, a))
    cuerpo, puntos = [], []
    for (de, a) in orden:
        ets, op = juntas[(de, a)]
        texto = ", ".join(ets)
        clase = "arco nueva" if op.get("nueva") else "arco"
        c1 = pos[de]
        if de == a:
            ang = {"arriba": -90, "abajo": 90, "izq": 180, "der": 0}[op.get("lazo", "arriba")]
            th = math.radians(ang)
            p = lambda g, r: (c1[0] + r * math.cos(th + math.radians(g)), c1[1] + r * math.sin(th + math.radians(g)))
            p1, k1, k2, p2 = p(-28, R), p(-38, R + 46), p(38, R + 46), p(28, R)
            cuerpo.append(f'<path class="{clase}" d="M{p1[0]:.1f},{p1[1]:.1f} C{k1[0]:.1f},{k1[1]:.1f} '
                          f'{k2[0]:.1f},{k2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"/>')
            cuerpo.append(_punta(p2, _u(p2[0] - k2[0], p2[1] - k2[1]), clase.replace("arco", "punta")))
            puntos += [k1, k2]
            w = ancho_texto(texto)
            extra = 9 if ang in (-90, 90) else w / 2 + 4
            lx, ly = c1[0] + (R + 28 + extra) * math.cos(th), c1[1] + (R + 28 + extra) * math.sin(th)
            cuerpo.append(_rotulo(lx, ly, texto, puntos))
            continue
        c2 = pos[a]
        dx, dy = _u(c2[0] - c1[0], c2[1] - c1[1])
        nx, ny = dy, -dx                      # normal a la izquierda de quien recorre
        curva = op.get("curva")
        if curva is None:
            curva = 18 if (a, de) in juntas and juntas[(a, de)][1].get("curva") is None else 0
        mx, my = (c1[0] + c2[0]) / 2, (c1[1] + c2[1]) / 2
        k = (mx + nx * 2 * curva, my + ny * 2 * curva)
        s = (c1[0] + R * _u(k[0] - c1[0], k[1] - c1[1])[0], c1[1] + R * _u(k[0] - c1[0], k[1] - c1[1])[1])
        e = (c2[0] + R * _u(k[0] - c2[0], k[1] - c2[1])[0], c2[1] + R * _u(k[0] - c2[0], k[1] - c2[1])[1])
        if curva:
            cuerpo.append(f'<path class="{clase}" d="M{s[0]:.1f},{s[1]:.1f} Q{k[0]:.1f},{k[1]:.1f} {e[0]:.1f},{e[1]:.1f}"/>')
        else:
            cuerpo.append(f'<path class="{clase}" d="M{s[0]:.1f},{s[1]:.1f} L{e[0]:.1f},{e[1]:.1f}"/>')
        cuerpo.append(_punta(e, _u(e[0] - k[0], e[1] - k[1]), clase.replace("arco", "punta")))
        tt = op.get("t", 0.5)
        bx = (1 - tt) ** 2 * s[0] + 2 * tt * (1 - tt) * k[0] + tt ** 2 * e[0]
        by = (1 - tt) ** 2 * s[1] + 2 * tt * (1 - tt) * k[1] + tt ** 2 * e[1]
        puntos.append((bx, by))
        lado = op.get("lado")
        if lado is None:
            if curva:
                lado = 1 if curva > 0 else -1
            else:
                lado = 1 if ny < -0.01 or (abs(ny) <= 0.01 and nx < 0) else -1
        w = ancho_texto(texto)
        dist = 10 + abs(nx) * w / 2
        cuerpo.append(_rotulo(bx + lado * nx * dist, by + lado * ny * dist, texto, puntos))
    # flecha de entrada
    if d.get("inicial"):
        c = pos[d["inicial"]]
        ux, uy = {"izq": (1, 0), "arriba": (0, 1), "abajo": (0, -1)}[d.get("entrada", "izq")]
        a0 = (c[0] - ux * (R + 30), c[1] - uy * (R + 30))
        a1 = (c[0] - ux * R, c[1] - uy * R)
        cuerpo.append(f'<path class="arco" d="M{a0[0]:.1f},{a0[1]:.1f} L{a1[0]:.1f},{a1[1]:.1f}"/>')
        cuerpo.append(_punta(a1, (ux, uy)))
        puntos.append(a0)
    for nombre, c in pos.items():
        clase = "estado"
        if nombre in muertos:
            clase += " muerto"
        if nombre in marcados:
            clase += " marcado"
        g = [f'<g class="{clase}">', f'  <circle class="borde" cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{R}"/>']
        if nombre in finales:
            g.append(f'  <circle class="borde" cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{R2}"/>')
        etiqueta = d.get("nombres", {}).get(nombre, nombre)
        tam = ' style="font-size:11px"' if len(etiqueta) > 3 else ""
        g.append(f'  <text class="nom" x="{c[0]:.1f}" y="{c[1]:.1f}" text-anchor="middle" '
                 f'dominant-baseline="central"{tam}>{esc(etiqueta)}</text>')
        g.append("</g>")
        cuerpo += g
        puntos += [(c[0] - R, c[1] - R), (c[0] + R, c[1] + R)]
    xs, ys = [p[0] for p in puntos], [p[1] for p in puntos]
    x0, y0 = min(xs) - MARGEN, min(ys) - MARGEN
    w, h = max(xs) + MARGEN - x0, max(ys) + MARGEN - y0
    cabeza = (f'<svg viewBox="{x0:.0f} {y0:.0f} {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" '
              f'role="img" aria-label="{esc(d.get("alt", "Diagrama de un autómata finito"))}">')
    return "\n".join([cabeza] + ["  " + l for l in cuerpo] + ["</svg>"])


# ----------------------------------------------------------- ER -> árbol

class ER:
    """Lee una ER con | . * + ? ε y paréntesis. Los símbolos son de un
    carácter. Prioridad: * sobre la concatenación sobre |; todo asocia por
    izquierda (como en la cátedra)."""

    def __init__(self, texto):
        self.s = [c for c in texto if not c.isspace()]
        self.i = 0
        self.arbol = self.union()
        if self.i != len(self.s):
            raise ValueError(f"sobra algo en la ER: {''.join(self.s[self.i:])}")

    def ver(self):
        return self.s[self.i] if self.i < len(self.s) else None

    def union(self):
        n = self.concat()
        while self.ver() == "|":
            self.i += 1
            n = ("|", n, self.concat())
        return n

    def concat(self):
        n = self.estrella()
        while self.ver() is not None and self.ver() not in "|)":
            n = (".", n, self.estrella())
        return n

    def estrella(self):
        n = self.atomo()
        while self.ver() in ("*", "+", "?"):
            op = self.s[self.i]
            self.i += 1
            if op == "*":
                n = ("*", n)
            elif op == "+":
                n = (".", n, ("*", n))
            else:
                n = ("|", n, ("ε",))
        return n

    def atomo(self):
        c = self.ver()
        if c == "(":
            self.i += 1
            n = self.union()
            if self.ver() != ")":
                raise ValueError("falta un paréntesis")
            self.i += 1
            return n
        if c is None or c in "|)*":
            raise ValueError("ER mal formada")
        self.i += 1
        return ("ε",) if c == EPS else ("s", c)


def a_python(texto):
    """La ER en sintaxis de re de Python (para probar cadenas)."""
    t = texto.replace(" ", "").replace(EPS, "")
    return "(?:" + t.replace("(", "(?:") + ")"


# ------------------------------------------------------------- Thompson

def thompson_afn(texto, con_dibujo=False):
    """AFN-ε de Thompson como lo dibuja la cátedra (en la concatenación el
    final de Nr y el inicial de Ns son el mismo estado). Devuelve
    (inicial, final, transiciones [(de, a, símbolo)], posiciones {estado: (col, fila)})
    y, con `con_dibujo`, también las opciones de dibujo de cada transición."""
    contador = [0]
    trans, pos = [], {}

    def nuevo():
        contador[0] += 1
        return contador[0]

    def mover(estados, dx, dy):
        for e in estados:
            x, y = pos[e]
            pos[e] = (x + dx, y + dy)

    def armar(n):
        """Devuelve (i, f, estados, ancho, arriba, abajo); i en (0,0), f en (ancho, 0)."""
        tipo = n[0]
        if tipo in ("s", "ε"):
            i, f = nuevo(), nuevo()
            pos[i], pos[f] = (0, 0), (1, 0)
            trans.append((i, f, n[1] if tipo == "s" else EPS, {}))
            return i, f, [i, f], 1, 0, 0
        if tipo == ".":
            i1, f1, e1, w1, a1, b1 = armar(n[1])
            i2, f2, e2, w2, a2, b2 = armar(n[2])
            mover(e2, w1, 0)
            # el inicial de Ns se funde con el final de Nr
            for k, (x, y, s, op) in enumerate(trans):
                trans[k] = (f1 if x == i2 else x, f1 if y == i2 else y, s, op)
            del pos[i2]
            e2 = [e for e in e2 if e != i2]
            return i1, f2, e1 + e2, w1 + w2, max(a1, a2), max(b1, b2)
        if tipo == "|":
            i1, f1, e1, w1, a1, b1 = armar(n[1])
            i2, f2, e2, w2, a2, b2 = armar(n[2])
            sep = 0.45
            y1, y2 = -(b1 + sep), a2 + sep
            mover(e1, 1, y1)
            mover(e2, 1, y2)
            w = max(w1, w2) + 2
            i, f = nuevo(), nuevo()
            pos[i], pos[f] = (0, 0), (w, 0)
            trans.extend([(i, i1, EPS, {}), (i, i2, EPS, {}), (f1, f, EPS, {}), (f2, f, EPS, {})])
            return i, f, e1 + e2 + [i, f], w, a1 - y1, b2 + y2
        if tipo == "*":
            i1, f1, e1, w1, a1, b1 = armar(n[1])
            mover(e1, 1, 0)
            i, f = nuevo(), nuevo()
            pos[i], pos[f] = (0, 0), (w1 + 2, 0)
            # la vuelta pasa por arriba de Nr y el salto por abajo
            trans.extend([(i, i1, EPS, {}), (f1, f, EPS, {}),
                          (f1, i1, EPS, {"curva": -(a1 + 0.55) * CELDA}),
                          (i, f, EPS, {"curva": -(b1 + 0.5) * CELDA})])
            return i, f, e1 + [i, f], w1 + 2, a1 + 0.75, b1 + 0.7
        raise ValueError(tipo)

    i, f, estados, *_ = armar(ER(texto).arbol)
    # numerar de izquierda a derecha y de arriba abajo
    orden = sorted(estados, key=lambda e: (round(pos[e][0], 3), round(pos[e][1], 3)))
    nombre = {e: str(k) for k, e in enumerate(orden)}
    t3 = [(nombre[a], nombre[b], s) for a, b, s, _ in trans]
    posiciones = {nombre[e]: pos[e] for e in estados}
    if con_dibujo:
        return nombre[i], nombre[f], t3, posiciones, [op for *_, op in trans]
    return nombre[i], nombre[f], t3, posiciones


def thompson(texto, **extra):
    i, f, trans, pos, ops = thompson_afn(texto, con_dibujo=True)
    lineas = [(a, b, s, op) if op else (a, b, s) for (a, b, s), op in zip(trans, ops)]
    d = dict(estados=pos, inicial=i, finales=[f], trans=lineas,
             alt=f"AFN-ε de Thompson para {texto}")
    d.update(extra)
    return d


# ------------------------------------------- subconjuntos y minimización

def clausura(T, trans):
    pila, vistos = list(T), set(T)
    while pila:
        e = pila.pop()
        for a, b, s in trans:
            if a == e and s == EPS and b not in vistos:
                vistos.add(b)
                pila.append(b)
    return frozenset(vistos)


def mueve(T, x, trans):
    return frozenset(b for a, b, s in trans if a in T and s == x)


def alfabeto(trans):
    return sorted({s for _, _, s in trans if s != EPS})


def subconjuntos(i, f, trans, sigma=None):
    sigma = sigma or alfabeto(trans)
    letras = iter("ABCDEFGHIJKLMNOPRSTUVWXYZ")
    inicio = clausura({i}, trans)
    nombres = {inicio: next(letras)}
    pendientes, filas, delta = [inicio], [], {}
    while pendientes:
        T = pendientes.pop(0)
        fila = []
        for x in sigma:
            m = mueve(T, x, trans)
            U = clausura(m, trans)
            if U not in nombres:
                nombres[U] = "∅" if not U else next(letras)
                if U:
                    pendientes.append(U)
            delta[(nombres[T], x)] = nombres[U]
            fila.append((x, m, U))
        filas.append((T, fila))
    finales = [nombres[T] for T in nombres if f in T]
    estados = [nombres[T] for T in nombres]
    if "∅" in estados:
        for x in sigma:
            delta[("∅", x)] = "∅"
    return nombres, filas, delta, estados, finales, sigma


def minimizar(estados, finales, delta, sigma):
    grupos = [sorted(e for e in estados if e in finales), sorted(e for e in estados if e not in finales)]
    grupos = [g for g in grupos if g]
    pasos = [grupos]
    while True:
        donde = {e: k for k, g in enumerate(grupos) for e in g}
        nuevos = []
        for g in grupos:
            sub = {}
            for e in g:
                firma = tuple(donde[delta[(e, x)]] for x in sigma)
                sub.setdefault(firma, []).append(e)
            nuevos += list(sub.values())
        if len(nuevos) == len(grupos):
            return pasos
        grupos = nuevos
        pasos.append(grupos)


def acepta_dfa(delta, inicial, finales, w):
    q = inicial
    for c in w:
        q = delta.get((q, c))
        if q is None:
            return False
    return q in finales


def resolver(texto):
    i, f, trans, pos = thompson_afn(texto)
    print(f"ER: {texto}\nThompson: inicial {i}, final {f}, {len(pos)} estados")
    for a, b, s in sorted(trans, key=lambda t: (int(t[0]), int(t[1]))):
        print(f"  {a} --{s}--> {b}")
    nombres, filas, delta, estados, finales, sigma = subconjuntos(i, f, trans)
    fmt = lambda S: "{" + ", ".join(sorted(S, key=int)) + "}" if S else "∅"
    print("\nSubconjuntos:")
    for T, fila in filas:
        print(f"  {nombres[T]} = {fmt(T)}" + ("  (final)" if nombres[T] in finales else ""))
        for x, m, U in fila:
            print(f"     mueve({nombres[T]},{x}) = {fmt(m)}  ->  ε-clausura = {fmt(U)} = {nombres[U]}")
    print("\nTabla del AFD:")
    for e in estados:
        print(f"  {e}{'*' if e in finales else ' '}  " + "  ".join(f"{x}:{delta[(e, x)]}" for x in sigma))
    print("\nParticiones:")
    pasos = minimizar(estados, finales, delta, sigma)
    for k, p in enumerate(pasos, 1):
        print(f"  P{k} = " + "  ".join("{" + ",".join(g) + "}" for g in p))
    print(f"  P{len(pasos) + 1} = P{len(pasos)}: no cambia, se termina")
    if "--html" in sys.argv:
        html_tablas(nombres, filas, delta, estados, finales, sigma, pasos)
    return nombres, delta, estados, finales, sigma


def html_tablas(nombres, filas, delta, estados, finales, sigma, pasos):
    """Las tablas de subconjuntos, del AFD y de la partición, listas para pegar."""
    fmt = lambda S: "{" + ", ".join(sorted(S, key=int)) + "}" if S else "∅"
    o = ["", '<div class="tabla-wrap">', '  <table class="t full">',
         "    <tr><th>Estado del AFD</th><th>Estados de Thompson</th>"
         + "".join(f"<th>mueve(T, {x})</th><th>ε-clausura: con {x} va a</th>" for x in sigma) + "</tr>"]
    for T, fila in filas:
        celdas = "".join(f"<td>{fmt(m)}</td><td>{fmt(U)} = <strong>{nombres[U]}</strong></td>" for x, m, U in fila)
        fin = " (final)" if nombres[T] in finales else ""
        o.append(f'    <tr><td class="lbl">{nombres[T]}{fin}</td><td>{fmt(T)}</td>{celdas}</tr>')
    o += ["  </table>", "</div>", "", '<div class="tabla-wrap">', '  <table class="t">',
          "    <tr><th>&delta;</th>" + "".join(f"<th>{x}</th>" for x in sigma) + "</tr>"]
    for e in estados:
        marca = ("&rarr; " if e == estados[0] else "") + e + (" *" if e in finales else "")
        o.append(f'    <tr><td class="lbl">{marca}</td>' + "".join(f"<td>{delta[(e, x)]}</td>" for x in sigma) + "</tr>")
    o += ["  </table>", "</div>", "", "<ul>"]
    for k, p in enumerate(pasos, 1):
        o.append(f"  <li><strong>P{k}</strong> = " + " &nbsp; ".join("{" + ", ".join(g) + "}" for g in p) + "</li>")
    o += [f"  <li><strong>P{len(pasos) + 1}</strong> = P{len(pasos)}: no cambia, se termina.</li>", "</ul>"]
    print("\n".join(o))


def acepta(d, w):
    """¿El dibujo d acepta w? Sirve para AFD, AFN, AFN-ε y para los pasos con
    ER en las etiquetas."""
    reglas = []
    for t in d["trans"]:
        et = "|".join("(" + p.strip() + ")" for p in t[2].split(","))
        reglas.append((t[0], t[1], re.compile(a_python(et))))
    vistos, pila = set(), [(d["inicial"], 0)]
    while pila:
        q, i = pila.pop()
        if (q, i) in vistos:
            continue
        vistos.add((q, i))
        for de, a, r in reglas:
            if de == q:
                for j in range(i, len(w) + 1):
                    if r.fullmatch(w[i:j]):
                        pila.append((a, j))
    return any((f, len(w)) in vistos for f in d.get("finales", []))


def cadenas(sigma, largo):
    for n in range(largo + 1):
        for t in product(sigma, repeat=n):
            yield "".join(t)


def main():
    if sys.argv[1] == "--resolver":
        resolver(sys.argv[2])
        return
    if sys.argv[1] == "--comparar":
        r1, r2 = sys.argv[2], sys.argv[3]
        sigma = sys.argv[4] if len(sys.argv) > 4 else "".join(sorted(set(re.sub(r"[|()*+?ε ]", "", r1 + r2))))
        p1, p2 = re.compile(a_python(r1)), re.compile(a_python(r2))
        dif = [w for w in cadenas(sigma, 9) if bool(p1.fullmatch(w)) != bool(p2.fullmatch(w))]
        print("iguales hasta largo 9" if not dif else f"DISTINTAS: {dif[:10]}")
        return
    if sys.argv[1] == "--verificar":
        espacio = {"D": {}, "thompson": thompson, "EPS": EPS}
        with open(sys.argv[2], encoding="utf-8") as f:
            exec(compile(f.read(), sys.argv[2], "exec"), espacio)
        malos = 0
        for nombre, d in espacio["D"].items():
            if "er" in d:
                r = re.compile(a_python(d["er"]))
                cumple = lambda w: bool(r.fullmatch(w))
            elif "cumple" in d:
                cumple = d["cumple"]
            else:
                continue
            dif = [w for w in cadenas(d["sigma"], 8) if acepta(d, w) != cumple(w)]
            malos += bool(dif)
            print(("ok      " if not dif else "DISTINTO") + f" {nombre}" + (f": {dif[:6]}" if dif else ""))
        sys.exit(1 if malos else 0)
    espacio = {"D": {}, "thompson": thompson, "EPS": EPS}
    with open(sys.argv[1], encoding="utf-8") as f:
        exec(compile(f.read(), sys.argv[1], "exec"), espacio)
    D = espacio["D"]
    raiz = sys.argv[2] if len(sys.argv) > 2 else "app/contenido/pyl"
    usados = set()
    patron = re.compile(r'(<div class="pd-grafico af" data-g="([^"]+)">)(.*?)(\n?[ \t]*</div>)', re.S)
    for carpeta, _, archivos in os.walk(raiz):
        for archivo in sorted(archivos):
            if not archivo.endswith(".html"):
                continue
            ruta = os.path.join(carpeta, archivo)
            with open(ruta, encoding="utf-8") as fh:
                viejo = fh.read()

            def cambiar(m):
                if m.group(2) not in D:
                    return m.group(0)
                usados.add(m.group(2))
                sangria = re.search(r"[ \t]*$", viejo[:m.start()]).group(0) + "  "
                dibujo = "\n".join(sangria + l for l in svg(D[m.group(2)]).splitlines())
                return f"{m.group(1)}\n{dibujo}\n{sangria[:-2]}</div>"

            nuevo = patron.sub(cambiar, viejo)
            if nuevo != viejo:
                with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(nuevo)
                print("ok:", os.path.relpath(ruta, raiz))
    for nombre in sorted(set(D) - usados):
        print("SIN USAR:", nombre)


if __name__ == "__main__":
    main()
