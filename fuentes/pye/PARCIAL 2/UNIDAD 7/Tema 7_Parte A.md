# Tema 7_Parte A

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/UNIDAD 7/Tema 7_Parte A.pdf` · 11 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Temario: técnicas de muestreo, distribuciones muestrales, TLC, inferencia. |
| 2 | Definiciones de población (finita/infinita) y parámetros poblacionales. |
| 3 | Muestra, inferencia estadística, muestra insesgada y sesgo. |
| 4 | Muestreo aleatorio irrestricto y sistemático, con ejemplos. |
| 5 | Muestreo por conglomerados y estratificado, con ejemplos. |
| 6 | Estratificado: ejemplo viento (Weibull) con estratos de áreas iguales ⚠ ver el PDF: gráfico con límites a, b, c y estratos |
| 7 | Estadísticas de muestreo: tendencia central y dispersión de la muestra (μx̄, σx̄, CV, cuartiles). |
| 8 | Distribución muestral de X̄: deducción de E(X̄) = μ. |
| 9 | E(X̄) = μ también por esperanza de combinación lineal. |
| 10 | Distribución muestral de la varianza de X̄: V(X̄) = V(X)/n. |
| 11 | Teorema del Límite Central: z = (x̄ − μ)/(σ/√n) ~ N(0;1) para n > 30. |

<!-- página 1 -->

Veremos en este tema algunas técnicas de muestreo de datos y
Distribuciones Muestrales.
w – Cap 8
● Definiciones de Población, Muestra  e Inferencia Estadística.
● Muestras, Sesgo, Tipos de Muestreo.
● Estadísticas de Muestreo y Distribuciones Muestrales: Tendencia Central y Variabilidad.
● Teorema del Límite Central.
● Inferencia: Media, Varianza, Desvío Estándar, Diferencia de Media, Cocientes de Varianza.
● Representaciones  Gráficas.

<!-- página 2 -->

• Población
     Totalidad de los elementos de la entidad bajo análisis.
     El numero de observaciones en la población se define como el tamaño de la
población y representa a todos los elementos en el ámbito de análisis.
Población
Finita. Ej. Número de alumnos en un aula. Ámbito: Aula.
Ej. Número de alumnos en una escuela. Ámbito: Escuela.
Infinita. Ej. mediciones diarias de concentración de gases en la atmósfera.
Ámbito: Atmósfera.
Cada observación de la población toma un valor de la variable aleatoria y su
comportamiento puede ser expresado como una función de variable aleatoria:
B(x; n, p)
N(μ, σ)
Función de V.A.D.
Función de V.A.C.
Cada una de estas funciones de V.A. tiene
parámetros poblacionales que no varían.
Parámetros de la POBLACIÓN

<!-- página 3 -->

• Muestra
     Es un subconjunto de la Población. Una parte de la Población a la cual
analizamos para intentar conocer las características de la Población sin tener que
observar a todos los elementos de ella.
• Inferencia Estadística
    Obtener conclusiones de la población desde el punto de vista estadístico a partir
del subconjunto de observaciones o Muestra.
Si se van a extraer conclusiones de una población a partir de los valores de una o
varias  muestras, éstas deben ser representativas de la población.
Esto significa que la muestra debe ser INSESGADA
• Sesgo
     Se produce por cuestiones de subjetividad en la elección de los elementos de
una o varias muestras de la población.

<!-- página 4 -->

• Técnicas para obtener muestras representativas de una población
- Muestreo Aleatorio Irrestricto
Elección de elementos AL AZAR a partir de la población
Independencia del observador Igual  probabilidad para
todos los elementos de
la población
Ej: función RND# de una calculadora
- Muestreo Sistemático
Elección de algunos elementos de la Población en un orden
SISTEMÁTICO tomando un PASO FIJO (de tiempo o incremento) donde
el primer elemento se selecciona al azar.
Ej: De una lista de alumnos ordenada por abecedario selecciono el primero al
azar y luego los demás tomando un paso de 5 alumnos (quinteo).

<!-- página 5 -->

- Muestreo por Conglomerados
Se opta por este método cuando los dos anteriores no son operativos.
Se seleccionan CONGLOMERADOS EN FORMA ALEATORIA y luego se
observan todos los elementos de ese conglomerado o se utiliza alguno
de los métodos anteriores en ese conglomerado.
Ej: Censo de maestros o alumnos en una provincia. Los alumnos están
agrupados en subconjuntos esparcidos geográficamente (localidades de la
provincia) y se hace oneroso respetar la selección aleatoria de la población de
alumnos para censarlos debido a los gastos de movilidad. En este caso se
seleccionan localidades al azar y se censan todo los alumnos de las escuelas de
las localidades seleccionadas.
- Muestreo Estratificado
La selección de los individuos o elementos de la muestra se PONDERA
POR ESTRATOS PREVIAMENTE DEFINIDOS cuando supongo que la
población no tiene una distribución Normal N(μ, σ). Estos estratos se
elijen en función de la forma de la f x  que define el comportamiento
de la población. Ej: Estratos que cumplan la condición de tener áreas iguales
bajo la f x .

<!-- página 6 -->

Ej: Velocidad del viento. Se sabe que esta variable no sigue una ~N(μ, σ) sino
una ~W α, β . Primero se establece la cantidad de estratos a elegir (debe ser
mayor a 3) para luego encontrar los límites de cada estrato en relación al área
bajo la curva de ~W α, β . Una vez obtenidos estos límites, se realiza el
registro de datos considerando cantidades iguales de mediciones en cada uno
de los estratos. Si no lo hago de esta manera corro el riesgo de tener un mayor
número de mediciones de valores bajos de velocidad del viento y no tener
ninguna medición con valores elevados.
1    2           3      4
 f x dx =  f x dx +  f x dx +  f x dx +  f x dx
∞
c
c
b
b
a
a
0
∞
0

a       b           c
1) Días con baja velocidad
2) Días con Velocidad cercana a Mo
3) Días con velocidad cercana a m
4) Días con altas velocidades

<!-- página 7 -->

Estadísticas de Muestreo
De Tendencia Central y de Dispersión de los parámetros de la
muestra (no de los elementos de la muestra como veníamos
viendo anteriormente.)
- Tendencia Central:  μx  ;   Mox  ;  Mex
- Dispersión:  σx  ;  σx   ;  CVx  ;  Q1 x  ;  Q3 x  ; Rx
2
Estas Estadísticas de Muestreo se obtiene
con ayuda de las Distribuciones Muestrales

<!-- página 8 -->

Distribuciones Muestrales
Densidad de Probabilidad de los estadísticos muestrales
Permite ajustar funciones de densidad de probabilidad de los datos
muestrales y realizar Inferencias acerca de los valores Poblacionales
Distribución Muestral de X:
Si x es una V.A. en una muestra de tamaño n entonces:
xa =  x1 + x2 +  … +  xi +  … +  xn
n      de la muestra a
xj =  x1 + x2 +  … +  xj +  … +  xn
n      de la muestra j
E x = μx =  xj
n = 1
n  xj
n
j=1
n
j=1

⋮
⋮
xn =  x1 + x2 +  … +  xi +  … +  xn
n      de la muestra n
pero  xj = nμ
n
j=1
 E x = 1
n nμ = μ

<!-- página 9 -->

E x = 1
n nμ = μ Que también se puede demostrar a partir de las
propiedades de la Esperanza de una función lineal de V.A.
E ax + b = aE x + b Para el caso de: E x = E
 x
n  a = 1
n , b = 0
x =  x
E x = 1
n E  x = 1
n  E x = 1
n nE x = E x = μ
xa xb xc xj
E x = μ x = μ

<!-- página 10 -->

Distribución Muestral de V(x):
Habíamos visto la propiedad de la Varianza de una combinación lineal de V.A. x:
V ax + b = a2V(x)
Entonces ahora:  V x = V 1
n  x  Como en el caso anterior a = 1
n , b = 0
x =  x
V x = 1
n2 V  x = 1
n2  V x = 1
n2 nV(x) = 1
n V(x)
V x = 1
n V(x)

<!-- página 11 -->

Teorema del Límite Central
Si x es una V.A. con ~N(μ, σ) y x  es un estadístico de la muestra
de tamaño n, entonces:
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

Por lo tanto si n → ∞  n > 30  entonces por más que la ~ V.A. x  ≠    ~N μ, σ :
z = x − μ
σ
n
      →        ~N(0,1)
