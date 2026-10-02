# Tema 3_Parte A

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 1/UNIDAD 3/Tema 3_Parte A.pdf` · 23 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Definición de variable aleatoria. |
| 2 | Variable aleatoria como función de eventos; P(A) ↔ P(X = x). |
| 3 | Tipos: variable aleatoria discreta (VAD) y continua (VAC), con ejemplos. |
| 4 | VAD: experimento de 3 artículos (D/N), espacio muestral de 8 elementos y X = N° de defectuosos. |
| 5 | Eventos asociados a X (X = 3, X ≥ 2) y sus probabilidades. |
| 6 | Probabilidades de X = 0, 1, 2, 3 (1/8, 3/8, 3/8, 1/8) y suma igual a 1. |
| 7 | Función de probabilidad f(x) = P(X = x) y su tabla. |
| 8 | Propiedades de la f(x) de una VAD: f(x) ≥ 0, Σ f(x) = 1. |
| 9 | Ej. 2 (8 computadoras, 3 defectuosas, se compran 2): f(0) con combinatorios = 10/28. |
| 10 | Ej. 2: f(1) = 3·5/28. |
| 11 | Ej. 2: f(2) = 3·1/28. |
| 12 | Ej. 2: distribución de probabilidad f(0)=10/28, f(1)=15/28, f(2)=3/28. |
| 13 | Ej. 2 por extracciones sucesivas: mismos resultados que con combinatorios. |
| 14 | Distribución acumulada F(x) de una VAD; a lo sumo 1 defectuosa = 25/28, al menos 1 = 18/28. |
| 15 | Gráfico de bastones de f(x) del Ej. 2 (sin polígono, porque es VAD). |
| 16 | Tabla y gráfico de la distribución acumulada discreta F(x) del Ej. 2. |
| 17 | VAC: P(X = x) = 0; solo tienen probabilidad los intervalos; se usa una función f(x). |
| 18 | Función de densidad de probabilidad: P(a < X < b) = ∫ f(x) dx. |
| 19 | Propiedades de la fdp de una VAC: f ≥ 0, integral total = 1, P por integral. |
| 20 | Ejemplo f(x) = x²/3 en (−1; 2): verificar que es fdp y P(−1 < x < 1) = 2/9. |
| 21 | P(x < 1,5) = 35/72; definición de F(x) de una VAC como integral. |
| 22 | Relación f(x) = dF/dx; F(x) = (x³+1)/9 del ejemplo, por tramos. |
| 23 | Distribuciones empíricas: cómo se infiere la forma de la distribución a partir de mediciones (curvas ilustrativas). |

<!-- página 1 -->

¿A qué se denomina Variable Aleatoria?
w – Cap 3
Es una función que asocia un número real a cada
elemento o subconjunto (evento) del Espacio
Muestral.

<!-- página 2 -->

Este valor es el resultado de realizar un
experimento y tiene por tanto una connotación
aleatoria ya que no están controladas todas las
variables (eventos fortuitos) ó se realiza ex profeso
al azar.
Evento → subconjunto del Espacio Muestral ⇒ Variable Aleatoria

   A    Asigno   X
P(A)    Asigno        P(X = x)
Toda la teoría de conjuntos es válida para la variable aleatoria.

<!-- página 3 -->

Tipos de Variables Aleatorias.
• Variables Aleatorias Discretas (VAD)
• Variables Aleatorias Continuas (VAC)
Variable Aleatoria Discreta (VAD)
Se puede contar el conjunto de resultados posibles (Escala
discreta) aunque el número de elementos sea infinito.
Ej: Resultados al arrojar un dado muchas veces. No existirán
resultados entre dos consecutivos.
Variable Aleatoria Continua (VAC)
No es posible contar el número de posibilidades que puede tomar
un valor de la VAC. (Escala Continua).
Ej: Posibles valores de medición de temperaturas. Siempre habrá
infinitos valores entre dos de ellos.

<!-- página 4 -->

a) Variable Aleatoria Discreta
La VAD toma cada uno de sus valores con cierta probabilidad
según el experimento y el evento asociado.
N° de elementos en el EM = n1.n2.n3  2.2.2 = 8

S = {DDD, DDN, DND, DNN, NDD, NDN, NND, NNN}

Definimos la Variable aleatoria X = N° de artículos defectuosos.
Ej: experimento: seleccionar 3 artículos
 de una cadena de fabricación.

Observación: clasificar como:
 Def (D) o No Def.  (N)

<!-- página 5 -->

a) Variable Aleatoria Discreta
La VAD toma cada uno de sus valores con cierta probabilidad
según el experimento y el evento asociado.
Eventos:

A:  {3 artículos defectuosos}
X = 3
P(A)  →  P X = 3

B: {Artículos defectuosos mayor o igual a 2}
 X ≥  2
P B →  P(X ≥  2)

<!-- página 6 -->

a) Variable Aleatoria Discreta
La VAD toma cada uno de sus valores con cierta probabilidad
según el experimento y el evento asociado.
SI X es una VAD que representa el
 N° de artículos defectuosos:

X = 0    con    P(X) =
1
8  ⇒P(X = 0) =
1
8
X = 1    con    P(X) =
3
8  ⇒P(X = 1) =
3
8
X = 2    con    P(X) =
3
8  ⇒P(X = 2) =
3
8
X = 3    con    P(X) =
1
8  ⇒P(X = 3) =
1
8

S = {DDD, DDN, DND, DNN, NDD, NDN, NND, NNN}

 P(X = x)
∀x
 =  1

<!-- página 7 -->

Se puede también utilizar una expresión matemática ligada a la probabilidad de la VA
donde f(x) = P(X = x)

El conjunto ordenado (x, f(x)) de una VAD se llama Función de Probabilidad de VAD
ó Función de Distribución ó Función de Cuantía.                     (fdp de VAD)
Función de distribución: Tabla con los pares (x, f(x))
X f(x)
0 1/8
1 3/8
2 3/8
3 1/8

<!-- página 8 -->

Propiedades de una fdp de VAD

1. f(x) ≥ 0

2.   f(x)∀x   = 1

3.  P(X =  x)  =  f(x)

<!-- página 9 -->

Ej. 2: un embarque de 8 computadoras similares para una tienda contiene 3
defectuosos. Una escuela compra 2 computadoras en esa tienda.

Encuentre la Distribución de Probabilidad para el N° de computadoras
defectuosas que compra la escuela. (Comparar con el caso de fabricación
en serie).
a) No compra ninguna defectuosa.
P(x)  =   n
N =  n1 . n2
N
n1:  0 de 3,   n2:   2 de 5
X =  0 ⇒  f(x =  0)  = ?
N:  2 de 8
f 0 =  n1 . n2
N  =
3
0  . 5
2
8
2

f 0 =
3!
0! 3!  . 5!
2! 3!
8!
2! 6!
= 1 . 10
28
⇒ Hay una sola forma de no tomar defectos.
Hay 10 formas de tomar 2 no defectuosas de 5.
Hay 28 formas de tomar 2 computadoras de 8
totales.

<!-- página 10 -->

Ej. 2: un embarque de 8 computadoras similares para una tienda contiene 3
defectuosos. Una escuela compra 2 computadoras en esa tienda.

Encuentre la Distribución de Probabilidad para el N° de computadoras
defectuosas que compra la escuela. (Comparar con el caso de fabricación
en serie).
b) Compra una defectuosa.
n1: 1 de 3,   n2:   1 de 5
X = 1 ⇒  f(x = 1)  = ?
N:  2 de 8
f(1)  =
3
1  . 5
1
8
2
 =  3 . 5
28

<!-- página 11 -->

Ej. 2: un embarque de 8 computadoras similares para una tienda contiene 3
defectuosos. Una escuela compra 2 computadoras en esa tienda.

Encuentre la Distribución de Probabilidad para el N° de computadoras
defectuosas que compra la escuela. (Comparar con el caso de fabricación
en serie).
c) Compra dos defectuosas.
n1: 2 de 3,   n2:   0 de 5
X = 2 ⇒  f(x = 2)  = ?
N:  2 de 8
f(2)  =
3
2  . 5
0
8
2
 =  3 . 1
28

<!-- página 12 -->

Ej. 2: un embarque de 8 computadoras similares para una tienda contiene 3
defectuosos. Una escuela compra 2 computadoras en esa tienda.

Encuentre la Distribución de Probabilidad para el N° de computadoras
defectuosas que compra la escuela. (Comparar con el caso de fabricación
en serie).
Distribución de Probabilidad:
X f(x)
0 10/28 = 0,357
1 15/28 = 0,536
2 3/28 = 0,107

<!-- página 13 -->

Ej. 2: un embarque de 8 computadoras similares para una tienda contiene 3
defectuosos. Una escuela compra 2 computadoras en esa tienda.
Otra forma de plantear el problema es sacar primero un artículo y luego otro.
P X =  1° extracción . 2° extracción
 P X =  n1
N1
 . n2
N2

n1:  opciones de la primera extracción.
N1:  n° total de artículos primera extracción.
n2:  opciones de la segunda extracción.
N2:  n° total de artículos segunda extracción.
P(X = 0):  No sacar ninguna defectuosa
P(X =  0)  =  5
8 . 4
7  =  20
56  =  10
28
P(X =  1)  =  3
8 . 5
7  +  5
8 . 3
7 =  15
56  +  15
56  =  30
56  =  15
28
P(X =  2)  =  3
8 . 2
7  =  6
56  =  3
28
P(X=0) -> {NN}
P(X=1) -> {DN ó ND}
P(X=2) -> {DD}

<!-- página 14 -->

Distribución acumulada F(X)
La F(X) de una VAD con distribución de probabilidad f(x) es:
F(X)  =  P(X ≤  x)  =   f(t)
t ≤x
    para   − ∞ < X <  +∞
Para el ejemplo anterior:
¿Qué probabilidad existe de comprar a lo sumo 1 defectuosa?
F(X ≤  1)  =    f(t)
t ≤1
 =  f(0)  +  f(1)  =  10
28  +  15
28  =  25
28
¿Qué probabilidad existe de comprar al menos 1 defectuosa?
F X ≥  1 = 1 −    f t
t ≤0
 = 1 −  f 0 =  28
28  −  10
28  =  18
28

<!-- página 15 -->

Histograma de Frecuencias: Gráfico de Barras o Bastones
x f(x)
0 0,357
1 0,536
2 0,107
f(X)

<!-- página 16 -->

X F(X)
0 0,357
1 0,893
2 1
Distribución Acumulada Discreta

<!-- página 17 -->

b) Distribuciones de Variable Aleatoria Continua (VAC)
Una Variable Aleatoria Continua tiene una probabilidad
P(X=x) = 0 de tomar exactamente cualquiera de sus
valores.
 P A → P(X = x) =  n
N si N →  ∞                 P(A) → 0
Si en cambio se trata de un intervalo a <  x <  b :

                             P a < X < b  puede ser diferente de cero
Una Variable Aleatoria Continua no se puede presentar de forma tabular
⇒ se utiliza una función f(X).

<!-- página 18 -->

f(X) en una Variable Aleatoria Continua se denomina:

 Función de Densidad de Probabilidad.
P(a < X < b)  =   f(x)dx
b
a

<!-- página 19 -->

Una función f(x) es una función de densidad de probabilidad para una
VAC ∈  ℝ si:
Propiedades de una fdp de VAC

1.  f(x)  ≥ 0      ∀x ∈ ℝ

2.  f(x) dx
+∞
−∞  =  1

3. P(a < x < b)  =   f(x) dx
b
a

<!-- página 20 -->

Ejemplo: sea f(x):
x2
3  ; −1 < x < 2
0 ; para cualquier otro caso
a) Comprobar que f(x) es una f. d. p.
1)  f(x)  ≥ 0 ; como x2
3  ≥ 0           ∨ x ∈ ℝ   ✔
2)  f(x) dx
+∞
−∞
 =   x2
3  dx
+∞
−∞
 =  1
3
x3
3
−1
2
= 8
9 + 1
9 = 1  ✔
b) Obtener P(−1 < x < 1)
P(−1 < x < 1)  =   x2
3  dx
1
−1
 = 1
3
x3
3
−1
1
=  2
9

<!-- página 21 -->

c) Obtener P(x < 1,5)
P(x < 1,5)  =  P(x < 3
2)  =   f(x) dx
3/2
−∞
 =    x2
3  dx
3/2
−1

P(x < 1,5)  =  x3
9
3 2
−1
 =  27
9 . 8  +  1
9  =  27
72   +  8
72  =  35
72
Función de distribución Acumulada de una VAC
F(x)  =  P(X ≤ x)  =   f(x) dx
x
−∞

<!-- página 22 -->

Relación entre F(x) y f(x)
Si       F x =   f t dt
x
−∞
 ⇒           f(x)  =  d F(x)
dx
Ejemplo: Obtener F(x) del ejemplo anterior
F x =   t2
3  dt
x
−∞
  =    t2
3  dt
x
−1
 =  x3
9  +  1
9  =  x3  +  1
9  ;       −1 < x < 2
F x = 0                                                                                         ;     −∞ < x < −1
F x = 1                                                                                         ;        x > 2

<!-- página 23 -->

Distribuciones Empíricas:
A menudo no sabemos la forma de la distribución de probabilidad (caso discreto)
o la función de distribución de probabilidad (caso continuo).
¿Cómo sabemos que
tienen esta forma?
Se han realizado mediciones → se han tabulado y graficado
este conjunto de mediciones (muestra) → se infiere según
estas gráficas que el comportamiento de la variable
(población) tiene esta forma.
