# md - teo - 2026 - U4

Fuente: `C:/Users/Administrator/Downloads/MATDISCRETA/Catedra/Unidad 4 - Relaciones de recurrencia/md - teo - 2026 - U4.pdf` · 41 página(s) · texto extraído con pypdf.
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
| 10 |  |
| 11 |  |
| 12 |  |
| 13 |  |
| 14 |  |
| 15 |  |
| 16 |  |
| 17 |  |
| 18 |  |
| 19 |  |
| 20 |  |
| 21 |  |
| 22 |  |
| 23 |  |
| 24 |  |
| 25 |  |
| 26 |  |
| 27 |  |
| 28 |  |
| 29 |  |
| 30 |  |
| 31 |  |
| 32 |  |
| 33 |  |
| 34 |  |
| 35 |  |
| 36 |  |
| 37 |  |
| 38 |  |
| 39 |  |
| 40 |  |
| 41 |  |

<!-- página 1 -->

Matem´atica Discreta
Licenciatura en Sistemas de Informaci´on
Docentes
Vaira, Stella - Fedonczuk, Miguel
Colliard, David - Cottonaro, Mariana - Froloff, B´arbara
FCyT - UADER
2025

<!-- página 2 -->

Unidad 4: Relaciones de recurrencia.
La relaci´on de recurrencia lineal de primer orden. La relaci´on de recu-
rrencia lineal homog´enea de segundo orden, con coeficientes constan-
tes. La relaci´on de recurrencia no homog´enea. Aplicaciones.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 2 / 41

<!-- página 3 -->

Sucesi´on num´erica
Una sucesi´on num´erica es una funci´on de dominio natural y codominio
real. Es decir,
f : N → R
La variable, que en este caso asume los valores de los n ´umeros natura-
les, se simboliza con n.
f : n→f (n)
Los valores asumidos por la sucesi´on, es decir las im´agenes, determinan
un conjunto ordenado que lo podemos anotar:
{f (1);f (2);f (3);...}
Como f (n) es el n-´esimo t´ermino de la sucesi´on, la anterior notaci´on se
sustituye por una letra afectada a un sub´ındice:
{a1;a2;a3;...}
En forma abreviada, se simbolizar´a {an}, donde an recibe el
nombre de t´ermino general de la sucesi´on.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 3 / 41

<!-- página 4 -->

Ejemplos
1
 n
n + 1

=
1
2; 2 3; 3 4; 4 5;... 
2 {(−1)n} = {−1;1;−1;1;...}
3

1 + 1 n  =  2; 3 2; 4 3; 5 4;... 
4
 1
2n

=
1
2; 1 4; 1 8;... 
5 {n} = {1;2;3;4;...}
Actividad 1
Para cada una de las sucesiones
listadas, determinar a10, y si es
posible extender el dominio a
N0.
En general, su representaci´on gr´afica
tradicional en el plano no se utiliza, en
cambio se opta por su representaci´on
en la recta, como se puede ver en el
siguiente ejemplo:
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 4 / 41

<!-- página 5 -->

Recursividad
A veces es dif´ıcil definir un objeto (secuencia, funci´on, conjunto, ...)
de forma expl´ıcita. Sin embargo, puede ser f´acil definir este objeto en
t´erminos de s´ı mismo. Este proceso se denomina recursividad.
Cuando definimos un conjunto de forma recursiva, especificamos algu-
nos elementos iniciales en un paso base y proporcionamos una regla
para construir nuevos elementos a partir de los que ya tenemos en el
paso recursivo.
Ejemplo 1 (factorial de un n ´umero)
• Paso Base: 0! = 1
• Paso Recursivo: n! = n· (n− 1)!,∀n≥ 1
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 5 / 41

<!-- página 6 -->

