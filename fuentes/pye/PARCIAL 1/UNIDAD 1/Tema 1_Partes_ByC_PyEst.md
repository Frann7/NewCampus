# Tema 1_Partes_ByC_PyEst

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 1/UNIDAD 1/Tema 1_Partes_ByC_PyEst.pdf` · 12 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Regla aditiva P(A∪B) = P(A) + P(B) − P(A∩B), con el Ej. 5 (8/12). |
| 2 | Unión de tres eventos, corolario para excluyentes, partición de S y P(A4) = 1 − suma de los demás. |
| 3 | Eventos complementarios: P(A) + P(Ā) = 1. |
| 4 | Probabilidad condicional P(B/A); Ej. 16: par dado que es > 3, A como nuevo espacio, 2/3. |
| 5 | Ej. 16 con la fórmula P(B/A) = P(A∩B)/P(A) = (1/3)/(1/2) = 2/3. |
| 6 | Ej. 17: vuelo sale y llega a horario; P(A/D) = 0,94 y P(D/A) = 0,95. |
| 7 | Eventos independientes: P(B/A) = P(B); regla multiplicativa P(A∩B) = P(A)·P(B) solo si son independientes. |
| 8 | Ej. 18: A = {X > 1}, B par en un dado; no son independientes ni excluyentes. |
| 9 | Intersección de k eventos (regla del producto) y teorema de probabilidad total con partición Bi. |
| 10 | Ej. 20: tres máquinas con 30/45/25% y 2/3/2% defectuosos; probabilidad total 0,0245. |
| 11 | Regla de Bayes (probabilidad de las causas): fórmula con probabilidad total en el denominador. |
| 12 | Aplicación de Bayes al Ej. 20: P(B2/A) = 0,0135/0,0245 ≈ 0,55. |

<!-- página 1 -->

Seguimos con la Teoría de Conjuntos
Reglas Aditivas
Si un evento puede ser expresado como la unión de otros eventos entonces:

P(C)  =  P(A ∪ B)  =  P(A) +  P(B) −  P( A ∩ B)
Del Ejemplo 5:  Si A =  {X | 3 < X < 9} y  B = {Y | 5 < Y < 12}

A ∪ B =  {C | 3 < Z < 12}
P(A) = 5
12 ;  P(B) = 6
12 ;  P(C) = 8
12
P(C) = P(A)  +  P(B) − P(A ∩ B)  =  5 + 6 − 3
12 = 8
12

<!-- página 2 -->

En el caso de tres eventos A, B y C; para la unión de los tres, representado por
el evento D, se tiene:
P(D) = P(A ∪ B ∪ C) = P(A) + P(B)  + P(C) − P(A ∩ B) − P(A ∩ C) − P(B ∩ C) + P(A ∩ B ∩ C)
Corolario:
● Si los eventos son mutuamente
excluyentes ⇒ P(A ∩ B)  =  (∅)  = 0
● P(C) = P(A ∪ B)  = P(A) + P(B)
● P(D) = P(A ∪ B ∪ C) = P(A) + P(B) + P(C)

Si los eventos pueden ser expresados como la
partición del Espacio Muestral S, entonces:

A1, A2, . . . An   son mutuamente excluyentes

Si A1, A2, . . . An  es una partición de S
entonces:(A1 ∩  A2 ∩ . . .∩ An) = {∅}
P(A1 ∪ A2 ∪ A3 ∪. . .∪  An)
= P(A1) + P(A2) + P(A3)+. . . +P(An)
= P(S) = 1
P(A4)  =  P(S) −  P(A1 ∪ A2 ∪ A3 ∪ A5)
P(A4)  =  1 − [P(A1) + P(A2) + P(A3) + P(A5)]

<!-- página 3 -->

• Si A y B son eventos complementarios:
P(B)  =  P A
P(A) + P(A) = P(S)  =  1
P(A) = 1 − P(A) = 1 − P(B)

<!-- página 4 -->

Probabilidad condicional

Probabilidad de ocurrencia de un evento cuando se sabe que ya ocurrió
otro relacionado con éste.
P(B/A): Probabilidad del evento B dado que ocurrió A
Ejemplo 16: Calcular la probabilidad de que salga un número par
al tirar un dado sabiendo que el número es mayor de 3.
Llamemos a X: {N° del dado}
Evento B: {X/X es par}
Evento A: {X/X > 3}
P(A) = 1/2
A: {4,5,6} = P(B/A) = 2/3
Ahora A es nuestro nuevo espacio muestral porque
sabemos (estamos seguros) que se produjo A.
RESULTADO
1
2
3 4
5
6
S
A
B

<!-- página 5 -->

Probabilidad condicional

Probabilidad de ocurrencia de un evento cuando se sabe que ya ocurrió
otro relacionado con éste.
P(B/A): Probabilidad del evento B dado que ocurrió A
Ejemplo 16: Calcular la probabilidad de que salga un número
par al tirar un dado sabiendo que el número es mayor de 3.
Ahora lo planteamos para el espacio muestral original  S:
P(A ∩ B)  =  1/3
P(A) = 1/2
Por lo tanto: P(B/A)  =  P(A ∩ B)
P(A) = 1/3
1/2 = 2
3
Siempre que  P(A) > 0
1
2
3 4
5
6
S
A
B

<!-- página 6 -->

Ejemplo 17:
La probabilidad de que un vuelo programado normalmente salga a horario es
P(D) = 0.83. La probabilidad de que llegue a horario es P(A) = 0.82 y la
probabilidad de que salga y llegue a horario es P(D∩A) = 0.78. Encuentre la
probabilidad que:

a) Un avión llegue a horario sabiendo que salió a horario.
b) Un avión salió a horario sabiendo que llegó a horario.
P(A/D)  =  P(A ∩ D)
P(D) = 0.78
0.83 = 0.94
Respuestas:
a)
b)  P(D/A)  =  P(A ∩ D)
P(A) = 0.78
0.82 = 0.95

<!-- página 7 -->

Eventos Independientes

En probabilidad condicional vemos cómo la ocurrencia de un evento altera la
probabilidad de ocurrencia de otro siempre y cuando exista una vinculación
entre ambos. Es decir, el conocimiento adicional de la ocurrencia de un evento
altera la probabilidad de otro siempre que exista dependencia. Justamente
cuando no exista esta dependencia no se altera la probabilidad de la
ocurrencia de un evento aunque sepamos de la ocurrencia del otro.
A esto llamamos EVENTOS INDEPENDIENTES
Por tanto:

P(B/A) = P(B) y P(A/B) = P(A)

Entonces A y B son eventos independientes.
Corolario: Regla multiplicativa solamente si los eventos son independientes
Si observamos la fórmula de condicionalidad de eventos decimos que:
P(B/A) . P(A)  =  P(A ∩ B) y también   P(A/B) . P(B)  =  P(A ∩ B)

Si los eventos A y B son independientes:
P(B/A) = P B    y P(A/B) = P(A)                     P(A ∩ B) = P(A) . P(B)

<!-- página 8 -->

Ejemplo 18:
A: {X/X > 1}; B: {X/X sea par}  en un tiro del dado.

a) ¿Son independientes?
b) ¿Son excluyentes?
Respuestas:
a) Para saber si son independientes verificamos las relaciones:
P(B/A) = P(B); P(A/B) = P(A)
Observamdo el Diagrama de Venn:
P(B/A) = P(B); 3
5 ≠ 1
2

          P(A/B) = P(A); 1 ≠
5
6
P(B/A)  =  P(A ∩ B)
P(A) = 1/2
5/6 = 3
5
P(A/B)  =  P(A ∩ B)
P(B) = 1/2
1/2 = 1
Aplicando las fórmulas de Probabilidad condicional:
a) No son independientes
b) No son excluyentes

<!-- página 9 -->

Extensión de la Intersección de eventos:

Si en un experimento pueden ocurrir  A1, A2, A3, . . . , Aneventos, entonces:
 P(A1 ∩ A2 ∩ A3 ∩. . .∩ Ak)  =  P(A1) . P(A2/A1) . P(A3/A1 ∩ A2)  . . . .
. . . . P(Ak/A1 ∩ A2 ∩ A2 ∩ A3 . . .∩ Ak−1)
Teorema de probabilidad total
Dado un evento A que puede ser descripto por suma de las intersecciones de éste con
eventos mutuamente excluyentes:
,    formados como una partición del Espacio Muestral S. Bi =  P(Bi)
k
i=1
 =  1

S
Entonces, según la fórmula de intersección de eventos:
P(A) =  P(Bi ∩ A)
k
i=1
 =  P Bi . P(A/Bi)
k
i=1

<!-- página 10 -->

Ejemplo 20:
En una planta de montaje existen 3 máquinas B1, B2, B3 que trabajan fabricando el
30%, 45% y 25% de las partes respectivamente. Se sabe por experiencia que el 2%, 3%
y 2% de estos productos fabricados respectivamente son defectuosos.
Suponga que se selecciona de forma aleatoria 1 producto terminado.
¿Cuál es la probabilidad de que sea defectuoso?
Resolución
Eventos:
A: Producto defectuoso.
B1: Producto fabricado por la máquina 1.
B2: Producto fabricado por la máquina 2.
B3: Producto fabricado por la máquina 3.
P B1 = 30%,
P B2 = 45%,
P B3 = 25%,
3%
P(A B1 ) = 2%
P(A B2) = 3%
P(A B3) = 2%
P A =  [P Bi . P(A Bi)] =
3
i=1

B1
B2
B3
A
S
30%
45%
25%
2%
2%
0.3 0.02 + 0.45 0.03 + 0.25 0.02 = 0.0245

<!-- página 11 -->

Regla de Bayes (o Probabilidad de las Causas)
Si los eventos B1, B2, . . . , Bkconstituyen una partición del Espacio Muestral S y
P(Bi) ≠ 0 para i = 1, 2, . . . , k entonces cualquier evento Br en S tal que
P(A) ≠ 0 puede expresarse como :
P(Br/A)  =  P(Br ∩ A) / P(A)  [ Probabilidad Condicional]
Como por la regla de la intersección: P(Br ∩ A)  = P(Br ) . P(A/Br )
Entonces:
P(Br/A)  =  P(Br ∩ A)
 P(Bi ∩ A)k
i=1
 =  P(Br ) . P(A/Br )
 P(Bi) . P(A/Bi )k
i=1

S
Y por el teorema de la Probabilidad Total:  P A =  [P Bi . P(A Bi)]
k
i=1

<!-- página 12 -->

En el ejemplo 20:
Si el artículo seleccionado es defectuoso.
¿Qué probabilidad existe que lo haya fabricado B2?
P(B2/A)  =  P(B2 ∩ A)
 P(Bi ∩ A)3
i=1
 =  P(B2) . P(A/B2 )
 P(Bi) . P(A/Bi )3
i=1

P(B2/A)  =  (0.45) . (0.03)
(0.3) . (0.02)  +  (0.45) . (0.03)  +  (0.25) . (0.02)
=  0.0135
0.006 +  0.0135 +  0.005 = 0.55
S
P(Br/A)  =  P(Br ∩ A)
 P(Bi ∩ A)k
i=1
 =  P(Br ) . P(A/Br )
 P(Bi) . P(A/Bi )k
i=1
