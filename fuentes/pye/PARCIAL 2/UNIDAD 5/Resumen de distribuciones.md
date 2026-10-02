# Resumen de distribuciones

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 5/Resumen de distribuciones.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Discretas (Bernoulli, binomial, geométrica, bin. negativa, hipergeométrica, Poisson), normal y gamma: f, E y V. ⚠ ver el PDF: combinatorios, fracciones y exponentes rotos |
| 2 | Gráficos de gamma y beta; exponencial, beta, uniforme, t, chi cuadrado, F: f, E y V. ⚠ ver el PDF: densidades con fracciones y exponentes rotos; gráficos |

<!-- página 1 -->

Probabilidad y Estadística – Licenciatura en Sistemas de Información  1
                PPrroobbaabbiilliiddaadd  yy  EEssttaaddííssttiiccaa
Funciones de probabilidad puntual o de densidad, esperanzas y varianzas de las variables aleatorias más
frecuentes.
DDiissttrriibbuucciioonneess  ddiissccrreettaass
Distribución
Binomial
Bi(n, p)
f(x) = ቀn
xቁ p௫(1 − p)௡ି௫
x = 0, 1, … , n;  0 < p < 1
E(X) = np Var(X) = np(1 − p)
Un caso particular de la distribución binomial es cuando n = 1. Esta distribución
suele denominarse Bernoulli de parámetro p, Be(p) = Bi(1, p).
Distribución
Geométrica
Ge(p)
f(x) = p(1 − p)௫ିଵ
x = 1,2, …  y 0 < p < 1 E(X) = 1
p Var(X) = 1 − p
pଶ
Distribución
Binomial Negativa
Bi∗(k, p)
f(x) = ቆx − 1
k − 1ቇ p௞(1 − p)௫ି௞
x = k, k + 1, k + 2, …  y 0 < p < 1
E(X) = k
p Var(X) = k(1 − p)
pଶ
La distribución geométrica es un caso particular de la distribución binomial
negativa en la cual k = 1, Bi∗(1, p) = Ge(p).
Distribución
Hipergeométrica
H(N, k, n)
f(x) =
൫k
x൯൫N−k
n−x൯
൫N
n൯

x ∈ ℤ; máx{k + n − N, 0} ≤ x ≤ mín{k, n}
E(X) = nk
N  Var(X) = nk(N − k)(N − n)
Nଶ(N − 1)
N: total poblacional; k: cantidad de “éxitos” en la población; n: tamaño muestral.
Distribución Poisson
P(λt)
f(x) = eିఒ௧(λt)௫
x!
x = 0,1, 2, … ;  λt > 0

E(X) = λt Var(X) = λt
DDiissttrriibbuucciioonneess  ccoonnttiinnuuaass
Distribución Normal
N(μ; σ)
f(x) = 1
σ√2π
eି (ೣషಔ)మ
మಚమ
con σ > 0
E(X) = μ Var(X) = σଶ
La distribución normal estándar
corresponde a la elección de parámetros μ =
0 y σ = 1: N(0, 1).

Distribución Gamma
Γ(α, β)
f(x) = βఈ
Γ(α) x஑ିଵeିఉ௫I(଴;ାஶ)(x)
con α > 0, β > 0
E(X) = α
β Var(X) = α
βଶ
El símbolo Γ(α) representa la función gamma definida por Γ(α) =
  ∫ xఈିଵeି௫dxஶ
଴ , siendo α > 0 y satisface las siguientes propiedades: i) Γ(1) =
1; ii) Γ(α) = (α − 1)Γ(α − 1), iii) Γ(n) = (n − 1)! con n = 1, 2, 3, …; iv) Γ ቀ
ଵ
ଶቁ =
√π.

<!-- página 2 -->

Probabilidad y Estadística – Licenciatura en Sistemas de Información  2
En el gráfico de la derecha figuran las
funciones de densidad gamma para distintos
valores de los parámetros: la curva de la
línea fina corresponde a α = 3, β = 3 ,  la
de la línea de grosor medio corresponde a
α = 2, β =
ଵ
ଶ , y la de la línea más gruesa
corresponde a α = 5, β = 1. Con líneas
punteadas están marcadas las esperanzas en
cada caso.

Distribución
Exponencial
Exp(λ)
f(x) = λeି ఒ௫   si x ≥ 0
con λ > 0 E(X) = 1
λ Var(X) = 1
λଶ
La distribución exponencial es un caso
particular de la distribución gamma en la
cual α = 1,  Exp(λ) = Γ(α, β).

Distribución Beta
β(a, b)
f(x) = Γ(a + b)
Γ(a)Γ(b) x௔ିଵ(1 − x)௕ିଵI(଴;ଵ)(x)
con a > 0, b > 0
E(X) = a
a + b Var(X) = a + b
(a + b)ଶ(a + b + 1)
En el gráfico de la derecha figuran las
curvas de densidades Beta para distintos
valores de los parámetros: la curva de la
línea fina corresponde a a = 3, b = 6; la de
la línea de grosor medio corresponde a a =
2, b = 2 y la de la línea gruesa corresponde
a a = 10, b = 3. Con líneas punteadas están
las esperanzas en cada caso.

Distribución
Uniforme
U[a, b]
f(x) = 1
b − a     con a ≤ x ≤ b

E(X) = a + b
2  Var(X) = (b − a)ଶ
12
La distribución uniforme en el intervalo (0,1) es un caso particular de la
distribución Beta: U(0,1) = β(1,1)
Distribución T de
Student con n grados
de libertad t௡
f(x) =
Γ ቀ
௡ାଵ
ଶ ቁ
Γ ቀ
௡
ଶቁ √πn
ቆ1 + xଶ
n ቇ
ି೙శభ
మ

E(X) = 0
n ≥ 2  Var(X) =
௡
௡ିଶ ;     n > 2
Distribución Chi
cuadrado con n
grados de libertad
χ௡ଶ = χଶ(n)
La distribución Chi cuadrado
con n grados de libertad es un
caso particular de la distribución
gamma: χ௡ଶ = Γ ቀ
௡
ଶ ; ଵ
ଶቁ, siendo
n ∈ ℕ.
E(X) = n
 Var(X) = 2n
Distribución F de
Snedecor con n y m
grados de libertad
F௡,௠

f(x) =
Γ ቀ
௠ା௡
ଶ ቁ
Γ ቀ
௠
ଶ ቁ Γ ቀ
௡
ଶቁ
ቀ n
mቁ
೙
మ
xቀ೙
మିଵቁ ቀ1 + n
m xቁ
ି೙శ೘
మ
I଴;ஶ(x)

Densidad Gamma
Densidad Beta
