# md - teo - 2025 - U6

Fuente: `C:/Users/Administrator/Downloads/MATDISCRETA/Catedra/Unidad 6 - Anillos y aritmetica modular/md - teo - 2025 - U6.pdf` · 52 página(s) · texto extraído con pypdf.
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
| 42 |  |
| 43 |  |
| 44 |  |
| 45 |  |
| 46 |  |
| 47 |  |
| 48 |  |
| 49 |  |
| 50 |  |
| 51 |  |
| 52 |  |

<!-- página 1 -->

Matem´atica Discreta
Licenciatura en Sistemas de Informaci´on
Docentes
Vaira, Stella - Fedonczuk, Miguel
Colliard, David - Cottonaro, Mariana - Froloff, B´arbara
FCyT - UADER
2025

<!-- página 2 -->

Unidad 6: Anillos y aritm´etica modular.
La estructura de anillo: definici´on y ejemplos. Propiedades de los ani-
llos. Subestructuras: subanillos e ideales. Los enteros m´odulo n: Propie-
dades. Relaciones con la funci´on ϕ de Euler. Homomorfismo e isomor-
fismo de anillos. Aplicaciones.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 2 / 52

<!-- página 3 -->

ESTRUCTURA DE ANILLO
Definci´on
Si R es un conjunto no vac´ıo con dos operaciones binarias cerradas,
denotadas con + y · (que pueden ser diferentes de la suma y producto
usuales). Entonces (R, +, ·) es un anillo si para todos a, b, c ∈ R se cumplen
las siguientes condiciones:
1 a + b = b + a. (ley de conmutativa de +)
2 a + (b + c) = (a + b) + c (ley asociativa de +)
3 ∃z ∈ R tal que a + z = z + a = a, ∀a ∈ R (Identidad para +)
4 ∀a ∈ R, ∃b ∈ R/ a + b = b + a = z (inverso bajo +)
5 a · (b · c) = (a · b) · c (ley asociativa de ·)
6 a · (b + c) = a · b + a · c, y (b + c) · a = b · a + c · a (distributivas)
Al trabajar con la segunda operaci´on, en vez de escribir a · b se escribe con frecuencia ab. Adem´as
por medio de Inducci´on matem´atica se puede probar que dichas propiedades sobre
las operaciones se pueden extender para n elementos del anillo definido.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 3 / 52

<!-- página 4 -->

Ejemplo 1
Con las operaciones binarias (cerradas) de la suma y producto usuales,
Z, Q, R y C son anillos. En todos estos anillos, la identidad de la suma
z es el entero 0 y el inverso aditivo de cualquier n ´umero x es −x.
Ejemplo 2
Sea M2(Z) el conjunto de todas las matrices 2×2 con elementos enteros.
En M2(Z), dos matrices son iguales si sus elementos correspondientes
son iguales en Z. Se definen + y · como sigue:
"
a b
c d
#
+
"
e f
g h
#
=
"
a + e b + f
c + g d + h
#
"
a b
c d
#"
e f
g h
#
=
"
ae + bg af + bh
ce + dg cf + dh
#
Conocidas como suma y producto usuales entre matrices.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 4 / 52

<!-- página 5 -->

Se puede probar que (M2(Z), +, ·) es un anillo. Como se puede ver f´acil-
mente, la identidad z y el inverso aditivos de A son respectivamente:
z =
"
0 0
0 0
#
A =
"
a b
c d
#
(−A) =
"
−a −b
−c −d
#
Observar qu´e ocurre con estas multiplicaciones:
"
1 2
1 1
#"
3 7
1 0
#
=
"
5 7
4 7
# "
3 7
1 0
#"
1 2
1 1
#
=
"
10 13
1 2
#
Entonces...
"
1 −1
−1 1
#"
2 1
2 1
#
=
"
0 0
0 0
#
Entonces...
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 5 / 52

<!-- página 6 -->

