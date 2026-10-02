# Unidad 2

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 1/UNIDAD 2/Unidad 2.pdf` · 10 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Resumen Tema 2: medidas descriptivas, media, media ponderada (muestra y población). ⚠ ver el PDF: fracciones y sumatorias rotas |
| 2 | Mediana, medias ponderadas (plazo fijo, media general), moda, cuartiles, deciles y percentiles. ⚠ ver el PDF: fórmulas de posición rotas |
| 3 | Caja y extensión, varianza, desvío, rango, CV; deducción de S². ⚠ ver el PDF: diagrama de caja y sumatorias rotas |
| 4 | Fórmula abreviada de S²; teorema de Chebyshev (k = 2, 75%). ⚠ ver el PDF: fracciones rotas y gráfico de la curva |
| 5 | Pasos con P12,5 y P87,5 para Chebyshev; problema de nicotina (40 datos), incisos a–o. ⚠ ver el PDF: gráfico de la curva |
| 6 | Resultados a–h: tallo y hojas, media 1,774, mediana 1,77, Q1, Q3, S² 0,152, SK, Cu; inicio de agrupar. |
| 7 | Caja y extensiones (IQ 0,365), S², R, CV, SK 0,031, Cu 0,5145; NIC = 7, A = 0,30. ⚠ ver el PDF: falta el gráfico de caja |
| 8 | Tabla de frecuencias agrupada de nicotina y deducción de la moda (aquí 1,72, no 1,78). ⚠ ver el PDF: histograma/polígono; el último IC acá es [2,4−2,8) |
| 9 | Ojiva y fórmulas de interpolación; media 1,785, mediana 1,794, Q1 1,618, Q3 2,03 agrupados. ⚠ ver el PDF: gráfico de la ojiva |
| 10 | Dispersión agrupada (S² 0,149, S 0,385, CV 0,2153), SK −0,046, Cu 0,2978 y comparación sin agrupar vs agrupado. ⚠ ver el PDF: tabla comparativa con columnas separadas |

<!-- página 1 -->

Tema 2: Resumen de datos y descripciones estadísticas

Finalidad: Presentar un conjunto de datos analizados desde el punto de vista estadístico.

Descripción Estadística: Realizar un análisis de datos considerando medidas descriptivas.

Medidas descriptivas:
● Medias de Posición
● Medidas de Dispersión
● Sesgo

Puede trabajarse:
● Con datos sin Agrupar (poca cantidad de datos)
● Con datos agrupados (en intervalos, muchos datos)

Medidas de Posición:
● Media Aritmética
● Media Ponderada
● Mediana
● Moda
● Cuartiles, Deciles, Percentiles.

Medidas de Dispersión:
● Desvío Estándar
● Varianza
● Rango
● Coeficiente de Variación

Otras medidas:
● Asimetría
● Curtosis

Medidas de Tendencia Central

Media Aritmética:
- de una muestra:  X̅ =
∑ Xi
n
i=1
n
- de una población: μ =
∑ XiN
i=1
N

Media Ponderada:
- de una muestra: Xw  =
∑ (w .x)n
i=1
∑ (w)n
i=1
- de una población: μw  =
∑ (w .x)N
i=1
∑ (w)N
i=1

<!-- página 2 -->

Mediana (centro de los datos):
Divide al conjunto de datos en dos partes iguales (se deben ordenar los datos).

X̃  =  Xn + 1
2
    n impar
 X̃ =
1
2 [Xn
2
 +  Xn
2 + 1]           n par

Medidas de Posición Ponderadas:
Tienen en cuenta la importancia relativa de cada dato.
Ej: inversiones a Plazo Fijo:

Rendimiento: 7%, 8%, 9% (si coloco diferentes cantidades de dinero a plazo fijo).
Rendimiento Medio:
7 + 8 + 9
3  =  8%
Rendimiento Medio Ponderado: Xw  =
x1 .w1 + x2 .w2 + x3 .w3
w1 + w2 + w3
 =
∑ (xi .wi)3
i=1
∑ (wi)3
i=1
Siendo wi: cantidad de dinero.

Ej: Media General
Si en un proceso de muestreo queremos conocer el Promedio General de los parámetros de las k
muestras distintas:
- Medias Muestrales:X1; X2; X3; . . . ; Xk
Obtenemos que: n1; n2; n3; . . . ; nk datos
X  =  n1 . X1  +  n2 . X2 + . . . + nk . Xk
n1  +  n2 + . . . + nk
 =
∑ (ni . Xi)k
i=1
∑ ni
k
i=1

Moda: Valor de mayor frecuencia
- Puede ser unimodal y bimodal
- Puede no haber moda. Ej: 3 valores o más con la misma frecuencia (más alta)

Cuartiles, Deciles y Percentiles (con datos ordenados):
Q1  =  Xn + 1
4
   ; Q2  =  Xn + 1
2
 =  X̃  ; Q3  =  X3 .(n + 1)
4
   con n impar
Q1  =
1
2 . (Xn
4
 +  Xn
4 + 1) ; Q2  =
1
2 . (Xn
2
 +  Xn
2 + 1) ; Q3  =
1
2 . (X3 .n
4
 +  X3
4 .( n + 1)) con n par

Ej: n = 10
1 2 (3) 4 5   | 6 7 (8) 9 10
  Q1     Q2   Q3
Ej: n = 12
1 2 3     | 4 5 6    | 7 8 9    | 10 11 12
       Q1       Q2       Q3

D1  =  Xn + 1
10
   ;  D2  =  X 2
10 .(n + 1)  ...   n impar
D1  =
1
2 . ( X n
10
 +   X n
10 + 1) ; D2  =
1
2 . ( X 2
100 .n  +  X 2
100 .(n + 1)) … n par

P1  =  Xn + 1
100
   ; P2  =  X 2
100 .(n + 1) …   n impar
P1  =
1
2 . (X n
100
 +  X n
100 + 1) ; P2  =
1
2 . (X 2
100 .n  +  X 2
100 .(n + 1))  n par

<!-- página 3 -->

Gráfico de Caja y Extensión
Rango intercuartil: RIQ  =  Q3  − Q1

Medidas de Dispersión
● Varianza
- Muestra: S2  =
∑ (Xi −X )2n
i=1
n − 1       (n-1 grados de libertad de los datos de la muestra)
- Población: σ2  =
∑ (Xi − μ)2N
i=1
N

● Desvío estándar:

- Muestra: S = √S2
- Población: σ = √σ2

● Rango: R =  Xmax  − Xmin

● Coeficiente de Variación
- Muestra: CV =
S
X
- Población: CV =
σ
μ

Fórmula desagregada de S2 a nivel de los datos:

S2  =
∑ (Xi −X)2n
i=1
n − 1    pero    X  =
∑ Xin
i=1
n

S2  =
∑ [Xi −(
∑ Xin
i=1
n )]
2
n
i=1
n − 1   cuadrado de un binomio

S2  =
∑ [Xi
2 − 2Xi (
∑ Xin
i=1
n ) +  (
∑ Xin
i=1
n )
2
]n
i=1
n − 1    distribución Σ

S2  =
∑ Xi
2n
i=1 −2 ∑ [Xi (
∑ Xin
i=1
n )]n
i=1   + ∑ (
∑ Xin
i=1
n )n
i=1
2
n − 1
∑ Xi
n
i=1
n  = es la media aritmética, por lo
           tanto es una Constante.

<!-- página 4 -->

S2  =
∑ Xi
2n
i=1 −  2 (∑ Xi
n
i=1
n ) (∑ Xi
n
i=1 )  +  n (∑ Xi
n
i=1
n )
2
n −  1
=
∑ Xi
2n
i=1   − 2 (∑ Xi
n
i=1 )2
n  +  (∑ Xi
n
i=1 )2
n
n −  1

S2  =
∑ Xi
2n
i=1   −  (∑ Xi
n
i=1  )2
n
n −  1  =  n ∑ Xi
2n
i=1   −  (∑ Xi
n
i=1  )2
n ( n −  1 )

S2  =  n ∑ Xi
2n
i=1   −  (∑ Xi
n
i=1  )2
n  ( n −  1 )

Teorema de Chebyshev

Si S es pequeño los datos están agrupados más cerca de la media.
¿Cómo definimos S pequeño o S grande?

Teorema: en relación a un conjunto de datos cualquiera (poblacional o muestral) y una constante
k > 1 cuando menos 1 −
1
k2 de los datos debe estar dentro de k desvíos estándar a uno y otro lado
de la media para que la dispersión se considere pequeña.

Ejemplo: si elegimos k =  2 entonces 1 −
1
k2  =
3
4  =  75 %. El 75% de los datos debe estar a
 X +  2S  y  X −  2S para que la desviación se considere pequeña.

a) Ordenar los datos
b) Calcular P12,5 y P87,5

P12,5  =
X12,5
100  . n ; P87,5  =
X87,5
100  . n

c) Calcular 1 −
1
k2   ⇒  Si k = 2 ⇒ 1 −
1
4  =
3
4

<!-- página 5 -->

d) Si  P12,5  >  X  +  2S  Y  P87,5  <  X  −  2S  entonces el 75% de los datos están dentro de 2
desvíos estándar alrededor de la media y la dispersión es pequeña.

Problema:
Se ha obtenido una muestra del contenido de nicotina (en miligramos) de 40 cigarrillos seleccionados
al azar de una empresa tabacalera.

1.24 2.08 1.79 1.58 1.67 1.69 0.72 2.31
1.51 2.55 1.88 1.75 1.37 1.63 1.09 2.46
1.47 1.40 2.03 2.09 0.85 1.92 1.70 1.93
1.68 1.64 1.85 2.37 1.79 1.82 2.11 1.86
1.64 1.69 1.97 2.17 1.74 1.75 2.28 1.90

a) Definir Población objetivo.
b) Definir variable aleatoria.
c) Realizar gráfico de tallo y hojas(original).
d) Realizar el gráfico de tallo y hojas ordenado.
e) Calcular las medidas de posición (X, X̃, Q1, Q2, Mo).
f) Realizar el gráfico de caja y extensiones.
g) Calcular las medidas de dispersión (S2, S, R, CV).
h) Calcular el coeficiente de asimetría de Pearson e indicar si existe asimetría y tipo.
i) Agrupar en intervalos de clase.
j) Realizar el Histograma y Polígono de frecuencias simples y relativas simples.
k) Realizar la gráfica de frecuencias acumuladas simples, relativas simples y la ojiva ascendente.
l) Determinar las medidas de posición para datos agrupados de forma gráfica y analítica.
m) Calcular la varianza, desvío estándar y coeficiente de variación para datos agrupados.
n) Calcule la asimetría de Pearson considerando las variables obtenidas para datos agrupados e
indique el tipo de asimetría.
o) Compare las medidas de posición y dispersión calculadas para datos sin agrupar y datos
agrupados. Extraiga conclusiones de esta comparación.

<!-- página 6 -->

Resultados:
a) La población objetivo es la población de cigarrillos que fabrica la empresa tabacalera.
b) La variable aleatoria es el contenido de nicotina de los cigarrillos en miligramos (mg).
c) Gráfico de Tallo y Hojas original:

0
0+ 85 72
1 24 47 40 37 09
1+ 51 68 64 64 69 79 88 85 97 58 75 67 79 74 69 63 92 82 75 70 90 80
93
2 08 03 09 37 17 11 28 31 46
2+ 55

d) Gráfico de Tallo y Hojas ordenado:
0
0+ 72 85
1 09 24 37 40 47
1+ 51 58 63 64 64 67 68 69 69 70 74 75 75 79 79 82 85 86 88 90 92 93
97
2 03 08 09 11 17 28 31 37 46
2+ 55

e) Medidas y posición
X =  ∑ xi/n
n
i=1
 =  70,97
40 = 1,774  mg

 X̃ = Xn/2 + Xn/2+1
2  =  X20 + X21
2  =  1,75 +  1,79
2  =  1,77  mg

Q1  =  Xn/4 + Xn/4+1
2  =   X10 + X11
2  =  1,63 + 1,64
2  =  1,635  mg

Q3  =  X3/4n + X3/4n+1
2  =   X30 + X31
2  =  1,97 + 2,03
2  =  2,000  mg

Mo : Sin moda.

<!-- página 7 -->

f) Gráfico de Caja y Extensiones

Q1 =  1,635  mg  IQ = Q3  =  Q1  =  0,365  mg
Q3  =  2,000  mg
 X̃ =  1,77  mg   Dato Raro Xr
+  =  Q3 + 1,5. IQ
 X =  1,774  mg    Xr
+  =  2,000 + 1,5.0,365
      Xr
+  =  2,5475 mg
Xmax  = >  Xr  →  Dato raro  X/X > 2,5475  mg
Xmin  =  Q1  −  1,5. IQ =  1,088 ;  X/X <  1,088   mg

g) Medidas de dispersión

 S2 =
n ∑ Xi
2n
i=1  − (∑ Xi
n
i=1  )2
n(n−1)  =
40 .  131,8343 − (70,97)2
40 (39)

S2  =  0,152 mg2   R =  Xmax  − Xmin  =  1,83  mg
S =  √S2  =  0,39 mg  CV =
S
X  =
0,39
1,774  =  0,2198

h) Coeficiente de Asimetría de Pearson

SK =  3 ( X − X̃ )
S  =  3 (1,774 −  1,77)
0,39  =  0,031
Leve asimetría positiva ➙ SK > 0
Cu =
1
n
∑ (xi−X)
4
 n
i=1
S4 − 3 =
1
40
3,2474
0,0231 − 3 = 0,5145 > 0          Leptocúrtica

i) Agrupar en intervalos de clase
NIC =  5 log10n  =  8,01
NIC =  √N   = √40  =  6,32

NIC =  5 log10n  =  8,01
NIC = 7 intervalos de clase
NIC =  √N   = √40  =  6,32

A =  R
NIC  =  Xmax  − Xmin
NIC  =  2,55 −  0,75
7  =  0,257
A → 0,30

<!-- página 8 -->

IC Xpm fa fr fr% Fa Fr Fr%
[0,7 - 1,0) 0,85 2 0,05 5 2 0,050 5
[1,0 - 1,3) 1,15 2 0,05 5 4 0,100 10
[1,3 - 1,6) 1,45 5 0,125 12,5 9 0,225 22,5
[1,6 - 1,9) 1,75 17 0,425 42,5 26 0,650 65  − Q1
[1,9 - 2,2) 2,05 9 0,225 22,5 35 0,875 82,5  − Q2
[2,2 - 2,4) 2,35 4 0,100 10,0 39 0,975 95
[2,4 - 2,8) 2,65 1 0,025 2,5 40 1,000 100
  40 1,000 100

j) Histograma y Polígono de frecuencias simples y relativas simples - Polígono de frecuencias

H1
b1
 =
H2
b2

b1 = fi − (fi − 1)      -   H2 = H1
b1
b2
H2 = A − H1

b2 = fi − (fi + 1)
A = H1 + H2                      0 = H1
b1
b2
− (A − H1)  0 = H1 (
b1
b2
+ 1) − A  H1 =
A
b1
b2
+1

H1 = Mo − Li =
A
fi−(fi−1)
fi−(fi+1)+1
 Mo = Li +
A
fi−(fi−1)
fi−(fi+1)+1
           Mo = 1,6 +
0,3
17−5
17−9+1
= 1,72 mg

<!-- página 9 -->

k) Gráfico de Frecuencias acumuladas simples y acumuladas relativas simples - Ojiva.

X̃−Li
A  =
0,5 − Fr(i−1)
Fri − Fr(i−1)
   ;
Q1−Li
A  =
0,25 − Fr(i − 1)
Fri − Fr(i − 1)
   ;
Q3−Li
A  =
0,75 − Fr(i − 1)
Fri − Fr(i − 1)

l) Medidas de Posición para datos agrupados

 X =  ∑(XPMi . fri)
k
i=1
 =  1,785  mg

 X̃ =  Li  +
0,5 −  Fr(i − 1)
Fri  −  Fr(i − 1)
 . A =  1,6 + 0,5 −  0,225
0,65 −  0,225 . 0,3 =  1,794   mg

Q1  =   Li  + 0,25 −  Fr(i − 1)
Fri  − Fr(i − 1)
 . A =  1,6 +  0,25 −  0,225
0,65 −  0,225 . 0,3 =  1,618  mg

Q3  =   Li  +
0,75 −  Fr(i − 1)
Fri  −  Fr(i − 1)
 . A =  1,9 +  0,75 −  0,65
0,875 −  0,65 . 0,3 =  2,03  mg

<!-- página 10 -->

m) Medidas de dispersión para datos agrupados

S2  =  n ∑ (XPM
2  . fai)k
i=1  −  [∑ (XPM . fai)k
i=1 ]
2

n (n −  1)  =  40 (133,6)  −  (71,5)2
40 (39)  =  0,149  mg
S =  √S2  =  0,385  mg
CV =  S
X
 =  0,385
1,7875  = 0,2153

n) Asimetría y Curtosis

SK =  3 ( X −  X̃)
5  =  3 (1,7875 −  1,794)
0,417  = −0,046
Levemente asimétrica negativa.   SK < 0

Cu =
1
n
∑ [(XPM−X)
4
.fai]k
i=1
S4 − 3 =
1
40
2,92855
0,0222 − 3 = 0,2978 > 0   Leptocúrtica

o) Comparación de medidas de posición y dispersión

 Datos sin agrupar Datos agrupados
X
Mo
Q1
Q3
X̃
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
1,72
1,618
2,030
1,794
-0,046
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
0,2153
2,1
