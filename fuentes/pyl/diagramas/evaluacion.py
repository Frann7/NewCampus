# Autómatas de los parciales (app/contenido/pyl/evaluacion/parciales/).
# python fuentes/automatas.py fuentes/pyl/diagramas/evaluacion.py            -> los mete en los fragmentos
# python fuentes/automatas.py --verificar fuentes/pyl/diagramas/evaluacion.py -> los prueba contra su ER

N = "nueva"


def nv(*t):
    """Una transición recién creada (se dibuja en verde)."""
    return (*t, {N: True})


# =============================================================== 2023 parcial
P23_ER = "(00*1|1)(01)*0(ε|0(0|1)*)"
P23_POS = {"q0": (0, 1.4), "q1": (1.5, 0.4), "q4": (2.6, 1.6), "q5": (4.3, 1.6), "q3": (3.9, 0.2)}

D["p23-af"] = dict(
    estados=P23_POS, inicial="q0", finales=["q3", "q5"], er=P23_ER, sigma="01",
    trans=[("q0", "q1", "0"), ("q0", "q4", "1"), ("q1", "q1", "0"), ("q1", "q4", "1"),
           ("q4", "q5", "0"), ("q5", "q4", "1"), ("q5", "q3", "0"), ("q3", "q3", "0"), ("q3", "q3", "1")],
    alt="Autómata del ejercicio 1 del parcial 2023",
)
_p = dict(P23_POS, i=(-1.3, 1.4), f=(5.6, 0.9))
D["p23-paso1"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=P23_ER, sigma="01",
    trans=[nv("i", "q0", "ε"), ("q0", "q1", "0"), ("q0", "q4", "1"), ("q1", "q1", "0"), ("q1", "q4", "1"),
           ("q4", "q5", "0"), ("q5", "q4", "1"), ("q5", "q3", "0"), ("q3", "q3", "0"), ("q3", "q3", "1"),
           nv("q3", "f", "ε"), nv("q5", "f", "ε")],
)
_p = {k: v for k, v in _p.items() if k != "q1"}
D["p23-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q3"], er=P23_ER, sigma="01",
    trans=[("i", "q0", "ε"), nv("q0", "q4", "00*1|1"),
           ("q4", "q5", "0"), ("q5", "q4", "1"), ("q5", "q3", "0"), ("q3", "q3", "0"), ("q3", "q3", "1"),
           ("q3", "f", "ε"), ("q5", "f", "ε")],
)
_p = {k: v for k, v in _p.items() if k != "q3"}
D["p23-paso3"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q5"], er=P23_ER, sigma="01",
    trans=[("i", "q0", "ε"), ("q0", "q4", "00*1|1"),
           ("q4", "q5", "0"), ("q5", "q4", "1"), nv("q5", "f", "ε|0(0|1)*")],
)
_p = {"i": (-1.3, 1.4), "q0": (0, 1.4), "q4": (2.6, 1.4), "f": (5.6, 1.4)}
D["p23-paso4"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q4"], er=P23_ER, sigma="01",
    trans=[("i", "q0", "ε"), ("q0", "q4", "00*1|1"), nv("q4", "q4", "01"), nv("q4", "f", "0(ε|0(0|1)*)")],
)
D["p23-paso5"] = dict(
    estados={"i": (-1.3, 0), "q0": (0, 0), "f": (4.6, 0)}, inicial="i", finales=["f"], marcados=["q0"],
    er=P23_ER, sigma="01",
    trans=[("i", "q0", "ε"), nv("q0", "f", "(00*1|1)(01)*0(ε|0(0|1)*)")],
)
D["p23-er"] = dict(
    estados={"i": (0, 0), "f": (4.6, 0)}, inicial="i", finales=["f"], er=P23_ER, sigma="01",
    trans=[nv("i", "f", "(00*1|1)(01)*0(ε|0(0|1)*)")],
)