Definiciones
Sea (R, +, ·) un anillo.
1 Si ab = ba, ∀a, b ∈ R, entonces R es un anillo conmutativo.
2 El anillo R no tiene divisores propios de cero si para cualquiera a, b ∈
R, ab = z implica que a = z o b = z.
3 Si un elemento u ∈ R es tal que u , z y au = ua = a para todo a ∈ R,
decimos que u es elemento unidad (o identidad para el producto) de
R. Entonces R es un anillo con unidad.
Actividad 1
Analicemos si la estructura (Z, ⊕, ⊙), con las operaciones definidas a
continuaci´on, es un anillo conmutativo con elemento unidad:
x ⊕ y = x + y − 1 x ⊙ y = x + y − xy
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 6 / 52

<!-- página 7 -->

Para todo x, y, z enteros (elementos del conjunto dado):
Ley de cierre para ⊕ y ⊙:
Conmutativa para ⊕:
Asociativa para ⊕:
Identidad para ⊕:
Inverso para ⊕:
Asociativa para ⊙:
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 7 / 52

<!-- página 8 -->

Distributiva de ⊙ respecto a ⊕:
Por lo demostrado, (Z, ⊕, ⊙) es un anillo.
¿Es un anillo conmutativo?:
¿Posee divisores propios de cero?:
¿Posee elemento unidad u?:
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 8 / 52

<!-- página 9 -->

Actividad 2
Sea U = {1, 2} y R = P(U). Definimos + y · sobre los elementos de R como:
A + B = A∆B = (A ∪ B) − (A ∩ B) A · B = A ∩ B
Como el conjunto de partes de U es finito, podemos ver los resultados
en las siguientes tablas. Analicemos si dicha estructura es un anillo:
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 9 / 52

<!-- página 10 -->

Actividad 3
Para R = {a, b, c, d, e}, definimos + y · mediante las siguientes tablas:
Dicha estructura es un anillo. Analizar algunas de las propiedades que
la hacen un anillo, identificar el elemento unidad, la identidad para +,
el inverso aditivo de cada elemento, y si tiene divisores propios de cero.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 10 / 52

<!-- página 11 -->

Definici´on
Sea R un anillo con elemento unidad u. Si a, b ∈ R y ab = ba = u, entonces
b es un inverso multiplicativo de a y a es una unidad de R. (tambi´en a es
inverso de b, y b es una unidad de R)
Es decir, que una unidad en R es un elemento que posee inverso multi-
plicativo.
No confundir con el elemento unidad u.
Definiciones
Sea R un anillo conmutativo con elemento unidad. Entonces:
• R es un dominio de integridad si R no tiene divisores propios de cero.
• R es un cuerpo (o campo) si todo elemento distinto de cero en R es
una unidad.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 11 / 52

<!-- página 12 -->

Actividad 4
Analizar si los conjuntos Z, Q, R y C con la suma y producto usuales
son dominio de integridad y cuerpo. Lo mismo para los anillos presen-
tados en las actividades 1, 2 y 3.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 12 / 52

<!-- página 13 -->

Actividad 5
Sea R = {s, t, v, w, x, y}. Definimos + y · por medio de las siguientes tablas.
Se puede probar que dicha estructura es un anillo. Analizar algunas de
las propiedades que la hacen un anillo, y si posee elemento unidad, y
en tal caso, hallar las unidades.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 13 / 52

<!-- página 14 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 14, apartado
14.1 (P´agina 707 ) del libro Matem´atica Discreta de Ralph Grimaldi que
se encuentra en el campus virtual: 2d, 2e, 4, 6, 7, 8, 9, 10, 12, 13.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 14 / 52

<!-- página 15 -->

