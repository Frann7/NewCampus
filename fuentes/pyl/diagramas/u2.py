# Autómatas de la Unidad 2 (De AF a ER).
# python fuentes/automatas.py fuentes/pyl/diagramas/u2.py
# python fuentes/automatas.py --verificar fuentes/pyl/diagramas/u2.py
#
# Cada ejercicio: u2-eN-af (el autómata dado) y u2-eN-pasoK (cómo queda después
# del Paso K del fragmento). Todos llevan la ER final: el lenguaje no cambia de
# paso a paso. Verde: la transición recién creada; celeste: el que se elimina después.

N = "nueva"


def nv(*t):
    """Una transición recién creada (se dibuja en verde)."""
    return (*t, {N: True})


def sin(pos, *fuera):
    return {k: v for k, v in pos.items() if k not in fuera}


# ------------------------------------------------ ejercicio 1: lineal con un lazo
E1 = "ab*ab"
_p = {"q0": (0, 0), "q1": (1.8, 0), "q2": (3.6, 0), "q3": (5.4, 0)}
D["u2-e1-af"] = dict(
    estados=_p, inicial="q0", finales=["q3"], er=E1, sigma="ab",
    trans=[("q0", "q1", "a"), ("q1", "q1", "b"), ("q1", "q2", "a"), ("q2", "q3", "b")],
    alt="Autómata del ejercicio 1",
)
_p = dict(_p, i=(-1.4, 0), f=(6.8, 0))
D["u2-e1-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q0"], er=E1, sigma="ab",
    trans=[nv("i", "q0", "ε"), ("q0", "q1", "a"), ("q1", "q1", "b"), ("q1", "q2", "a"), ("q2", "q3", "b"),
           nv("q3", "f", "ε")],
)
_p = sin(_p, "q0")
D["u2-e1-paso3"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=E1, sigma="ab",
    trans=[nv("i", "q1", "a"), ("q1", "q1", "b"), ("q1", "q2", "a"), ("q2", "q3", "b"), ("q3", "f", "ε")],
)
_p = sin(_p, "q1")
D["u2-e1-paso4"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q2"], er=E1, sigma="ab",
    trans=[nv("i", "q2", "ab*a"), ("q2", "q3", "b"), ("q3", "f", "ε")],
)
_p = sin(_p, "q2")
D["u2-e1-paso5"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q3"], er=E1, sigma="ab",
    trans=[nv("i", "q3", "ab*ab"), ("q3", "f", "ε")],
)
D["u2-e1-paso6"] = dict(
    estados={"i": (0, 0), "f": (2.6, 0)}, inicial="i", finales=["f"], er=E1, sigma="ab",
    trans=[nv("i", "f", "ab*ab")],
)

# ------------------------------------------------ ejercicio 2: ida y vuelta
E2 = "a(ba)*bb"
_p = {"q0": (0, 0), "q1": (1.8, 0), "q2": (3.6, 0), "q3": (5.4, 0)}
D["u2-e2-af"] = dict(
    estados=_p, inicial="q0", finales=["q3"], er=E2, sigma="ab",
    trans=[("q0", "q1", "a"), ("q1", "q2", "b"), ("q2", "q1", "a"), ("q2", "q3", "b")],
    alt="Autómata del ejercicio 2",
)
_p = dict(_p, i=(-1.4, 0), f=(6.8, 0))
D["u2-e2-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q0"], er=E2, sigma="ab",
    trans=[nv("i", "q0", "ε"), ("q0", "q1", "a"), ("q1", "q2", "b"), ("q2", "q1", "a"), ("q2", "q3", "b"),
           nv("q3", "f", "ε")],
)
_p = sin(_p, "q0")
D["u2-e2-paso3"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q3"], er=E2, sigma="ab",
    trans=[nv("i", "q1", "a"), ("q1", "q2", "b"), ("q2", "q1", "a"), ("q2", "q3", "b"), ("q3", "f", "ε")],
)
_p = sin(_p, "q3")
D["u2-e2-paso4"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q2"], er=E2, sigma="ab",
    trans=[("i", "q1", "a"), ("q1", "q2", "b"), ("q2", "q1", "a"), nv("q2", "f", "b")],
)
_p = sin(_p, "q2")
D["u2-e2-paso5"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=E2, sigma="ab",
    trans=[("i", "q1", "a"), nv("q1", "q1", "ba"), nv("q1", "f", "bb")],
)
D["u2-e2-paso6"] = dict(
    estados={"i": (0, 0), "f": (2.8, 0)}, inicial="i", finales=["f"], er=E2, sigma="ab",
    trans=[nv("i", "f", "a(ba)*bb")],
)

