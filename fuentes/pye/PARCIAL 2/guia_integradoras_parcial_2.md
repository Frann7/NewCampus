# guia_integradoras_parcial_2

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/guia_integradoras_parcial_2.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Ej. 1: continua, densidad kx(2−x) (k, F(x), E, V, costo, demostración de V) · Ej. 2: conjunta discreta 3x3 (marginales, Cov, ρ, independencia) · Ej. 3: Poisson λ = 3,2/día · Ej. 4: normal (μ = 240, σ = 30) y X̄ con n = 36 · Ej. 5: t de Student, IC para μ (n = 12) · Ej. 6 (incisos a a c): elegir modelo (binomial negativa, geométrica, exponencial) |
| 2 | Ej. 6 (incisos d a f): binomial, Poisson, t de Student · Ej. 7: uniforme discreta, binomial, hipergeométrica · Ej. 8: geométrica (falta de memoria) y binomial negativa · Ej. 9: uniforme continua y exponencial · Ej. 10: gamma y Weibull · Ej. 11: aproximación normal de la binomial · Ej. 12: chi-cuadrada · Ej. 13: F de Snedecor (los Ej. 10, 12 y 13 no son del programa) |

<!-- página 1 -->

Universidad Autónoma de Entre Ríos – Facultad de Ciencia y Tecnología
Licenciatura en Sistemas de Información – Probabilidad y Estadística
Prof. Clarisa Affranchino y Prof. Melina Flesler
Guía integradora para el segundo parcial
Ejercicio 1 – Variable aleatoria continua.
El tiempo diario, medido en horas, durante el cual un servi-
dor permanece sometido a una carga elevada se modela me-
diante la variable aleatoria continuaX, cuya función de den-
sidad es
f(x) =
{︄
kx(2−x),0<x<2,
0,en otro caso.
a) Determine el valor dekpara quefsea una función de
densidad.
b) CalculeP(0.5<X <1.5)yP(X >1.2).
c) Obtenga la función de distribución acumuladaF(x).
d) CalculeE(X)yE(X 2).
e) CalculeV(X)y el desvío estándar deX.
f) Si el costo diario asociado a la carga se expresa mediante
C(X) = 120 + 35X−10X 2,
calculeE[C(X)]e interprete el resultado.
g) Demuestre, partiendo de la definición de varianza, que
V(X) =E(X 2)−[E(X)] 2.
Ejercicio 2 – Distribución conjunta.
En una jornada de trabajo se registran el número de servi-
cios críticos que presentan fallas,X, y el nivel de demanda
del soporte técnico,Y. La distribución conjunta es:
Y= 1Y= 2Y= 3 fX(x)
X= 1 0.10 0.05 0.02
X= 2 0.10 0.35 0.05
X= 3 0.03 0.10 0.20
fY (y) 1
a) Complete las distribuciones marginales deXy deY.
b) CalculeE(X),E(Y),V(X)yV(Y).
c) CalculeE(XY)yCov(X,Y).
d) Calcule el coeficiente de correlación linealρXY .
e) Interprete el signo y la intensidad de la relación
obtenida.
f) Determine siXeYson independientes. Justifique uti-
lizando probabilidades.
g) Demuestre que
Cov(X,Y) =E(XY)−E(X)E(Y).
h) Explique por qué la independencia implica covarianza
nula y por qué la recíproca no es necesariamente ver-
dadera.
Ejercicio 3 – Distribución de Poisson.
Las interrupciones de un servicio web ocurren de manera
independiente, a una tasa promedio de 3.2 por día. SeaX
el número de interrupciones registradas durante un día.
a) Justifique por qué puede utilizarse un modelo de Poisson
e identifique su parámetro.
b) Calcule la probabilidad de que no se produzcan inter-
rupciones durante un día.
c) Calcule la probabilidad de que se produzcan, como máx-
imo, dos interrupciones.
d) Calcule la probabilidad de que se produzcan más de cu-
atro interrupciones.
e) Determine la esperanza y la varianza deX.
f) Suponiendo que la tasa se mantiene constante, calcule
la probabilidad de que durante 6 horas ocurra al menos
una interrupción.
Ejercicio 4 – Distribución normal y media muestral.
El tiempo de respuesta de una aplicación se distribuye nor-
malmente con media240milisegundos y desvío estándar30
milisegundos.
a) Calcule la probabilidad de que una solicitud tarde más
de290milisegundos.
b) Determine el tiempo que no es superado por el90%de
las solicitudes.
c) Si se selecciona una muestra aleatoria de 36 solicitudes,
indique la distribución de¯X, su media y su error están-
dar.
d) CalculeP(232< ¯X <248).
e) Compare los resultados de los incisos a) y d). Explique
porquéladistribucióndelasmediasmuestralespresenta
menor dispersión.
Ejercicio 5 – Distribucióntde Student.
Luego de una actualización se toma una muestra aleatoria
de 12 tiempos de respuesta. Se obtiene una media de248
milisegundos y un desvío estándar muestral de18milisegun-
dos. Supongaquelavariablesedistribuyeaproximadamente
de forma normal y que el desvío poblacional es desconocido.
a) Explique por qué corresponde utilizar la distribuciónt
de Student e indique los grados de libertad.
b) Calcule el valor del estadístico
T=
¯X−µ 0
S/√n
para analizar la afirmaciónµ0 = 240.
c) Determine si el estadístico pertenece al intervalo com-
prendido entre−t 0.025 yt 0.025.
d) Construya un intervalo de confianza del95%para el
tiempo medio de respuesta.
e) Redacte una conclusión contextualizada. Diferencie en-
treno rechazarla afirmación y afirmar que fue de-
mostrada.
Ejercicio 6 – Selección del modelo.
Para cada situación, identifique una distribución adecuada,
defina la variable aleatoria y especifique sus parámetros. No
realice los cálculos.
a) Número de intentos necesarios hasta lograr tres conex-
iones exitosas, con probabilidad constante de conexión.
b) Númerodeintentosnecesarioshastalaprimeraconexión
exitosa.
c) Tiempo transcurrido hasta la próxima interrupción de
un sistema con tasa constante.

