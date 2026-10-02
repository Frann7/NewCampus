# Unidad 4

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 4/Unidad 4.pdf` · 7 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Esperanza: definición, E(x) discreta y continua. Ej. apostador con 3 monedas: E = −1. |
| 2 | Ej. duración de dispositivo f = 20000/x³ (x > 100): verifica f, E = 200 h. Ej. bolillas: E = 1,7. ⚠ ver el PDF: integrales impropias con límites y fracciones C(k,x) rotas |
| 3 | Esperanza de g(x) discreta y continua. Ej. lavadero: g = 50(x+1), E = $275/día, $8250/mes. |
| 4 | Propiedad E(ax+b) = aE(x)+b con demostración. Varianza: definición y fórmula alternativa E(x²) − E(x)². ⚠ ver el PDF: derivaciones con sumatorias, subíndices y exponentes desordenados |
| 5 | V(ax+b) = a²V(x) con demostración. Covarianza: definición, discreta y continua. |
| 6 | Demostración de Cov = E(xy) − μx·μy (continuo). Cov 0 no implica independencia; Cov no mide fuerza. ⚠ ver el PDF: dobles integrales con límites desordenados |
| 7 | Coeficiente de correlación (−1 ≤ ρ ≤ 1), independencia f = fx·fy, E(xy) = E(x)E(y) con prueba. |

<!-- página 1 -->

Unidad 4
-Esperanza matemática.
-Varianza.
-Covarianza.
-Coeficiente de correlación.
Esperanza Matemática

-Media de la Población o valor más probable (sólo si se trata de una distribución normal)
-Media o Valor Promedio de una muestra que caracteriza la población.
-Valor promedio de un conjunto de datos.
-”Cuando expresamos en términos de probabilidad entonces la media pasa a llamarse el valor esperado o
Esperanza Matemática.”

E(x)  =  ∑ (x . p(x))x    x Discreta
E(x)  = ∫ x. f(x) dx
∞
−∞   x Continua

Ejemplo: un apostador lanza 3 monedas: si salen 3 caras ó 3 cruces gana $5
      si salen 1 ó 2 caras pierde $3.

¿Cuál es la ganancia esperada del apostador?

Variable aleatoria X: Valor del dinero en las dos alternativas: x1 = +5, x2 = -3
Espacio muestral  = {ccc, ccs, csc, scc, css, scs, ssc, sss}
Eventos:
A1 = {ccc, sss}  →  P(A1)  =  1/8 +  1/8 = 1/4
A2 = {ccs, csc, scc, css, scs, ssc}  → P(A2)  =  6/8 =  3/4

Ωi P(Ωi)
ccc 1/8
ccs 1/8
csc 1/8
css 1/8
scc 1/8
scs 1/8
ssc 1/8
sss 1/8
Esperanza de la ganancia:
E(x) =  ∑(x . p(x))
x
  = x1. p(A1) +  x2. p(A2) = 5 . 1
4 − 3 . 3
4  =  −1
Por tanto en cada jugada se espera (o se tiene la esperanza de) perder $1.

Ejemplo: Sea X  la duración en horas de un dispositivo electrónico con la siguiente función:

<!-- página 2 -->

20000
x3  , x > 100

   0 , cualquier otro caso

a) Verificar que f(x) es una función de distribución de probabilidad.
b) Obtener E(x).

a) f(x) ≥ 0     ∀    x
            ∫ f(x)dx
+∞
−∞ = 1  :
∫ f(x) dx
∞
−∞
 = ∫ 20000
x3  dx
∞
100
 = 20000 . ∫ x−3  dx
∞
100
 =  20000. x−2
−2 |
100
∞

=   20000. [  x−2
2 |
∞
100
] = 10000. [ 1
1002 − lim
x→∞
1
x2] =  1

b)
∫ x. f(x) dx
∞
−∞
 = ∫ x. 20000
x3  dx
∞
100
 = 20000 . ∫ x−2  dx
∞
100
 =  20000. x−1
−1 |
100
∞

=   20000. [  x−1
1 |
∞
100
] = 20000. [ 1
100 − lim
x→∞
1
x] =  200
E(x)  =  200 ℎs

Se espera que el dispositivo dure 200 horas.

Ejemplo: Una caja posee 4 bolillas rojas y 3 verdes. Se extraen 3 bolillas sin reposición. ¿Cuántas bolillas rojas
se esperan obtener?
x f(x)
0 1/35
1 12/35
2 18/35
3 4/35

f(x)  =
(k
x) (N − k
n − x )
(N
n)

N: n° total de bolillas
k: n° de bolillas rojas
n: n° de bolillas que pueden extraerse

E(x)  =  ∑ x . f(x)
x
 =  0 . 1
35  + 1 . 12
35  +  2 . 18
35  +  3 . 4
35  =  60
35  =  1,7
No es posible esperar quitar 1,7 bolillas rojas, por tanto lo más lógico es suponer tomar 2.

<!-- página 3 -->

El valor más probable no es lo mismo que el valor promedio ya que el valor promedio no es necesariamente
uno de los resultados del experimento.

Esperanza de Función de Función

Esperanza Matemática de una función de variable aleatoria (discreta o continua) y supongamos que nuestro
interés no es la variable aleatoria X, sino una función de x, digamos Y = g(x). Siendo f(x) la función de
probabilidad, nos interesa hallar la esperanza de g(x), E[g(x)]:
V.A.D.
μg(x) = E[g(x)] = ∑ g(x) . f(x)
x

V.A.C.
μg(x) = E[g(x)] = ∫ g(x) . f(x)
+∞
−∞
dx

De manera tal que E[Y] funciona como un operador aplicado a la función Y.

Ejemplo: en un lavadero de autos ingresan x vehículos por día con una distribución de probabilidad f(x).
El empleado gana por día en función de los autos que lava g(x) = 50(x+1) pesos.
¿Cuánto espera ganar el empleado por día? E[g(x)]
¿y por mes?

x f(x) g(x)
0 1/64 = 0,015625 50
1 3/64 = 0,046875 100
2 ⅙ = 0,0625 150
3 ⅛ = 0,125 200
4 ¼ = 0,25 250
5 ¼ = 0,25 300
6 ⅛ = 0,125 350
7 1/16 = 0,0625 400
8 3/64 = 0,046875 450
9 1/64 = 0,015625 500

Considere: μx =  E(x) = ∑ x . f(x)x   μg(x) = E[g(x)] = ∑ g(x) . f(x)x

E[g(x)]  = ∑ g(x) . f(x)
x
  =  50 . 1/64 +  100 . 3/64 + 150 . 1/16 +  200 . 1/8 +
250 . 1/4 +  300 . 1/4 +  350 . 1/8 + 400 . 1/16 +  450 . 3/64 + 500 . 1/64 =  275

Por tanto se espera recibir $275 por día y $8250 al cabo de 30 días.

<!-- página 4 -->

Propiedades:
μg(x) = E[g(x)] = ∑ g(x) . f(x)x    V.A.D
μg(x) = E[g(x)] = ∫ g(x) . f(x)
∞
−∞   dx V.A.C

E(x): la esperanza de una combinación lineal de variable aleatoria x es la combinación lineal de E(x):
Sea E[g(x)]  =  E[ax + b]  =  a . E(x) +  b. El operador E[Y] cumple la propiedad de combinación lineal.

Demostración:
E[g(x)]  = ∑[g(x)  +  f(x)]
x
  = ∑[(ax + b) . f(x)]
x

E[g(x)] = ∑[ax. f(x)] + ∑[b
x
. f(x)]
x
  = a. ∑[x . f(x)]
x
+ b. ∑ f(x)
x

=  a . E(x)  +  b

Varianza

Sea X una variable aleatoria con ~ f(x) y E(x)=∑ x. f(x)x , la varianza de x, σx
2 =E[(x − E(x))2]

Demostración:
σx
2 =
∑ (xi−μ)2x
N = ∑ [(x − μ)2. f(x)]x      con      E(x)  = μ = ∑ [x. f(x)]x    y    g(x) = [x − E(x)]2
entonces
σx
2 = ∑[(x − E(x))2 . f(x)]
x
  = ∑[g(x). f(x)]
x
= E[g(x)]   = E[(x − E(x))2]

Equivalencias (fórmula alternativa de σx
2):
σx
2  = E[(x − μx)2]  =  E[x2  −  2xμx + μx
2] ,  Distributiva del operador E.
 =  E(x2)  −  2E(x μx) + E(μx
2)
 = E(x2) −  2μx E(x) +  μx
2E(1) = E(x2) −  2μx
2 + μx
2 = E(x2) − μx
2 = E(x2) − E(x)2

Esta equivalencia es ideal para aplicar en lenguaje de computación:

σx
2 = E[(x − μx)2] =
∑ (xi−μ)2x
N :

>  Con la fórmula original necesitaríamos pasar por los datos dos veces: Un Loop para calcular
∑ xi
N
1 ,   con lo que luego calculamos μ  y  otro para   ∑ (xi − μ)2N
1  .

 -> Con la nueva fórmula sólo es necesario pasar una vez por todos los datos: Un sólo Loop para calcular
∑ (xi)N
1       y     ∑ (xi
2)N
1 . Luego E(x2) =
∑ (xi
2)N1
N     y   E(x) =
∑ (xi)N1
N . Por lo que:

σx
2 = E(x2) − E(x)2

<!-- página 5 -->

Varianza de una combinación lineal g(x) = ax+b:

La Varianza de la V.A. x es:   V(x) = σx
2 =  E(x2) −  E(x)2

La Varianza de una función g(x) de V. A. x es:

V(g(x))  =  E[g(x)2]  −  E[g(x)]2   con    g(x) = ax+b

  = V(ax + b)  = E[(ax + b)2] ⏟
(1)
−  [E(ax + b)⏟
(2)
]2
Siendo (1):
                        = E[(ax + b)2] = E[a2x2 + 2abx + b2]

  = a2E(x2)  +  2abE(x) + b2
Y (2)2:
  = [E(ax + b)]2 = [aE(x) + b]2 = a2[E(x)]2 + 2abE(x) + b2

Por tanto con (1) y (2):

V(g(x))  =  a2E(x2) +  2abE(x) + b2  − {a2[E(x)]2 + 2abE(x) + b2}

                 = a2E(x2) +  2abE(x) + b2 – a2[E(x)]2 − 2abE(x) − b2

a2[E(x2)  − E(x)2] = a2V(x)

V(g(x)) = V(ax + b) = a2V(x)

Covarianza

Medida de asociación o dependencia entre 2 variables aleatorias. La covarianza puede ser positiva o negativa
(la varianza siempre es positiva).

Si X e Y son variables aleatorias con distribución de probabilidad conjunta (d.d.p.c) fx,y(x, y), entonces la
covarianza de (x,y) ó COV(x, y)  = σxy

σxy = E[(x − μx) . (y − μy)]

=  ∑ ∑ (x − μx) . (y − μy) . fx,y(x, y)yx   Discreto
= ∫ ∫ (x − μx) . (y − μy) . fx,y(x, y) dx dy
∞
−∞
∞
−∞  Continuo

<!-- página 6 -->

Demostrar la fórmula alternativa de la COV: σxy = E(xy) − μx. μy  para el caso continuo:

σxy = E[(x − μx) . (y − μy)]

σxy = ∫ ∫ (x − μx) . (y − μy) . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞

σxy = ∫ ∫ [x. y. fx,y(x, y)  − μx . y .  fx,y(x, y)  − x . μy . fx,y(x, y)  + μx . μy .  fx,y(x, y)] dx dy
x=∞
x=−∞
y=∞
y=−∞

σxy = ∫ ∫ x . y . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
 − μx ∫ ∫ y . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞

− μy ∫ ∫ x .  fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
+ μx . μy ∫ ∫ fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞

Tenemos que:
∫ ∫ x . y . fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
 =  E(xy)
Como:
∫ fx,y(x, y) dx
x=∞
x=−∞
=  ℎ(y)  →  Función marginal de y
Entonces:
∫ ∫ y .  fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
 =   = ∫ y . ℎ(y) dy
y=∞
y=−∞
  = μy
Del mismo modo:
∫ ∫ x .  fx,y(x, y) dx dy
x=∞
x=−∞
y=∞
y=−∞
 = μx
Además:
∫ ∫ fx,y(x, y) dx dy
∞
−∞
∞
−∞
 =  1

Reemplazando estos valores en la función anterior nos queda:

σxy = E(xy) − μx. μy − μy. μx + μx. μy

σxy = E(xy) − μx. μy

El signo de la covarianza indica la relación directa o inversa entre X e Y. Si son estadísticamente
independientes, la covarianza dará 0. Lo opuesto no es necesariamente cierto, es decir si la Covarianza da 0 no
necesariamente son estadísti camente independientes. La covarianza sólo describe la relación lineal entre dos
variables aleatorias. Por consiguiente, si una covarianza entre X y Y es cero, X y Y podrían tener una relación
no lineal, lo cual significa que no necesariamente son independ ientes. Serán independientes en el caso que la
fdp o fdpc sean de carácter lineal.
Aunque la covarianza indica el sentido de la dependencia entre X e Y, no indica nada al respecto de la fuerza de
esta relación, ya que está ligado a las escalas de X e Y.

<!-- página 7 -->

La versión de la covarianza libre de escala se llama “Coeficiente de correlación”:

ρx,y = σxy
σx .σy

Debería quedar claro para el lector que  ρx,y no tiene las unidades de X e Y. El coeficiente de correlación
satisface la desigualdad –1 ≤ ρx,y ≤ 1. Toma un valor de cero cuando σxy = 0.

Independencia: Si X e Y son variables aleatorias conjuntas con función de distribución de probabilidad
fx,y(x, y) y si es posible que fx,y(x, y) puede factorizarse como un producto de las funciones de distribución de
probabilidad marginales fx(x)(ó g(x)) y fy(y)(ó ℎ(y)), entonces se dice que X e Y son variables aleatorias
independientes.
fx,y(x, y) = fx(x) . fy(y)

Se dice que X e Y son independientes si el valor de la variable X no tiene efecto sobre el valor de la variable Y,
y viceversa.
Alternativamente, X e Y podrían ser dependientes: cuando observamos que un valor aleatorio para X, podría
influir en los valores aleatorios de Y. Por ejemplo, X podría ser la altura de una persona seleccionada al azar, e
Y podría ser el peso. En general, los valores más grandes de X se asocian con valores más grandes de Y.

Esta propiedad puede aplicarse sobre esperanza:

E(xy)  =  E(x) . E(y)

Nota: existen casos particulares donde esta propiedad se cumple aun cuando X e Y sean dependientes.

De manera general puede expresarse como: E[g(x) . ℎ(y)]  =  E[g(x)] . E[ℎ(y)]. Es decir, la independencia de
dos variables aleatorias implica que tanto la covarianza como la correlación son cero. Este resultado nos ayuda
a demostrar un resultado más general, que es que las funciones de dos variables aleatorias independientes
también son independientes

Prueba:
E(xy)  = ∫ ∫ x . y .  fx,y(x, y) dy dx
y=∞
y=−∞
x=∞
x=−∞

Si X e Y son independientes: fx,y(x, y)  =  g(x) . ℎ(y)

E(xy)  = ∫ ∫ x . y . g(x) . ℎ(y) dy dx
y=∞
y=−∞
x=∞
x=−∞
 = ∫ x g(x) dx
x=∞
x=−∞
 . ∫ y ℎ(y) dy
y=∞
y=−∞

Donde se sabe que: ∫ x g(x) dx
x=∞
x=−∞  = E(x) y ∫ y ℎ(y) dy
y=∞
y=−∞   =  E(y)

Al integrar:
E(xy) = =  E(x) . E(y)
