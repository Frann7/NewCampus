# Autómatas de la Unidad 3 (De ER a AFD mínimo).
# python fuentes/automatas.py fuentes/pyl/diagramas/u3.py
# python fuentes/automatas.py --verificar fuentes/pyl/diagramas/u3.py

# ------------------------------------------------ práctica, ejercicio 1: (a|b)*b
D["u3-e1-thompson"] = thompson("(a|b)*b", er="(a|b)*b", sigma="ab")
D["u3-e1-afd"] = dict(
    estados={"A": (0, 1), "B": (1.9, 0), "C": (1.9, 2)},
    inicial="A", finales=["C"], er="(a|b)*b", sigma="ab",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("B", "B", "a", {"lazo": "der"}), ("B", "C", "b"),
           ("C", "B", "a"), ("C", "C", "b", {"lazo": "der"})],
)
D["u3-e1-min"] = dict(
    estados={"A": (0, 0), "C": (2, 0)},
    inicial="A", finales=["C"], er="(a|b)*b", sigma="ab",
    trans=[("A", "A", "a"), ("A", "C", "b"), ("C", "A", "a"), ("C", "C", "b")],
)

# ------------------------------------------------ práctica, ejercicio 2: a|bc*
D["u3-e2-thompson"] = thompson("a|bc*", er="a|bc*", sigma="abc")
D["u3-e2-afd"] = dict(
    estados={"A": (0, 1), "B": (2, 0), "C": (2, 2), "D": (4, 3), "∅": (4, 1)},
    inicial="A", finales=["B", "C", "D"], muertos=["∅"], er="a|bc*", sigma="abc",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("A", "∅", "c"),
           ("B", "∅", "a"), ("B", "∅", "b"), ("B", "∅", "c"),
           ("C", "∅", "a"), ("C", "∅", "b"), ("C", "D", "c"),
           ("D", "∅", "a"), ("D", "∅", "b"), ("D", "D", "c", {"lazo": "der"}),
           ("∅", "∅", "a", {"lazo": "der"}), ("∅", "∅", "b"), ("∅", "∅", "c")],
)
D["u3-e2-min"] = dict(
    estados={"A": (0, 1), "B": (2, 0), "C": (2, 2), "∅": (4, 1)},
    inicial="A", finales=["B", "C"], muertos=["∅"], er="a|bc*", sigma="abc",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("A", "∅", "c"),
           ("B", "∅", "a"), ("B", "∅", "b"), ("B", "∅", "c"),
           ("C", "∅", "a"), ("C", "∅", "b"), ("C", "C", "c", {"lazo": "abajo"}),
           ("∅", "∅", "a", {"lazo": "der"}), ("∅", "∅", "b"), ("∅", "∅", "c")],
)

# ------------------------------------------------ práctica, ejercicio 3: (ab)*a
D["u3-e3-thompson"] = thompson("(ab)*a", er="(ab)*a", sigma="ab")
D["u3-e3-afd"] = dict(
    estados={"A": (0, 0), "B": (2, 0), "C": (4, 0), "∅": (2, 1.8)},
    inicial="A", finales=["B"], muertos=["∅"], er="(ab)*a", sigma="ab",
    trans=[("A", "B", "a"), ("A", "∅", "b"), ("B", "∅", "a"), ("B", "C", "b"),
           ("C", "B", "a"), ("C", "∅", "b"),
           ("∅", "∅", "a", {"lazo": "abajo"}), ("∅", "∅", "b")],
)
D["u3-e3-min"] = dict(
    estados={"A": (0, 0), "B": (2, 0), "∅": (1, 1.8)},
    inicial="A", finales=["B"], muertos=["∅"], er="(ab)*a", sigma="ab",
    trans=[("A", "B", "a"), ("A", "∅", "b"), ("B", "∅", "a"), ("B", "A", "b"),
           ("∅", "∅", "a", {"lazo": "abajo"}), ("∅", "∅", "b")],
)

# ------------------------------------------------ práctica, ejercicio 4: a(b|ε)c*
D["u3-e4-thompson"] = thompson("a(b|ε)c*", er="a(b|ε)c*", sigma="abc")
D["u3-e4-afd"] = dict(
    estados={"A": (0, 0), "B": (2, 0), "C": (4, 0), "D": (6, 0), "∅": (3, 2)},
    inicial="A", finales=["B", "C", "D"], muertos=["∅"], er="a(b|ε)c*", sigma="abc",
    trans=[("A", "B", "a"), ("A", "∅", "b"), ("A", "∅", "c"),
           ("B", "∅", "a"), ("B", "C", "b"), ("B", "D", "c", {"curva": 40}),
           ("C", "∅", "a"), ("C", "∅", "b"), ("C", "D", "c"),
           ("D", "∅", "a"), ("D", "∅", "b"), ("D", "D", "c", {"lazo": "der"}),
           ("∅", "∅", "a", {"lazo": "abajo"}), ("∅", "∅", "b"), ("∅", "∅", "c")],
)
D["u3-e4-min"] = dict(
    estados={"A": (0, 0), "B": (2, 0), "C": (4, 0), "∅": (2, 1.8)},
    inicial="A", finales=["B", "C"], muertos=["∅"], er="a(b|ε)c*", sigma="abc",
    trans=[("A", "B", "a"), ("A", "∅", "b"), ("A", "∅", "c"),
           ("B", "∅", "a"), ("B", "C", "b"), ("B", "C", "c"),
           ("C", "∅", "a"), ("C", "∅", "b"), ("C", "C", "c", {"lazo": "der"}),
           ("∅", "∅", "a", {"lazo": "abajo"}), ("∅", "∅", "b"), ("∅", "∅", "c")],
)

