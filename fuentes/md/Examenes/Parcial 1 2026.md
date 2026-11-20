# Parcial 1 2026 (LSI-FCyT-UADER · Matemática Discreta)

Fuente: foto de la hoja de un alumno (pasada por chat, no está en el repo). Se transcribe solo lo
impreso: los nombres y lo que el alumno escribió a mano (en la tabla y en el diagrama del ej. 4, y
el sistema del ej. 6) no se copian. Unidades: 2 (lenguajes y MEF) y 3 (álgebras de Boole). Este
año **no** entró combinatoria (U1) en el primer parcial.

## Ejercicio 1 (10 puntos)
Dados \(I = \{a, b\}\) y \(O = \{0, 1\}\), construir una máquina de estados finito que reconozca
cadenas que terminan en \(abba\) (detecta solapamientos).

## Ejercicio 2 (10 puntos)
Dados los lenguajes \(A = \{01, 10\}\), \(B = \{0, 1\}\) y \(C = \{11\}\), con \(\Sigma = \{0, 1\}\),
describir unívocamente, en términos de prefijo y sufijo, las cadenas del lenguaje \(AB^{+}C^{2}\).

## Ejercicio 3 (10 puntos)
Para la función booleana \(f : B^{4} \to B \,/\, f = \prod M(1, 3, 5, 6, 10, 12, 13)\), sin realizar
la tabla y justificando claramente, hallar \(f(1, 0, 1, 1)\).

## Ejercicio 4 (30 puntos)
Dada la siguiente máquina de estados finito, representada por su tabla y su diagrama de estados:

Tabla impresa (vacío = no se da):

| | ν 0 | ν 1 | ω 0 | ω 1 |
| :-- | :-- | :-- | :-- | :-- |
| s0 | s1 | | | 0 |
| s1 | s1 | s3 | 0 | |
| s2 | s4 | s2 | 1 | 0 |
| s3 | | s3 | 0 | 1 |
| s4 | | | 0 | |

Diagrama impreso (arista = entrada,salida):
s0 → s1 con 0,0 · s0 → s2 con 1,0 · s1 → s1 (lazo) con 0,0 · s1 → s3 con 1,0 ·
s3 → s3 (lazo) con 1,1 · s2 → s2 (lazo) con 1,0 · s2 → s4 con 0,1.
(No hay flechas que salgan de s4 ni flecha s3 → s4 en lo impreso.)

a) (6p) Rellenar los datos faltantes en la tabla y el diagrama con la información disponible
   (quedará incompleto, no se preocupe).
b) (6p) ¿Cuántas máquinas, con la información disponible hasta el momento, es posible construir
   que tengan un solo estado sumidero?

En los siguientes ítems trabajar con: \(\nu(s_3, 0) = s_4\), \(\nu(s_4, 0) = \nu(s_4, 1) = s_4\),
\(\omega(s_4, 1) = 0\).

c) (4p) Completar la tabla con la nueva información suministrada.
d) (4p) Determinar una submáquina que no sea sumidero. Indicar si la misma es fuertemente conexa.
e) (10p) Escribir como concatenación de lenguajes, el conjunto de cadenas que detecta.

## Ejercicio 5 (20 puntos)
La siguiente función booleana \(f : B^{3} \to B\) está definida como
\(f(x, y, z) = \overline{xy} + \overline{y}z + \overline{z}(z + \overline{x})\), se pide:

a) (10p) Escribir \(f\) en su forma más simple.
b) (5p) Construir la tabla de valores de \(f\) (puede utilizarla como verificador del ítem a)).
c) (5p) Hallar la **expresión algebraica** de la forma normal disyuntiva (f.n.d.) de \(f\).

(En la foto, la barra del primer término se ve **continua sobre \(xy\)**: \(\overline{xy}\), no
\(\overline{x}\,\overline{y}\). Se resuelve así, y la explicación muestra en una línea qué daría la
otra lectura.)

## Ejercicio 6 (20 puntos)
Resolver el siguiente sistema de ecuaciones booleanas:
\(\overline{w + \overline{x}} = 0 \wedge w \cdot \overline{y} = 1 \wedge x + z = 1 \wedge \overline{y \cdot z} = 1\)