# ej. 2: b(a*|b)|a
D["p23-thompson"] = thompson("b(a*|b)|a", er="b(a*|b)|a", sigma="ab")
D["p23-afd"] = dict(
    estados={"A": (0, 1.2), "B": (2, 0), "C": (2, 2.4), "D": (4, 2.4), "E": (4, 1.2), "∅": (4, 0)},
    inicial="A", finales=["B", "C", "D", "E"], muertos=["∅"], er="b(a*|b)|a", sigma="ab",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("C", "D", "a"), ("C", "E", "b"), ("D", "D", "a", {"lazo": "der"}),
           ("D", "∅", "b", {"curva": -40}), ("B", "∅", "a"), ("B", "∅", "b"), ("E", "∅", "a"), ("E", "∅", "b"),
           ("∅", "∅", "a"), ("∅", "∅", "b")],
)
D["p23-min"] = dict(
    estados={"A": (0, 1.2), "B": (2, 0), "C": (2, 2.4), "D": (4, 2.4), "∅": (4, 0)},
    inicial="A", finales=["B", "C", "D"], muertos=["∅"], er="b(a*|b)|a", sigma="ab",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("C", "D", "a"), ("C", "B", "b"), ("D", "D", "a", {"lazo": "der"}),
           ("D", "∅", "b"), ("B", "∅", "a"), ("B", "∅", "b"), ("∅", "∅", "a", {"lazo": "der"}), ("∅", "∅", "b", {"lazo": "der"})],
)

# ej. 3: identificadores sobre {M, N, D, o}
D["p23-ident"] = dict(
    estados={"q0": (0, 0), "q1": (1.9, 0), "q2": (3.8, 0)}, inicial="q0", finales=["q2"],
    er="M(M|N|D)*M", sigma="MNDo",
    trans=[("q0", "q1", "M"), ("q1", "q1", "N"), ("q1", "q1", "D"), ("q1", "q2", "M"),
           ("q2", "q2", "M"), ("q2", "q1", "N"), ("q2", "q1", "D")],
)

# ======================================================== 2023 recuperatorio
R23_ER = "(ab|ba)(ab)*(ε|b(a|b)*)"
R23_POS = {"q0": (0, 1.5), "q2": (2.2, 0.1), "q1": (2.2, 3.0), "q4": (2.9, 1.6), "q3": (4.8, 1.6), "q5": (4.7, 0.1)}
_t = [("q0", "q2", "b"), ("q0", "q1", "a"), ("q2", "q3", "a"), ("q1", "q3", "b"), ("q3", "q1", "a"),
      ("q3", "q5", "b"), ("q5", "q5", "a"), ("q5", "q5", "b")]
D["r23-af"] = dict(
    estados=R23_POS, inicial="q0", finales=["q3", "q5"], er=R23_ER, sigma="ab",
    trans=_t + [("q2", "q4", "b"), ("q1", "q4", "a"), ("q4", "q4", "a", {"lazo": "der"}), ("q4", "q4", "b", {"lazo": "der"})],
    alt="Autómata del ejercicio 1 del recuperatorio 2023",
)
D["r23-muerto"] = dict(D["r23-af"], muertos=["q4"])
_p = {k: v for k, v in R23_POS.items() if k != "q4"}
_p.update(i=(-1.3, 1.5), f=(6.2, 0.9))
D["r23-paso1"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q5"], er=R23_ER, sigma="ab",
    trans=[nv("i", "q0", "ε")] + _t + [nv("q3", "f", "ε"), nv("q5", "f", "ε")],
)
_p = {k: v for k, v in _p.items() if k != "q5"}
D["r23-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q2"], er=R23_ER, sigma="ab",
    trans=[("i", "q0", "ε")] + _t[:5] + [nv("q3", "f", "ε|b(a|b)*")],
)
_p = {k: v for k, v in _p.items() if k != "q2"}
D["r23-paso3"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=R23_ER, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "q3", "ba"), ("q0", "q1", "a"), ("q1", "q3", "b"), ("q3", "q1", "a"),
           ("q3", "f", "ε|b(a|b)*")],
)
_p = {"i": (-1.3, 1.5), "q0": (0, 1.5), "q3": (2.6, 1.5), "f": (5.6, 1.5)}
D["r23-paso4"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q3"], er=R23_ER, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "q3", "ba|ab"), nv("q3", "q3", "ab"), ("q3", "f", "ε|b(a|b)*")],
)
D["r23-paso5"] = dict(
    estados={"i": (-1.3, 0), "q0": (0, 0), "f": (4.4, 0)}, inicial="i", finales=["f"], marcados=["q0"],
    er=R23_ER, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "f", "(ba|ab)(ab)*(ε|b(a|b)*)")],
)
D["r23-er"] = dict(
    estados={"i": (0, 0), "f": (4.4, 0)}, inicial="i", finales=["f"], er=R23_ER, sigma="ab",
    trans=[nv("i", "f", "(ba|ab)(ab)*(ε|b(a|b)*)")],
)

