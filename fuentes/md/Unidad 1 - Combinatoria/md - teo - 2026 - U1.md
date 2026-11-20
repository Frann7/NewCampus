# md - teo - 2026 - U1

Fuente: `C:/Users/Administrator/Downloads/MATDISCRETA/Catedra/Unidad 1 - Combinatoria/md - teo - 2026 - U1.pdf` · 43 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Matem´atica Discreta
Licenciatura en Sistemas de Informaci´on
Docentes
Vaira, Stella - Fedonczuk, Miguel
Colliard, David - Cottonaro, Mariana - Froloff, B´arbara
FCyT - UADER
2026

<!-- página 2 -->

Unidad 1: Combinatoria.
Principios fundamentales del conteo: principio de multiplicaci´on y de
la suma. Concepto de factorial. Permutaciones. Permutaciones con re-
petici´on. Combinaciones. Combinaciones con repetici´on: distribucio-
nes. Teoremas fundamentales. Propiedades. Aplicaciones.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 2 / 1

<!-- página 3 -->

Principio de multiplicaci´on
Si una actividad se puede construir en t pasos sucesivos y el paso 1 se
puede hacer de n1 maneras, el paso 2 se puede realizar de n2 maneras,
..., y el paso t de nt maneras, entonces el n ´umero de actividades posibles
diferentes es n1 · n2 ··· nt .
paso1forma1
p2f1
p3f1 p3f2
p2f2
p3f1 p3f2
p2f3
p3f1 p3f2
paso1forma2
p2f1
p3f1 p3f2
p2f2
p3f1 p3f2
p2f3
p3f1 p3f2
Paso 1: dos formas (n1 = 2)
Paso 2: tres formas (n2 = 3)
Paso 3: dos formas (n3 = 2)
Total de formas de realizar la actividad: 2 · 3 · 2 = 12
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 3 / 1

<!-- página 4 -->

Caso particular: Si una actividad/evento A se puede realizar de m for-
mas diferentes y luego se puede realizar otra actividad/evento B de n
formas diferentes, el n ´umero total de formas en que pueden ocurrir A
y B es igual a m · n. Es decir, ambos eventos se realizan, primero uno y
luego el otro. El ≪y≫ indica multiplicaci´on.
Ejemplo 1
Un club de teatro realiza ensayos para una obra. Si cuatro hombres y
tres mujeres ensayan para los papeles principales (masculino y feme-
nino), ¿de cu´antas formas el director puede elegir a la pareja principal?
Realizar el diagrama de ´arbol correspondiente y verificar el principio
de la multiplicaci´on.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 4 / 1

<!-- página 5 -->

Ejemplo 2
Bajo las siguientes condiciones, se desea saber cu´antas placas patentes
diferentes de autom´oviles se pueden fabricar que consten de dos letras
seguidas por tres d´ıgitos y luego dos letras m´as (LLDDDLL), si
1 ninguna letra o d´ıgito se puede repetir
2 se permite repetir las letras y los d´ıgitos
3 con repetici´on, s´olo usando vocales y los d´ıgitos pares.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 5 / 1

<!-- página 6 -->

Principio de la suma
Suponga que X1, ..., Xt son conjuntos y que el i-´esimo conjunto Xi tiene
ni elementos. Si {X1, ..., Xt } es una familia de conjuntos disjuntos por
pares (es decir, si i , j, Xi ∩ Xj = ∅), el n ´umero de elementos posibles
que se pueden seleccionar de X1 o X2 o ... o Xt es
n1 + n2 + ··· + nt
(De manera equivalente, la uni´on X1 ∪ X2 ∪ ... ∪ Xt contiene n1 + n2 + ··· + nt elementos)
Es decir, para el caso de X1 y X2, si una primera tarea puede realizarse
de n1 formas distintas, mientras que una segunda tarea puede realizar-
se de n2 formas distintas, y no es posible realizar ambas tareas de mane-
ra simult´anea, entonces, para llevar a cabo cualquiera de ellas pueden
realizarse cualquiera de n1 + n2 formas distintas.
Esta idea es generalizable para t tareas.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 6 / 1

<!-- página 7 -->

