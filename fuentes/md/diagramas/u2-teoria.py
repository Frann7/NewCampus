# Máquinas de estados finitos de la teoría de la Unidad 2 (Matemática Discreta).
# python fuentes/automatas.py fuentes/md/diagramas/u2-teoria.py app/contenido/md
#
# Cada flecha dice "entrada,salida". Sin estados finales (son máquinas de Mealy):
# el "reconocer" lo hace la salida 1, no un estado de aceptación.

SEP = " | "


def maq(estados, trans, alt, **op):
    return dict(estados=estados, inicial="s0", finales=[], trans=trans, sep=SEP, alt=alt, **op)


def fila(n, paso=2.2):
    return {f"s{i}": (i * paso, 0) for i in range(n)}


# ------------------------------------------------ Ejemplo 12 (reconoce 101)
D["u2t-e12"] = maq(
    fila(3, 2.4),
    [("s0", "s0", "0,0"), ("s0", "s1", "1,0"), ("s1", "s1", "1,0"), ("s1", "s2", "0,0"),
     ("s2", "s1", "1,1"), ("s2", "s0", "0,0", {"curva": 55})],
    "Máquina del Ejemplo 12 de la cátedra",
)

# ------------------------------------------------ Sumador binario en serie
D["u2t-sumador"] = maq(
    {"s0": (0, 0), "s1": (3.2, 0)},
    [("s0", "s0", "00,0"), ("s0", "s0", "01,1"), ("s0", "s0", "10,1"), ("s0", "s1", "11,0"),
     ("s1", "s0", "00,1"), ("s1", "s1", "01,0"), ("s1", "s1", "10,0"), ("s1", "s1", "11,1")],
    "Sumador binario en serie",
)

# ------------------------------------------------ 111 con solapamiento (Ejemplo 14)
D["u2t-111"] = maq(
    fila(3),
    [("s0", "s0", "0,0"), ("s0", "s1", "1,0"), ("s1", "s0", "0,0"), ("s1", "s2", "1,0"),
     ("s2", "s2", "1,1"), ("s2", "s0", "0,0", {"curva": 50})],
    "Reconocedor de 111 con solapamiento",
)

# ------------------------------------------------ 111 sin solapamiento
D["u2t-111-sin"] = maq(
    fila(3),
    [("s0", "s0", "0,0"), ("s0", "s1", "1,0"), ("s1", "s0", "0,0"), ("s1", "s2", "1,0"),
     ("s2", "s0", "0,0"), ("s2", "s0", "1,1", {"curva": 50})],
    "Reconocedor de 111 sin solapamiento",
)

# ------------------------------------------------ 111 en posición 3k (Ejemplo 15)
D["u2t-111-3k"] = maq(
    {"s0": (0, 0), "s1": (2.5, 0), "s2": (5, 0), "s3": (0.6, 2), "s4": (3.4, 2)},
    [("s0", "s1", "1,0"), ("s1", "s2", "1,0"), ("s2", "s0", "0,0", {"curva": -45}), ("s2", "s0", "1,1"),
     ("s0", "s3", "0,0"), ("s1", "s4", "0,0"), ("s3", "s4", "0,0"), ("s3", "s4", "1,0"),
     ("s4", "s0", "0,0"), ("s4", "s0", "1,0")],
    "Reconocedor de 111 en las posiciones múltiplo de tres",
)

# ------------------------------------------------ 0101 con solapamiento (Ejemplo 16 a)
D["u2t-0101"] = maq(
    fila(4),
    [("s0", "s0", "1,0"), ("s0", "s1", "0,0"), ("s1", "s1", "0,0"), ("s1", "s2", "1,0"),
     ("s2", "s3", "0,0"), ("s2", "s0", "1,0", {"curva": 45}),
     ("s3", "s2", "1,1", {"curva": -22}), ("s3", "s1", "0,0", {"curva": 70})],
    "Reconocedor de 0101 con solapamiento",
)

# ------------------------------------------------ 0101 en posición 4k (Ejemplo 16 b)
D["u2t-0101-4k"] = maq(
    {"s0": (0, 0), "s1": (2.2, 0), "s2": (4.4, 0), "s3": (6.6, 0),
     "s4": (2.2, 2), "s5": (4.4, 2), "s6": (6.6, 2)},
    [("s0", "s1", "0,0"), ("s1", "s2", "1,0"), ("s2", "s3", "0,0"),
     ("s3", "s0", "0,0", {"curva": -55}), ("s3", "s0", "1,1"),
     ("s0", "s4", "1,0"), ("s1", "s5", "0,0"), ("s2", "s6", "1,0"),
     ("s4", "s5", "0,0"), ("s4", "s5", "1,0"), ("s5", "s6", "0,0"), ("s5", "s6", "1,0"),
     ("s6", "s0", "0,0", {"curva": 75}), ("s6", "s0", "1,0")],
    "Reconocedor de 0101 en las posiciones múltiplo de cuatro",
)

# ------------------------------------------------ baab con solapamiento
D["u2t-baab"] = maq(
    fila(4),
    [("s0", "s0", "a,0"), ("s0", "s1", "b,0"), ("s1", "s1", "b,0"), ("s1", "s2", "a,0"),
     ("s2", "s3", "a,0"), ("s2", "s1", "b,0", {"curva": -22}),
     ("s3", "s1", "b,1", {"curva": 45}), ("s3", "s0", "a,0", {"curva": 75})],
    "Reconocedor de las cadenas que terminan en baab",
)