<!-- página 2 -->

d) Número de paquetes defectuosos entre 20 paquetes in-
dependientes.
e) Cantidad de solicitudes que llegan a un servidor durante
un minuto.
f) Promedio de una variable normal calculado a partir de
unamuestrapequeña, convarianzapoblacionaldescono-
cida.
Ejercicio 7 – Uniforme discreta, binomial e hiperge-
ométrica.
Resuelva cada situación identificando previamente la vari-
able aleatoria, su soporte y sus parámetros.
a) Unsistemaasigna, alazaryconigualprobabilidad, cada
nueva tarea a uno de 8 servidores numerados del 1 al 8.
SeaXel número del servidor elegido. Escriba la función
de probabilidad, calculeP(X≥6),E(X)yV(X).
b) Cada paquete transmitido tiene una probabilidad0.08
de llegar con error, independientemente de los demás.
Si se observan 20 paquetes, calcule la probabilidad de
que exactamente 2 presenten error, de que ninguno lo
presente y de que haya al menos 3 con error. Obtenga
también la esperanza y la varianza.
c) En un lote de 50 módulos de memoria hay 6 defectuosos.
Se seleccionan 5 sin reemplazo. Calcule la probabilidad
de obtener exactamente uno defectuoso y la probabili-
dad de obtener al menos uno.
d) Explique por qué en b) corresponde usar una binomial y
en c) una hipergeométrica. Indique qué cambia respecto
de la independencia de los ensayos.
Ejercicio 8 – Geométrica y binomial negativa.
La probabilidad de que un intento de conexión resulte exi-
toso es0.70. Considere intentos independientes y una prob-
abilidad de èxito constante.
a) SeaXel número de intentos necesarios hasta la primera
conexión exitosa. Identifique su distribución y calcule
P(X= 3),P(X >4),E(X)yV(X).
b) Utilice la propiedad de falta de memoria para calcular
P(X >7|X >4).
Interprete el resultado.
c) SeaYel número de intentos necesarios hasta alcanzar
la tercera conexión exitosa. Identifique su distribución
y calculeP(Y= 5)yP(Y≤5).
d) Explique la relación entre las distribuciones geométrica
y binomial negativa.
Ejercicio 9 – Uniforme continua y exponencial.
a) El tiempo de descarga de un archivo se distribuye uni-
formemente entre 8 y 20 segundos. Escriba la densi-
dad, represéntela gráficamente y calculeP(X <12),
P(10<X <16),E(X)yV(X).
b) El tiempo, en minutos, hasta la próxima solicitud a un
servidor se modela mediante una distribución exponen-
cial con tasaλ= 2. CalculeP(X >1),P(X≤0.5),
E(X)yV(X).
c) CalculeP(X >2.5|X >1.5)y relacione el resultado
con la propiedad de falta de memoria.
d) Indique la relación existente entre la distribución expo-
nencial de los tiempos entre llegadas y la distribución de
Poisson del número de llegadas.
Ejercicio 10 – Gamma y Weibull.
a) Las solicitudes llegan a un servidor según un proceso de
Poisson a una tasa de 2 por minuto. SeaTel tiempo
transcurrido hasta la cuarta solicitud. Identifique la dis-
tribución deTy sus parámetros. CalculeE(T),V(T)y
P(T >3).
b) La duraciónX, en horas, de un componente electrónico
tiene distribución Weibull con función de distribución
F(x) = 1−e −(x/500)2
, x>0.
Calcule la probabilidad de que el componente dure más
de 400 horas, la probabilidad de que falle antes de 600
horas y la mediana de la duración.
c) Compare las aplicaciones habituales de las distribu-
ciones gamma, exponencial y Weibull. Señale cuál de
ellas posee la propiedad de falta de memoria.
Ejercicio 11 – Aproximación normal de la binomial.
En una plataforma, el35%de los usuarios habilita la aut-
enticación en dos pasos. Se seleccionan al azar 200 usuarios
y se defineXcomo la cantidad que tiene habilitada esta
función.
a) Identifique la distribución exacta deXy calcule su me-
dia y su varianza.
b) Verifique las condiciones para aproximar la distribución
binomial mediante una normal.
c) Utilizando la corrección por continuidad, aproxime
P(60≤X≤80).
d) Aproxime la probabilidad de que más de 75 usuarios
tengan habilitada la autenticación.
e) Explique por qué debe utilizarse la corrección por con-
tinuidad.
Ejercicio 12 – Distribución chi-cuadrada.
El tiempo de ejecución de un proceso se distribuye normal-
mente. Una muestra aleatoria de 15 ejecuciones presenta
una varianza muestral de16segundos cuadrados. Se desea
analizar si la varianza poblacional puede considerarse igual
a9segundos cuadrados.
a) Identifique la variable pivotal basada enS 2 y su dis-
tribución.
b) Calcule el estadístico
χ2 = (n−1)S 2
σ2
0
y determine sus grados de libertad.
c) Busque en la tabla los valores críticos que dejan0.025
en cada cola.
d) Determine si el valor calculado pertenece a la región cen-
tral del95%y redacte una conclusión.
e) Construya un intervalo de confianza del95%paraσ 2.
Ejercicio 13 – DistribuciónFde Snedecor.
Se comparan los tiempos de respuesta de dos configuraciones
de un sistema. Para la configuración A se obtienen1 = 10
yS 2
1 = 25; para la configuración B,n 2 = 12yS 2
2 = 9.
Suponga poblaciones normales y muestras independientes.
a) Forme el cociente de varianzas colocando la mayor en el
numerador e indique los grados de libertad del numer-
ador y del denominador.
b) Calcule el valor observado deF.
c) Busque en la tabla el valorf0.05(ν1,ν 2)y compárelo con
el estadístico calculado.
d) Analice si existe evidencia para considerar diferentes las
varianzas poblacionales al nivel del5%.
e) Explique por qué se cumple
f1−α(ν1,ν 2) = 1
fα(ν2,ν 1).
