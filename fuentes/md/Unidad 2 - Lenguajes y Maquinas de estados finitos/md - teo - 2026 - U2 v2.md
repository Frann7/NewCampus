# md - teo - 2026 - U2 v2

Fuente: `C:/Users/Administrator/Downloads/MATDISCRETA/Catedra/Unidad 2 - Lenguajes y Maquinas de estados finitos/md - teo - 2026 - U2 v2.pdf` · 44 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Matem´atica Discreta
Licenciatura en Sistemas de Informaci´on
Docentes
Vaira, Stella - Fedonczuk, Miguel
Colliard, David - Cottonaro, Mariana - Froloff, B´arbara
FCyT - UADER
2026

<!-- página 2 -->

Unidad 2: Lenguaje – M´aquinas de estados finitos.
Lenguajes: Introducci´on. Definiciones. Teor´ıa de conjuntos de las cade-
nas. M´aquinas de estados finitos.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 2 / 35

<!-- página 3 -->

Las sucesiones de s´ımbolos, o caracteres, tienen un papel clave en el
procesamiento de informaci´on en una computadora. Como los progra-
mas puede representarse en t´erminos de sucesiones finitas de caracte-
res, se necesita alguna forma algebr´aica para manejar tales sucesiones
finitas, tambi´en llamadas cadenas, palabras o enunciados.
Alfabeto
El s´ımbolo Σ representa a un conjunto de s´ımbolos finitos no vac´ıo, que
llamaremos alfabeto.
Ejemplo 1
Σ = {0,1} Σ = {a,b,c,d,e} Σ = {0,1,α,β,],),a,t,×}
Se descartan los alfabetos del tipo: Σ = {a,b,c,aab,ca}
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 3 / 35

<!-- página 4 -->

Potencia de Σ
Si Σ es un alfabeto y n∈ Z+, definimos las potencia de Σ recursivamente
de la siguiente manera:
Σ1 = Σ, y Σn+1 = {xy/x∈ Σ,y ∈ Σn}, donde xy denota la yuxtaposici´on
de x e y.
Ejemplo 2
Dado Σ = {0,1}, hallar: Σ2 y Σ3
Σ2 =
Σ3 =
En general, para todo entero positivo n, se verifica que |Σn| = |Σ|n, ya que
estamos trabajando con disposiciones (de tama˜no n) con reposici´on.
Ejemplo 3
Dado Σ = {a,b,c,d,e}, ¿cu´antos elementos tiene Σ3? Mostrar algunos.
|Σ3| =
Algunos de sus elementos son:
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 4 / 35

<!-- página 5 -->

Cadena vac´ıa
Para cualquier alfabeto Σ definimos Σ0 = {λ}, donde λ denota la cadena
vac´ıa, es decir, la cadena que no consta de ning ´un s´ımbolo tomado de
Σ. Su cardinal,

Σ0

 = |{λ}| = 1.
Observaciones:
• El s´ımbolo λ nunca es un elemento de nuestro alfabeto Σ
•{λ} ⊈ Σ ya que λ < Σ
•{λ} , ∅ ya que |{λ}| = 1 , 0 = |∅|
(La cadena es vac´ıa, no el conjunto que la incluye)
Σ+ y Σ∗
Si Σ es cualquier alfabeto, entonces
Σ+ = S∞ n=1 Σn = S n∈Z+ Σn, y Σ∗ = S∞ n=0 Σn
Observe que la ´unica diferencia entre Σ+ y Σ∗ es el elemento λ, con lo
cual
Σ∗ = Σ+ ∪ Σ0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 5 / 35

<!-- página 6 -->

Sean w1,w2 ∈ Σ+, por lo tanto, w1 = x1x2...xm y w2 = y1y2...yn, para
m,n∈ Z+, con x1,x2,...,xm,y1,y2,...,yn ∈ Σ; se definen:
Cadenas iguales
Decimos que las cadenas w1 y w2 son iguales, y escribimos w1 = w2 si
m = n, y xi = yi, para todo 1 ≤i≤m.
Longitud de una cadena
La longitud de w1, que se denota como ∥w1 ∥, como el valor m.
Para el caso de λ: ∥λ∥= 0.
Concatenaci´on de cadenas
La concatenaci´on de w1 y w2, denotada como w1w2, es la cadena
x1x2...xmy1y2...yn.
La concatenaci´on con λ ser´a: w1λ = w1, λw1 = w1 y λλ = λ.
Para w1,w2 ∈ Σ∗: ||w1w2|| = ||w1|| + ||w2||.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 6 / 35

