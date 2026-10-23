# Autómatas del parcial de práctica (app/contenido/pyl/evaluacion/parciales/2026-parcial-de-practica/).
# python fuentes/automatas.py fuentes/pyl/diagramas/practica-parcial.py            -> los mete en los fragmentos
# python fuentes/automatas.py --verificar fuentes/pyl/diagramas/practica-parcial.py -> los prueba contra su ER

N = "nueva"


def nv(*t):
    """Una transición recién creada (se dibuja en verde)."""
    return (*t, {N: True})


# =============================================================== ej. 1: AF -> ER
PP_ER = "a(ba)*b|(b|a(ba)*a)(a|ba)*b"
PP_POS = {"q0": (0, 1.3), "q1": (1.8, 0), "q2": (3.8, 0), "q3": (1.8, 2.6), "q4": (3.8, 2.6), "q5": (5.6, 1.3)}
_t = [("q0", "q1", "a"), ("q0", "q3", "b"), ("q1", "q2", "b"), ("q2", "q1", "a"), ("q1", "q3", "a"),
      ("q3", "q3", "a", {"lazo": "abajo"}), ("q3", "q4", "b"), ("q4", "q3", "a")]

D["pp-af"] = dict(
    estados=PP_POS, inicial="q0", finales=["q2", "q4"], er=PP_ER, sigma="ab",
    trans=_t + [("q2", "q5", "b"), ("q4", "q5", "b"), ("q5", "q5", "a", {"lazo": "der"}), ("q5", "q5", "b", {"lazo": "der"})],
    alt="Autómata del ejercicio 1 del parcial de práctica",
)
D["pp-muerto"] = dict(D["pp-af"], muertos=["q5"])
_p = {k: v for k, v in PP_POS.items() if k != "q5"}
_p.update(i=(-1.3, 1.3), f=(5.6, 1.3))
D["pp-paso1"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q2"], er=PP_ER, sigma="ab",
    trans=[nv("i", "q0", "ε")] + _t + [nv("q2", "f", "ε"), nv("q4", "f", "ε")],
)
_p = {k: v for k, v in _p.items() if k != "q2"}
D["pp-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q4"], er=PP_ER, sigma="ab",
    trans=[("i", "q0", "ε"), ("q0", "q1", "a"), ("q0", "q3", "b"), nv("q1", "q1", "ba"), nv("q1", "f", "b"),
           ("q1", "q3", "a"), ("q3", "q3", "a", {"lazo": "abajo"}), ("q3", "q4", "b"), ("q4", "q3", "a"),
           ("q4", "f", "ε")],
)
_p = {k: v for k, v in _p.items() if k != "q4"}
D["pp-paso3"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=PP_ER, sigma="ab",
    trans=[("i", "q0", "ε"), ("q0", "q1", "a"), ("q0", "q3", "b"), ("q1", "q1", "ba"), ("q1", "f", "b"),
           ("q1", "q3", "a"), nv("q3", "q3", "a|ba", {"lazo": "abajo"}), nv("q3", "f", "b")],
)
_p = {"i": (-1.3, 0), "q0": (0, 0), "q3": (2.6, 1.8), "f": (5.6, 0)}
D["pp-paso4"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q3"], er=PP_ER, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "f", "a(ba)*b"), nv("q0", "q3", "b|a(ba)*a"),
           ("q3", "q3", "a|ba", {"lazo": "abajo"}), ("q3", "f", "b")],
)
D["pp-paso5"] = dict(
    estados={"i": (-1.3, 0), "q0": (0, 0), "f": (5.0, 0)}, inicial="i", finales=["f"], marcados=["q0"],
    er=PP_ER, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "f", "a(ba)*b|(b|a(ba)*a)(a|ba)*b")],
)
D["pp-er"] = dict(
    estados={"i": (0, 0), "f": (5.0, 0)}, inicial="i", finales=["f"], er=PP_ER, sigma="ab",
    trans=[nv("i", "f", "a(ba)*b|(b|a(ba)*a)(a|ba)*b")],
)

# =============================================================== ej. 2: (ab*|b)a
D["pp-thompson"] = thompson("(ab*|b)a", er="(ab*|b)a", sigma="ab")
D["pp-afd"] = dict(
    estados={"A": (0, 1.2), "B": (1.8, 0), "C": (1.8, 2.4), "E": (3.8, 0), "D": (3.8, 1.2), "∅": (3.8, 2.8)},
    inicial="A", finales=["D"], muertos=["∅"], er="(ab*|b)a", sigma="ab",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("B", "D", "a"), ("B", "E", "b"), ("E", "D", "a"),
           ("E", "E", "b", {"lazo": "der"}), ("C", "D", "a"), ("C", "∅", "b"), ("D", "∅", "a"), ("D", "∅", "b"),
           ("∅", "∅", "a", {"lazo": "der"}), ("∅", "∅", "b", {"lazo": "der"})],
)
D["pp-min"] = dict(
    estados={"A": (0, 1.2), "B": (1.8, 0), "C": (1.8, 2.4), "D": (3.8, 1.2), "∅": (3.8, 2.8)},
    inicial="A", finales=["D"], muertos=["∅"], er="(ab*|b)a", sigma="ab",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("B", "D", "a"), ("B", "B", "b", {"lazo": "arriba"}),
           ("C", "D", "a"), ("C", "∅", "b"), ("D", "∅", "a"), ("D", "∅", "b"),
           ("∅", "∅", "a", {"lazo": "der"}), ("∅", "∅", "b", {"lazo": "der"})],
)

# =============================================================== ej. 3: terminan con z, impar de x
D["pp-impar"] = dict(
    estados={"q0": (0, 0), "q1": (2.2, 0), "q2": (4.4, 0)}, inicial="q0", finales=["q2"],
    er="(y|z)*x(y|z|x(y|z)*x)*z", sigma="xyz",
    cumple=lambda w: w.endswith("z") and w.count("x") % 2 == 1,
    trans=[("q0", "q0", "y"), ("q0", "q0", "z"), ("q0", "q1", "x"), ("q1", "q0", "x"),
           ("q1", "q1", "y"), ("q1", "q1", "z"), ("q1", "q2", "z")],
)

# ------------------------------------------------ la ER del ej. 3 contra su definición
import re as _re
from itertools import product as _product
for _n, _d in D.items():
    if "cumple" not in _d:
        continue
    _r = _re.compile("(?:" + _d["er"].replace("ε", "").replace("(", "(?:") + ")")
    for _k in range(9):
        for _w in map("".join, _product(_d["sigma"], repeat=_k)):
            if bool(_r.fullmatch(_w)) != _d["cumple"](_w):
                raise ValueError(f"{_n}: la ER no coincide con la definición en '{_w}'")
