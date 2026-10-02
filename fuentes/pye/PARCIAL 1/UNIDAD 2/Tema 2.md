# Tema 2

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 1/UNIDAD 2/Tema 2.pdf` · 23 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Finalidad de la estadística descriptiva. |
| 2 | Descripción estadística: medidas de posición, dispersión y forma; datos sin agrupar (n<30) vs agrupados (n>30). |
| 3 | Listado de medidas de posición, dispersión y forma, con su definición. |
| 4 | Sin agrupar: media, mediana, moda, media ponderada (muestra y población). ⚠ ver el PDF: fracciones y sumatorias rotas |
| 5 | Cuartiles, deciles y percentiles (n par e impar); rango intercuartil. ⚠ ver el PDF: fórmulas de posición rotas y gráfico de caja |
| 6 | Varianza, desvío, rango y coeficiente de variación, muestra y población. ⚠ ver el PDF: sumatorias y raíces rotas |
| 7 | Deducción de la fórmula abreviada de S² (n·ΣX² − (ΣX)²)/(n(n−1)). ⚠ ver el PDF: derivación con sumatorias rotas |
| 8 | Teorema de Chebyshev: al menos 1 − 1/k² de los datos a k desvíos; ejemplo k = 2 (75%). ⚠ ver el PDF: falta el gráfico de la curva |
| 9 | Procedimiento para verificar Chebyshev con P12,5 y P87,5 (k = 2). ⚠ ver el PDF: fórmulas rotas y gráfico de la curva |
| 10 | Asimetría de Pearson SK = 3(media − mediana)/S; SK<0, =0, >0. ⚠ ver el PDF: gráfico de curvas asimétricas con media/mediana/moda |
| 11 | Curtosis Cu: mesocúrtica (0), leptocúrtica (>0), platicúrtica (<0). ⚠ ver el PDF: fórmula rota y gráficos de curvas |
| 12 | Enunciado: nicotina de 40 cigarrillos (datos), incisos a–i. |
| 13 | Solución a–d: población, variable, tallo y hojas original y ordenado. |
| 14 | e) Medidas de posición sin agrupar: media 1,774; mediana 1,77; Q1 1,635; Q3 2,000; sin moda. ⚠ ver el PDF: fracciones rotas |
| 15 | f) Caja y extensiones: IQ 0,365, límites de datos raros 1,088 y 2,5475. ⚠ ver el PDF: falta el gráfico de caja |
| 16 | g, h) S² 0,152, S 0,39, R 1,83, CV 0,2198; SK 0,031 (leve asimetría positiva); Cu 0,5145 (leptocúrtica). ⚠ ver el PDF: fracciones rotas |
| 17 | Datos agrupados: NIC (5·log10 n o √n), ancho A = R/NIC; para nicotina NIC = 7, A = 0,30. |
| 18 | Tabla de frecuencias de nicotina (IC, Xpm, fa, fr, Fa, Fr) y tallo y hojas ordenado. |
| 19 | Histograma y polígono; deducción de la moda agrupada Mo = Li + A/(...+1) = 1,78. ⚠ ver el PDF: histograma/polígono y deducción |
| 20 | Ojiva de frecuencias acumuladas y fórmulas para mediana y cuartiles por interpolación. ⚠ ver el PDF: gráfico de la ojiva |
| 21 | Medidas de posición agrupadas: media 1,785; mediana 1,794; Q1 1,618; Q3 2,03; moda 1,78. ⚠ ver el PDF: fracciones rotas |
| 22 | Dispersión y forma agrupadas: S² 0,149, S 0,385, CV 0,2157, SK −0,070, Cu 0,29792. ⚠ ver el PDF: fórmulas con sumatorias rotas |
| 23 | Comparación de estadísticos: datos sin agrupar vs agrupados. ⚠ ver el PDF: tabla con columnas separadas, hay que emparejarla con la imagen |

<!-- página 1 -->

Finalidad:
L – Cap 2 y 3
¿Para qué la Estadísitca?
Para presentar un conjunto de datos analizándolos y
resumiendo sus características principales. Esto de
denomina una DESCRIPCIÓN ESTADÍSTICA DE DATOS

<!-- página 2 -->

Descripción Estadística de Datos:
Realizar un análisis de datos considerando MEDIDAS DESCRIPTIVAS

Medidas Descriptivas:
• Medidas de Posición
• Medidas de Dispersión
• Medidas de Forma

¿Cómo analizamos los datos?
a) Datos sin agrupar (pocos datos, n < 30)
b) Datos Agrupados en intervalos (muchos datos, n > 30)

<!-- página 3 -->

Medidas de Posición: Dividen a los datos obtenidos en partes proporcionales,
de forma que cada parte tenga el mismo número de elementos.
• Media Aritmética
• Media Ponderada
• Mediana
• Moda
• Cuartiles
• Deciles
• Percentiles
Medidas de Dispersión: Nos informan sobre cuánto se alejan del centro los
valores que toman los datos a analizar.
• Desvío Estándar
• Varianza
• Rango
• Coeficiente de Variación
Medidas de Forma: Nos informan acerca de la forma de la distribución de los
datos alrededor de las medidas de tendencia central.
• Asimetría
• Curtosis

<!-- página 4 -->

a) Trabajando con datos sin agrupar
a.1) Medidas de Posición o de Tendencia Central
Media Aritmética:
de una muestra:  X =
 Xin
i=1
n

de una población: μ =
 XiN
i=1
N
Mediana: centro de los datos.
Divide al conjunto de datos en dos
partes iguales (se deben ordenar los
datos).
X  =  Xn + 1
2
        n impar
X =
1
2 Xn
2
 +  Xn
2 + 1    n par
Moda: Valor de mayor frecuencia.  Puede ser unimodal y bimodal.
Puede no haber moda si 3 valores o más son los de mayor frecuencia.
Media Ponderada: Tienen en cuenta la importancia
relativa de cada dato.
de una muestra: Xw  =
 (w .x)n
i=1
 (w)n
i=1

de una población: μw  =
 (w .x)N
i=1
 (w)N
i=1
DATOS ORDENADOS

<!-- página 5 -->

Cuartiles, Deciles y Percentiles: Dividen los datos en cuatro, diez o cien partes iguales.
Los datos deben estar ordenados.
Q1  =  Xn + 1
4
;                  Q2  =  Xn + 1
2
 =  X  ;       Q3  =  X3 .(n + 1)
4
  con n impar
Q1  =
1
2 (Xn
4
+ Xn
4 + 1); Q2  =
1
2 (Xn
2
+ Xn
2 + 1); Q3  =
1
2 (X3 .n
2
+ X3
4 .( n + 1)) con n par
Gráfico de Caja y Extensión: Permite observar
la forma de la distribución de los datos.
Rango intercuartil: RIQ  =  Q3  −  Q1

<!-- página 6 -->

a.2) Medidas de Dispersión
● Varianza:
 Muestra: S2  =
 (Xi −X )2n
i=1
n − 1       (n-1 grados de libertad de los datos de la muestra)
 Población: σ2  =
 (Xi − μ)2N
i=1
N
● Desvío estándar:
 Muestra: S = S2
 Población: σ = σ2

● Rango: R =  Xmax  −  Xmin
● Coeficiente de Variación:
 Muestra: CV =
S
X
 Población: CV =
σ
μ

<!-- página 7 -->

Fórmula desagregada de S2 a nivel de los datos:

S2  =
 (Xi −X)2n
i=1
n − 1     pero    X  =
 Xin
i=1
n     S2  =
 Xi  −  Xi
n
i=1
n
2
n
i=1
n −  1
cuadrado de un binomio: S2  =
 Xi
2  −  2Xi   Xi
n
i=1
n  +    Xi
n
i=1
n
2
n
i=1
n −  1
distribución Σ: S2  =
 Xi
2n
i=1 − 2  Xi   Xi
n
i=1
n
n
i=1   +    Xi
n
i=1
n
n
i=1
2
n −  1
 Xi
n
i=1
n  es la media aritmética, por lo tanto es una Constante:
S2  =
 Xi
2n
i=1 −  2  Xi
n
i=1
n  Xi
n
i=1  +  n  Xi
n
i=1
n
2
n −  1 =
 Xi
2n
i=1   −  2 ( Xi
n
i=1 )2
n  +  ( Xi
n
i=1 )2
n
n −  1
S2  =
 Xi
2n
i=1   −  ( Xi
n
i=1  )2
n
n −  1  =  n  Xi
2n
i=1   −  ( Xi
n
i=1  )2
n ( n −  1 )
Computar:      Xi
2n
i=1
                         Xi
n
i=1
para el cálculo. Se evita pasar
dos veces por todos los datos

<!-- página 8 -->

Teorema de Chebyshev: en relación a un conjunto de datos cualquiera (poblacional o
muestral) y una constante k > 1 cuando menos (1 - 1/k2)  de los datos debe estar
dentro de k desvíos estándar a uno y otro lado de la media para que la dispersión se
considere pequeña.
Si S es pequeño los datos están agrupados más cerca de la media.
¿Cómo definimos S pequeño o S grande?
Ejemplo: si elegimos k =  2 entonces 1 −
1
k2  =
3
4  = 0,75. El 75% de los
datos debe estar a  X +  2S  y  X −  2S para que la desviación se considere
pequeña.

<!-- página 9 -->

a) Ordenar los datos
b) Calcular P12,5 y P87,5

P12,5  = X12,5
100.n ; P87,5  = X87,5
100.n

c) Calcular 1 −
1
k2   ⇒  Si k = 2 ⇒ 1 −
1
4  =
3
4
d) Si  P87,5  >  X  +  2S  Y  P12,5  <  X  −  2S  entonces el 75% de los datos
están dentro de 2 desvíos estándar alrededor de la media y la dispersión
es pequeña.

<!-- página 10 -->

a.3) Medidas de Forma
Asimetría: Miden la mayor o menor simetría de la distribución.

Un índice de Asimetría muy utilizado es el de Pearson.
 SK = 3 X − X
S
SK < 0 SK > 0
SK = 0

<!-- página 11 -->

Curtosis: Miden la mayor o menor concentración de datos alrededor de la media.

El grado de Curtosis es:
Cu = 1
n
 xi − X
4
 n
i=1
S4 − 3
Si este coeficiente es nulo, la distribución se dice normal (similar a la distribución normal de
Gauss) y recibe el nombre de mesocúrtica. Si el coeficiente es positivo, la distribución se
llama leptocúrtica, más puntiaguda que la anterior. Hay una mayor concentración de los
datos en torno a la media. Si el coeficiente es negativo, la distribución se llama platicúrtica y
hay una menor concentración de datos en torno a la media. sería más achatada que la
primera.

<!-- página 12 -->

Ejemplo:
Se ha obtenido una muestra del contenido de nicotina (en miligramos) de 40 cigarrillos
seleccionados al azar de una empresa tabacalera.
1.24 2.08 1.79 1.58 1.67 1.69 0.72 2.31
1.51 2.55 1.88 1.75 1.37 1.63 1.09 2.46
1.47 1.40 2.03 2.09 0.85 1.92 1.70 1.93
1.68 1.64 1.85 2.37 1.79 1.82 2.11 1.86
1.64 1.69 1.97 2.17 1.74 1.75 2.28 1.90
a) Definir Población objetivo.
b) Definir variable aleatoria.
c) Realizar gráfico de tallo y hojas(original).
d) Realizar el gráfico de tallo y hojas ordenado.
e) Calcular las medidas de posición (X, X , Q1, Q2, Mo).
f) Realizar el gráfico de caja y extensiones.
g) Calcular las medidas de dispersión (S2, S, R, CV).
h) Calcular el coeficiente de asimetría de Pearson e indicar si existe asimetría y tipo.
i) Calcular la Curtosis e indicar tipo.

<!-- página 13 -->

Solución:
a) La población objetivo es la población de cigarrillos que fabrica la empresa tabacalera.
b) La variable aleatoria es el contenido de nicotina de los cigarrillos en miligramos (mg).
c) Gráfico de Tallo y Hojas original:
0
0+ 85 72
1 24 47 40 37 09
1+ 51 68 64 64 69 79 88 85 97 58 75 67 79 74 69 63 92 82 75
70 90 80 93
2 08 03 09 37 17 11 28 31 46
2+ 55
d) Gráfico de Tallo y Hojas ordenado:
0
0+ 72 85
1 09 24 37 40 47
1+ 51 58 63 64 64 67 68 69 69 70 74 75 75 79 79 82 85 86 88
90 92 93 97
2 03 08 09 11 17 28 31 37 46
2+ 55

<!-- página 14 -->

e) Medidas y posición
X =
 Xi
n
i=1
n  =  70,97
40 = 1,774 mg
 X =
Xn
2
+ Xn
2+1
2  =  X20 + X21
2  =  1,75 +  1,79
2  =  1,77   mg
Q1  =
Xn
4
+ Xn
4+1
2  =   X10 + X11
2  =  1,63 + 1,64
2  =  1,635   mg
Q3  =
X3n
4
+ X3n
4 +1
2  =   X30 + X31
2  =  1,97 + 2,03
2  =  2,000   mg
Mo : Sin moda.

<!-- página 15 -->

f) Gráfico de Caja y Extensiones:
Q1 =  1,635  mg
 X =  1,77 mg
Q3  =  2,000  mg IQ = Q3  −  Q1  =  0,365  mg
 X =  1,774  mg
Dato Raro Xr+  =  Q3 + 1,5. IQ
Xr+  =  2,000 + 1,5.0,365 = 2,5475 mg
Xmax  = >  Xr  →  Dato raro  X/X > 2,5475 mg
Xmin  =  Q1  −  1,5. IQ =  1,088 ;  X/X <  1,088 mg

<!-- página 16 -->

g) Medidas de dispersión:
S2 =  n  Xi
2n
i=1  −  ( Xi
n
i=1  )2
n(n − 1)  =  40 . 131,8343 −  (70,97)2
40 (39) = 0,152  mg2
S =  S2  =  0,39 mg R =  Xmax  −  Xmin  =  1,83 mg
CV =  S
X
 =  0,39
1,774  =  0,2198
h) Coeficiente de Asimetría de Pearson y Curtosis:
SK =  3 ( X − X  )
S  =  3 (1,774 −  1,77)
0,39  =  0,031
Leve asimetría positiva ➙ SK >  0
Cu = 1
n
 xi − X
4
 n
i=1
S4 − 3 = 1
40
3,2474
0,0231 − 3 = 0,5145 > 0 Leptocúrtica

<!-- página 17 -->

b) Trabajando con datos agrupados
b.0) Agrupar en Intervalos de Clase: IC
NIC = 5. log10 n
NIC = n
5 ≤ NIC ≤ 15
Ancho del IC: A Número de IC: NIC
A = R
NIC
Para el ejemplo de los cigarrillos:
NIC =  5 log10n  =  8,01
NIC =  N   = 40  =  6,32
NIC =  5 log10n  =  8,01
NIC = 7 intervalos de clase NIC =  N   = 40  =  6,32
5 ≤ NIC ≤ 15
A =  R
NIC  =  Xmax  −  Xmin
NIC  =  2,55 −  0,75
7  =  0,257 → 0,30

<!-- página 18 -->

IC Xpm fa fr fr% Fa Fr Fr%
[0,7 - 1,0) 0,85 2 0,05 5 2 0,050 5
[1,0 - 1,3) 1,15 2 0,05 5 4 0,100 10
[1,3 - 1,6) 1,45 5 0,125 12,5 9 0,225 22,5
[1,6 - 1,9) 1,75 17 0,425 42,5 26 0,650 65   − Q1, X
[1,9 - 2,2) 2,05 9 0,225 22,5 35 0,875 82,5  − Q3
[2,2 - 2,5) 2,35 4 0,100 10,0 39 0,975 95
[2,5 - 2,8] 2,65 1 0,025 2,5 40 1,000 100
    40 1,000 100
Tabla de Frecuencias
0
0+ 72 85
1 09 24 37 40 47
1+ 51 58 63 64 64 67 68 69 69 70 74 75 75 79 79 82 85 86 88
90 92 93 97
2 03 08 09 11 17 28 31 37 46
2+ 55
Sabiendo que:
NIC = 7 y A = 0,3
con los datos
originales armamos
La tabla de Frecuencias
Diagrama de tallo y hojas ordenado

<!-- página 19 -->

Histograma y Polígono de frecuencias simples y relativas simples - Polígono de frecuencia
H1
b1
 =  H2
b2

b1 = fi − fi−1
b2 = fi − fi+1
A = H1 + H2
H2 = H1
b2
b1
H2 = A − H1

0 = H1
b2
b1
− A − H1  0 = H1
b2
b1
+ 1 − A H1 = A
b2
b1
+ 1

H1 = Mo − Li = A
fi − fi+1
fi − fi−1
+ 1

 Mo = Li + A
fi − fi+1
fi − fi−1
+ 1
 Mo = 1,6 + 0,3
17 − 9
17 − 5 + 1
= 1,78 mg

<!-- página 20 -->

Gráfico de Frecuencias acumuladas simples y acumuladas relativas simples - Ojiva.
X −Li
A =
0,5 − Fr(i−1)
Fri − Fr(i−1)
   ;
Q1−Li
A =
0,25 − Fr(i − 1)
Fri − Fr(i − 1)
   ;
Q3−Li
A =
0,75 − Fr(i − 1)
Fri − Fr(i − 1)

<!-- página 21 -->

b.1) Medidas de Posición o de Tendencia Central
 X =   (XPMi . fri)
k
i=1
 =  1,785  mg
 X =  Li  +
0,5 −  Fr(i − 1)
Fri  −  Fr(i − 1)
 . A =  1,6 +  0,5 −  0,225
0,65 −  0,225 . 0,3 =  1,794   mg
Q1  =   Li  +  0,25 −  Fr i − 1
Fri  −  Fr i − 1
 . A =  1,6 +  0,25 −  0,225
0,65 −  0,225 . 0,3 =  1,618  mg
Q3  =   Li  +
0,75 −  Fr(i − 1)
Fri  −  Fr(i − 1)
 . A =  1,9 +  0,75 −  0,65
0,875 −  0,65 . 0,3 =  2,03  mg
Mo = Li + A
fi − fi+1
fi − fi−1
+ 1
= 1,6 + 0,3
17 − 9
17 − 5 + 1
= 1,78 mg

<!-- página 22 -->

b.2) Medidas de Dispersión
S2  =  n  (XPM
2  . fai)k
i=1  −   (XPM . fai)k
i=1
2
n (n −  1)  =  40 133,6  −  (71,5)2
40 (39)  =  0,149  mg2
S =  S2  =  0,385  mg
CV =  S
X
 =  0,385
1,785  = 0,2157
a.3) Medidas de Forma
Asimetría: SK =  3 ( X −  X )
S  =  3 (1,785 −  1,794)
0,385  = −0,070
SK < 0 ➙ Levemente asimétrica negativa
Curtosis: Cu = 1
n
 XPM − X
4
. fai
k
i=1
S4 − 3 = 1
40
2,92855
0,0222 − 3 = 0,29792
Cu > 0    Leptocurtica

<!-- página 23 -->

Comparación de estadísticos entre los análisis de datos sin agrupar y datos agrupados
  Datos sin agrupar Datos agrupados
X
Mo
Q1
Q3
X
SK
Cu
1,774
Sin Moda
1,635
2,000
1,77
0,031
0,5145
1,785
1,78
1,618
2,030
1,794
-0.070
0,2978
S2
S
CV
R
0,152
0,390
0,2198
1,83
0,149
0,385
0,2157
2,1
