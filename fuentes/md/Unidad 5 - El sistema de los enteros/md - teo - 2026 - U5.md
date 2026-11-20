# md - teo - 2026 - U5

Fuente: `C:/Users/Administrator/Downloads/MATDISCRETA/Catedra/Unidad 5 - El sistema de los enteros/md - teo - 2026 - U5.pdf` · 26 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Matem´atica Discreta
Licenciatura en Sistemas de Informaci´on
Docentes
Vaira, Stella - Fedonczuk, Miguel
Colliard, David - Cottonaro, Mariana - Froloff, B´arbara
FCyT - UADER
2026

<!-- página 2 -->

Unidad 5: El sistema de los Enteros.
Principio del buen orden. Principio de inducci´on matem´atica. Defini-
ciones recursivas. Algoritmo de la divisi´on. N ´umeros primos. M´axi-
mo com ´un divisor. Algoritmo de Euclides. Teorema fundamental de la
Aritm´etica. La funci´on φ de Euler.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 2 / 26

<!-- página 3 -->

ALGORITMO DE LA DIVISION: NUMEROS PRIMOS
Retomemos una relaci´on entre n ´umeros presentada cuando se abord´o
´Algebras de Boole, solo que ahora se definir´a para todo n ´umero entero
de la siguiente manera:
Definici´on
Si a,b∈ Z y b , 0, decimos que “b divide a a”, y lo denotamos b|a, si
existe un entero n tal que a = bn.
Cuando esto ocurre, decimos que b es un divisor de a, o que a es m ´ulti-
plo de b.
Notar que si bien esta relaci´on est´a ligada con la operaci´on divisi´on
dentro de Z, no son lo mismo.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 3 / 26

<!-- página 4 -->

La relaci´on de divisibilidad verifica las siguientes propiedades:
Para cualquier a,b,c,x,y,z∈ Z (siempre que el divisor no sea 0)
1 a|a
2 1|a (1 es divisor universal)
3 a|0
4 (a|b∧b|a) ⇒a = ±b
5 (a|b∧b|c) ⇒a|c
6 a|b⇒a|bx
Si a divide b, entonces a divide a cualquier m ´ultiplo de b
7 Si x = y + z y a divide a dos de x,y,z, entonces a divide al restante.
8 (a|b∧a|c) ⇒a|(bx + cy)
Si a divide a dos n ´umeros, divide a cualquier combinaci´on lineal
de ellos
Generalizaci´on: a|ci entonces a|(c1x1 + c2x2 + ... + cnxn)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 4 / 26

<!-- página 5 -->

Definici´on
Un n ´umero natural p mayor a 1 se dice primo si 1 y p son sus ´unicos
divisores positivos. Si un n ´umero natural n mayor a 1 no es primo, di-
remos que es compuesto.
Extensi´on a Z:
• p∈ Z es primo si tiene ex´actamente 4 divisores (1, −1, p y −p).
• n∈ Z con |n|> 1 es compuesto si no es primo.
• Los enteros 0, 1 y −1 quedan fuera de estas definiciones.
Si bien se extiende la definici´on a los enteros, salvo menci´on expresa,
nos referiremos de aqu´ı en m´as a primos positivos.
La sucesi´on de primos comienza con 2,3,5,7,11,13,17,19,23,29,... y
se puede probar que es infinita.
Proposici´on
Si n es compuesto, entonces existe un primo p tal que p|n.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 5 / 26

<!-- página 6 -->

Actividad 1
a Sea a> 1 y n un entero cualquiera, probar que si a|(3n−1) y a|(4n+9)
entonces a es un n ´umero primo.
b ¿Existen enteros x,y,z tales que 6x + 9y + 15z = 107?
c ∀a,b∈ Z, sea 2a+3b un m ´ultiplo de 17, demuestre que 17|(9a+5b).
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 6 / 26

<!-- página 7 -->

ALGORITMO DE LA DIVISION
Sean a,b∈ Z, b> 0, entonces existen ´unicos q,r∈ Z tales que
a = qb + r, con 0 ≤r<b
Al entero b se lo llama divisor, a es el dividendo, q el cociente y r resto.
En el caso de que r = 0 diremos que la divisi´on es exacta, y que b|a.
Actividad 2
Hallar el cociente y el resto de dividir a a por b
• a = 170 y b = 11
• a = 98 y b = 7
• a = −45 y b = 8
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 7 / 26

<!-- página 8 -->

Proposici´on
Si n∈ Z+ y n es compuesto, entonces existe un primo p tal que p|n y
p≤√n.
Esto constituye un criterio b´asico para evaluar si un n ´umero n es primo
o no, ya que si n NO es divisible por algunos de los primos menores
o iguales a su ra´ız cuadrada, entonces n NO es compuesto, es decir, es
primo.
Actividad 3
Evaluar la primalidad de 3553 y de 7919.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 8 / 26

<!-- página 9 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 4, apartado
4.3 (P´agina 213 ) del libro Matem´atica Discreta de Ralph Grimaldi que se
encuentra en el campus virtual: 2(a, b, c), 4, 5, 7, 8, 9, 10, 12, 13.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 9 / 26

