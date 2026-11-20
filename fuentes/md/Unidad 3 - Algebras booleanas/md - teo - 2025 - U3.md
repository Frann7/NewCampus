# md - teo - 2025 - U3

Fuente: `C:/Users/Administrator/Downloads/MATDISCRETA/Catedra/Unidad 3 - Algebras booleanas/md - teo - 2025 - U3.pdf` · 29 página(s) · texto extraído con pypdf.
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
| 20 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 21 |  |
| 22 |  |
| 23 |  |
| 24 |  |
| 25 |  |
| 26 |  |
| 27 |  |
| 28 |  |
| 29 |  |

<!-- página 1 -->

Matem´atica Discreta
Licenciatura en Sistemas de Informaci´on
Docentes
Vaira, Stella - Fedonczuk, Miguel
Colliard, David - Cottonaro, Mariana - Froloff, B´arbara
FCyT - UADER
2025

<!-- página 2 -->

Unidad 3: ´Algebras booleanas.
Introducci´on. Definici´on: operaciones, propiedades. Ejemplos. Aplica-
ciones: redes l´ogicas.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 2 / 1

<!-- página 3 -->

GEORGE BOOLE
• Naci´o en Lincoln (Inglaterra) en 1815
• A pesar de provenir de una familia humilde, Boole fue pr´actica-
mente autodidacta en matem´aticas y lenguas. Aprendi´o lat´ın, grie-
go, franc´es y alem´an por su cuenta.
• Comenz´o a trabajar como maestro a los 16 a˜nos. En 1834, abri´o su
propia escuela en Lincoln.
• 1847: Publica “The Mathematical Analysis of Logic”, introducien-
do las ideas b´asicas del ´algebra booleana.
• 1849: Fue nombrado primer profesor de matem´aticas en el Queen’s
College Cork (ahora University College Cork), en Irlanda.
• 1854: Publica “An Investigation of the Laws of Thought”, su obra
m´as influyente, donde desarrolla completamente el sistema l´ogico
que lleva su nombre.
Su legado
El ´algebra booleana es la base del dise˜no de circuitos digitales y siste-
mas de l´ogica computacional. Su trabajo es un pilar
fundamental de la inform´atica moderna y la l´ogica matem´atica.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 3 / 1

<!-- página 4 -->

CLAUDE SHANNON
Claude Shannon fue un matem´atico, ingeniero el´ectrico y cript´ografo estadou-
nidense que se considera el “padre de la teor´ıa de la informaci´on”.
• En 1937, tesis de maestr´ıa en el MIT: “A Symbolic Analysis of Relay and
Switching Circuits”. Conecta los principios de ´algebra booleana con la
teor´ıa de circuitos el´ectricos. Base de la l´ogica digital moderna.
• Durante la Segunda Guerra Mundial, hizo avances claves en Criptograf´ıa.
En 1948, publica “A Mathematical Theory of Communication”. Con ello,
sent´o las bases para la seguridad moderna de las comunicaciones. Fue el
primero en formalizar y analizar la seguridad de los sistemas de cifrado
y propuso el uso de un “cifrado de clave secreta”.
• En los a˜nos 50, Shannon desarroll´o un concepto clave para la inteligen-
cia artificial: el “juego de ajedrez”. Cre´o uno de los primeros programas
de ajedrez en una computadora, estudi´o los aut´omatas y los sistemas que
pod´ıan imitar el razonamiento humano, sentando las bases para los futu-
ros desarrollos de la inteligencia artificial.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 4 / 1

<!-- página 5 -->

Conjunto de partes
Dado el conjunto S, podemos enumerar todos los subconjuntos posi-
bles de S, o dicho de otro modo todos los conjuntos incluidos en S.
Construimos entonces un nuevo conjunto con todos esos conjuntos co-
mo elementos, este nuevo conjunto se llama conjunto de partes de S y se
indica con P (S).
Para S = {a}
P (S) = {∅, S}
Para S = {a, b}
P (S) = {∅, {a}, {b}, S}
Para S = {a, b, c}
P (S) = {∅, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, S}
Notemos que todos los elementos de P (S) se escriben entre llaves por-
que son conjuntos, salvo el conjunto vac´ıo que se escribe sin llaves.
Por ejemplo para S = {a, b, c}: {a, b}∈ P (S).
En general, si S tiene n elementos, ¿De cu´antos elementos consta P (S)?
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 5 / 1