Ejemplo 1
¿De cu´antas formas se puede seleccionar un libro distinto entre 30 li-
bros de Programaci´on en Python y 25 libros de Matem´atica Discreta?
Ejemplo 2
Durante las elecciones primarias argentinas, tambi´en llamadas PASO
(Primarias, Abiertas, Simult´aneas y Obligatorias) se presentan como
candidatos a presidente nueve candidatos del partido A y cinco del par-
tido B.
1 Si el presidente va a ser alguno de estos candidatos, ¿cu´antas posi-
bilidades hay para el posible ganador?
2 ¿Cu´antas posibilidades hay para que una pareja de candidatos (uno
de cada partido) se opongan entre s´ı en la elecci´on final?
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 7 / 1

<!-- página 8 -->

Ejemplo 3
Toyota posee una planta de fabricaci´on en la cual puede producir 5
modelos diferentes (Yaris, Corolla, Etios, SW4 y Hilux), 6 colores, 3 ta-
ma˜nos de motor y 2 tipos de transmisi´on.
1 ¿Cu´antos autos distintos se pueden fabricar en esa planta?
2 ¿Cu´antas variantes de una Hilux con el motor mas potente se pue-
den fabricar?
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 8 / 1

<!-- página 9 -->

Ejemplo 4
Un laboratorio de investigaci´on tiene 12 miembros. De entre los cua-
les, en las pr´oximas elecciones, se deben renovar los cargos de director,
vicedirector, secretario y tesorero. Calcular la cantidad de formas de
realizar la selecci´on.
Supongamos ahora que de sus 12 miembros, 4 son ingenieros. ¿Cu´antos
selecciones del inciso anterior se pueden formar bajo las siguientes con-
diciones?
1 Con un tesorero que sea un ingeniero.
2 Con dos ingenieros exactamente en la lista.
3 Con al menos un ingeniero en la lista.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 9 / 1

<!-- página 10 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 6, apartado
6.1 (P´agina 226 ) del libro Matem´aticas Discretas de Johsonbaugh que se
encuentra en el campus virtual:
1 1 al 4
2 6
3 8 al 16
4 17 al 19
5 21 al 28
6 32 al 41
7 54 al 60
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 10 / 1

<!-- página 11 -->

Permutaci´on
Una permutaci´on de n elementos diferentes x1, x2, ..., xn es un ordenamien-
to de los n elementos x1, x2, ..., xn.
Si queremos permutar las letras a, b, c hay 3 · 2 · 1 = 6 formas posibles:
abc, acb, bac, bca, cab, cba
Factorial de un n ´umero
Para un entero n ≥ 0, n factorial (que se denota con n!) se define como
0! = 1,
n! = n · (n − 1) · (n − 2)···3 · 2 · 1, ∀n ∈ Z+
As´ı, por ejemplo, el problema anterior se puede calcular como
3! = 3 · 2 · 1 = 6
Nota: Esta operaci´on est´a disponible en la calculadora mediante la tecla [x!].
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 11 / 1

<!-- página 12 -->

Teorema
Existen n! permutaciones de n elementos.
Por lo que si queremos permutar 10 elementos, la cantidad de formas
que lo podemos hacer es 10! = 3628800
Una propiedad que vamos a utilizar durante los c´alculos es la posibili-
dad de asociar alguno de los primeros factores del factorial:
n! = n · (n − 1) · (n − 2)···(n − i + 1) · (n − i)!
Por ejemplo:
10! = 10 · 9 · 8 · 7· 6 · 5 · 4 · 3 · 2 · 1
10! = 10 · 9 · 8 · 7· 6!
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 12 / 1

<!-- página 13 -->

Ejemplo 1
Sof´ıa trabaja como encargada de la gesti´on de pedidos en una tienda
de electrodom´esticos. Una tarde, ella observa que durante el d´ıa se han
recibido 15 pedidos para su preparaci´on. ¿De cu´antas formas puede
ordenar la preparaci´on de esos pedidos si
1 no existe restricciones?
2 Sof´ıa considera que 6 de los pedidos no son urgentes y desea pro-
cesarlos al final?
3 primero los separa teniendo en cuenta cu´ando se van a retirar: 3
por la ma˜nana, 7 por la tarde y 5 antes de cerrar el local; y luego
los procesa en ese orden de retiro.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 13 / 1

<!-- página 14 -->

Ejemplo 2
Se tienen 9 carteles: ⇒ ⇒ ⇒ ⇒ ⇒ 3 6 4 1
¿De cu´antas formas es posible realizar un camino si las flechas indican
un paso hacia la derecha y los n ´umeros indican pasos hacia abajo, sin
utilizar dos flechas consecutivas?
Ejemplo 3
Un profesor de ciencias de la computaci´on tiene cinco libros de Python
y seis de R, todos de diferentes autores. ¿De cu´antas formas se pueden
ordenar estos libros en una repisa si
1 no hay restricciones?
2 los lenguajes se deben alternar?
3 si todos los libros de R deben estar juntos?
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 14 / 1