Ejemplo 2 (sumatorias)
• Paso Base:
0X
k=0
ak = a0
• Paso Recursivo:
n+1X
k=0
ak =
nX
k=0
ak + an+1,∀n≥ 0
Ejemplo 3 (la sucesi´on de los n ´umeros arm´onicos)
• Paso Base: H1 = 1
• Paso Recursivo: Hn+1 = Hn + 1 n + 1,∀n≥ 1
Actividad 2
Calcular los 5 primeros t´erminos de la sucesi´on de n ´umero arm´onicos.
Es claro que una sucesi´on queda determinada no solo por su expresi´on
recursiva, sino tambi´en por su valor inicial fijado en el paso base.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 6 / 41

<!-- página 7 -->

Algunos ejemplos de definiciones recursivas trabajadas en Lenguajes
Ejemplo 4 (potencia de un alfabeto)
• Paso Base: Σ1 = Σ
• Paso Recursivo: Σn+1 = {xy/x∈ Σ,y∈ Σn}
Ejemplo 5
Dado Σ = {0,1}, queremos definir recursivamente el lenguaje A de todas
las palabras de longitud par que sean capic ´uas.
• Paso Base: λ∈A
• Paso Recursivo: ∀x∈A : 1x1 ∈A∧ 0x0 ∈A
Ejemplo 6
Ahora el lenguaje B contiene a todas las palabras capic ´uas de longitud
impar.
• Paso Base: 0 ∈B∧ 1 ∈B
• Paso Recursivo: ∀x∈B : 1x1 ∈B∧ 0x0 ∈B
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 7 / 41

<!-- página 8 -->

Ejemplo 7 (sucesiones peri´odicas)
• Paso Base: x0 = 1,x1 = 4,x2 = 7
• Paso Recursivo: xn+3 = xn,∀n≥ 0
{1,4,7,1,4,7,1,4,7,1,4,7,...}
Ejemplo 8 (progresiones artim´eticas)
Se denomina as´ı a toda sucesi´on en que cada t´ermino, menos el primero,
se obtiene sumando al anterior una cantidad fija.
• Paso Base: a0 = −2
• Paso Recursivo: an = an−1 + 3,∀n≥ 1
{−2,1,4,7,10,13,16,19,...}
Ejemplo 9 (progresiones geom´etricas)
Se denomina as´ı a toda sucesi´on en que cada t´ermino, menos el primero,
se obtiene multiplicando al anterior una cantidad fija.
• Paso Base: a0 = 3
• Paso Recursivo: an = −2an−1,∀n≥ 1
{3,−6,12,−24,48,−96,...}
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 8 / 41

<!-- página 9 -->

Relaci´on de recurrencia
Una relaci ´on de recurrencia para una sucesi´on {an} es una expresi´on
que relaciona su t´ermino general an con uno o m´as t´erminos preceden-
tes a0, a1, a2, ... an−1, para cualquier n entero mayor o igual que un
entero inicial m. Los valores de los primeros t´erminos necesarios para
empezar a calcular se llaman condiciones iniciales.
Resolver una ecuaci ´on recurrente es encontrar una funci´on de n
expl´ıcita f (n) tal que an = f (n),∀n≥ 0
Por ejemplo, para la relaci´on de recurrencia
 an = −2an−1,∀n≥ 1 a0 = 3
{3,−6,12,−24,48,−96,...}
Verificar que su soluci´on es an = 3(−2)n,∀n≥ 0
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 9 / 41

<!-- página 10 -->

Relaci´on de recurrencia lineales
Una relaci ´on de recurrencia de orden k se llama relaci ´on de recurren-
cia lineal cuando su t´ermino general an es combinaci´on lineal de sus k
t´erminos anteriores m´as una funci´on g(n) que es independiente de di-
chos t´erminos:
an = α1an−1 + α2an−2 + ··· + αkan−k + g(n),∀n≥k
Si g(n) ≡ 0, la relaci´on de recurrencia lineal se denomina homog´enea;
caso contrario, se llamar´a no homog´enea.
Como se puede observar, el orden de una relaci´on de recurrencia es
la diferencia entre el mayor y el menor sub´ındice que aparecen en la
relaci´on. As´ı, por ejemplo:
• an+2 − 3an = 0 es de segundo orden.
• an+1 − 3an−1 + an−2 + n2 = 0 es de tercer orden.
• an + an−2 + 2n = 0 es de segundo orden.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 10 / 41

