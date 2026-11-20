# Máquinas de estados finitos de la práctica de la Unidad 2: guía complementaria del
# Parcial 1 (máquinas) y recuperatorio de las Actividades de vacaciones (act. B, parte b).
# python fuentes/automatas.py fuentes/md/diagramas/u2-practica-compl.py app/contenido/md
#
# Etiquetas "entrada,salida"; las paralelas se juntan con " | ". Sin estados finales
# (son máquinas de Mealy: el "sí" es la salida 1). Cada máquina se verificó simulándola
# con todas las cadenas hasta largo 10-12 (script en el scratchpad del agente).

SEP = " | "


def M(estados, trans, alt, **kw):
    return dict(estados=estados, inicial="s0", trans=trans, sep=SEP, alt=alt, **kw)


# CM-1: dos primeros bits 10 y después la entrada retardada dos lugares
D["u2pc-cm1"] = M(
    {"s0": (0, 0), "s1": (3, 0), "s2": (3, 2.2), "s3": (0, 2.2)},
    [("s0", "s1", "0,1"), ("s0", "s2", "1,1"),
     ("s1", "s1", "0,0"), ("s1", "s2", "1,0"),
     ("s2", "s0", "0,0"), ("s2", "s3", "1,0"),
     ("s3", "s0", "0,1"), ("s3", "s3", "1,1", {"lazo": "abajo"})],
    "Máquina que escribe 10 y después repite la entrada con dos lugares de retardo",
)

# CM-2: suma acumulada módulo 3
D["u2pc-cm2"] = M(
    {"s0": (0, 0), "s1": (3, 0), "s2": (1.5, 2.4)},
    [("s0", "s0", "0,0"), ("s0", "s1", "1,1"), ("s0", "s2", "2,2"),
     ("s1", "s1", "0,1"), ("s1", "s2", "1,2"), ("s1", "s0", "2,0"),
     ("s2", "s2", "0,2", {"lazo": "abajo"}), ("s2", "s0", "1,0"), ("s2", "s1", "2,1")],
    "Máquina de la tabla del ejercicio 2: tres estados, uno por resto de dividir por 3",
    nombres={"s0": "S0", "s1": "S1", "s2": "S2"},
)

# CM-3a: termina en 01
D["u2pc-cm3a"] = M(
    {"s0": (0, 0), "s1": (2.6, 0)},
    [("s0", "s0", "1,0"), ("s0", "s1", "0,0"), ("s1", "s1", "0,0"), ("s1", "s0", "1,1")],
    "Reconocedor de {0,1}*{01}",
)

# CM-3b: termina en 00 o en 11
D["u2pc-cm3b"] = M(
    {"s0": (0, 0), "s1": (2.6, -1.2), "s2": (2.6, 1.2)},
    [("s0", "s1", "0,0"), ("s0", "s2", "1,0"),
     ("s1", "s1", "0,1"), ("s1", "s2", "1,0"),
     ("s2", "s2", "1,1", {"lazo": "abajo"}), ("s2", "s1", "0,0")],
    "Reconocedor de {0,1}*{00} unión {0,1}*{11}",
)

# CM-4: paridad par (cantidad par de unos), cadenas no vacías
D["u2pc-cm4"] = M(
    {"s0": (0, 0), "s1": (2.6, 0)},
    [("s0", "s0", "0,1"), ("s0", "s1", "1,0"), ("s1", "s1", "0,0"), ("s1", "s0", "1,1")],
    "Reconocedor de las cadenas no vacías con una cantidad par de unos",
)

# CM-5a: cada 101, con solapamiento
D["u2pc-cm5a"] = M(
    {"s0": (0, 0), "s1": (2.4, 0), "s2": (4.8, 0)},
    [("s0", "s0", "0,0"), ("s0", "s1", "1,0"),
     ("s1", "s1", "1,0"), ("s1", "s2", "0,0"),
     ("s2", "s1", "1,1"), ("s2", "s0", "0,0", {"curva": 45})],
    "Reconocedor de cada aparición de 101, con solapamiento",
)

# CM-5b: 101 solo si termina en una posición múltiplo de 3
D["u2pc-cm5b"] = M(
    {"s0": (0, 0), "s1": (2.2, 0), "s2": (4.4, 0), "s3": (0, 2), "s4": (2.2, 2)},
    [("s0", "s1", "1,0"), ("s0", "s3", "0,0"),
     ("s1", "s2", "0,0"), ("s1", "s4", "1,0"),
     ("s2", "s0", "1,1", {"curva": -50}), ("s2", "s0", "0,0"),
     ("s3", "s4", "0,0"), ("s3", "s4", "1,0"),
     ("s4", "s0", "0,0"), ("s4", "s0", "1,0")],
    "Reconocedor de 101 en bloques de tres símbolos",
)