<!-- página 10 -->

MAXIMO COMUN DIVISOR
Definici´on
Sean a,b∈ Z+ 0 , no ambos nulos simult´aneamente. Entonces d∈ Z+ es el
m´aximo com´un divisor de a y b, y se denota mcd(a,b) si:
• d|a, d|b
• para cualquier divisor c de a y b, entonces c|d
En otras palabras mcd(a,b) es el mayor de sus divisores positivos comu-
nes. Es decir,
mcd(a,b) = max{D+(a) ∩D+(b)}
Ejemplo 1
Hallamos mcd(120,84) analizando los conjuntos D+(120) y D+(84):
D+(120) = {1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120}
D+(84) = {1,2,3,4,6,7,12,14,21,28,42,84}
D+(a) ∩D+(b) = {1,2,3,4,6,12}
mcd(a,b) = max{D+(a) ∩D+(b)} = 12
Observar que el m´etodo no es pr´actico.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 10 / 26

<!-- página 11 -->

Proposici´on
El m´aximo com ´un divisor entre dos n ´umeros es ´unico
Esta proposici´on nos asegura que utilizando cualquier m´etodo para ha-
llar el m´aximo com ´un divisor, arribaremos a un ´unico resultado.
Definici´on
Se dice que a,b son primos relativos (o coprimos) si mcd(a,b) = 1.
As´ı
• 15 y 33 no son coprimos porque mcd(15,33) = 3
• 15 y 22 son coprimos porque mcd(15,22) = 1
Actividad 4
Para cualquier n∈ Z+, demostrar que los enteros 8n + 3 y 5n + 2 son
primos relativos.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 11 / 26

<!-- página 12 -->

Propiedades y extensi´on a todos los enteros:
• mcd(0,0) no est´a definido
• mcd(a,a) = |a|
• mcd(a,b) = mcd(b,a)
• mcd(a,1) = 1
• mcd(a,0) = |a|
• mcd(a,b) = mcd(|a|,|b|)
• mcd(a,b) = mcd(a−b,b)
Esta ´ultima propiedad constituye un m´etodo para hallar el mcd(a,b).
Actividad 5
a Verificar, utilizando la propiedad anterior, que mcd(120,84) = 12
b Probar que dos n ´umeros enteros consecutivos son coprimos.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 12 / 26

<!-- página 13 -->

Proposici´on
Si d = mcd(a,b), entonces existen enteros x e y tales que d = ax + by. Es
decir, el mcd(a,b) siempre se puede escribir como combinaci´on lineal
de a y b. Adem´as, el mcd(a,b) es la menor combinaci´on lineal positiva
de a y b.
Ejemplo 2
mcd(14,25) = 1 = (9)·14+(−5)·25 = (34)·14+(−19)·25 = (59)·14+(−33)·25
mcd(15,33) = 3 = (−2) · 15 + 1 · 33 = (9) · 15 + (−4) · 33 = (20) · 15 + (−9) · 33
Claramente, la combinaci´on lineal no es ´unica.
Al elegir una combinaci´on lineal cualquiera entre 15 y 33, el resultado
ser´a el mcd o alg ´un m ´ultiplo de ´el, pero la menor combinaci´on lineal
positiva es el mcd.
• (−1) · 15 + (15) · 33 = 480
• (−2) · 15 + (14) · 33 = 432
• (−3) · 15 + (−4) · 33 = −177
• (7) · 15 + (73) · 33 = 2514
• (2) · 15 + (−1) · 33 = −3
• (−33) · 15 + (15) · 33 = 0
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 13 / 26

<!-- página 14 -->

Algoritmo de Euclides y el m´aximo com ´un divisor
Proposici´on
Sean a y b n ´umeros enteros, a , 0 y sea r, el resto de dividir a a por b;
entonces mcd(a,b) = mcd(b,r).
Esta proposici´on es muy importante, ya que si el algoritmo se repite
hasta obtener una divisi´on exacta ...
a =bq1 + r1
b =r1q2 + r2
r1 =r2q3 + r3
...
rn−2 =rn−1qn + rn
rn−1 =rnqn+1 + 0,
entonces mcd(a,b) = mcd(b,r1) = mcd(r1,r2) = ··· = mcd(rn,0) = rn.
El m´aximo com ´un divisor es el ´ultimo resto no nulo de la
sucesi´on de restos en este algoritmo.
Proposici´on
Sean a y b n ´umeros enteros, a , 0 y sea r = rb(a); entonces (a : b) = (b : r).
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 14 / 26

<!-- página 15 -->

Actividad 6
a Determinar el mcd(259,111) y expresarlo como una combinaci´on
lineal de estos enteros.
b Hallar una expresi´on general que permita encontrar todos los en-
teros x e y tales que mcd(259,111) = 259x + 111y
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 15 / 26

<!-- página 16 -->

