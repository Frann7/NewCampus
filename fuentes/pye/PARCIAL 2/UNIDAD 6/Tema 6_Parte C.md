# Tema 6_Parte C

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 6/Tema 6_Parte C.pdf` · 9 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Chi cuadrada: gamma con α=ν/2, β=2; f(x) con ν grados de libertad, E=ν, V=2ν; gráfico ν=1 a 5. |
| 2 | Usos de chi cuadrada en inferencia; definición de log-normal (Y=ln X normal). La fórmula de la densidad no está en el PDF. |
| 3 | Log-normal: Y=ln X; gráfico de densidades con μ=0 y μ=1 (σ=1); se usa la normal para calcular probabilidades. |
| 4 | Ej. 7: log-normal μ=3,2, σ=1, P(X>8): z=(ln 8−3,2)/1=−1,12. |
| 5 | Ej. 7: tabla A.3 con fila −1,1 resaltada; P(X<8)=0,1314, P(X>8)=0,8686. ⚠ ver el PDF: la tabla es imagen (el valor usado sí está en el texto). |
| 6 | Weibull: usos (fallas, viento), f(v) con k forma y c escala; histograma ajustado; Walpole: 1/c=α, k=β. |
| 7 | Weibull: momentos con Γ (E(v)=cΓ(1+1/k)), varianza, ecuación para k por iteraciones, energía eólica. |
| 8 | Ej. 8: viento de Paraná, v̄=3,04, s=1,81 → k=1,72947, c=3,41095, P(v>8)=0,0126775. |
| 9 | Captura de StatGraphics, Weibull k=1,72947, c=3,41095: cola inferior en 8 = 0,987322, cola superior = 0,0126775. |

<!-- página 1 -->

Distribución Chi cuadrada ~χ 2
La Distribución Chi cuadrada es otro caso especial de la Distribución Gamma
pero en este caso ∝= ν 2  y β = 2. Por tanto, partiendo de la ~Γ:
E x = ν
V x = 2ν
Tema 6 C
f x =
1
βαΓ α xα−1e
−x
β x > 0
0                 otro caso

∝= ν 2  y β = 2
f x =
1
2
ν
2  Γ ν
2
x
ν
2−1e−x
2           x > 0
0                              otro caso

Por lo tanto la Distribución tiene un solo
Parámetro ν:   GRADOS DE LIBERTAD
La Esperanza y Varianza son:

<!-- página 2 -->

Aplicaciones: La distribución chi cuadrada desempeña un papel fundamental en
la inferencia estadística. Tiene una aplicación considerable tanto en la
metodología como en la teoría. La distribución chi cuadrada es un componente
importante de la prueba estadística de hipótesis y de la estimación estadística.
Los temas en los que se trata con distribuciones de muestreo, análisis de
varianza y estadística no paramétrica implican el uso extenso de la distribución
chi cuadrada.
Distribución Log-Normal ~Ln − Normal
La Distribución logarítmica Normal ~Ln − Normal se aplica en casos donde una
transformación logarítmica natural tiene como resultado una distribución normal
(~N)
La variable aleatoria continua X tiene una distribución logarítmica normal si la
variable aleatoria Y = ln X tiene una distribución normal con media μ y
desviación estándar σ. La función de densidad de X que resulta es:

<!-- página 3 -->

Y = ln X
Es muy útil cuando se cumple la condición de normalidad del Ln de la variable
X ya que puede utilizarse la distribución normal para calcular probabilidades.

<!-- página 4 -->

Ejemplo 7: Se sabe que históricamente la concentración de contaminantes
producidos por plantas químicas exhiben un comportamiento que se parece a una
distribución logarítmica normal. Esto es importante cuando se consideran
cuestiones relacionadas con el cumplimiento de las regulaciones gubernamentales.
Suponga que la concentración de cierto contaminante, en partes por millón, tiene
una distribución logarítmica normal con los parámetros μ = 3.2 y σ = 1. ¿Cuál es la
probabilidad de que la concentración exceda 8 partes por millón?
Solución:
P X > 8 = 1 − P X < 8 . Como X posee una ~Ln − N entonces Y = Ln X  tiene ~N(μ, σ)
Estandarizamos la variable independiente Y para poder utilizar la normal estándar Z
Z = Y − μ
σ = Ln X − μ
σ = Ln 8 − 3.2
1 = −1.12
De Tabla 3:

<!-- página 5 -->

P X < 8 = 0.1314 P X > 8 = 1 − 0.1314 = 0. 8686

<!-- página 6 -->

Distribución Weibull ~W
La Distribución Weibull es muy utilizada en probabilidad de fallas de sistemas
eléctricos y además, es especialmente utilizada en cálculo de probabilidad de la
Velocidad del viento. Posee dos parámetros por lo que puede ajustarse a los datos
medidos por el anemómetro de una estación meteorológica. Al igual que la ~Γ el
parámetro k es el de forma y el parámetro c  es el de escala:
f v =
k
c
v
c
k−1
e− v
c
k
         v > 0
          0                        otro caso

El ajuste de la distribución Weibull al
régimen de vientos de un lugar es obtenido
calculando los parámetros “c” y “k” de
Weibull para un período de tiempo t.
Los parámetros “c” y “k” de Weibull para un período de tiempo t pueden
estimarse sobre la base del valor medio y la varianza.
Otros autores indican
1
c = α, k = β (Walpole)

<!-- página 7 -->

E v = v  = c. Γ 1 + 1
k
El valor medio es el Primer Momento de la variable independiente V. Éste es v
que coincide con la Esperanza.
El segundo momento es:  v2 = c2. Γ 1 +
2
k
El tercer momento es:  v3 = c3. Γ 1 +
3
k
que nos ayudará a calcular la V(v)
que es directamente proporcional a la
Energía eólica.
V v =  v − v  2
n = v − v  2 = v2 − 2vv  + v  2 = v2  − v  2
V v = c2. Γ 1 + 2
k − v  2 Γ 1 + 2
k = V v + v  2
c2 ; c2 = v  2
Γ 1 + 1
k
2
Γ 1 + 2
k = V v + v  2
v  2 . Γ 1 + 1
k
2
 V(v)
v  2 + 1 =
Γ 1 + 2
k
Γ 1 + 1
k
2
que se resuelve por iteraciones ya que sólo
depende del factor de forma k
Ed = 1
2 mv2 =  1
2 ρ. Vol. v2 = 1
2 ρ. A. v. t. v2 = 1
2 ρ. A. t. v3;   Ed = 1
2 ρ. A. t. v3

<!-- página 8 -->

V(v)
v 2 + 1 =
Γ 1 + 2
k
Γ 1 + 1
k
2 Cálculo de c y k de Weibull por iteraciones si se
conocen V v  y v   del viento en un lugar.
Calculo_wei
Resultados
Ejemplo 8: Calcule los parámetros “c” y “k” de Weibull
y realice la gráfica de la distribución de probabilidades
de viento para Paraná AERO (87374) sabiendo que
para un año normal la velocidad media del viento y su
desvío estándar son:
v  = 3.04 m/s
s = 1.81 m/s
Utilice el programa StatGraphics para calcular la probabilidad de que la
velocidad del viento exceda los 8 m/s (28.8 Km/hs) para un día cualquiera
elegido al azar del año en ese lugar.
k = 1.72947;    c = 3.41095;       P v > 8 = 0.0126775
Solución:

<!-- página 9 -->

Programa StatGrphics para análisis estadístico
Distribución Weibull de dos parámetros