<!-- página 7 -->

Potencia de x
Para cualquier x∈ Σ∗, definimos las potencias de x como x0 = λ, x1 = x,
x2 = xx, x3 = xx2,...,xn+1 = xxn,..., donde n∈ N.
Ejemplo 4
Sea Σ = {0,1} y x = 10, hallar x0, x2, x5, ∥x3 ∥, ∥x7 ∥, y una regla general
para, ∥xn ∥, ∀n∈ N.
• x0 =
• x2 =
• x5 =
•∥x3 ∥=
•∥x7 ∥=
•∀n∈ N: ∥xn ∥=
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 7 / 35

<!-- página 8 -->

Prefijo y sufijo
Si x,y∈ Σ∗ y w = xy, entonces:
• La cadena x es un prefijo de w (prefijo propio si y , λ).
• La cadena y es un sufijo de w (sufijo propio si x , λ)
Ejemplo 5
Para w = 0100110, listar todos los prefijos, prefijos propios, sufijos y
sufijos propios.
prefijos:
p. propios:
sufijos:
s. propios:
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 8 / 35

<!-- página 9 -->

Subcadena
Si x,y,z∈ Σ∗ y w = xyz, entonces y es una subcadena de w. Cuando x o z
es diferente a λ (de modo que y es diferente de w), y es una subcadena
propia.
En otras palabras, si una subcadena es propia no es igual a la misma ca-
dena. Lo mismo ocurre para prefijo propio y sufijo propio, no pueden
ser iguales a la cadena dada.
Ejemplo 6
Para w = 0100110, listar cuatro subcadenas propias.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 9 / 35

<!-- página 10 -->

Lenguaje
Para un alfabeto dado Σ, cualquier subconjunto de Σ∗ es un lenguaje so-
bre Σ. Esto incluye al subconjunto ∅, al que llamaremos lenguaje vac´ıo.
Concatenaci´on de lenguajes
Para un alfabeto Σ y los lenguajes A,B⊆ Σ∗, la concatenaci´on de A y B,
se denota con AB, y es {ab/a∈A,b∈B}.
Ejemplo 7
Sea Σ = {x,y,z}, y los lenguajes A = {x,xy,z}, B = {λ,y}. Hallar AB, BA, y
verificar que |AB| , |BA| y |AB| , |A||B|.
AB =
BA =
|AB| , |BA| porque
|AB| , |A||B| porque
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 10 / 35

<!-- página 11 -->

Teorema
Para un alfabeto Σ y A,B,C⊆ Σ∗ se verifica:
• A{λ} = {λ}A = A • (AB)C = A(BC)
• A(B∪C) = AB∪AC • (B∪C)A = BA∪CA
• A(B∩C) ⊆AB∩AC • (B∩C)A⊆BA∩CA
Para cualquier lenguaje A⊆ Σ∗ podemos construir otros lenguajes de la
manera siguiente:
• A0 = {λ}, A1 = A y ∀n∈ Z+: An+1 = {ab/a∈A,b∈An}
• A+ = S n∈Z+ An (Clausura positiva de A)
• A∗ = A+ ∪{λ} (Clausura de Kleene)
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 11 / 35

<!-- página 12 -->

Descripci´on de los elementos de un lenguaje
Ejemplo 8
Sea Σ = {x,y}
• Si A = {xx,xy,yx,yy}, entonces A∗ es el lenguaje de todas las cade-
nas w∈ Σ∗ de longitud par.
• Con A de la primera parte, y B = {x,y}, el lenguaje BA∗ contiene
todas las cadenas de Σ∗ de longitud impar.
• El lenguaje {x}{x,y}∗ contiene cada cadena de Σ∗ para la cual x es
un prefijo.
• El lenguaje {x,y}+{yy} contiene todas las cadenas de Σ∗ para la cual
yy es un sufijo propio.
• Cada cadenas del lenguaje {x,y}∗{xxy}{x,y}∗ tiene a xxy como sub-
cadena.
• Cualquier cadena de {x}∗{y}∗ consta de λ y de todas las cadenas con
un n ´umero finito de x seguido de un n ´umero finito de y.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 12 / 35

<!-- página 13 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 6, apartado
6.1 (P´agina 325 ) del libro Matem´atica Discreta de Ralph Grimaldi que se
encuentra en el campus virtual:
1 1 al 10
2 12 al 14
3 22 al 24
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 13 / 35

