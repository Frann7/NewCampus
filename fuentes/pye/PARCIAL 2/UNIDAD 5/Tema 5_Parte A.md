# Tema 5_Parte A

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 5/Tema 5_Parte A.pdf` · 14 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Repaso: probabilidad como frecuencia relativa de datos de una muestra. |
| 2 | Repaso: media muestral y E(X), inferencia estadística, V.A.D. vs V.A.C., f.d. y f.d.p. |
| 3 | Repaso: P(X>2) con integral (continua) o suma (discreta); lista de distribuciones a ver. |
| 4 | Título de distribuciones discretas; definición de la uniforme. |
| 5 | Uniforme: f(x,k)=1/k, E y V; enunciados ej. 1 (moneda) y 2 (dado). |
| 6 | Resolución ej. 1 (E=1/2, V=1/4) y ej. 2 (E=3,5, V=35/12). |
| 7 | Binomial: condiciones del proceso de Bernoulli, E=np, V=npq. |
| 8 | Ej. 3: 3 artículos, tabla de eventos y f(x) binomial, p=0,2. |
| 9 | Ej. 4 (vehículos): se chequea que cumple Bernoulli, f binomial. |
| 10 | Ej. 4: x, n, p, q y cuenta f(2; 5; 0,25)=0,26. |
| 11 | Ej. 5: urna 6R 2N con reposición, chequeo de Bernoulli, n=5, p=0,25. |
| 12 | Ej. 5: tabla f(x) para x=0 a 5 y gráfico de barras. |
| 13 | Ej. 5 bis: urna sin reposición, hipergeométrica; f(0)=0,107, f(1)=0,536, f(2)=0,357. |
| 14 | Hipergeométrica: definición, N, n, k, x, E y V; si N es grande tiende a la binomial. |

<!-- página 1 -->

Repaso:
w – Cap 5
• Vimos cómo se pueden calcular probabilidades de ocurrencia de
eventos a partir de la Estadística descriptiva ⇒ Análisis de datos
tomados de una muestra del objeto de estudio.
      Distribuciones empíricas: Tablas, Gráficos, Histogramas.
P A = n
N =  fr → Tablas de frecuencias relativas

<!-- página 2 -->

• Vimos que algunos parámetros  estadísticos como por ejemplo
la media aritmética de una muestra X se pueden expresar en
términos de Probabilidad.
X                →                                E(x)  = μ
Proceso muestral                ↧            Esperanza (valor esperado de la población)
  Inferencia estadística
La inferencia estadística es el conjunto de métodos y técnicas que permiten
inducir, a partir de la información empírica proporcionada por una muestra, cuál
es el comportamiento de una determinada población con un riesgo de error
medible en términos de probabilidad.

S2  → V(x)  = σ2
S  → σ
V. A. D → Función de Distribución   | V AD → f.d.
V. A. C.    →             Función de Densidad de Probabilidad | V AC → f.d.p

<!-- página 3 -->

• Vimos que con las funciones de distribución o función de
densidad de probabilidad se pueden calcular probabilidades de
eventos.
Ej:
X → V. A. C
P(X >  2)  =   f(x) dx
∞
2   → f.d.p de V .A.C

X → V. A. D
P(X ≥  2)  =   f(x) ∞
2   → f.d. de V .A.D
Vamos ahora a estudiar en más detalle estas  f(x) (funciones de distribución) para V .A.D:

● Distribución Uniforme
● Distribución Binomial
● Distribución Hipergeométrica

<!-- página 4 -->

Distribuciones Discretas de probabilidad
Describen el comportamiento de una V.A.D. por su distribución de probabilidad o
cuantía.
• Distribución uniforme
     Cada uno de los elementos del espacio muestral toma probabilidades idénticas.

<!-- página 5 -->

f(x, k)  =  1
k ; x = x1, x2, . . . , xk k  elementos del espacio muestra.
E(x) = μ =  x f(x, k)
k
1
= 1
k  x
k
1

V(x) = σ2 =  (x − μ)2 f(x, k)
k
1

= 1
k   (x − μ)2
k
1

Ejemplo 1.
Arrojar una moneda siendo X el número de caras
f x, k =  1
k = 1
2
Ejemplo 2.
Arrojar un dado y observar el resultado de la
cara superior.
f x, k =  1
k = 1
6
Calcule la Esperanza y la varianza para los ejemplos 1 y 2

<!-- página 6 -->

Ejemplo 1.
E(x) = μ = 1
k  x = 1
2 0 + 1 = 1
2
k
1

V x = σ2 = 1
k  (x − μ)2
k
1
= 1
2  x − 1
2
2
= 1
2
2
x=1
0 − 1
2
2
+ 1 − 1
2
2
= 1
4
Ejemplo 2.
E(x) = μ = 1
k  x = 1
6 1 + 2 + 3 + 4 + 5 + 6 = 21
6 = 3,5
k
1

V x = σ2 = 1
k   (x − μ)2
k
1
= 1
6  x − 21
6
2
= 1
6
6
x=1
1 − 21
6
2
+ … + 6 − 21
6
2
= 35
12

<!-- página 7 -->

• Distribución binomial
     Los resultados de cada una de las pruebas se clasifican en dos categorías.
 Pruebas repetidas con 2 resultados posibles (dicotómica: éxito o fracaso).
 Las pruebas son independientes. El resultado de la anterior no incide en el resultado
de la próxima prueba.
 La probabilidad no varía para cada prueba.
 Extracción con reemplazo si n es finito.
 p =  constante.
 E x = n. p
 V x = n. p. q
En este caso se dice que la variable aleatoria X sigue un Proceso de Bernoulli

-  El experimento consiste en n pruebas que se repiten.
-  Es dicotómica (éxito o fracaso).
-  La probabilidad de éxito se mantiene constante en cada prueba.
-  Las pruebas que se repiten son independientes.

<!-- página 8 -->

Ejemplo 3: Selección aleatoria de tres artículos de un proceso de fabricación
para luego ser clasificados como “D” Defectuoso; “N” No defectuoso. Sea X el
número de artículos defectuosos. Obtener f(x) sabiendo que la máquina tiene
una probabilidad de fabricar un artículo defectuoso del 20%.
Función de distribución: Tabla con los pares (x, f(x))
Evento X Prob.
NNN 0 0,8. 0,8. 0,8
NND 1 0,8. 0,8. 0,2
NDN 1 0,8. 0,2. 0,8
DNN 1 0,2. 0,8. 0,8
NDD 2 0,8. 0,2. 0,2
DND 2 0,2 .0,8. 0,2
DDN 2 0,2. 0,2. 0,8
DDD 3 0,2. 0,2. 0,2
S = {NNN, NND, NDN, DNN, NDD, DND, DDN, DDD} Espacio muestral
P x = 0 = 0,83
P x = 1 = 3. 0,2. 0,82
P x = 2 = 3. 0,22. 0,8
P x = 3 = 0,23
f x = 3
x 0,2x. 0,8 3−x
f x = n
x px. q n−x
siendo:    q = 1 − p
E x = n. p
V x = n. p. q

<!-- página 9 -->

Ejemplo 4: En el Acceso Norte de la ciudad de Paraná se ha comprobado que
durante el fin de semana el 75% de los vehículos que circulan provienen del
interior de la provincia. ¿Cuál es la probabilidad de que dos de los próximos
cinco vehículos no sean del interior?
Solución:
¿Responde al modelo de Bernoulli?
-  El experimento consiste en n pruebas que se repiten.
-  Es dicotómica (éxito o fracaso).
-  La probabilidad de éxito se mantiene constante en cada prueba.
-  Las pruebas que se repiten son independientes.
Pasaje de vehículos en el Acceso
El vehículo es del interior o no lo es.
No cambia  la prob.  de
que el próximo vehículo
sea del interior si el
vehículo que pasó antes
lo era.
No hay vínculo entre el pasaje de dos vehículos sucesivos.
CUMPLE TODOS LOS CRITERIOS DEL PROCESO DE BERNOULLI
f x; n, p =  n
x pxq n−x    ;   x:   V. A. D.  número de veℎiculos de la Capital.
Distribución Binomial
¿Es VAD?

<!-- página 10 -->

f x; n, p =  n
x pxq n−x    ;   x:   V. A. D.  número de veℎiculos de la Capital.
x:
n:
p:
2 vehículos
5 vehículos
0,25
q:  0,75
Ejemplo 4: En el Acceso Norte de la ciudad de Paraná se ha comprobado que
durante el fin de semana el 75% de los vehículos que circulan provienen del
interior de la provincia. ¿Cuál es la probabilidad de que dos de los próximos
cinco vehículos no sean del interior?
f 2; 5,0,25 =  5
2 0,252. 0,753 = 0,26

<!-- página 11 -->

Ejemplo 5: De una urna que contiene 6 bolillas rojas (6R) y 2 bolillas negras
(2N) encontrar la función de distribución para la variable aleatoria x = número
de bolillas negras si se extraen cinco bolillas con reposición.
Solución: ¿Responde al modelo de Bernoulli?
-  El experimento consiste en n pruebas que se repiten.
-  Es dicotómica (éxito o fracaso).
-  La probabilidad de éxito se mantiene constante en cada prueba.
-  Las pruebas que se repiten son independientes.
Sí, n = 5
Sí, Sale R ó N, R -> fracaso, N -> éxito
Sí, porque cada
vez que sacamos
una bolilla, la
reponemos para
la próxima
extracción
Que haya salido R en la extracción anterior no condiciona el resultado
de la siguiente porque la bolilla extraída se repone a la caja.
Con
reposición
x:
n:
p:
N° de bolillas N
5 extracciones
0,25
q:  0,75
f x; 5,0,25 =  5
x 0,25x. 0,75 5−x =

<!-- página 12 -->

Ejemplo 5: De una urna que contiene 6 bolillas rojas (6R) y 2 bolillas negras
(2N) encontrar la función de distribución para la variable aleatoria x = número
de bolillas negras si se extraen cinco bolillas con reposición.
f x; 5,0,25 =  5
x 0,25x. 0,75 5−x
Con
reposición
Función de distribución:
x f(x)
0 0,236
1 0,395
2 0,264
3 0,088
4 0,014
5 0,001
0.000
0.050
0.100
0.150
0.200
0.250
0.300
0.350
0.400
0 1 2 3 4 5
Número de bolillas negras
f(x)

<!-- página 13 -->

Ejemplo 5 (bis): De una urna que contiene 6 bolillas rojas (6R) y 2 bolillas
negras (2N) encontrar la función de distribución para la variable aleatoria
x = número de bolillas negras si se extraen cinco bolillas SIN reposición.
Sin
reposición
• Distribución Hipergeométrica
Como no importa el orden usamos
                  COMBINATORIA
f 0 =  n1 . n2
N  =
2
0
6
5
8
5
= 0,107
x f(x)
0 0,107
1 0,536
2 0,357
Tabla de distribución:
f 1 =  n1 . n2
N  =
2
1
6
4
8
5
= 0,536
f 2 =  n1 . n2
N  =
2
2
6
3
8
5
= 0,357

<!-- página 14 -->

• Distribución Hipergeométrica
Una V. A. x tiene distribución Hipergeométrica si el resultado del experimento consiste en
pruebas DEPENDIENTES, es decir, no se cumplen los postulados de Bernoulli:

- Las probabilidades de éxito cambian de una prueba a otra.
- El resultado de una prueba depende del resultado de la prueba anterior.

Esto ocurre cuando las extracciones son SIN REEMPLAZO y el número de elementos es finito.
H x; N, n, k =
k
x
N−k
n−x
N
n

N: N° total de elementos.
n: N° de extracciones o pruebas
k: N° de elementos de éxito.
x: N° de éxitos de la prueba.
éxitos fracasos
¿Qué pasa si N        ∞ ?
E x = n. k
N  V x = n. k
N 1 − k
N
N − n
N − 1
n ≪ N
k
N = p → ctte E x → n. p V x → n. p. q
H(x; N, n, k) → b(x; n, p)
1
p
