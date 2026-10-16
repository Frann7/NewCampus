# Autómatas de la teoría de las cuatro unidades (las prácticas tienen su archivo: u2.py, u3.py, u4.py).
# python fuentes/automatas.py fuentes/pyl/diagramas/teoria.py
# python fuentes/automatas.py --verificar fuentes/pyl/diagramas/teoria.py


def nv(*t):
    return (*t, {"nueva": True})


# ===================================================================== Unidad 1
D["u1-par-a"] = dict(
    estados={"q0": (0, 0), "q1": (2, 0)}, inicial="q0", finales=["q0"], er="(b|ab*a)*", sigma="ab",
    trans=[("q0", "q1", "a"), ("q1", "q0", "a"), ("q0", "q0", "b"), ("q1", "q1", "b")],
    alt="AFD de las cadenas con cantidad par de a",
)
D["u1-empieza-a"] = dict(
    estados={"q0": (0, 0), "q1": (2, 0), "qm": (0, 1.7)}, inicial="q0", finales=["q1"], muertos=["qm"],
    er="a(a|b)*", sigma="ab",
    trans=[("q0", "q1", "a"), ("q1", "q1", "a"), ("q1", "q1", "b"), ("q0", "qm", "b"),
           ("qm", "qm", "a", {"lazo": "der"}), ("qm", "qm", "b", {"lazo": "der"})],
    alt="AFD de las cadenas que empiezan con a, con su estado muerto",
)
D["u1-termina-ab"] = dict(
    estados={"q0": (0, 0), "q1": (1.9, 0), "q2": (3.8, 0)}, inicial="q0", finales=["q2"],
    er="(a|b)*ab", sigma="ab",
    trans=[("q0", "q0", "b"), ("q0", "q1", "a"), ("q1", "q1", "a"), ("q1", "q2", "b"),
           ("q2", "q1", "a", {"curva": -40}), ("q2", "q0", "b", {"curva": 55})],
    alt="AFD de las cadenas que terminan en ab",
)
D["u1-afnd-ab"] = dict(
    estados={"q0": (0, 0), "q1": (1.9, 0), "q2": (3.8, 0)}, inicial="q0", finales=["q2"],
    er="(a|b)*ab(a|b)*", sigma="ab",
    trans=[("q0", "q0", "a"), ("q0", "q0", "b"), ("q0", "q1", "a"), ("q1", "q2", "b"),
           ("q2", "q2", "a"), ("q2", "q2", "b")],
    alt="AFND de las cadenas que contienen ab",
)
D["u1-afne"] = dict(
    estados={"q0": (0, 0), "q1": (2, 0)}, inicial="q0", finales=["q1"], er="a*b*", sigma="ab",
    trans=[("q0", "q0", "a"), ("q0", "q1", "ε"), ("q1", "q1", "b")],
    alt="AFN-ε de a*b*",
)

# ===================================================================== Unidad 2
# la regla α β* γ
D["u2-regla-antes"] = dict(
    estados={"q": (0, 0), "t": (1.9, 0), "p": (3.8, 0)}, inicial=None, finales=[], marcados=["t"],
    trans=[("q", "t", "α"), ("t", "t", "β"), ("t", "p", "γ")],
    alt="Un estado t con entrada α, lazo β y salida γ",
)
D["u2-regla-despues"] = dict(
    estados={"q": (0, 0), "p": (3.8, 0)}, inicial=None, finales=[],
    trans=[nv("q", "p", "αβ*γ")],
    alt="Después de eliminar t queda una sola transición αβ*γ",
)
# ejemplo chico: termina en ab
D["u2-ej1-af"] = dict(D["u1-termina-ab"], er="(a|b)*ab")
D["u2-ej1-paso1"] = dict(
    estados={"i": (-1.3, 0), "q0": (0, 0), "q1": (1.9, 0), "q2": (3.8, 0), "f": (5.2, 0)},
    inicial="i", finales=["f"], marcados=["q1"], er="(a|b)*ab", sigma="ab",
    trans=[nv("i", "q0", "ε"), ("q0", "q0", "b"), ("q0", "q1", "a"), ("q1", "q1", "a"), ("q1", "q2", "b"),
           ("q2", "q1", "a", {"curva": -40}), ("q2", "q0", "b", {"curva": 55}), nv("q2", "f", "ε")],
)
D["u2-ej1-paso2"] = dict(
    estados={"i": (-1.3, 0), "q0": (0, 0), "q2": (2.6, 0), "f": (4.2, 0)},
    inicial="i", finales=["f"], marcados=["q0"], er="(a|b)*ab", sigma="ab",
    trans=[("i", "q0", "ε"), ("q0", "q0", "b"), nv("q0", "q2", "aa*b"), nv("q2", "q2", "aa*b"),
           ("q2", "q0", "b", {"curva": 45}), ("q2", "f", "ε")],
)
D["u2-ej1-paso3"] = dict(
    estados={"i": (-1.3, 0), "q2": (1.6, 0), "f": (3.4, 0)},
    inicial="i", finales=["f"], marcados=["q2"], er="(a|b)*ab", sigma="ab",
    trans=[nv("i", "q2", "b*aa*b"), nv("q2", "q2", "aa*b|bb*aa*b"), ("q2", "f", "ε")],
)
D["u2-ej1-er"] = dict(
    estados={"i": (0, 0), "f": (4.0, 0)}, inicial="i", finales=["f"], er="(a|b)*ab", sigma="ab",
    trans=[nv("i", "f", "b*aa*b(aa*b|bb*aa*b)*")],
)

