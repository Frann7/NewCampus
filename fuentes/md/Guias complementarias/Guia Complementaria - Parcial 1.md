# Guia Complementaria - Parcial 1

Fuente: `C:/Users/Administrator/Downloads/MATDISCRETA/Catedra/Guias complementarias/Guia Complementaria - Parcial 1.pdf` · 4 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |

<!-- página 1 -->

Lic. en Sistemas de Informaci´on
Matem´atica Discreta
Gu´ıa de ejercicios complementarios
Lenguajes
M´aquinas de estados finito
´Algebras de Boole
Lenguajes
1. Sea Σ = {x, y}
a. Obtener Σ2, Σ3, Σ+, Σ∗.
b. ¿Cu´antas cadenas de longitud menor o igual a 12 comienzan con xy en Σ∗?
2. Sean A = {1011} y B = {00, 1} dos lenguajes sobre el alfabeto Σ = {0, 1}. Determinar
cada uno de los siguientes lenguajes: a) AB b) BA c) A3 d) B2
3. Sea Σ = {a, b, c} :
a. ¿Cu´antas cadenas de Σ∗ son tales que tienen longitud menor o igual a cinco, y
prefijo propio bb?
b. ¿La cadena accccbccccabc ∈ {a, b, c}∗{b}? Justifique la respuesta.
c. Describa las cadenas de {a, b, c}{b}∗.
4. Sean A y B lenguajes de un alfabeto Σ∗. Especificar cu´ales de las siguientes afirmacio-
nes son verdaderas y cu´ales falsas. En el caso de que sean falsas mostrar un contraejem-
plo y las verdaderas justificar la respuesta (puede ser enunciando alguna propiedad).
a. A ∪ B ⊆ A
b. Σ∗ = Σ+ ∪ {λ}
c. A ⊆ A+
5. Sea Σ = {a, b, c}, use los lenguajes finitos de Σ∗, junto con las operaciones de conjuntos,
para describir el conjunto de cadenas de Σ∗ tales que:
a. Contienen exactamente una ocurrencia de b
b. Comienzan con la secuencia ab
c. Terminan con la secuencia cc
6. Dado el alfabeto Σ = {a, b, c, d, e}, determinar:
a. ¿Cu´antas cadenas de Σ4 contienen la subcadena bc exactamente una vez?
b. ¿Cu´antas cadenas de Σ6 comienzan con c y terminan con a?
c. Sea A el lenguaje definido de Σ∗ que contiene un n ´umero impar de letras a y B
es el lenguaje definido por el conjunto de cadenas que tienen a ac como prefijo
propio:
i. Escribir 5 elementos de cada lenguaje A y B.
ii. Determinar si la cadena w = aaaaab est´a en la concatenaci´on AB o en la con-
catenaci´on BA o en el lenguaje BA2.
7. Sea Σ = {0, 1}. Encontrar un lenguaje A para describir el conjunto de cadenas de Σ∗
1

<!-- página 2 -->

que tengan a 011 como subcadena.
a. Escribir simb´olicamente el lenguaje A, que contiene solamente a todas las pala-
bras de longitud par, que tengan a 10 como sufijo propio.
b. Sea B el lenguaje de Σ∗ = {a, b}∗ que contiene todas las cadenas de longitud
impar que s´olo contiene a en la posici´on central (por ejemplo: bbabb). Definir re-
cursivamente a B.
M´aquinas de estados finito
1. Construir una m´aquina de estados finitos que tenga como alfabeto de entrada y salida
{0, 1}, y que ante una cadena de entrada de longitud n, produzca una salida cuyos dos
primeros bits sean 10, y luego produzca los bits de la entrada (con m´as precisi´on, los
n-2 primeros).
2. La tabla siguiente corresponde a una m´aquina de estados finito cuyo conjunto de en-
trada y salida es {0, 1, 2}
a. Para cada cadena de entrada xi d´e la cadena de salida correspondiente
ν ω
0 1 2 0 1 2
S0 S0 S1 S2 0 1 2
S1 S1 S2 S0 1 2 0
S2 S2 S0 S1 2 0 1
x1 = 0110 x2 = 21000 x3 = 111
b. Dibujar el diagrama de estados.
c. Describir brevemente lo que realiza esta m´aquina.
3. Construir una m´aquina de estados para una m´aquina de estados finito con O = I =
{0, 1} que reconozca todas las cadenas del lenguaje:
a. {0, 1}∗{01}
b. {0, 1}∗{00} ∪ {0, 1}∗{11}
4. Para O = I = {0, 1}, una cadena x ∈ I∗ tiene paridad par si contiene un n ´umero par
de unos. Construir un diagrama de estados para una m´aquina de estados finitos que
reconozca todas las cadenas no vac´ıas de paridad par.
5. Sea O = I = {0, 1}. Construir una m´aquina de estados finito que reconozca:
a. Cada ocurrencia de 101 en una cadena x ∈ I∗ (con solapamiento)
b. 101 en una cadena x ∈ I∗, con la condici´on de reconocer ´unicamente aquellas
ocurrencias que terminen en una posici´on m ´ultiplo de tres.
6. Construir el diagrama de estados de una m´aquina de estados finito que, trabajando
con un alfabeto de entrada igual al de salida Σ = {0, 1}, reconozca produciendo un 1
en la salida toda vez que en la cadena de entrada se encuentre la subcadena 0001, de
tal forma que el 1 est´e en las posiciones 4, 8, 12, . . .
7. Sea Σ = {0, 1} y los lenguajes:
A = {010, 110, 00} y B = {x ∈ Σ∗/|x| ≤ 4 ∧ x tiene como prefijo propio 11}
2

