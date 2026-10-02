# Tema 5_Parte B

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 5/Tema 5_Parte B.pdf` · 13 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Geométrica: ej. 6 (urna con reposición), P(X=x)=q^(x−1)·p, E=1/p, V=(1−p)/p². |
| 2 | Ej. 6: tabla f(x) para x=1 a 5, gráfico, E(X)=4 y comentario sobre moda. |
| 3 | Binomial negativa: definición, ej. 6b (hasta 2 rojas), fórmula b*(x; k, p). |
| 4 | Ej. 6b: tabla f(x) para x=2 a 6 y gráfico de barras. |
| 5 | Poisson: proceso de Poisson y sus tres propiedades. |
| 6 | Poisson: fórmula, λ y t; ej. 7 (llamadas, P(X<3)=2,77·10⁻³), E=V=λt. |
| 7 | Ej. 8 (ambulancias): P(X>3)=0,1426 y gráfico sesgado a la derecha. |
| 8 | Poisson se hace simétrica al crecer la media. ⚠ ver el PDF: gráficos de Poisson con μ=0,1, 2 y 5 (sin texto) |
| 9 | Ej. 9 (camiones): enunciado, P(X>15)=1−P(X≤15), uso de la tabla A.2. |
| 10 | Ej. 9: P(X≤15)=0,9513 leído de la tabla A.2; P(X>15)=0,0487. |
| 11 | Ej. 9 b: tabla f(x) de Poisson λt=10, x=0 a 15, y gráfico. |
| 12 | Binomial tiende a Poisson (n→∞, p→0, np constante); E=np=λt. |
| 13 | Ej. 10 (burbujas): binomial n=8000, p=0,001 aproximada por Poisson λt=8; P(X<7)=0,3134. |

<!-- página 1 -->

Distribución Geométrica
Ahora estamos interesados en el N° de pruebas hasta obtener el 1° éxito.
X: N° de pruebas ℎasta obtener el primer éxito
OJO: Acá X no puede tomar el valor CERO Probabilidad de éxito     = p
Probabilidad de fracaso  q = 1 − p
Sigue los postulados del Proceso de Bernoulli.
Ejemplo 6: De una urna que contiene 6 bolillas rojas (6R) y 2 bolillas negras (2N)
encontrar la función de distribución para la variable aleatoria X = número de pruebas
hasta obtener la primer bolilla negra. Las extracciones son con reposición.
Con
reposición
P X = 1 =
P X = 2 = 6
8 . 2
8 = q. p
P X = 3 = 6
8 . 6
8 . 2
8 = q2. p
P X = x = qx−1. p
N
R N
R R N
E x = 1
p V x = 1 − p
p2
2
8 = 1
4 = p

<!-- página 2 -->

Función de distribución: Tabla con los pares (x, f(x))
Evento X Prob.
N 1 0,25
RN 2 0,1875
RRN 3 0,1406
RRRN 4 0,1055
RRRRN 5 0,0791
P X = x = qx−1. p
0.000
0.050
0.100
0.150
0.200
0.250
0.300
1 2 3 4 5
Pruebas hasta obtener la primer bolilla negra
f(x)
Calcule la Esperanza y la Varianza
E x = 1
p = 4 Esperamos que en la cuarta extracción salga la primer bolilla negra
No necesariamente la E(X) = Pmax(X), depende de la forma de la distribución.
Por esto decimos que la Esperanza no indica lo más probable. Lo más probable
está asociada la Moda (lo más frecuente) en el análisis estadístico de los datos.

<!-- página 3 -->

Distribución Binomial Negativa
Ahora estamos interesados en el N° de pruebas hasta que se verifiquen k éxitos.
Como en el caso anterior:
Probabilidad de éxito     = p
Probabilidad de fracaso  q = 1 − p
Sigue los postulados del Proceso de Bernoulli.
Ejemplo 6 b: De una urna que contiene 6 bolillas rojas (6R) y 2 bolillas negras (2N)
encontrar la función de distribución para la variable aleatoria X = número de pruebas
hasta obtener dos bolillas rojas. Las extracciones son con reposición.
Con
reposición
P X = 2 = 6
8 . 6
8 = p2
P X = 3 = 2. 2
8 . 6
8 . 6
8 = 2. p2. q
P X = 4 = 3. q2. p2
R R
N R R
R N R
R R N
N N R R
N R N R
R N N R
P(X = 2, k = 2)
P(X = 3, k = 2)
P(X = 4, k = 2)
b∗ x; k, p = x − 1
k − 1 pkqx−k;        x ≥ k

<!-- página 4 -->

Función de distribución: Tabla con los pares (x, f(x))
X Prob.
2 0.563
3 0.281
4 0.105
5 0.035
6 0.011
b∗ x; k, p = x − 1
k − 1 pkqx−k
0.000
0.100
0.200
0.300
0.400
0.500
0.600
2 3 4 5 6
Pruebas hasta obtener 2 bolillas rojas
f(x)

<!-- página 5 -->

Distribución Poisson
Pruebas de ocurrencia en un Intervalo de Tiempo o en una Región.
Proceso de Poisson: resultados de un experimento aleatorio que se presentan
en un intervalo de tiempo o en una región.
Propiedades:

1° Los resultados que se observan son independientes entre intervalos de
tiempo o regiones (proceso sin memoria).

2° La probabilidad de que ocurra un solo resultado en un Δt → 0 depende de Δt.

3° La probabilidad de que ocurran 2 o más resultados (éxitos) en un intervalo
corto o pequeña región se aproxima a cero.

<!-- página 6 -->

P(x, λt) = e−λt(λt)x
x!
x: 0, 1, 2, …
l: N° de resultados promedio por unidad de tiempo o región.     l = ctte.
t: Longitud del intervalo (tiempo o región).
Ejemplo 7: El número de llamadas que se realizan en una central de atención al cliente de
una empresa es de 10 por minuto. Obtener la probabilidad que en el próximo minuto se
presenten menos de tres llamadas.
λ = 10 llamadas/min
Solución:
t = 1 minuto
x < 3 llamadas
P X < 3 = P X = 0 + P X = 1 + P X = 2
P x = 0 = e−10.1 10.1 0
0! = e−10 = 4,54. 10−5
P x = 1 = e−10.1 10.1 1
1! = 10e−10 = 4,54. 10−4
P x = 2 = e−10.1 10.1 2
2! = 50e−10 = 2,27. 10−3
P x < 3 = 4,54. 10−5 + 4,54. 10−4 + 2,27. 10−3 = 2,77. 10−3
E x = λt V(x) = λt

<!-- página 7 -->

Ejemplo 8: Un hospital cuenta con tres ambulancias. Si el número promedio de
requerimiento diario de ambulancias es de dos ambulancias ¿cuál es la probabilidad que
en un día cualquiera haya más de tres pedidos?
λ = 2 ambulancias/día
Solución:
t = 1 día
x > 3 ambulancias
P X > 3 = 1 − P X ≤ 3
P x = 0 = e−2.1 2.1 0
0! = e−2 = 0,135
P x = 1 = e−2.1 2.1 1
1! = 2e−2 = 0,271
P x = 2 = e−2.1 2.1 2
2! = 2e−2 = 0,271
P X ≤ 3 = P X = 0 + P X = 1 + P X = 2 + P(X = 3)
P x = 3 = e−2.1 2.1 3
3! = 4
3 e−2 = 0,180
P X ≤ 3 = 0,8574
P X > 3 = 1 − P X ≤ 3  P X > 3 = 0,1426
0.000
0.050
0.100
0.150
0.200
0.250
0.300
0 1 2 3 4 5
Número de ambulancias solicitadas en un día
f(x)
La distribución es sesgada a la derecha

<!-- página 8 -->

En el ejemplo anterior vimos que la distribución Poisson tiene una
asimetría positiva, sin embargo la forma de la distribución de Poisson se
vuelve cada vez más simétrica, incluso con forma de campana, a medida
que la media se hace más grande.

<!-- página 9 -->

Ejemplo 9: En una estación de carga llegan en promedio 10 camiones por día. La estación
puede abastecer hasta un máximo de 15 camiones.
a) ¿cuál es la probabilidad de que un día haya camiones que no puedan ser abastecidos?
b) Graficar la función de distribución.
λ = 10 camiones/día
Solución:
t = 1 día
x > 15 camiones
P X > 15 = 1 − P X ≤ 15
En lugar de calcular con la fórmula se puede usar la Tabla A.2
del Walpole, Miers y Miers que brinda la P(X ≤ x) para la
Distribución de Poisson.
a)

<!-- página 10 -->

Ejemplo 9: En una estación de carga llegan en promedio 10 camiones por día. La estación
puede abastecer hasta un máximo de 15 camiones.
a) ¿cuál es la probabilidad de que un día haya camiones que no puedan ser abastecidos?
b) Graficar la función de distribución.
λ = 10 camiones/día
Solución:
t = 1 día
x > 15 camiones
P X > 15 = 1 − P X ≤ 15
En lugar de calcular con la fórmula se puede usar la Tabla A1
del Walpole, Miers y Miers que brinda la P(X < x) para la
Distribución de Poisson.
P X ≤ 15 =
P X > 15 = 1 − 0,9513
P X > 15 = 0,0487
0,9513

<!-- página 11 -->

b) Tabla de función de distribución
0.000
0.020
0.040
0.060
0.080
0.100
0.120
0.140
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Número de camiones para abastecimiento en un día
f(x)
x f(x)
0 0.00005
1 0.00045
2 0.00227
3 0.00757
4 0.01892
5 0.03783
6 0.06306
7 0.09008
8 0.11260
9 0.12511
10 0.12511
11 0.11374
12 0.09478
13 0.07291
14 0.05208
15 0.03472

<!-- página 12 -->

Caso extremo:
Cuando n → ∞    y      p → 0 la b x; n, p → P(x; λt)
∗ n → ∞ Vamos hacia el espacio continuo o tiempo continuo (se acerca a Poisson).
* Independencia de las pruebas:  Igual premisa en ambas distribuciones.
∗ n → ∞ ⇒ p → 0 Para conservar le producto  n. p = ctte
E x = n. p
E x = λ. t
binomial
Poisson
Además, si  p → 0 es la 3° propiedad de Poisson.

<!-- página 13 -->

Ejemplo 10: En un proceso de fabricación donde se manufacturan productos de vidrio
ocurren defectos o burbujas, lo cual ocasionalmente hace que la pieza ya no se pueda
vender. Se sabe que, en promedio, 1 de cada 1000 artículos producidos tiene una o más
burbujas. ¿Cuál es la probabilidad de que una muestra aleatoria de 8000 tenga menos de 7
artículos con burbujas?
Solución:
f x; n, p =  n
x pxq n−x    ;   x:   V. A. D.  número de artículos con burbujas.
P(X < 7)
n:
p:
8000
0,001
X = número de artículos con burbujas. Es una V.A.D. Es dicotómica porque la
muestra tiene o no tiene burbujas.
Como  n → ∞    y      p → 0, b x; n, p → P(x; λt)
λt = 8000.0,001 = 8
Con la binomial: P X < 7 =  n
x pxq n−x
6
0

Con Poisson:  P X < 7 =  e−λt(λt)x
x!
6
0
= 0,3134 de la Tabla A.2
con m = 8   y   r = 6
de la Tabla A.1
0,1 ≤ p ≤ 0,9
               n ≤ 20
