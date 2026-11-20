# Complementaria Parcial 3 MD

Fuente: `C:/Users/Administrator/Downloads/MATDISCRETA/Catedra/Guias complementarias/Complementaria Parcial 3 MD.pdf` · 4 página(s) · texto extraído con pypdf.
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
Anillos
Grupo y Teor´ıa de la Codificaci´on
Anillos
1. En A = {a, b, c, d, e} se definen las operaciones de adici´on y multiplicaci´on mediante las tablas:
+ a b c d e
a a b c d e
b b c d e a
c c d e a b
d d e a b c
e e a b c d
· a b c d e
a a a a a a
b a b c d e
c a c e b d
d a d b e c
e a e d c b
De esta manera, A con las operaciones definidas, determinan un anillo finito. Se pide:
a. El elemento neutro de la adici´on y el elemento neutro de la multiplicaci´on.
b. Determinar la lista de los opuestos, y si existen elementos que tengan inverso multiplica-
tivo.
c. ¿Es conmutativo el anillo?
d. ¿Es un Dominio de Integridad? ¿Es un Cuerpo?
2. Sea S un subconjunto del anillo M2×2, con S =
{︃(︃0 a
a 0
)︃
/a ∈ R
}︃
. Determinar si S es subanillo
de M2×2 y/o un Ideal de dicho anillo.
3. Para los anilos Z9 y Z11 determinar las unidades y los divisores propios de cero.
4. En el anillo Z1028 hallar, si existen, los inversos multiplicativosde 275 y 257.
5. Hallar el conjunto soluci´on de la ecuaci´on x3 − x + 1 = 0 en Z4.
6. Dado el anillo R = Z230:
a. ¿Cu´antas unidades tiene R?
b. Hallar 77−1.
c. Resolver 77x − 204 ≡ 0 (mod 230).
d. Hallar cuatro divisores propios de cero.
e. ¿Es R un cuerpo?
f. Determinar un anillo isomorfo a R. Luego mostrar las im´agenes de 10 y 211.
7. Hallar el resto de dividir 132019 por 11. (Teorema de Fermat)
8. Resolver 132019x ≡ 5 (mod 11)
9. ¿Cu´al es el resto de dividir 750 por 30? (Teorema de Fermat-Euler)
10. Indicar un cuerpo con m´as de 100 elementos.
1

<!-- página 2 -->

11. Dado el anillo Z7 × Z15, hallar el opuesto de (2, 8) y el inverso de (6, 2).
12. Sea la funci´on f : Z12 → Z4 × Z6:
a. Probar que f es un homomorfismo de anillos.
b. Encontrar un elemento de Z4 × Z6 que no est´e en la imagen de f .
c. ¿Cu´al elemento n de Z12 es tal que f (n) = (1, 3); es decir, la preimagen de (1, 3).
d. ¿Determina f un isomorfismo entre los anillos dados?
13. Efectuar la siguiente operaci´on en Z234:
[35]−1 · [2] + [13]5
14. Utilizar el Teorema Chino del Resto para establecer un isomorfismo entre los anillos Z30 y
Z2 × Z3 × Z5.
Calcular f (18) y f (−20).
Calcular la preimagen de (1, 1, 1).
15. Utilizar el Teorema Chino del Resto (parte 2) para hallar f −1(7, 21) en el isomorfismo
f : Z611 → Z13 × Z47.
16. Se puede demostrar que para cualquier entero a y primo p: ap ≡ a (mod p).
Utilizar esta propiedad para demostrar que n7
7 + n5 5 + 23n 35 es un n ´umero natural para todo n ∈ N
17. Los n ´umeros pseudoaleatorios se generan a trav´es de la relaci´on de recurrencia aplicada suce-
sivamente: xn+1 ≡ axn + c (m´od m). Hallar x5 para m = 9, a = 7, c = 4 y x0 = 3.
18. Recordemos la cantidad de soluciones que tienen las ecuaciones lineales en diferentes anillos:
• si tenemos la ecuaci´on ax = b en el cuerpo de los n ´umeros R, sabemos que tiene una ´unica
soluci´on si a ̸= 0, tiene infinitas soluciones si a = b = 0, no tiene soluci´on si a = 0 y b ̸= 0; •
la misma ecuaci´on en el anillo de los Z tiene ´unica soluci´on si a ̸= 0 y b m ´ultiplo de a, tiene
infinitas soluciones si a = b = 0 y no tiene soluci´on si a = 0 y b ̸= 0 o cuando a ̸= 0 y b no es
m ´ultiplo de a.
En las ecuaciones lineales en congruencia, ax ≡ b (m´odulo n), es decir en el anillo de los enteros
m´odulo n (Zn), pasa algo similar:
• si mcd(a, n) = 1 (que siempre divide a b) tiene una ´unica soluci´on (ya que en este caso a tiene
inverso multiplicativo en ese anillo m´odulo n),
• si mcd(a, n)|b, entonces tiene exactamente d soluciones, donde d = mcd(a, n) de soluciones,
• si mcd(a, n) no divide a b, la ecuaci´on no tiene soluci´on.
Las ecuaciones lineales en congruencia (como las ecuaciones lineales) est´a estudiadas: desde el
punto de vista de la cantidad de soluciones se puede dar que tengan una ´unica soluci´on, una
cierta cantidad d de soluciones o ninguna soluci´on.
Proponer en el anillo Z90 una ecuaci´on en congruencia de cada tipo, seg ´un el n ´umero de solu-
ciones que tenga: una soluci´on, ninguna soluci´on, exactamente 5 soluciones.
2

