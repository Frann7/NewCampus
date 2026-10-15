# Autómatas de la Unidad 4 (Diseñar AF y ER).
# python fuentes/automatas.py fuentes/pyl/diagramas/u4.py
# python fuentes/automatas.py --verificar fuentes/pyl/diagramas/u4.py
#
# Cada dibujo lleva la `er` del ejercicio (--verificar prueba el AF contra ella) y
# `cumple`, la definición en palabras pasada a Python: al final del archivo se
# prueba cada `er` contra su `cumple`, así no se escapa una ER mal armada.

# ------------------------------------------------ ej. 1 (TP I 5): longitud par
D["u4-e1-af"] = dict(
    estados={"q0": (0, 0), "q1": (2, 0)}, inicial="q0", finales=["q0"],
    er="((a|b)(a|b))*", sigma="ab", cumple=lambda w: len(w) % 2 == 0,
    trans=[("q0", "q1", "a"), ("q0", "q1", "b"), ("q1", "q0", "a"), ("q1", "q0", "b")],
)

# ------------------------------------------------ ej. 2 (TP I 24): binarios impares
D["u4-e2-af"] = dict(
    estados={"q0": (0, 0), "q1": (2, 0)}, inicial="q0", finales=["q1"],
    er="(0|1)*1", sigma="01", cumple=lambda w: w.endswith("1"),
    trans=[("q0", "q0", "0"), ("q0", "q1", "1"), ("q1", "q1", "1"), ("q1", "q0", "0")],
)

# ------------------------------------------------ ej. 3 (TP I 26): longitud múltiplo de 3
D["u4-e3-af"] = dict(
    estados={"q0": (0, 0), "q1": (2.2, 0), "q2": (1.1, 1.8)}, inicial="q0", finales=["q0"],
    er="((x|y)(x|y)(x|y))*", sigma="xy", cumple=lambda w: len(w) % 3 == 0,
    trans=[("q0", "q1", "x"), ("q0", "q1", "y"), ("q1", "q2", "x", {"lado": 1}), ("q1", "q2", "y", {"lado": 1}),
           ("q2", "q0", "x", {"lado": 1}), ("q2", "q0", "y", {"lado": 1})],
)

# ------------------------------------------------ ej. 4 (TP I 7): empiezan y terminan con 0
D["u4-e4-af"] = dict(
    estados={"q0": (0, 0), "q1": (2, 0), "q2": (4, 0)}, inicial="q0", finales=["q1"],
    er="0|0(0|1)*0", sigma="01", cumple=lambda w: w[:1] == "0" and w[-1:] == "0",
    trans=[("q0", "q1", "0"), ("q1", "q1", "0"), ("q1", "q2", "1"), ("q2", "q2", "1"), ("q2", "q1", "0")],
)

# ------------------------------------------------ ej. 5 (TP I 6): terminan con abb
D["u4-e5-af"] = dict(
    estados={"q0": (0, 0), "q1": (1.8, 0), "q2": (3.6, 0), "q3": (3.6, 1.9)}, inicial="q0", finales=["q3"],
    er="(a|b)*abb", sigma="ab", cumple=lambda w: w.endswith("abb"),
    trans=[("q0", "q0", "b"), ("q0", "q1", "a"), ("q1", "q1", "a"), ("q1", "q2", "b"), ("q2", "q1", "a"),
           ("q2", "q3", "b"), ("q3", "q1", "a"), ("q3", "q0", "b")],
)

# ------------------------------------------------ ej. 6 (TP I 12): contienen 000
D["u4-e6-af"] = dict(
    estados={"q0": (0, 0), "q1": (1.8, 0), "q2": (3.6, 0), "q3": (5.4, 0)}, inicial="q0", finales=["q3"],
    er="(0|1)*000(0|1)*", sigma="01", cumple=lambda w: "000" in w,
    trans=[("q0", "q0", "1"), ("q0", "q1", "0"), ("q1", "q0", "1"), ("q1", "q2", "0"),
           ("q2", "q0", "1", {"curva": 55}), ("q2", "q3", "0"),
           ("q3", "q3", "0", {"lazo": "der"}), ("q3", "q3", "1", {"lazo": "der"})],
)