# ===================================================================== Unidad 3
D["u3-th-eps"] = dict(estados={"i": (0, 0), "f": (1.6, 0)}, inicial="i", finales=["f"], trans=[("i", "f", "ε")],
                      alt="Thompson para ε")
D["u3-th-a"] = dict(estados={"i": (0, 0), "f": (1.6, 0)}, inicial="i", finales=["f"], trans=[("i", "f", "a")],
                    alt="Thompson para un símbolo")
D["u3-th-union"] = thompson("a|b", alt="Thompson para a|b")
D["u3-th-concat"] = thompson("ab", alt="Thompson para ab")
D["u3-th-estrella"] = thompson("a*", alt="Thompson para a*")
D["u3-th-ej"] = thompson("ab*", er="ab*", sigma="ab")
D["u3-th-ej2"] = thompson("(a|b)c", er="(a|b)c", sigma="abc")
D["u3-sub-ej-afd"] = dict(
    estados={"A": (0, 0), "B": (1.9, 0), "C": (3.8, 0), "∅": (1.9, 1.7)},
    inicial="A", finales=["B", "C"], muertos=["∅"], er="ab*", sigma="ab",
    trans=[("A", "B", "a"), ("A", "∅", "b"), ("B", "C", "b"), ("B", "∅", "a"), ("C", "C", "b", {"lazo": "der"}),
           ("C", "∅", "a"), ("∅", "∅", "a", {"lazo": "abajo"}), ("∅", "∅", "b", {"lazo": "abajo"})],
)
D["u3-min-ej"] = dict(
    estados={"A": (0, 0), "B": (1.9, 0), "∅": (1.9, 1.7)},
    inicial="A", finales=["B"], muertos=["∅"], er="ab*", sigma="ab",
    trans=[("A", "B", "a"), ("A", "∅", "b"), ("B", "B", "b", {"lazo": "der"}), ("B", "∅", "a"),
           ("∅", "∅", "a", {"lazo": "abajo"}), ("∅", "∅", "b", {"lazo": "abajo"})],
)