<!-- página 11 -->

RR LINEAL (a coeficientes constantes) DE PRIMER ORDEN HOMOG ´ENEA
Buscaremos inductivamente la soluci´on para este tipo de RR
 an = dan−1,∀n≥ 1 a0 = A (dado)
• a1 = d·a0 = dA
• a2 = d·a1 = d(dA) = d2A
• a3 = d·a2 = d(d2A) = d3A
• a4 = d·a3 = d(d3A) = d4A
•···
• an = d·an−1 = d(dn−1A) = dnA
Soluci´on
an = Adn,∀n≥ 0
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 11 / 41

<!-- página 12 -->

Actividad 3
Dada la siguiente relaci´on de recurrencia
 2an + an−1 = 0,∀n≥ 1 a0 = 48
1 Listar los primeros 4 t´erminos de la sucesi´on que genera.
2 Resolverla.
3 Determinar k, tal que ak = −0,09375.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 12 / 41

<!-- página 13 -->

Actividad 4
Dada la sucesi´on {5,−2, 4 5 ,− 8 25 , 16 125 ,− 32 625 , 64 3125 ...}
1 Justificar por qu´e es una progresi´on geom´etrica.
2 Encontrar una RR, con una condici´on inicial, que determine de ma-
nera ´unica dicha sucesi´on.
3 Resolver dicha RR.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 13 / 41

<!-- página 14 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los ejercicios del 1 al 6 del cap´ıtulo 10, secci´on
10.1 (P´agina 470) del libro Matem´atica Discreta de Ralph Grimaldi que
se encuentra en el campus virtual.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 14 / 41

<!-- página 15 -->

RR LINEAL (a coeficientes constantes) DE SEGUNDO ORDEN HOMOG ´ENEA
Buscaremos una soluci´on de la forma an = Arn, con A , 0 y r , 0, para
este tipo de RR
 Cnan + C1an−1 + C2an−2 = 0,∀n≥ 2 a0; a1 (dados)
• Cnan + C1an−1 + C2an−2 = 0
• CnArn + C1Arn−1 + C2Arn−2 = 0
• Arn−2  Cnr2 + C1r + C2  = 0 y como Arn−2 , 0
• Cnr2 + C1r + C2 = 0 (ecuaci´on caracter´ıstica)
Sean r1 y r2 soluciones de la ecuaci´on caracter´ıstica, la
soluci´on de la RR depender´a de las caracter´ısticas de las mismas.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 15 / 41

<!-- página 16 -->

CASO 1
Para r1 y r2 reales y distintas:
an = A1rn 1 + A2rn 2 ,∀n≥ 0
Donde las constantes A1 y A2 depender´an de las condiciones iniciales.
Ejemplo 10:
Resolver a0 = 9;a1 = −7;an + an−1 − 6an−2 = 0,∀n≥ 2
• r2 + r− 6 = 0 (ecuaci´on caracter´ıstica)
• r1 = 2 y r2 = −3 (soluciones de la ecuaci´on caracter´ıstica)
• an = A12n + A2(−3)n,∀n≥ 0
• Calculamos A1 y A2 a partir de las condiciones iniciales:
•
 a0 = 9 a1 = −7 ⇔  A120 + A2(−3)0 = 9 A121 + A2(−3)1 = −7 ⇔  A1 + A2 = 9 2A1 − 3A2 = −7 ⇔  A1 = 4 A2 = 5
• Soluci´on:



an = 4 · 2n + 5(−3)n,∀n≥ 0
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 16 / 41

<!-- página 17 -->