SUBESTRUCTURAS: SUBANILLOS E IDEALES
Teorema
En cualquier anillo (R, +, ·)
• el elemento neutro z es ´unico
• el inverso aditivo de cada elemento del anillo es ´unico.
Observaciones
• El inverso aditivo de un elemento a se denotar´a como −a
• Hablaremos de resta en un anillo haciendo referencia a
x − y = x + (−y)
Teorema (leyes de cancelaci´on para la suma)
Para cualesquiera a, b, c de un anillo (R, +, ·)
• a + b = b + c =⇒ b = c
• b + a = c + a =⇒ b = c
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 15 / 52

<!-- página 16 -->

Teorema
Dado un anillo (R, +, ·) y a ∈ R: za = az = z
Teorema
Dado un anillo (R, +, ·) y a, b ∈ R:
•−(−a) = a
• a(−b) = (−a)b = −(ab)
• (−a)(−b) = ab
Teorema
En cualquier anillo (R, +, ·)
• el elemento unidad (u), es ´unico
• si R tiene un elemento unidad y a es una unidad de R, entonces el
inverso multiplicativo de a es ´unico.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 16 / 52

<!-- página 17 -->

Teorema
Si (F, +, ·) es un cuerpo, entonces es un dominio de integridad.
Estamos afirmando que si F es un cuerpo, no posee divisores propios
de cero.
Teorema
Un dominio de integridad finito (D, +, ·) es un cuerpo.
Definici´on
Para un anillo (R, +, ·) , un subconjunto no vac´ıo S de R es un subanillo
de R si (S, +, ·) es un anillo.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 17 / 52

<!-- página 18 -->

Ahora, ¿c´omo podemos asegurar que un subconjunto no vac´ıo de un
anillo, es subanillo?
Teorema
En cualquier anillo (R, +, ·), si ∅ , S ⊆ R,
• entonces (S, +, ·) es un subanillo de R si y solo si para todo a, b ∈ S,
tenemos que a − b ∈ S y ab ∈ S;
• y si S es finito, entonces (S, +, ·) es un subanillo de R si y solo si para
todo a, b ∈ S, tenemos que a + b ∈ S y ab ∈ S;
Ejemplo 3
Consideremos el anillo R = M2 (Z) y el subconjunto de R
S =
("
x x + y
x + y x
#
/x, y ∈ Z
)
Es claro que es un subconjunto no vac´ıo, por ejemplo, cuando x = y = 0,"
0 0
0 0
#
∈ S.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 18 / 52

<!-- página 19 -->

Sean dos elementos de S, las matrices de componentes enteros
"
a a + b
a + b a
#
y
"
c c + d
c + d c
#
La resta es cerrada, porque"
a a + b
a + b a
#
−
"
c c + d
c + d c
#
=
"
a − c (a + b) − (c + d)
(a + b) − (c + d) a − c
#
"
a a + b
a + b a
#
−
"
c c + d
c + d c
#
=
"
a − c (a − c) + (b − d)
(a − c) + (b − d) a − c
#
El producto es cerrado, porque"
a a + b
a + b a
#"
c c + d
c + d c
#
=
"
bd + ad + bc +2ac ad + bc +2ac
ad + bc +2ac bd + ad + bc +2ac
#
=
=
"
bd + ad + bc +2ac (bd + ad + bc +2ac) + (−bd)
(bd + ad + bc +2ac) + (−bd) bd + ad + bc +2ac
#
Con lo cual S es un subanillo de R.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 19 / 52

<!-- página 20 -->

Definici´on
Para un anillo (R, +, ·) , un subconjunto no vac´ıo I de R es un ideal de R
si para todo a, b ∈ I y para todo r ∈ R, se verifica que a − b ∈ I y ar, ra ∈ I.
Representaci´on en diagramas de Venn de la diferencia entre un subani-
llo S y un ideal I, de un anillo R:
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 20 / 52

<!-- página 21 -->

