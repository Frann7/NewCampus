# Tema 8_Parte A

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 3/UNIDAD 8/Tema 8_Parte A.pdf` · 16 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Se profundizarán los conceptos dados en el tema anterior acerca
de la inferencia estadística de los parámetros poblacionales a
partir de muestras.
w – Cap 9
● Métodos clásicos de estimación: Puntual y por intervalos de clase.
● Error de estimación puntual y cálculo del tamaño de la muestra según el error que se fije.
● Límites de tolerancia.
● Inferencia de la media y de la diferencia de medias.
● Estimación de una proporción y de la diferencia de dos proporciones.
● Estimación de la varianza y del cociente de varianzas por intervalos de clase.

<!-- página 2 -->

Estimación de μ usando x y la ~N 0,1  cuando σ es conocido:
Repaso
z = x − μ
σ
n
  Cuando x tiene ~N(μ, σ) aunque n < 30
               x no tiene ~N μ, σ  pero n ≥ 30
Estimación de μ usando x y la ~t 0, ν  cuando σ es desconocido:
T = x − μ
S
n
  Cunado x tiene ~N(μ, σ) aunque n < 30
              x no tiene ~N μ, σ  pero n ≥ 30
Estimación de σ2 usando S2 y la ~χ2 ν, α :
V = ν. S2
σ2  Cuando x tiene ~N(μ, σ)

<!-- página 3 -->

F =
S1 σ1
S2 σ2

Estimación de μ1 − μ2 usando x1 − x2 y la ~N 0,1  cuando σ1 y σ2 son conocidos:
Z = x1 − x2 − μ1 − μ2
1
n1
σ1 + 1
n2
σ 2
 Cuando x tiene ~N(μ, σ) aunque n < 30
              x no tiene ~N μ, σ  pero n ≥ 30
Estimación de μ1 − μ2 usando x1 − x2 y la ~t 0, ν  cuando σ1 y σ2 son desconocidos:
T = x1 − x2 − μ1 − μ2
1
n1
S1 + 1
n2
S2

2 2
2 2
Cuando x tiene ~N(μ, σ) aunque n < 30
               x no tiene ~N μ, σ  pero n ≥ 30
2
2
2
2
Estimación de σ1 σ2   usando y la ~f ν1, ν2 :
2
2
Cuando x tiene ~N(μ, σ)
Repaso

<!-- página 4 -->

Métodos Clásicos de Estimación
a) Estimación Puntual
b) Estimación por Intervalos de Confianza
a) Estimación Puntual
Estima los parámetros poblacionales a partir de un estadístico de la muestra
Por ejemplo:  • Estimo μ a partir de x.
• Estimo μ a partir de x .
• Estimo σ2 a partir de S2.
• Estimo σ2 a partir de Q3 − Q1.
Se basan en los datos de una muestra seleccionada aleatoriamente.
No se espera que un estimador θ  x, x , S2, RIC  logre estimar el parámetro
de la población θ sin error, lo que en realidad se espera es que no este muy
alejado. Por ejemplo, no se espera que x estime μ con exactitud.
Llamemos θ  al estadístico de la muestra y θ al parámetro poblacional a estimar.

<!-- página 5 -->

Estimador insesgado:  Es aquel que cumple la condición:
xa xb xc xj
μ x =  x
n = E x = μ
S2 es un estimador insesgado de σ2 pero S suele ser un estimador sesgado
de σ, un sesgo que en el caso de muestras grandes se vuelve insignificante.
Por esto es que para el cálculo de σ se debe dividir la expresión
 xi − x 2  por (n − 1) en vez de n, el último valor de xi queda fijado por
la x y no puede tomar cualquier valor.
μθ = E θ = θ
μS = E S ≠  σ

<!-- página 6 -->

Varianza de un Estimador puntual:
Si θ 1 y θ 2 son dos estimadores insesgados del parámetro poblacional θ
elegimos el estimador cuya distribución muestral tenga menor varianza.
σθ 1 < σθ 2 θ 1 es un estimador más eficiente de θ  que θ 2
xa xb xc xj xb  xa  xc
σx < σx
2 2
2 2
Entonces, x es mejor estimador de μ que x

<!-- página 7 -->

b) Estimación por intervalos de confianza
Como sabemos que con el estimador no pretendemos obtener el valor
exacto del parámetro poblacional al estimar, este método propone fijar un
nivel o grado de confianza 1 − α , donde α es el grado de significancia.
De esta forma, a la estimación del parámetro poblacional θ la podemos
plantear como una probabilidad de que se encuentre entre ciertos límites
θ 1 y θ 2 con una confianza del 1 − α .
P θ 1 < θ < θ 2 = 1 − α Planteado como probabilidad con:
IC = θ 1 < θ < θ 2  Intervalo de confianza y:
LC = θ 1, θ 2  Límites de confianza

<!-- página 8 -->

Ejemplo 1: Estimar μ a partir del estimador x por IC con (1 − α) nivel de confianza
donde σ es conocido.
Z = x − μ
σ
n

P −Zα 2 < Z <  Zα 2 = 1 − α
Solución: Como σ es conocido se puede plantear el Teorema del Límite Central
Que planteado como probabilidad entre dos valores de la
variable estandarizada  Z con α nivel de significancia resulta:
Z
Z está en esta zona con una
confianza (1 − α)

<!-- página 9 -->

P −Zα 2 < Z <  Zα 2 = 1 − α
Multiplicando m.a.m. por σ
n   y sumando x
P x − Zα 2
σ
n < x + Z σ
n <   x + Zα 2
σ
n = 1 − α
μ
Z = x − μ
σ
n

P x − Zα 2
σ
n < μ <   x + Zα 2
σ
n = 1 − α
IC = x − Zα 2
σ
n < μ <   x + Zα 2
σ
n
LC = x − Zα 2
σ
n ;  x + Zα 2
σ
n
Intervalo de confianza
Límites de confianza

<!-- página 10 -->

x − Zα 2
σ
n   x + Zα 2
σ
n
μ
μ está en esta zona con una
confianza (1 − α)
En el caso de que σ sea desconocido y n < 30 reemplazo Z por T y utilizo la ~t
IC = x − tα 2
S
n < μ <   x + tα 2
S
n
x

<!-- página 11 -->

Error de estimación puntual
x − Zα 2
σ
n   x + Zα 2
σ
n μ x
error exacto
error de
estimación puntual
Por lo tanto, el nivel de confianza
1 − α  proporciona una
presición de nuestra estimación
puntual.
Si 1 − α = 0,95 entonces tengo una confianza de 95% que el error de estimación de μ no
excede de Z0,025
σ
n.
Si 1 − α = 0,99 entonces tengo una confianza de 99% que el error de estimación de μ no
excede de ±Z0,005
σ
n.
El error de
estimación puntual
es entonces:
e = Zα 2
σ
n

<!-- página 12 -->

¿Cuál de los dos casos es más exigente, el 95% o el 99%?
x − Zα 2
σ
n   x + Zα 2
σ
n x
El caso de α más pequeño es el menos exigente porque las zonas de rechazo son
más pequeñas.
Entonces, el 95% de confianza es más exigente que el 99% de confianza.

<!-- página 13 -->

Cálculo del tamaño de la muestra con un error fijado
Ahora, con una idea de los errores de estimación que se comenten según el nivel
de confianza podemos preguntarnos ¿qué tan grande debe ser la muestra para
cometer un error menor que un valor fijado (por ejemplo por alguna
reglamentación)?
Podemos calcular el tamaño de la muestra n de antemano para asegurar que
nuestro error de estimación puntual no excederá de un valor e establecido.
e = Zα 2
σ
n
Despejamos n
n =
Zα 2 . σ
e
2

Error estándar de estimación puntual
s. e. (standard error) es el desvío estándar del error de
estimación puntual. En el caso de estimar μ con
x y σ es conocido, el Zα 2  está fijado por α, entonces el error
varía con
σ
n , por lo tanto:
s. e. = σ
n

<!-- página 14 -->

Límites de tolerancia
Ahora en lugar de preocuparnos en estimar μ, queremos determinar límites de
tolerancia para aceptar o rechazar elementos, por ejemplo, en un proceso de
control de calidad.
Se plantea que con una confianza de 1 − γ %  se acepten 1 − α % de los
elementos realizando mediciones de los mismos en un sistema de control.
Para el caso que se conozcan μ y σ puedo
proponerme un 100% de confianza de
aceptar el 95% de las piezas fabricas
μ −1,96. σ 1,96. σ
95%
Esto es porque sé exactamente cuál es el valor de μ y de
σ de ls piezas que se están fabricando

<!-- página 15 -->

En el caso de que no sé exactamente o no estoy seguro de los parámetros μ y σ voy
a tener que calcular los límites de tolerancia con un nivel de confianza (1 − γ).
x − Zα 2
σ
n   x + Zα 2
σ
n μ x
95%
x − K. S x + K. S
En este ejemplo tengo un 1 − γ % = 95% de confianza que μ se encuentre en el
intervalo x ± Zα 2
σ
n . Necesito tomar una muestra de n elementos para calcular S y
estimar K.
Si, por ejemplo, deseo aceptar el 99% de las piezas, el valor de K me asegura de
aceptar el 1 − α % = 99% de las piezas con un 1 − γ % = 95% de confianza.

<!-- página 16 -->

La Tabla A.7 permite obtener los valores de K para el cálculo de los límites de
tolerancia:  L. T. = x ± K. S