<!-- página 15 -->

Algunas veces se desea permutar s´olo alguno de los elementos de un
conjunto, no la totalidad.
Permutaci´on de r en n
Una permutaci´on r de n elementos (distintos) x1, x2, ..., xn es un ordena-
miento de r elementos de {x1, x2, ..., xn}. El n ´umero de permutaciones r
de un conjunto de n elementos diferenties se denota por P (n, r).
Por ejemplo, si se desea armar las permutaciones de orden 2 a partir de
4 elementos distintos a, b, c, d
ab ca
ac cb
ad cd
ba da
bc db
bd dc
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 15 / 1

<!-- página 16 -->

Teorema
El n ´umero de permutaciones de r de un conjunto de n objetos diferentes
es
P (n, r) = n · (n − 1) · (n − 2)···(n − r + 1)
|                                {z                                }
r−veces
, ∀r ≤ n
Si utilizamos la notaci´on factorial:
n(n − 1)(n − 2)···(n − r + 1) · (n − r)(n − r − 1)···3 · 2 · 1 (n − r)(n − r − 1)···3 · 2 · 1 = n! (n − r)! = P (n, r)
As´ı, la cantidad de maneras de seleccionar el director, vicedirector, se-
cretario y tesorero de un grupo de 12 personas es
P (12, 4) = 12! (12 − 4)! = 12! 8! = 12 · 11 · 10 · 9 = 11880
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 16 / 1

<!-- página 17 -->

Ejemplo 1
Bajo las siguientes condiciones, se desea saber cu´antas permutaciones
en la palabra “murcielago” es posible hacer si
1 no se permiten repeticiones.
2 s´olo se utilizan tres de sus letras.
3 se permiten repeticiones y se desea calcular el n ´umero de secuen-
cias de 15 letras.
Ejemplo 2
En una fiesta de cumplea˜nos, la quincea˜nera desea sacarse una foto en
un sill´on con sus 10 amigos. Si en el sill´on s´olo hay lugar para 7 perso-
nas, ¿de cu´antas maneras diferentes puede hacerse la foto cambiando
la ubicaci´on de los amigos pero con la quincea˜nera en el medio?
´Estos ordenamientos reciben el nombre de disposiciones lineales
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 17 / 1

<!-- página 18 -->

Ejemplo 3
Si seis personas, designadas como A, B, ..., F, se sientan en torno de
una mesa redonda, ¿cu´antas disposiciones circulares diferentes son po-
sibles?
Respuesta
Las disposiciones se consideran iguales cuando una puede obtenerse de
otra mediante una rotaci´on. En la figura: (a) y (b) id´enticas - (b), (c) y
(d) distintas.
Por lo que si define: x : n ´umero de disposiciones circulares, y : n ´umero
de disposiciones lineales. As´ı 6 · x = y ⇐⇒ 6 · x = 6! ⇐⇒ x = 5! = 120
En general, la cantidad de disposiciones circulares de n objetos
distintos es (n − 1)!
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 18 / 1

<!-- página 19 -->

¿Qu´e ocurre si queremos seleccionar objetos de un conjunto sin que nos
importe el orden de selecci´on?
Combinaciones de n en r
Dado un conjunto X = {x1, x2, ..., xn} que contiene n elementos diferen-
tes,
1 Una combinaci´on r de X es una selecci´on no ordenada de r elemen-
tos de X (es decir, un subconjunto de X de r elementos).
2 El n ´umero de combinaciones r de un conjunto de n elementos dis-
tintos se denota por C(n, r),  n r  o Cn,r .
Supongamos que queremos seleccionar de entre los docentes Marta, Bel´en, Roc´ıo, Anal´ıa y Nahuel
un grupo de tres para que realicen una clase de consulta.
¿De cu´antas maneras pueden armarse dicho grupo?
Evidentemente no importa el orden de selecci´on, por lo cual, seleccionar a Marta, Anal´ıa y Nahuel,
es lo mismo que seleccionar a Anal´ıa, Nahuel y Marta.
Si listamos las posibilidades se ve que existen 10 maneras:
MBR, MBA, MRA, BRA, MBN , MRN , BRN , MAN , BAN , RAN , por lo que C(5, 3) = 10.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 19 / 1