Actividad 6
Para el anillo y el subanillo del ejemplo 3, ¿es S un ideal de R?
Observaci´on
Un ideal es un subanillo (¿por qu´e?), pero el rec´ıproco no siempre se
cumple: (Z, +, ·) es un subanillo de (Q, +, ·) pero no es un ideal, ya que
por ejemplo para 4 ∈ Z y 1 3 ∈ Q, pero 4 3 < Z
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 21 / 52

<!-- página 22 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 14, apartado
14.2 (P´agina 715 ) del libro Matem´atica Discreta de Ralph Grimaldi que
se encuentra en el campus virtual: 3a, 4, 5, 6, 7, 8, 9, 10, 15, 16, 20 .
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 22 / 52

<!-- página 23 -->

LOS ENTEROS MODULO n
Definci´on
Sea n ∈ Z+, n > 1. Para a, b ∈ Z, decimos que a es congruente con b m´odulo
n, y escribimos:
a ≡ b (mod n)
si n|(a − b) o equivalentemente a = b + kn para alg ´un k ∈ Z
Ejemplo 4
10 ≡ 1 (mod 3) porque 3|(10 − 1), es decir 10 = 3(3) + 1.
Tambi´en ser´an equivalentes con 1 (mod 3) los enteros que al ser dividi-
dos por 3 dan como resto 1.
30 ≡ 5 (mod 25) porque 25|(30 − 5), es decir 30 = 25(1) + 5.
Tambi´en ser´an equivalentes con 5 (mod 25) los enteros que al ser divi-
didos por 25 dan como resto 5.
29 ≡−1 (mod 5) porque 5|(29 − (−1)), es decir 29 = 5(6) + (−1).
¿Qu´e puedes decir respecto del resto de dividir a 29 por 5?

<!-- página 24 -->

Teorema
La congruencia m´odulo n es una relaci´on de equivalencia sobre Z
Para n ≥ 2 esta relaci´on de equivalencia induce una partici´on sobre Z.
La conguencia m´odulo n divide a Z en n clases de equivalencias.
Por ejemplo, si n = 6:
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 24 / 52

<!-- página 25 -->

Teorema
La congruencia m´odulo n es una relaci´on de equivalencia sobre Z
Para n ≥ 2 esta relaci´on de equivalencia induce una partici´on sobre Z.
La conguencia m´odulo n divide a Z en n clases de equivalencias:
[0] = {..., −2n, −n, 0, n, 2n, ...} = {nx + 0/x ∈ Z}
[1] = {..., −2n + 1, −n + 1, 1, n + 1, 2n + 1, ...} = {nx + 1/x ∈ Z}
[2] = {..., −2n + 2, −n + 2, 2, n + 2, 2n + 2, ...} = {nx + 2/x ∈ Z}
... ...
[n − 1] = {..., −2n + (n − 1), −n + (n − 1), n − 1, n + (n − 1), 2n + (n − 1), ...}
[n − 1] = {nx + (n − 1)/x ∈ Z}
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 25 / 52

<!-- página 26 -->

Por el algoritmo de la divisi´on: ∀t ∈ Z t = qn + r con 0 ≤ r < n
Por lo que t pertenece a la clase [r] o la clase de t es la misma que la
clase de r ([t] = [r])
Zn = {[0], [1], [2], ..., [n − 1]}
si consideramos que a es un elemento de Zn, y no hay ambig¨uedad en
la notaci´on, podemos escribir:
Zn = {0, 1, 2, ..., (n − 1)}
En este conjunto se definen las operaciones binarias cerradas adici´on y
multiplicaci´on, como sigue
∀[a], [b] ∈ Z:
[a] + [b] = [a + b] [a] · [b] = [a][b] = [ab]
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 26 / 52

<!-- página 27 -->

