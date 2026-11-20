# Probabilidad y Estadística (PyE) — cómo se escribe su contenido

Las reglas generales de teoría y práctica están en `docs/contenido.md` (raíz del repo); acá va
solo lo propio de PyE. Si se toca el banco de preguntas: `evaluacion/preguntas/FORMATO.md` y
`docs/evaluacion.md`.

## Fuentes y alcance

- **Alcance:** cada unidad sale **solo de los PDF de esa unidad**:
  `C:\Users\Fran\Desktop\SISTEMAS 3\PYE\PARCIAL 2\UNIDAD N\` (U1 a U3: `PARCIAL 1\UNIDAD N\`, más
  la hoja de fórmulas de descriptiva e integrales, `app/pdf/pye/formulas-descriptiva-e-integrales.pdf`).
  La prueba de hipótesis no es U7.
- **U9 (Prueba de hipótesis, para el final):** fuente `PARCIAL 2\Tema 9\` (Tema 9, la guía y su
  resolución en R). H₀ con "=" como la resolución de la cátedra; Z o t con la misma regla que el IC.
  El Tema 9 no explica el valor p: la sección sale de los finales y de la guía de la t. El cálculo
  de β y la prueba para dos poblaciones solo se nombran (no aparecieron en finales).
- **1er parcial (U1 a U3):** cuartiles con la convención de la hoja de fórmulas (n par: promedio de
  las posiciones \(\frac{k}{4}n\) y \(\frac{k}{4}n+1\); coincide con los Resultados). Atípicos con las
  vallas \(Q_1 - 1{,}5\,IQ\) y \(Q_3 + 1{,}5\,IQ\).
- **3er parcial (U8, Estimación):** la profe dijo (2026) que entran **solo** `PARCIAL 3\UNIDAD 8\
  Estimacion_Parte 1.pdf` y `Estimacion_Parte 2.pdf`: IC para μ (con error y tamaño de muestra),
  para una proporción π y para μ₁ − μ₂ (Z, pooled y Welch). De la guía entran 1 a 15, 20 y 21; no
  entran 16 a 19 (F y chi cuadrado; la pregunta "¿varianzas iguales?" del 16 y el 17 se contesta con
  la regla práctica S²mayor/S²menor ≤ 3, lo confirmó la profe el 01/11/2026) ni 22 a 24 (diferencia
  de proporciones). Tampoco prueba de hipótesis (el ej. 2 y el 1b-1c del Parcial 3 2025) ni "decidir
  si un valor es aceptable" con el IC. El 10 y el 11 los tacharon los compañeros en el Miro por la
  Resolución 2023, pero están en el diagrama de la profe: entran. Regla de Z o t: σ conocida → Z con cualquier n;
  σ desconocida: n ≥ 30 → Z con S, n < 30 → t (ν = n − 1). Lo corrigió Fran el 04/11/2026 con el diagrama
  de la parte 2 y el Tema 8 Parte A (antes estaba "n < 30 → t aunque den σ": era un error). En diferencia de
  medias, igual: σ₁ y σ₂ conocidas → Z. Las preguntas del banco `u8` llevan
  `data-origen="parcial"` aunque el tema no se haya tomado (es para el 3er parcial).
- Otros materiales del 2do parcial: `PYE\PARCIAL 2\guia_integradoras_parcial_2.pdf`, `Respuestas.pdf`,
  `Guia_distribucion_t_Student_yRtas.pdf`, `Parcial 2 2025.jpg`, y finales en `PYE\PARCIALES\`.
- **Texto extraído:** cada PDF está en texto en `fuentes/pye/` (raíz del repo), con la misma ruta
  que en `SISTEMAS 3\PYE\` y `.md` en vez de `.pdf`; `fuentes/pye/INDICE.md` dice qué es cada uno.
  **Primero el texto extraído** (con la tabla de arriba de cada `.md` o Grep, se lee solo el rango
  de `<!-- página N -->` que hace falta); **el PDF solo en las páginas marcadas ⚠ o si algo no
  cierra**. Las imágenes (`Parcial 2 2025.jpg`, `PARCIAL 3\Parcial 3 2025.jpg` y las de PARCIAL 1)
  no tienen texto: se miran.
- **Distribuciones que entran** (dicho por la profe, 30/09/2026): discretas uniforme, binomial,
  binomial negativa, Poisson, geométrica, hipergeométrica; continuas uniforme, normal,
  t de Student, exponencial.

## Cómo se escribe

- **Estructura de cada sección (modelo: la U5):** Cuándo se usa → Fórmulas → Qué significa cada
  letra (tabla) → De dónde sale → Ejemplos. En cada ejemplo, "Desarme del enunciado" (Frase /
  Traducción / Cuenta / A dónde va) y **cada paso explicado**: qué se hace, por qué y qué significa
  el resultado. Teoría general corta y simple; el detalle va en los ejemplos. Nunca resumir pasos.
- **Fórmula repetida** en cada inciso antes de reemplazar los números. Nada se usa sin explicarlo
  antes en general. Ejemplos **autocontenidos** (repiten la tabla y los datos; nunca "la tabla de la
  sección 5"). Mínimo 2 ejemplos por apartado, contextos de sistemas como el Parcial 2025.
- **Números verificados** (con Python) y contra los "Resultados" de la cátedra. Ojo:
  `Respuestas.pdf` usa z sin redondear; la app usa z con 2 decimales y F(z) de tabla con 4.
- **Notación de la cátedra:** X ~ N(μ; σ) **con el desvío**; b(x; n, p); P(x; λt); H(x; N, n, k);
  t con ν = n − 1. En la hoja se arranca: "X: ... → v.a. discreta/continua · X ~ ...".
- **Marcas de examen:** ★ dorado solo si lo tomaron en un **parcial**; ◈ violeta si solo en finales.
- **Gráficos** (U6): SVG generado por script (no a ojo), para entender; nunca exigir "graficá
  siempre": la cátedra resuelve con cuentas.
- Decimales con coma; en LaTeX `{,}`. MathJax con `\( \)` y `\[ \]`, nunca `$`.

## Pendientes e ideas

- **Paso a paso en todos los gráficos y búsquedas en tabla** (pedido de Fran, 20/11/2026; regla en
  `docs/contenido.md`). Hechos los 4 finales (modelo: Final 29/07/2026, ej. 1 b; cada final tiene
  su `fuentes/pye/graficos_final_*.py`). Falta el resto: Parciales, Práctica y Teoría de U1 a U9
  (~140 gráficos y las lecturas de tabla Z/t/binomial).

- Banco de autoevaluación de U1 a U3 (no está hecho). La práctica de U2 no tiene marcas de examen.
- Interpretaciones sin resultado oficial, a confirmar con Fran: Parcial 1 2025 ej. 3e ("entre 629 y
  697" con extremos, 60 %; sin ellos, 50 %); U1 guía ej. 14b ("al menos uno disponible") y 15a; el
  criterio del CV (15 % y 30 %) para baja/moderada/alta variabilidad.

- Sumar preguntas urgentes de **exponencial** a la 1ra instancia (la profe confirmó que entra).
- Ofrecido: que el paso de "a lo sumo 2" del fundamental de Poisson enseñe a usar la tabla
  acumulada directo.
- Datos raros señalados en el banco: `u4-e-final-2025-12-10-ej2` (Cov/V inconsistentes con la
  densidad), `u7-e-final-2026-07-29-ej2` (μ = 355 dado y estimado a la vez).