<!-- página 6 -->

´Algebra de Boole de conjuntos
Sea S un conjunto, entonces (P (S), ∪, ∩, c, ∅, S) es un ´Algebra de Boole.
Posee un primer elemento ∅ y un ´ultimo elemento S. Existe una rela-
ci´on de orden que se establece entre sus elementos, que en este caso es
la inclusi´on. La misma constituye una relaci´on de orden parcial. ¿Por qu´e?
Esta relaci´on entre sus elementos puede representarse mediante un
Diagrama de Hasse:
{a}
∅
{a, b}
{a} {b}
∅
{a, b, c}
{a, b} {a, c} {b, c}
{a} {b} {c}
∅
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 6 / 1

<!-- página 7 -->

Actividad 1
a Listar los elementos de P (S) para S = {a, b, c, d}.
b Establecer una relaci´on de sus elementos con el sistema binario.
c Analizar c´omo es su diagrama de Hasse.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 7 / 1

<!-- página 8 -->

Relaci ´on de divisibilidad entre dos n ´umeros naturales
Si x y y son n ´umeros naturales, diremos que “x divide a y”, y se denota
x|y, si y s´olo si existe un n ´umero natural k tal que y = kx.
Diremos “x es un divisor(factor) de y”, “y es un m ´ultiplo de x” o “y es
divisible por x”
Por ejemplo:
5|15 porque 15 = 5 · 3, y por lo cual 3|15
1|14 porque 14 = 1 · 14, y tambi´en 14|14
Con D(n), denotamos al conjunto de divisores de n ∈ N.
Ejemplo: D(10) = {1, 2, 5, 10}
N ´umero natural libre de cuadrados
Un n ´umero natural se dice libre de cuadrados, si ning ´un cuadrado mayor
a 1 lo divide.
Por ejemplo: 30 es libre de cuadrados, pero 75 no lo es.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 8 / 1

<!-- página 9 -->

´Algebra de Boole de los divisores de n
Sea n un n ´umero natural libre de cuadrados, entonces (D(n), ∨, ∧, ∽, 1, n)
es un ´Algebra de Boole.
Posee un primer elemento 1 y un ´ultimo elemento n. La relaci´on de or-
den que se establece entre sus elementos es la divisibilidad. La misma
constituye una relaci´on de orden parcial. ¿Por qu´e?
En toda ´Algebra de Boole intervienen dos operaciones binarias y una
unaria (pensar en el ejemplo anterior cu´ales son). En este caso, para dos
elementos x e y:
• x ∨ y = mcm(x, y)
• x ∧ y = mcd(x, y)
• ∽ x = cociente(n, x)
(se lee “vilella x”)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 9 / 1

<!-- página 10 -->

Ejemplo 1
Sea n = 30, D(30) = {1, 2, 3, 5, 6, 10, 15, 30}
Para x = 6 e y = 10:
• x ∨ y = mcm(6, 10) = 30
• x ∧ y = mcd(6, 10) = 2
• ∽ x = cociente(30, 6) = 5
30
6 10 15
2 3 5
1
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 10 / 1

<!-- página 11 -->

Todo ´Algebra de Boole verifica las siguientes propiedades.
Sean A, B y C elementos de P (S), podemos expresar dichas propiedades
en t´erminos de los dos ejemplos anteriores:
1. Ley del doble complemento
(Ac)c = A ∽ (∽ x) = x
2. Leyes de De Morgan
(A ∪ B)c = Bc ∩ Ac ∽ (x ∨ y) =∽ x∧ ∽ y
(A ∩ B)c = Bc ∪ Ac ∽ (x ∧ y) =∽ x∨ ∽ y
3. Leyes conmutativas
A ∪ B = B ∪ A x ∨ y = y ∨ x
A ∩ B = B ∩ A x ∧ y = y ∧ x
4. Leyes asociativas
A ∪ (B ∪ C) = (A ∪ B) ∪ C x ∨ (y ∨ z) = (x ∨ y) ∨ z
A ∩ (B ∩ C) = (A ∩ B) ∪ C x ∧ (y ∧ z) = (x ∧ y) ∧ z
5. Leyes distributivas
A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)
A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z)