[a] + [b] = [a + b] [a] · [b] = [a][b] = [ab]
Por ejemplo, en Z7:
• [2] + [6] = [2 + 6] = [8] = [1]
• [2][6] = [2 · 6] = [12] = [5]
En t´erminos de m´odulo diremos que:
Si a ≡ b (mod n) y c ≡ d (mod n), entonces
a + c ≡ b + d (mod n) y ac ≡ bd (mod n)
Por ejemplo, en Z7, es decir n = 7:
• 2 + 6 ≡ 8 ≡ 1 (mod 7)
• 2 · 6 ≡ 12 ≡ 5 (mod 7)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 27 / 52

<!-- página 28 -->

Teorema
Para n ∈ Z+, n > 1:
Zn es un anillo conmutativo con elemento unidad igual a [1] en las
operaciones binarias cerradas definidas antes.
Al ser Zn un anillo finito, podemos expresar las operaciones entre los
elementos por medio de dos tablas.
Ejemplo 5
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 28 / 52

<!-- página 29 -->

Actividad 7
Para Z5: identificar las unidades, sus respectivos inversos multiplicati-
vos. ¿Tiene divisores propios de cero? ¿Cu´ales son?
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 29 / 52

<!-- página 30 -->

Actividad 8
Para Z6: identificar las unidades, sus respectivos inversos multiplicati-
vos. ¿Tiene divisores propios de cero? ¿Cu´ales son?
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 30 / 52

<!-- página 31 -->

Teorema
Zn es un cuerpo si y s´olo si n es primo.
Ejemplo 6
Z2, Z3, Z5, Z7, ··· son cuerpo; y Z6, Z9, Z200, por ejemplo, no lo son.
Teorema
En Zn, [a] es una unidad si y s´olo si mcd(a, n) = 1
Ejemplo 7
En Z15: [1], [2], [4], [7], [8], [11], [13], [14] son unidades.
[a] 1 2 4 7 8 11 13 14
[a]−1
[3], [5] son divisores propios de cero porque [3][5] = [15] = [0]
[6], [10] son divisores propios de cero porque [6][10] = [60] = [0]
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 31 / 52

<!-- página 32 -->

Ejemplo 8
Buscaremos el inverso multiplicativo de [25] en Z72
[25]−1 es tal que [25]−1[25] ≡ 1 (mod 72)
Si [25]−1 = x, buscamos que 25x = 72y + 1, con y ∈ Z
De esta manera debemos resolver la ecuaci´on diof´antica: 25x − 72y = 1.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 32 / 52

<!-- página 33 -->

Ya sabemos c´omo identificar si un elemento es, o no, una unidad. Ahora
nos preguntamos:
¿Cu´antas unidades tiene el anillo Zn?
Para calcular dicho n ´umero utilizamos la funci´on ϕ(n)
Sea la factorizaci´on de n como producto de primos distintos:
n = p1 e1 p2 e2 . . . pr er
ϕ(n) = n
 p1 − 1
p1
! p2 − 1
p2
!
···
 pr − 1
pr
!
En Zn, existen ϕ(n) unidades y n − 1 − ϕ(n) divisores propios de cero.
Ejemplo 9
Para n = 7875 = 32537, Z7875 tiene:
ϕ(7875) = 7875 2 3 4 5 6 7 = 3600 unidades, y 4274 divisores propios de cero.
C.Aux: 7875 − 1 − 3600 = 4274
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 33 / 52

<!-- página 34 -->

Definici´on
Una ecuaci´on de la forma ax ≡ b(m´odm) se llama ecuaci´on lineal de
congruencia.
La ecuaci´on ax ≡ b(m´odm) se puede expresar como ax − my = b. Y la
resolubilidad de ambas est´a asegurada si mcd(a, m) divide a b.
Entonces 3x ≡ 4(m´od15) no tiene soluci´on, pero 3X ≡ 12(m´od15) s´ı.
Con lo cual, si mcd(a, m) = 1, toda ecuaci´on ax ≡ b(m´odm) tiene una
´unica soluci´on dada por x ≡ a−1b(m´od m).
Ejemplo 10
Como 7−1 = 3 en Z10:
7x ≡ 6(m´od10)
x ≡ 3 · 6(m´od10)
x ≡ 8(m´od10)
S = {8}
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 34 / 52

