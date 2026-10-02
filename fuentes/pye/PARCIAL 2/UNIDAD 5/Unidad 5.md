# Unidad 5

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 5/Unidad 5.pdf` · 4 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Repaso (frecuencia relativa, E, V.A.D./V.A.C.); lista de distribuciones; uniforme. |
| 2 | Uniforme (E, V), binomial (Bernoulli), hipergeométrica: fórmula, E, V, aproximación a binomial. |
| 3 | Geométrica, binomial negativa y Poisson (propiedades, fórmula, λ y t). |
| 4 | Poisson: E=V=λt, binomial→Poisson; ejemplo de llamadas (P(X<3)≈0,0028). |

<!-- página 1 -->

Unidad 5
Repaso:
*Vimos cómo se pueden calcular probabilidades de ocurrencia de eventos a partir de la Estadística descriptiva
⇒ Análisis de datos tomados de una muestra del objeto de estudio.

Distribuciones empíricas:
Tablas, Gráficos, Histogramas.

P(A)  =  n/N =  fr → Tablas de frecuencias relativas

*Vimos que algunos parámetros como X se pueden expresar en términos de Probabilidad.
X    → E(x)  = μ
Proceso muestral ↧ Esperanza (valor esperado de la población)
  Inferencia estadística

La inferencia estadística es el conjunto de métodos y técnicas que permiten inducir, a partir de la información
empírica proporcionada por una muestra, cu ál es el comportamiento de una determinada población con un
riesgo de error medible en términos de probabilidad.

S2  → V(x)  = σ2
S  → σ
V. A. D. → Función de Distribución     | VAD → f.d.
V. A. C. →         Función de Densidad de Probabilidad | VAC → f.d.p

*Vimos que con las funciones de distribución o función de densidad de probabilidad se pueden calcular
probabilidades de eventos.
Ej:
X → V. A. C
P(X >  2)  =  ∫ f(x) dx
∞
2   → f.d.p. de V.A.C

X → V. A. D
P(X ≥  2)  =  ∑ f(x) ∞
2   → f.d. de V.A.D

Vamos ahora a estudiar en más detalle estas f(x) para V.A.D:
● Distribución Uniforme
● Distribución Binomial
● Distribución Hipergeométrica
● Distribución Geométrica
● Distribución Binomial Negativa
● Distribución Poisson

Distribuciones Discretas de probabilidad

Describen el comportamiento de una V.A.D. por su distribución de probabilidad o cuantía.

Distribución uniforme
Cada uno de los elementos del espacio muestral toma probabilidades idénticas.

<!-- página 2 -->

f(x, k)  =
1
k  ; x = x1, x2, . . . ,  xk k elementos del espacio muestra.
E(x) = μ = ∑ x f(x, k)
k
1
= 1
k ∑ x
k
1

V(x) = σ2 = ∑(x − μ)2 f(x, k)
k
1
 = 1
k  ∑(x − μ)2
k
1

Distribución Binomial
 Pruebas repetidas con 2 resultados posibles (dicotómica: éxito o fracaso).
 Son independientes. El resultado de la anterior no incide en el resultado de la próxima prueba.
 La probabilidad no varía para cada prueba.
 Extracción con reemplazo si n es finito.
 p =  constante.
 E(x) = n. p
 V(x) = n. p. q

La variable aleatoria X sigue un Proceso de Bernoulli
-El experimento consiste en n pruebas que se repiten.
-Es dicotómica (éxito o fracaso).
-La probabilidad de éxito se mantiene constante en cada prueba.
-Las pruebas que se repiten son independientes.

Distribución Hipergeométrica
Una variable aleatoria x tiene una distribución Hipergeométrica si el resultado de un experimento consiste en
pruebas dependientes (sin reemplazo ⇒  p ≠ constante).
Pruebas repetidas con 2 posibilidades (éxito o fracaso).

N: n° total de elementos
n: n° de extracciones o pruebas
k: n° de elementos de éxito
x: n° de éxitos de la muestra

H(N, n, k, x)  =
(k
x) (N − k
n − x )
(N
n)

 con:  x = 0,1,2, … , k

E(x) = nk
N ;                    V(x)  = (nk
N ) (1 − k
n) (N − n
N − 1)

¿Qué pasa si N es grande y n es pequeño?

n << N  ⇒
k
N = p → constante ⇒ E(x) → n. p V(x) = n. p. q

<!-- página 3 -->

Podría decirse que si N es grande y n es pequeño la distribución Hipergeométrica tiene a una distribución
Binomial.

Distribución Geométrica
Ahora estamos interesados en el N° de pruebas que hay que hacer hasta obtener el 1° éxito.
x: N° de pruebas ℎasta obtener el primer éxito
Probabilidad de éxito     = p
Probabilidad de fracaso  q = 1 − p
Proceso continuo.
Extracción con reemplazo.

g(x, p) = qx−1. p
E(x) = 1
p

V(x) = 1 − p
p2

Distribución Binomial Negativa
N° de pruebas hasta que se verifiquen k éxitos.
-Pruebas independientes.
-Probabilidad de éxito es p y de fracaso 1 − p (p es constante en todos los experimentos).

b∗(x; k, p) = (x − 1
k − 1) pkqx−k    ,    x ≥ k

Distribución de Poisson
-Pruebas de ocurrencia en un Intervalo de Tiempo o en una Región.
Proceso de Poisson: resultados de un experimento aleatorio que se presentan en un intervalo de tiempo o en
una región.
λ: constante.

Propiedades:
1- Los resultados que se observan son independientes entre intervalos de tiempo o regiones (proceso sin
memoria).
2- La probabilidad de que ocurra un solo resultado en un Δt → 0 depende de Δt y no de los resultados que
ocurren en t2 < t1 − t0 < t3.
3- La probabilidad de que  ocurran 2 o más resultados (éxitos) en un intervalo corto o pequeña región se
aproxima a cero.
P(x, λt) = e−λt(λt)x
x!
Con:  x = 0,1,2,...

λ: n° promedio de resultados por unidad de tiempo o región.
t: longitud del intervalo (tiempo, área).

<!-- página 4 -->

E(x) = μ = λt
V(x) = σ2 = λt

Nota adicional: cuando n → ∞ y p → 0, la distribución Binomial tiende a la distribución de Poisson.

*Cuando n → ∞, vamos hacia el espacio o tiempo continuo (Poisson).

*Independencia de pruebas: propiedad que se cumple tanto para la distribución normal como la distribución de
Poisson.

*Si n → ∞   y  p → 0 para conservar el producto p. n = constante:
E(x) = p. n Binomial
  ↧
E(x) = λt Poisson

Además p → 0 corresponde a la propiedad 3° de Poisson.

b(x; n, p)  →  p(x, λt)
(n → ∞
p → 0 )

Ejemplo: el número de llamados que se presentan en una central telefónica es 10 por minuto.
Obtener la probabilidad que en el próximo minuto se observen menos de 3 llamadas.

p(0, λt)  =  e−10 100
0!  =  4,54 x 10−5
p(1, λt)  =  e−10 101
1!  =  4,54 x 10−4
p(2, λt)  =  e−10 102
2!  =  2,27 x 10−3
p(x < 3, λt)  =  2,77 x  10−3 ≃ 0,0028