# ===================================================================== Unidad 4
D["u4-empieza"] = dict(
    estados={"q0": (0, 0), "q1": (1.8, 0), "q2": (3.6, 0)}, inicial="q0", finales=["q2"],
    er="ab(a|b)*", sigma="ab",
    trans=[("q0", "q1", "a"), ("q1", "q2", "b"), ("q2", "q2", "a"), ("q2", "q2", "b")],
    alt="Empiezan con ab",
)
D["u4-termina"] = dict(D["u1-termina-ab"], alt="Terminan en ab")
D["u4-contiene"] = dict(
    estados={"q0": (0, 0), "q1": (1.9, 0), "q2": (3.8, 0)}, inicial="q0", finales=["q2"],
    er="(a|b)*ab(a|b)*", sigma="ab",
    trans=[("q0", "q0", "b"), ("q0", "q1", "a"), ("q1", "q1", "a"), ("q1", "q2", "b"),
           ("q2", "q2", "a"), ("q2", "q2", "b")],
    alt="Contienen ab (AFD)",
)
D["u4-no-contiene"] = dict(
    estados={"q0": (0, 0), "q1": (1.9, 0), "q2": (3.8, 0)}, inicial="q0", finales=["q0", "q1"], muertos=["q2"],
    er="b*a*", sigma="ab",
    trans=[("q0", "q0", "b"), ("q0", "q1", "a"), ("q1", "q1", "a"), ("q1", "q2", "b"),
           ("q2", "q2", "a"), ("q2", "q2", "b")],
    alt="No contienen ab: el mismo AFD con los finales al revés",
)
D["u4-paridad"] = dict(
    estados={"P": (0, 0), "I": (2, 0)}, inicial="P", finales=["P"], er="(0|1(0)*1)*", sigma="01",
    trans=[("P", "I", "1"), ("I", "P", "1"), ("P", "P", "0"), ("I", "I", "0")],
    alt="Cantidad par de 1",
)
D["u4-longitud"] = dict(
    estados={"q0": (0, 0), "q1": (1.8, 0), "q2": (3.6, 0)}, inicial="q0", finales=["q0"],
    er="((a|b)(a|b)(a|b))*", sigma="ab",
    trans=[("q0", "q1", "a"), ("q0", "q1", "b"), ("q1", "q2", "a"), ("q1", "q2", "b"),
           ("q2", "q0", "a", {"curva": -45}), ("q2", "q0", "b", {"curva": -45})],
    alt="Longitud múltiplo de 3",
)
# combinar: empieza con a Y cantidad par de b
D["u4-combina"] = dict(
    estados={"q0": (0, 0.9), "P": (1.9, 0.9), "I": (3.9, 0.9)}, inicial="q0", finales=["P"],
    er="a(a|ba*b)*", sigma="ab",
    trans=[("q0", "P", "a"), ("P", "P", "a"), ("P", "I", "b"), ("I", "P", "b"), ("I", "I", "a")],
    alt="Empiezan con a y tienen cantidad par de b",
)
D["u4-union"] = dict(
    estados={"i": (0, 1.1), "p0": (1.5, 0), "p1": (3.1, 0), "p2": (4.7, 0),
             "r0": (1.5, 2.2), "r1": (3.1, 2.2), "r2": (4.7, 2.2)},
    inicial="i", finales=["p2", "r2"], er="aa(a|b)*|(a|b)*bb", sigma="ab",
    trans=[("i", "p0", "ε"), ("p0", "p1", "a"), ("p1", "p2", "a"),
           ("p2", "p2", "a", {"lazo": "der"}), ("p2", "p2", "b", {"lazo": "der"}),
           ("i", "r0", "ε"), ("r0", "r0", "a", {"lazo": "abajo"}), ("r0", "r0", "b", {"lazo": "abajo"}),
           ("r0", "r1", "b"), ("r1", "r2", "b")],
    alt="AFN-ε: empiezan con aa o terminan con bb",
)
D["u4-par-par"] = dict(
    estados={"PP": (0, 0), "IP": (2.2, 0), "PI": (0, 2), "II": (2.2, 2)},
    inicial="PP", finales=["PP"], sigma="ab",
    cumple=lambda w: w.count("a") % 2 == 0 and w.count("b") % 2 == 0,
    trans=[("PP", "IP", "a"), ("IP", "PP", "a"), ("PI", "II", "a"), ("II", "PI", "a"),
           ("PP", "PI", "b"), ("PI", "PP", "b"), ("IP", "II", "b"), ("II", "IP", "b")],
    alt="Cantidad par de a y cantidad par de b",
)

# pensar por ramas: empiezan con aa o con b, y tienen cantidad par de b
D["u4-ramas"] = dict(
    estados={"q0": (0, 1.1), "r1": (1.6, 0), "R": (3.2, 0), "S": (5.0, 0),
             "T": (1.6, 2.2), "U": (3.4, 2.2)},
    inicial="q0", finales=["R", "U"], er="(aa|ba*b)(a|ba*b)*", sigma="ab",
    trans=[("q0", "r1", "a"), ("r1", "R", "a"), ("R", "R", "a"), ("R", "S", "b"), ("S", "R", "b"),
           ("S", "S", "a"), ("q0", "T", "b"), ("T", "T", "a", {"lazo": "abajo"}), ("T", "U", "b"),
           ("U", "T", "b"), ("U", "U", "a", {"lazo": "abajo"})],
    alt="Por ramas: una rama para los que empiezan con aa y otra para los que empiezan con b",
)
D["u4-ramas-junto"] = dict(
    estados={"q0": (0, 1.1), "r1": (1.6, 0), "P": (3.2, 0), "I": (3.2, 2.2)},
    inicial="q0", finales=["P"], er="(aa|ba*b)(a|ba*b)*", sigma="ab",
    trans=[("q0", "r1", "a"), ("r1", "P", "a"), ("P", "P", "a", {"lazo": "der"}), ("P", "I", "b"),
           ("I", "P", "b"), ("I", "I", "a", {"lazo": "der"}), ("q0", "I", "b")],
    alt="Las dos ramas juntas: R y U son el mismo estado (par), S y T también (impar)",
)