# ej. 2: (a*|b*)|ab*
D["r23-thompson"] = thompson("(a*|b*)|ab*", er="(a*|b*)|ab*", sigma="ab")
D["r23-afd"] = dict(
    estados={"A": (0, 1.2), "B": (2, 0), "C": (2, 2.4), "D": (4, 0), "E": (4, 1.2), "∅": (4, 2.4)},
    inicial="A", finales=["A", "B", "C", "D", "E"], muertos=["∅"], er="(a*|b*)|ab*", sigma="ab",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("B", "D", "a"), ("B", "E", "b"), ("C", "C", "b", {"lazo": "abajo"}),
           ("C", "∅", "a"), ("D", "D", "a", {"lazo": "der"}), ("D", "∅", "b", {"curva": -50}),
           ("E", "E", "b", {"lazo": "der"}), ("E", "∅", "a"), ("∅", "∅", "a", {"lazo": "der"}), ("∅", "∅", "b", {"lazo": "der"})],
)
D["r23-min"] = dict(
    estados={"A": (0, 1.2), "B": (2, 0), "C": (2, 2.4), "D": (4, 0), "∅": (4, 2.4)},
    inicial="A", finales=["A", "B", "C", "D"], muertos=["∅"], er="(a*|b*)|ab*", sigma="ab",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("B", "D", "a"), ("B", "C", "b"), ("C", "C", "b", {"lazo": "abajo"}),
           ("C", "∅", "a"), ("D", "D", "a", {"lazo": "der"}), ("D", "∅", "b"),
           ("∅", "∅", "a", {"lazo": "der"}), ("∅", "∅", "b", {"lazo": "der"})],
)

# ej. 3: sin abba ni baab
D["r23-sin"] = dict(
    estados={"q0": (0, 1.5), "q1": (1.6, 0.3), "q2": (3.4, 0.3), "q3": (5.2, 0.3),
             "q4": (1.6, 2.7), "q5": (3.4, 2.7), "q6": (5.2, 2.7)},
    inicial="q0", finales=["q0", "q1", "q2", "q3", "q4", "q5", "q6"], sigma="ab",
    cumple=lambda w: "abba" not in w and "baab" not in w,
    trans=[("q0", "q1", "a"), ("q0", "q4", "b"), ("q1", "q1", "a"), ("q1", "q2", "b"),
           ("q2", "q5", "a"), ("q2", "q3", "b"), ("q3", "q4", "b", {"curva": 30, "t": 0.3}),
           ("q4", "q5", "a"), ("q4", "q4", "b", {"lazo": "abajo"}), ("q5", "q6", "a"), ("q5", "q2", "b"),
           ("q6", "q1", "a", {"curva": -30, "t": 0.3})],
)

# =============================================================== 2025 parcial
P25_ER = "a|(b|ab)(ab)*(ε|a)"
P25_POS = {"q0": (0, 1.3), "q1": (2.2, 0), "q2": (2.2, 2.6), "q3": (4.4, 1.3)}
_t = [("q0", "q1", "a"), ("q0", "q2", "b"), ("q2", "q1", "a"), ("q1", "q2", "b")]
D["p25-af"] = dict(
    estados=P25_POS, inicial="q0", finales=["q1", "q2"], er=P25_ER, sigma="ab",
    trans=_t + [("q1", "q3", "a"), ("q2", "q3", "b"), ("q3", "q3", "a", {"lazo": "der"}), ("q3", "q3", "b", {"lazo": "der"})],
    alt="Autómata del ejercicio 1 del parcial 2025",
)
D["p25-muerto"] = dict(D["p25-af"], muertos=["q3"])
_p = {"i": (-1.3, 1.3), "q0": (0, 1.3), "q1": (2.2, 0), "q2": (2.2, 2.6), "f": (4.2, 1.3)}
D["p25-paso1"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=P25_ER, sigma="ab",
    trans=[nv("i", "q0", "ε")] + _t + [nv("q1", "f", "ε"), nv("q2", "f", "ε")],
)
_p = {k: v for k, v in _p.items() if k != "q1"}
D["p25-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q2"], er=P25_ER, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "q2", "b|ab"), nv("q2", "q2", "ab", {"lazo": "abajo"}),
           nv("q0", "f", "a"), nv("q2", "f", "ε|a")],
)
D["p25-paso3"] = dict(
    estados={"i": (-1.3, 0), "q0": (0, 0), "f": (4.0, 0)}, inicial="i", finales=["f"], marcados=["q0"],
    er=P25_ER, sigma="ab",
    trans=[("i", "q0", "ε"), nv("q0", "f", "a|(b|ab)(ab)*(ε|a)")],
)
D["p25-er"] = dict(
    estados={"i": (0, 0), "f": (4.0, 0)}, inicial="i", finales=["f"], er=P25_ER, sigma="ab",
    trans=[nv("i", "f", "a|(b|ab)(ab)*(ε|a)")],
)

