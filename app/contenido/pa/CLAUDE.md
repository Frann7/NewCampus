# Programación Avanzada (PA) — cómo se escribe su contenido

Las reglas generales están en `docs/contenido.md` (raíz del repo); acá va solo lo propio de PA.
PA no tiene unidades sino **clases** (`c1`..`c6` en `materias.json`, "Clase N" en el menú).

## Fuentes y alcance

- **Alcance:** cada clase sale **solo del material de esa clase**:
  `C:\Users\Fran\Desktop\SISTEMAS 3\PA\CLASE N\` (TEORIA, PRACTICA y sus zips). El examen es
  `PA\Parcial PHP.pdf` (20 preguntas del Aula Virtual). El TP (`PA\TP\`, `TP_Centro_*`) no entra.
- **Texto extraído:** cada PDF está en texto en `fuentes/pa/` (raíz del repo), con la misma ruta y
  `.md`; `fuentes/pa/INDICE.md` dice qué es cada uno. **Primero el texto extraído; el PDF solo en
  las páginas marcadas ⚠ o si algo no cierra** (`python fuentes/pagina.py "<PDF>" N` y Read del PNG).
  Los zips se leen con `unzip -p` (son ejemplos de código chicos).
- **Datos de otras personas, nunca al repo:** `PA\ExamenPA-2026.pdf` es la lista de alumnos (está
  en `fuentes/pa/excluir.txt`), `PA\REPO actividad aulica\` tiene archivos con DNI.

## Cómo se escribe

- **Teoría, cada sección:** Para qué sirve → Sintaxis → Qué es cada parte (tabla) → Ejemplos →
  Errores y trampas (`.caja.caja-ojo`). Teoría corta y simple; el detalle va en los ejemplos.
  Mínimo 2 ejemplos por apartado, uno simple y uno con formato del Parcial PHP ("¿cuál es la
  salida?", "¿qué valores...?").
- **En cada ejemplo con código:** el código, después **qué hace cada línea** (tabla Línea / Qué
  hace / Cómo quedan las variables) y al final **qué imprime y por qué**. Nunca resumir pasos.
- **Toda salida se verifica corriendo el código** con `C:\xampp\php\php.exe` (archivo temporal en
  el scratchpad) antes de escribirla. Lo que dependa de la fecha o del entorno se aclara.
- **Código en el HTML:** bloques en `<pre class="codigo"><code>...</code></pre>`, lo que imprime en
  `<pre class="salida">...</pre>`, y en el texto `<code>...</code>`. Dentro del código, `<` va como
  `&lt;`, `>` como `&gt;` y `&` como `&amp;` (`<?php` se escribe `&lt;?php`). El `$` va tal cual
  (MathJax solo mira `\( \)` y `\[ \]`); no escribir `\(` dentro de código.
- **Marcas de examen:** ★ (`data-examen="igual"`, `data-examen-ref="Parcial PHP · preg. N"`) en lo
  que tomó el Parcial PHP. ◈ queda para lo que solo tome el examen teórico, cuando se cargue.
- `00-intro.html` de cada clase: título, bajada y "Cómo leer esta clase" (`data-abierta`): qué
  tomó el parcial de esta clase y en qué orden leer.
- Términos en inglés de la cátedra (array, string, request) se usan tal cual y se explican la
  primera vez.

## Evaluación

- Parcial transcripto y resuelto en `evaluacion/parciales/parcial-php/` (un archivo por pregunta,
  con `pd-resultados` y `pd-explicacion`).
- Banco: `evaluacion/preguntas/parcial-php/`, las 20 preguntas del parcial en el formato de la 1ra
  etapa (`preguntas/FORMATO.md` de PyE), ids `pa-php-01`..`pa-php-20` en el orden del parcial.
  **No se inventan preguntas de más.**
- La autoevaluación de PA es simple: se crea como en PyE, pero sin etapas, modo interactivo,
  estilos ni elegir clases; corre las 20 en orden, formato Aula Virtual, con reloj (40 min por
  defecto), nota sobre 100 y revisión con explicación.

## Pendientes e ideas

- El examen teórico (`PA\Examen Teórico 2025.pdf`) en Evaluación.