<!-- página 20 -->

Si consideramos que por cada combinaci´on se pueden ordenar los ele-
mentos seleccionados, y de esta manera, obtener una permutaci´on de
dichos elementos, se tiene que P (n, r) = C(c, r) · r!
Teorema
El n ´umero de combinaciones r de de un conjuntos de n objetos distintos
es
C(n, r) = P (n, r) r! = n! r!(n − r)! , r ≤ n
Para el ejemplo anterior, la selecci´on de 3 docentes de un grupo de 5, se
puede calcular la cantidad de maneras diferentes de hacer dicha selec-
ci´on mediante
C(5, 3) = 5! 3!2! = 10
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 20 / 1

<!-- página 21 -->

Ejemplo 1
En el sistema Braille, un s´ımbolo, como una letra min ´uscula, un signo
de puntuaci´on, un sufijo, etc., se escribe resaltando al menos uno de los
puntos de la disposici´on de seis puntos que aparecen en la parte (a) de
la figura. En las partes b) a la g) se presentan algunos ejemplos.
1 ¿Cu´antos s´ımbolos diferentes podemos representar en el sistema
Braille?
2 ¿Cu´antos s´ımbolos tienen exactamente tres puntos en relieve?
3 ¿Cu´antos s´ımbolos tienen un n ´umero par de puntos en relieve?
4 ¿Cu´antos s´ımbolos tienen al menos cuatro puntos en relieve?
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 21 / 1

<!-- página 22 -->

Ejemplo 2
¿Cu´antos bytes contienen...
1 exactamente tres ceros?
2 un n ´umero par de unos?
3 al menos seis unos?
Ejemplo 3
¿De cu´antas formas un estudiante que realiza un examen puede res-
ponder
1 seis de quince preguntas?
2 tres de las primeras cinco y cuatro de las ´ultimas diez.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 22 / 1

<!-- página 23 -->

Ejemplo 4
Una empresa decide contratar a 12 personas, de entre 10 arquitectos y
8 dise˜nadores gr´aficos postulantes, para entrenar una IA. ¿De cu´antas
maneras se puede realizar la selecci´on si
1 no hay restricciones?
2 debe haber un n ´umero par de arquitectos?
3 debe haber m´as dise˜nadores que arquitectos?
4 debe haber al menos siete aquitectos?
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 23 / 1

<!-- página 24 -->

Ejemplo 5
Verificar y luego demostrar las siguientes propiedades:
1
 n
0
 = 1 2  n n  = 1 3  n 1  = n 4  n p  =   n n−p 
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 24 / 1

<!-- página 25 -->

Ejemplo 6
Resolver las siguientes ecuaciones:
1 P (n, 2) − P (n − 1, 2) = 100 2 6C(n, 2) = P (n + 1, 2) + 720
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 25 / 1

<!-- página 26 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 6, apartado
6.2 (P´agina 237) del libro Matem´aticas Discretas de Johsonbaugh que se
encuentra en el campus virtual:
1 1 al 6
2 31 al 37
3 44 al 49
4 58 al 62
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 26 / 1

<!-- página 27 -->

¿Cu´antas disposiciones (lineales) se pueden formar con las letras de la
palabra M I S S I S S I P P I ?.
Se tienen 11 lugares para ubicar 11 letras, pero la respuesta no es 11!,
ya que tenemos s´ımbolos repetidos.
Consideremos ubicar:
Dos letras P en esos 11 lugares: C(11, 2)
Cuatro letras S en los 9 lugares restantes: C(9, 4)
Cuatro letras I en los 5 lugares disponibles: C(5, 4)
Por ´ultimo queda una letra M que se ubicar´a en el ´unico lugar restante.
Haciendo uso de la regla del producto:
C(11, 2)C(9, 4)C(5, 4) = 11! 2!9! 9! 4!5! 5! 4!1! = 11! 2!4!4!1!|   {z   }
Observa
= 34650
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 27 / 1

<!-- página 28 -->

Teorema
Suponga que una sucesi´on S de n art´ıculos tiene n1 objetos id´enticos del
tipo 1, n2 objetos id´enticos del tipo 2, ..., nt objetos id´enticos del tipo t,
donde n1 + n2 + ... + nt = n. Entonces, el n ´umero de ordenamientos de S
es
n!
n1!n2!··· nt !
Ejemplo 1
Calcular el n ´umero de disposiciones de las letras de TALLAHASSEE.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 28 / 1

