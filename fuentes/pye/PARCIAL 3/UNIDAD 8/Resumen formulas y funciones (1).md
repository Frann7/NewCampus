# Resumen formulas y funciones (1)

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 3/UNIDAD 8/Resumen formulas y funciones (1).pdf` · 3 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |

<!-- página 1 -->

      Probabilidad y Estadística – Licenciatura en Sistemas de Información
Probabilidad y Estadística – Licenciatura en Sistemas de Información

ESTIMACIÓN DE LA MEDIA POBLACIONAL μ

EN R STUDIO:  se puede hacer directamente con la función t.test(…)$conf.int siempre que contemos
con las observaciones de la muestra cargadas en un vector x.
t.test(x,conf.level = 0.99)$conf.int
ESTIMACIÓN DE LA DIFERENCIA DE MEDIAS DE DOS POBLACIONES μ1 − μ2

EN R STUDIO:  se puede hacer directamente con la función t.test(…)$conf.int siempre que contemos
con las observaciones de las muestras cargadas en dos vectores x1 y x2, por ejemplo. Se fija
“var.equal=TRUE” si las varianzas poblacionales son IGUALES o “var.equal=FALSE” si son diferentes.
t.test(x1,x2, var.equal=FALSE, conf.level = 0.90)$conf.int

Tema 8: Estimación de Parámetros
Síntesis de fórmulas y funciones en R Studio

<!-- página 2 -->

      Probabilidad y Estadística – Licenciatura en Sistemas de Información
Probabilidad y Estadística – Licenciatura en Sistemas de Información

ESTIMACIÓN DEL COCIENTE DE VARIANZAS
σ1
2
σ2
2 DE DOS POBLACIONES

EN R STUDIO:  se puede hacer directamente con la función var.test(…)$conf.int  siempre que
contemos con las observaciones de las muestras cargadas en dos vectores x1 y x2, por ejemplo.
var.test(x1, x2, conf.level = 0.94)$conf.int

OBSERVACIÓN : si se tiene que hacer un IC para diferencia de medias y no se sabe nada acerca de las
varianzas poblacionales, los pasos a seguir son:

ESTIMACIÓN DE UNA VARIANZA σଶ DE UNA POBLACIÓN

EN R STUDIO :  Aplicamos la fórmula ingresando el ALFA/2 que corresponde.
(n-1)*var(x)/qchisq(0.025,df=4,lower.tail=FALSE)
(n-1)*var(x)/qchisq(0.025,df=4,lower.tail=TRUE)
¿LAS VARIANZAS
SON IGUALES?
Se cargan
los datos
• ¿1 pertenece al
intervalo?
• Sí: Son IGUALES
• No: Son diferentes
IC para
VARIANZAS
•var.equal=TRUE
•var.equal=FALSE
IC para
DIFERENCIA
DE MEDIAS
Estimación por intervalo del (1 − α). 100% de confianza:
s1
2
s2
2
1
fα
2
(ν1,ν2) < σ1
2
σ2
2 <
s1
2
s2
2 fα
2
(ν2, ν1)
1 ε IC
Varianzas IGUALES
1 ∉  IC
Varianzas DISTINTAS
1 ∉  IC
Varianzas DISTINTAS
t.test(x1,x2, var.equal=…, conf.level = 0.90)$conf.int  var.test(x1,x2, conf.level = 0.90)$conf.int
CONCLUIR

<!-- página 3 -->

      Probabilidad y Estadística – Licenciatura en Sistemas de Información
Probabilidad y Estadística – Licenciatura en Sistemas de Información

ESTIMACIÓN DE LA PROPORCIÓN DE ÉXITOS POBLACIONAL P
p̂ ± zഀ
మ
. ට௣ො.௤ො
௡               siendo p̂ =
௫
௡      qො = 1 −p̂
EN R STUDIO:  se puede hacer directamente con la función prop.test(…)$conf.int  para lo cual
necesitamos x (nro. éxitos en muestra) y n (tamaño de la muestra).
prop.test(x=, n=, conf.level=0.95)

ESTIMACIÓN DE LA DIFERENCIA DE PROPORCIONES DE DOS POBLACIONES p1 − p2

EN R STUDIO:  se puede hacer directamente con la función prop.test(…)$conf.int  para lo cual
necesitamos x1 (nro. éxitos en muestra 1), x2 (nro. éxitos en muestra 2), n1 (tamaño de muestra 1)
y n2 (tamaño de muestra 2).
prop.test(x=c(x1, x2), n=c(n1, n2), conf.level=0.95)