<!-- página 35 -->

Ejemplo 11
¿Qu´e ocurre cuando a y m no son coprimos?
152x ≡−88(m´od36)
En primera instancia reducimos los coeficientes m´odulo 36
8x ≡ 20(m´od36)
Como mcd(8, 36) = 4 divide a 20, la ecuaci´on dada tiene soluci´on. Es
m´as, tendr´a tantas como el mcd, en este caso, 4.
Es claro que no podemos “despejar x”, para ello necesitar´ıamos el in-
verso multiplicativo de 8 en Z36, que no existe.
Buscaremos la forma que tienen esas 4 soluciones, dividiendo todos los
coeficientes de la ecuaci´on por 4.
2x ≡ 5(m´od9) =⇒ x ≡ 5 · 5(m´od9) =⇒ x ≡ 7(m´od9)
Los x que satisfacen la ecuaci´on original son de la forma 9k + 7
en Z36, con lo cual S = {7, 16, 25, 34}.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 35 / 52

<!-- página 36 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 14, apartado
14.3 (P´agina 721 ) del libro Matem´atica Discreta de Ralph Grimaldi que
se encuentra en el campus virtual: 1, 2, 3, 5, 8, 9, 10a, 11, 16, 17, 20.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 36 / 52

<!-- página 37 -->

HOMOMORFISMO E ISOMORFISMO DE ANILLOS
Observemos el siguiente conjunto:
R = Z2 × Z3 × Z5
Sus elementos son ternas, y cada componente pertenece a Z2, Z3 y Z5,
respectivamente. De esta manera la cantidad de elementos de R es
|R| = |Z2|·|Z3|·|Z5| = 30.
Se definen las operaciones adici´on y multiplicaci´on en R como sigue:
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 37 / 52

<!-- página 38 -->

Se puede demostrar que la estructura (R, ⊕, ⊙) es un anillo conmutativo
con elemento unidad, donde z = (0, 0, 0) y u = (1, 1, 1).
Sus treinta elementos son:
Actividad 9
Resolver las siguientes operaciones en dicho anillo:
1 (0, 2, 3) ⊕ (1, 2, 2) ⊙ (1, 1, 4) =
2 (1, 2, 2) ⊕ (1, 1, 3) =
Por lo que (1, 2, 2) y (1, 1, 3) son ...
3 (1, 2, 2) ⊙ (1, 2, 3)
Por lo que (1, 2, 2) y (1, 2, 3) son ...
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 38 / 52

<!-- página 39 -->

Definici´on
Sea (R, +, ·) y (S, ⊕, ⊙) anillos. Una funci´on f : R → S es un homomorfis-
mo de anillos si para todos a, b de R:
1 f (a + b) = f (a) ⊕ f (b)
2 f (a · b) = f (a) ⊙ f (b)
Si adem´as, la funci´on f es biyectiva, entonces tendremos un isomorfis-
mo de anillos.
Ejemplo 12
Consideremos los anillos (Z, +, ·) y (Zn, +(mod n), ·(mod n)), y definimos
f : Z → Zn /f (x) = [x]
Como para todo entero x e y se verifica:
f (x + y) = [x + y] = [x]+[y] = f (x)+f (y)
f (x · y) = [xy] = [x]·[y] = f (x)·f (y)
resulta f un homomorfismo entre los anillos dados.
¿Es f un isomorfirmo de anillos?¿es f biyectiva?
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 39 / 52

<!-- página 40 -->

Ejemplo 13
Consideremos los anillos (R, +, ·) y (Z5, +(m´od5), ·(m´od5)), y definimos
f : R → Z5 tal que:
f (a) = [0], f (b) = [1], f (c) = [2], f (d) = [3], f (e) = [4]
Si vemos las respectivas tablas de operaciones, se puede observar un
solapamiento entre ellas. As´ı, f determina un isomorfirmo entre los
anillos dados.
R
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 40 / 52