# ------------------------------------------------ ejercicio 3: dos estados finales
E3 = "ba|(a|baa)b*"
_p = {"q0": (0, 1), "q1": (2.6, 0), "q2": (1.3, 2.2), "q3": (2.6, 2.2)}
D["u2-e3-af"] = dict(
    estados=_p, inicial="q0", finales=["q1", "q3"], er=E3, sigma="ab",
    trans=[("q0", "q1", "a"), ("q1", "q1", "b"), ("q0", "q2", "b"), ("q2", "q3", "a"), ("q3", "q1", "a")],
    alt="Autómata del ejercicio 3",
)
_p = dict(_p, i=(-1.4, 1), f=(4.2, 1.1))
D["u2-e3-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q2"], er=E3, sigma="ab",
    trans=[nv("i", "q0", "ε"), ("q0", "q1", "a"), ("q1", "q1", "b"), ("q0", "q2", "b"), ("q2", "q3", "a"),
           ("q3", "q1", "a"), nv("q1", "f", "ε"), nv("q3", "f", "ε")],
)
_p = sin(_p, "q2")
D["u2-e3-paso3"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q3"], er=E3, sigma="ab",
    trans=[("i", "q0", "ε"), ("q0", "q1", "a"), ("q1", "q1", "b"), nv("q0", "q3", "ba"),
           ("q3", "q1", "a"), ("q1", "f", "ε"), ("q3", "f", "ε")],
)
_p = sin(_p, "q3")
D["u2-e3-paso4"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=E3, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "q1", "a|baa"), ("q1", "q1", "b"), nv("q0", "f", "ba"), ("q1", "f", "ε")],
)
D["u2-e3-paso5"] = dict(
    estados={"i": (-1.4, 0), "q0": (0, 0), "f": (3.6, 0)}, inicial="i", finales=["f"], marcados=["q0"],
    er=E3, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "f", "ba|(a|baa)b*")],
)
D["u2-e3-paso6"] = dict(
    estados={"i": (0, 0), "f": (3.6, 0)}, inicial="i", finales=["f"], er=E3, sigma="ab",
    trans=[nv("i", "f", "ba|(a|baa)b*")],
)

# ------------------------------------------------ ejercicio 4: con un estado muerto
E4 = "aba*b(b|aa*b)*"
_p = {"q0": (0, 0), "q1": (1.8, 0), "q2": (3.6, 0), "q4": (5.4, 0), "q3": (1.8, 1.8)}
D["u2-e4-af"] = dict(
    estados=_p, inicial="q0", finales=["q4"], er=E4, sigma="ab",
    trans=[("q0", "q1", "a"), ("q0", "q3", "b"), ("q1", "q2", "b"), ("q1", "q3", "a"),
           ("q2", "q2", "a"), ("q2", "q4", "b"), ("q4", "q2", "a"), ("q4", "q4", "b"),
           ("q3", "q3", "a", {"lazo": "abajo"}), ("q3", "q3", "b", {"lazo": "abajo"})],
    alt="Autómata del ejercicio 4",
)
D["u2-e4-paso1"] = dict(D["u2-e4-af"], muertos=["q3"], alt="El mismo autómata con el estado muerto q3 en gris")
_p = dict(sin(_p, "q3"), i=(-1.4, 0), f=(6.8, 0))
D["u2-e4-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q0"], er=E4, sigma="ab",
    trans=[nv("i", "q0", "ε"), ("q0", "q1", "a"), ("q1", "q2", "b"), ("q2", "q2", "a"), ("q2", "q4", "b"),
           ("q4", "q2", "a"), ("q4", "q4", "b"), nv("q4", "f", "ε")],
)
_p = sin(_p, "q0")
D["u2-e4-paso3"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=E4, sigma="ab",
    trans=[nv("i", "q1", "a"), ("q1", "q2", "b"), ("q2", "q2", "a"), ("q2", "q4", "b"),
           ("q4", "q2", "a"), ("q4", "q4", "b"), ("q4", "f", "ε")],
)
_p = sin(_p, "q1")
D["u2-e4-paso4"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q2"], er=E4, sigma="ab",
    trans=[nv("i", "q2", "ab"), ("q2", "q2", "a"), ("q2", "q4", "b"),
           ("q4", "q2", "a"), ("q4", "q4", "b"), ("q4", "f", "ε")],
)
_p = sin(_p, "q2")
D["u2-e4-paso5"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q4"], er=E4, sigma="ab",
    trans=[nv("i", "q4", "aba*b"), nv("q4", "q4", "b|aa*b"), ("q4", "f", "ε")],
)
D["u2-e4-paso6"] = dict(
    estados={"i": (0, 0), "f": (3.4, 0)}, inicial="i", finales=["f"], er=E4, sigma="ab",
    trans=[nv("i", "f", "aba*b(b|aa*b)*")],
)