<!-- página 14 -->

M ´AQUINAS DE ESTADOS FINITOS
Funcionamiento de una m´aquina - Un ejemplo sencillo.
Supongamos que una m´aquina expendedora tiene dos tipos de produc-
tos A y B. El precio de cada producto es de 10 centavos de d´olar. La
m´aquina admite ´unicamente monedas de 5 y 10 centavos y devuelve el
cambio necesario. Dispone de un bot´on rojo que expide el producto A
y uno verde que hace lo mismo con el producto B.
La m´aquina est´a en un estado de espera (estado s0), hasta que un cliente
comience a insertar monedas por un total de 10 centavos o m´as, y opri-
ma el bot´on para obtener el producto deseado. Si en cualquier momento
del proceso, el total de monedas insertadas supera los diez centavos, la
m´aquina devuelve el cambio necesario antes de que el cliente oprima
el bot´on correspondiente.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 14 / 35

<!-- página 15 -->

Ulises para comprar el producto A, introdujo consecutivamente dos
monedas de 5c. Luego apret´o el bot´on rojo y obtuvo el producto de-
seado.
Representemos el proceso con una tabla, donde t0 es el instante inicial
cuando inserta su primera moneda y ti con i = 1,2,3 son los instantes
posteriores:
Input → t0 t1 t2 t3
Estado s0 s1 s2 s0
Entrada 5 5 R –
Salida nada nada A –
En el instante t0, Ulises inserta su primera moneda de 5c. No recibe
nada pero en el instante siguiente t1 la m´aquina est´a en el estado s1
(tiene almacenados 5c). En este instante t1, la m´aquina no devuelve
nada pero, al depositar una nueva moneda de 5c, en el instante t2 la
m´aquina se encuentra en un nuevo estado s2 (tiene almacenados 10c).
Ulises todav´ıa no recibe nada puesto que la m´aquina no sabe que tipo
de producto quiere. Al oprimir el bot´on rojo en el instante t2, la m´aqui-
na expide el producto A y en el instante siguiente t3 se coloca de nuevo
en el estado inicial s0 (ning ´un centavo almacenado).

<!-- página 16 -->

La siguiente tabla resume qu´e hace la m´aquina que utiliza Ulises en
cada estado, c´omo responde a las entradas, y a qu´e estado cambia y qu´e
salida produce:
Estados
Transici´on Salida
Entrada Entrada
5 10 R V 5 10 R V
s0 s1 s2 s0 s0 n n n n
s1 s2 s2 s1 s1 n 5 n n
s2 s2 s2 s0 s0 5 10 A B
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 16 / 35

<!-- página 17 -->

M ´AQUINAS DE ESTADOS FINITOS
Funcionamiento de una m´aquina expendedora de chicles en blister:
• Posee dos tipos de chicles: Menta (M) y Fruta (F).
• El costo de cada uno es 20 centavos de dolar.
• La m´aquina acepta monedas de 5, 10 y 25 centavos; y devuelve el
cambio.
• Posee dos botones que se presionan luego de insertar las monedas:
BM y BF, para obtener M y F, respectivamente.
Representaci´on del funcionamiento de la m´aquina expendedora
Siguiente estado Salida
Input → 5c 10c 25c BM BF 5c 10c 25c BM BF
Posee 0c (s0)
Posee 5c (s1)
Posee 10c (s2)
Posee 15c (s3)
Posee 20c (s4)
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 17 / 35

<!-- página 18 -->

M ´AQUINAS DE ESTADOS FINITOS
Completar la tabla
• Posee dos tipos de chicles: Menta (M) y Fruta (F).
• El costo de cada uno es 20 centavos de dolar.
• La m´aquina acepta monedas de 5, 10 y 25 centavos; y devuelve el
cambio.
• Posee dos botones que se presionan luego de insertar las monedas:
BM y BF, para obtener M y F, respectivamente.
Siguiente estado Salida
Input → 5c 10c 25c BM BF 5c 10c 25c BM BF
Posee 0c (s0) s2 s4 s0 n 5c n
Posee 5c (s1) s3 s1 s1 10c n
Posee 10c (s2) s4 s2 n n
Posee 15c (s3) s4 s3 n 5c n
Posee 20c (s4) s0 s0 5c 10c F
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 18 / 35

<!-- página 19 -->

