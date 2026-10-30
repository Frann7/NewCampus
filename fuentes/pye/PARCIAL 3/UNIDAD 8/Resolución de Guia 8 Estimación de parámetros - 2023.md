# Resolución de Guia 8 Estimación de parámetros - 2023

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 3/UNIDAD 8/Resolución de Guia 8 Estimación de parámetros - 2023.pdf` · 10 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Resolución de la Guía de Estimación de Parámetros

Ejercicio 1 (estimación de la media)
X v.a.c.: Duración de los focos (hs)
n=30 (grande), x̅ = 780, σ = 40 (σ2 conocido), población aproximadamente normal, 1 − α = 0.96
Como la muestra es grande utilizaremos la Normal Estándar (Z).
Lo haremos “a mano” ya que los datos están resumidos (no contamos con el vector de observaciones).
x̅ ± zα
2
. σ
√n
# EJERCICIO 1
media=780
n=30
sd=40
alfa=0.04
media-qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n) #lim inf
media+qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n) #lim sup

Respuesta: 765.0015 < μ < 794.9985

Ejercicio 2 (estimación de la media)
X v.a.c.: Estatura de estudiantes de la carrera LSI (cm)
n=50 (grande), x̅ = 174.5, s = 6.9 (σ2 desconocido), 1 − α = 0.98
Como la muestra es grande utilizaremos la Normal Estándar (Z).
Lo haremos “a mano” ya que los datos están resumidos (no contamos con el vector de observaciones).
x̅ ± zα
2
. s
√n
# EJERCICIO 2
media=174.5
n=50
sd=6.9
alfa=0.02
media-qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n) #lim inf
media+qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n) #lim sup

Respuesta: a) 172.23 < μ < 176.77
b) El error máximo de estimación es E =
lim sup − lim inf
2 = 2.27
c)
# Repetir el IC al 90%
alfa=0.10
media-qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n) #lim inf
media+qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n) #lim sup
# Repetir el IC al 95%
alfa=0.05
media-qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n) #lim inf
media+qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n) #lim sup
# Repetir el IC al 99%
alfa=0.01
media-qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n) #lim inf

<!-- página 2 -->

media+qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n) #lim sup

IC al 90%: 172.89 < μ < 176.11 en el cual E =
lim sup − lim inf
2 = 1.61
IC al 95%: 172.59 < μ < 176.41 en el cual E =
lim sup − lim inf
2 = 1.91
IC al 99%: 171.99 < μ < 177.01 en el cual E =
lim sup − lim inf
2 = 2.51
d) Cuanto mayor es el nivel de confianza, mayor es el tamaño del error máximo de estimación.

Ejercicio 3 (estimación de la media)
X v.a.c.: Distancia recorrida por autos en la ciudad de Paraná en un año (km)
n=100 (grande), x̅ = 23500, s = 3900 (σ2 desconocido), 1 − α = 0.99
Como la muestra es grande utilizaremos la Normal Estándar (Z).
Lo haremos “a mano” ya que los datos están resumidos (no contamos con el vector de observaciones).
x̅ ± zα
2
. s
√n
# EJERCICIO 3
media=23500
n=100
sd=3900
alfa=0.01
media-qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n)
media+qnorm(alfa/2,lower.tail=FALSE)*sd/sqrt(n)

Respuesta: a) 22495.43 < μ < 24504.57
b) El error máximo de estimación es E =
lim sup − lim inf
2 = 1004.57

Ejercicio 4 (estimación de la media, cálculo de tamaño de muestra)
Se utilizó en ejercicio 1 la siguiente fórmula, siendo:
E = zα
2
. σ
√n →   n = (
zα
2
. σ
E )
2

Despejamos n para un E=10 y al 96% de confianza.
10 = z0.02. 40
√n →   10 = 2.05 . 40
√n →    n = [(2.05). 40
10 ]
2
→ n = 68
El valor de z se lo puede  obtener de R Studio con: qnorm(0.02, lower.tail=FALSE). O bien hacer el
cálculo completo de n con la sintaxis dispuesta debajo.
Siempre el resultado se redondea al entero siguiente.
#EJERCICIO 4
# tamaño de muestra para E=10
error=10
alfa=0.04
sd=40
(qnorm(alfa/2,lower.tail=FALSE)*sd/error)^2

Respuesta: n = 68

<!-- página 3 -->

Ejercicio 5 (estimación de la media, cálculo de tamaño de muestra)
X v.a.c.: Tiempo en perforar una placa metálica (segundos)
a)   1 −  α = 0.95, E = 12,     σ = 40,   n =?
Se parte de esta fórmula:
E = zα
2
. σ
√n  →   n = (
zα
2
. σ
E )
2

Despejamos n para un E=12 y al 95% de confianza.
12 = z0.025. 40
√n →   12 = 1.96  . 40
√n →    n = [(1.96). 40
12 ]
2
→ n = 43
El valor de z se lo puede obtener de R Studio con: qnorm(0.025, lower.tail=FALSE). O bien hacer el
cálculo completo de n con la sintaxis dispuesta debajo.
Siempre el resultado se redondea al entero siguiente.
#EJERCICIO 5
# tamaño de muestra para E=12
error=12
alfa=0.05
sd=40
(qnorm(alfa/2,lower.tail=FALSE)*sd/error)^2

Respuesta: n = 43

b) Se repite para el procedimiento para alcanzar
1
2 E = 6.
# tamaño de muestra para E=12/2=6
error=6
alfa=0.05
sd=40
(qnorm(alfa/2,lower.tail=FALSE)*sd/error)^2

Respuesta: n = 171

Ejercicio 6 (estimación de la media)
X v.a.c.: Contenido de azúcar en barras de cereal (gr)
n=20 (chico), x̅ = 11.3, s = 2.45 (σ2 desconocido), población normal, 1 − α = 0.95
Como la muestra es chica, la varianza poblacional desconocida y la población normal, utilizaremos la T
de Student.
Lo haremos “a mano” ya que los datos están resumidos (no contamos con el vector de observaciones).
x̅ ± tα
2,ν=n−1. s
√n
# EJERCICIO 6
n=20
media=11.3
sd=2.45
alfa=0.05
media-qt(alfa/2,df=n-1,lower.tail = FALSE)*sd/sqrt(n)
media+qt(alfa/2,df=n-1,lower.tail = FALSE)*sd/sqrt(n)
Respuesta: 10.15 < μ < 12.45

<!-- página 4 -->

Ejercicio 7 (estimación de la media)
X v.a.c.: Diámetros de piezas metálicas de forma cilíndrica (cm)
n=9 (chico), población normal, 1 − α = 0.99
Como la muestra es chica, la varianza poblacional desconocida y la población normal, utilizaremos la T
de Student.
Al contar con un vector de observaciones, se puede realizar directo con la función t.test(…)$conf.int

# EJERCICIO 7
diametros=c(1.01,0.97,1.03,1.04,0.99,0.98,0.99,1.01,1.03)
t.test(diametros,conf.level=0.99)$conf.int

Respuesta: 0.978 < μ < 1.033

Ejercicio 8 (estimación de la media)
X v.a.c.: Tiempos de secado de cierta pintura vinílica (hs)
n=15 (chico), población normal, 1 − α = 0.95
Como la muestra es chica, la varianza poblacional desconocida y la población normal, utilizaremos la T
de Student.
Al contar con un vector de observaciones, se puede realizar directo con la función t.test(…)$conf.int

# EJERCICIO 8
tiempos=c(3.4,2.5,4.8,2.9,3.6,2.8,3.3,5.6,
          4.4,4.0, 5.2,3.0,4.8,3.7,2.8)
t.test(tiempos,conf.level = 0.95)$conf.int

Respuesta: 3.25 < μ < 4.32

Ejercicio 9 (estimación de la media)
X v.a.d.: Número de caracteres tipeados por minuto por graduados de la carrera
n=12 (chico), x̅ = 79.3, s = 7.8 (σ2 desconocido), población normal, 1 − α = 0.95
Como la muestra es chica, la varianza poblacional desconocida y la población normal, utilizaremos la T
de Student.
Lo haremos “a mano” ya que los datos están resumidos (no contamos con el vector de observaciones).
x̅ ± tα
2,ν=n−1. s
√n
# EJERCICIO 9
79.3-qt(0.025,df=11,lower.tail=FALSE)*7.8/sqrt(12) #lim inf
79.3+qt(0.025,df=11,lower.tail=FALSE)*7.8/sqrt(12) #lim sup

Respuesta: 74.34 < μ < 84.26

Ejercicio 10 (estimación de la diferencia de medias)
Anulado de esta guía, sólo trabajamos con ejercicios de diferencia de medias cuando se cuenta con
vectores de observaciones.

Ejercicio 11 (estimación de la diferencia de medias)
Anulado de esta guía, sólo trabajamos con ejercicios de diferencia de medias cuando se cuenta con
vectores de observaciones.

<!-- página 5 -->

Ejercicio 12 (estimación de la diferencia de medias)
*Definimos las variables según el orden en el cual queremos la diferencia (NOGOPAINT-ALBA)*
X1 v.a.c.: Tiempo de secado de pintura Nogopaint (hs)
X2 v.a.c.: Tiempo de secado de pintura Alba (hs)
n1 = 15 (chico), n2 = 15 (chico),  σ1
2 y σ2
2   desconocidas e IGUALES, poblaciones normales
1 − α = 0.95
Como los tamaños muestrales son chicos, las varianzas poblacionales son desconocidas y las
poblaciones subyacentes son normales, utilizaremos la T de Student.
Al contar con dos vectores de observaciones, se puede realizar directo con la función t.test(…)$conf.int

# EJERCICIO 12
nogopaint=c(4.7, 3.9, 4.5, 5.5, 4.0, 5.3, 4.3,
            6.0, 5.2, 3.7, 5.5, 6.2, 5.1, 5.4, 4.8)
alba=c(3.5, 2.7, 3.9, 4.2, 3.6, 2.7, 3.3, 5.2,
       4.2, 2.9, 4.4, 5.2, 4.0, 4.1, 3.4)
t.test(nogopaint,alba, var.equal=TRUE, conf.level = 0.95)$conf.int

Respuesta: 0.55 < μ1 − μ2 < 1.69 Con un 95% de confianza podemos concluir que existe diferencia
significativa entre las medias (ya que 0 ∉IC) y es mayor el tiempo de secado de la p intura Nogopaint,
en promedio (porque los signos positivos en ambos extremos indican que la media de población 1 es
mayor que la 2). Por lo tanto, la marca de látex que brinda tiempo de secado más rápido es Alba.

Ejercicio 13 (estimación de la diferencia de medias)
X1 v.a.c.: Duración de películas disponibles en sitio web A (minutos)
X2 v.a.c.: Duración de películas disponibles en sitio web B (minutos)
n1 = 5 (chico), n2 = 7 (chico),  σ1
2 y σ2
2   desconocidas y DIFERENTES, poblaciones aprox. normales
1 − α = 0.90
Como los tamaños muestrales son chicos, las varianzas poblacionales son desconocidas y las
poblaciones subyacentes son aprox. normales, utilizaremos la T de Student.
Al contar con dos vectores de observaciones, se puede realizar directo con la función t.test(…)$conf.int

# EJERCICIO 13
a=c(103, 94, 110, 87, 98)
b=c(97, 82, 123, 92, 175, 88, 118)
t.test(a,b, var.equal=FALSE, conf.level = 0.90)$conf.int

Respuesta: −36.427 < μ1 − μ2 < 11.798 Con un 90% de confianza podemos concluir que no existe
diferencia significativa entre las medias (ya que 0 εIC) de los tiempos de duración de las películas en
sitios web A y B.

<!-- página 6 -->

Ejercicio 14 (estimación de la diferencia de medias)
X1 v.a.c.: Ganancia de peso del ganado porcino con DIETA TRADICIONAL (kg)
X2 v.a.c.: Ganancia de peso del ganado porcino con DIETA NUEVA (kg)
n1 = 12 (chico), n2 = 12 (chico),  σ1
2 y σ2
2   desconocidas, poblaciones normales
1 − α = 0.94
Como los tamaños muestrales son chicos, las varianzas poblacionales son desconocidas y las
poblaciones subyacentes son aprox. normales, utilizaremos la T de Student.
Al contar con dos vectores de observaciones, se puede realizar directo con la función t.test(…)$conf.int

PASO 1: ¿Las varianzas se asumen iguales o diferentes? Armamos el IC para cociente de varianzas.
# EJERCICIO 14
trad=c(16,24,18,19,22,12,15,16,11,14,25,31)
nueva=c(31,34,29,25,38,34,29,31,32,29,32,28)
mean(trad)
mean(nueva)
#IC para el cociente de variancias ¿es cierto que son iguales?
var.test(trad, nueva, conf.level = 0.94)$conf.int

El resultado es: 0.927 <
σ12
σ2
2 < 10.063 , como el 1  εIC  podemos concluir que las varianzas
poblacionales son IGUALES.

PASO 2: Realizamos el IC para diferencia de medias, asumiendo varianzas iguales.
# IC para diferencia de Medias
t.test(trad, nueva, var.equal=TRUE, conf.level = 0.94)$conf.int

Respuesta: −16.318 < μ1 − μ2 < −8.516 Con un 9 4% de confianza podemos concluir que existe
diferencia significativa entre las medias (ya que 0 ∉IC) y es mayor la ganancia de peso con la dieta
nueva, en promedio (porque los signos negativos en ambos extremos indican que la media de
población 2 es mayor que la 1). Por lo tanto, la dieta es efectiva para lograr ganancia de peso.

<!-- página 7 -->

Ejercicio 15 (estimación de la diferencia de medias)
X1 v.a.c.: Resistencia del alambre A (ohms)
X2 v.a.c.: Resistencia del alambre B (ohms)
n1 = 6 (chico), n2 = 6 (chico),  σ1
2 y σ2
2   desconocidas
1 − α = 0.95
Como los tamaños muestrales son chicos, las varianzas poblacionales son desconocidas y las
poblaciones subyacentes las asumimos normales, utilizaremos la T de Student.
Al contar con dos vectores de observaciones, se puede realizar directo con la función t.test(…)$conf.int

PASO 1: ¿Las varianzas se asumen iguales o diferentes? Armamos el IC para cociente de varianzas.
# EJERCICIO 15
a=c(0.140,0.138,0.143,0.142,0.144,0.137)
b=c(0.135,0.140,0.136,0.142,0.138,0.140)
#IC para el cociente de variancias ¿es cierto que son iguales?
var.test(a, b, conf.level = 0.95)$conf.int

El resultado es: 0.155 <
σ12
σ2
2 < 7.918 , como el 1 εIC  podemos concluir que las varianzas poblacionales
son IGUALES.

PASO 2: Realizamos el IC para diferencia de medias, asumiendo varianzas iguales.
# IC para diferencia de Medias
t.test(a,b, var.equal=TRUE, conf.level = 0.95)$conf.int

Respuesta: −0.0014 < μ1 − μ2 < 0.0057 Con un 90% de confianza podemos concluir que no existe
diferencia significativa entre las medias (ya que 0εIC) de las resistencias de los alambres A y B. Por lo
tanto, no puede afirmarse que A sea más resistente que B en promedio, a partir de lo obtenido.

<!-- página 8 -->

Ejercicio 16 (estimación de cociente de varianzas) – refiere al ejercicio 13
X1 v.a.c.: Duración de películas disponibles en sitio web A (minutos)
X2 v.a.c.: Duración de películas disponibles en sitio web B (minutos)
1 − α = 0.90
Al contar con vectores de observaciones, se puede realizar directo con la función var.test(…)$conf.int

# EJERCICIO 16
a=c(103, 94, 110, 87, 98)
b=c(97, 82, 123, 92, 175, 88, 118)
#IC para el cociente de variancias ¿es cierto que son DISTINTAS?
var.test(a, b, conf.level = 0.90)$conf.int

Respuesta: 0.016 <
σ12
σ2
2 < 0.454 Como el 1 ∉ IC  podemos concluir que las varianzas poblacionales son
DIFERENTES. Por lo tanto , estuvo bien suponerlas distintas en el IC para diferencia de medias del
ejercicio 13.

Ejercicio 17 (estimación de cociente de varianzas) – refiere al ejercicio 12
X1 v.a.c.: Tiempo de secado de pintura Nogopaint (hs)
X2 v.a.c.: Tiempo de secado de pintura Alba (hs)
1 − α = 0.95
Al contar con vectores de observaciones, se puede realizar directo con la función var.test(…)$conf.int

# EJERCICIO 17
nogopaint=c(4.7, 3.9, 4.5, 5.5, 4.0, 5.3, 4.3,
            6.0, 5.2, 3.7, 5.5, 6.2, 5.1, 5.4, 4.8)
alba=c(3.5, 2.7, 3.9, 4.2, 3.6, 2.7, 3.3, 5.2,
       4.2, 2.9, 4.4, 5.2, 4.0, 4.1, 3.4)
var.test(nogopaint, alba, conf.level = 0.95)$conf.int

Respuesta: 0.314 <
σ12
σ2
2 < 2.787 Como el 1 εIC  podemos concluir que las varianzas poblacionales son
IGUALES. Por lo tanto, estuvo bien suponerlas iguales en el IC para diferencia de medias del ejercicio
12.

Ejercicio 18 (estimación de una varianza)
Anulado de la guía para el cursado de este año.
Ejercicio 19 (estimación de una varianza)
Anulado de la guía para el cursado de este año.

<!-- página 9 -->

Ejercicio 20 (estimación de la proporción de éxitos)
X v.a.d.: Número de hombres africanos que padecen cierto trastorno sanguíneo
n=100, x = 24,     p̂ =
24
100   , 1 − α = 0.99
Lo hacemos directamente con la función prop.test(…)$conf.int de R Studio.

# EJERCICIO 20
prop.test(x=24, n=100, conf.level=0.99)$conf.int

Respuesta: 0.144 < p < 0.369. Con un 99% de confianza podemos afirmar que el real porcentaje de
hombres africanos que sufren este trastorno sanguíneo está entre 14.4 y 36.9% aproximadamente.

Ejercicio 21 (estimación de la proporción de éxitos)
X v.a.d.: Número de viviendas que utilizan petróleo como combustible para calefacción
n=1000, x = 228,     p̂ =
228
1000   , 1 − α = 0.99
Lo hacemos directamente con la función prop.test(…)$conf.int de R Studio.

# EJERCICIO 21
prop.test(x=228, n=1000, conf.level=0.99)$conf.int

Respuesta: 0.195 < p < 0.264 . Con un 99% de confianza podemos afirmar que el real porcentaje de
vivienda que u tilizan petróleo para calefaccionarse en dicha ciudad varía entre 19.5 y 26.4%
aproximadamente.

Ejercicio 22 (estimación de diferencia de proporciones)
X1 v.a.d.: Cantidad de hombres que padecen cierto trastorno sanguíneo
X2 v.a.d.: Cantidad de mujeres que padecen cierto trastorno sanguíneo
Hombres: n1 = 1000, x1 = 250,     p1̂ =
250
1000
Mujeres: n2 = 1000, x2 = 275,     p2̂ =
275
1000
1 − α = 0.95
Lo hacemos directamente con la función prop.test(…)$conf.int de R Studio.

# EJERCICIO 22
prop.test(x=c(250,275),n=c(1000,1000),conf.level=0.95)$conf.int

Respuesta: −0.065 < p1 − p2 < 0.015 . Con un 95% de confianza podemos afirmar que no existe
diferencia significativa entre las proporciones (ya que 0 εIC) de hombres y mujeres que pad ecen este
trastorno sanguíneo.

<!-- página 10 -->

Ejercicio 23 (estimación de diferencia de proporciones)
X1 v.a.d.: Cantidad de ingenieros eléctricos que son mujeres
X2 v.a.d.: Cantidad de ingenieros químicos que son mujeres
Ingeniería eléctrica: n1 = 250, x1 = 80,     p1̂ =
80
250
Ingeniería química: n2 = 175, x2 = 40,     p2̂ =
40
175
1 − α = 0.90
Lo hacemos directamente con la función prop.test(…)$conf.int de R Studio.

# EJERCICIO 23
prop.test(x=c(80,40),n=c(250,175),conf.level=0.90)$conf.int

Respuesta: 0.015 < p1 − p2 < 0.168. Con un 90% de confianza podemos afirmar que existe
diferencia significativa entre las proporciones (ya que 0 ∉IC) de mujeres en estas ingenierías, siendo
mayor en la Ingeniería Eléctrica (como ambos extremos son positivos, concluimos que p1 es mayor que
p2).

Ejercicio 24 (estimación de diferencia de proporciones)
X1 v.a.d.: Cantidad de estudiantes que ACTUALMENTE eligen al equipo A como su favorito
X2 v.a.d.: Cantidad de estudiantes que EN 2012 eligen al equipo A como su favorito
Encuesta 2022: n1 = 1000, x1 = 274,     p1̂ =
274
1000
Encuesta 2012:  n2 = 760, x2 = 240,     p2̂ =
240
760
1 − α = 0.95

# EJERCICIO 24
prop.test(x=c(274,240),n=c(1000,760),conf.level=0.95)$conf.int

Respuesta: −0.086 < p1 − p2 < 0.002 . Con un 95% de confianza podemos afirmar que no existe
diferencia significativa entre las proporciones (ya que 0εIC) de estudiantes que favorecen a este equipo
actualmente y en 2012. Por lo tanto, la proporción de adeptos a este equipo se mantiene constante.
