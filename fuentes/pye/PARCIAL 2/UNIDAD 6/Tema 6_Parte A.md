# Tema 6_Parte A

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 6/Tema 6_Parte A.pdf` · 18 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Temario: uniforme, normal, gamma y exponencial, chi cuadrada, Weibull. |
| 2 | Uniforme continua: f(x)=C en (a,b), C=1/(b−a) porque el área vale 1; gráfico del rectángulo. |
| 3 | Ej. 1: uniforme, reunión de 0 a 3 hs, f=1/3, P(1<x<2)=1/3. |
| 4 | Uniforme: E(x)=(a+b)/2 y planteo de E(x²)=(1/3)(b³−a³)/(b−a). |
| 5 | Uniforme: división da b²+ba+a², E(x²)=(b²+ba+a²)/3, V(x)=(b−a)²/12. |
| 6 | Normal: descripción, f(x)=1/(√(2π)σ)·e^(−½((x−μ)/σ)²); gráfico con μ±σ = 68 %. |
| 7 | Propiedades 1 y 2: moda en x=μ y simetría; 0,5 de área a cada lado de μ. |
| 8 | Propiedad 3: puntos de inflexión en μ±σ; gráfico: 68 % en ±σ, 95 % en ±1,96σ, 99 % en ±2,576σ. |
| 9 | Propiedad 4: f(x)→0 cuando x→±∞ (colas). |
| 10 | Propiedad 5: cóncava abajo en μ±σ, arriba afuera; propiedad 6: integral de f = 1. |
| 11 | Rol de los parámetros: μ distintas con igual σ (se desplaza), σ distintas con igual μ (más ancha o angosta). |
| 12 | Rol de los parámetros: μ y σ distintas a la vez (μ1<μ2, σ1<σ2). |
| 13 | Problema: alturas μ=170, σ=12, P(165<x<190) = integral sin primitiva; da 0,6137 (61,37 %). |
| 14 | Estandarización Z=(x−μ)/σ, cambio de variable x=μ+σz, P(x1<x<x2)=P(z1<z<z2). |
| 15 | Normal estándar μ=0, σ=1; gráfico de la normal original y la transformada con z1, z2. |
| 16 | F(z) acumulada: P(x1<x<x2)=P(z<z2)−P(z<z1), con tabla. ⚠ ver el PDF: tabla (primeras filas) y gráfico sin texto |
| 17 | Tabla A.3 de áreas F(z), z de −3,4 a 3,4. ⚠ ver el PDF: tabla sin texto extraído |
| 18 | Ej. 2: normal μ=50, σ=10, P(45<X<62): z=−0,5 y 1,2, resultado 0,5764 por tabla. |

<!-- página 1 -->

Veremos en este tema los modelos teóricos de las Distribuciones
de densidad de probabilidad de Variable Aleatoria Continua - VAC.
w – Cap 6
● Distribución Uniforme
● Distribución Normal
● Distribución Gamma y Exponencial.
● Distribución Chi Cuadrada
● Distribución Weibull

<!-- página 2 -->

• Distribución uniforme
     Al igual que en una VAD, la Distribución Uniforme de una VAC se puede utilizar
cuando la f(x) es plana, es decir, la probabilidad es uniforme en un intervalo de la
VAC.
f(x, k)  =  C, a < x < b
0, otro caso
¿Cuánto debe valer la constante C
para que f(x) sea una f.d.p.?
 f x dx = 1 →  C. dx = 1
b
a
+∞
−∞

C. x
b
= 1 → C. b − a = 1 →  C = 1
b − a a

<!-- página 3 -->

Ejemplo 1.
Un salón de reuniones está disponible 3 horas por día. Las reuniones tiene diferente
duración dentro de ese lapso de tiempo.  ¿Cuál es la probabilidad que una reunión dure
entre 1 hora y 2 horas?
Solución:
Como no hay ninguna mención a diferencias en la probabilidad de la duración de las
reuniones entonces todas las duraciones tienen la misma probabilidad de ocurrencia en
ese intervalo de tiempo (VAC). Podemos utilizar la Distribución uniforme de VAC.
Si el salón está disponible 3 horas por día, las duraciones pueden ser desde 0 hs  hasta 3 hs
a = 0, b = 3,   C = 1
b − a = 1
3 − 0 = 1
3
P 1 < x < 2 =
 1
b − a dx =  1
3 − 0 dx
2
1
=
2
1

 1
3 dx = 1
3
2
1
x
2
= 1
3 2 − 1 = 1
3 1

<!-- página 4 -->

E x = 1
2 b − a b2 − a2 = 1
2 b − a b + a b − a =
E x = 1
2 b + a
E x =  x. f x dx =  x. C. dx =  1
b − a . x. dx = 1
b − a . x2
2
bb
a
b
a
+∞
−∞
=
a
Esperanza y Varianza de una Distribución uniforme continua:
V x = E x2 − E(x) 2
E x2 =  x2. f x dx
+∞
−∞
=  x2. C. dx = 1
b − a . x3
3
b
= 1
3
b3 − a3
b − a =
b
a

a
b3 + 0b2a + 0ba2 − a3     b − a

<!-- página 5 -->

b3 + 0b2a + 0ba2 − a3     b − a
b2 −b2a b3
b2a +0ba2
+ba
−ba2 b2a
ba2 − a3
+ a2
−a3 ba2
0
b3 − a3
b − a = b2 + ba + a2
E x2 = 1
3 b2 + ba + a2 ,
V x = E x2 − E x 2 = 1
3 b2 + ba + a2 − 1
2 b + a
2
= b2 + ba + a2
3 − b + a 2
4
E x = 1
2 b + a
V x = 4 b2 + ba + a2 − 3 b2 + 2ba + a2
12 = b2 − 2ba + a2
12 = b − a 2
12
V x = b − a 2
12

<!-- página 6 -->

• Distribución normal
     La distribución de probabilidad continua más importante en todo el campo de la
estadística. Su gráfica se denomina ‘curva normal’ o ‘gaussiana’ en honor de Karl
Friedrich Gauss (1777-1855), quien también derivó su ecuación a partir de un
estudio de errores en mediciones repetidas de la misma cantidad. Es la curva
con forma de campana, la cual describe de manera aproximada muchos
fenómenos que ocurren en la naturaleza, la industria y la investigación.
m - s m + s
68 %
f x = 1
2πσ
e−1
2
x−μ
σ
2

−∞ < x < +∞

<!-- página 7 -->

Propiedades
2° Simetría: La curva es simétrica alrededor del eje vertical donde x = m
1° La moda ocurre cuando x = m
μ ≡ Mo

<!-- página 8 -->

Propiedades
3° puntos de inflexión
Cambio de curvatura Cambio de curvatura

<!-- página 9 -->

Propiedades
4° Tendencias
f(x) → 0
x →  +∞ x → −∞
f(x) → 0

<!-- página 10 -->

Propiedades
5° Concavidad
Concavidad hacia abajo
Concavidad hacia arriba Concavidad hacia arriba
μ − σ < x < μ + σ
x > μ + σ x < μ − σ
6° Área bajo la curva  f x dx =  1
2πσ
e−1
2
x−μ
σ
2
dx = 1
+∞
−∞
+∞
−∞

<!-- página 11 -->

Rol de los Parámetros
Diferentes medias
con igual desvío estándar
Diferentes desvío estándar
con igual valor medio

<!-- página 12 -->

Rol de los Parámetros
Diferentes medias
y desvío estándar

<!-- página 13 -->

Problema
Hallar la integral bajo la curva entre dos valores de la VAC para diferentes problemas se
hace muy complejo. Por ejemplo: Alturas de las personas con una m de 170 cm y un
desvío estándar de 12 cm. ¿Qué porcentaje de la población mide entre 165 cm y 190 cm?
P a < x < b =  f x dx =  1
2πσ
e−1
2
x−μ
σ
2
dx = ?
b
a
b
a

<!-- página 14 -->

La curva normal estandarizada:
Por fortuna, podemos transformar todas las observaciones de cualquier variable
aleatoria normal X en un nuevo conjunto de observaciones de una variable aleatoria
normalizada Z con media 0 y varianza 1. Esto se puede realizar mediante la
transformación:
Z = x − μ
σ
De esta forma, la integral de la f(x) pasa a transformarse en la integral de f(z). Al hacer
resta transformación se anula uno de los parámetros:
x = μ + σ. z
dx = σ. dz
P x1 < x < x2 = P z1 < z < z2
P x1 < x < x2 =  f x dx =  1
2πσ
e−1
2
x−μ
σ
2
dx =
x2
x1
x2
x1

P z1 < z < z2 =  1
2πσ
e−1
2 z 2
σ. dz
z2
z1

z1 = x1 − μ
σ
z2 = x2 − μ
σ
Y es fácil tabular las áreas bajo la curva cuando solo depende de la variable Z

<!-- página 15 -->

La distribución normal estándar tiene entonces:
μ = 0
σ = 1

<!-- página 16 -->

Se pueden tabular las F(z), ‘funciones acumuladas de la variable normalizada Z’
De esta forma: P(x1 < x < x2) se transforma en P z < z2 − P(z < z1)
Buscando los valores de z1  y z2  en la tabla.

<!-- página 17 -->

Tabla de áreas bajo la curva F(z)

<!-- página 18 -->

Ejemplo 2.
Dada una variable aleatoria X que tiene una distribución normal con μ = 50 y σ = 10,
calcule la probabilidad de que X tome un valor entre 45 y 62.
Solución: Los valores z que corresponden a X1 = 45 y X2 = 62 son
z1 = 45 − 50
10 = −0.5
z2 = 62 − 50
10 = 1.2
Por tanto:  P 45 < x < 62 = P −0.5 < z < 1.2 = P z < 1.2 − P(z < −0.5)
De tabla: P z < 1.2 = 0.8849 P z < −0.5 = 0.3085
P 45 < x < 62 = 0.8849 − 0.3085 = 0.5764