<!-- página 29 -->

Ejemplo 2
De los 831600 ordenamientos anteriores, ¿cu´antas no tienen letras A
adyacentes?
Ayuda: primero se ordenan las letras restantes, y luego se considera que las
letras A se pueden ubicar en cualquiera de los nueve lugares disponibles al
inicio de la palabra o entre las letras restantes:
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 29 / 1

<!-- página 30 -->

Ejemplo 3
Siete amigos en un restaurante, luego de cenar, van a elegir cada uno
un postre de entre los siguientes disponibles: (c) cheesecake, (h) helado,
(t) tiramis ´u ´o (f) flan con DDL . ¿Cu´antos pedidos distintos es posible
hacer?
Si observamos la segunda columna, el problema pasa a ser: ¿a d´onde
coloco la barra divisoria que me separa el tipo de postre?
Pensado de esta manera, ¿cu´antos pedidos distintos es posible hacer?
En general, este tipo de problema, se lo conoce como un problema de
Combinaciones con Repetici´on.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 30 / 1

<!-- página 31 -->

Combinaciones con repetici´on
Si X es un conjunto que contiene t elementos, el n ´umero de selecciones
no ordenadas de k elementos de X, con repetici´on, es
 k + t − 1
t − 1
!
Tener en cuenta que tambi´en es correcto plantear C(t+k−1, k), ¿por qu´e?
Ejemplo 1
¿De cu´antas formas podemos distribuir ocho alfajores iguales entre cin-
co ni˜nos, de modo que cada uno reciba al menos uno?
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 31 / 1

<!-- página 32 -->

Ejemplo 2
Se deslizan por una rampa 15 pelotas de tenis que caer´an en alguna
de las seis bolsas que se encuentran al final de la rampa. ¿De cu´antas
maneras distintas se pueden distribuir en dichas bolsas, si
1 no hay restricciones?
2 cada bolsa recibe al menos una pelota?
3 la tercera bolsa 10 pelotas?
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 32 / 1

<!-- página 33 -->

Ejemplo 3
Una tienda de helados tiene disponibles 31 sabores de helado.
¿De cu´antas formas de puede obtener una docena de conos de helado si
1 no queremos el mismo sabor m´as de una vez?
2 un sabor puede obtenerse hasta 12 veces?
3 un sabor no puede ordenarse m´as de un 11 veces?
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 33 / 1

<!-- página 34 -->

Ejemplo 4
Una PYME tiene cuatro gerentes: Ana, Mar´ıa, Juan y Ra ´ul. Se quiere
distribuir entre ellos 10000 dolares en concepto de premios; cada pago
se har´a con billetes de 100 dolares. Calcular el n ´umero de formas de
distribuir esos premios si
1 es posible que uno o m´as gerentes no obtenga nada.
2 cada gerente debe recibir al menos 1000 dolares.
3 cada gerente debe recibir al menos 1000 dolares y Juan, recibe al
menos 5000.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 34 / 1

<!-- página 35 -->

Ejemplo 5
Un mensaje est´a formado por 12 s´ımbolos diferentes y se va a transmi-
tir a trav´es de un canal de comunicaci´on. Adem´as de los 12 s´ımbolos,
el transmisor tambi´en enviar´a un total de 45 espacios en blanco entre
los s´ımbolos, usando al menos tres espacios entre cada par de s´ımbolos
consecutivos. ¿De cu´antas formas puede el transmisor enviar ese men-
saje?
Ejemplo 6
Determinar todas las soluciones enteras no negativas de la ecuaci´on
x1 + x2 + x3 + x4 + x5 = 9
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 35 / 1

<!-- página 36 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 6, apartado
6.6 (P´agina 265) del libro Matem´aticas Discretas de Johsonbaugh que se
encuentra en el campus virtual:
1 3-4-5
2 8-9
3 12-13
4 24
5 26
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 36 / 1

<!-- página 37 -->

Supongamos que se tiene una suma de n ´umeros (o expresiones) que
cumplen con cierto patr´on, por ejemplo: 1 + 3 + 5 + 7 + ... + 533 + 535
Existe una notaci´on abreviada de la misma. La idea consiste en encon-
trar un patr´on que cumple cada t´ermino, en este caso es la suma de
todos los impares desde 1 hasta 535. Por lo que cada t´ermino tendr´a la
forma de un impar.
Sumatoria (o Notaci´on Sigma)
La operaci´on sumatoria se expresa con la letra griega sigma may ´uscula
Σ, y se representa as´ı:
nX
i=a
xi
xi : es una funci´on de i con dominio en Z, y que tiene la propiedad de definir
un´ıvocamente cada t´ermino de la suma.
i: es la variable (puede ser otra letra), recorre todos los enteros entre a (l´ımite
inferior) y n (l´ımite superior).
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 37 / 1