# ------------------------------------------------ ej. 7 (TP I 8): contienen 001 o 100 (AFND)
D["u4-e7-af"] = dict(
    estados={"q0": (0, 1), "q1": (1.8, 0), "q2": (3.6, 0), "q3": (1.8, 2), "q4": (3.6, 2), "q5": (5.4, 1)},
    inicial="q0", finales=["q5"],
    er="(0|1)*(001|100)(0|1)*", sigma="01", cumple=lambda w: "001" in w or "100" in w,
    trans=[("q0", "q0", "0", {"lazo": "abajo"}), ("q0", "q0", "1", {"lazo": "abajo"}),
           ("q0", "q1", "0"), ("q1", "q2", "0"), ("q2", "q5", "1"),
           ("q0", "q3", "1"), ("q3", "q4", "0"), ("q4", "q5", "0"),
           ("q5", "q5", "0", {"lazo": "der"}), ("q5", "q5", "1", {"lazo": "der"})],
)

# ------------------------------------------------ ej. 8 (TP I 14): sin dos unos seguidos
D["u4-e8-af"] = dict(
    estados={"q0": (0, 0), "q1": (2, 0)}, inicial="q0", finales=["q0", "q1"],
    er="(0|10)*(ε|1)", sigma="01", cumple=lambda w: "11" not in w,
    trans=[("q0", "q0", "0"), ("q0", "q1", "1"), ("q1", "q0", "0")],
)

# ------------------------------------------------ ej. 9 (TP I 15): sin 101
D["u4-e9-af"] = dict(
    estados={"q0": (0, 0), "q1": (2, 0), "q2": (4, 0)}, inicial="q0", finales=["q0", "q1", "q2"],
    er="(0|11*00)*(ε|11*(ε|0))", sigma="01", cumple=lambda w: "101" not in w,
    trans=[("q0", "q0", "0"), ("q0", "q1", "1"), ("q1", "q1", "1"), ("q1", "q2", "0"),
           ("q2", "q0", "0", {"curva": 50})],
)

# ------------------------------------------------ ej. 10 (TP I 9): identificadores con guiones
D["u4-e10-af"] = dict(
    estados={"q0": (0, 0), "q1": (2, 0), "q2": (4, 0)}, inicial="q0", finales=["q1"],
    er="L(L|D|G(L|D))*", sigma="LDG",
    cumple=lambda w: w[:1] == "L" and "GG" not in w and not w.endswith("G"),
    trans=[("q0", "q1", "L"), ("q1", "q1", "L"), ("q1", "q1", "D"), ("q1", "q2", "G"),
           ("q2", "q1", "L"), ("q2", "q1", "D")],
)

# ------------------------------------------------ ej. 11 (TP I 28): impar de 0 y par de 1
E28 = "(00|11|(01|10)(00|11)*(01|10))*0|(00|11)*(01|10)(00|11|(01|10)(00|11)*(01|10))*1"
D["u4-e11-af"] = dict(
    estados={"q0": (0, 0), "q1": (2.6, 0), "q2": (0, 2.2), "q3": (2.6, 2.2)}, inicial="q0", finales=["q1"],
    er=E28, sigma="01", cumple=lambda w: w.count("0") % 2 == 1 and w.count("1") % 2 == 0,
    trans=[("q0", "q1", "0"), ("q1", "q0", "0"), ("q2", "q3", "0"), ("q3", "q2", "0"),
           ("q0", "q2", "1"), ("q2", "q0", "1"), ("q1", "q3", "1"), ("q3", "q1", "1")],
)

# ------------------------------------------------ ej. 12 (TP I 66): a...a, impar de a, longitud par (AFND)
E66 = "a(aa|bb)*(ab|ba)(aa|bb|(ab|ba)(aa|bb)*(ab|ba))*a"
D["u4-e12-af"] = dict(
    estados={"q0": (0, 0), "q1": (1.8, 0), "q2": (4.2, 0), "q3": (1.8, 2.2), "q4": (4.2, 2.2), "q5": (6.2, 2.2)},
    inicial="q0", finales=["q5"], er=E66, sigma="ab",
    cumple=lambda w: w[:1] == "a" and w[-1:] == "a" and w.count("a") % 2 == 1 and len(w) % 2 == 0,
    trans=[("q0", "q1", "a"), ("q1", "q2", "a"), ("q2", "q1", "a"), ("q3", "q4", "a"), ("q4", "q3", "a"),
           ("q1", "q3", "b"), ("q3", "q1", "b"), ("q2", "q4", "b"), ("q4", "q2", "b"), ("q4", "q5", "a")],
)

# ------------------------------------------------ cada ER contra su definición
import re as _re
from itertools import product as _product
for _n, _d in D.items():
    _r = _re.compile("(?:" + _d["er"].replace("ε", "").replace("(", "(?:") + ")")
    for _k in range(9):
        for _t in _product(_d["sigma"], repeat=_k):
            _w = "".join(_t)
            if bool(_r.fullmatch(_w)) != _d["cumple"](_w):
                raise ValueError(f"{_n}: la ER no coincide con la definición en '{_w}'")
