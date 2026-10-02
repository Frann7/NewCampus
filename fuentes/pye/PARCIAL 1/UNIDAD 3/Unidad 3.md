# Unidad 3

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 1/UNIDAD 3/Unidad 3.pdf` · 11 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Índice del Tema 3; definición de variable aleatoria; VAD y VAC. |
| 2 | Ejemplo de 3 artículos defectuosos/no: X = N° de defectuosos, f(x) y propiedades de la fdp de VAD. |
| 3 | Tabla de f(x) y Ej. 2: computadoras defectuosas (planteo con combinatorios). |
| 4 | Ej. 2: f(0), f(1), f(2) con combinatorios y distribución 10/28, 15/28, 3/28. |
| 5 | Ej. 2 por extracciones sucesivas; F(x) acumulada; a lo sumo 1 = 25/28, al menos 1 = 3/28. |
| 6 | Gráfico de barras y polígono de f(x); distribución acumulada discreta (tabla de F). |
| 7 | Tabla de F(x) y 1 − F(x); VAC: P(X = x) = 0, función de densidad. |
| 8 | fdp de VAC y propiedades; ejemplo f = x²/3 en (−1; 2): P(−1<x<1) = 2/9, P(x<1,5) = 35/72; F(x). |
| 9 | Relación f = dF/dx; F(x) = (x³+1)/9; distribuciones empíricas; distribuciones conjuntas (propiedades discreta y continua). |
| 10 | Probabilidad en conjunta, marginales g(x) y h(y), condicionales f(y/x) y f(x/y); independencia de eventos. |
| 11 | Independencia estadística de variables: f(x,y) = g(x)·h(y). |

<!-- página 1 -->

Tema 3
Variables Aleatorias y Distribuciones de Probabilidad

● Variable aleatoria: Definición
● Variable aleatoria Discreta (VAD) y Continua (VAC)
● Propiedades de una Función de Distribución de Probabilidad de VAD f(x)
● Función de distribución acumulada F(x)
● Función de Densidad de Probabilidad de una VAC
● Propiedades de una f.d.p
● Relación entre F(x) y f(x)
● Distribución de Probabilidad Distribución Conjunta (f.d.c)
● Propiedades de una f.d.c
● Distribuciones Marginales
● Distribución de Probabilidad Condicional de una f.d.c
● Independencia Estadística

Variable Aleatoria: Definición

Es una función que asocia un número real a cada elemento o subconjunto (evento) del Espacio
Muestral.

Este valor es el resultado de realizar un experimento y tiene por tanto una connotación aleatoria ya
que no están controladas todas las variables (eventos fortuitos) ó se realiza ex profeso al azar.

Evento → subconjunto del Espacio Muestral ⇒ Variable Aleatoria
E    Asigno   X
P(E)    Asigno        P(X = x)

Toda la terna de conjuntos es válida para la variable aleatoria.

Variable Aleatoria Discreta (VAD)

Se puede contar conjunto de resultados posibles (Escala discreta) aunque el número de elementos
sea infinito (Ej: Arrojar un dado muchas veces)

Variable Aleatoria Continua (VAC)

No es posible contar el número de posibilidades que puede tomar un valor de la VAC. (Escala
Continua).
Ej: medición de temperaturas.

VAD: la VAD toma c/u de sus valores con cierta probabilidad según el experimento y el evento
asociado.

<!-- página 2 -->

Ej: experimento: seleccionar 3 artículos de una cadena de fabricación.

Observación: clasificar como Def (D) o No Def.  (N)
N° de elementos = 23 = 8
S = {DDD, DDN, DND, DNN, NDD, NDN, NND, NNN}
Variable aleatoria X = N° de artículos defectuosos.

Eventos:
A:{N° de artículos defectuosos igual a 3}   X = 3
P(A)  →  P(X = 3)

B:{N° de artículos defectuosos mayor o igual a 2} x ≥  2
P(B)  =  P(X ≥  2)

.-etc.

SI X es una VAD que representa el N° de artículos defectuosos:

X = 0  con P(X) =
1
8  ⇒ P(X = 0) =
1
8
X = 1  con P(X) =
3
8  ⇒ P(X = 1) =
3
8
X = 2  con P(X) =
3
8  ⇒ P(X = 2) =
3
8
X = 3  con P(X) =
1
8  ⇒ P(X = 3) =
1
8

∑ P(X = x)
∀x
 =  1

Se puede también utilizar una expresión matemática ligada a la probabilidad de la VA
donde f(x) = P(X = x)

El conjunto ordenado (x, f(x)) se llama Función de Probabilidad o Distribución de
Probabilidad (fdp)

Propiedades de una fdp de VAD

1. f(x) ≥ 0

2. ∑ f(x)∀x   = 1

3. P(X =  x)  =  f(x)

<!-- página 3 -->

Distribución de probabilidad: Tabla con los pares (x, fx)

X f(x)
0 1/8
1 3/8
2 3/8
3 1/8

Ejemplo de tomar 3 artículos y clasificarlos como defectuosos o no defectuosos.

Definir X = N° de artículos defectuosos.

Ej. 2: un embarque de 8 computadoras similares para una tienda contiene 3
defectuosos. Una escuela compra 2 computadoras en esa tienda.
Encuentre la Distribución de Probabilidad para el N° de computadoras defectuosas que
compra la escuela. (Comparar con el caso de fabricación en serie. No es lo mismo)

P(X) =
n
N

X: N° de computadoras defectuosas en la compra de la escuela.

<!-- página 4 -->

a) No compra ninguna defectuosa.

P(x)  =   n
N =  n1 . n2
N

X =  0 ⇒  f(x =  0)  = ?
n1: 0 de 3,    n2:  2 de 5
N: 2 de 8

f(0)  =  n1 . n2
N  =
(3
0) . (5
2)
(8
2)
 =
3!
0! (3!) . 5!
2! (3!)
8!
2! (6!)

f(0)  =  1 . 10
28
⇒ Hay una sola forma de no tomar defectos. Hay 10 formas de tomar 2 no
defectuosas de 5. Hay 28 formas de tomar 2 computadoras de 8 totales.

f(1)  =
(3
1) . (5
1)
(8
2)
 =  3 . 5
28

b)
f(2)  =
(3
2) . (5
0)
(8
2)
 =  3 . 1
28

Distribución de Probabilidad:

X f(x)
0 10/28 = 0,357
1 15/28 = 0,536
2 3/28 = 0,107

<!-- página 5 -->

Otra forma de plantear el problema es sacar primero un artículo y luego otro.

P(x)  =  1° extracción . 2° extracción =  n1
N1
 . n2
N2

n1: opciones de la primera extracción.
N1: n° total de artículos primera extracción.
n2: opciones de la segunda extracción.
N2: n° total de artículos en la segunda extracción.

P(X = 0): No sacar ninguna defectuosa
P(X =  0)  =  5
8 . 4
7  =  20
56  =  10
28

P(X =  1)  =  3
8 . 5
7 + 5
8 . 3
7 =  15
56 + 15
56  =  30
56  =  15
28

P(X =  2)  =  3
8 . 2
7  =  6
56  =  3
28

Este método da resultados iguales al anterior.

Distribución acumulada

La F(X) de una VAD con distribución de probabilidad f(x) es:
F(X)  =  P(X ≤  x)  =  ∑ f(t)
t ≤x
    para   − ∞ <  x <  +∞

Para el ejemplo anterior: ¿Qué probabilidad existe de comprar a lo sumo 1 defectuosa?

F(X ≤  1)  =  ∑ f(t)
t ≤1
  =  f(0) +  f(1)  =  10
28 + 15
28  =  25
28

¿Qué probabilidad existe de comprar al menos 1 defectuosa?

F(X ≥  1)  = 1 − ∑ f(t)
t ≤1
  = 1 − [ f(0) +  f(1)]  =  28
28 − 25
28  =  3
28

<!-- página 6 -->

Gráfico de Barras → Polígono de Frecuencias

(x, f(x))
x f(x)
0 0,357
1 0,536
2 0,107

Distribución Acumulada Discreta

<!-- página 7 -->

(x, F(x))
x f(x)
0 0,357
1 0,893
2 1

x 1 - f(x)
0 0,643
1 0,107
2 0

Distribuciones Continuas
Una Variable Aleatoria Continua tiene una probabilidad P(X=x) = 0 de tomar
exactamente cualquiera de sus valores.

P(n)  =
n
N  si N →  ∞                 P(n) → ∞
Si en cambio se trata de un intervalo (a <  x <  b)
- Una Variable Aleatoria Continua no se puede presentar de forma tabular ⇒ se
utiliza una función f(x)

f(x) en una Variable Aleatoria Continua se denomina: Función de Densidad de
Probabilidad.

<!-- página 8 -->

P(a < x < b)  =  ∫ f(x)dx
b
a

Una función f(x) es una función de densidad de probabilidad para una VAC ∈  ℝ si:

1-  f(x)  ≥ 0      ∀x ∈ ℝ
2- ∫ f(x) dx
+∞
−∞  =  1
3- P(a < x < b)  =  ∫ f(x) dx
b
a

Ejemplo: sea f(x)
x2
3  ; −1 < x < 2
0 ; para cualquier otro caso

a) Comprobar que f(x) es una f. d. p.
1)  f(x)  ≥ 0 si
x2
3  ≥ 0           ∨ x ∈ ℝ se cumple
2) ∫ f(x) dx
+∞
−∞
 =  ∫ x2
3  dx
+∞
−∞
 =  x3
9  ; ( para (x =  2) − (x =  −1)) =  8
9 + 1
9 = 1  ✔

b) Obtener P(−1 < x < 1)

P(−1 < x < 1)  =  ∫ x2
3  dx
1
−1
 =  x3
9   ; ( para (x =  1) −  (x =  −1) )   =  2
9

c) Obtener P(x < 1,5)

P(x < 1,5)  =  P(x < 3
2)  =  ∫ f(x) dx
3/2
−∞
 =   ∫ x2
3  dx
3/2
−1

P(x < 1,5)  =  x3
9  ; ( para (x = 3/2 ) − (x =  −1) )  =  27
9 . 8 + 1
9  =  27
72   + 8
72
=  35
72

Función de distribución Acumulada de una VAC
F(x)  =  P(X ≤ x)  =  ∫ f(x) dx
x
−∞

Relación entre F(x) y f(x)

<!-- página 9 -->

Si       F(x)  =  ∫ f(t) dt
x
−∞
 ⇒  f(x)  =  d F(x)
dx

Ejemplo: Obtener F(x) del ejemplo anterior
F(x)  = ∫
 t2
3  dt
x
−∞   =  ∫
 t2
3  dt
x
−1  =
x3
9  +
1
9  =
x3 + 1
9  ✔

Distribuciones Empíricas: A menudo no sabemos la forma de la distribución de
probabilidad (caso discreto) o la función de distribución de probabilidad (caso continuo).

Ejemplo:

¿Cómo sabemos que tienen esta forma?
Se han realizado mediciones → se han tabulado y graficado este conjunto de
mediciones (muestra) → se infiere según estas gráficas que el comportamiento de la
variable (población) tiene esta forma.

Distribuciones Conjuntas
Espacios muestrales multidimensionales.

Propiedades
Discreta Continua
F(x, y) ≥ 0 ; ∀(x, y) f(x, y)  ≥ 0   ;   f(x, y)
∑ ∑ f(x, y)
yx
  =  1; ∀(x, y) ∫ ∫ f(x, y) dx dy
+∞
−∞
+∞
−∞
 =  1
P(X =  x, Y =  y)  = f(x, y)
P(a < x < b, c < y < d )  = ∫ ∫ f(x, y)dx dy
d
c
b
a

si {a ≤ x ≤ b ;  c ≤ y ≤ d}

<!-- página 10 -->

P[(x, y)  ∈ ℝ]  = ∑ ∑ f(x, y)
yx

Distribuciones Marginales
Distribución de una variable cuando la otra toma todos los valores posibles.
g(x)  =  ∑ f(x, y)y    y  ℎ(y)  =  ∑  f(x, y)x   caso Discreto
g(x)  =  ∫ f(x, y) dy
y=+∞
y=−∞  y  ℎ(x)  =  ∫ f(x, y) dx
x=+∞
x=−∞  caso Continuo

Distribución de Probabilidad Condicional
De la definición:  P(B/A)  =
P(A∩B)
P(A)  ;  P(A) > 0

A y B son dos eventos definidos por X = x; Y = y  (Variables aleatorias asociadas a los
eventos)

P(Y =  y / X =  x)  =
P (X = x ; Y = y)
P(X = x)  =
f(x ,y)
g(x)   si g(x)  >  0;
Siendo g(x) todos los valores posibles de y

f (y/x)  =
f(x,y)
g(x)  y a la inversa f (x/y)  =
f(x,y)
ℎ(y)   con  g(x), ℎ(y) > 0
Siendo ℎ(y) todos los valores posibles de x

Independencia Estadística
Al igual que con la teoría de conjuntos:
P (A B⁄ ) = P(A)
P (B A⁄ ) = P(B)
Se dice que los eventos A y B son independientes.
Como consecuencia:
P (A B⁄ ) = P(A ∩ B)
P(B) − −→ P(A ∩ B) = P(A). P(B)

<!-- página 11 -->

P (B A⁄ ) = P(A ∩ B)
P(B) − −→ P(A ∩ B) = P(B). P(A)

De la misma forma entonces para la variable aleatoria de distribución conjunta (x,y):
f(x y⁄ ) = g(x)
f (y x⁄ ) = ℎ(y)
Se dice que x e y son independientes.
Entonces:
f(x y⁄ ) = g(x) = f(x, y)
ℎ(y)   − −→ f(x, y) = f(x). ℎ(y)

f (y x⁄ ) = ℎ(y) = f(x, y)
g(x)   − −→ f(x, y) = ℎ(y). f(x)
Que son las consecuencias de la independencia estadística entre las variables x,y
