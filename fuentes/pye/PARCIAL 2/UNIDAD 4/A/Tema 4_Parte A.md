# Tema 4_Parte A

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 4/A/Tema 4_Parte A.pdf` · 22 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Portada: motivación de la esperanza, pasar del análisis estadístico a prever a futuro. |
| 2 | Definición de esperanza matemática: valor promedio en términos de probabilidad. |
| 3 | Resumen E(x): discreta (Σ x·p) y continua (∫ x·f dx); media de datos agrupados/sin agrupar. ⚠ ver el PDF: símbolos Σ/∫ perdidos y grilla de la lámina desordenada |
| 4 | Ej. apostador con 3 monedas: planteo, X = +5 / −3, espacio muestral y eventos (árbol). |
| 5 | Ej. apostador: tabla de ocho resultados con 1/8, P(gana) = 1/4, P(pierde) = 3/4, E = −$1. |
| 6 | Ej. dispositivo f(x) = 20000/x³, x > 100: planteo, a) verificar f ≥ 0 e integral = 1. |
| 7 | Ej. dispositivo: cuenta de la integral = 1 y b) E(x) = 200 h. ⚠ ver el PDF: integrales con límites y fracciones de la cuenta desordenadas |
| 8 | Ej. bolillas (4 rojas, 3 verdes, 3 extraídas): planteo; tabla x f(x) vacía. |
| 9 | Ej. bolillas: arranca la tabla, x = 0 con 3/7·2/6·1/5 = 1/35. |
| 10 | Ej. bolillas: f(0) = 1/35 y f(1) = 12/35 por secuencias R/V. |
| 11 | Ej. bolillas: se suma f(2) = 18/35. |
| 12 | Ej. bolillas: se suma f(3) = 4/35. |
| 13 | Ej. bolillas: tabla completa 1/35, 12/35, 18/35, 4/35 (repite la página 12). |
| 14 | Ej. bolillas: mismas f(x) calculadas con la fórmula hipergeométrica C(4,x)·C(3,3−x)/C(7,3). ⚠ ver el PDF: combinatorios (C(4,x)·C(3,3−x)/C(7,3)) rotos |
| 15 | Ej. bolillas: E(x) = 60/35 = 1,7; valor más probable (2) distinto del promedio. |
| 16 | Esperanza de una función g(x): fórmulas discreta y continua; E como operador. |
| 17 | Ej. lavadero g(x) = 50(x+1): tabla f(x) y g(x), E[g(x)] = $275/día, $8250 en 30 días. |
| 18 | Propiedad lineal E(ax+b) = aE(x)+b y su demostración. |
| 19 | Varianza: definición σ² = E[(x − E(x))²] y demostración desde E[g(x)]. ⚠ ver el PDF: sumatorias, fracciones y subíndices desordenados |
| 20 | Fórmula alternativa de la varianza: σ² = E(x²) − E(x)², desarrollo del cuadrado. ⚠ ver el PDF: desarrollo con exponentes y subíndices desordenados |
| 21 | Varianza de g(x)=ax+b: arma (1) E[(ax+b)²] y (2) [E(ax+b)]². ⚠ ver el PDF: exponentes y esperanzas (1)/(2) desordenados |
| 22 | Se restan (1) y (2): V(ax+b) = a²V(x). ⚠ ver el PDF: exponentes y términos (1)/(2) desordenados |

<!-- página 1 -->

¿La Matemática tiene Esperanza? ¿de qué?
w – Cap 4
Vimos que un análisis estadístico permitía tener conocimiento del
comportamiento de una variable en el pasado. Para llevar adelante
este análisis necesitamos registrar un número considerable de datos
de la variable.
¿Permite este análisis hacer previsiones a futuro? ¿Cómo espero
que se comporte la variable en el futuro?  ESPERANZA

<!-- página 2 -->

Esperanza Matemática: Es el valor promedio de la
variable en estudio expresado en términos de
probabilidad de ocurrencia para el futuro.
Valor Promedio de una muestra que caracteriza la
población o valor más probable (sólo si se trata de
una distribución normal).

Cuando expresamos en términos de probabilidad
entonces la media pasa a llamarse:
      Valor Esperado o Esperanza Matemática

<!-- página 3 -->

E(x)  =   x . p(x)
x

Esperanza Matemática:    E(x)
Análisis Estadístico: Valor promedio de una muestra de datos
X =   Xi
n
i=1
n  X =   (XPMi . fri)
k
i=1

E(x)  =  x. f(x) dx
∞
−∞

Datos sin agrupar Datos agrupados
V.A.D.
V.A.C.
Función de distribución
Función de densidad de probabilidad

<!-- página 4 -->

Ejemplo: un apostador lanza 3 monedas: si salen 3 caras ó 3 cruces gana $5 si
salen 1 ó 2 caras pierde $3.

¿Cuál es la ganancia esperada del apostador?
Variable aleatoria X:  Valor del dinero en las dos alternativas: x1 = +5,   x2 = -3
Gana Pierde
Espacio muestral:  = {ccc, ccs, csc css, scc, scs, ssc, sss}
C
S
C
S
C
S
C
S
C
S
C
S
C
S
C  C  C
C  C  S
C  S  C
C  S  S
S  C  C
S  C  S
S  S  C
S  S  S
Eventos:
A1 = ccc, sss  → Gana $ 5
A2 = ccs, csc, scc, css, scs, ssc
Pierde $ 3
E(x)  =   x . p(x)
x

<!-- página 5 -->

Ωi P(Ωi)
ccc 1/8
ccs 1/8
csc 1/8
css 1/8
scc 1/8
scs 1/8
ssc 1/8
sss 1/8
Tabla de distribución:
A1 = {ccc, sss}  →  P(x1)  =  1/8 +  1/8 = 1/4
A2 = {ccs, csc, scc, css, scs, ssc}  → P(x2)  =  6/8 =  3/4
E(x)  =   x . p(x)
x

Cálculo de la Esperanza
E x =   x . p x
x
  = x1. p x1 +  x2. p x2 = $ 5 . 1
4 + −$ 3 . 3
4  =  −$ 1
Por tanto en cada jugada se espera (o se tiene la esperanza de) perder $1.

<!-- página 6 -->

Ejemplo: Sea X  la duración en horas de un dispositivo electrónico con la siguiente
función:
20000
x3  , x  > 100
0 , cualquier otro caso
a) Verificar que f(x) es una función de distribución de probabilidad.
b) Obtener E(x).
f x ≥ 0     ∀    x
Solución:
a)
 f x dx
+∞
−∞
= 1

<!-- página 7 -->

 f(x) dx
∞
−∞
 =  20000
x3  dx
∞
100
 = 20000 .  x−3  dx
∞
100
 =  20000. x−2
−2
100
∞

=   20000.   x−2
2
∞
100
= 10000. 1
1002 − lim
x→∞
1
x2 =  1
b)
 x. f(x) dx
∞
−∞
 =  x. 20000
x3  dx
∞
100
 = 20000 .  x−2  dx
∞
100
 =  20000. x−1
−1
100
∞

E(x)  =  x. f(x) dx
∞
−∞

=   20000.   x−1
1
∞
100
= 20000. 1
100 − lim
x→∞
1
x =  200
E(x)  =  200 ℎs

<!-- página 8 -->

Ejemplo: Una caja posee 4 bolillas rojas y 3 verdes. Se extraen 3 bolillas
sin reposición. ¿Cuántas bolillas rojas se esperan obtener?
E(x)  =   x . p(x)
x
  V.A.D.
Tabla de distribución:
x f(x)
Variable aleatoria X:  Número de bolillas rojas

<!-- página 9 -->

Ejemplo: Una caja posee 4 bolillas rojas y 3 verdes. Se extraen 3 bolillas
sin reposición. ¿Cuántas bolillas rojas se esperan obtener?
E(x)  =   x . p(x)
x
  V.A.D.
Tabla de distribución:
x f(x)
0
1
2
3
Variable aleatoria X:  Número de bolillas rojas
x = 0 3
7 . 2
6 . 1
5 =  1
35
V   V    V

<!-- página 10 -->

Ejemplo: Una caja posee 4 bolillas rojas y 3 verdes. Se extraen 3 bolillas
sin reposición. ¿Cuántas bolillas rojas se esperan obtener?
E(x)  =   x . p(x)
x
  V.A.D.
Tabla de distribución:
x f(x)
0 1/35
1
2
3
Variable aleatoria X:  Número de bolillas rojas
x = 0 3
7 . 2
6 . 1
5 =  1
35
V   V    V
x = 1 R   V    V    +     V   R    V    +    V    V    R
4
7 . 3
6 . 2
5    +      3
7 . 4
6 . 2
5    +     3
7 . 2
6  . 4
5 =  12
35

<!-- página 11 -->

Ejemplo: Una caja posee 4 bolillas rojas y 3 verdes. Se extraen 3 bolillas
sin reposición. ¿Cuántas bolillas rojas se esperan obtener?
E(x)  =   x . p(x)
x
  V.A.D.
Tabla de distribución:
x f(x)
0 1/35
1 12/35
2
3
Variable aleatoria X:  Número de bolillas rojas
x = 0 3
7 . 2
6 . 1
5 =  1
35
V   V    V
x = 1 R   V    V    +     V   R    V    +    V    V    R
4
7 . 3
6 . 2
5    +      3
7 . 4
6 . 2
5    +     3
7 . 2
6  . 4
5 =  12
35
x = 2 R   R    V    +     R   V    R    +    V    R    R
4
7 . 3
6 . 3
5    +      4
7 . 3
6 . 3
5    +     3
7 . 4
6  . 3
5 =  18
35

<!-- página 12 -->

Ejemplo: Una caja posee 4 bolillas rojas y 3 verdes. Se extraen 3 bolillas
sin reposición. ¿Cuántas bolillas rojas se esperan obtener?
E(x)  =   x . p(x)
x
  V.A.D.
Tabla de distribución:
x f(x)
0 1/35
1 12/35
2 18/35
3
Variable aleatoria X:  Número de bolillas rojas
x = 0 3
7 . 2
6 . 1
5 =  1
35
V   V    V
x = 1 R   V    V    +     V   R    V    +    V    V    R
4
7 . 3
6 . 2
5    +      3
7 . 4
6 . 2
5    +     3
7 . 2
6  . 4
5 =  12
35
x = 2 R   R    V    +     R   V    R    +    V    R    R
4
7 . 3
6 . 3
5    +      4
7 . 3
6 . 3
5    +     3
7 . 4
6  . 3
5 =  18
35
x = 3 R   R   R
4
7 . 3
6 . 2
5 =  4
35

<!-- página 13 -->

Ejemplo: Una caja posee 4 bolillas rojas y 3 verdes. Se extraen 3 bolillas
sin reposición. ¿Cuántas bolillas rojas se esperan obtener?
E(x)  =   x . p(x)
x
  V.A.D.
Tabla de distribución:
x f(x)
0 1/35
1 12/35
2 18/35
3 4/35
Variable aleatoria X:  Número de bolillas rojas
x = 0 3
7 . 2
6 . 1
5 =  1
35
V   V    V
x = 1 R   V    V    +     V   R    V    +    V    V    R
4
7 . 3
6 . 2
5    +      3
7 . 4
6 . 2
5    +     3
7 . 2
6  . 4
5 =  12
35
x = 2 R   R    V    +     R   V    R    +    V    R    R
4
7 . 3
6 . 3
5    +      4
7 . 3
6 . 3
5    +     3
7 . 4
6  . 3
5 =  18
35
x = 3 R   R   R
4
7 . 3
6 . 2
5 =  4
35

<!-- página 14 -->

Ejemplo: Una caja posee 4 bolillas rojas y 3 verdes. Se extraen 3 bolillas
sin reposición. ¿Cuántas bolillas rojas se esperan obtener?
E(x)  =   x . p(x)
x
  V.A.D.
Tabla de distribución:
x f(x)
0 1/35
1 12/35
2 18/35
3 4/35
Variable aleatoria X:  Número de bolillas rojas
f 0 =  n1 . n2
N  =
4
0  . 3
3
7
3
= 1.1
35
f 1 =  n1 . n2
N  =
4
1  . 3
2
7
3
= 4.3
35
f 2 =  n1 . n2
N  =
4
2  . 3
1
7
3
= 6.3
35 f 3 =  n1 . n2
N  =
4
3  . 3
0
7
3
= 4.1
35

<!-- página 15 -->

Ejemplo: Una caja posee 4 bolillas rojas y 3 verdes. Se extraen 3 bolillas sin
reposición. ¿Cuántas bolillas rojas se esperan obtener?
E(x)  =   x . p(x)
x
  V.A.D.
Tabla de distribución:
x f(x)
0 1/35
1 12/35
2 18/35
3 4/35
Variable aleatoria X:  Número de bolillas rojas
E(x)  =   x . f x
x
 =  0 . 1
35  + 1 . 12
35  +  2 . 18
35  +  3 . 4
35
=  60
35  =  1,7
No es posible esperar obtener 1,7 bolillas rojas, por
tanto lo más lógico es suponer 2 bolillas rojas.
El valor más probable (2 bolillas rojas) no es lo mismo que el valor promedio (1,7 bolillas
rojas) ya que el valor promedio no es necesariamente uno de los resultados del experimento.

<!-- página 16 -->

Esperanza de Función de Función
Esperanza Matemática de una función de variable aleatoria (discreta o continua).
Supongamos que nuestro interés no es la variable aleatoria X, sino una función de
x, digamos Y = g(x). Siendo f(x) la función de probabilidad, nos interesa hallar la
esperanza de g(x), E[g(x)]:
V.A.D. μg(x) = E[g(x)] =  g(x) . f(x)
x

V.A.C. μg(x) = E[g(x)] =  g(x) . f(x)
+∞
−∞
dx
De manera tal que E[Y] funciona como un operador aplicado a la función Y.
E[Y] =  Y . f(x)
x
 E[Y] =  Y . f(x)
+∞
−∞
dx V.A.D. V.A.C.

<!-- página 17 -->

Ejemplo: en un lavadero de autos ingresan x vehículos por día con una distribución de
probabilidad f(x).
El empleado gana por día en función de los autos que lava g(x) = 50(x+1) pesos.
¿Cuánto espera ganar el empleado por día? E[g(x)]
¿y por mes?
x f(x) g(x)
0 1/64 = 0,015625   50
1 3/64 = 0,046875 100
2 ⅙ = 0,0625 150
3 ⅛ = 0,125 200
4 ¼ = 0,25 250
5 ¼ = 0,25 300
6 ⅛ = 0,125 350
7 1/16 = 0,0625 400
8 3/64 = 0,046875 450
9 1/64 = 0,015625 500
μx =  E(x) =  x . f(x)
x

μg(x) = E[g(x)] =  g(x) . f(x)
x

Entonces:
E g x =  g x . f x
x

E g x =  50 . 1/64 +  100 . 3/64 + 150 . 1/16
+  200 . 1/8 +  250 . 1/4 +  300 . 1/4
+  350 . 1/8 + 400 . 1/16 +  450 . 3/64
+ 500 . 1/64 =  275
Por tanto se espera recibir $275 por día y $8250 al
cabo de 30 días.

<!-- página 18 -->

Propiedades:
E(x): la esperanza de una combinación lineal de variable aleatoria x es la combinación
lineal de E(x):

Sea E[g(x)]  =  E[ax + b]  =  a . E(x)  +  b.
El operador E[Y] cumple la propiedad de combinación lineal.
Demostración: E[g(x)]  =  [g x . f(x)]
x
  =  [(ax + b) . f(x)]
x

E g x =  ax. f x +   [b
x
. f(x)]
x
  = a.  [x . f x ]
x
+ b.  f(x)
x

E g x =  a . E(x)  +  b

<!-- página 19 -->

Varianza
Sea X una variable aleatoria con ~ f(x) y E(x)= x. f(x)x , la varianza de x,
σx2 es:
                                                  σx2 = E[(x − E(x))2]
Demostración:
σx2 =
 xi − μ 2x
N =  x − μ 2. f(x)
x
  con  E(x)  = μ =  x. f(x)
x
 y
g x = x − E(x) 2
Entonces:
σx2 =  [(x − E(x))2 . f(x)]
x
  =  [g x . f x ]
x
= E[g(x)]   = E[(x − E(x))2]

<!-- página 20 -->

Equivalencias (fórmula alternativa de σx2):
σx2  = E[(x − μx)2]  =  E[x2  −  2xμx + μx2]
=  E(x2)  −  2E(x μx) + E(μx2)
= E x2 −  2μx E x + μx2E 1 = E x2 −  2μx2 + μx2

σx2 = E x2 − μx2

σx2 = E x2 − E x 2

<!-- página 21 -->

Varianza de una combinación lineal g(x) = ax+b
La Varianza de la V .A. x es: V x = σx2 =  E(x2) −  E(x)2
La Varianza de una función g(x) de V . A. x es: V g(x)  =  E[g x 2] −  E[g(x)]2
con    g(x) = ax+b
V g(x) = V(ax + b)  = E[(ax + b)2]
(1)
−  [E(ax + b)
(2)
]2
Siendo (1): E[(ax + b)2] = E[a2x2 + 2abx + b2]
= a2E(x2) +  2abE(x) + b2
y (2)2: [E(ax + b)]2= [aE x + b]2= a2 E x 2 + 2abE(x) + b2

<!-- página 22 -->

Por tanto con (1) y (2):
V g(x) =  a2E(x2) +  2abE(x) + b2  −  a2 E(x) 2 + 2abE(x) + b2
V g(x) = a2E x2 +  2abE x + b2 – a2 E x 2 − 2abE x − b2
(1) (2)
V g(x) = a2[E(x2) − E(x)2] = a2V(x)
V g(x) = V(ax + b) = a2V(x)