<!-- página 41 -->

Por ejemplo, f (c + d) = f (a) = [0] = [2] + [3], mientras que f (be) = f (e) =
[4] = [1][4] = f (b)f (e).
Como no disponemos de otros m´etodos y teoremas, hay que verificar 25
igualdades de este tipo para que se preserven las operaciones binarias.
Ejemplo 14
Sean C el cuerpo de los n ´umeros complejos y S el anillo de las matrices
cuadradas reales de orden 2 de la forma
"
a b
−b a
#
; definimos para todo
complejo a + bi:
f (a + bi) =
"
a b
−b a
#
La cual es biyectiva (probar!).
Adem´as, f determina un homomorfismo entre los anillos, ya que
∀z, w ∈ C:
f (z + w) = f (z) + f (w) y f (zw) = f (z)f (w)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 41 / 52

<!-- página 42 -->

f ((a + bi) + (x + yi)) = f ((a + x) + (b + y)i)
=
"
a + x b + y
−(b + y) a + x
#
=
"
a b
−b a
#
+
"
x y
−y x
#
= f (a + bi) + f (x + yi),
f ((a + bi)(x + yi)) = f ((ax − by) + (bx + ay)i)
=
"
ax − by bx + ay
−(bx + ay) ax − by
#
=
"
a b
−b a
#"
x y
−y x
#
= f (a + bi)f (x + yi).
Con lo cual f es un isomorfirmo de anillos, y podr´ıamos usarlo para
calcular (2 + 3i) + (4 − 7i)3
i5
"
2 3
−3 2
#
+
"
4 −7
7 4
#3   " 0 1 −1 0 #5  −1 = " 9 527 −527 9 #
(2 + 3i) + (4 − 7i)3
i5 = 9 + 527i
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 42 / 52

<!-- página 43 -->

Teorema Chino del Resto (Parte 1)
Sea la descomposici´on factorial de n = pe1 1 pe2 2 ··· pek k , los anillos Zn y
Zm1 × Zm2 ×···× Zmk son isomorfos, con m1 = pe1 1 , m2 = pe2 2 , . . . , mk = pek k
Ejemplo 15
Z30 y Z2 × Z3 × Z5 lo son. Las operaciones involucradas en cada estruc-
tura son adici´on y multiplicaci´on, cada una en su respectivo m´odulo. A
continuaci´on se puede ver que la siguiente funci´on
f : Z30 → Z2 × Z3 × Z5 determina un homomorfirmo entre los anillos.
∀a ∈ Z30 : f (a) = (a m´od 2, a m´od 3, a m´od 5)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 43 / 52

<!-- página 44 -->

Adem´as, la tabla muestra que la funci´on es biyectiva (uno a uno); y de
esta manera los anillos involucrados resultan isomorfos.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 44 / 52

<!-- página 45 -->

Actividad 10
Utilizando la tabla, hallar:
1 (0, 2, 3) ⊕ (1, 2, 2) ⊙ (1, 1, 4)
2 (1, 2, 2)−1
3 (1, 2, 2) ⊙ X = (0, 2, 3) ⊕ (1, 2, 2) ⊙ (1, 1, 4)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 45 / 52

<!-- página 46 -->

