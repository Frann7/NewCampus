# Tema 7_Parte B

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 7/Tema 7_Parte B.pdf` · 15 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Repaso del TLC (z normalizada, n > 30, o n < 30 con población normal). |
| 2 | Distribución de la diferencia de medias muestrales: E, V y z con σ conocidas. |
| 3 | Distribución muestral de la varianza: χ² con ν = n−1 (Tabla A.5 del Walpole). |
| 4 | Tabla A.5 χ² (ν = 1 a 25, α de 0,995 a 0,50, α = área a la derecha) ⚠ ver el PDF: tabla de valores solo en imagen |
| 5 | t de Student cuando σ² es desconocida: T = (x̄ − μ)/(S/√n), ν = n−1; si n > 30, t ≈ N. |
| 6 | Relación entre t, Z y χ²: T = Z/√(V/ν); Tabla A.4 del Walpole (α a la derecha de t_α). |
| 7 | Tabla A.4 t de Student (ν = 1 a 17, α de 0,40 a 0,025) ⚠ ver el PDF: página sin texto, solo imagen de tabla |
| 8 | Ejemplo 1: P(−t₀,₀₂₅ < T < t₀,₀₅) = 0,925. |
| 9 | Distribución F de Snedecor para el cociente de varianzas: F = (U/ν₁)/(V/ν₂). |
| 10 | La F depende del orden de ν₁ y ν₂: f(6;10) ≠ f(10;6). |
| 11 | Tabla A.6 (continuación) F de Snedecor, f₀,₀₅(ν₁; ν₂) con ν₁ = 10 a ∞, ν₂ = 1 a 20 ⚠ ver el PDF: tabla de valores solo en imagen |
| 12 | f₁₋α(ν₁; ν₂) = 1/f_α(ν₂; ν₁); Ejemplo 2: f₀,₉₅(6;10) = 0,246. |
| 13 | Relación de F con varianzas muestrales: F = (S₁²/σ₁²)/(S₂²/σ₂²). |
| 14 | Ejemplo 3: cociente de varianzas de dos minas de carbón, F = 1,4423 (ν₁ = 4, ν₂ = 5). |
| 15 | Ejemplo 3, cierre: f₀,₀₅(4;5) = 5,19 > F, se aceptan varianzas iguales. |

<!-- página 1 -->

Teorema del Límite Central
Si x es una V.A. con cualquier distribución y x  es un estadístico de
la muestra de tamaño n, entonces:
La V. A. normalizada      z =
x−μx
σx
      →      ~N(0,1)  si  n → ∞
Además como μx = μ   y   σx = V(x) =
1
n V(x) =
σx
n
Entonces: z =
x−μx
σx
=
x−μ
σ
n

Por lo tanto si n → ∞  n > 30  entonces por más que la ~ V.A. x  ≠   ~N μ, σ :
z = x − μ
σ
n
      →        ~N(0,1)
Si n < 30  y  la ~ V.A. x tiene ~N μ, σ  entonces también:
Repaso

<!-- página 2 -->

Distribución de la diferencia de promedios muestrales
Sabiendo que: E x1 − x2 = μx1−x2 = μx1 − μx2 = μ1 − μ2
y que: V x1 − x2 = σx1−x2 =
2
σx1 + σx2 =
2 2 1
n1
σ1 + 1
n2
σ 2
2 2
Se puede construir la variable normalizada Z:
Z =
x1 − x2 − μx1−x2
σx1−x2
= x1 − x2 − μ1 − μ2
1
n1
σ1 + 1
n2
σ 2

2 2 ~N(0,1)
Se puede plantear que las medias poblacionales sean iguales  μ1 − μ2 = 0  o que las
mismas difieran en una cantidad Y : μ1 − μ2 = Y
En cualquier caso, se necesita conocer las varianzas de cada población.

<!-- página 3 -->

Distribución Muestral de la Varianza
Para la Varianza se utiliza la Distribución Chi cuadrada que es uno de los
casos especiales de la Distribución Gamma con ∝= ν 2  y β = 2.
Si   S2  la varianza de una muestra aleatoria de tamaño n  que se toma de una
población con ~N μ,σ  entonces:
S2 =  xi − x 2
n − 1   xi − x 2 = S2. n − 1
La V.A.  V =  xi − x 2
σ2 = n − 1 S2
σ2  posee una distribución Chi Cuadrada  χ2
con ν = n − 1  grados de libertad.
Tabla A.5 del Walpole

<!-- página 4 -->

ν = n − 1
α:   área a la
derecha del
valor
χ2

<!-- página 5 -->

Distribución de la diferencia de promedios σ2desconocido
Vimos que uno de los requisitos necesarios para estimar la media muestral
usando el Teorema del Límite Central es que la varianza poblacional sea
conocida.
En muchos casos este parámetro poblacional se desconoce por lo que  William
Sealy Gosset's en 1908 propuso la distribución conocida como t-Student en la
que no es necesario conocer la varianza de la población. Puede obtenerse este
dato a partir de la varianza de la muestra aunque la distribución tendrá mayor
dispersión respecto de la Normal debido a que la varianza de la muestra
presenta generalmente mayor incertidumbre.
En principio se supone que σ 2 =  S 2 pero en lugar de utilizar una ~N se utiliza la ~t
T = x − μ
S
n
      →        ~t(0, ν)
Donde ν representa los grado de libertad de la muestra:  ν = n − 1

<!-- página 6 -->

Aquí podemos afirmar que si n > 30 entonces la ~t ≅  ~N y puede usarse
independientemente cualquiera de ellas pero si n < 30  entonces la ~t  se
aparta de la ~N .
¿Pero qué relación existe entre la ~t y la ~N?
T = x − μ
S
n
= x − μ
σ
n
. σ
S = x − μ
σ
n
. 1
S σ = Z. 1
S2
σ2

V = n − 1 S2
σ2
Por lo tanto:  T = Z
V ν
 Donde Z es una variable con ~N 0,1  y V con ~ χ 2 de
ν grados de libertad
La Tabla A.4 del Walpole presenta los valores de α (probabilidad) a la derecha de tα

<!-- página 7 -->



<!-- página 8 -->

Ejemplo 1: Encuentre P −t0.025 < T <  t0.05 .
Solución: como t0.05 deja un área de 0.05 a la derecha y −t0.025 deja un área de
0.025 a la izquierda, entonces:
P −t0.025 < T <  t0.05 = 1 − 0.05 − 0.025 = 0.925.

<!-- página 9 -->

Distribución del cociente de varianzas
La comparación entre varianzas de dos poblaciones se realiza utilizando el cociente
de varianzas de manera tal que cuando ambas son iguales entonces el cociente es
igual a la unidad.
Esto es debido a que puede conocerse la distribución del cociente de varianzas
poblacionales a partir del cociente de las varianzas muestrales utilizando la
distribución f de Snedecor, también conocida como distribución de Fisher-
Snedecor.
F =
U ν1
V ν2

Sean U y V dos V.A. independientes donde ambas tienen ~χ2 con ν1 grados de
libertad para U y ν2 grados de libertad para V, entonces la V. A. F formada por el
cociente entre ambas variables aleatorias divididas por sus respectivos grados de
libertad tiene una distribución f de Fisher– Snedecor.
~ f de Snedecor

<!-- página 10 -->

La ~ f depende no sólo de los dos parámetros ν1 y ν2  sino también del orden en
que se establecen:
f ν1, ν2 = f 6, 10
f ν1, ν2 = f 10 , 6
f 6, 10  ≠ f 10, 6

<!-- página 11 -->

Se puede utilizar la Tabla A.6 de Walpole para encontrar las áreas  α a la derecha
del valor  fα(ν1, ν2)
Que está tabulada para valores de α = 0.05 y α = 0.01

<!-- página 12 -->

Sin embargo, se puede usar la tabla para calcular f0.95 y  f0.99 sabiendo que:
f1−α ν1, ν2 =  1
fα ν2, ν1

Ejemplo 2: Encuentre el valor de f0.95 6,10  que deja un 95% del área bajo la curva
a la derecha de ese valor.
f0.95 6, 10 = 0. 246
α = 95 %
f0.95 6,10 =  1
f0.05 10, 6 = 1
4.06 = 0.246

<!-- página 13 -->

F =
U ν1
V ν2
 ¿Pero cómo se relaciona esta variable con las varianzas  de
ambas muestras?
Si las muestras proviene de poblaciones con ~N con varianzas σ1 y σ2 entonces:
Porque la V.A. U tiene ~χ2 con ν1 = n1 − 1  grados de libertad U =  n1 − 1 . S1
σ1

2
2
V =  n2 − 1 . S2
σ2

2
2 Porque la V.A. V tiene ~χ2 con ν2 = n2 − 1  grados de libertad
De esta forma, el cociente de ambas V.A. resulta: F =
S1 σ1
S2 σ2

2
2
2
2

<!-- página 14 -->

Ejemplo 3: Considere las mediciones de la Capacidad Calorífica de producción de
Calor de Carbón de dos minas:
Mina 1 8260 8130 8350 8070 8340
Mina 2 7950 7890 7900 8140 7920 7840
¿Se puede concluir que las dos varianzas de la producción total de ambas minas
son iguales?
Solución: Se calculan las varianzas muestrales de cada una de las minas.
S1 = n1  xi
n1
1 −  xi
n1
1
2
n1 − 1 = 15750    ;
2
S2 = n2  xi
n2
1 −  xi
n2
1
2
n2 − 1 = 10920
2
La   V.A.  F =
S1 σ1
S2 σ2

2
2
2
2
;   pero supongo en principio que     σ1 = σ 2     por lo tanto:
F = S1
S2
= 15750
10920 = 1.4423
2 2
2
2
Si esta suposición es cierta la probabilidad que
F = 1.4423 debería ser elevada.
ν 1 = 4
ν 2 = 5

<!-- página 15 -->

Consideremos como valor límite de aceptación a todos los valores de F que estén
dentro del  95 % de probabilidad, por tanto rechazamos la suposición de varianzas
poblacionales iguales si  el valor de F cae fuera de este rango.
95%
5%
De la Tabla A.6 el valor límite para
fα ν1, ν2 =  f0.05 4,5 = 5.19
Como  F = 1.4423 está dentro del   95%
Entonces aceptamos que las varianzas
poblacionales de ambas producciones
de carbón son iguales:
1.4423  5.19
F
f0.05 4,5 > F