Actividad 5
Resolver a0 = 1;a1 = 4;an− 6an−1 + 5an−2 = 0,∀n≥ 2
1 Determinar los primeros cinco t´erminos de la sucesi´on que genera.
2 Resolver dicha RR para calcular a10
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 17 / 41

<!-- página 18 -->

CASO 2
Para r1 y r2 reales e iguales: r1 = r2 = r
an = A1rn + A2rnn,∀n≥ 0
Donde las constantes A1 y A2 depender´an de las condiciones iniciales.
Ejemplo 11:
Resolver a0 = 7;a1 = 8;an+2 = 4an+1 − 4an,∀n≥ 0
• r2 − 4r + 4 = 0 (ecuaci´on caracter´ıstica)
• r1 = r2 = 2 (soluciones de la ecuaci´on caracter´ıstica)
• an = A12n + A22nn,∀n≥ 0
• Calculamos A1 y A2 a partir de las condiciones iniciales:
•
 a0 = 7 a1 = 8 ⇔  A120 + A220 · 0 = 7 A121 + A221 · 1 = 8 ⇔  A1 = 7 2A1 + 2A2 = 8 ⇔  A1 = 7 A2 = −3
• Soluci´on:



an = 7 · 2n− 3n· 2n,∀n≥ 0
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 18 / 41

<!-- página 19 -->

Actividad 6
Resolver a0 = 2;a1 = 9;an + 6an−1 + 9an−2 = 0,∀n≥ 2
1 Determinar los primeros cinco t´erminos de la sucesi´on que genera.
2 Resolver dicha RR para calcular a10
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 19 / 41

<!-- página 20 -->

CASO 3
Para r1 y r2 complejas conjugadas:
an = A1|z|n cos(nθ) + A2|z|n sen(nθ),∀n≥ 0
Con |z| = |r1| = |r2| y θ el argumento de r1 ´o r2, en su forma polar.
Adem´as, las constantes A1 y A2 depender´an de las condiciones iniciales.
Ejemplo 12:
Resolver a0 = 3;a1 = −2;an− 2an−1 + 2an−2 = 0,∀n≥ 2
• r2 − 2r + 2 = 0 (ecuaci´on caracter´ıstica)
• r1 = 1 + i y r2 = 1 −i (soluciones de la ecuaci´on caracter´ıstica)
•|z| = |1 + i| = √ 2 y θ = 45o = π 4
• an = A1
√
2
n
cos(πn 4 ) + A2 √ 2 n sen(πn 4 ),∀n≥ 0
• Calculamos A1 y A2 a partir de las condiciones iniciales:
•
 a0 = 3 a1 = −2 ⇔  A1 √ 2 0 cos( 0 4 ) + A2 √ 2 0 sen( 0 4 ) = 3 A1 √ 2 1 cos(π 4 ) + A2 √ 2 1 sen(π 4 ) = −2 ⇔  A1 = 3 A2 = −5
• Soluci´on:



an = 3
√
2
n
cos
πn
4

− 5
√
2
n
sen
πn
4

,∀n≥ 0
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 20 / 41

<!-- página 21 -->

Actividad 7
Resolver a0 = 4;a1 = 15;an + 9an−2 = 0,∀n≥ 2
1 Determinar los primeros cinco t´erminos de la sucesi´on que genera.
2 Resolver dicha RR para calcular a10
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 21 / 41

<!-- página 22 -->

