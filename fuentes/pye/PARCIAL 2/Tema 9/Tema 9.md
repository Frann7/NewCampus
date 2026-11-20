# Tema 9

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 2/Tema 9/Tema 9.pdf` · 16 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Portada: temas (hipótesis estadística, H0 y H1, estadístico, pasos, errores tipo I y II); Walpole cap. 10 |
| 2 | Qué es una hipótesis estadística; H0 = valor exacto del parámetro, H1 = rango que lo excluye; nunca hay certeza |
| 3 | ⚠ ver el PDF · diagrama del procedimiento: muestra (evidencia) → consistente con H0 (no hay evidencia para rechazar) o inconsistente (conclusión firme) |
| 4 | Analogía con la ley penal; resultados posibles a) y b); no rechazar no es aceptar H0 |
| 5 | El estadístico de una prueba: se elige el de menor varianza (media mejor que mediana) |
| 6 | ⚠ ver el PDF · eficiencia de estimadores (dibujo de dos distribuciones muestrales; el texto sale roto) |
| 7 | Los seis pasos del test; paso 1: H0 como igualdad (μ = 20 mg) |
| 8 | Paso 2: las tres H1 (<, >, ≠); paso 3: α = riesgo de rechazar H0 cierta, habitual 5 % |
| 9 | ⚠ ver el PDF · paso 4: regiones críticas, tres campanas t (±tα/2, tα, −tα) para cada H1 |
| 10 | Paso 5: estadístico T = (x̄ − μ)/(S/√n) ~ t; el de dos poblaciones (μ1 − μ2) con la fórmula rota ⚠ |
| 11 | ⚠ ver el PDF · paso 6: comparar y decidir; tres campanas con T adentro o afuera de la región |
| 12 | Errores tipo I (P = α, solo si se rechaza) y tipo II (P = β, depende del valor real del parámetro) |
| 13 | ⚠ ver el PDF · dibujo de α y β: curva de H0 (μ = 20) y curva real (μ = 15), β(15) rayado |
| 14 | Cuadro de decisiones y errores; Ejemplo 1: peso medio 68 kg, n = 36, x̄ = 70, S = 3,6 (Z aunque σ desconocida) |
| 15 | Ejemplo 1: H0 μ = 68, H1 μ ≠ 68, α = 0,05, críticos ±1,96 |
| 16 | ⚠ ver el PDF · Ejemplo 1: Z = 2/0,6 = 3,3̂ (lo llama T), campana con T afuera; se rechaza, error tipo I del 5 % |

<!-- página 1 -->

Se presentan los formalismos para formular tests de hipótesis
referidos a procedimientos de decisión que se basan en los datos y
que pueden producir una conclusión acerca de algún sistema
científico.
W – Cap 10
● Hipótesis estadística.
● La Hipótesis Nula y la Hipótesis Alternativa.
● El Estadístico de una prueba.
● Pasos para realizar un test de Hipótesis.
● Errores de tipo I y II. α , β y n en la probabilidad de errores Tipo I y II.

<!-- página 2 -->

Hipótesis Estadística
Se debe formular la Hipótesis indicando específicamente el valor que toma el
parámetro. A esta afirmación se la denomina Hipótesis Nula.
Hipótesis Nula  H0: Valor exacto del parámetro.

Hipótesis Alternativa: H1: Rango de valores alternativos
que excluyen al valor planteado en la H0.
El resultado de la Hipótesis Estadística planteada puede ser que no exista
evidencia en la muestra utilizada para rechazar la H0 o que exista fuerte
evidencia para rechazarla.
Es la afirmación que se realiza acerca de un parámetro estadístico
de la población:

Media
Rango
Desvío
…

La verdad o falsedad nunca se sabe con absoluta certeza sino que se utilizan
NIVELES DE CONFIANZA ya que no se examina a toda la población.

<!-- página 3 -->

Procedimiento:
Se toma una Muestra Aleatoria → (EVIDENCIA)
Se plantea la H0 y la H1
Consistente con H0 Inconsistente con H0
No hay evidencia para rechazar H0 Existe fuerte evidencia de la inconsistencia
 de H0 (CONCLUSIÓN FIRME)
Es mejor llegar a una conclusión firme rechazando una H0 que indicar que no
hay evidencia para rechazarla.

<!-- página 4 -->

Es muy parecido a la Ley PENAL: El acusado es inocente hasta que no se
demuestre lo contrario.
Resultados posibles del test de Hipótesis:

a) La evidencia actual (muestra) es contundente para el rechazo de H0.

b) La evidencia actual (muestra) no alcanza para rechazar H0 pero es
posible que con más evidencia alcance para rechazarla.
Esto es porque la evidencia es una muestra de la población que la representa con
un NIVEL DE CONFIANZA menor al 100%.
Observe que en el caso (b) las conclusiones no implican una
“aceptación de H0” formal y literal.

<!-- página 5 -->

Habíamos visto en el tema anterior que para seleccionar un
estadístico deberíamos prestar atención al que tenga menor
varianza. Así, para estimar la media poblacional  μ se elige como
estadístico a la media muestral X en lugar de la mediana
muestral X  porque σX
2 < σX
2.
La prueba de hipótesis se basa en construir, a partir de la muestra
aleatoria, un estadístico y según el valor que tome este estadístico de
prueba se aceptará o se rechazará la hipótesis.
Llamemos θ  al estadístico de la muestra y θ al parámetro poblacional a estimar.
El estadístico de una prueba

<!-- página 6 -->

Varianza de un Estimador puntual (Estadístico del Test de Hipótesis):
Si θ 1 y θ 2 son dos estimadores insesgados del parámetro poblacional θ
elegimos el estimador cuya distribución muestral tenga menor varianza.
σθ 1 < σθ 2 θ 1 es un estimador más eficiente de θ  que θ 2
xa xb xc xj xb  xa  xc
σx < σx
2 2
2 2
Entonces, x es mejor estimador de μ que x

<!-- página 7 -->

Una vez elegido el estadístico de la muestra que representa mejor la población
se realiza el Test de Hipótesis con un procedimiento que contempla los
siguientes pasos:
Pasos para realizar un test de hipótesis
1. Establecer H0
2. Establecer H1
3. Fijar el nivel de significancia α.
4. Obtener regiones críticas.
5. Calcular el estadístico.
6. Comparar y decidir NO RECHAZAR H0 ó RECHAZAR H0 (que implica ACEPTAR H1).
1. Establecer H0 implica indicar un valor exacto que toma el parámetro poblacional
a estimar:

      H0:  μ = 20 mg (p. ejemplo).

      Es decir, la H0 se plantea como una igualdad para ser probada por el test.

<!-- página 8 -->

2. Establecer H1 implica indicar un intervalo que toma el parámetro poblacional a
estimar y que excluye al valor planteado en H0. El planteo de H1 puede ser
alguno de los siguientes:

      H1 < 20 mg. (caso de intervalo inferior al valor planteado en H0).

      H1 > 20 mg. (caso de intervalo superior al valor planteado en H0).

      H1 ≠ 20 mg. (caso de intervalo diferente al valor planteado en H0).

      Es decir, la H1 se plantea como un intervalo de valores que excluyan al valor
      exacto planteado en H0 utilizando alguna de las tres alternativas.
3. Fijar el nivel de significancia α implica elegir el porcentaje de casos en los cuales
el rechazo de la H0 es erróneo, es decir el riesgo que corremos al rechazar una
hipótesis nula cuando es cierta. Cuanto más alto sea el nivel de significancia que
utilizamos para probar una hipótesis, mayor será la probabilidad de rechazar la
hipótesis nula cuando es cierta. En la mayoría de los test de hipótesis se utiliza
un α = 5% pero puede elegirse cualquier valor para el nivel de significancia.

<!-- página 9 -->

4. Obtener las Regiones Críticas: Implica elegir los valores umbrales para no
rechazar o rechazar H0 según la distribución teórica de la variable aleatoria.
        Al elegir estos valores umbrales se delimitan las regiones críticas de rechazo de
       H0 (o aceptación de H1) según se haya planteado la hipótesis alternativa H1.
H1:   μ ≠   20 mg
H1:   μ >   20 mg H1:   μ <   20 mg
Se observa que
este paso está
estrechamente
ligado al anterior.
H0:  μ = 20 mg

<!-- página 10 -->

5. Calcular el estadístico: Implica el cálculo del valor del estadístico de la prueba
utilizando los datos muestrales.

        Por ejemplo, en el caso de la distribución t de la variable aleatoria se calcula el
        estadístico T para ser comparado con los valores críticos de la distribución.
T = x − μ
S
n
      →        ~t(0, ν)
El cálculo de estadístico se realiza según la distribución de la variable  aleatoria
por un lado y de la H0 que se plantee. Esta última se refiere a si se está
interesado en la prueba de una población o de la comparación de dos
poblaciones, por ejemplo en este último caso el estadístico T se calcula como:
T = x1 − x2 − μ1 − μ2
1
n1
S1 + 1
n2
S2

<!-- página 11 -->

6. Comparar y decidir. Aquí, en este último paso se decide por alguna de las dos
opciones siguientes:

         a) RECHAZAR H0.

         b) NO RECHAZAR H0.
T
T T
Caso de rechazo de H0 con
H1:   μ ≠   20 mg
Ejemplos
Caso de no rechazo de H0 con
H1:   μ <   20 mg
Caso de rechazo de H0 con
H1:   μ >   20 mg
H0:  μ = 20 mg

<!-- página 12 -->

Errores Tipo I y II
Error Tipo I: Es el error que se comente al rechazar una H0 cuando en realidad es
verdadera. Este error está ligado a la elección del nivel de significancia α.
P ET I = α
Este error puede cometerse sólo en el caso de haber rechazado H0
Error Tipo II: Es el error que se comente al no rechazar una H0 cuando en
realidad es falsa porque el parámetro poblacional es diferente, mayor o menor
al que se estableció en H0. Este error está ligado a la propuesta de elección del
valor del parámetro poblacional distinto del que se planteó H0 ya que puede
calcularse así una probabilidad β que corresponde al Error Tipo II.
P ET II = β

<!-- página 13 -->

En nuestro ejemplo de la distribución t de Student:
T
Caso de rechazo de H0 con
H1:   μ ≠   20 mg
T Caso de rechazo de H0 con
H1:   μ >   20 mg
T
Caso de no rechazo de H0 con
H1:   μ <   20 mg
P ET I = α
P ET I = α
μ = 20
μ = 20 μ = 20 μ = 15
H0:  μ = 20 mg
β
P ET II = β(15)

<!-- página 14 -->

En definitiva, los casos posibles de cometer errores al no rechazar o rechazar
H0 se pueden resumir en la siguiente tabla:
H0 es verdadera H0 es falsa
No rechazar H0 Decisión correcta Error Tipo II
Rechazar H0  Error Tipo I Decisión correcta
Ejemplo 1: El peso medio de las personas de una provincia es de 68 Kg. Se toma una
muestra de 36 individuos obteniendo:
x = 70 Kg
S = 3,6 Kg
¿Se puede afirmar que el peso medio se mantiene?
¿Qué tipo de error puede cometerse y cuál es el valor del mismo?
Solución:

Como el número de individuos es mayor a 30 se utilizará la distribución normal aunque
σ sea desconocida.

<!-- página 15 -->

1. Establecer H0:
H0:  μ = 68 Kg

2. Establecer H1:
H1:  μ ≠ 68 Kg

3. Fijar el nivel de significancia α:
α = 0,05

4. Obtener regiones críticas:
−Zα 2 = −Z0,025 = −1,96 Zα 2 = Z0,025 = 1,96

<!-- página 16 -->

5. Calcular el estadístico.
Z = x − μ
S
n
= 70 − 68
3,6
36
= 2
0,6 = 3, 3
6. Comparar y decidir.
−Zα 2 = −1,96 Zα 2 = 1,96 Z = 0 T = 3, 3
Como T > Zα 2  se rechaza H0 con un nivel de significancia de α = 5%
Al rechazar la H0:  μ = 68 Kg  puede cometerse ERROR Tipo I del 5%
