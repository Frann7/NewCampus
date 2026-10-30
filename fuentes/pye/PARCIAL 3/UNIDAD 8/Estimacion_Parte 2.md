# Estimacion_Parte 2

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 3/UNIDAD 8/Estimacion_Parte 2.pdf` · 15 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Portada |
| 2 | Diferencia de medias, muestras independientes |
| 3 | Diagrama de decisión (Z, pooled, Welch) |
| 4 | Regla empírica S²mayor/S²menor ≤ 3 |
| 5 | ⚠ ver el PDF: caso Z con muestras grandes (fórmula imagen) |
| 6 | ⚠ ver el PDF: caso pooled (fórmulas imagen) |
| 7 | ⚠ ver el PDF: caso Welch y ν (fórmulas imagen) |
| 8 | Ejemplo 4 (carbono) |
| 9 | ⚠ ver el PDF: resolución del Ejemplo 4 (resta SM − PCH) |
| 10 | Conclusión del Ejemplo 4 |
| 11 | Ejemplo 5 (sedimentos, datos sueltos) |
| 12 | Regla empírica del Ejemplo 5 (6,12 &gt; 3) |
| 13 | ν y el IC del Ejemplo 5 |
| 14 | Conclusión del Ejemplo 5 (incluye el 0) |
| 15 | ⚠ ver el PDF: ejercicio sin resolver (SQL vs NoSQL, pooled) |

<!-- página 1 -->

PROBABILIDAD Y ESTADÍSTICA
Estimación – Segunda Parte
Licenciatura en Sistemas

<!-- página 2 -->

Diferencia de medias
Muestras independientes

<!-- página 3 -->

Diagrama de decisión
¿Son conocidas las
varianzas σ₁², σ₂²?
NO
(varianzas desconocidas)
Varianzas
Supuestas iguales
(S²mayor/S²menor ≤ 3)
Poblaciones independientes
con X1 y X2 con distrib. normal y
n1 y n2 <30
→ s2-pooled (s2
p)
(n₁+n₂−2 gl)
Varianzas
No supuestas iguales
(S²mayor/S²menor > 3)
Poblaciones independientes
con X1 y X2 con distrib.
normal y n1 y n2 <30
→ t-t-Welch
(ν gl aprox.)
X1 y X2 con distrib normal,
independientes y muestras
grandes (n₁, n₂ ≥ 30)
→ Z con S₁², S₂²
SI → usar σ₁², σ₂²
directamente (Z)

<!-- página 4 -->

Regla empírica
mmmmmmmmmm SS2
mmmmmmmmmm SS2 > 3
mmmmmmmmmm SS2
mmmmmmmmmm SS2 < 3
Varianzas no
supuestas iguales
Varianzas
supuestas iguales
Vamos a utilizar una regla empírica para decidir si
es posible suponer varianzas poblacionales iguales:

<!-- página 5 -->

Estimación de la diferencia de medias poblacionales
Varianzas desconocidas (Muestras grandes)
Condiciones:
✔ Muestras independientes
✔ n₁ ≥ 30  y  n₂ ≥ 30
✔ Varianzas desconocidas
✔ Se reemplazan σᵢ² por Sᵢ²
z_{α/2}: valor z que deja área α/2 a la derecha
Nota: Por el TeoremaCentral del Límite, con muestras grandes la distribución de (x̄₁ − x̄₂) es aproximadamente
normal independientemente de la distribución poblacional. Esto justifica el uso del valor z.
Si �XX1 y �XX2 son las medias de muestras aleatorias independientes de tamaño n₁ y n₂
de poblaciones con varianzas conocidas S₁² y S₂² respectivamente, un intervalo de
confianza de (1-α).100% para μ₁ - μ₂ está dado por:
Donde zα/2 es el valor z que deja un área
de α/2 a la derecha

<!-- página 6 -->

Estimación de la diferencia de medias poblacionales
Varianzas desconocidas, supuestas iguales (Muestras chicas)
La varianza "pooled" se define:
Si �XX1 y �XX2 son las medias de muestras aleatorias independientes de tamaño n₁ y n₂ de poblaciones
aproximadamente normales con varianzas iguales pero desconocidas, el intervalo de confianza de (1-
α).100% para μ₁ - μ₂ está dado por:
donde Sp es la estimación ¨pooled¨ de la desviación
estándar poblacional y t(α/2; ν) es el valor t con (n1+n2 –2)
grados de libertad, que deja un área de α/2 a la derecha.
Nota: Cuando se acepta la suposición que las dos varianzas poblacionales son iguales (y para
este caso en el que la variable se distribuye normal en ambas poblaciones) el estimador de la
diferencia de medias poblacionales se distribuye T-Student con n1+n2-2 grados de libertad; α/2
y con variancia conjunta Sp2.

<!-- página 7 -->

Estimación de la diferencia de medias poblacionales
Varianzas desconocidas, no supuestas iguales (Muestras
chicas)
Estimación de los grados de libertad para la t
(Welch-Satterthwaite)
Si �XX1 y �XX2 son las medias de muestras aleatorias independientes de tamaño n₁ y n₂
de poblaciones aproximadamente normales con varianzas desconocidas y
diferentes, el intervalo de confianza de (1-α) 100% para μ₁ - μ₂ está dado por:
Nota: ν generalmente no es un entero — se redondea al entero más cercano
(truncar hacia abajo es el criterio más conservador).

<!-- página 8 -->

Ejemplo 4 — Emisiones de carbono total
En una investigación sobre las emisiones de carbono a la atmósfera producto de
incendios forestales, se determinó el carbono total (en tn/ha) liberado por
incendios en la región del Parque Chaqueño y en la Selva Misionera durante el
año 2008.
En la primera región, la determinación sobre 26 incendios proporcionaron un valor
promedio de ̅xx1 = 110,45 tn/ha y una varianza de S₁² = 63 (tn/ha)².
En la segunda región se evaluaron 16 incendios y los valores encontrados para la
media y la varianza fueron de ̅xx2= 229,51 tn/ha y S₂² = 48 (tn/ha)² respectivamente.
Suponiendo que la variable contenido de carbono se distribuye normalmente, se
desea construir un intervalo de confianza del 95% para la diferencia de medias
poblacionales μ₁ - μ₂.

<!-- página 9 -->

Resolución
Medida Parque chaqueño Selva misionera
n 26 16
x̄ (tn/ha) 110,45 229,51
s2 (tn/ha) 63 48
Datos del
problema:
IC 95%: (114.19 ; 123.93)

<!-- página 10 -->

Resolución
Observar que el intervalo de confianza del 95% no incluye al cero, entonces
para este nivel de confianza puede concluirse que existe diferencia significativa
entre las medias.
Se estima que la diferencia entre las emisiones medias de carbono
liberadas a la atmósfera por ambas regiones es de (114.19 ; 123.93)
tn/ha, siendo significativamente mayor la emisión media en la
Selva Misionera.
IC 95%: (114.19 ; 123.93)

<!-- página 11 -->

Ejemplo 5 — Sedimentos en dos lugares
En un estudio realizado sobre el tipo de sedimentos hallados en dos lugares de perforación distintos,
se han anotado los siguientes datos acerca del porcentaje en volumen de arcilla presente en las
muestras de sondeo:
Lugar 1: 31 18 17 16 37 16 32 13 14 49 25 19 13 32 27
Lugar 2: 15 17 13 25 22 22 20 24 12 23 15 20 18
Calcular un IC del 95% para la diferencia media poblacional de los lugares 1 y 2.

<!-- página 12 -->

Resolución
Regla empírica:
10.562
4,272 = 6.12 > 3
Resumen numérico
usando R:
Varianzas poblacionales no supuestas
iguales

<!-- página 13 -->

Resolución
==
10.562
15 + 4.272
13
2
10.562
15
2
15 − 1 +
4.272
13
2
13 − 1
= 8.842
3.94 + 0.16 = 19.06
Grados de libertad:
tt: αα = 0.05
αα
2 = 0.025 tt0.025 ;19 = 2.093
Intervalo de confianza:
LI:    23.93 − 18.92 − 2.093 .
10.562
15 +
4.272
13 = 5.01 − 6.22 = −1.21
LS: 23.93 − 18.92 + 2.093 .
10.562
15 +
4.272
13 = 5.01 + 6.22 = 11.23

<!-- página 14 -->

Resolución
Solución usando R:
función: t.test
Dado que el intervalo de confianza incluye el valor cero, no es posible afirmar que existe una
diferencia estadísticamente significativa entre las medias poblacionales entre los porcentajes de
sedimento en ambos lugares
Conclusión:
IC 95%: (-1.21 ; 11.23)

<!-- página 15 -->