LA SUCESI ´ON DE LOS N ´UMEROS DE FIBONACCI
Esta sucesi´on hace referencia a la secuencia ordenada de n ´umeros des-
crita por Leonardo de Pisa, matem´atico italiano del siglo XIII:
0,1,1,2,3,5,8,13,21,34,55,89,144,...
Esta sucesi´on fue descrita por Fibonacci como la soluci´on a un problema de cr´ıa de conejos: “Cier-
to hombre tiene una pareja de conejos juntos en un lugar cerrado y desea saber cu´antos son creados a
partir de este par en un a˜no cuando, de acuerdo a su naturaleza, cada pareja necesita un mes para enve-
jecer y cada mes posterior procrea otra pareja” (Laurence Sigler, Fibonacci’s Liber Abaci)
La respuesta a esta pregunta es la que sigue:
• Partimos de una pareja de conejos el primer mes. (F1 = 1)
• Durante el segundo mes la pareja envejece pero no procrea. (F2 = 1)
• El tercer mes la pareja procrea otra pareja (es decir, ya tenemos dos parejas). (F3 = 2)
• El cuarto mes, la primera pareja vuelve a procrear y la pareja nueva envejece sin procrear
(luego tenemos tres parejas). (F4 = 3)
• El quinto mes, las dos parejas m´as viejas vuelven a procrear mientras que la nueva pareja
no procrea (cinco parejas en total). (F5 = 5)
• . . .
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 22 / 41

<!-- página 23 -->

Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 23 / 41

<!-- página 24 -->

Los n´umeros de Fibonacci pueden definirse recursivamente, mediante
una relaci´on de recurrencia lineal de segundo orden homog´enea: F0 = 0; F1 = 1; Fn = Fn−1 + Fn−2,∀n≥ 2
Resolvamos dicha RR:
• r2 −r− 1 = 0 (ecuaci´on caracter´ıstica)
• r1 = 1+
√
5
2 ; r2 = 1−
√
5
2 (soluciones de la ecuaci´on caracter´ıstica)
• Fn = A1

1+
√
5
2
n
+ A2

1−
√
5
2
n
• Calculamos A1 y A2 a partir de las condiciones iniciales:  0 = A1  1+ √ 5 2 0 + A2  1− √ 5 2 0 1 = A1  1+ √ 5 2 1 + A2  1− √ 5 2 1 ⇔  0 = A1 + A2 2 = A1  1 + √ 5  + A2  1 − √ 5  (*) ⇔  A1 = 1√ 5 A2 = −1√ 5
• Soluci´on:



Fn = 1√ 5

1+
√
5
2
n
− 1√ 5

1−
√
5
2
n
∀n≥ 0
(∗): Aplicar propiedad distributiva en la segunda ecuaci´on, y utilizar A1 + A2 = 0
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 24 / 41

<!-- página 25 -->

Una sucesi´on estrechamente relacionada con los n ´umeros de Fibonacci
es la de los n´umeros de Lucas, la cual se define:
 L0 = 2; L1 = 1; Ln = Ln−1 + Ln−2,∀n≥ 2
2,1,3,4,7,11,18,29,47,76,123,199,322,...
Actividad 8
Hallar la soluci´on para esta RR, tendiendo en cuenta que tiene simili-
tudes con la de los n ´umeros de Fibonacci.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 25 / 41

<!-- página 26 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 10, secci´on
10.2 del libro Matem´atica Discreta de Ralph Grimaldi que se encuentra
en el campus virtual.
• 1 (a, b, c, f)
• 3, 4, 6 (a), 8 (a), 9, 11, 13
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 26 / 41

<!-- página 27 -->

RELACIONES DE RECURRENCIA LINEALES NO HOMOG ´ENEAS
Recordemos que
Una relaci ´on de recurrencia de orden k es de la forma:
an = α1an−1 + α2an−2 + ··· + αkan−k + g(n),∀n≥k
Si g(n) ≡ 0, la relaci´on de recurrencia lineal se denomina homog´enea;
caso contrario, se llamar´a no homog´enea.
Trabajaremos en esta secci´on con g(n) . 0.
El m´etodo que utilizaremos para resolver dichas RR No Homog´eneas
recibe el nombre de m´etodo de coeficientes indeterminados. Consiste en
descomponer la soluci´on como suma de la soluci´on de la RR Homog´enea
asociada (es decir para g(n) ≡ 0) y una soluci´on particular de la RR No
Homog´enea dada. Es decir:
an = a(h) n + a(p) n
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 27 / 41