<!-- página 12 -->

6. Leyes de idempotencia
A ∪ A = A x ∨ x = x
A ∩ A = A x ∧ x = x
7. Leyes de identidad
A ∪ ∅ = A x ∨ 1 = x
A ∩ S = A x ∧ n = x
8. Leyes de los inversos
A ∪ Ac = S x∨ ∽ x = n
A ∩ Ac = ∅ x∧ ∽ x = 1
9. Leyes de dominaci ´on
A ∪ S = S x ∨ n = n
A ∩ ∅ = ∅ x ∧ 1 = 1
10. Leyes de absorci ´on
A ∪ (A ∩ B) = A x ∨ (x ∧ y) = x
A ∩ (A ∪ B) = A x ∧ (x ∨ y) = x
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 12 / 1

<!-- página 13 -->

´Algebra de los interruptores
Supongamos que los valores de entrada 1, 0 corresponden respectiva-
mente a las posiciones ON y OFF de los interruptores de un circuito
mientras que los valores 1, 0 del interior representan la salida o no de
corriente.
Entonces + representa un circuito con dos interruptores en paralelo y ·
representa un circuito con dos interruptores en serie, x e y variables o
estados que pueden tomar valores 1 (ON, pasa corriente) ´o 0 (OFF, no
pasa corriente):
x y
Circuito en serie x · y = xy
x
y Circuito en paralelo x + y
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 13 / 1

<!-- página 14 -->

Funciones de conmutaci ´on
Un interruptor el´ectrico puede encenderse (pasa la corriente) o apagar-
se (no pasa la corriente). De esta manera, como todo dispositivo de dos
estados, se relaciona con la l´ogica de dos valores de verdad.
En programaci´on, los valores booleanos 1 y 0 son aquellos que repre-
sentan un estado true (verdadero) o false (falso), respectivamente.
Sea B = {0, 1}, el conjunto de valores booleanos, definimos en dicho con-
junto la suma, multiplicaci´on y complemento:
1 0 + 0 = 0; 0 + 1 = 1; 1 + 0 = 1; 1 + 1 = 1
2 0 · 0 = 0; 0 · 1 = 0; 1 · 0 = 0; 1 · 1 = 1
3 ¯0 = 1; ¯1 = 0
Una variable x es una variable booleana si x toma valores de B.
Observaciones:
1 x + x = x ; x · x = x (Propiedades de idempotencia)
2 x + y = 0 ⇔ x = y = 0
3 x · y = 1 ⇔ x = y = 1
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 14 / 1

<!-- página 15 -->

Funciones booleanas
Sea n ∈ Z+, Bn = {(b1, b2, . . . , bn) /bi ∈{0, 1}, ∀i}. Es decir, Bn est´a formado
por las n-uplas de componentes 0 o 1.
Una funci´on f : Bn → B es una funci´on funci´on booleana, tambi´en lla-
mada funci´on de conmutaci´on.
En general, ¿cu´antas filas posee una tabla de f : Bn → B?
Ejemplo 2
f : B3 → B definida por f (x, y, z) = xy + z
x y z f (x, y, z) = xy + z
0 0 0 0 · 0 + 0 = 0
0 0 1 0 · 0 + 1 = 1
0 1 0 0 · 1 + 0 = 0
0 1 1 0 · 1 + 1 = 1
1 0 0 1 · 0 + 0 = 0
1 0 1 1 · 0 + 1 = 1
1 1 0 1 · 1 + 0 = 1
1 1 1 1 · 1 + 1 = 1
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 15 / 1

<!-- página 16 -->

Actividad 2
Completar la tabla con el recorrido de las siguientes funciones:
x y z h(x, y, z) = x + z m(x, y, z) = xy ¯z
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
Actividad 3
Construir la tabla para la funci´on booleana j(x, y) = xy + ¯x.
Actividad 4
Analizar c´omo est´a conformada cada tabla de las funciones
f1(x, y, z) = 1 y f0(x, y, z, w) = 0.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 16 / 1

<!-- página 17 -->

