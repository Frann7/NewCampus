# 4 - Analisis Lexico-Automatas Finitos-Expresiones Regulares-Parte 3

Fuente: `C:/Users/Fran/AppData/Local/Temp/claude/C--Users-Fran-Desktop-NewCampus/196b4912-5fa9-4a20-89f0-578e09e99c9b/scratchpad/pyl-pdf/TOPIC 2/4 - Analisis Lexico-Automatas Finitos-Expresiones Regulares-Parte 3.pdf` · 8 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

1
Análisis Léxico,
Lenguajes Formales,
Autómatas Finitos,
Expresiones Regulares
Paradigmas y Lenguajes

<!-- página 2 -->

2
Equivalencia entre ER y AF
1. Transformación de Autómata Finito a Expresión Regular [ya vista]
2. Transformación de Expresión Regular a Autómata Finito
No Determinístico con -transiciones (ER -> AFN-)
◼ Construcción de Thompson
◼ La transformación se realiza en forma inductiva en base a la
definición de ER
◼ Características de los AFN- resultantes:
◼ un solo estado final
◼ del estado final no salen transiciones
◼ al estado inicial no llegan transiciones
Entrada: una ER r
Salida: un AFN-, que llamaremos N, que reconoce el mismo lenguaje

<!-- página 3 -->

3
Transformación de ER a AFN-
i f
◼ Procedimiento
Siguiendo el orden de evaluación de la expresión regular r, construimos el
AFN- N aplicando las siguiente reglas:
1. Para  se construye el AFN-
2. Para  se construye
3. Para todo símbolo a en , se construye
4. Si r y s son ER y Nr y Ns son los AFN- correspondientes, entonces:
1) Para (r | s) se construye
1) Para (r . s) se construye
1) Para (r*) se construye
i f
i fa

<!-- página 4 -->

4
Transformación AFN- a AFD
1. Transformación de Autómata Finito a Expresión Regular
2. Transformación de Expresión Regular a Autómata Finito No Determinístico con -
transiciones (ER -> AFN-)
3. Transformación de Autómata Finito No Determinístico con -
transiciones a Autómata Finito Determinístico (AFN- -> AFD)
Entrada: un AFN-, que llamaremos N
Salida: un AFD, que llamaremos D y que reconoce el mismo lenguaje
Funciones auxiliares:
◼ -clausura (T): donde T QN, es el subconjunto de estados de N,
alcanzables mediante 0 o más -transiciones a partir de algún estado
s en T
◼ mueve (T,a): donde T QN y a en , es el subconjunto de estados de
N hacia los cuales hay una a-transición desde algún estado s en T.

<!-- página 5 -->

5
Transformación AFN- a AFD
Algoritmo
1. Calcular el estado inicial q0D de D como la -clausura ({q0N}) y
agregarlo a QD como estado “no tratado”
2. Mientras haya un estado T “no tratado” en QD, hacer:
1. Marcar T como “tratado”
2. Para cada a en  hacer:
▪ U:= -clausura ( mueve(T, a) )
▪ Si (U no está en QD), agregarlo como “no tratado”
▪ D [T, a]:= U
3. Agregar a FD todo estado T que contenga al menos un estado final
de N

<!-- página 6 -->

6
Minimización de un AFD
1. Transformación de Autómata Finito a Expresión Regular
2. Transformación de Expresión Regular a Autómata Finito No Determinístico
con -transiciones (ER -> AFN-)
3. Transformación de Autómata Finito No Determinístico con -transiciones a
Autómata Finito Determinístico (AFN- -> AFD)
4. Minimización de un AFD
◼ Para todo AFD se puede construir un AFD equivalente con mínima cantidad
de estados.
◼ El procedimiento se basa en la búsqueda de estados “no distinguibles”.
Estados distinguibles
◼ Dos estados s y t son distinguibles si existe una cadena w, tal que partiendo
desde s y aplicando las transiciones mediante los símbolos de w, se llega a un
estado final, mientras que partiendo desde t y aplicando w se llega a un
estado no final (o viceversa)
◼ En símbolos: dos estado s y t son distinguibles mediante w si:
((s,w) en F)  ((t,w) en Q-F)^ ^

<!-- página 7 -->

7
Minimización de un AFD
Algoritmo de Minimización
Entrada: un AFD D
Salida: un AFD M, con una mínima cantidad de estados tal que LD = LM
Método:
1. Construir una Partición inicial de QD denominada P1, conformada por dos grupos: el
grupo de los estados finales y el grupo de los estados no finales (ya que son distinguibles
mediante ).
2. Sea Pi la partición actual, crear una nueva partición Pi+1 de la siguiente manera:
1. Para (cada grupo G en Pi) hacer:
◼ Particionar G en subgrupos tales que dos estados s y t están en el mismo subgrupo si
y solo si, para todos los símbolos a en , s y t tienen a-transiciones hacia los mismos
grupos de Pi.
2. Sustituir G en Pi+1 por los nuevos subgrupos
3. Si  Pi+1 = Pi seguir con el paso 4, si no, volver al punto 2 considerando a Pi+1 como la
partición actual Pi
4. Elegir un estado representante de cada grupo de la última partición e incorporarlo como
estado a QM. Redirigir todas las transiciones que lleguen al grupo representado, hacia este
estado.
◼ El grupo que contiene el estado inicial de D, será el estado inicial de M
◼ Los grupos de estados finales de D, serán los estados finales de M

<!-- página 8 -->

8
Lenguajes Formales y Autómatas
Finitos
Fin parte III - Expresiones Regulares y Autómatas
Finitos