<!-- página 28 -->

La soluci´on particular de la RR No Homog´enea depender´a de la familia
de funciones a la que pertenece g(n) dada.
La siguiente tabla muestra que cuando g(n) sea de la familia de funcio-
nes que indica la primera columna, la soluci´on particular que se debe
tomar es la asociada en la segunda columna.
g(n) a(p) n
Polin´omica de grado t
c, cte A, una constante
n A1n + A0, polinomio completo de grado 1
n2 A2n2 + A1n + A0, polinomio completo de grado 2
n3 A3n3 + A2n2 + A1n + A0, polinomio completo de grado 3
nt polinomio completo de grado t
Exponencial de base r
rn Arn, una constante por la misma exponencial
Trigonom´etricas
sen(θn) A1 sen(θn) + A2 cos(θn)
cos(θn) A1 sen(θn) + A2 cos(θn)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 28 / 41

<!-- página 29 -->

Para combinaciones de las funciones presentadas se sigue el mismo ra-
zonamiento.Veamos algunos ejemplos:
g(n) =3n2 + 1 a(p) n = A2n2 + A1n + A0
g(n) =3n· 5n a(p) n = (A1n + A0) · 5n
g(n) =3n + 5n a(p) n = A1n + A0 + A5n
g(n) =7n sen(θn) a(p) n = 7n[A1 sen(θn) + A2 cos(θn)]
g(n) =(−3)n cos(θn) a(p) n = (−3)n[A1 sen(θn) + A2 cos(θn)]
En los siguientes tres ejemplos veremos situaciones donde la soluci´on
particular propuesta es un m ´ultiplo constante de un t´ermino de solu-
ci´on de la RR homog´enea asociada. En estos casos se propone multi-
plicar la primera por n (o alguna potencia de n, seg ´un se requira) para
evitarlo.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 29 / 41

<!-- página 30 -->

Ejemplo 13
Sea an+2 − 10an+1 + 21an = g(n),∀n≥ 0, con a0 y a1 dados:
• La soluci´on de la RR homog´enea asociada es:


a(h) n = C13n + C27n
Es claro que las constantes C1 y C2 no pueden ser halladas en este
paso, ya que las condiciones iniciales son de la RR dada, y no de la
homog´enea asociada. Por lo que se calcular´an al final.
• En la siguiente lista, se presentan algunas funciones y sus respec-
tivas soluciones particulares que se deben plantear:
g(n) =5n2 − 3n + 7 a(p) n = A2n2 + A1n + A0
g(n) =3 · 11n a(p) n = A· 11n
g(n) =5 · 7n a(p) n = An· 5n
g(n) =8 · 5n− 4 · 3n a(p) n = A1 · 5n + A2n· 3n
g(n) =8 · 7n− 4 · 3n a(p) n = A1n· 7n + A2n· 3n
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 30 / 41

<!-- página 31 -->

Ejemplo 14
Sea an+2 − 4an+1 + 3an = g(n), ∀n≥ 0, con a0 y a1 dados. La soluci´on de
la RR homog´enea asociada es:



a(h) n = C13n + C21n = C13n + C2
Como vemos, el segundo t´ermino resulta una constante no nula (en
principio), es decir, un polinomio de grado 1. Entonces, si
g(n) =11 a(p) n = An
g(n) =5n2 − 3n + 7 a(p) n = A2n3 + A1n2 + A0n
g(n) =3 · 11n a(p) n = A· 11n
g(n) =5 · 3n a(p) n = An· 3n
g(n) =8 · 5n− 4 a(p) n = A1 · 5n + A2n
g(n) =8 · 3n− 4 a(p) n = A1n· 3n + A2n
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 31 / 41

<!-- página 32 -->

Ejemplo 15
Sea an+2 − 4an+1 + 4an = g(n), ∀n≥ 0, con a0 y a1 dados. La soluci´on de
la RR homog´enea asociada es:



a(h) n = A12n + A2n2n
Entonces, si
g(n) =2 · 11n a(p) n = A· 11n
g(n) =5 · 2n a(p) n = A· 2nn2
Una vez propuesta la soluci´on particular, se prosigue calculando sus
constantes al sustituirla en la RR dada, ya que al ser una soluci´on par-
ticular, verificar´a dicha ecuaci´on.
Luego se plantea la soluci´on general: an = a(h) n + a(p) n , y a partir de las
condiciones iniciales se calculan las constantes que restan hallar.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 32 / 41

<!-- página 33 -->

Actividad 9
Resolver
 2an + an−1 = 5 · 7n,∀n≥ 1 a0 = 2
Tener en cuenta que la RRH asociada se trabaj´o en la actividad 3.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 33 / 41

<!-- página 34 -->

Actividad 10
Resolver
 2an + an−1 = 5 ·  − 1 2 n ,∀n≥ 1 a0 = 3
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 34 / 41

<!-- página 35 -->

Actividad 11
Resolver
 a0 = 1;a1 = 4; an− 6an−1 + 5an−2 = 2 · 3n,∀n≥ 2
Tener en cuenta que la RRH asociada se trabaj´o en la actividad 5.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 35 / 41

<!-- página 36 -->

Actividad 12
Resolver
 a0 = 1 2 ;a1 = 1; an− 6an−1 + 5an−2 = −8n,∀n≥ 2
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 36 / 41

<!-- página 37 -->

Actividad 13
Resolver
 a0 = 1 2 ;a1 = 1; an− 6an−1 + 5an−2 = 2 · 5n,∀n≥ 2
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 37 / 41

<!-- página 38 -->

LAS TORRES DE HANOI
´Edouard Lucas, (1842-1891) fue un reconocido matem´atico franc´es. En
1883 public´o el juego de “La Torre de Hanoi” bajo el pseud´onimo de
Profesor N. Claus de Siam.
El juego de las Torres de Han´oi es un dispositivo que consta de tres
varillas verticales A, B y C y un n ´umero variable de discos. Los n discos
son todos de diferente tama˜no y, en la posici´on de partida del juego,
todos los discos est´an colocados en la varilla A ordenados de mayor a
menor tama˜no. El juego consiste en pasar todos los discos a la tercera
varilla coloc´andolos en el mismo orden.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 38 / 41

<!-- página 39 -->

Reglas
• Solo se puede mover un disco cada vez.
• Un disco de mayor tama˜no no puede descansar sobre uno m´as pe-
que˜no que ´el mismo.
• Solo se puede desplazar el disco que se encuentra arriba de cada
varilla.
Veamos el caso para 3 discos
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 39 / 41

<!-- página 40 -->

Problema
¿Cu´al es la menor cantidad de movimientos que se requieren para hacerlo?
La respuesta viene a partir de un algoritmo recursivo.
Si tenemos n discos, llamaremos an al m´ınimo n ´umero de movimientos
necesario para transportar los n discos desde una varilla a otra. As´ı,
para mover n + 1 discos hacemos:
• Pasamos los n discos de arriba, de la varilla 1 a la 2, con las indica-
ciones dadas. Esto se realiza en an pasos.
• Pasamos el disco m´as grande de la varilla 1 a la 3. Esto se hace en
un paso.
• Por ´ultimo, pasamos los n discos de la varilla 2 a la 3, donde ya est´a
el de mayor tama˜no. Esto requiere otros an moviemientos.
De esta manera, la relaci´on que se establece es:



an = 2an−1 + 1,∀n≥ 0 con a0 = 0
y su soluci´on es an = 2n− 1 ∀n≥ 0
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 40 / 41

<!-- página 41 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 10, secci´on
10.3 del libro Matem´atica Discreta de Ralph Grimaldi que se encuentra
en el campus virtual.
• 1 (a, b, c, d)
• 5 (a, b)
• 3 (a), 4, 6 y 9
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 41 / 41