# ------------------------------------------------ práctica, ejercicio 5: (a|ba)*b
D["u3-e5-thompson"] = thompson("(a|ba)*b", er="(a|ba)*b", sigma="ab")
D["u3-e5-afd"] = dict(
    estados={"A": (0, 1), "B": (2, 0), "C": (2, 2), "D": (4, 1), "∅": (2, 3.6)},
    inicial="A", finales=["C"], muertos=["∅"], er="(a|ba)*b", sigma="ab",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("B", "B", "a"), ("B", "C", "b"),
           ("C", "D", "a"), ("C", "∅", "b"), ("D", "B", "a"), ("D", "C", "b"),
           ("∅", "∅", "a", {"lazo": "abajo"}), ("∅", "∅", "b")],
)
D["u3-e5-min"] = dict(
    estados={"A": (0, 0), "C": (2, 0), "∅": (4, 0)},
    inicial="A", finales=["C"], muertos=["∅"], er="(a|ba)*b", sigma="ab",
    trans=[("A", "A", "a"), ("A", "C", "b"), ("C", "A", "a"), ("C", "∅", "b"),
           ("∅", "∅", "a"), ("∅", "∅", "b")],
)

# ------------------------------------------------ práctica, ejercicio 6: x(y|z)*x
D["u3-e6-thompson"] = thompson("x(y|z)*x", er="x(y|z)*x", sigma="xyz")
D["u3-e6-afd"] = dict(
    estados={"A": (0, 1), "B": (2, 1), "E": (3.7, 1), "D": (4.6, -1), "C": (5.6, 3.4), "∅": (2, 4.4)},
    inicial="A", finales=["C"], muertos=["∅"], er="x(y|z)*x", sigma="xyz",
    trans=[("A", "B", "x"), ("A", "∅", "y"), ("A", "∅", "z"),
           ("B", "C", "x"), ("B", "D", "y"), ("B", "E", "z"),
           ("C", "∅", "x"), ("C", "∅", "y"), ("C", "∅", "z"),
           ("D", "C", "x"), ("D", "D", "y"), ("D", "E", "z"),
           ("E", "C", "x"), ("E", "D", "y"), ("E", "E", "z", {"lazo": "abajo"}),
           ("∅", "∅", "x", {"lazo": "abajo"}), ("∅", "∅", "y"), ("∅", "∅", "z")],
)
D["u3-e6-min"] = dict(
    estados={"A": (0, 0), "B": (2, 0), "C": (4, 0), "∅": (2, 2)},
    inicial="A", finales=["C"], muertos=["∅"], er="x(y|z)*x", sigma="xyz",
    trans=[("A", "B", "x"), ("A", "∅", "y"), ("A", "∅", "z"),
           ("B", "C", "x"), ("B", "B", "y"), ("B", "B", "z"),
           ("C", "∅", "x"), ("C", "∅", "y"), ("C", "∅", "z"),
           ("∅", "∅", "x", {"lazo": "abajo"}), ("∅", "∅", "y"), ("∅", "∅", "z")],
)

# ------------------------------------------------ práctica, ejercicio 7: a(a|b)*b|b(a|b)*
D["u3-e7-thompson"] = thompson("a(a|b)*b|b(a|b)*", er="a(a|b)*b|b(a|b)*", sigma="ab")
D["u3-e7-afd"] = dict(
    estados={"A": (0, 2.5), "B": (2, 0.9), "D": (4, 0), "E": (4, 1.8),
             "C": (2, 4.1), "F": (4, 3.2), "G": (4, 5)},
    inicial="A", finales=["C", "E", "F", "G"], er="a(a|b)*b|b(a|b)*", sigma="ab",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("B", "D", "a"), ("B", "E", "b"),
           ("C", "F", "a"), ("C", "G", "b"),
           ("D", "D", "a", {"lazo": "der"}), ("D", "E", "b"),
           ("E", "D", "a"), ("E", "E", "b", {"lazo": "der"}),
           ("F", "F", "a", {"lazo": "der"}), ("F", "G", "b"),
           ("G", "F", "a"), ("G", "G", "b", {"lazo": "der"})],
)
D["u3-e7-min"] = dict(
    estados={"A": (0, 1), "B": (2, 0), "E": (4, 0), "C": (2, 2)},
    inicial="A", finales=["C", "E"], er="a(a|b)*b|b(a|b)*", sigma="ab",
    trans=[("A", "B", "a"), ("A", "C", "b"), ("B", "B", "a"), ("B", "E", "b"),
           ("E", "B", "a"), ("E", "E", "b"),
           ("C", "C", "a", {"lazo": "der"}), ("C", "C", "b")],
)