# ej. 2: (nn*)(k|n)n*
D["p25-thompson"] = thompson("(nn*)(k|n)n*", er="(nn*)(k|n)n*", sigma="kn")
D["p25-afd"] = dict(
    estados={"A": (0, 1.2), "B": (1.7, 1.2), "C": (3.4, 2.4), "D": (3.4, 0), "E": (5.1, 2.4), "F": (5.1, 0),
             "∅": (1.7, 3.2)},
    inicial="A", finales=["C", "D", "E", "F"], muertos=["∅"], er="(nn*)(k|n)n*", sigma="kn",
    trans=[("A", "∅", "k"), ("A", "B", "n"), ("B", "C", "k"), ("B", "D", "n"), ("C", "∅", "k"), ("C", "E", "n"),
           ("D", "C", "k"), ("D", "F", "n"), ("E", "∅", "k", {"curva": 30}), ("E", "E", "n", {"lazo": "der"}),
           ("F", "C", "k"), ("F", "F", "n", {"lazo": "der"}), ("∅", "∅", "k", {"lazo": "izq"}), ("∅", "∅", "n", {"lazo": "izq"})],
)
D["p25-min"] = dict(
    estados={"A": (0, 0), "B": (1.8, 0), "D": (3.6, 0), "C": (3.6, 1.9), "∅": (1.8, 1.9)},
    inicial="A", finales=["C", "D"], muertos=["∅"], er="(nn*)(k|n)n*", sigma="kn",
    trans=[("A", "B", "n"), ("A", "∅", "k"), ("B", "C", "k"), ("B", "D", "n"), ("D", "D", "n"),
           ("D", "C", "k"), ("C", "C", "n", {"lazo": "der"}), ("C", "∅", "k"),
           ("∅", "∅", "k", {"lazo": "abajo"}), ("∅", "∅", "n", {"lazo": "abajo"})],
)

# ej. 3: empiezan con 01 o 2 y tienen cantidad par de 2
D["p25-pares"] = dict(
    estados={"q0": (0, 1), "q1": (1.7, 0), "q2": (3.6, 0), "q3": (3.6, 2)},
    inicial="q0", finales=["q2"], er="(01|2(0|1)*2)(0|1|2(0|1)*2)*", sigma="012",
    trans=[("q0", "q1", "0"), ("q1", "q2", "1"), ("q0", "q3", "2"), ("q2", "q2", "0", {"lazo": "der"}),
           ("q2", "q2", "1", {"lazo": "der"}), ("q2", "q3", "2"), ("q3", "q2", "2"),
           ("q3", "q3", "0", {"lazo": "der"}), ("q3", "q3", "1", {"lazo": "der"})],
)

# ======================================================== 2025 recuperatorio
R25_ER = "(aa|(b|ab)(ab)*(b|aa))*(ε|(b|ab)(ab)*)"
R25_POS = {"q0": (0, 1.4), "q1": (2.5, 0), "q2": (2.5, 2.8), "q3": (4.8, 1.4)}
_t = [("q0", "q1", "a"), ("q1", "q0", "a"), ("q0", "q2", "b"), ("q2", "q0", "b"),
      ("q2", "q1", "a", {"t": 0.75}), ("q1", "q2", "b", {"t": 0.25})]
