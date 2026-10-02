# Unidad 1

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 1/UNIDAD 1/Unidad 1.pdf` · 14 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Resumen de la unidad: usos de la probabilidad, P = n/N, definiciones de evento, espacio muestral, experimento. |
| 2 | Ej. 1 moneda y Ej. 2 dado (eventos A, B, C); variante con cara superior e inferior. |
| 3 | Diagrama de tallo y hoja: moneda/dado; Ej. 3 con tres artículos D/N (N = 8); S = {(x, y) / x² + y² ≤ 4}. |
| 4 | Complemento, intersección, excluyentes y unión (Ej. 4 y 5); Venn y Ej. 6 con resultados. ⚠ ver el PDF: Venn del Ej. 6 con la ubicación de los elementos 1–7; barras de complemento perdidas. |
| 5 | P(A) = n/N con igualmente probables; Ej. 7 dado cargado, P(B) = 4/9; necesidad de contar. |
| 6 | Regla de multiplicación (Ej. 3, dado y moneda, Ej. 8: pares de 3 dígitos = 24); permutaciones, Ej. 9: 3! = 6. |
| 7 | n!, 0! = 1, permutaciones de r en n (nPr); Ej. 10: 4P2 = 12 y Ej. 11: 20P2 = 380. |
| 8 | Ej. 12: 5P3 = 60; permutaciones con repetidos (Ej. 13: 1260); circulares (n−1)!; inicio de combinaciones. |
| 9 | Combinaciones Cn,r; Ej. 14 comités (18) y Ej. 15 póker 3 ases y 2 reyes (24/2.598.960). |
| 10 | Reglas aditivas para 2 y 3 eventos, excluyentes y partición de S. |
| 11 | Complementarios; probabilidad condicional y Ej. 16 (par dado > 3, 2/3). |
| 12 | Ej. 17 vuelos (0,94 y 0,95); eventos independientes, regla multiplicativa; Ej. 18 y 19. |
| 13 | Independencia por el absurdo (Ej. 19), extensión de la intersección, probabilidad total; enunciado del Ej. 20. |
| 14 | Ej. 20: probabilidad total 0,0245; regla de Bayes y Ej. 21: P(B2/A) ≈ 0,55. |

<!-- página 1 -->

Unidad 1: Probabilidad
Ejemplos
Permite ponderar (estimar cuantitativamente) la ocurrencia de un evento futuro con ayuda del análisis
del mismo evento ocurrido en el pasado (Estadística).

*Usos o aplicaciones (teóricas): Permitir valorar la ocurrencia de un evento en términos económicos,
es decir:

Evento negativo: contrastarlo con el costo de evitar que ocurra (si puedo) o pagar o perder dinero
(seguros); o reglamentar normas.
Evento positivo: invertir o no dinero para beneficiarse si el evento ocurre (lotería, etc.).

En la gestión estatal: Vial, Mantenimiento, Urbanismo, Salud.
En las ciencias: Cs. Sociales, Cs. Naturales, Cs. Biológicas, Informática, Ingeniería.

Ejemplos

● Costo de abrir una caja adicional en peaje de autopista o en supermercado.
● Costo de comprar un repuesto de mejor calidad en informática.
● Costo de colocar un semáforo.
● Costo de abrir una agencia en una localidad.
● Costo de habilitar un nuevo cajero automático en bancos, supermercados, facultades.
● Costo de aumentar la resistencia de partes de líneas de transmisión de energía eléctrica en
redes.

Probabilidad: Cuantificar la ocurrencia de un evento con ayuda de la estadística.

P(A)  =
n
N
casos favorables del evento A
casos posibles del evento A
Jamás la probabilidad es mayor a 1

A Evento:
Suceso que se estudia.
Subconjunto de un Espacio Muestral.

B Espacio Muestral (E.M o S):
Conjunto de todos los resultados posibles de un experimento (finito o infinito).

Experimento:
Cualquier proceso que genere un conjunto de datos.

Elemento (o Puntos Muestrales):
Dato perteneciente a un Espacio Muestral.

Observación:
Registro de los datos que genera un experimento.

Tipos de datos:
Categóricos (Discretos).
Numéricos (Discretos o continuos).

<!-- página 2 -->

Ej. 1: Lanzar una moneda
Experimento: Lanzar una moneda al aire 1 vez.
Observación: Dato: Indica el resultado del lanzamiento según lo que observo del experimento.
Espacio Muestral:   S =  {C, X} Conjunto de todos los elementos posibles.
Elementos: C (cara), X (seca ó cruz).
Evento: Suceso Cara ( C ), un subconjunto del S.

P(C)  =  n
N  =  1
2  =  0,5

Ej. 2: Lanzar un dado
Experimento: Lanzar un dado.
Observación: Dato que muestra la cara superior del dado.
Elementos: 1,2,3,4,5,6.
Espacio Muestral: S =  {1,2,3,4,5,6}
Eventos (Subconjunto):
A → Que salga impar
B → Que sea mayor que 4
C → Que sea un 2

Probabilidad de los eventos A,B,C
P(A)  =  n
N = 3
6 = 1
2
P(B)  =  n
N = 2
6 = 1
3
P(C)  =  n
N = 1
6

Se observa que según se define el evento, la probabilidad es diferente para el mismo experimento y el
mismo espacio muestral.
¿Si cambiamos el experimento, cambia el espacio muestral? Sí.

Ej. Experimento: Lanzar un dado una vez y observar la cara superior e inferior del dado.

Espacio muestral: S = {1,6;  2,5;  3,4;  6,1;  5,2;  4,3}

¿La probabilidad de los eventos cambia? Sí.
P(A)  =  n
N  =  6
6 =  1
P(B)  =  n
N  =  4
6 = 2
3
P(C)  =  n
N  =  2
6 = 1
3
Si cambia.

<!-- página 3 -->

Diagrama de tallo y hoja

Experimento: Lanzar una moneda al aire una vez y dos en caso que ocurra cara, si ocurre cruz
entonces lanzar un dado.

S =  {cc, cx, x1, x2, x3, x4, x5, x6}

Ej. 3: Selección aleatoria de 3 artículos de un proceso de fabricación para ser clasificados como:
D = Defectuoso
N = No defectuoso

-Construya el diagrama de tallo y hoja
-Obtenga el Espacio Muestral.

S =  {(D, D, D); (D, D, N); (D, N, D); (D, N, N); (N, D, D); (N, D, N); (N, N, D); (N, N, N)}
N = 8

También puede indicarse el Espacio Muestral con una expresión matemática en vez de listar los
elementos:
S =  {(x, y) / x2 + y2  ≤  4}    → ¿ Que es ?

<!-- página 4 -->

Teoría de conjuntos ⇒ Más definiciones
Complemento:
De un evento A del espacio muestral S es el conjunto de todos los elementos de S que no pertenecen
a A.

Del Ej. 2:
A =  {1,2,3,4}  → A = {5,6}
Del Ej. 3:
B =  {N >=  1}Al menos uno no defectuoso
B  =  {DDD}

Intersección:
De dos eventos A y B (A ∩ B) es el conjunto de todos los elementos comunes de A y B.

Ej. 4:
Sea M = {a, e, i, o, u} y N = {r, s, t}
M ∩ N = ⊘

Si dos eventos no pueden ocurrir simultáneamente se dice que son “Mutuamente Excluyentes”

Unión: Evento que contiene a todos los elementos que pertenecen a dos o más eventos del Espacio
Muestral. (A ∪ B)

Ej. 5:
Si M =  {X | 3 < X < 9} y  N = {Y | 5 < Y < 12}
M ∪ N =  {Z | 3 < Z < 12}

Representación Gráfica → Diagrama de Venn
Espacio Muestral → Un rectángulo
Eventos → Círculos dentro del rectángulo

Ej. 6:

A ∩ B =  {1,2}
B ∩ C =  {1,3}
A ∪ C =  {1,2,3,4,5,7}
B ∩ A =  {4,7}
A ∩ B ∩ C =  {1}
(A ∪ B) ∩ C  =  {2,6,7}

<!-- página 5 -->

Definición relacionada a teorema de conjuntos
Probabilidad: si un evento puede tener como resultado cualquiera de los N diferentes resultados
igualmente probables y si exactamente n de estos resultados corresponde al evento A, entonces:
P(A)  =
n
N

En muchos casos todos los eventos tienen la misma oportunidad de ocurrencia y se les asigna la
misma probabilidad.
Caso dado: S =  {1,2,3,4,5,6}

Evento A: que salga 1 en la cara superior.
P(A)  =
n
N =
1
6  (Todos los números tienen la misma probabilidad de salir)
Igualmente Probables

Cada número es un punto muestral.
El evento A corresponde en este caso a 1 punto muestral.

Evento B: {x/x < 4}  P(B)  =
3
6 (suma de los puntos muestrales) =
1
2

¿Qué sucede si no todos los puntos muestrales tienen la misma probabilidad de ocurrir?

Ej. 7: Se carga un dado de manera que sea 2 veces más probable que salga un número par que uno
impar. Calcular la probabilidad del evento B.
Evento B: {x/x < 4}

En vez de sumar los puntos muestrales correspondientes a este evento debemos hacer una suma
ponderada dando más “peso” al que tiene más probabilidad de ocurrencia.

Llamemos w a la probabilidad de que salga Impar.
Llamemos 2w a la probabilidad de que salga par.

P(S)  =  1 ⇒ suma de los puntos muestrales

P(S)  = w + 2w + w + 2w + w + 2w = 9w = 1

Entonces w =
1
9

P(x/x es impar)  =  3w =  3
9
P(x/x es par)  =  3. (2w)  =  6
9
P(B)  =  P(1) +  P(2) +  P(3)  = w + 2w + w = 4w =
4
9  P(B)  =
4
9

En muchos casos se hace difícil conocer los N diferentes resultado de un experimento para el cálculo
de probabilidad.

Para calcular en forma rápida la cantidad de elementos de un espacio muestral puede usarse la regla
de la multiplicación

<!-- página 6 -->

Regla de Multiplicación

N: N° de elementos en un Espacio Muestral que resulta de un experimento con varias operaciones.

“Si una operación puede realizarse de N1formas y por cada una de estas, una segunda operación
puede realizarse de n2formas, entonces las 2 operaciones se pueden realizar juntas de N1N2formas”

N =  N1N2  …  Ns  Ns: N° de elementos en la operación S

Del Ej. 3 ⇒ 3 elementos y 2 posibilidades (Defectuoso/No defectuoso) para cada uno.
N = n1.n2.n3 = 2.2.2 = 8
Del Ej. 2 ⇒ Se lanza un dado y luego una moneda. Obtener el número de puntos muestrales o
elementos en este espacio muestral.
N1 = 6 N° de elementos de S es 12

N1N2  =  (6)(2) = 12 N2 = 2

Ej. 8: ¿Cuántos números pares de 3 dígitos pueden formarse con los dígitos 1, 2, 5, 6 y 9 si cada uno
de ellos puede utilizarse sólo una vez?

N3 = 2    (Número par) en las unidades N1 N2 N3
⬜.⬜.2
 c  d  u

Al ocuparse un número en las unidades (u), quedan 4 números disponibles para las decenas (d).

N2 =  4  (Los 4 números restantes) ⬜.4.2
N1 = 3  (los 3 números restantes) en las centenas 3.4.2
N1. N2.  N3 =  (3). (4). (2)  =  24 números pares de 3 dígitos

Permutaciones

Número posible de arreglos de todos o algunos elementos de un Espacio Muestral.

A Todos distintos N = n!  n: N° de elementos a ordenar

Ej. 9: Considere las letras a, b, c. ¿ Cuántas formas posibles de ordenar estas letras sin repetir
ninguna existen?

n3 = 3 (puede estar cualquiera de ellas)
n2 = 2 (quedan 2)
n1 = 1 (queda 1)
N =  n1 . n2. n3  =  3!  =  6 formas
n1 n2 n3   a, b, c
⬜.⬜.⬜               a, c, b
(1)(2)(3)   b, c, a
    c, b, a
    b, a, c
    c, a, b

<!-- página 7 -->

¿Y si es posible que se repitan?
n1 = 3;   n2 = 3;  n3 = 3    ⇒    n1. n2. n3 = 27
El número de permutaciones de n objetos distintos es n!
n!  =  n. (n − 1). (n − 2). …  1 Ya que al usar un objeto en una posición, quedan (n-1) objetos para
las demás

3! = 3.2.1 = 6

Por definición:
1!  = 1
0!  = 1

Si en vez de tomar todos los elementos para arreglarlos o acomodarlos se toman solo una parte de
ellos se tiene:
   ‘N’ objetos tomados “de a ‘r’

¿Cuantas formas hay de arreglarlos? (Importa el orden. No repetir.)
n(n − 1)(n − 2)(n − r − 1) formas

B Todos distintos, se toma una parte (importa el orden).

nPr =  n!/(n − r)!

Ej. 10: De las 4 primeras letras del abecedario, tomar de a 2 sin repetir.

a,b a,c a,d

12 formas

b,a c,a d,a
b,c c,b b,d
d,b c,d d,c

nPr =  4P2  = (n − r +  1)!  =  (4 − 2 + 1)!  =  3!  =  12

nPr =  4P2  = n!
(n − r)!  =  4.3.2.1
2.1  =  12

Ej. 11: Se sacan 2 ticket de lotería para el 1° y 2° premio de un total de 20. Encuentre el número de
posibles formas de sacar el 1° y 2° premio.

n = 20   nPr = 20P2  =
n!
(n−r)! =
20!
18!  =  (20). (19)
r = 2   20P2  =  380 formas de sacar el 1° y 2° premio

<!-- página 8 -->

Ej. 12: 3 Disertantes se pueden ubicar en 5 fechas distintas. ¿ Cuál es el número total de formas en
que se podrían organizar estas 3 disertaciones?

n = 5 fechas  5P3  =
5!
(5−3)!  =  5.4.3 =  60
r = 3 disertantes

Rta: Estos 3 disertantes se pueden organizar de 60 formas diferentes.

C Caso en que no todos los elementos son distintos (algunos son iguales)

Ej. 13: Árbol de navidad   4 focos rojos
      3 focos verdes
      2 focos azules
¿Cuantas formas tengo para ordenarlas en el árbol?
Sean n objetos de los cuales:
n1  =  tipo 1
n2  =  tipo 2
...        ....
nk  =  tipo k

nPk  =  n!
n1! n2!. . . nk!
9P3  =  9!
4! 3! 2!  = 9.8.7.6.5
(3.2).2 =  1260

D Permutaciones de n objetos distintos arreglados en un círculo

nP° =  (n − 1)!
nP° =  (8 − 1)!  =  7!
8P° =  5040
3 Elementos: a, b, c

Combinatoria   Cr
n =
n
r

N° de formas posibles de seleccionar r objetos de un total de n sin importar el orden.

Del Ejemplo 4 letras del abecedario

a,b a,c a,d
de las 12
formas
sólo
quedan
6
b,a c,a d,a
b,c c,b b,d
d,b c,d d,c

<!-- página 9 -->

Cr
n = n!
r! (n − r)!
a, b, c, d
a,b b,c
a,c b,d
a,d c,d

C2
4 = 4
2  =  4!
2! 2! = 4.3.2
2.2 = 6

Ej. 14: Encuentre el número de formas de organizar comités científicos que estén representados por 2
químicos y 1 físico sabiendo que se cuenta con 4 químicos y 3 físicos.

Solución:
1. De los 4 químicos, debo elegir 2.
2. De los 3 físicos debo elegir 1.
3. Con la regla de la multiplicación puedo encontrar el n° de comités sabiendo que hay químicos y
físicos.
N = Q (formas de elegir químicos 1).F (formas de elegir físicos 2)

1. Formas de elegir 2 químicos de 4 sin importar el orden.
nQ = C2
4 = 4!
2! 2! = 6
2. Formas de elegir 1 físico de 3
 nF = C1
3 =
3!
1! = 3
3. Número de comités científicos          N = Q. F = (6). (3)  = 18 comités

Ej. 15: En una mano de póker que consiste en 5 cartas, encuentre la posibilidad de obtener 3 ases y 2
reyes si el mazo de cartas es de 52.

Solución:
A.A.A R.R
n1 n2

1. n1:formas de obtener 3 ases de 4 ases posibles
n1 = C3
4 = 4
2. n2:formas de obtener 2 reyes de 4 posibles
n2 = C2
4 = 6
3. ¿Cuantas manos de 3 ases y 2 reyes son posibles?
n = n1. n2 = 4.6 = 24 manos
4. ¿Cuantas formas de obtener esas manos de 3 ases y 2 reyes del total de cartas?
N = C5
52 = 52!
5! (47!) = 2.598.960
P(A): 3 ases y 2 reyes en una mano de poker
P(A) = n
N = 24
2.598.960

<!-- página 10 -->

Reglas Aditivas

Si un evento puede ser expresado como la unión de otros eventos entonces:
P(C)  =  P(A ∪ B)  =  P(A) +  P(B) −  P(   A ∩ B   )

Del ejemplo de unión:

A: {x/3 < x < 9};  B: {y/5 < y < 12}
P(A ∪ B)  =  K: {z/3 < z < 12}
P(A) = 5
12 ;  P(B) = 6
12 ;  P(C) = 8
12
P(C) = P(A) +  P(B) − P(A ∩ B)  =  5 + 6 − 3
12 = 8
12
En el caso de tres eventos A, B y C; para la unión de los tres, representado por el evento D, se tiene:

P(D) = P(A ∪ B ∪ C) = P(A) + P(B)  + P(C) − P(A ∩ B) − P(A ∩ C) − P(B ∩ C) + P(A ∩ B ∩ C)

Corolario:
● Si los eventos son mutuamente excluyentes ⇒ P(A ∩ B)  =  (∅)  = 0
● P(C) = P(A ∪ B)  = P(A) + P(B)
● P(D) = P(A ∪ B ∪ C) = P(A) + P(B) + P(C)
● Si los eventos pueden ser expresados como la partición del Espacio Muestral S, entonces:
 A1, A2, . . . Anson mutuamente excluyentes
Si A1, A2, . . . Anes una partición de S entonces:(A1 ∩  A2 ∩ . . .∩ An) = {∅}
P(A1 ∪ A2 ∪ A3 ∪. . .∪ An) = P(A1) + P(A2) + P(A3)+. . . +P(An) = P(S) = 1

P(A4)  =  P(S) −  P(A1 ∪ A2 ∪ A3 ∪ A5)
P(A4)  =  1 − [P(A1) + P(A2) + P(A3) + P(A5)]

<!-- página 11 -->

● Si A y B son eventos complementarios:
P(B)  =  P(A̅)
P(A) + P(A̅) = P(S)  =  1
P(A) = 1 − P(A̅) = 1 − P(B)

Probabilidad condicional

Probabilidad de ocurrencia de un evento cuando se sabe que ocurrió otro relacionado con éste.

P(B/A): Probabilidad del evento B dado que ocurrió A

Ejemplo 16: Calcular la probabilidad de que salga un número par al tirar un dado sabiendo que el
número es mayor de 3.

X: {N° del dado}

B: {X/X es par}  P(B/A) = ?  P(A) = 1/2
A: {X/X > 3}   A: {4,5,6} = P(B/A) = 2/3

Ahora A es nuestro nuevo espacio muestral porque sabemos (estamos seguros) que se produjo A.

P(B/A) = 2
3

Para el espacio muestral original

P(A ∩ B)  =  1/3 y P(A) = 1/2

Por lo tanto P(B/A)  =
P(A∩B)
P(A) =
1/3
1/2 =
2
3 Si P(A) > 0

<!-- página 12 -->

Ejemplo 17:
La probabilidad de que un vuelo programado normalmente salga a horario es P(D) = 0.83 . La
probabilidad de que llegue a horario es P(A) = 0.82 y la probabilidad de que salga y llegue a horario
es P(D∩A) = 0.78. Encuentre la probabilidad que:
a) Un avión llegue a horario sabiendo que salió a horario.
b) Un avión salió a horario sabiendo que llegó a horario.

Rta a) P(A/D)  =
P(A∩D)
P(D) =
0.78
0.83 = 0.94

Rta b) P(D/A)  =
P(A∩D)
P(A) =
0.78
0.82 = 0.95

Eventos Independientes

En probabilidad condicional vemos cómo la ocurrencia de un evento altera la probabilidad de
ocurrencia de otro siempre y cuando exista una vinculación entre ambos. Es decir, el conocimiento
adicional de la ocurrencia de un evento altera la probabilidad de otro siempre que exista dependenci a
entre ambos eventos. Justamente cuando no exista esta dependencia no se altera la probabilidad de
la ocurrencia de un evento aunque sepamos de la ocurrencia del otro evento.

Por tanto:
P(B/A) = P(B)  y P(A/B) = P(A)

Entonces A y B son eventos independientes.

Reglas multiplicativas

Si observamos la fórmula de condicionalidad de eventos decimos que:
P(B/A) . P(A)  =  P(A ∩ B)  y también  P(A/B) . P(B)  =  P(A ∩ B)

Si los eventos A y B son independientes:
P(B/A) = P(B) y P(A/B) = P(A) ⇒ P(A ∩ B) = P(A) . P(B) (Sólo para eventos independientes)

Ejemplo 18: Eventos no independientes y no excluyentes.
A: {X/X > 1};  B: {X/X sea par} en un tiro de dado.
P(B/A) = P(B); P(A/B) = P(A) ⇒ No son independientes

3
5 ≠
1
2                        1 ≠
5
6

Ejemplo 19: Comprobar que los eventos: A: {X/X es par} y  B: {X/X > 3} no son independientes al tirar
un dado.

Por el absurdo:
a) Si fueran independientes entonces:
P(B/A) = P(B)
P(A/B) = P(A)

P(B/A) = ⅔ pero P(B) = ½
P(A/B) = ⅔  pero P(A) = ½

<!-- página 13 -->

Por tanto no son independientes por la regla multiplicativa.

b) Si lo fueran

P(A ∩ B) = P(B/A) . P(A)
Para 2 eventos
P(A ∩ B) = P(A/B) . P(B)

P(A ∩ B) =
1
3 pero P(B/A) . P(A)  =
2
3 .
1
2 =
1
3
P(A ∩ B)  =  P(A) . P(B) = 1
4

Si son independientes P(B/A) = P(B) y P(A/B) . P(B) =
2
3 .
1
2 =
1
3
    P(A/B) = P(A) y P(B/A) . P(A) =
1
2 .
1
2 =
1
4
Debido a que ⅓ ≠ ¼ entonces no se cumple.

Extensión

Si en un experimento pueden ocurrir  A1, A2, A3, . . . , Aneventos, entonces:
 P(A1 ∩ A2 ∩ A3 ∩. . .∩ Ak)  =  P(A1) . P(A2/A1) . P(A3/A1 ∩ A2)  . . ..
. . . . P(Ak/A1 ∩ A2 ∩ A2 ∩ A3 . . .∩ Ak−1)
Teorema de probabilidad total

P(A) = ∑ P(Bi ∩ A)
k
i=1
 = ∑[P(Bi). P(A/Bi)]
k
i=1

Bi: Partición del Espacio Muestral ⇒∑ P(Bi)k
i=1  =  1

Si quisiéramos encontrar la probabilidad del evento A en términos de los eventos Bi donde todos los
Bi son mutuamente excluyentes.

Ejemplo 20:
En una planta de montaje existen 3 máquinas B1, B2, B3que trabajan fabricando el 30%, 45% y 25% de
las partes respectivamente. Se sabe por experiencia que el 2%, 3% y 2% de estos productos
fabricados respectivamente son defectuosos.

<!-- página 14 -->

Suponga que se selecciona de forma aleatoria 1 producto terminado.

¿Cuál es la probabilidad de que sea defectuoso?

Eventos:
A: Producto defectuoso.
B1: Producto fabricado por la máquina 1.
B2: Producto fabricado por la máquina 2.
B3: Producto fabricado por la máquina 3.

Las B1son mutuamente excluyentes (cada producto es fabricado sólo por una máquina)
P(A) = P(B1 ∩ A)  +  P(B2 ∩ A)  +  P(B3 ∩ A)  =
= P(B1) . P(A/B1) +  P(B2) . P(A/B2) +  P(B3) . P(A/B3)

=  (0.3) . (0.02)  +  (0.45) . (0.03)  + (0.25) . (0.02)  =  0.0245

Regla de Bayes (Probabilidad de las causas)

Si los eventos B1, B2,  . . . , Bkconstituyen una partición del Espacio Muestral S  y P(Bi) ≠ 0 para
i = 1,2, . . . , k  entonces cualquier evento Bren S tal que P(A) ≠ 0  puede expresarse como
P(Br/A)  =  P(Br ∩ A) / P(A)  [ Probabilidad Condicional].
Como P(A/Br )  =  P(Br ∩ A) / P(Br )  ⇒ P(Br ∩ A)  = P(Br ) . P(A/Br )

P(Br/A)  =  P(Br ∩ A)
∑ P(Bi ∩ A)k
i=1
 =  P(Br ) . P(A/Br )
∑ [P(Bi) . P(A/Bi )]k
i=1

Ejemplo 21: (Con respecto al caso anterior del Ejemplo 20):
¿Qué probabilidad existe de que lo haya fabricado la máquina 2 (B2) sabiendo que el producto elegido
al azar es defectuoso?

P(B2/A)  =  P(B2 ∩ A)
∑ P(Bi ∩ A)3
i=1
 =  P(B2) . P(A/B2 )
∑ [P(Bi) . P(A/Bi )]3
i=1

P(B2/A)  =  (0.45) . (0.03)
(0.3) . (0.02)  +  (0.45) . (0.03) + (0.25) . (0.02)  =  0.0135
0.006 +  0.0135 +  0.005 = 0.55