Igualdad entre funciones booleanas
Para n ∈ Z+, n ≥ 2, sean f , g : Bn → B dos funciones booleanas de n
variables booleanas x1, x2, . . . , xn. Decimos que f y g son iguales (es-
cribimos f = g) si las columnas para f y g (en sus respectivas tablas de
funci´on) para las mismas entradas (x1, x2, . . . , xn) son exactamente las
mismas.
Actividad 5
Probar que f (x, y, z) = xy + z y g(x, y, z) = ( ¯x + ¯y)¯z son iguales.
x y z f (x, y, z) g(x, y, z)
0 0 0 0
0 0 1 1
0 1 0 0
0 1 1 1
1 0 0 0
1 0 1 1
1 1 0 1
1 1 1 1
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 17 / 1

<!-- página 18 -->

Funciones booleanas complementarias
Para n ∈ Z+, n ≥ 2, sean f : Bn → B un funci´on booleana, entonces el
complemento de f , que se denota ¯f , es la funci´on booleana definida
sobre Bn como:
¯f (x1, x2, . . . , xn) = f (x1, x2, . . . , xn)
Ejemplo 3
x y z f (x, y, z) = xy + z ¯f (x, y, z) = xy + z
0 0 0 0
0 0 1 1
0 1 0 0
0 1 1 1
1 0 0 0
1 0 1 1
1 1 0 1
1 1 1 1
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 18 / 1

<!-- página 19 -->

Adici´on y multiplicaci´on de funciones booleanas
Para n ∈ Z+, n ≥ 2, sean f , g : Bn → B dos funciones booleanas de n
variables booleanas x1, x2, . . . , xn. Definimos la adici´on y multiplicaci´on
entre funciones booleanas como:
• (f + g)(x1, x2, . . . , xn) = f (x1, x2, . . . , xn) + g(x1, x2, . . . , xn)
• (f · g)(x1, x2, . . . , xn) = f (x1, x2, . . . , xn) · g(x1, x2, . . . , xn)
De esta manera hemos definido tres operaciones:
complemento (unaria), adici´on y multiplicaci´on (binarias).
En la siguiente tabla se establecen las Leyes que verifican las funciones
booleanas, como consecuencia de sus operaciones definidas.
Observar que en cada ley numerada, aparece una propiedad (s) y su
dual (sd ), que surge de intercambiar las operaciones.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 19 / 1

<!-- página 20 -->



<!-- página 21 -->

Las leyes de las funciones booleanas nos permiten simplificar (o expan-
dir) expresiones booleanas. Como por ejemplo:
xy + (x + y)¯z + y L5= xy + x ¯z + y ¯z + y L10= y + x ¯z
L5: Leyes distributivas
L10: Leyes de absorci´on
Tambi´en nos permiten representar una adici´on como una multiplica-
ci´on, y viceversa. Como por ejemplo:
y + x ¯z L5= (y + x)(y + ¯z)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 21 / 1

<!-- página 22 -->

Forma Normal Disyuntiva (fnd)
Para n ∈ Z+, si f : Bn → B es una funci´on booleana sobre las n variables
booleanas x1, x2, . . . , xn, entonces:
1 Cada xi , o su complemento ¯xi , es un literal.
2 Una expresi´on de la forma y1y2 ··· yn donde yi = xi o yi = ¯xi , es una
conjunci´on fundamental.
3 Una representaci´on de f como una adici´on de conjunciones fun-
damentales es una forma normal disyuntiva (fnd) de la funci´on
booleana.
Observaci´on: La fnd de toda funci´on booleana, en su expresi´on m´as
simple, es ´unica.
Ejemplo 4
• f (x, y, z) = xyz + yz + z no est´a expresada en su fnd, no posee con-
junciones fundamentales en todos sus t´erminos.
• g(x, y, z) = xyz + ¯xy ¯z est´a en su fnd, cada t´ermino posee los tres
literales.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 22 / 1

<!-- página 23 -->

Toda funci´on booleana puede expresarse como una ADICI ´ON DE CON-
JUNCIONES FUNDAMENTALES, y la misma, tiene su representaci´on
como una ADICI ´ON DE MINT ´ERMINOS.
Ejemplo 5
f (x, y, z) = xy + yz
= xy1 + 1yz
= xy(z + ¯z) + (x + ¯x)yz
= xyz + xy ¯z + xyz + ¯xyz
f (x, y, z) = xyz + xy ¯z + ¯xyz (f nd)
et x y z f conj.f . et
0 0 0 0 0
1 0 0 1 0
2 0 1 0 0
3 0 1 1 1 ¯xyz 3
4 1 0 0 0
5 1 0 1 0
6 1 1 0 1 xy ¯z 6
7 1 1 1 1 xyz 7
f (x, y, z) = xyz + xy ¯z + ¯xyz =
X
m(3, 6, 7)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 23 / 1