# ------------------------------------------------ {00}{0,1}*{111} (Ejemplo 17)
D["u2t-00-111"] = maq(
    {"s0": (0, 0), "s1": (2, 0), "s2": (4, 0), "s3": (6, 0), "s4": (8, 0), "s5": (1, 2)},
    [("s0", "s1", "0,0"), ("s0", "s5", "1,0"), ("s1", "s5", "1,0"), ("s1", "s2", "0,0"),
     ("s2", "s2", "0,0"), ("s2", "s3", "1,0"), ("s3", "s2", "0,0"), ("s3", "s4", "1,0"),
     ("s4", "s4", "1,1"), ("s4", "s2", "0,0", {"curva": 45}),
     ("s5", "s5", "0,0", {"lazo": "abajo"}), ("s5", "s5", "1,0", {"lazo": "abajo"})],
    "Reconocedor del lenguaje {00}{0,1}*{111}",
)

# ------------------------------------------------ prefijo b y sufijo aab, I = {a, b, c}
D["u2t-b-aab"] = maq(
    {"s0": (0, 0), "s1": (2.4, 0), "s2": (4.8, 0), "s3": (7.2, 0), "s4": (1.2, 2)},
    [("s0", "s1", "b,0"), ("s0", "s4", "a,0"), ("s0", "s4", "c,0"),
     ("s4", "s4", "a,0", {"lazo": "abajo"}), ("s4", "s4", "b,0", {"lazo": "abajo"}),
     ("s4", "s4", "c,0", {"lazo": "abajo"}),
     ("s1", "s1", "b,0"), ("s1", "s1", "c,0"), ("s1", "s2", "a,0"),
     ("s2", "s1", "b,0"), ("s2", "s1", "c,0"), ("s2", "s3", "a,0"),
     ("s3", "s3", "a,0"), ("s3", "s1", "b,1", {"curva": 50}), ("s3", "s1", "c,0", {"curva": 50})],
    "Reconocedor de las cadenas con prefijo b y sufijo aab",
)

# ------------------------------------------------ retardo de una unidad (Ejemplo 18)
D["u2t-retardo1"] = maq(
    {"s0": (0, 1), "s1": (2.2, 0), "s2": (2.2, 2)},
    [("s0", "s1", "0,0"), ("s0", "s2", "1,0"), ("s1", "s1", "0,0", {"lazo": "der"}),
     ("s1", "s2", "1,0"), ("s2", "s1", "0,1"), ("s2", "s2", "1,1", {"lazo": "der"})],
    "Máquina de retardo unitario",
)

# ------------------------------------------------ retardo de dos unidades (Ejemplos 19 y 22)
D["u2t-retardo2"] = maq(
    {"s0": (0, 1.55), "s1": (1.8, 0.25), "s2": (1.8, 2.85),
     "s3": (3.8, -0.4), "s4": (3.8, 0.9), "s5": (3.8, 2.2), "s6": (3.8, 3.5)},
    [("s0", "s1", "0,0"), ("s0", "s2", "1,0"),
     ("s1", "s3", "0,0"), ("s1", "s4", "1,0"), ("s2", "s5", "0,0"), ("s2", "s6", "1,0"),
     ("s3", "s3", "0,0", {"lazo": "der"}), ("s3", "s4", "1,0", {"lado": -1}),
     ("s4", "s5", "0,0"), ("s4", "s6", "1,0", {"curva": 45}),
     ("s5", "s4", "1,1"), ("s5", "s3", "0,1", {"curva": 75}),
     ("s6", "s5", "0,1", {"lado": -1}), ("s6", "s6", "1,1", {"lazo": "der"})],
    "Máquina de retardo de dos unidades",
)

# ------------------------------------------------ Ejemplos 20 y 21 (transitorio, sumidero, submáquina)
D["u2t-e20"] = maq(
    fila(3, 2.4),
    [("s0", "s1", "1,0"), ("s0", "s1", "0,0"), ("s1", "s1", "0,0", {"lazo": "abajo"}),
     ("s1", "s2", "1,0"), ("s2", "s2", "1,1", {"lazo": "abajo"}), ("s2", "s2", "0,0", {"lazo": "abajo"})],
    "Máquina de los Ejemplos 20 y 21 de la cátedra",
)

# ------------------------------------------------ máquina para leer el lenguaje que detecta
D["u2t-lenguaje"] = maq(
    {"s0": (0, 1), "s1": (2.2, 0), "s2": (2.2, 2), "s3": (4.4, 1)},
    [("s0", "s1", "0,0"), ("s0", "s2", "1,0"), ("s1", "s1", "1,1"), ("s1", "s3", "0,0"),
     ("s2", "s2", "0,0", {"lazo": "abajo"}), ("s2", "s3", "1,1"),
     ("s3", "s3", "0,0", {"lazo": "der"}), ("s3", "s3", "1,0", {"lazo": "der"})],
    "Máquina con un estado sumidero",
)

# ------------------------------------------------ la misma máquina, a medio dar (sección 13)
_pl = {"s0": (0, 1), "s1": (2.2, 0), "s2": (2.2, 2), "s3": (4.4, 1)}
D["u2t-incompleta"] = maq(
    _pl,
    [("s0", "s1", "0,0"), ("s0", "s2", "1,0"), ("s1", "s1", "1,1"), ("s1", "s3", "0,0"),
     ("s2", "s3", "1,1")],
    "Diagrama incompleto",
)
D["u2t-incompleta-b"] = maq(
    _pl,
    [("s0", "s1", "0,0"), ("s0", "s2", "1,0"), ("s1", "s1", "1,1"), ("s1", "s3", "0,0"),
     ("s2", "s2", "0,0", {"lazo": "abajo", "nueva": True}), ("s2", "s3", "1,1")],
    "Diagrama completado con la tabla",
)