De esta manera, si f : Z30 → Z2 × Z3 × Z5 podemos construir una tabla
con todas las asignaciones, y buscar, por ejemplo:
• f (20) = (0, 2, 0). La imagen de 20 que es (0, 2, 0)
• f −1(1, 2, 3) = 23. La preimagen del (1, 2, 3) que es el 23.
Si la cantidad de elementos del anillo es muy grande, no tiene sentido
armar la tabla de asignaciones, pero podemos hallar la imagen de un
elemento en particular. Por ejemplo, en f : Z437 → Z23 × Z19, la imagen
de 400 es
f (400) = (400 m´od 23, 400 m´od 19) = (9, 1)
El problema es hallar la preimagen de un elemento de Z23 × Z19.
¿cu´al ser´a la preimagen de (18, 17)?
¿Cu´al es el n ∈ Z437 tal que n ≡ 18(m´od23) y n ≡ 17(m´od19)?
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 46 / 52

<!-- página 47 -->

Teorema Chino del Resto (Parte 2)
Sean m1, m2, . . . , mr n ´umeros naturales coprimos dos a dos y sea M
su producto. Si a1, a2, . . . , ar es una secuencia cualquiera de n ´umeros
enteros, existe un n ´umero entero x que verifica simult´aneamente las
congruencias x ≡ ai (m´od mi ), i = 1, 2, . . . , r.
Adem´as, x est´a un´ıvocamente determinado m´odulo M.
Para hallar x, definimos
M = Qr i=1 mi Mi = M mi vi (el inverso de Mi (m´od mi )).
El entero x buscado es
x =
rX
i=1
Mi vi ai
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 47 / 52

<!-- página 48 -->

Ejemplo 16
Calcular f −1(2, 7, 3) para f : Z315 → Z7 × Z9 × Z5
a1 = 2 a2 = 7 a3 = 3
M1 = 45 M2 = 35 M3 = 63 M = 315
M1 ≡ 3(m´od7) M2 ≡ 8(m´od9) M3 ≡ 3(m´od5)
v1 = 5 v2 = 8 v3 = 2
x = 2 · 45 · 5 + 7 · 35 · 8 + 3 · 63 · 2 = 2788 ≡ 268(m´od315)
x = 268 en Z325
Verificaci´on
f (268) = (268(m´od7), 268(m´od9), 268(m´od5)) = (2, 7, 3)
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 48 / 52

<!-- página 49 -->

Actividad 11
¿Cu´al es el precio de una enciclopedia que vale menos de $1000, si se
ofrecen los siguientes planes de pago sin inter´es?
• Anticipo de $20 y cuotas mensuales de $18.
• Anticipo de $30 y cuotas mensuales de $25.
• Anticipo de $37 y cuotas mensuales de $49.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 49 / 52

<!-- página 50 -->

Teorema de Fermat
Si p es un n ´umero primo y a es un entero no divisible por p, entonces
ap−1 ≡ 1(m´od p)
Este teorema es conocido como el “Peque˜no Teorema de Fermat”. Para
ejemplificarlo, podemos decir que 2010 ≡ 1(m´od11) porque 11 ̸|20 .
Actividad 12
Hallar el resto de dividir a 51235415 por 13.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 50 / 52

<!-- página 51 -->

Definici´on
Si m es un n ´umero natural, la cantidad de n ´umeros naturales menores
o iguales a m y coprimos con m ser´a llamada indicador de Euler de m,
que notaremos ϕ(m)
Su c´alculo se mostr´o cuando fue necesario hallar la cantidad de elemen-
tos de Zn que poseen inverso multiplicativo.
Teorema de Fermat-Euler
Sea m un n ´umero natural y sea a es un entero coprimo con m, entonces
aϕ(m) ≡ 1(m´od m)
Si m es primo, se tiene el Peque˜no Teorema Fermat (¿por qu´e?)
Actividad 13
Determinar las ´ultimas dos cifras del n ´umero 74578963.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 51 / 52

<!-- página 52 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 14, apartado
14.4 (P´agina 728 ) del libro Matem´atica Discreta de Ralph Grimaldi que
se encuentra en el campus virtual: 1, 3, 4, 6, 7, 9, 10, 11.
Vaira-Fedonczuk-Colliard-Cottonaro-Froloff Matem´atica Discreta - LSI - UADER 2025 52 / 52