Principales caracter´ısticas de una m´aquina como la expendedora del
ejemplo anterior
1 Cantidad finita de estados (estados internos). En un instante dado,
la memoria total disponible de la m´aquina es el conocimiento del
estado interno en el que se encuentra en ese instante.
2 N ´umero finito de s´ımbolos de entrada, que se conocen como el al-
fabeto de entrada I
3 Por cada combinaci´on de entradas y estados internos se determina
una salida y un estado siguiente. El conjunto finito de todas las sali-
das posibles constituyen el alfabeto de salida O de la m´aquina.
4 Suponemos que los procesos secuenciales est´an sincronizados por
pulso de reloj separados y distintos y que la m´aquina opera de ma-
nera determin´ıstica. La salida queda determinada por el estado ini-
cial y la secuencia de entrada.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 19 / 35

<!-- página 20 -->

M´aquinas de estados finitos
Una m´aquina de estados finitos es una 5-upla M = (S,I,O,ν,ω), donde
S es el conjunto de estados internos de M; I es el alfabeto de entrada de
M; O es el alfabeto de salida de M; ν : S×I→S es la funci´on siguiente
estado; y ω : S×I→O es la funci´on de salida.
Ejemplo 10
Para el ejemplo de la m´aquina expendedora de chicles, determinar los
elementos S, I y O, y mostrar dos elementos de cada una de las funcio-
nes ν y ω.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 20 / 35

<!-- página 21 -->

Ejemplo 11
Un sumador binario en serie es una m´aquina de estados finitos que podemos usar para obterner
x + y, donde x e y seran dos cadenas binarias de igual longitud, y garanticen el espacio suficiente
para completar la suma.
As´ı, si x = x5x4x3x2x1 = 00111 e y = y5y4y3y2y1 = 01101
Observe que x1 = y1 = 1 y z1 = 0, mientras que x3 = y3 = 1 pero z3 = 1 por el acarreo de la suma
de x2 +y2. Por lo tanto la salida depende de la suma de dos entradas y de la habilidad de recordar
un acarreo de 0 o 1.
Determinar los elementos S, I y O, y mostrar dos elementos de cada una de las funciones ν y ω.
Luego completar la tabla de estados.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 21 / 35

<!-- página 22 -->

Otra forma de representar a las m´aquinas de estados finitos es un dia-
gramas de estados.
Se representa mediante un c´ırculo con s dentro de ´el. Para representar
la transici´on de si a sj utilizamos una arista dirigida (o arco) como se
puede ver en la figura siguiente, donde ∀x∈I y ∀y∈O:
ν(si,x) = sj ω(si,x) = y
si sj
x,y
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 22 / 35

<!-- página 23 -->

Ejemplo 12
Considere la m´aquina de estados finitos M = (S,I,O,ν,ω), donde S =
{s0,s1,s2}, I = O = {0,1}. A partir de su representaci´on en diagramas de
estado, realizar la tabla.
s0start s1 s2
0,0
1,0
1,0
0,0
1,1
0,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 23 / 35

<!-- página 24 -->

Ejemplo 13
El diagrama de estados para la m´aquina de estados finitos del sumador
binario en series anteriormente es.
ν ω
00 01 10 11 00 01 10 11
s0 s0 s0 s0 s1 0 1 1 0
s1 s0 s1 s1 s1 1 0 0 1
s0start s1
00,0
01,1
10,1
11,0
01,0
10,0
11,1
00,1
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 24 / 35

<!-- página 25 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 6, apartado
6.2 (P´agina 333 ) del libro Matem´atica Discreta de Ralph Grimaldi que se
encuentra en el campus virtual: 1, 2, 3, 5, 6, 7, 8, 9.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 25 / 35

<!-- página 26 -->

Ejemplo 14
Dados I = O = {0,1}, la siguiente m´aquina de estados finitos reconoce cada
aparici´on de la secuencia 111 al encontrarla en cualquier cadena de entrada
x∈I∗.
Por ejemplo, si x = 1110101111, su salida correspondiente debe ser 0010000011.
En otras palabras, esta m´aquina es un reconocedor del lenguaje A = {0,1}∗{111}.
Como se puede observar, esta m´aquina permite solapamiento.
s0start
s1
s2
0,0
1,0
0,0
1,0
0,0 1,1
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 26 / 35

<!-- página 27 -->

