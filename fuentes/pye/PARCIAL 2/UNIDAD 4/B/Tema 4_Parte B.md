# Tema 4_Parte B

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 4/B/Tema 4_Parte B.pdf` · 19 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Covarianza: medida de asociación, signo, definición σxy = E[(x−μx)(y−μy)]. |
| 2 | Cov discreta (doble Σ) y continua (doble ∫); fórmula alternativa E(xy) − μx·μy. ⚠ ver el PDF: dobles integrales con límites desordenados |
| 3 | Demostración de la fórmula alternativa de Cov (continuo): arranca con distributiva. |
| 4 | Demostración Cov: repite la página 3. |
| 5 | Demostración Cov: repite la página 3. |
| 6 | Demostración Cov: repite página 3, anuncia separar en varias integrales. |
| 7 | Demostración Cov: integral separada en 4 términos; E(xy) y marginal de Y. ⚠ ver el PDF: dobles integrales con límites desordenados, numeración 1–4 suelta |
| 8 | Demostración Cov: se resuelven los términos 3 (μx) y 4 (integral doble = 1). ⚠ ver el PDF: dobles integrales con límites desordenados |
| 9 | Demostración Cov: resultado E(xy) − μxμy; independencia implica Cov = 0, no al revés. ⚠ ver el PDF: dobles integrales con límites desordenados |
| 10 | Ej. f = 4xy en [0,1]²: verificar que f es válida (integral doble = 1). ⚠ ver el PDF: dobles integrales con límites y fracciones desordenados |
| 11 | Ej. f = 4xy: E(xy) = 4/9, marginal g(x) = 2x, μx = μy = 2/3. ⚠ ver el PDF: dobles integrales, límites y fracciones rotos |
| 12 | Cov = 0, X e Y independientes. Ej. repuestos de bolígrafos: planteo con tabla conjunta y marginales. |
| 13 | Ej. repuestos: μx = 3/4, μy = 1/2, E(xy) = 3/14, Cov = −9/56. |
| 14 | Coeficiente de correlación ρ = σxy/(σxσy), sin unidades, entre −1 y 1. |
| 15 | Ej. repuestos: σx² = 45/112, σy² = 9/28, ρ = −0,4472. ⚠ ver el PDF: fracciones, raíz y exponentes de la cuenta de ρ rotos |
| 16 | Independencia estadística: f = g(x)·h(y) y E(xy) = E(x)E(y). |
| 17 | Demostración de E(xy) = E(x)E(y) para independientes; Cov = 0. ⚠ ver el PDF: dobles integrales con límites desordenados |
| 18 | V(ax+by+c) = a²V(x) + b²V(y) + 2ab·Cov: planteo de la demostración. ⚠ ver el PDF: exponentes y términos (1)/(2) desordenados |
| 19 | Demostración: resta (1) − (2) y agrupa, resultado final de la varianza de la combinación lineal. ⚠ ver el PDF: exponentes y agrupación de términos desordenados |

<!-- página 1 -->

Covarianza
En Espacios muestrales bidimensionales es interesante analizar la relación
entre ambas variables.
La COVARIANZA es una medida de asociación o dependencia
entre 2 variables aleatorias. La covarianza puede ser positiva o
negativa (la varianza siempre es positiva). Si valores grandes de X a
menudo dan como resultado valores grandes de Y, o valores
pequeños de X, dan como resultado valores pequeños de Y, la
covarianza será positiva. Caso contrario será negativa.
Si X e Y son variables aleatorias con función de distribución conjunta (fdc),
fx,y x, y , para el caso discreto (VAD) o función de densidad de probabilidad
conjunta (fdpc) para el caso continuo (VAC), entonces la covarianza de (x,y) ó
COV(x, y)  = σxy es:
σxy = E[(x − μx) . (y − μy)]

<!-- página 2 -->

σxy =    (x − μx) . (y − μy) . fx,y(x, y)
yx

σxy = E[(x − μx) . (y − μy)]
VAD
σxy =   (x − μx) . (y − μy) . fx,y(x, y) dx dy
+∞
x=−∞
+∞
y=−∞
 VAC
Una fórmula alternativa de cálculo de COV es:
σxy = E xy − μx. μy
Donde, por definición del operador Esperanza:
E xy =   x . y . fx,y(x, y) dx dy
+∞
x=−∞
+∞
y=−∞
 E xy
E[Y] =  Y . f(x)
+∞
−∞
dx

<!-- página 3 -->

Demostrar la fórmula alternativa de la COV:
para el caso continuo:
σxy = E xy − μx. μy
Partamos de la definición de COV: σxy = E[(x − μx) . (y − μy)]
σxy =   (x − μx) . (y − μy) . fx,y(x, y) dx dy
+∞
x=−∞
+∞
y=−∞

que para una VAC:
¿Qué hacemos ahora? Apliquemos propiedad distributiva
σxy =   [x. y. fx,y(x, y)  − μx . y . fx,y(x, y)  − x . μy . fx,y(x, y)  + μx . μy . fx,y (x, y)] dx dy
x=∞
x=−∞
y=∞
y=−∞

<!-- página 4 -->

Demostrar la fórmula alternativa de la COV:
para el caso continuo:
σxy = E xy − μx. μy
Partamos de la definición de COV: σxy = E[(x − μx) . (y − μy)]
σxy =   (x − μx) . (y − μy) . fx,y(x, y) dx dy
+∞
x=−∞
+∞
y=−∞

que para una VAC:
¿Qué hacemos ahora? Apliquemos propiedad distributiva
σxy =   [x. y. fx,y(x, y)  − μx . y . fx,y(x, y)  − x . μy . fx,y(x, y)  + μx . μy . fx,y (x, y)] dx dy
x=∞
x=−∞
y=∞
y=−∞

<!-- página 5 -->

Demostrar la fórmula alternativa de la COV:
para el caso continuo:
σxy = E xy − μx. μy
Partamos de la definición de COV: σxy = E[(x − μx) . (y − μy)]
σxy =   (x − μx) . (y − μy) . fx,y(x, y) dx dy
+∞
x=−∞
+∞
y=−∞

que para una VAC:
¿Qué hacemos ahora? Apliquemos propiedad distributiva
σxy =   [x. y. fx,y(x, y)  − μx . y . fx,y(x, y)  − x . μy . fx,y(x, y)  + μx . μy . fx,y (x, y)] dx dy
x=∞
x=−∞
y=∞
y=−∞

<!-- página 6 -->

Demostrar la fórmula alternativa de la COV:
para el caso continuo:
σxy = E xy − μx. μy
Partamos de la definición de COV: σxy = E[(x − μx) . (y − μy)]
σxy =   (x − μx) . (y − μy) . fx,y(x, y) dx dy
+∞
x=−∞
+∞
y=−∞

que para una VAC:
¿Qué hacemos ahora? Apliquemos propiedad distributiva
σxy =   [x. y. fx,y(x, y)  − μx . y . fx,y(x, y)  − x . μy . fx,y(x, y)  + μx . μy . fx,y (x, y)] dx dy
x=∞
x=−∞
y=∞
y=−∞

¿Y ahora? Separemos en varias integrales distribuyendo en los términos
del integrando

<!-- página 7 -->

σxy =   [x. y. fx,y(x, y)  − μx . y . fx,y(x, y)  − x . μy . fx,y(x, y)  + μx . μy . fx,y (x, y)] dx dy
x=∞
x=−∞
y=∞
y=−∞

σxy =   x . y . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
 − μx   y . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞

− μy   x . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
+ μx . μy   fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞

sabiendo que m x y m y son constantes ya que son los promedios poblacionales:
1 2
3 4
1 E xy =   x . y . fx,y(x, y) dx dy
+∞
x=−∞
+∞
y=−∞

2  fx,y(x, y) dx
x=∞
x=−∞
=  ℎ(y)  →  Función marginal de Y
  y . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
 =    y . ℎ(y) dy
y=∞
y=−∞
  = E y =  μy
Como:

<!-- página 8 -->

σxy =   [x. y. fx,y(x, y)  − μx . y . fx,y(x, y)  − x . μy . fx,y(x, y)  + μx . μy . fx,y (x, y)] dx dy
x=∞
x=−∞
y=∞
y=−∞

σxy =   x . y . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
 − μx   y . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞

− μy   x . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
+ μx . μy   fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞

sabiendo que m x y m y son constantes ya que son los promedios poblacionales:
1 2
3 4
3 De igual forma que en el caso anterior:   x . fx,y(x, y) dy dx
y=∞
y=−∞
x=∞
x=−∞
 = E x = μx
4   fx,y(x, y) dx dy
∞
−∞
∞
−∞
 =  1 Y la integral doble:

<!-- página 9 -->

Reemplazando estos valores en la función anterior nos queda:
σxy =   x . y . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
 − μx   y . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞

− μy   x . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
+ μx . μy   fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞

1 2
3 4
σxy = E xy − μx. μy − μy. μx + μx. μy σxy = E xy − μx. μy
= 1
El signo de la covarianza indica la relación directa (+) o inversa (-) entre X e Y. Si
son estadísticamente independientes, la covarianza dará 0. Lo opuesto no es
necesariamente cierto, es decir si la Covarianza da 0 no necesariamente son
estadísticamente independientes. La covarianza sólo describe la relación lineal
entre dos variables aleatorias, por consiguiente, si una covarianza entre X e Y es
cero pero X e Y no tienen una relación lineal, no significa que son
independientes. Serán independientes en el caso que la fdp o fdpc sean de
carácter lineal.

<!-- página 10 -->

Ejemplo: Sea X el tiempo de reacción, en segundos, de dos componentes
químicos e Y  la temperatura (en °C) a la cual inicia la reacción. Suponga que
las dos variables aleatorias, X e Y, tienen la densidad conjunta:
f x, y =  4xy                para 0 ≤ x ≤ 1;  0 ≤ y ≤ 1
0                    para otro caso
Solución:
a) f(x, y) ≥ 0 ; ∀(x, y)
b)
Determine si esta fdpc es válida. En caso afirmativo, calcule la COV entre X e Y
para determinar si existe relación entre la velocidad de reacción y la
temperatura y si la misma es directa o inversa.
  f x, y dx dy =
+∞
x=−∞
+∞
y=−∞

= 4   xy dxdy
1
x=0
=
1
y=0
4  y x2
2   dy = 2  y  dy = 2 y2
2
1
y=0
= 1
1
y=0

0 0
1 1

<!-- página 11 -->

σxy = E xy − μx. μy
E xy =   xy . fx,y(x, y) dx dy
+∞
x=−∞
+∞
y=−∞
=   xy. 4xy dx dy
1
x=0
1
y=0

E xy = 4   x2y2 dx dy = 4  y2
1
y=0
x3
3  dy = 4  y2 1
3 dy = 4
3
y3
3  = 4
9
1
y=0
1
x=0
1
y=0

0
1
0
1
μx = E x =  x g x  dx
+∞
x=−∞
 con  g x =  fx,y x, y dy = 4x  y dy = 2x
1
y=0
+∞
y=−∞

μx = E x =  x g x  dx = 2  x2dx = 2
3
1
x=0
+∞
x=−∞

μy = E y =  y ℎ y  dy = 2  y2dy = 2
3
1
y=0
+∞
y=−∞

<!-- página 12 -->

σxy = E xy − μx. μy = 4
9 − 2
3 . 2
3 = 0
Como sabemos que la fdpc es de carácter lineal, f x, y = 4xy, entonces
podemos decir que las variables X e Y son independientes.
Ejemplo: El número de repuestos de bolígrafos azules X y el número de
repuestos de bolígrafos rojos Y se encuentran en una caja para la venta. Cuando
se seleccionan dos repuestos para bolígrafo al azar se obtiene la distribución de
probabilidad conjunta siguiente:
f(x,y) X h(y)
0 1 2
Y
0 3/28 9/28 3/28 15/28
1 3/14 3/14 0 3/7
2 1/28 0 0 1/28
g(x) 5/14 15/28 3/28 1
Calcule la covarianza de X e Y

<!-- página 13 -->

Solución:  σxy = E xy − μx. μy
E xy =   x. y. f x, y = 3
14
yx

f(x,y) X h(y)
0 1 2
Y
0 3/28 9/28 3/28 15/28
1 3/14 3/14 0 3/7
2 1/28 0 0 1/28
g(x) 5/14 15/28 3/28 1
μx = E x =  x. g(x)
x
= 0 . 5
14 + 1 . 15
28 + 2 . 3
28 = 21
28 = 3
4
μy = E y =  y. ℎ(y)
y
= 0 . 15
28 + 1 . 3
7 + 2 . 1
28 = 14
28 = 1
2
σxy = 3
14 − 3
4 . 1
2 = 3
14 − 3
8 = 12 − 21
56 = − 9
56
De manera tal que si
en la extracción se
observan más biromes
azules se reducirá el
número de biromes
rojas.

<!-- página 14 -->

Aunque la covarianza indica el sentido de la dependencia entre X e Y, no indica
nada al respecto de la fuerza de esta relación, ya que está ligado a las escalas de
X e Y.
La versión de la covarianza libre de escala se llama “Coeficiente de correlación”:
ρx,y = σxy
σx . σy

Debería quedar claro para el lector que ρx,y no tiene las unidades de X e Y. El
coeficiente de correlación satisface la desigualdad –1 ≤ ρx,y ≤ 1. Toma un valor de
cero cuando σxy = 0.
Coeficiente de Correlación

<!-- página 15 -->

Ejemplo: Calcule ρx,y del ejemplo de los repuestos de bolígrafos.
Solución:
f(x,y) X h(y)
0 1 2
Y
0 3/28 9/28 3/28 15/28
1 3/14 3/14 0 3/7
2 1/28 0 0 1/28
g(x) 5/14 15/28 3/28 1
ρx,y = σxy
σx . σy
 con  σxy =  − 9
56
V x = σx2 =  E x2 −  E x 2 =  x2 g x −  x g(x)
x
2
x

σx2 = 1 2. 15
28 + 2 2. 3
28 − 3
4
2
= 27
28 − 9
16 = 45
112
σy2 = 1 2. 3
7 + 2 2. 1
28 − 1
2
2
= 16
28 − 1
4 = 16 − 7
28 = 9
28
ρx,y = − 9
56 . 1
45
112 . 9
28
= − 1
5

ρx,y = −0,4472

<!-- página 16 -->

Independencia estadística
Habíamos visto que si X e Y son variables aleatorias conjuntas con función de
distribución de probabilidad fx,y(x, y) y si es posible que fx,y(x, y) puede
factorizarse como un producto de las funciones de distribución de probabilidad
marginales g(x) y ℎ(y), entonces se dice que X e Y son variables aleatorias
independientes fx,y x, y = g x . ℎ y .
Podemos deducir entonces que en términos de esperanza X e Y podrían ser
independientes cuando observamos que un valor aleatorio para X, podría no
influir (o tiene la esperanza de no influir) en los valores aleatorios de Y si se
verifica que:
E(xy)  =  E(x) . E(y)

<!-- página 17 -->

Demostración de:
E(xy)  =   x . y . fx,y (x, y) dy dx
y=∞
y=−∞
x=∞
x=−∞

E(xy) = E(x). E(y) se cumple cuando  f x, y = g x . ℎ y ,
es decir, cuando X e Y son independientes.
Si X e Y son independientes, entonces sabemos que: fx,y(x, y)  =  g(x) . ℎ(y)
Por lo tanto reemplazando:
E(xy)  =   x y g(x) ℎ(y) dy dx
y=∞
y=−∞
x=∞
x=−∞
 =  x g(x) dx
x=∞
x=−∞
 .  y ℎ(y) dy
y=∞
y=−∞

E x                         E(y)
Entonces: E xy = E x . E y = μx. μy
Esta identidad, que es verificada cuando existe independencia, reafirma lo que se
postuló respecto de la covarianza:
σxy = E xy − μx. μy = 0 ya que X e Y son independientes

<!-- página 18 -->

Varianza de una combinación lineal
Habíamos visto que la V ax + b = a2V x . En el caso de un par de variables
aleatorias (X, Y) la varianza de una combinación lineal de estas variables, puede
demostrarse que resulta:

           V ax + by + c = a2V x + b2V y + 2abCOV(x, y)
Demostración para el caso de una VAC:
Por definición de Varianza:
V(ax + by + c)  = E[(ax + by + c)2]
(1)
−  [E(ax + by + c)
(2)
]2
V x = σx2 =  E(x2) −  E(x)2
Siendo (1): E[(ax + by + c)2] = E[a2x2 + b2y2 + c2 + 2 axby + byc + axc ]
= a2E x2 + b2E(y2) + c2 + 2abE xy + 2bcE y + 2acE(x)
y (2)2: [E(ax + by + c)]2= [aE x + bE y + c]2
= a2 E x 2 + b2 E(y) 2 + c2 + 2abE x E y + 2bcE y + 2acE x

<!-- página 19 -->

Por tanto: (1) - (2):
V(ax + by + c) = a2E x2 + b2E(y2) + c2 + 2abE xy + 2bcE y + 2acE x
 − a2 E x 2 − b2 E y 2 − c2 − 2abE x E y − 2bcE y −  2acE x
V(ax + by + c) = a2 E x2 − E x 2 + b2 E(y2 − E y 2] + 2ab[E xy − E x E(y)]
V(x) V(y) COV(x, y)
V(ax + by + c) = a2V(x) + b2V(y) + 2abCOV(x, y)
Agrupando términos
