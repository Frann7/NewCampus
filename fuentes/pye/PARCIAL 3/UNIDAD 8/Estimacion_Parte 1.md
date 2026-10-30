# Estimacion_Parte 1

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 3/UNIDAD 8/Estimacion_Parte 1.pdf` · 19 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Portada |
| 2 | Población, muestra, estadísticos y parámetros (esquema) |
| 3 | Estadístico, parámetro, distribución muestral |
| 4 | Estimación puntual, propiedades del mejor estimador |
| 5 | Parámetros y sus estimadores |
| 6 | Idea del IC |
| 7 | TLC |
| 8 | IC: nivel de confianza 1 − α |
| 9 | IC para μ con n ≥ 30 (Z), tabla de z |
| 10 | Esquema del IC y error de estimación |
| 11 | IC para μ con n &lt; 30 (t, ν = n − 1) |
| 12 | Qué significa 1 − α de confianza |
| 13 | ⚠ ver el PDF: Ejemplo 1 (imagen; transcripto en el campus, U8 sección 3) |
| 14 | Resolución del Ejemplo 1 |
| 15 | Ejemplo 2 (t) |
| 16 | Resolución del Ejemplo 2 |
| 17 | ⚠ ver el PDF: IC para una proporción (la fórmula es imagen) |
| 18 | Ejemplo 3 (proporción) |
| 19 | Resolución del Ejemplo 3 (dice 99 %, es 95 %) |

<!-- página 1 -->

PROBABILIDAD Y ESTADÍSTICA
Estimación – Primera Parte
Licenciatura en Sistemas

<!-- página 2 -->

Inferencia Estadística
POBLACIÓN
 MUESTRA
ALEATORIA
Datos
Numéricos
Interés en una…
 Se generan
Estadísticos: �XX,
μpp, SS
Que se los utiliza para:
Estimar o plantear hipótesis
Parámetros:
μμ, ππ, σσ
Que son usados
para describir la

<!-- página 3 -->

Función definida sobre los valores numéricos de una muestra. Cuando su objetivo es estimar un
parámetro poblacional, se denomina también estimador.
Conceptos fundamentales
ESTADÍSTICO �θθ = ff(xx₁, xx₂, … , xxx)
Es una VARIABLE ALEATORIA: su valor cambia de muestra en muestra.
PARÁMETRO POBLACIONAL μ, ππ, σσ
Constante que resume todos los valores de una variable en un único valor. Caracteriza a la
población completa.
Es un valor fijo (casi siempre desconocido). Se simboliza con letra griega θθ.
DISTRIBUCIÓN MUESTRAL PP(�θθ = xx) = ff(xx)
Modelo probabilístico que describe la distribución de probabilidades de un estadístico
considerado como variable aleatoria.
Permite calcular probabilidades sobre el estadístico.

<!-- página 4 -->

Estimación Puntual
Estimamos al parámetro de interés θθ con un único valor calculado a partir de una muestra aleatoria de
tamaño nn. El estadístico elegido debe ser el "mejor estimador" del parámetro.
Propiedades del Mejor Estimador:
Insesgado
EE( �θθ) = θθ
El estimador no sobreestima ni subestima el
parámetro en promedio.
Eficiente
Mínima varianza entre todos los estimadores
insesgados posibles.
Consistente
A medida que nn aumenta, el estimador converge al
verdadero parámetro.
Suficiente
Usa toda la información disponible en la muestra
sobre el parámetro.
Mejores estimadores puntuales: μμμ = �XX �σσ2=S²        �ππ = pp

<!-- página 5 -->

Parámetros Poblacionales y sus Estimadores
Parámetro Poblacional  (θ) Estadístico Estimador (θ)
Media Poblacional μ Media Muestral �XX
Proporción Poblacional π Proporción Muestral �pp
Desvío Estándar
Poblacional σ Desvío Muestral S
Varianza Poblacional σ² Varianza Muestral S²
^

<!-- página 6 -->

Estimación por Intervalo de Confianza
Dado que es improbable que hasta con el estimador “insesgado más eficaz” se
estime puntualmente con exactitud al parámetro poblacional, es preferible
determinar un intervalo dentro del cual esperaríamos encontrar a dicho
parámetro con cierta probabilidad.
Esta alternativa se denomina: ESTIMACIÓN POR INTERVALO DE CONFIANZA
Necesitamos conocer la distribución de
probabilidad del estimador

<!-- página 7 -->

Teorema del Límite Central
Enunciado: Si se extraen muestras aleatorias de nn observaciones de una
población no normal con media finita μμ y desviación estándar σσ, entonces,
cuando nn es grande, la distribución muestral de la media muestral �XXes
aproximadamente normal, con media μμ �XX = μμ y desviación estándar σσ �XX =
σσ
nn
La aproximación se vuelve más precisa a medida que nn aumenta.
Independientemente de su forma, la distribución muestral de �XX siempre tiene una media idéntica a
la media de la población muestreada y una desviación estándar igual a la desviación estándar
poblacional σσ dividida por nn.
Valor Esperado
μμ(�XX) = EE(�XX) = μμ
Varianza
σσ²(�XX) = VVVVVV(�XX) = σσ²/nn

<!-- página 8 -->

Estimación por Intervalos de Confianza
Este método propone fijar un nivel o grado de confianza (1 − αα), donde αα es la
significancia.
De esta forma, a la estimación del parámetro poblacional θθ la podemos plantear como
una probabilidad de que se encuentre entre ciertos límites �θθ1 y �θθ2 con una confianza
del (1 − αα).
PP �θθ1 < θθ < �θθ2 = 1 − αα,

<!-- página 9 -->

Intervalo de Confianza para μ (nn ≥ 3333)
Por el Teorema Central del Límite, si el tamaño de la muestra es grande (≥ 30), se puede asumir una distribución
normal para el estadístico, quedando de la siguiente forma:
PP −zzαα
2
< ZZ =
�XX − μμ
SS
nn
< zzαα/2 = 1 − αα,
donde zzαα/2 es el valor de zz que deja un área de αα/2
a la derecha
�XX − zzαα
2
SS
nn < μμ < �XX + zzαα
2
SS
nn
Nivel de Confianza → Valor zzαα/2
90% z = 1,645
95% z = 1,960
99% z = 2,576
Operando algebraicamente se obtiene:
Intervalo de confianza del
(11 − αα). 1133331 para μμ

<!-- página 10 -->

Estimación por Intervalo de Confianza
μ X̄
LI
X̄ − z(α/2) · S/√n
LS
X̄ + z(α/2) · S/√n
Error de Estimación (E.E.)
Nivel de Confianza =
(1−α)·100%
α/2 α/2
Error de Estimación
 Tamaño de muestra

<!-- página 11 -->

Intervalo de Confianza para μ – para (nn < 3333)
Como σσ es desconocida, se reemplaza por SS.
Intervalo de confianza del (11 − αα). 1133331 para μμ
�XX − ttαα
22;vv
SS
nn < μμ < �XX + ttαα
22;vv
SS
nn ,
donde ttαα/2 es el valor de tt que deja un área de αα/2 a la derecha
Si se tiene una muestra chica extraida aleatoriamente de una población y la variable
XX tiene distribución normal, entonces el estadístico
TT =
�XX−μμ
SS
nn
tiene una distribución tt de Student con vv = nn − 1 grados de libertad.

<!-- página 12 -->

¿Qué significa que tengamos “ 1 − αα 1001 de confianza”?
Significa que si se repite MUCHAS veces el
procedimiento de: seleccionar una
muestra, calcular �XX y 11 − αα 1133331 de
dichos intervalos contendrán el verdadero
valor de μμ.
Como consecuencia, sólo el αα. 1133331 no
contendrá al verdadero valor de μμ.

<!-- página 13 -->

Ejemplo 1
nn ≥ 3333

<!-- página 14 -->

Resolución
Datos:
nn = 64 ≥ 3333
�XX = 22 SS = 4
Nivel de confianza = 95%  →  αα = 0.05 →  zzαα/2 = 1.96
22 − 1.96 4
64
< μμ < 22 + 1.96 4
64
21.02 < μμ
< 22.98
Reemplazamos los datos en la fórmula:
Resultado: IC 95% para μμ =  (21.02 ; 22.98)
Se tiene un 95% de confianza de que el verdadero tiempo medio de respuesta
en las peticiones a un microservicio de autenticación se encuentra entre 21.02
y 22.98 microsegundos

<!-- página 15 -->

Ejemplo 2
nn < 3333
El área de Business Analytics e infraestructura de un sitio de comercio electrónico
analizó el costo de comisión operativa (en dólares USD) por cada microtransacción
procesada a través de su pasarela de pagos en la nube.
Una muestra aleatoria de 16 transacciones arrojó un costo medio muestral de $0.02
USD con una desviación estándar muestral de $0.01 USD.
Suponga que el costo por transacción sigue una distribución aproximadamente
normal y construya un intervalo de confianza del 99% para la media poblacional del
costo por transacción.

<!-- página 16 -->

Resolución
Datos:
0.02 − 2.947 0.01
16
< μμ < 0.02 + 2.947 0.01
16
0.012 < μμ < 0.027
Reemplazamos los datos en la fórmula:
Resultado: IC 99% para μμ =  (0.012 ; 0.027)
Se tiene un 99% de confianza de que el verdadero costo de comisión operativa (en dólares
USD) por cada microtransacción procesada a través de su pasarela de pagos en la nube se
encuentra entre 0.012 y 0.027 microsegundos
nn = 16 �XX = 0.02 SS = 0.01 nn − 1 = 16 − 1 = 15 grados de libertad
Nivel de confianza = 99%  →  αα = 0.01 →  ttαα
2;15 = 2.947

<!-- página 17 -->

Intervalo de Confianza para una Proporción (ππ)
Si �ππ = μpp es la proporción de éxitos en una muestra aleatoria de tamaño nn, un
intervalo de confianza del 1 − αα . 1001 para el parámetro binomial ππ (probabilidad
de éxito) está dado por:
Para muestras grandes.
�pp Proporción muestral
(número de éxitos / n)
 �qq �qq = 1 − μpp
(proporción de fracasos)
nn Tamaño de la muestra
aleatoria tomada
 zzαα/22 Percentil de una normal estándar

<!-- página 18 -->

Ejemplo 3
En una muestra de 300 estudiantes de la Licenciatura en Sistemas, el
80% respondió que cuenta con una computadora portátil propia para
realizar las prácticas de las materias de programación.
Calcular un intervalo de confianza del 95% para la proporción
poblacional (π) de estudiantes que asiste todas las semanas al cine.

<!-- página 19 -->

Resolución
Datos:
0.80 − 1,96 0.80 . 0.20
300 < ππ < 0.80 + 1,96 0.80 . 0.20
300
0,755 < ππ <0,845
< ππ < 0.027
Reemplazamos los datos en la fórmula:
Resultado: IC 99% para ππ =  (0.755 ; 0.845)
Se tiene un 95% de confianza de que la verdadera proporción de estudiantes que cuentan con
una comptadora portátil propia s encuentra entre 0.755y 0.845 microsegundos.
nn = 300 μpp = 0,80 �qq = 1 − 0,80 = 0,20
Nivel de confianza = 95%  →  αα = 0,05 →  zzαα/2 = 1,96