Ejemplo 14
Dados I = O = {0,1}, la siguiente m´aquina de estados finitos reconoce cada
aparici´on de la secuencia 111 al encontrarla en cualquier cadena de entrada
x∈I∗.
Por ejemplo, si x = 1110101111, su salida correspondiente debe ser 0010000011.
En otras palabras, esta m´aquina es un reconocedor del lenguaje A = {0,1}∗{111}.
Como se puede observar, esta m´aquina permite solapamiento.
s0start
s1
s2
0,0
1,0
0,0
1,0
0,0 1,1
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 26 / 35

<!-- página 28 -->

Ejemplo 14
Dados I = O = {0,1}, la siguiente m´aquina de estados finitos reconoce cada
aparici´on de la secuencia 111 al encontrarla en cualquier cadena de entrada
x∈I∗.
Por ejemplo, si x = 1110101111, su salida correspondiente debe ser 0010000011.
En otras palabras, esta m´aquina es un reconocedor del lenguaje A = {0,1}∗{111}.
Como se puede observar, esta m´aquina permite solapamiento.
s0start
s1
s2
0,0
1,0
0,0
1,0
0,0 1,1
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 26 / 35

<!-- página 29 -->

Ejemplo 14
Dados I = O = {0,1}, la siguiente m´aquina de estados finitos reconoce cada
aparici´on de la secuencia 111 al encontrarla en cualquier cadena de entrada
x∈I∗.
Por ejemplo, si x = 1110101111, su salida correspondiente debe ser 0010000011.
En otras palabras, esta m´aquina es un reconocedor del lenguaje A = {0,1}∗{111}.
Como se puede observar, esta m´aquina permite solapamiento.
s0start
s1
s2
0,0
1,0
0,0
1,0
0,0 1,1
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 26 / 35

<!-- página 30 -->

Ejemplo 15
La siguiente m´aquina de estados finitos reconoce la ocurrencia de la
secuencia 111 pero solamente en la posiciones m ´ultiplo de tres (3k-
´esima). Por ejemplo, si x = 111100111, su salida correspondiente debe
ser 001000001.
s0start s1 s2
s3 s4
1,0 1,0
1,1
1,0
0,0
1,0
0,0
0,0
1,1
0,0
1,0
0,0
1,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 27 / 35

<!-- página 31 -->

Ejemplo 15
La siguiente m´aquina de estados finitos reconoce la ocurrencia de la
secuencia 111 pero solamente en la posiciones m ´ultiplo de tres (3k-
´esima). Por ejemplo, si x = 111100111, su salida correspondiente debe
ser 001000001.
s0start s1 s2
s3 s4
1,0 1,0
1,1
1,0
0,0
1,0
0,0
0,0
1,1
0,0
1,0
0,0
1,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 27 / 35

<!-- página 32 -->

Ejemplo 15
La siguiente m´aquina de estados finitos reconoce la ocurrencia de la
secuencia 111 pero solamente en la posiciones m ´ultiplo de tres (3k-
´esima). Por ejemplo, si x = 111100111, su salida correspondiente debe
ser 001000001.
s0start s1 s2
s3 s4
1,0 1,0
1,1
1,0
0,0
1,0
0,0
0,0
1,1
0,0
1,0
0,0
1,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 27 / 35

<!-- página 33 -->

Ejemplo 15
La siguiente m´aquina de estados finitos reconoce la ocurrencia de la
secuencia 111 pero solamente en la posiciones m ´ultiplo de tres (3k-
´esima). Por ejemplo, si x = 111100111, su salida correspondiente debe
ser 001000001.
s0start s1 s2
s3 s4
1,0 1,0
1,1
1,0
0,0
1,0
0,0
0,0
1,1
0,0
1,0
0,0
1,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 27 / 35

<!-- página 34 -->

Ejemplo 15
La siguiente m´aquina de estados finitos reconoce la ocurrencia de la
secuencia 111 pero solamente en la posiciones m ´ultiplo de tres (3k-
´esima). Por ejemplo, si x = 111100111, su salida correspondiente debe
ser 001000001.
s0start s1 s2
s3 s4
1,0 1,0
1,1
1,0
0,0
1,0
0,0
0,0
1,1
0,0
1,0
0,0
1,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 27 / 35

<!-- página 35 -->

Ejemplo 15
La siguiente m´aquina de estados finitos reconoce la ocurrencia de la
secuencia 111 pero solamente en la posiciones m ´ultiplo de tres (3k-
´esima). Por ejemplo, si x = 111100111, su salida correspondiente debe
ser 001000001.
s0start s1 s2
s3 s4
1,0 1,0
1,1
1,0
0,0
1,0
0,0
0,0
1,1
0,0
1,0
0,0
1,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 27 / 35