# ------------------------------------------------ ejercicio 5: AFN con una ε
E5 = "(ab|ab*a)*(ab|ab*a)"
_p = {"q0": (0, 1), "q1": (2, 0), "q2": (2, 2), "q3": (4, 1)}
_t = [("q0", "q1", "a"), ("q0", "q2", "a"), ("q1", "q1", "b"), ("q1", "q3", "a"), ("q2", "q3", "b"),
      ("q3", "q0", "ε")]
D["u2-e5-af"] = dict(
    estados=_p, inicial="q0", finales=["q3"], er=E5, sigma="ab", trans=_t,
    alt="Autómata del ejercicio 5",
)
_p = dict(_p, i=(-1.4, 1), f=(5.4, 1))
D["u2-e5-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q2"], er=E5, sigma="ab",
    trans=[nv("i", "q0", "ε")] + _t + [nv("q3", "f", "ε")],
)
_p = sin(_p, "q2")
D["u2-e5-paso3"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=E5, sigma="ab",
    trans=[("i", "q0", "ε"), ("q0", "q1", "a"), ("q1", "q1", "b"), ("q1", "q3", "a"), nv("q0", "q3", "ab"),
           ("q3", "q0", "ε"), ("q3", "f", "ε")],
)
_p = sin(_p, "q1")
D["u2-e5-paso4"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q3"], er=E5, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "q3", "ab|ab*a"), ("q3", "q0", "ε"), ("q3", "f", "ε")],
)
D["u2-e5-paso5"] = dict(
    estados={"i": (-1.4, 0), "q0": (0, 0), "f": (3, 0)}, inicial="i", finales=["f"], marcados=["q0"],
    er=E5, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "q0", "ab|ab*a"), nv("q0", "f", "ab|ab*a")],
)
D["u2-e5-paso6"] = dict(
    estados={"i": (0, 0), "f": (3.6, 0)}, inicial="i", finales=["f"], er=E5, sigma="ab",
    trans=[nv("i", "f", "(ab|ab*a)*(ab|ab*a)")],
)

# ------------------------------------------------ ejercicio 6: forma de parcial
E6 = "(1|00*1)(10|010*1)*(1|00(0|1)*)"
E6B = "1(10)*1|1(10)*00(0|1)*|(0|1(10)*01)(0|1(10)*01)*(1(10)*1|1(10)*00(0|1)*)"
_p = {"q0": (0, 1.2), "q1": (1.6, 0), "q2": (1.8, 2.4), "q3": (3.4, 1.2), "q4": (5, 1.2), "q5": (3.9, 3.1)}
_t = [("q0", "q1", "0"), ("q0", "q2", "1"), ("q1", "q1", "0"), ("q1", "q2", "1"), ("q2", "q3", "0"),
      ("q3", "q1", "1"), ("q3", "q4", "0"), ("q4", "q4", "0"), ("q4", "q4", "1"), ("q2", "q5", "1"),
      ("q5", "q2", "0")]
