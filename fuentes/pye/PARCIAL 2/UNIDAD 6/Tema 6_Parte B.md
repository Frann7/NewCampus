# Tema 6_Parte B

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 6/Tema 6_Parte B.pdf` · 12 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Aprox. normal de la binomial: n≥30, p lejos de 0 y 1; b(x;n,p)→N(μ,σ), μ=np, σ²=npq. |
| 2 | Ej. 3: binomial n=15, p=3/7 (bolillas verdes) y su aprox. N(6,429; 1,917); tabla parcial. |
| 3 | Ej. 3: P(x≤6) exacta 0,5185 vs. normal con corrección 6,5 (z=0,04) → 0,5160. |
| 4 | Ej. 4: vacuna 60 % eficaz, n=100, P(x>70) por normal N(60;√24) con 69,5: z=1,94, 0,0262. |
| 5 | Gamma y exponencial: usos; función Γ(α) integrada por partes: Γ(α)=(α−1)Γ(α−1). |
| 6 | Γ(α)=(α−1)!; densidad gamma (α forma, β escala), μ=αβ, σ²=αβ²; gráficos variando scale y shape. |
| 7 | Exponencial: f(x)=(1/β)e^(−x/β), μ=β, σ²=β², λ=1/β, F(x)=1−e^(−λx); gráfico con λ=0,5; 1; 1,5. |
| 8 | Poisson y exponencial: tiempo hasta el primer evento, P(x=0; λt)=e^(−λt). |
| 9 | P(t>T)=e^(−λT), igual a Poisson con x=0; β=1/λ es el tiempo medio entre eventos. |
| 10 | Ej. 5: tiempo medio de falla 5 años, 5 sistemas, P(al menos 2 funcionan a 8 años)=0,2627. |
| 11 | Gamma como tiempo hasta α eventos de Poisson. Ej. 6: 5 solicitudes/min, α=2, planteo de P(t<1). |
| 12 | Ej. 6: integral por partes de t·e^(−5t); resultado P(t<1)=1−6e^(−5)=0,9596. |

<!-- página 1 -->

Aproximación Normal de la Binomial
Existe cierta vinculación entre las distribuciones teóricas discretas con las
continuas ya que en ciertos casos es posible utilizar una distribución continua
para una variable discreta. Esto es posible bajo ciertas condiciones que se
deben cumplir en el problema de uso de la variable discreta.
En el problema de V.A.D. el número de pruebas      n → ∞   , (n ≥ 30)
b x; n, p)  → N(μ, σ
p → 0  ó  p → 1
E x = n. p
V x = n. p. q
Tema 6 B
Estas condiciones son, en general, las siguientes:
Esto implica que la V.A.D puede tratarse con una distribución de V.A.C.
En el caso de la Distribución binomial en particular, otra aproximación que debe
cumplirse para que el problema pueda ser resuelto usando la distribución
Normal es que:
Si se cumplen estas dos condiciones entonces:
Esto implica que la distribución binomial no es asimétrica:
Como en una
distribución Binomial:
Entonces, en la
distribución Normal:
E x = μ = n. p
V x = σ2 = n. p. q

<!-- página 2 -->

Ejemplo 3: Sea una V.A.D. con distribución binomial con x: número de bolillas verdes.
Con
reposición
b x; n, p) = b(x; 15, 0.429
Aún si la primera premisa n → ∞ no se cumple, la aproximación es bastante
buena cuando p → 0.5
p = 3
7 = 0.429 → 0.5 Se extraen 15 bolillas: n = 15 < 30
x f(x)
0 2.24x10-4
1 2.52x10-3
2 1.33x10-2
3 4.32x10-2
4 9.73x10-2
5 1.61x10-1
6 2.01x10-1
… …
15 3.07x10-6
N μ, σ = N(n. p, n. p. q )
N(6.429,1.917)
Encentre la probabilidad de sacar al menos 6 bolillas verdes en 15 intentos:

<!-- página 3 -->

Encentre la probabilidad de sacar al menos 6 bolillas verdes en 15 intentos:
a) b x; n, p) = b(x ≤ 6; 15, 0.429
x f(x)
0 2.24x10-4
1 2.52x10-3
2 1.33x10-2
3 4.32x10-2
4 9.73x10-2
5 1.61x10-1
6 2.01x10-1
… …
15 3.07x10-6
P x ≤ 6 = P x = 0 + P x = 1 + ⋯ + P x = 6 = 0. 5185
b) N(π, σ)
6.5
P x < 6.5 = P(Z < Z1) Z1 = x − n. p
n. p. q
Z1 = 6.5 − 6.429
1.917 = 0.037
De tabla 3:
P Z < 0.04 = 0. 5160
Con muchos menos cálculos se llega a resultados muy similares
Es muy útil en los caso en que se pide                        ó   P x < X  P x > X
En los casos donde sólo debe usar una sola vez la  b x; n, p), b(x = 6; 15, 0.429
no se justifica usar esta aproximación ya que para ello hay que hacer P 5.5 < x < 6.5

<!-- página 4 -->

Ejemplo 4: Una dosis de la vacuna SINOFARM contra el virus SAR COVID-19 es
eficiente en el 60 % de los casos. ¿Cuál es la probabilidad de que sea efectiva en por
lo menos 70 casos de una muestra de 100 pacientes?
Es un caso de distribución binomial:  Solución:  b x; n, p) = b(x > 70; 100, 0.6
n → ∞, n = 100 (n ≥ 30)
p → 0.5, p = 0.6
Se puede usar la Distribución Normal
N μ, σ = N n. p, n. p. q = N 60, 24
P x > 69.5 = 1 − P(Z < Z1)
De tabla 3:
Z1 = 69.5 − 60
24
= 1.94
P Z < 1.94 = 0.9738
P x > 69.5 = 1 − 0.9738 = 0. 0262
La probabilidad de que sea efectiva en más de 70 casos de una muestra de 100
pacientes es de 2.62 %

<!-- página 5 -->

Distribución Gamma (~Γ) y Exponencial (~exp )
La Distribución Exponencial es un caso particular de la distribución Gamma.
Ambas se utilizan en la Teoría de Extremos (valores máximos de variables) y
en la teoría de confiabilidad. También en el cálculo de probabilidad de
tiempos de falla de componentes y sistemas eléctricos.
Antes de definir las Distribuciones Gamma y Exponencial vamos a definir la
FUNCION GAMMA (Γ):
Γ α =  xα−1
∞
0
e−xdx ∝ ∈ Z+ Que posee una propiedad muy interesante:
Al integrar por partes: u = x∝−1
dv = e−xdx du = ∝ −1 x∝−2dx
v = −e−x
Γ α =  u. dv
∞
0
= u. v −  v. du = −e−x. xα−1
∞
0
+ α − 1  xα−2e−xdx
∞
0

0
∞
Γ α = ∝ −1  xα−2
∞
0
e−xdx = ∝ −1 . Γ α − 1  Si repetimos hasta llegar a α = 1

<!-- página 6 -->

Γ α = ∝ −1 . α − 2 . α − 3 … Γ 1
Como: Γ 1 =  x0e−xdx =  e−xdx = −e−x = − 0 − 1 = 1
∞
0
∞
0

0
∞
Entonces: Γ α = ∝ −1 . α − 2 . α − 3 … .1 Γ α = ∝ −1 !
Distribución Gamma
f x =
1
βαΓ α xα−1e
−x
β x > 0
0                 otro caso

α: Factor de Forma sℎape
β: Factor de Escala (scale)
μ = α. β Valor medio:
Varianza: σ 2 = α. β2

<!-- página 7 -->

Distribución Exponencial
f x =
1
β e
−x
β x > 0
0         otro caso

β: Factor de Escala (scale)
μ = β Valor medio:
Varianza: σ 2 = β2
Es un caso particular de la ~Γ  ya que α = 1
Si elegimos λ =
1
β; f x =   λe−λx x > 0
0 otro caso
¿Existe una relación con la ~ Poisson?
La Función acumulada de la ~exp:
F x =  λe−λtdt = −λ e
λ
−λt
= − e−λx − 1 = 1 − e−λx
x
0

0
x

<!-- página 8 -->

Distribución Poisson
Pruebas de ocurrencia en un Intervalo de Tiempo o en una Región.
Proceso de Poisson: resultados de un experimento aleatorio que se presentan
en un intervalo de tiempo o en una región.
Si deseo conocer la probabilidad de tiempo que debe transcurrir hasta que
ocurra el primer evento
Cambio V.A.D (número de eventos en un intervalo de tiempo) a una V.A.C. (transcurso
de tiempo hasta que ocurra el primer evento).
Si el evento es el primero entonces quiere decir que durante el transcurso del tiempo no
ocurre ningún evento,  X = 0  en la ~Poisson.
0 1er
evento
x
t (tiempo)
P x = 0, λt = e−λt(λt)0
0! = e−λt
A medida que pasa el tiempo la probabilidad de que
no ocurra ningún evento decae exponencialmente

<!-- página 9 -->

De la ~ exp  vimos que la
 F x = 1 − e−λx
Si cambiamos t por x:
P t > T = 1 − F T = 1 − 1 − e−λT = e−λT
T
Que, como vimos, es la ~Poisson con x = 0
Por tanto, la probabilidad de que se exceda un tiempo T  hasta que ocurra el primer
evento P t > T   en un modelo con ~Poisson está dado por la ~exp
Como en la ~Poisson, λ es el numero de eventos promedio en la unidad de tiempo (1/s)
entonces β =
1
λ  (s) es el tiempo medio entre eventos.

<!-- página 10 -->

Ejemplo 5: Sea un sistema caracterizado por un tiempo medio de falla de 5 años.
Se instalan 5 de estos sistemas. ¿Cuál es la probabilidad de que al cabo de 8 años
sigan funcionando al menos dos de ellos?
Solución:  Sea x el número de sistemas que funcionan al cabo de 8 años.
¿Qué tipo de variable es? ¿qué modelo utilizamos?
Es una V.A.D. donde x es el número de sistemas que funcionan al cabo de 8 años.
El modelo es apropiado para una ~ b x ≥ 2; n, p .
n = 5. (número de sistemas que se instalaron).
p es la probabilidad que no falle un sistema.
Ésta está dada por el tiempo medio de falla β = 5 años. Que se exceda de ese tiempo
significa que seguirá funcionando. Por tanto podemos usar la ~exp
P t > T = e−λT con T = 8 años  y  λ =
1
5  (1/s) P t > 8 = e− 8
5 = 0.2
Que es la probabilidad de que un sistema siga funcionando al cabo de 8 años.
b x ≥ 2; n, p = 1 − b x < 2; n, p = 1 −  5
x 0.2x0.85−x = 0. 26272
1
0

<!-- página 11 -->

Corolario de la relación entre la ~exp y la ~Poisson
Como la ~exp es un caso especial de la ~Γ con α = 1 entonces α es el número de
eventos en la ~Poisson, es decir, α es el primer evento de ~Poisson.
Por tanto, en lugar de considerar el tiempo transcurrido hasta el primer evento, podemos
preguntarnos por el tiempo transcurrido hasta que ocurran 2, 3 o α eventos usando la ~Γ.
Ejemplo 6: Las solicitudes que llegan a una central de atención al usuario son de 5
por minuto en promedio. ¿Cuál es la probabilidad de que antes de transcurrido un
minuto hallan llegado dos solicitudes?
Solución:
λ = 5 (1/min) β =
1
λ = 0.2 min en promedio entre solicitudes
α = 2 solicitudes
P t < 1 =  1
βαΓ α tα−1e
−t
β
1
0
dt =  1
0.22Γ 2 t2−1e− t
0.2dt
1
0
= 25  t. e−5t dt
1
0

Se resuelve por partes

<!-- página 12 -->

 t. e−5tdt
1
0
 Al integrar por partes: u = t
dv = e−5tdt
du = dt
v = − 1
5 e−5t
 t. e−5tdt
1
0
= − t
5 . e−5t −  − 1
5 e−5tdt
1
0
= − 1
5 e−5 + 1
5  e−5tdt
1
0
=
0
1
= − 1
5 e−5 + 1
5 − 1
5 e−5t = − 1
5 e−5 − 1
25 e−5 − 1 = 1
25 −5e−5 − e−5 + 1 =
0
1
= 1
25 1 − 6e−5
P t < 1 = 25. 1
25 1 − 6e−5 = 1 − 6e−5 = 0. 9596