D["r25-af"] = dict(
    estados=R25_POS, inicial="q0", finales=["q0", "q2"], er=R25_ER, sigma="abc",
    trans=_t + [("q0", "q3", "c", {"t": 0.25}), ("q1", "q3", "c"), ("q2", "q3", "c"),
                ("q3", "q3", "a", {"lazo": "der"}), ("q3", "q3", "b", {"lazo": "der"}), ("q3", "q3", "c", {"lazo": "der"})],
    alt="Autómata del ejercicio 1 del recuperatorio 2025",
)
D["r25-muerto"] = dict(D["r25-af"], muertos=["q3"])
_p = {"i": (-1.3, 1.4), "q0": (0, 1.4), "q1": (2.5, 0), "q2": (2.5, 2.8), "f": (4.4, 2.0)}
D["r25-paso1"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q1"], er=R25_ER, sigma="abc",
    trans=[nv("i", "q0", "ε")] + _t + [nv("q0", "f", "ε"), nv("q2", "f", "ε")],
)
_p = {k: v for k, v in _p.items() if k != "q1"}
D["r25-paso2"] = dict(
    estados=_p, inicial="i", finales=["f"], marcados=["q2"], er=R25_ER, sigma="abc",
    trans=[("i", "q0", "ε"), nv("q0", "q0", "aa"), nv("q0", "q2", "b|ab"), nv("q2", "q0", "b|aa"),
           nv("q2", "q2", "ab", {"lazo": "abajo"}), ("q0", "f", "ε"), ("q2", "f", "ε")],
)
D["r25-paso3"] = dict(
    estados={"i": (-1.3, 1.0), "q0": (0, 1.0), "f": (4.2, 1.0)}, inicial="i", finales=["f"], marcados=["q0"],
    er=R25_ER, sigma="abc",
    trans=[("i", "q0", "ε"), nv("q0", "q0", "aa|(b|ab)(ab)*(b|aa)"), nv("q0", "f", "ε|(b|ab)(ab)*")],
)
D["r25-er"] = dict(
    estados={"i": (0, 0), "f": (6.2, 0)}, inicial="i", finales=["f"], er=R25_ER, sigma="abc",
    trans=[nv("i", "f", "(aa|(b|ab)(ab)*(b|aa))*(ε|(b|ab)(ab)*)")],
)

# ej. 2: ab*(a|b|ε)
D["r25-thompson"] = thompson("ab*(a|b|ε)", er="ab*(a|b|ε)", sigma="ab")
D["r25-afd"] = dict(
    estados={"A": (0, 0), "B": (1.8, 0), "C": (3.6, 0), "D": (1.8, 1.9), "∅": (3.6, 1.9)},
    inicial="A", finales=["B", "C", "D"], muertos=["∅"], er="ab*(a|b|ε)", sigma="ab",
    trans=[("A", "B", "a"), ("A", "∅", "b", {"curva": -70}), ("B", "C", "a"), ("B", "D", "b"), ("C", "∅", "a"),
           ("C", "∅", "b"), ("D", "C", "a"), ("D", "D", "b", {"lazo": "abajo"}),
           ("∅", "∅", "a", {"lazo": "der"}), ("∅", "∅", "b", {"lazo": "der"})],
)
D["r25-min"] = dict(
    estados={"A": (0, 0), "B": (1.8, 0), "C": (3.6, 0), "∅": (2.7, 1.7)},
    inicial="A", finales=["B", "C"], muertos=["∅"], er="ab*(a|b|ε)", sigma="ab",
    trans=[("A", "B", "a"), ("A", "∅", "b"), ("B", "C", "a"), ("B", "B", "b"), ("C", "∅", "a"),
           ("C", "∅", "b"), ("∅", "∅", "a", {"lazo": "abajo"}), ("∅", "∅", "b", {"lazo": "abajo"})],
)

# ej. 3: terminan en 0 o 2 y tienen cantidad par de 1
D["r25-pares"] = dict(
    estados={"q0": (0, 0), "q1": (2.4, 0), "q2": (0, 1.9)},
    inicial="q0", finales=["q2"], er="(0|2|1(0|2)*1)*(0|2)", sigma="012",
    trans=[("q0", "q0", "0"), ("q0", "q0", "2"), ("q0", "q1", "1"), ("q1", "q0", "1"),
           ("q1", "q1", "0", {"lazo": "der"}), ("q1", "q1", "2", {"lazo": "der"}),
           ("q0", "q2", "0"), ("q0", "q2", "2")],
)
