# Sistemas Operativos — Teoría (so-teoria) — cómo se escribe su contenido

Las reglas generales están en `docs/contenido.md` (raíz del repo); acá va solo lo propio de SO Teoría.

## Qué hay

- **Solo Evaluación**, igual que SO Práctica: sin unidades en `materias.json`, con
  `"evaluacion": { "tipo": "simple" }`.
- **Parciales** (`evaluacion/parciales/`), uno por pregunta (`NN-pregunta-NN.html`):
  - `2025-segundo-parcial`: 55 preguntas V/F y opción única, de 1 o 2 puntos (100 en total), de
    `cmps\2do parcial teorico (1).pdf` (capturas de la revisión de un intento, sin texto: se leyó
    pasando las páginas a imagen). Las respuestas son las que el Aula Virtual da como correctas;
    en las 22, 28 y 50 se cita la devolución del Aula Virtual. Las explicaciones citan Tanenbaum
    (*Sistemas operativos modernos*) y Stallings (*Sistemas operativos*), de donde salen los
    textos, sin número de página.
  - `2026-segundo-parcial`: el parcial en papel del 2/11/2026 (27 preguntas, +1/−1), de dos fotos.
    Casi todas repiten el 2025: se armaron copiando esas explicaciones y reordenando las opciones.
    Cambian la 7 ("inseguro": falso) y la 25 (B pide el recurso V: falso, sin ciclo; si fue un
    error de tipeo de la cátedra sería verdadero). La 4 (spooling) y la 14 (trasgresor) son nuevas.
- **Autoevaluación** (`evaluacion/preguntas/parcial-2025/`, ids `so-teo-NN`): las 55 en formato
  cuestionario, `data-etapa="1"`, todas con el mismo peso (en el parcial real algunas valían 1 y
  otras 2). Las armó un script desde el mismo texto que el parcial (no quedó en el repo): si se
  corrige una pregunta del parcial, corregirla también acá. Las opciones se mezclan al sortear,
  así que la explicación nombra cada opción por su texto, nunca por la letra.

## Forma de cada pregunta

- Cabecera con `Pregunta N`, los puntos y el tema en `parcial-tema`; "Seleccione una:" en cursiva;
  opciones en `ol.parcial-incisos`; V/F en un `<p>`.
- Resultados: la respuesta sola. Explicación: qué evalúa, la idea (tabla), opción por opción
  (`¿Va?` y por qué) y trampas.
