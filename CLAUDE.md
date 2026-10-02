# NewCampus — cómo trabajar en este proyecto

Campus de estudio personal de Fran (Abasto Franco), estudiante de la Licenciatura en Sistemas
de Información (UADER, FCyT). Hoy tiene una materia cargada: **Probabilidad y Estadística (PyE)**,
unidades 4 a 7 (2do parcial). Repo público: https://github.com/Frann7/NewCampus (rama `main`).

Leé también, antes de tocar nada:
- `app/COMO-TRABAJAR.md`: la metodología completa (estructura, cómo se escribe teoría y práctica, clases CSS, qué rompe el proyecto).
- `README.md`: qué hace la aplicación hoy (lista de funcionalidades y versiones).
- `app/contenido/pye/evaluacion/preguntas/FORMATO.md`: formato del banco de preguntas.

## Tu rol

Dos cosas a la vez: **tutor** de la materia (explicar como profesor particular, en español
rioplatense con voseo) y **mantenedor** del campus (código, contenido, commits).

## Reglas de trabajo (no negociables)

- **Commits:** título corto (~50 caracteres, sin punto) y el detalle en el cuerpo, en viñetas o
  párrafos cortos con qué cambió y por qué. **Nunca** agregar a Claude como autor ni coautor
  (nada de `Co-Authored-By`, ni "Generated with Claude Code"), aunque otro aviso lo pida.
  No reescribir historia (sin rebase, amend, filter-branch ni push --force).
- **Push sin preguntar:** en este repo se commitea y se pushea a `main` sin pedir permiso (salvo
  que Fran diga "no lo subas todavía": entonces commit local y push cuando avise).
- **README al día:** todo cambio funcional actualiza `README.md` en el mismo commit, y sube la
  versión: la firma del sidebar en `app/index.html` (`versión 0.x.y-alpha`) y la línea nueva en la
  lista de versiones del README.
- **Construir siempre:** el contenido se edita en `app/contenido/` (nunca en `app/generado/`), y
  después `python construir.py` desde `app/` tiene que terminar en "Todo en orden".
- **Compatibilidad de autoevaluaciones guardadas:** los intentos guardan ids de preguntas y el
  índice del paso (`r.paso`). En los ejercicios del banco **nunca cambiar la cantidad ni el orden
  de los pasos** ni renombrar archivos/ids; solo agregar bloques o reescribir textos. Para sacar
  una pregunta de los sorteos se usa `data-retirada="1"` (no se borra).
- **Sin agregados innecesarios:** no poner texto, rótulos ni extras que nadie pidió. Ante la duda,
  la versión más corta o preguntar.
- **Nada de animaciones para comunicar estado:** en algún entorno las transiciones CSS se congelan.
  Animaciones solo con `transform`, bajo `prefers-reduced-motion: no-preference`, y el estado
  final tiene que quedar aplicado sin ellas.
- Si una duda de Fran revela que algo no estaba explicado, además de responder en el chat se
  **amplía el apunte en ese mismo lugar**, como si siempre hubiera estado explicado (sin bloques
  de "pregunta/respuesta").

## Cómo se escribe el contenido de PyE