# CM-6: 0001 con el 1 en las posiciones 4, 8, 12...
D["u2pc-cm6"] = M(
    {"s0": (0, 1), "s1": (2, 0), "s2": (4, 0), "s3": (6, 0),
     "s4": (2, 2), "s5": (4, 2), "s6": (6, 2)},
    [("s0", "s1", "0,0"), ("s0", "s4", "1,0"),
     ("s1", "s2", "0,0"), ("s1", "s5", "1,0"),
     ("s2", "s3", "0,0"), ("s2", "s6", "1,0"),
     ("s3", "s0", "1,1", {"curva": -90}), ("s3", "s0", "0,0"),
     ("s4", "s5", "0,0"), ("s4", "s5", "1,0"),
     ("s5", "s6", "0,0"), ("s5", "s6", "1,0"),
     ("s6", "s0", "0,0", {"curva": 90}), ("s6", "s0", "1,0")],
    "Reconocedor de 0001 en bloques de cuatro símbolos",
)

# CM-8: cada 01110, con solapamiento
D["u2pc-cm8"] = M(
    {"s0": (0, 0), "s1": (2, 0), "s2": (4, 0), "s3": (6, 0), "s4": (8, 0)},
    [("s0", "s0", "1,0", {"lazo": "izq"}), ("s0", "s1", "0,0"),
     ("s1", "s1", "0,0"), ("s1", "s2", "1,0"),
     ("s2", "s1", "0,0"), ("s2", "s3", "1,0"),
     ("s3", "s1", "0,0", {"curva": 55}), ("s3", "s4", "1,0"),
     ("s4", "s1", "0,1", {"curva": 100}), ("s4", "s0", "1,0", {"curva": -110})],
    "Reconocedor de cada aparición de 01110, con solapamiento",
    entrada="abajo",
)

# CM-9: A = {0}{0,1}*{001}
D["u2pc-cm9"] = M(
    {"s0": (0, 0), "s1": (2.2, 0), "s2": (4.4, 0), "s3": (6.6, 0), "s4": (0, 2)},
    [("s0", "s1", "0,0"), ("s0", "s4", "1,0"),
     ("s4", "s4", "0,0", {"lazo": "abajo"}), ("s4", "s4", "1,0"),
     ("s1", "s1", "1,0"), ("s1", "s2", "0,0"),
     ("s2", "s1", "1,0"), ("s2", "s3", "0,0"),
     ("s3", "s3", "0,0"), ("s3", "s1", "1,1", {"curva": 50})],
    "Reconocedor de {0}{0,1}*{001}; s4 es un sumidero",
)

# CM-11: xyxy como prefijo propio
D["u2pc-cm11"] = M(
    {"s0": (0, 0), "s1": (2, 0), "s2": (4, 0), "s3": (6, 0), "s4": (8, 0), "s5": (4, 2.2)},
    [("s0", "s1", "x,0"), ("s0", "s5", "y,0"),
     ("s1", "s2", "y,0"), ("s1", "s5", "x,0"),
     ("s2", "s3", "x,0"), ("s2", "s5", "y,0"),
     ("s3", "s4", "y,0"), ("s3", "s5", "x,0"),
     ("s4", "s4", "x,1"), ("s4", "s4", "y,1"),
     ("s5", "s5", "x,0", {"lazo": "abajo"}), ("s5", "s5", "y,0")],
    "Reconocedor de las cadenas con prefijo propio xyxy",
)

# CM-12: la máquina dada en la guía (redibujada)
D["u2pc-cm12"] = M(
    {"s0": (0, 1), "s1": (1.6, 0), "s2": (1.6, 2), "s3": (3.4, 0), "s4": (3.4, 2)},
    [("s0", "s1", "1,0"), ("s0", "s2", "0,0"),
     ("s1", "s1", "1,0"), ("s1", "s1", "0,0"),
     ("s2", "s1", "1,0"), ("s2", "s4", "0,0"),
     ("s4", "s3", "0,0"), ("s4", "s3", "1,0"),
     ("s3", "s3", "0,1", {"lazo": "der"}), ("s3", "s3", "1,1")],
    "Máquina del ejercicio 12 de la guía complementaria",
)

# Recuperatorio, actividad B b): prefijo c y sufijo abaab
D["u2pc-vb"] = M(
    {"s0": (0, 2.6), "s6": (0, 4.6), "s1": (4.5, 2.6),
     "s2": (2, 0), "s3": (4.5, 0), "s4": (7, 0), "s5": (9.5, 0)},
    [("s0", "s1", "c,0"), ("s0", "s6", "a,0"), ("s0", "s6", "b,0"),
     ("s6", "s6", "a,0", {"lazo": "abajo"}), ("s6", "s6", "b,0"), ("s6", "s6", "c,0"),
     ("s1", "s1", "b,0", {"lazo": "abajo"}), ("s1", "s1", "c,0"), ("s1", "s2", "a,0"),
     ("s2", "s2", "a,0", {"lazo": "izq"}), ("s2", "s3", "b,0"), ("s2", "s1", "c,0"),
     ("s3", "s4", "a,0"), ("s3", "s1", "b,0"), ("s3", "s1", "c,0"),
     ("s4", "s5", "a,0"), ("s4", "s3", "b,0"), ("s4", "s1", "c,0"),
     ("s5", "s3", "b,1", {"curva": -45}), ("s5", "s2", "a,0", {"curva": -100}), ("s5", "s1", "c,0")],
    "Reconocedor de las palabras con prefijo c y sufijo abaab",
)
