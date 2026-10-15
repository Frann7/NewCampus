# Analisis_Lexico-Automatas_Finitos-Expresiones_Regulares-Parte_2

Fuente: `C:/Users/Fran/AppData/Local/Temp/claude/C--Users-Fran-Desktop-NewCampus/196b4912-5fa9-4a20-89f0-578e09e99c9b/scratchpad/pyl-pdf/TOPIC 2/Analisis_Lexico-Automatas_Finitos-Expresiones_Regulares-Parte_2.pdf` · 9 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |
| 9 |  |

<!-- página 1 -->

1
Análisis Léxico, Lenguajes
Formales, Autómatas Finitos,
Expresiones Regulares
Paradigmas y Lenguajes

<!-- página 2 -->

2
Expresiones Regulares
◼ Es una notación que permite generar Lenguajes Regulares
◼ Definición formal
Las Expresiones Regulares sobre el alfabeto S y los lenguajes que generan,
se definen recursivamente mediante las siguientes reglas:
1.  es una Expresión Regular y genera el lenguaje {}
2. e es una Expresión Regular y genera el lenguaje {e}
3. Para todo símbolo a en S, a es una ER y genera {a}
4. Si r y s son ER y generan los lenguajes Lr y Ls respectivamente,
entonces:
1) (r | s) es una ER y genera  Lr  Ls
2) (r . s) es una ER y genera  Lr . Ls - también se puede escribir (rs)
3) (r*) es una ER y genera  Lr*
4) (r) es una ER y genera Lr

<!-- página 3 -->

3
Expresiones Regulares
◼ Desde el punto de vista del Análisis Léxico, sirve para especificar los
Patrones que definen los Componentes Léxicos
◼ Cada punto de la definición consta de dos partes, su especificación sintáctica
y su especificación semántica. Por ejemplo:
 es una Expresión Regular [sintaxis] y genera el lenguaje {} [semántica]
◼ En el punto 4, se definen la operaciones válidas con las cuales se pueden
componer expresiones más complejas. Se utilizan paréntesis para que no
haya ambigüedad en cuanto al orden de evaluación de las operaciones.
◼ Ejemplo de expresión regular compuesta:    ((a|((ba)*))|e)
◼ Las Expresiones Regulares generan la Clase de los Lenguajes Regulares

<!-- página 4 -->

4
Expresiones Regulares
◼ Interpretación
◼ La Expresión Regular   ((a|((ba)*))|e) se interpreta de la siguiente
manera:
◼ Por la regla 3, la ER a, genera {a} y la ER b, genera {b}
◼ Por la regla 2, la ER e, genera {e}
◼ Por la regla 4.2, la ER (ba) genera {b}.{a}={ba}
◼ Por la regla 4.3, la ER ((ba)*) genera {ba}* = {e, ba, baba, bababa,
…}
◼ Por la regla 4.1, la ER (a|((ba)*)) genera {a}  {e, ba, baba,
bababa, …} = {e, a, ba, baba, bababa, …}
◼ Finalmente, por la regla 4.1 nuevamente, la ER ((a|((ba)*))|e)
genera {e}  {e, a, ba, baba, bababa, …} = {e, a, ba, baba,
bababa, …}

<!-- página 5 -->

5
Expresiones Regulares
◼ Uso de paréntesis
◼ Para evitar el uso excesivo de los paréntesis, convenimos las siguientes
prioridades y asociatividad para los operadores
◼ Prioridades: el operador de mayor prioridad es * (clausura), seguido de
. (concatenación) y por último | (unión). Es decir que, a menos que se
usen explícitamente los paréntesis, primero se resuelven las clausuras,
luego las concatenaciones y por último las uniones.
◼ Asociatividad: todos los operadores son asociativos por izquierda (se
resuelven de izquierda a derecha).
◼ Aplicando estas convenciones, la expresión regular ((a|((ba)*))|e) se puede
escribir como:
a | (ba)* | e
◼ Nota: en algunos libros se utiliza el operador + en lugar de |. También es
común el uso de l en lugar de e.

<!-- página 6 -->

6
Equivalencia entre ER y AF
1. Transformación de Autómata Finito a Expresión Regular
Entrada: un AFD o un AFN o un AFN-e, que llamaremos m
Salida: una ER r que genera el mismo lenguaje
Procedimiento:
1. Eliminar los estados muertos de m (si posee)
2. Agregar dos estados a m: un nuevo estado inicial con una e-transición al
estado inicial original y un nuevo estado final al que llega una e-transición
desde cada estado final original de m. El estado inicial original deja de serlo,
y los estados finales originales pasan a ser no finales

<!-- página 7 -->

7
Equivalencia entre ER y AF
[continuación Transformación de Autómata Finito a Expresión Regular]
3. Eliminar uno a uno, todos los estados intermedios (los que no son finales ni el
inicial) de la siguiente manera:
1. Reemplazar cada par de transiciones paralelas (las que salen de un mismo
estado y llegan a un mismo estado) etiquetadas r1 y r2, por una única
transición etiquetada con (r1 | r2).
2. Elegir un estado intermedio t, y reemplazarlo por  n.m (donde n es la
cantidad de transiciones de entrada de t y m es la cantidad de transiciones de
salida de t) transiciones de la forma:
donde:
qi pj
ai b* gj
q1
t
p1
qn pm
.
.
.
.
.
.
a1
an gm
g1
b
con   i:1..n
j:1..m

<!-- página 8 -->

8
Equivalencia entre ER y AF
[continuación Transformación de Autómata Finito a Expresión Regular]
4. Reemplazar cada par de transiciones paralelas etiquetadas r1 y r2, por una
única transición etiquetada con (r1 | r2).
5. La expresión regular resultante r, será la etiqueta de una única transición del
estado inicial al estado final.
◼ Todo AF, ya sea determinístico, no-determinístico o determinístico con e-
transiciones, se puede transformar a una Expresión Regular equivalente mediante
el procedimiento visto.

<!-- página 9 -->

9
Lenguajes Formales y Autómatas Finitos
Fin parte II - Expresiones Regulares y Autómatas
Finitos
