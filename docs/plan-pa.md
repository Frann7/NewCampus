# Plan: sumar Programación Avanzada (PA)

Decidido con Fran el 4/10/2026. **Una fase = una sesión = un commit** (o pocos). Al terminar una
fase, se tacha acá y se anota lo que quedó. Cuando estén todas, este archivo se borra y lo que
siga valiendo pasa a `docs/` y a `app/contenido/pa/CLAUDE.md`.

## Qué se decidió

- **Clases, no unidades:** las 6 clases de `C:\Users\Fran\Desktop\SISTEMAS 3\PA\CLASE N\`, en
  `materias.json` como `{ "clave": "c1", "num": "Clase 1", "nombre": "..." }`. Entran las 6
  (la 4 es JavaScript, DOM y API REST: no la toma el Parcial PHP, pero es de la materia).
- **Tareas y Calendario pasan al menú lateral**, como entradas fijas arriba de las materias. La
  barra de cada materia queda en Teoría · Práctica · Evaluación.
- **Evaluación por materia:** PyE sigue igual. PA tiene una versión simple: la lista de parciales
  (transcriptos, con resultados y explicación) y **Rendir** el parcial entero. Sin etapas, sin modo
  interactivo, sin elegir clases ni cantidad.
- **Rendir = como el Aula Virtual:** las 20 preguntas en una página, en el orden original, con
  reloj de cuenta regresiva de 40 min. Al entregar: nota sobre 100 (5 c/u; puntaje parcial en
  emparejamiento y en varias correctas), y revisión con la explicación de cada pregunta. Sin la
  condición 30/60 de PyE (no se sabe el reglamento de PA: no se inventa).
- **No se crean preguntas de más:** el banco de PA son las 20 del Parcial PHP y nada más.
- **La teoría sale de los PDFs de cátedra**, como en PyE. `Apuntes_Programacion_Avanzada.html`
  (un apunte viejo de Fran) es solo referencia de qué le sirvió.
- El examen teórico (`Examen Teórico 2025.pdf`) queda para después.

## Material (en `SISTEMAS 3\PA\`)

| Clase | Teoría | Práctica |
| :-- | :-- | :-- |
| 1 | PHP básico: etiquetas, comentarios, variables, operadores, if/switch, while/do/for (Presentación 20 p., Teoría 17 p.); guía de instalación de XAMPP | `PA_Clase_11` + resuelta |
| 2 | Arreglos (asociativos, multidimensionales, recorrer), strings (Presentación 21 p., Teoría 20 p.); `introduccion_a_xhtml.pdf` (libro, 184 p.: solo referencia) | `PA-Clase-2` + resuelta, `ejemplo.zip` |
| 3 | HTML, formularios, GET/POST, datos desde PHP (Presentación 18 p., Teoría 6 p.) | `PA-Clase-3`, `site.zip` |
| 4 | Navegador, DOM, JavaScript, clases JS, API REST, JSON (solo Presentación 18 p.) | `EjemplosJavascript.zip`, `sitePoo.zip` |
| 5 | Sesiones (Teoría 6 p.) | `PA-Clase-5`; `sessiones`, `formularios` (captcha, token), `ataqueForm`, `objeto` (zips) |
| 6 | Conexión a BD con mysqli (Teoría 4 p.) | `PA-Clase-6` (está en TEORIA), `SitioEjemplo.zip` |

- **`Parcial PHP.pdf`** (= `Parical PHP.pdf`, copia exacta): 20 preguntas del Aula Virtual, 5 puntos
  c/u. Formatos: opción única, V/F, varias correctas (la 15) y emparejamiento con desplegables
  (1, 3, 4, 7).
- **Datos de otras personas: NUNCA al repo.** `ExamenPA-2026.pdf` no es un examen: es la lista de
  alumnos con nombre y horario. `REPO actividad aulica\` tiene archivos con DNI. `TP\` y los zips
  `TP_Centro_Veterinario_*` son el TP del grupo de Fran (fuera de alcance).
- Notas propias de Fran: `Apuntes de practica.docx` (phpMyAdmin, MyISAM/InnoDB, permisos);
  `ResumenTeoria.docx` está vacío.

## Fases

### Fase 0 — Fuentes en texto y reglas de PA
- Sumarle a `fuentes/extraer.py` una forma de **excluir** archivos y extraer `SISTEMAS 3\PA` a
  `fuentes/pa/` **sin `ExamenPA-2026.pdf`**. Índice "página → qué hay" y ⚠ como en PyE (los PDFs
  son chicos: un agente o dos alcanzan); del libro de XHTML, solo un índice por capítulos.
  `fuentes/pa/INDICE.md`.
- Crear `app/contenido/pa/CLAUDE.md`: fuentes y alcance, y **cómo se escribe teoría de
  programación** (ver Fase 4).
- Clases en `materias.json` (`c1`..`c6`, con nombre).

### Fase 1 — Tareas y Calendario al menú lateral
- Rutas propias (`#tareas`, `#calendario`), entradas fijas arriba de las materias. Las rutas
  viejas (`#pye/u7/tareas`) redirigen. Revisar `?panel=1` (sacar a otra ventana) y la ruta de
  inicio (`app.js:1339`).