D["u2-e6-af"] = dict(
    estados=_p, inicial="q0", finales=["q4", "q5"], er=E6, sigma="01", trans=_t,
    alt="Autómata del ejercicio 6",
)
_p = dict(_p, i=(-1.4, 1.2), f=(6.5, 2.4))
D["u2-e6-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q4"], er=E6, sigma="01",
    trans=[nv("i", "q0", "ε")] + _t + [nv("q4", "f", "ε"), nv("q5", "f", "ε")],
)
_p = sin(_p, "q4")
_t = [("i", "q0", "ε"), ("q0", "q1", "0"), ("q0", "q2", "1"), ("q1", "q1", "0"), ("q1", "q2", "1"),
      ("q2", "q3", "0"), ("q3", "q1", "1")]
D["u2-e6-paso3"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q5"], er=E6, sigma="01",
    trans=_t + [nv("q3", "f", "0(0|1)*"), ("q2", "q5", "1"), ("q5", "q2", "0"), ("q5", "f", "ε")],
)
_p = sin(_p, "q5")
_t = _t + [("q3", "f", "0(0|1)*")]
D["u2-e6-paso4"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q0"], er=E6, sigma="01",
    trans=_t + [nv("q2", "q2", "10", {"lazo": "abajo"}), nv("q2", "f", "1")],
)
_p = sin(_p, "q0")
_t = [("q1", "q1", "0"), ("q1", "q2", "1"), ("q2", "q3", "0"), ("q3", "q1", "1"), ("q3", "f", "0(0|1)*"),
      ("q2", "q2", "10", {"lazo": "abajo"}), ("q2", "f", "1")]
D["u2-e6-paso5"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q3"], er=E6, sigma="01",
    trans=[nv("i", "q1", "0"), nv("i", "q2", "1")] + _t,
)
_p = sin(_p, "q3")
D["u2-e6-paso6"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=E6, sigma="01",
    trans=[("i", "q1", "0"), ("i", "q2", "1"), ("q1", "q1", "0"), ("q1", "q2", "1"),
           ("q2", "q2", "10", {"lazo": "abajo"}), nv("q2", "q1", "01"), nv("q2", "f", "1|00(0|1)*")],
)
_p = {"i": (0, 0), "q2": (2.6, 0), "f": (6.2, 0)}
D["u2-e6-paso7"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q2"], er=E6, sigma="01",
    trans=[nv("i", "q2", "1|00*1"), nv("q2", "q2", "10|010*1"), ("q2", "f", "1|00(0|1)*")],
)
D["u2-e6-paso8"] = dict(
    estados={"i": (0, 0), "f": (5.4, 0)}, inicial="i", finales=["f"], er=E6, sigma="01",
    trans=[nv("i", "f", "(1|00*1)(10|010*1)*(1|00(0|1)*)")],
)
# Orden B: desde el paso 5, q2 antes que q3 y q1.
_pb = {"i": (0, 2.6), "q1": (2.7, 0), "q3": (2.7, 1.8), "f": (5.4, 2.6)}
D["u2-e6-b-paso6"] = dict(
    estados=_pb, inicial="i", finales=["f"], marcados=["q3"], er=E6, sigma="01",
    trans=[("i", "q1", "0"), ("q1", "q1", "0"), ("q3", "q1", "1"), ("q3", "f", "0(0|1)*"),
           nv("i", "q3", "1(10)*0"), nv("i", "f", "1(10)*1"), nv("q1", "q3", "1(10)*0"), nv("q1", "f", "1(10)*1")],
)
_pb = {"i": (0, 1.4), "q1": (3, 0), "f": (6.4, 1.4)}
D["u2-e6-b-paso7"] = dict(
    estados=_pb, inicial="i", finales=["f"], marcados=["q1"], er=E6, sigma="01",
    trans=[nv("i", "q1", "0|1(10)*01"), nv("q1", "q1", "0|1(10)*01"),
           nv("i", "f", "1(10)*1|1(10)*00(0|1)*"), nv("q1", "f", "1(10)*1|1(10)*00(0|1)*")],
)
D["u2-e6-b-paso8"] = dict(
    estados={"i": (0, 0), "f": (9.6, 0)}, inicial="i", finales=["f"], er=E6B, sigma="01",
    trans=[nv("i", "f", E6B)],
)
