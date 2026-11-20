# Máquinas de estados finitos de los parciales (app/contenido/md/evaluacion/parciales/).
# python fuentes/automatas.py fuentes/md/diagramas/parciales.py app/contenido/md/evaluacion/parciales

SUB = {f"s{i}": f"s{chr(0x2080 + i)}" for i in range(6)}

# ============================================== Parcial 1 2026 · ej. 1 (termina en abba)
D["ev-p1-2026-ej1"] = dict(
    estados={"s0": (0, 1), "s1": (2, 1), "s2": (4, 1), "s3": (6, 1)},
    inicial="s0", sep=" | ", nombres=SUB,
    trans=[("s0", "s0", "b,0", {"lazo": "arriba"}), ("s0", "s1", "a,0"),
           ("s1", "s1", "a,0", {"lazo": "arriba"}), ("s1", "s2", "b,0"),
           ("s2", "s1", "a,0"), ("s2", "s3", "b,0"),
           ("s3", "s1", "a,1", {"curva": 70}), ("s3", "s0", "b,0", {"curva": 125})],
    alt="MEF que reconoce las cadenas que terminan en abba",
)

# ============================================== Parcial 1 2026 · ej. 4
P1E4 = {"s0": (0, 1.2), "s1": (2, 0), "s2": (2, 2.4), "s3": (4.4, 0), "s4": (4.4, 2.4)}
_impreso = [("s0", "s1", "0,0"), ("s0", "s2", "1,0"), ("s1", "s1", "0,0", {"lazo": "arriba"}),
            ("s1", "s3", "1,0"), ("s3", "s3", "1,1", {"lazo": "der"}),
            ("s2", "s2", "1,0", {"lazo": "arriba"}), ("s2", "s4", "0,1")]
D["ev-p1-2026-ej4-impreso"] = dict(
    estados=P1E4, inicial="s0", sep=" | ", nombres=SUB, trans=_impreso,
    alt="Diagrama impreso del ejercicio 4 (incompleto)",
)
D["ev-p1-2026-ej4-completa"] = dict(
    estados=P1E4, inicial="s0", sep=" | ", nombres=SUB,
    trans=_impreso + [("s3", "s4", "0,0"), ("s4", "s4", "0,0", {"lazo": "der"}),
                      ("s4", "s4", "1,0", {"lazo": "der"})],
    alt="Máquina del ejercicio 4 completa",
)