<!-- página 36 -->

Ejemplo 15
La siguiente m´aquina de estados finitos reconoce la ocurrencia de la
secuencia 111 pero solamente en la posiciones m ´ultiplo de tres (3k-
´esima). Por ejemplo, si x = 111100111, su salida correspondiente debe
ser 001000001.
s0start s1 s2
s3 s4
1,0 1,0
1,1
1,0
0,0
1,0
0,0
0,0
1,1
0,0
1,0
0,0
1,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 27 / 35

<!-- página 37 -->

Ejemplo 16
Dados I = O = {0,1}, construir dos m´aquinas de estados finitos que
reconozcan la ocurrencia de la cadena de entrada 0101: (a) sin im-
portar d´onde ocurra, (b) en la posici´on 4k-´esima. Hallar para ambas,
ν(s0,01010100101) y ω(s0,01010100101)
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 28 / 35

<!-- página 38 -->

Ejemplo 17
Dados I = O = {0,1}, construir una m´aquina de estados finitos que re-
conozca solamente a todas las cadenas del lenguaje {00}{0,1}∗{111}
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 29 / 35

<!-- página 39 -->

Ejemplo 18
La siguiente m´aquina de estados finitos se conoce como m´aquina de re-
tardo unitario, ya que su prop´osito es retardar la salida del elemento de
la entrada en una posici´on. Por ejemplo, ω(s0,011100) = 001110.
s0start
s1
s2
0,0
1,0
1,0
0,0
0,1
1,1
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 30 / 35

<!-- página 40 -->

Ejemplo 19
Completar la siguiente m´aquina de estados finitos, la cual retarda la
salida del elemento de la entrada en dos posiciones.
Por ejemplo, ω(s0,0110100) = 0001101.
s0start
s1
s2
s3
s4
s5
s6
0,0
1,0
0,0
1,0
0,0
1,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 31 / 35

<!-- página 41 -->

Definiciones 1
Sea M = (S,I,O,ν,ω) una m´aquina de estados finitos.
• Para si,sj ∈S, se dice que sj se puede alcanzar desde si si si = sj o si
existe una entrada x∈I tal que ν(si,x) = sj.
• Un estado s∈S es transitorio si ν(s,x) = s para x∈I∗ implica x = λ;
es decir, no existe x∈I + tal que ν(s,x) = s.
• Un estado s∈S es estado sumidero, si ν(s,x) = s, para x∈I∗.
Ejemplo 20
s0 es transitorio s2 es sumidero
s0start s1 s2 1,0 0,0
0,0
1,0
1,1
0,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 32 / 35

<!-- página 42 -->

Definiciones 2
Sea M = (S,I,O,ν,ω) una m´aquina de estados finitos.
• Sea S1 ⊆S,I1 ⊆I. Si ν1 = ν|S1×I1 : S1 ×I1 →S1, con ω1 = ω|S1×I1 ,
entonces M1 = (S1,I1,O1,ν1,ω1) es una subm´aquina de M.
• Una m´aquina es fuertemente conexa si para cualquier estado si,sj ∈
S, podemos alcanzar sj desde si.
Ejemplo 21
M1 = (S1,I1,O1,ν1,ω1) con S1 = {s1,s2} es una subm´aquina de M, aun-
que no fuertemente conexa ya que no se puede alcanzar s1 desde s2.
s0start s1 s2 1,0 0,0
0,0
1,0
1,1
0,0
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 33 / 35

<!-- página 43 -->

Ejemplo 22
La m´aquina de retardo 2 posee una subm´aquina fuertemente conexa:
M1 = (S1,I1,O1,ν1,ω1) con S1 = {s3,s4,s5,s6}.
Los estados s0, s1 y s2 son transitorios.
No posee estados sumideros.
s0start
s1
s2
s3
s4
s5
s6
0,0
1,0
0,0
1,0
0,0
1,0
0,0
1,0
0,0
1,0
0,1
1,1
1,1
0,1
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 34 / 35

<!-- página 44 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 6, apartado
6.3 (P´agina 342 ) del libro Matem´atica Discreta de Ralph Grimaldi que se
encuentra en el campus virtual: 1, 2, 3, 5, 7.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 35 / 35
