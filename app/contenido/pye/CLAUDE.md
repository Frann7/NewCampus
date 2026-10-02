# Probabilidad y Estadística (PyE) — cómo se escribe su contenido

Las reglas generales de teoría y práctica están en `docs/contenido.md` (raíz del repo); acá va
solo lo propio de PyE. Si se toca el banco de preguntas: `evaluacion/preguntas/FORMATO.md` y
`docs/evaluacion.md`.

## Fuentes y alcance

- **Alcance:** cada unidad sale **solo de los PDF de esa unidad**:
  `C:\Users\Fran\Desktop\SISTEMAS 3\PYE\PARCIAL 2\UNIDAD N\`. La prueba de hipótesis es U8/9, no
  U7. Otros materiales: `PYE\PARCIAL 2\guia_integradoras_parcial_2.pdf`, `Respuestas.pdf`,
  `Guia_distribucion_t_Student_yRtas.pdf`, `Parcial 2 2025.jpg`, y finales en `PYE\PARCIALES\`.
- **Texto extraído:** cada PDF está en texto en `fuentes/pye/` (raíz del repo), con la misma ruta
  que en `SISTEMAS 3\PYE\` y `.md` en vez de `.pdf`; `fuentes/pye/INDICE.md` dice qué es cada uno.
  **Primero el texto extraído** (con la tabla de arriba de cada `.md` o Grep, se lee solo el rango
  de `<!-- página N -->` que hace falta); **el PDF solo en las páginas marcadas ⚠ o si algo no
  cierra**. Las imágenes (`Parcial 2 2025.jpg` y las de PARCIAL 1) no tienen texto: se miran.
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

- Sumar preguntas urgentes de **exponencial** a la 1ra instancia (la profe confirmó que entra).
- Ofrecido: que el paso de "a lo sumo 2" del fundamental de Poisson enseñe a usar la tabla
  acumulada directo.
- Datos raros señalados en el banco: `u4-e-final-2025-12-10-ej2` (Cov/V inconsistentes con la
  densidad), `u7-e-final-2026-07-29-ej2` (μ = 355 dado y estimado a la vez).