Ecuaciones diof´anticas (diofantinas)
Definici´on
Una ecuaci´on algebraica cuyos coeficientes son n ´umeros enteros, y el
conjunto soluci´on es un subconjunto de Z, recibe el nombre de Ecuaci´on
diof´antica (diofantina).
Ejemplo 3
2x + 5y = 9 7x− 8y2 + z = 1 x2 − 9y2 = 6
2x− 5xy + y = 1 x + y + z + w = 1 x3 + y3 = z3
En particular son de inter´es las ecuaciones diof´anticas lineales con dos
inc´ognitas. Son de la forma:
ax + by = c con a,b,c∈ Z
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 16 / 26

<!-- página 17 -->

Actividad 7
Hallar el conjunto soluci´on de las siguientes ecuaciones diof´anticas
7x + 9y = 102, 84x− 120y = 60, 25x + 30y = 42
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 17 / 26

<!-- página 18 -->

Actividad 8
En cada caso, plantear la ecuaci´on diof´antica que modela el problema,
y resolver:
a Juan depura un programa en Pascal en 6 minutos, pero en Python
tarda 10 minutos. Si trabaja en forma continua durante 104 mi-
nutos y no le sobr´o tiempo, ¿cu´antos programas depur´o en cada
lenguaje?
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 18 / 26

<!-- página 19 -->

b En una empresa de servicios de correo postal s´olo se tienen sellos
de 140 y 210 pesos. ¿De qu´e formas se pueden sellar un paquete
mediano por importe de $ 7770?
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 19 / 26

<!-- página 20 -->

c Una ferreter´ıa arma combos de tornillos para clientes mayoristas.
Hay dos tipos de cajas: Caja A con 37 tornillos, y Caja B con 102
tornillos. Un cliente pide exactamente 1017 tornillos. Determinar
si es posible cumplir con el pedido.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 20 / 26

<!-- página 21 -->

M´ınimo com ´un m ´ultiplo
Definici´on
El m´ınimo com ´un m ´ultiplo de dos n ´umero enteros positivos a y b, de-
notado mcm(a,b), es el ´unico n ´umero entero positivo m que satisface:
• m es m ´ultiplo de a y de b.
• Todo m ´ultiplo com ´un de a y b es m ´ultiplo m.
Ejemplo 4
M ´ultiplos positivos de 84: 84,168,252,336,420,504,588,672,840,···
M ´ultiplos positivos de 120: 120,240,360,480,600,720,840,···
mcm(84,120) = 840
Proposici´on
Para a,b∈ Z+, ab = mcm(a,b) ·mcd(a,b)
Ejemplo 5
mcm(84,120) = 84 · 120 12 = 840
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 21 / 26

<!-- página 22 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 4, apartado
4.4 (P´agina 225 ) del libro Matem´atica Discreta de Ralph Grimaldi que se
encuentra en el campus virtual: 1(a, c, d), 2, 3, 5, 6, 11, 13, 14, 15, 16,
19, 20.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 22 / 26

<!-- página 23 -->

Teorema fundamental de la aritm´etica (TFA)
Proposici´on
Si a,b∈ Z+, p es un primo y p|ab, entonces p|a o p|b.
Y generalizando esta idea ...
Sea ai ∈ Z+ para todo 1 ≤i≤n. Si p es primo y p|a1a2...an, entonces p|ai
para alg ´un 1 ≤i≤n.
Teorema
Todo entero n> 1 se factoriza un´ıvocamente de la forma
n = pc1 1 pc2 2 ···pcr r
donde p1, p2, ..., pr son los divisores primos de n
y los exponentes c1, c2, ..., cr son n ´umeros naturales.
Esta representaci´on de n recibe el nombre de representaci ´on can ´onica.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 23 / 26

<!-- página 24 -->

Si bien, por ejemplo 440 = 44·10 = 2·22·10; su representaci´on can´onica,
a la que llamaremos simplemente su “factorizaci´on” es 440 = 23 · 5 · 11.
Aunque los resultados te´oricos son claros, en la pr´actica no es tan f´acil
factorizar un n ´umero muy grande en tiempos computacionales razona-
bles.
Actividad 9
a Factorizar 980220.
b ¿En cu´antos ceros termina 80!?¿Cu´al es la m´axima potencia de 45
que lo divide?
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 24 / 26

<!-- página 25 -->

Sean las factorizaciones de dos n ´umeros enteros mayores a 1:
n = p1 e1 p2 e2 ...pek k m = p1 f1 p2 f2 ...pfk k
Si m|n, entonces 0 ≤fi ≤ei, para todo 1 ≤i≤k, por la regla del produc-
to, el n ´umero de divisores positivos de n es
#D+(n) = (e1 + 1)(e2 + 1)...(ek + 1)
Ejemplo 6
n = 819896 = 23 · 71 · 114, entonces sus divisores tendr´an la forma:
m = 2f1 · 7f2 · 11f3 , donde
f1 puede tomar valores entre 0 y 3,
f2 puede tomar valores entre 0 y 1, y
f3 puede tomar valores entre 0 y 4. Por lo que
#D+(819896) = (3 + 1)(1 + 1)(4 + 1) = 40
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 25 / 26

<!-- página 26 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 4, apartado
4.5 (P´agina 232 ) del libro Matem´atica Discreta de Ralph Grimaldi que se
encuentra en el campus virtual: 1, 2, 4, 5, 12, 13, 15, 19.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2026 26 / 26