- La barra de pestañas de la materia: Teoría · Práctica · Evaluación (`index.html:76-82`).
- Textos "Unidad"/"Unidades" que se ven en una materia por clases: usar el `num` del menú o
  "Unidades/Clases" según la materia (calendario `detalle.js:269`, `app.js:1404`).
- README + versión. `docs/pestanias.md`.

### Fase 2 — Evaluación simple por materia
- En `materias.json`, por materia, qué evaluación tiene (p. ej. `"evaluacion": "simple"`; PyE
  sin cambios). `evaluacion.js` (hoy siempre arma Parciales + Finales + formulario de PyE,
  `121-146`) dibuja la simple para PA: los exámenes y, en los que tienen banco, **Rendir**.
- `cuestionario.js` + `banco.js`: una rama con **conjunto fijo y en orden** (`config.ids`, o la
  carpeta del banco con el mismo nombre que el examen), formato virtual, reloj de 40 min, sin
  mezclar el orden de las preguntas, y el informe **sin** la condición 30/60
  (`nucleo.js:147-153`) ni chips de unidad (`numeroDeUnidad`).
- Los intentos se guardan como los de PyE (misma clave, filtrados por materia).
- Código en el texto: estilo para `<pre><code>` (no hay ninguno hoy en `estilos.css`), sin
  librerías. El `<` del código va como `&lt;` (regla del proyecto). Ojo con `revisar_formulas`
  de `construir.py`, que cuenta `\(` y `\)`: que no marque código como fórmula rota.
- README + versión. `docs/evaluacion.md`.

### Fase 3 — El Parcial PHP: transcripción, resolución y banco
- `contenido/pa/evaluacion/parciales/<id>/`: `meta.json` + un archivo por pregunta, con
  `pd-resultados` y `pd-explicacion` (qué evalúa, en qué clase se ve, por qué cada opción está
  bien o mal, la trampa). **Cada salida se verifica corriendo el script** con
  `C:\xampp\php\php.exe`.
- El banco: `contenido/pa/evaluacion/preguntas/<id>/`, las 20 en el formato de la 1ra etapa
  (`opcion` para única y V/F, `multiple` para la 15, `completar` con desplegables para los
  emparejamientos), `data-origen="parcial"`.
- Para mirar con cuidado:
  - Preg. 5: el script imprime `Hola, mundo!` y el enunciado dice `Hola, Mundo!`. Se llega
    con `$a` falso, `$b` falso y `$c` verdadero (opción d).
  - Preg. 10: `sort()` y "a nivel de claves", redacción ambigua. Ver qué dice la teoría de la
    Clase 2 antes de dar la respuesta.
  - Preg. 17: `$_REQUEST` trae GET, POST y COOKIE, no SESSION.
  - Preg. 18: depende de la fecha; la respuesta es el formato `d/m/Y`.

### Fase 4 — Teoría por clase (6 clases)
- Estructura de cada sección, adaptada de la de PyE a programación: **Para qué sirve → Sintaxis →
  Qué es cada parte (tabla) → Ejemplos** (código, qué imprime y por qué, línea por línea) **→
  Errores y trampas**. Teoría corta; el detalle en los ejemplos.
- ★ (`data-examen="igual"`) en lo que tomó el Parcial PHP, con `data-examen-ref="Parcial PHP ·
  preg. N"`.
- Agentes en paralelo, uno por clase, cada uno con su `fuentes/pa/CLASE N/`. Todo ejemplo con
  salida se corre con PHP antes de escribirla.

### Fase 5 — Práctica por clase
- Las guías prácticas resueltas y explicadas (C1 y C2 traen resolución de la cátedra; C3, C5 y
  C6 hay que resolverlas). Los zips como ejemplos de código, explicados.

### Después
- El examen teórico (`Examen Teórico 2025.pdf`) en Evaluación.