<!-- página 24 -->

Forma Normal Conjuntiva (fnc)
Para n ∈ Z+, si f : Bn → B es una funci´on booleana sobre las n variables
booleanas x1, x2, . . . , xn, entonces:
1 Cada xi , o su complemento ¯xi , es un literal.
2 Una expresi´on de la forma (y1 + y2 + ··· + yn) donde yi = xi o yi = ¯xi ,
es una disyunci´on fundamental.
3 Una representaci´on de f como una multiplicaci´on de disyunciones
fundamentales es una forma normal conjuntiva (fnc) de la funci´on
booleana.
Observaci´on: La fnc de toda funci´on booleana, en su expresi´on m´as sim-
ple, es ´unica.
Ejemplo 6
• f (x, y, z) = (x + y)(x + ¯y + z) no est´a expresada en su fnc, no posee
disyunciones fundamentales en todos sus factores.
• g(x, y, z) = (x + y + z)(x + ¯y + ¯z) est´a en su fnc, cada factor posee los
tres literales.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 24 / 1

<!-- página 25 -->

Problema dual: fnd ←→ fnc
• conjunciones fundamentales ←→ disyunciones fundamentales
(xyz) ←→ (x + y + z)
• buscamos c.f. tales que f=1 ←→ buscamos d.f. tales que f=0
• forma normal disyuntiva ←→ forma normal conjuntiva
• adici´on de mint´erminos ←→ multiplicaci´on de maxt´erminos
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 25 / 1

<!-- página 26 -->

Expresi´on de una funci´on booleana como una MULTIPLICACI ´ON DE
DISYUNCIONES FUNDAMENTALES y una MULTIPLICACI ´ON DE
MAXT ´ERMINOS.
Ejemplo 7
f (x, y, z) = xy + yz = y(x + z)
= ((y + 0) + 0)(x + z + 0)
= ((y + x · ¯x) + z · ¯z)((x + z) + y · ¯y)
= (y + x · ¯x + z)(y + x ¯x + ¯z)(x + z + y)(x + z + ¯y)
= (y + x + z)(y + ¯x + z)(y + x + ¯z)(y + ¯x + ¯z)(x + z + y)(x + z + ¯y)
= (x + y + z)( ¯x + y + z)(x + y + ¯z)( ¯x + y + ¯z)(x + ¯y + z)
f (x, y, z) = (x + y + z)( ¯x + y + z)(x + y + ¯z)( ¯x + y + ¯z)(x + ¯y + z)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 26 / 1

<!-- página 27 -->

et x y z f disy.f . et
0 0 0 0 0 x + y + z 0
1 0 0 1 0 x + y + ¯z 1
2 0 1 0 0 x + ¯y + z 2
3 0 1 1 1
4 1 0 0 0 ¯x + y + z 4
5 1 0 1 0 ¯x + y + ¯z 5
6 1 1 0 1
7 1 1 1 1
f (x, y, z) = (x + y + z)( ¯x + y + z)(x + y + ¯z)( ¯x + y + ¯z)(x + ¯y + z)
f (x, y, z) =
Y
M(0, 1, 2, 4, 5)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 27 / 1

<!-- página 28 -->

Actividad 6
Hallar la expresi´on m´as simple de cada una de las siguientes funciones:
• f (x, y, z) = P m(1, 3, 5, 7) • g(x, y, z) = Q M(4, 6, 7)
et x y z f conj.f . g disy.f .
0 0 0 0
1 0 0 1
2 0 1 0
3 0 1 1
4 1 0 0
5 1 0 1
6 1 1 0
7 1 1 1
• f (x, y, z) =
• g(x, y, z) =
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 28 / 1

<!-- página 29 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los ejercicios del 1 al 13 de la secci´on 15.1 (P´agina
743) del libro Matem´atica Discreta de Ralph Grimaldi que se encuentra
en el campus virtual.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 29 / 1