<!-- página 3 -->

Se pide:
a. Listar los elementos de A2B.
b. Indicar si la cadena 1100 pertenece a BA
8. Sea I = O = {0, 1}. Construir un diagrama de estados para una m´aquina de estados
que reconozca cada ocurrencia de 01110 en una cadena de x ∈ I∗ (se permite solapa-
miento)
9. Sea A = {0}{0, 1}∗{001}, describir en t´erminos de sufijo y prefijo, los elementos de A.
Construir una m´aquina de estado finito que solamente reconozca todas las entradas
de A.
10. Sea la m´aquina de estados finitos M = (S, I, O, ν, ω), donde S = {s0, s1, s2}, I =
{a, b, c, d, e} y O = {0, 1}, calcular:
a. El n ´umero de funciones ν : S × I → S tales que ∀x ∈ I : ν(si, x) ̸= si
(queremos decir: tales que para cualquier entrada no se produce un bucle); y,
b. La cantidad de m´aquinas de estados finitos que se pueden construir con las ca-
racter´ısticas anteriores.
c. La cantidad de funciones tales que se produzcan en exactamente dos de sus esta-
dos sumideros.
11. Sea Σ = {x, y}, construir un diagrama de estados para la m´aquina de estados finitos
que reconozca la ocurrencia de todas las cadenas de Σ∗ que posean xyxy como prefijo
propio.
12. Dada la m´aquina de estados finitos:
s0
s1
s2 s4
s31,0
0,0
1,0
0,0
1,0
0,0
0,0
1,0
0,1
1,1
a. Escribir la tabla de estados de la m´aquina.
b. Obtener la secuencia de salida para x = 011011.
c. Determinar si es cierto que ν(s0, 001) = 000; ω(s0, 001) = s3.
d. Encontrar una subm´aquina.
e. Describa en palabras y/o en lenguajes de I∗ lo que hace esta m´aquina.
´Algebras de Boole
1. a. Sea la funci´on booleana f : B3 −→ B, tal que f = (x + y)( ¯x + z), escribir su forma
normal disyuntiva en t´erminos de sus variables.
b. Analizar si las siguientes afirmaciones son verdaderas o falsas:
i. Para f : B3 −→ B, existen solamente 6 funciones g tales los t´erminos 1 y 2 son
3

<!-- página 4 -->

mint´erminos.
ii. Sean las funciones booleanas f y g, ambas de B3 en B, tales que f = ∑ min(1, 2, 3)
y g = ∏ max(1, 2, 3), entonces f + g = 1.
2. Sea F5, la familia de todas las funciones booleanas f : B5 −→ B, se pide:
a. Calcular la cantidad de elementos que tiene F5.
b. Calcular la cantidad de funciones f que cumplen con
f (x1, x2, x3, x4, x5) = f (x1, x2, ¯x3, x4, ¯x5)
c. ¿Cu´antas conjunciones fundamentales existen en F5?
d. Calcular la cantidad de funciones booleanas que tienen exactamente 4 unos en su
salida.
e. ¿Cu´antas funciones f ∈ F5 toman el valor 1 cuando exactamente dos de sus 5
variables toman el valor 1 (en el resto no importa el valor de f ).
f. Determinar qu´e valores de las variables booleanas verifican
x1x2x3x4x5 = x1 + x2 + x3 + x4 + x5
g. Proponer una expresi´on booleana y su problema dual.
h. Dado el conjunto de las preim´agenes de 1: f −1(1) = {11001, 11111, 00011, 10101, 00110},
encontrar la forma normal disyuntiva de f .
3. Construir la tabla, y expresar la fnd y la fnc de la funci´on booleana:
f : B3 → B/ f (x, y, z) = (x + y)(x + ¯z)
4. Demostrar la Ley de absorci´on: x + xy = x.
5. Resolver las ecuaciones simult´aneas: (x + y) · z = 1 ; x + z = 1 ; y + ¯z = x.
4