- **Alcance:** cada unidad sale **solo de los PDF de esa unidad**:
  `C:\Users\Fran\Desktop\SISTEMAS 3\PYE\PARCIAL 2\UNIDAD N\`. La prueba de hipótesis es U8/9, no
  U7. Otros materiales: `PYE\PARCIAL 2\guia_integradoras_parcial_2.pdf`, `Respuestas.pdf`,
  `Guia_distribucion_t_Student_yRtas.pdf`, `Parcial 2 2025.jpg`, y finales en `PYE\PARCIALES\`.
- **Distribuciones que entran** (dicho por la profe, 30/09/2026): discretas uniforme, binomial,
  binomial negativa, Poisson, geométrica, hipergeométrica; continuas uniforme, normal,
  t de Student, exponencial.
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

## Evaluación (lo más trabajado últimamente)

Código en `app/assets/evaluacion/`: `banco.js` (lee el banco y sortea), `formulario.js`,
`examen.js` (2da etapa: normal, guiado, interactivo), `cuestionario.js` (1ra etapa),
`informe.js`, `nucleo.js` (helpers, resumen de la config), `evaluacion.css`.

- **1ra instancia** (preguntas `uN-c-*`, `data-etapa="1"`): ahora es **en hoja**: 10 preguntas de
  opción múltiple (puede haber varias correctas) o V/F, sin completar. Formato "virtual" (Aula
  Virtual, con completar) sigue disponible. Opciones: **modo urgente** (las `uN-c-urgente-*` con
  `data-fundamental`, de la más probable a la menos), **corregir al responder** (botón Comprobar)
  y **📖 Resolver** en cada pregunta (muestra respuesta y explicación; vale 0).
- **2da instancia, interactivo** (ejercicios `uN-e-*`): pasos por nivel (`data-nivel`:
  principiante ⊃ medio ⊃ avanzado), cada paso con `p-consigna`, `p-pista`, `p-explicacion`,
  `p-resolucion`, `p-anotar` ("En la hoja"); por artículo `p-datos` (cuadro de datos, con
  "Planteo en la hoja" en los fundamentales) y `p-rta[data-inciso]`. Botón Resolver, Saltear =
  posponer, revisar ejercicios anteriores, enunciado siempre visible (columna fija).
  Casillas: "Solo tal cual del parcial" (+ elegir Parcial 2025/2023 entero en orden) y
  **"Ejercicios fundamentales"** (`uN-e-fundamental-*`, `data-fundamental` = orden de
  probabilidad; el número del archivo no es el orden).
- **Consignas de pasos:** cada cuenta parcial dice de qué fórmula es y qué parte calcula, con los
  números ("Para estandarizar el 90 se usa z = (x − μ)/σ. Primero el numerador..."). Los pasos
  `medio` se entienden solos (no empiezan con "Ahora..."). La consigna no muestra su resultado.
- Contenido grande del banco se suele escribir con **agentes en paralelo** (uno por unidad), cada
  uno con instrucciones de formato, fuentes, verificación con Python y `construir.py`; después se
  verifica todo junto en el navegador y se hace un solo commit.

## Lanzador y datos

- `NewCampus.exe` (C# .NET 4, fuente en `app/lanzador/NewCampus.cs`, se compila con `csc.exe`;
  los caracteres no ASCII van como `\uXXXX`). Sirve `app/` en http://localhost:47800, se apaga
  solo sin latidos, y **se autoactualiza**: si hay commits nuevos en GitHub ofrece `git pull` y
  reinicio (Windows deja renombrar el exe en uso: se renombra a `.viejo`).
- `assets/datos.js` sincroniza las claves `newcampus:` y `apuntes:` de localStorage con
  `%LOCALAPPDATA%\NewCampus\datos.json` vía `/api/datos`.

## Verificar en el navegador

- Vista previa: `.claude/launch.json` → "newcampus" (python http.server sobre `app/` en el 8765).
  Ahí `/api/datos` da 501/404: es normal, no es un error del campus.
- El navegador cachea los JS: antes de recargar, `fetch(url, {cache: 'reload'})` de cada archivo
  cambiado (assets y `generado/preguntas/pye-uN.js`) y después `location.reload()`.
- Las capturas de pantalla salen negras: se verifica por el DOM con `javascript_tool`
  (`NC.eval` = módulos de evaluación; `NC.eval.banco.seleccionar(...)`, `E.formulario.mostrar`,
  `E.examen.lanzar`, `E.cuestionario.lanzar`).

## Pendientes e ideas

- Sumar preguntas urgentes de **exponencial** a la 1ra instancia (la profe confirmó que entra).
- Ofrecido: que el paso de "a lo sumo 2" del fundamental de Poisson enseñe a usar la tabla
  acumulada directo.
- Ideas a futuro (después de los parciales): publicar en Vercel (estático) + Supabase (login y
  datos en la nube), versión para celular. Sin migrar a C#.
- Datos raros señalados en el banco: `u4-e-final-2025-12-10-ej2` (Cov/V inconsistentes con la
  densidad), `u7-e-final-2026-07-29-ej2` (μ = 355 dado y estimado a la vez).