<!-- página 38 -->

Volviendo a nuestro ejemplo, utilizando la notaci´on sigma tenemos:
1 + 3 + 5 + 7 + ... + 533 + 535 =
268P
i=1
(2i − 1)
o tambi´en
1 + 3 + 5 + 7 + ... + 533 + 535 =
267P
k=0
(2k + 1)
(Si no estas covencido, sustituye los valores de i (o k) en la funci´on.)
Otros ejemplos:
8 + 9 + 10 + 11 + 12 + 13 + ... + 998 + 999 =
999P
k=8
k
 7
0
!
+
 7
1
!
+
 7
2
!
+
 7
3
!
+
 7
4
!
=
4X
i=0
 7
i
!
1 − 2 + 4 − 8 + 16 − 32 + ... + 256 − 512 + 1024 =
10P
i=0
(−2)i
1
3 + 1 4 + 1 5 + 1 6 + ... + 1 n = nP i=3 1 i
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 38 / 1

<!-- página 39 -->

Observemos el desarrollo del cubo de un binomio:
(a + b)3 = (a + b)(a + b)(a + b) = (a + b)(aa + ab + ba + bb)
(a + b)3 = aaa + aab + aba + abb + baa + bab + bba + bbb
(a + b)3 = 1 · a3 + 3 · a2b + 3 · ab2 + 1 · b3
(a + b)3 =
 3
0
!
a3b0 +
 3
1
!
a2b +
 3
2
!
ab2 +
 3
3
!
a0b3
Generalizando esta idea
Teorema Binomial
Si a y b son variables, y n es un entero positivo, entonces
(a + b)n =
 n
0
!
anb0 +
 n
1
!
an−1b1 +
 n
2
!
an−2b2 + ... +
 n
n − 1
!
a1bn−1 +
 n
n
!
a0bn
Lo que en notaci´on sigma es (a + b)n =
nX
i=0
 n
i
!
an−i bi
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 39 / 1

<!-- página 40 -->

Ejemplo 1
¿Cu´antos t´erminos tiene el desarrollo de (2a+b)7?, determinar el quinto.
Ejemplo 2
Calcular el coeficiente del t´ermino que posee x5y2 en el desarrollo de
(x − 3y)7.
Ejemplo 3
Probar que para cualquier entero n > 0:
 n
0
!
+
 n
1
!
+
 n
2
!
+ ... +
 n
n
!
= 2n
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 40 / 1

<!-- página 41 -->

La generalizaci´on del teorema del binomio se conoce como el teorema
multinomial.
Teorema multinomial
Sean n y t naturales, el coeficiente de xn1 1 xn2 2 xn3 3 ...xnt t en el desarrollo de
(x1 + x2 + ... + xt )n es n! n1!n2!n3!··· nt !
donde cada ni es un natural entre 0 y nt , ∀≤ i ≤ t
y adem´as, n1 + n2 + n3 + ... + nt = n.
Este coeficiente se denomina coeficiente multinomial.
Tambi´en se puede escribir como
 n
n1, n2, ..., nt
!
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 41 / 1

<!-- página 42 -->

Ejemplo 1
Calcular el coeficiente del t´ermino que contiene a x2y2z3 en el desarro-
llo de (x + y + z)7, y en el desarrollo de (2x + y + 3z + 5w)7 .
Ejemplo 2
Hallar el t´ermino que contiene a a4b5 en el desarrollo de (3a + 2b − 5)11.
Ejemplo 3
Calcular la cantidad de t´erminos que tiene (3v + 2w + x + y + z)8 en su
desarrollo.
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 42 / 1

<!-- página 43 -->

Actividades propuestas
Para realizar las actividades pr´acticas correspondientes a este apartado
te sugerimos realizar los siguientes ejercicios del cap´ıtulo 6, apartado
6.7 (P´agina 270) del libro Matem´aticas Discretas de Johsonbaugh que se
encuentra en el campus virtual:
1 1
2 2
3 4-5
4 10-11
Vaira-Fedonczuk-Colliard-Cottonaro Matem´atica Discreta - LSI - UADER 2026 43 / 1
