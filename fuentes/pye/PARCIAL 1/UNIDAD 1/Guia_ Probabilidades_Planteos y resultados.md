# Guia_ Probabilidades_Planteos y resultados

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 1/UNIDAD 1/Guia_ Probabilidades_Planteos y resultados.pdf` · 11 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Resuelto Ej. 2.55: P(A∪B)=0,8, intersección y ninguna ciudad con De Morgan; resultados 0,3 y 0,2. |
| 2 | Resuelto Ej. 2.56: inversión en bonos o fondos, unión 0,75 y ninguno 0,25. |
| 3 | Resuelto Ej. 2.57: letra del alfabeto (26) vocal, antes de la j, después de la g; Laplace. |
| 4 | Resuelto Ej. 2.58: defectos de frenos o combustible, unión 0,27 y complemento 0,73. |
| 5 | Resuelto Ej. 2.59: código de 3 letras y 4 dígitos, regla de multiplicación y variaciones; ≈ 0,0855. |
| 6 | Resuelto Ej. 2.61: dos cartas sin reemplazo mayores que 2 y menores que 8; 20·19/(52·51) ≈ 0,1433. |
| 7 | Resuelto Ej. 2.62: 3 libros de 9 con combinaciones: diccionario 1/3, 2 novelas y 1 poema 5/14. |
| 8 | Resuelto Ej. 2.63: mano de póker, 3 ases ≈ 0,001736 y 4 corazones y 1 trébol ≈ 0,003576. |
| 9 | Resuelto Ej. 2.68: vida del componente, complementos 0,58 y 0,96. |
| 10 | Resuelto Ej. 2.69: fallar y deformarse excluyentes; no falla 0,8, unión 0,55, perfecto 0,45. |
| 11 | Síntesis: unión, De Morgan, complemento y sucesos mutuamente excluyentes. |

<!-- página 1 -->

Sean los sucesos:
 A: “La fábrica se ubica en Shanghai”; P(A)=0,7
 B: “La fábrica se ubica en Beijin”; P(B)=0,4
 P A ∪ B = 0,8
Probabilidad y Estadística
Ejercicios de Probabilidades
Ejercicio
2.55
Licenciatura en Sistemas de Información – FCYT UADER
Recordando que la unión representa “ocurren A
o B o ambos” aunque como la disyunción es
inclusiva muchas veces omitimos decir “o
ambos”, pero siempre está incluida.
a) La probabilidad de que la industria se
ubique en ambas ciudades: P(A ∩ B)
0,8 = 0,7 + 0,4 − P(A ∩ B)
P A ∩ B = 1,1 − 0,8
P A ∩ B = 0,3
Recordando que la intersección representa
“ocurren A y B”.
Pág.
11
b) Probabilidad de que la industria se
ubique en ninguna de esas ciudades:
P ഥA ∩ ഥB
P ҧA ∩ തB = 0,2
P A ∪ B = P A + P B − P(A ∩ B)
“no en Shanghai y no en Beijin”
Recordando que ҧA representa que “no ocurre A”
P ҧA ∩ തB = P A ∪ B
= 1 − P(A ∪ B)
= 1 − 0,8
Leyes de De
Morgan
para conjuntos:
A ∪ B = ҧA ∩ തB
A ∩ B = ҧA ∪ തB
P ҧA = 1 − P(A)

<!-- página 2 -->

Sean los sucesos:
 B: “invertirá en bonos libres de impuestos”; P(B)=0,6
 F: “invertirá en fondos mutualistas”; P(F)=0,3
 B ∩ F : “invertirá en ambos”; P B ∩ F = 0,15
Probabilidad y Estadística
Ejercicios de Probabilidades
Ejercicio
2.56
Licenciatura en Sistemas de Información – FCYT UADER
a) La probabilidad de que invierta en bonos
libres de impuestos o en fondos mutualistas.
P B ∪ F = P B + P F − P B ∩ F
P B ∪ F = 0,6 + 0,3 − 0,15
P B ∪ F = 0,75
b) La probabilidad de no invierta en ninguno
de esos instrumentos.
P A ∪ B = P A + P B − P(A ∩ B) P തB ∩ തF = P B ∪ F
= 1 − P(B ∪ F)
= 1 − 0,75
= 0,25
“no B y no F”
Ley de De Morgan
Prob. de complemento

<!-- página 3 -->

a) A: “sea una vocal excepto la y”
Como “y” no es vocal, contabilizamos 5
vocales del espacio muestral que serán el
numerador de la probabilidad y el
denominador siempre es la cantidad total de
puntos muestrales.
P A =
5
26
b) B: “esté listada en algún lugar antes de la j”
P B = 9
26
Sea el experimento aleatorio: ε: “elegir al azar una letra del alfabeto inglés”
Averiguamos que el alfabeto inglés tiene 26 letras, por lo tanto el espacio muestral S está
formado por 26 puntos muestrales.
N° de vocales
Probabilidad y Estadística
Ejercicios de Probabilidades
Ejercicio
2.57
Licenciatura en Sistemas de Información – FCYT UADER
Pág.
5
c) C: “esté listada en algún lugar después de
la g”.
P C = 19
26
Probabilidad: si un experimento puede tener como resultado cualquiera de los N
diferentes resultados igualmente probables y si exactamente n de estos resultados
corresponden al evento A, entonces: P A =
n
N
N° de elementos de S
Todos los resultados podemos dejarlos expresados
como fracciones irreducibles o números decimales
aproximados a 4 cifras decimales.

<!-- página 4 -->

Sean los sucesos:
 F: “que haya defecto en el sistema de frenos”; P(F)=0,25
 T: “que haya defecto en la transmisión”; P(T)=0,18
 C: “que haya defecto en el sistema de combustible”; P(C)=0,17
 A: “que haya defecto en otra área”; P(A)=0,40
Probabilidad y Estadística
Ejercicios de Probabilidades
Ejercicio
2.58
Licenciatura en Sistemas de Información – FCYT UADER
a) La probabilidad de que el defecto esté en
los frenos o en el sistema de combustible,
siendo que la probabilidad de efectos
simultáneos en ambos sistemas es de 0,15.
P F ∩ C = 0,15.
P F ∪ C = P F + P C − P F ∩ C
P F ∪ C = 0,25 + 0,17 − 0,15
P F ∪ C = 0,27
b) La probabilidad de que no haya defectos
en los frenos o en el sistema de combustible.
P A ∪ B = P A + P B − P(A ∩ B)
P F ∪ C = 1 − P(F ∪ C)
= 1 − 0,27
= 0,73

<!-- página 5 -->

Sea el experimento aleatorio:
ε: “seleccionar al azar un artículo con un código formado por 3 letras distintas seguidas por 4 dígitos
distintos de cero”
Sea el suceso A: “el código elegido comienza con vocal y el último dígito es par”.
Para calcular la probabilidad de A, comenzaremos calculando el denominador (elementos de S) y luego el
numerador (elementos de A), atendiendo a que importa el orden de las letras y números, pues mismas letras
y números originan muchos códigos sólo permutando sus elementos.
P A = 5. 25. 24 . 9 . 9 . 9 .4
26. 25. 24 . 9 . 9 . 9 .9 = 5 . 4
26 . 9 ≅ 0,0855
Aquí solo lo razonamos empleando la regla de la multiplicación (pág. 6) pero podemos recurrir a
variaciones (n elementos tomados de a r, r≤n, importa el orden). Cualquiera de las dos estrategias es
válida.
P A = 5. V26
2 VR9
3. 4
V26
3 VR9
4
Probabilidad y Estadística
Ejercicios de Probabilidades
Ejercicio
2.59
Licenciatura en Sistemas de Información – FCYT UADER
Código:                ___ ___ ___       ___ ___ ___ ___
3 letras distintas
(26 letras del abecedario)
4 dígitos no nulos,
se pueden repetir
(9 dígitos no nulos)
Al no poderse repetir las letras, a
la 1era. letra la elegimos de 26, la
2da. de 25 y la 3ra. de 24.
Al poderse repetir los dígitos,
el 1ero. lo elegimos de entre 9,
2do., 3ero. y 4to. También.
Elegimos un 1 dígito par de entre 4Elegimos una vocal de entre 5
Primero anotar
denominador,
luego
numerador

<!-- página 6 -->

Sea el experimento aleatorio:
ε: “Se sacan dos cartas de una baraja sin reemplazo”
Si bien no se aclara pero el libro trabaja con cartas de póker en sus ejercicios (52: 13 de trébol, 13 de
diamante, 13 de corazón y 13 de pica).
A: “ambas cartas sean mayores que 2 y menores que 8”.
Para calcular la probabilidad de A, comenzaremos calculando el denominador (elementos de S) y
luego el numerador (elementos de A), atendiendo en este caso a que importa el orden en que las
extraemos y que no pueden repetirse ya que no se devuelve la primera carta al mazo antes de sacar la
segunda.
P A = 20 . 19
52 . 51 ≅ 0,1433
O bien empleando variaciones:
P A = V20
2
V52
2
Probabilidad y Estadística
Ejercicios de Probabilidades
Ejercicio
2.61
Licenciatura en Sistemas de Información – FCYT UADER
Al no haber reemplazo la primera
carta la elijo entre 52, y la
segunda entre 51.
Hay 5 números mayores que 2 y
menores que 8 en las cartas, para los
4 palos.Primero anotar
denominador,
luego
numerador
La siguiente la elijo entre 19, porque
no hay reemplazo.

<!-- página 7 -->

a) A: “se seleccione diccionario”
Para calcular esta probabilidad comenzamos
escribiendo el denominador. Son todos los
puntos muestrales de S, que serán todas las
posibles extracciones de 3 libros seleccionados
de un total de 9, sin reposición y sin importar el
orden. Luego, para obtener el numerador
bastará con contabilizar cuántas de esas
extracciones contienen el diccionario.
P A =
1
1
8
2
9
3
=
1
3
Para verificar: La suma de las bases (órdenes) de los
números combinatorios del numerador es igual a la base
(orden) del número combinatorio del denominador.
Sea el experimento aleatorio:
ε: “extraer al azar 3 libros de un librero que contiene 5 novelas, 3 libros de poemas y 1 diccionario”
Si pensamos que extraemos los 3 libros para leer el fin de semana, la idea es que sacamos uno y no
los devolvemos antes de extraer el siguiente (no habrá repetición), y tampoco tendrá importancia el
orden en que los elegimos. En este caso trabajaremos con combinaciones (n elementos tomados de a
r, r≤n, no importa el orden) que las calculamos por definición empleando números combinatorios.
Diccionario
Probabilidad y Estadística
Ejercicios de Probabilidades
Ejercicio
2.62
Licenciatura en Sistemas de Información – FCYT UADER
No diccionario
b) B: “se seleccionen 2 novelas y 1 poema”
P B =
5
2
3
1
1
0
9
3
=
5
14
DiccionarioPoemasNovelas
En la calculadora para ingresar un
número combinatorio de base n y
orden r ingresamos:
n nCr r     ó n shift % r
Primero anotar
denominador,
luego
numerador

<!-- página 8 -->

a) A: “tener tres ases”
Para calcular esta probabilidad comenzamos
escribiendo el denominador. Son todos los
puntos muestrales de S, que serán todas las
posibles manos de 5 cartas de un total de 52, sin
reposición y sin importar el orden. Luego, para
obtener el numerador bastará con contabilizar
cuántas de esas manos tienen 3 ases.
P A =
4
3
48
2
52
5
≅ 0,001736
Para verificar: La suma de las bases (órdenes) de los
números combinatorios del numerador es igual a la base
(orden) del número combinatorio del denominador.
Consideramos una mano de póker formada por 5 cartas extraídas de una baraja con 52
cartas (13 de trébol, 13 de diamante, 13 de corazón y 13 de pica).
En este ejercicio tampoco se usa el reemplazo y no interesa el orden en que han salido las
cartas del mazo.
Ases
Probabilidad y Estadística
Ejercicios de Probabilidades
Ejercicio
2.63
Licenciatura en Sistemas de Información – FCYT UADER
No ases
b) B: “tener 4 corazones y 1 trébol”
P B =
13
4
13
1
13
0
13
0
52
5
≅ 0,003576
PicaTrébolCorazón Diamante

<!-- página 9 -->

a)
ҧA: “la vida del componente es menor o igual a
6000 horas”.
P ഥA = 1 − P A = 1 − 0,42 = 0,58
Sean los sucesos
A: “el componente funciona más de 6000 horas”; P(A)=0,42
B: “el componente no dura más de 4000 horas”; P(B)=0,04.
Probabilidad y Estadística
Ejercicios de Probabilidades
Ejercicio
2.68
Licenciatura en Sistemas de Información – FCYT UADER
0
A
6000
0 4000
B
b)
തB: “la vida del componente es mayor a 4000
horas”.
P ഥB = 1 − P B = 1 − 0,04 = 0,96
0 6000
AഥA ഥB
0 4000
B

<!-- página 10 -->

Sean los sucesos:
 A: “el componente falle en una prueba específica”; P(A)=0,20
 B: “el componente se deforme pero no falle en la prueba”; P(B)=0,35
Notar que A y B son sucesos mutuamente excluyentes ya que A ∩ B = ∅
Probabilidad y Estadística
Ejercicios de Probabilidades
Ejercicio
2.69
Licenciatura en Sistemas de Información – FCYT UADER
a) La probabilidad de que el componente no
falle en la prueba.
P ҧA = 1 − P A = 1 − 0,2 = 0,8
b) La probabilidad de que funcione
perfectamente (ni falle ni se deforme).
c) Probabilidad de que el componente falle o
se deforme en la prueba.
P A ∪ B = P A + P B = 0,55
P ҧA ∩ തB = P A ∪ B
= 1 − P(A ∪ B)
= 1 − P A + P B
= 1 − 0,20 + 0,35
= 0,45
“no A y no B”
Ley de De Morgan
Prob. de complemento
Unión de suc.
mutuamente
excluyentes

<!-- página 11 -->

Probabilidad y Estadística
Ejercicios de Probabilidades
Síntesis
Licenciatura en Sistemas de Información – FCYT UADER
Dados dos sucesos A y B cualesquiera:
P A ∪ B = P A + P B − P(A ∩ B)
Leyes de De Morgan:
A ∪ B = ҧA ∩ തB
A ∩ B = ҧA ∪ തB
Probabilidad del complemento de un suceso
P ҧA = 1 − P(A)
Dados dos sucesos A y B mutuamente excluyentes:
P A ∪ B = P A + P B
A y B son sucesos mutuamente excluyentes
si y sólo si A ∩ B = ∅ o bien P A ∩ B = 0
