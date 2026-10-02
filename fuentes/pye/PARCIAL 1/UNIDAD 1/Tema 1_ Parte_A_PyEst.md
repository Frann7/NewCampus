# Tema 1_ Parte_A_PyEst

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 1/UNIDAD 1/Tema 1_ Parte_A_PyEst.pdf` · 29 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Definición de probabilidad: ponderar la ocurrencia de un evento futuro con datos pasados. |
| 2 | Usos de la probabilidad en economía, gestión estatal y ciencias; ejemplos de costos. |
| 3 | Definiciones clásica, frecuencial (límite de n/N) y axiomática de probabilidad. |
| 4 | Teoría de conjuntos: evento, espacio muestral, experimento, punto muestral, observación, tipos de datos; ejemplo dado. |
| 5 | Definición axiomática (Kolmogorov): axiomas, 0 ≤ P(A) ≤ 1; Ω del dado con sucesos elementales. ⚠ ver el PDF: los axiomas A1–A3 son imagen, sin texto. |
| 6 | Igual a la 5 con diagrama de los sucesos elementales A1…A6 del dado. ⚠ ver el PDF: los axiomas son imagen, sin texto. |
| 7 | Ej. 1: lanzar una moneda, S = {C, X}, P(C) = 0,5. |
| 8 | Ej. 2: lanzar un dado, eventos A impar, B > 4, C = 2; P cambia según el evento. |
| 9 | Variante del Ej. 2 (cara superior e inferior): cambia S y las probabilidades. |
| 10 | Diagrama de tallo y hojas: moneda y dado, S = {cc, cx, x1…x6}; piden 2 secas y 2 caras. |
| 11 | Ej. 3: tres artículos D/N, diagrama de árbol y S de 8 elementos. |
| 12 | Espacio muestral por comprensión: S = {(x, y) / x² + y² ≤ 4}, círculo de radio 2. |
| 13 | Complemento de un evento, con los Ej. 2 y 3. |
| 14 | Intersección y unión de eventos; Ej. 4 (M ∩ N = ∅) y Ej. 5 (uniones de intervalos). |
| 15 | Diagramas de Venn; Ej. 6: A∩B, B∩C, A∪C, A∩B∩C, (A∪B)∩C con resultados. ⚠ ver el PDF: Venn con la ubicación de los elementos 1–7; barras de complemento perdidas. |
| 16 | Probabilidad como n/N con resultados igualmente probables; dado, eventos A y B (P(B) = 1/2). |
| 17 | Ej. 7: dado cargado (par = 2w, impar = w), w = 1/9, P(B) = 4/9. |
| 18 | Conteo de puntos muestrales: regla de la multiplicación N = n1·n2·…·ns. |
| 19 | Regla de la multiplicación aplicada al Ej. 3 (2·2·2 = 8) y dado más moneda (6·2 = 12). |
| 20 | Ej. 8: números pares de 3 dígitos con 1, 2, 5, 6, 9 sin repetir; 3·4·2 = 24. |
| 21 | Permutaciones de n objetos distintos: n!; 3! = 6. |
| 22 | Permutaciones de n tomados de a r: nPr = n!/(n−r)!; Ej. 10: 4P2 = 12. |
| 23 | Ej. 11: premios de lotería, 20P2 = 380; Ej. 12: 3 disertantes en 5 fechas, 5P3 = 60. |
| 24 | Permutaciones con elementos repetidos n!/(n1!…nk!); Ej. 13: focos del árbol, 1260. |
| 25 | Permutaciones circulares (n−1)!; PC5 = 24. |
| 26 | Combinaciones Cn,r = n!/(r!(n−r)!); de 4P2 = 12 a C(4,2) = 6. |
| 27 | Ejemplo de combinaciones: triángulos con 5 puntos no colineales, C(5,3) = 10. ⚠ ver el PDF: sin texto, es una imagen. |
| 28 | Ej. 14: comités de 2 químicos (de 4) y 1 físico (de 3); 6·3 = 18. |
| 29 | Ej. 15: mano de póker con 3 ases y 2 reyes; 24/2.598.960. |

<!-- página 1 -->

Definiciones:
W – Cap 2
¿Qué entendemos por probabilidad de ocurrencia de algún evento?
Permite ponderar (estimar cuantitativamente) la
ocurrencia de un evento futuro con ayuda del análisis
del mismo evento ocurrido en el pasado (Estadística).

<!-- página 2 -->

Usos o aplicaciones

En Economía: Permitir valorar la ocurrencia de un evento en términos económicos, es decir:

Evento negativo: contrastarlo con el costo de evitar que ocurra (si puedo) o pagar o perder dinero
(seguros); o reglamentar normas.

Evento positivo: invertir o no dinero para beneficiarse si el evento ocurre (lotería, etc.).

Ejemplos
●  Costo de abrir una caja adicional en peaje de autopista o en supermercado.
●  Costo de comprar un repuesto de mejor calidad en informática.
●  Costo de colocar un semáforo.
●  Costo de abrir una agencia en una localidad.
●  Costo de habilitar un nuevo cajero automático en bancos, supermercados, facultades.
●  Costo de aumentar la resistencia de partes de líneas de transmisión de energía eléctrica en redes.

En la gestión estatal: Vial, Mantenimiento, Urbanismo, Salud.
En las ciencias: Cs. Sociales, Cs. Naturales, Cs. Biológicas, Informática, Ingeniería.

Ejemplos

<!-- página 3 -->

Definiciones de Probabilidad
• Definición clásica: La probabilidad P de que suceda un evento A “P(A)” de un total
de N casos posibles igualmente probables es la razón del número de ocurrencias n
de dicho caso en el pasado y el número total de casos posibles N.
  P(A)  =
n
N
casos favorables del evento A
casos posibles del evento A

• Definición como Frecuencia Relativa: La probabilidad frecuencial o frecuentista
hace referencia a la definición de probabilidad entendida como el cociente entre el
número de casos favorables y el número de casos posibles, cuando el número de
casos tiende a infinito.
lim
N→∞
n
N = lim
N→∞
fa
N = fr = P(A)

En palabras sencillas, el valor al que tiende la probabilidad de un suceso, cuando
repetimos el experimento muchísimas veces.

• Definición Axiomática: Se define utilizando la teoría de conjuntos.

<!-- página 4 -->

Teoría de Conjuntos
La teoría de conjuntos es una rama de la lógica matemática que estudia las
propiedades y relaciones de los conjuntos: colecciones abstractas de objetos,
consideradas como objetos en sí mismas.
Evento:
Suceso que se estudia.
Subconjunto de un Espacio Muestral.

Espacio Muestral (E.M o S):
Conjunto de todos los resultados posibles de un experimento (finito o infinito).

Experimento:
Cualquier proceso que genere un conjunto de datos.

Elementos (o Puntos Muestrales):
Dato perteneciente a un Espacio Muestral.

Observación:
Registro de los datos que genera un experimento.

Tipos de datos:
Categóricos (Discretos).
Numéricos (Discretos o continuos).
1 2
3
4 5
6
S = {1, 2, 3, 4, 5, 6}
A1 = {impares}
A2 = {2, 3}
A1 A2
S
Ej: tirar el dado

<!-- página 5 -->

Definiciones de Probabilidad
0 ≤ P(A) ≤ 1
1 2
3
4 5
6
W W = {1, 2, 3, 4, 5, 6}
A1 = {1}
A2 = {2}
     .
     .
A6 = {6}
Y
Y Ó

<!-- página 6 -->

Definiciones de Probabilidad
0 ≤ P(A) ≤ 1
1 2
3
4 5
6
W W = {1, 2, 3, 4, 5, 6}
A1 = {1}
A2 = {2}
     .
     .
A6 = {6}
Y A2
Y Ó
A3 A4
A6
A5
A1

<!-- página 7 -->

Ejemplo 1: Lanzar una moneda

Experimento: Lanzar una moneda al aire 1 vez.

Observación: Dato: Indica el resultado del
                        lanzamiento según lo que
                        observo del experimento.

Elementos: C (cara), X (seca ó cruz).

Espacio Muestral:  S =  *C, X+ Conjunto de todos los elementos
                                 o puntos muestrales posibles.

Evento: Suceso Cara ( C ), un subconjunto del S.
                      P(C)  =  n
N  =  1
2  =  0,5

S
C
X

<!-- página 8 -->

Ejemplo 2: Lanzar un dado

Experimento: Lanzar un dado.

Observación: Dato: Número de puntos que muestra la cara superior
                        del dado

Elementos: 1, 2, 3, 4, 5, 6.

Espacio Muestral:  S =  1,2,3,4,5,6  Conjunto de todos los  elementos o puntos muestrales
                                 posibles.

Eventos: A -> Que salga un número impar.
                 B -> Que sea mayor que 4.             B = {x/x > 4}
                 C -> que sea un 2.                            C = {x/x = 2}

 P A =
n
N  =
3
6    ,  P B =
n
N  =
2
6  =
1
3  ,  P C =
n
N  =
1
6

1
2
3 4
5
6
S
A C
B
Se observa que según se define el evento, la probabilidad cambia para el mismo
experimento y el mismo espacio muestral.

<!-- página 9 -->

Si cambiamos el experimento ¿cambia el Espacio Muestral?
Variante del Experimento del ejemplo 2: Lanzar el dado una vez y observar la
cara superior e inferior del dado.
S = {1,6; 2,5; 3,4; 4,3; 6,1; 5,2}
¿y la probabilidad de los eventos A, B y C cambia?
1,6 2,5
3,4 4,3
5,2 6,1
S
Eventos: A -> Que salga un número impar.
                 B -> Que sea mayor que 4.             B = {x/x > 4}
                 C -> que se aun 2.                            C = {x/x = 2}
 P A =
n
N  =
6
6 = 1   ,  P B =
n
N  =
4
6  =
2
3  ,  P C =
n
N  =
2
6
A
B
C

<!-- página 10 -->

Diagrama de Tallo y Hojas
Experimento: Lanzar una moneda al aire una vez y dos en caso que ocurra cara,
si ocurre seca entonces lanzar un dado.
Cara
Suceso 1 Suceso 2 E.M
S =  *cc, cx, x1, x2, x3, x4, x5, x6+
Cruz
¿Qué probabilidad existe que ocurran dos secas en este experimento? ¿y dos caras?

<!-- página 11 -->

Ejemplo 3: Selección aleatoria de tres artículos de un proceso de
fabricación para luego ser clasificados como “D” Defectuoso; “N” No
defectuoso.

1. Construya el Diagrama de Tallo y hojas
2. Obtenga el Espacio Muestral

S =  *(D, D, D); (D, D, N); (D, N, D); (D, N, N); (N, D, D); (N, D, N); (N, N, D); (N, N, N)+

<!-- página 12 -->

También puede indicarse el Espacio Muestral con una expresión
matemática en vez de listar los elementos:
S =  *(x, y) / x2 + y2  ≤  4+                      ¿ Que es ?
r = 2
Círculo de radio 2

<!-- página 13 -->

Teoría de Conjuntos: Más definiciones
Complemento:
De un evento A del espacio muestral S es el conjunto de todos los elementos
de S que no pertenecen a A.
Del Ej. 2:
A =  *1,2,3,4+  → A = *5,6+
Del Ej. 3:
B =  *N >=  1+ Al menos uno no defectuoso
B  =  *DDD+
S =  *(D, D, D); (D, D, N); (D, N, D); (D, N, N); (N, D, D); (N, D, N); (N, N, D); (N, N, N)+
S =  1,2,3,4,5,6
Ejemplo 2
Ejemplo 3

<!-- página 14 -->

Intersección:
De dos eventos A y B, (A∩B) es el conjunto de todos los elementos comunes
de A y B.
Ejemplo 4:
Sea M = *a, e, i, o, u+ y N = r, s, t                      M ∩ N = ⊘

Unión:
Evento que contiene a todos los elementos que pertenecen a dos o más
eventos del Espacio Muestral. (A ∪ B)

Ejemplo 5:
Si M =  *X | 3 < X < 9+ y  N = *Y | 5 < Y < 12+

M ∪ N =  *Z | 3 < Z < 12+

<!-- página 15 -->

Representación Gráfica → Diagrama de Venn
Espacio Muestral → Un rectángulo
Eventos → Círculos dentro del rectángulo

A ∩ B =
B ∩ C =
A ∪ C =
B ∩ A =
A ∩ B ∩ C =
(A ∪ B) ∩ C  =
S
*1,2+
*1,3+
*1,2,3,4,5,7+
*4,7+
*1+
*2,6,7+
Ejemplo 6:

<!-- página 16 -->

Probabilidad: si un evento A puede tener como resultado cualquiera de los
N diferentes resultados igualmente probables y si exactamente n de estos
resultados corresponde al evento A, entonces: P(A)  =
n
N

En muchos casos todos los eventos tienen la misma oportunidad de ocurrencia y
se les asigna la misma probabilidad.

Caso Ejemplo 2: S =  *1,2,3,4,5,6+
Evento A: que salga 1 en la cara superior.
P(A)  =
n
N =
1
6  (Todos los números tienen la misma probabilidad de salir)
Igualmente Probables

Cada número es un punto muestral.
El evento A corresponde en este caso a un punto muestral.

Evento B: x/x < 4             P(B)  =
3
6 (suma de los puntos muestrales) =
1
2

¿Qué sucede si no todos los puntos muestrales tienen la misma probabilidad de
ocurrir?

<!-- página 17 -->

Ejemplo 7: Se carga un dado de manera que sea 2 veces más probable que salga
un número par que uno impar. Calcular la probabilidad del evento B.

Evento B: *x/x < 4+
Dado cargado
En vez de sumar los puntos muestrales correspondientes
a este evento debemos hacer una suma ponderada dando
más “peso” al que tiene más probabilidad de ocurrencia.

Llamemos w a la probabilidad de que salga Impar.
Llamemos 2w a la probabilidad de que salga par.

Según el Axioma del suceso seguro en la definición axiomática de la Probabilidad:
P(S)  =  1 ⇒ suma de los puntos muestrales

P(S)  = w + 2w + w + 2w + w + 2w = 9w = 1
Entonces:     w =
1
9
P(B)  =  P(1)  +  P(2)  +  P(3)
= w + 2w + w = 4w = 4
9

<!-- página 18 -->

Formas de Calcular  todos los resultados posibles N:
CONTEO DE PUNTOS MUESTRALES
En muchos casos se hace difícil conocer los N diferentes resultados de un
experimento para el cálculo de probabilidad.

Para calcular en forma rápida la cantidad de elementos de un espacio muestral
puede usarse la regla de la multiplicación:
Regla de Multiplicación

N: N° de elementos en un Espacio Muestral que resulta de un experimento con
varias operaciones.

“Si una operación puede realizarse de n1 formas y por cada una de estas, una
segunda operación puede realizarse de n2 formas, entonces las 2 operaciones se
pueden realizar juntas de n1n2 formas”
N =  n1n2  …  ns ns: N° de elementos en la operación.

<!-- página 19 -->

Del Ejemplo 3 ⇒ 3 elementos y 2 posibilidades (Defectuoso/No defectuoso) para
cada uno.                          →    N = n1. n2. n3 = 2. 2. 2 = 8
Diagrama de Tallo y hojas
1
2
3
4
5
6
C
X
C
X
C
X
C
X
C
X
C
X
1C
1X
1C
2X
3C
3X
4C
4X
5C
5X
6C
6X
N = 12 puntos muestrales
n1 = 6 N° de elementos de S es
12

N = n1n2  =  (6)(2) = 12
n2 = 2
Del Ejemplo 2 una variante    ⇒ Se lanza un dado y luego una moneda. Obtener el
número de puntos muestrales o elementos en este espacio muestral.

<!-- página 20 -->

Ejemplo 8: ¿Cuántos números pares de 3 dígitos pueden formarse con los
dígitos 1, 2, 5, 6 y 9 si cada uno de ellos puede utilizarse sólo una vez?
n3 = 2    (Número par) en las unidades n1 n2 n3
⬜ . ⬜ . 2
 c  d  u

Al ocuparse un número en la casilla de unidades (u), quedan 4 números
disponibles para las decenas (d).

n2 =  4  (Los 4 números restantes) ⬜ . 4. 2

n1 = 3  (los 3 números restantes) en las centenas (c)      3.4.2

n1. n2. n3 =  (3). (4). (2)  =  24 números pares de 3 dígitos

<!-- página 21 -->

Permutaciones

Número posible de arreglos de todos o algunos elementos de un Espacio Muestral.

Todos distintos N = Pn = n!  n: N° de elementos a ordenar
El número de permutaciones de n objetos distintos es n!
n!  =  n. (n − 1). (n − 2). …  1
Ya que al usar un objeto en una posición, quedan (n-1) objetos para las demás

3! = 3.2.1 = 6

<!-- página 22 -->

Si en vez de tomar todos los elementos para arreglarlos o acomodarlos se toman
solo una parte de ellos se tiene:

   n objetos tomados de a r
 ¿Cuantas formas hay de arreglarlos? (Importa el orden. No repetir.)
nPr = n!
n − r !
Ejemplo 10: De las 4 primeras letras del abecedario, tomar de a 2 sin repetir.
a,b a,c a,d

12 formas

b,a c,a d,a
b,c c,b b,d
d,b c,d d,c
nPr =  4P2  = n!
(n − r)!  =  4.3.2.1
2.1  =  12

<!-- página 23 -->

Ejemplo 11: Se sacan 2 ticket de lotería para el 1° y 2° premio de un total de 20.
Encuentre el número de posibles formas de sacar el 1° y 2° premio.
n = 20   nPr = 20P2  =
n!
(n−r)! =
20!
18!  =  (20). (19)
r = 2   20P2  =  380 formas de sacar el 1° y 2° premio

Ejemplo 12: 3 Disertantes se pueden ubicar en 5 fechas distintas. ¿ Cuál es el
número total de formas en que se podrían organizar estas 3 disertaciones?
n = 5 fechas  5P3  =
5!
(5−3)!  =  5.4.3 =  60
r = 3 disertantes

Rta: Estos 3 disertantes se pueden organizar de 60 formas diferentes.

<!-- página 24 -->

Caso en que no todos los elementos son distintos (algunos son iguales)
Ejemplo 13: Árbol de navidad   4 focos rojos
      3 focos verdes
      2 focos azules
¿Cuantas formas tengo para ordenarlas en el árbol?
Sean n objetos de los cuales:
n1  =  tipo 1
n2  =  tipo 2
            ...        ....
nk  =  tipo k

nPk  =  n!
n1! n2!. . . nk !

9P3  =  9!
4! 3! 2!  = 9.8.7.6.5
(3.2). 2 =  1260

<!-- página 25 -->

Permutaciones de n objetos distintos arreglados en un círculo
PC5 = (5-1)! = 4! = 24
El primer elemento que "se sitúe" determina el principio y el final.
Entonces se reducen las formas de ordenar el resto.
¿Porqué existe menor cantidad de permutaciones circulares que en línea?

<!-- página 26 -->

Combinatoria

N° de formas posibles de seleccionar r objetos de un total de n sin importar el orden.
Del Ejemplo 10: De las 4 primeras letras del abecedario, tomar de a 2 sin repetir.
a,b a,c a,d

12 formas

b,a c,a d,a
b,c c,b b,d
d,b c,d d,c
nPr =  4P2  = n!
(n − r)!  =  4.3.2.1
2.1  =  12
Ahora no importa el orden de las letras Quedan 6
Crn = n!
r! (n − r)! C2
4 = 4
2  =  4!
2! 2! = 4.3.2
2.2 = 6

<!-- página 27 -->



<!-- página 28 -->

Ejemplo 14: Encuentre el número de formas de organizar comités científicos
que estén representados por 2 químicos y 1 físico sabiendo que se cuenta con 4
químicos y 3 físicos.
Q
Comité Científico
Q F
Químicos: Q
Físicos: F
Solución:
De los 4 químicos, debo elegir 2.
De los 3 físicos debo elegir 1.
Con la regla de la multiplicación puedo encontrar el
n° de comités sabiendo que hay químicos y físicos.

N = nQ .nF               Regla de la multiplicación.
nQ : Formas de elegir 2 químicos de 4 sin importar el orden.
nQ = C2
4 = 4!
2! 2! = 6
nF: Formas de elegir 1 físico de 3 sin importar el orden.
nF = C1
3 = 3!
1! 3 − 1 ! = 3
Número de comités científicos
N = nQ.nF = 6.3 = 18 comités

<!-- página 29 -->

Ejemplo. 15: En una mano de póker que consiste en 5
cartas, encuentre la posibilidad de obtener 3 ases y 2
reyes si el mazo de cartas es de 52.
A.A.A R.R
n1 n2
Solución:
n1:formas de obtener 3 ases de 4 posibles
n1 = C3
4 = 4
n2:formas de obtener 2 reyes de 4 posibles
n2 = C2
4 = 6
¿Cuantas manos de 3 ases y 2 reyes
son posibles?
n = n1. n2 = 4.6 = 24 manos
¿Cuantas formas de obtener esas
manos de 3 ases y 2 reyes del total
de cartas?
N = C5
52 = 52!
5! (47!) = 2.598.960
P(A): 3 ases y 2 reyes en una mano de póker
P(A) = n
N = 24
2.598.960