<!-- página 3 -->

Grupo y Teor´ıa de la Codificaci´on
1. Sea G = R∗ × R, y la operaci´on ⊙ definida entre elementos de G por
(a, b) ⊙ (x, y) = (ax, bx + y). Probar que (G, ⊙) es un grupo abeliano.
2. Hallar todos los subgrupos de (Z20, +).
3. Dado el grupo multiplicativo (U12, ·):
a. Realizar la tabla para ·.
b. Hallar el neutro y los inversos multiplicativos de cada elementos.
c. Determinar todos los subgrupos.
d. Determinar el orden de cada elemento de U12.
e. ¿Con qui´en puede establecer un isomorfismo de grupos al grupo multiplicativo U12?
4. Sea Z∗ 8 un grupo multiplicativo c´ıclico, buscar un generador (g) del grupo y resolver la ecua-
ci´on logar´ıtmica discreta: logg(5) = n.
5. Considerar el grupo multiplicativo de las unidades U18
a. Hallar el inverso de cada elemento.
b. ¿Es U18 c´ıclico?
c. Sea H =< 13 >, qu´e elementos tiene H, qu´e orden tienen el elemento 13?
d. Calcular φ(18). ¿C´omo interpreta esta cantidad?
6. Considerar el grupo (Z × Z = G; + : ”suma usual de pares ordenados”) y f : G → (Z, +),
definida por f (x; y) = x − 3y.
a. Probar que f es un homomorfismo de grupos y que f es sobreyectiva. ¿Es f inyectiva?
b. Hallar ker f = {(x, y)/ f (x, y) = 0} (como conjunto de pares ordenados).
7. Sea E : Z2 2 → Z6 2 una funci´on de codificaci´on definida como: E(00) = 000000, E(01) = 011001,
E(10) = 100110, E(11) = 111111.
a. Escriba los elementos de la siguiente esfera S(E(01) = 011001, 1).
Concluya: la esfera cuenta con exactamente 7 palabras (la original + 6 vecinas). Si al trans-
mitir 011001 ocurre un error en el canal de transmisi´on y llega, por ejemplo, 010001, el
decodificador ver´a que este vector cae dentro de la esfera de 011001 y lo corregir´a au-
tom´aticamente.
b. Calcular la distancia m´ınima entre las palabras codificadas.
c. Completar la Tabla: (C: conjunto de palabras codificadas, +)
+ (en Z2) 000000 011001 100110 111111
000000 011001
011001
100110 111111 000000 011001
111111 000000
c. Justificar por qu´e es un grupo.
3

<!-- página 4 -->

d. Comprobar que la distancia m´ınima es igual al peso m´ınimo de cada palabra codificada
diferente del cero del grupo.
e. Reconstruir la matriz G (2x6) generadora de este conjunto de palabras codificadas, de este
c´odigo.
8. Demostrar que el grupo aditivo (Z4, +) y el grupo multiplicativo (Z∗ 5, ·) son isomorfos.
9. Probar que 1 y 5 son generadores del grupo c´ıclico finito (Z6, +).
10. La siguiente tabla da la operaci´on binaria para un grupo (G, ∗):
∗ e a b c d f
e e a b c d f
a a b e d f c
b b e a f c d
c c f d e b a
d d c f a e b
f f d c b a e
a. Dar la lista de los elementos del subgrupo generado por ⟨a⟩.
b. Mostrar que ⟨a⟩ ∗ c = c ∗ ⟨a⟩.
c. Determinar todas las clases laterales de ⟨d⟩.
11. La matriz Generadora del C´odigo para la funci´on de codificaci´on E : Z3 2 → Z6 2 es
G =
⎛
⎝
1 0 0 1 0 1
0 1 0 1 1 0
0 0 1 0 1 1
⎞
⎠:
a. Hallar el conjunto C de palabras codificadas.
b. Calcular la distancia m´ınima entre palabras y hacer un comentario sobre la capacidad de
detecci´on y correcci´on de errores.
c. Decodificar las palabras recibidas: r1 = 111011 y r2 = 000111.
4
