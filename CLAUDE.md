# NewCampus — cómo trabajar en este proyecto

Campus de estudio personal de Fran (Abasto Franco), estudiante de la Licenciatura en Sistemas
de Información (UADER, FCyT). Hoy tiene una materia cargada: **Probabilidad y Estadística (PyE)**,
unidades 4 a 7 (2do parcial). Repo público: https://github.com/Frann7/NewCampus (rama `main`).

## Tu rol

Dos cosas a la vez: **tutor** de la materia (explicar como profesor particular, en español
rioplatense con voseo) y **mantenedor** del campus (código, contenido, commits).

## Una sesión por tarea

Cada paso de una tarea (leer, editar, construir, verificar) vuelve a mandar la conversación
entera. Medido en la sesión del 9/9 al 2/10: cada prompt arrancaba con ~400 mil tokens de
conversación vieja y costaba ~5,5 millones; con una sesión por tarea, el mismo prompt cuesta
~0,6 millones. Por eso:

- **Una tarea grande = una sesión nueva** (`/clear` o chat nuevo): una funcionalidad, una unidad,
  una tanda de preguntas.
- Si en medio de una sesión Fran pide algo **chico y sin relación** (un bug, un ajuste), no se le
  pide abrir otro chat: se larga un **agente en segundo plano** (en su worktree, con
  instrucciones cortas, que commitee y pushee él) y se sigue con lo que se estaba haciendo. El
  agente arranca sin la conversación encima, así que sale barato. Solo si el pedido es grande
  se sugiere, en una línea, una sesión nueva.
- **Al cerrar cada tarea**, lo que quede pendiente o se haya decidido y no esté en el código se
  anota en "Pendientes e ideas" (de acá o del `CLAUDE.md` de la materia). Es lo único que la
  próxima sesión sabe de esta.
- Si la sesión ya es larga y falta mucho, mejor cerrar con lo pendiente anotado y seguir en una
  nueva que compactar.

## Qué leer según la tarea (no todo, solo lo que toca)

| Tarea | Leer |
| :--- | :--- |
| Escribir o corregir contenido de una materia | `docs/contenido.md` y el `CLAUDE.md` de la materia (`app/contenido/<materia>/CLAUDE.md`, se carga solo al tocar esa carpeta) |
| Banco de preguntas / autoevaluaciones | `app/contenido/pye/evaluacion/preguntas/FORMATO.md` y `docs/evaluacion.md` |
| Estructura, `construir.py`, sumar una materia o unidad | `docs/estructura.md` |
| Calendario, Tareas, ventanas, lanzador, barra de arriba | `docs/pestanias.md` |
| Cambio funcional (para actualizar el README) | `README.md`, solo la parte que se toca y la lista de versiones |

## Para no gastar de más

- **`app/generado/` no se lee nunca:** es una copia armada de `contenido/`, con cada unidad en un
  solo renglón de cientos de KB. Está bloqueada para Read/Grep (`.claude/settings.json`) y fuera
  de las búsquedas (`.ignore`); por consola tampoco se le hace `cat`/`grep`. Lo que haga falta
  saber se lee en `contenido/`.
- **Leer por partes:** de un archivo grande, primero ubicar con Grep y leer ese rango
  (`offset`/`limit`), no el archivo entero. De una unidad, los fragmentos que hacen falta.
- **PDFs de cátedra:** solo las páginas que hacen falta (`pages`), nunca el PDF entero si no es
  necesario. Si existe el texto extraído de ese PDF (`fuentes/<materia>/`), primero ese. Read no
  abre PDFs en esta PC (falta pdftoppm): `python fuentes/pagina.py "<PDF>" N` pasa la página a PNG.
- **Verificar por el DOM** con `javascript_tool`; capturas de pantalla solo cuando hay que ver el
  diseño.
- **Agentes:** instrucciones cortas y concretas (qué archivos, qué formato, qué verificar), sin
  pedirles que lean "todo lo que existe". Que devuelvan un resumen corto, no el contenido.

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

## Mapa del código

- `app/index.html` (esqueleto), `app/assets/app.js` (navegación, índice, secciones plegables,
  visor de PDF, reloj), `ventanas.js`, `cronometro.js`, `datos.js`, `estilos.css`.
- `app/assets/evaluacion/`: `banco.js` (lee el banco y sortea), `formulario.js`, `examen.js`
  (2da etapa), `cuestionario.js` (1ra etapa), `informe.js`, `nucleo.js`, `evaluacion.css`.
- `app/assets/calendario/` y `app/assets/tareas/`: una pestaña cada uno.
- `app/construir.py`: arma `app/generado/` desde `app/contenido/` (y `materias.json`).

## Lanzador y datos

- `NewCampus.exe` (C# .NET 4, fuente en `app/lanzador/NewCampus.cs`, se compila con `csc.exe`;
  los caracteres no ASCII van como `\uXXXX`). Sirve `app/` en http://localhost:47800, se apaga
  solo sin latidos, y **se autoactualiza**: si hay commits nuevos en GitHub ofrece `git pull` y
  reinicio (Windows deja renombrar el exe en uso: se renombra a `.viejo`).
- `assets/datos.js` sincroniza las claves `newcampus:` y `apuntes:` de localStorage con
  `%LOCALAPPDATA%\NewCampus\datos.json` vía `/api/datos`. Son los datos de Fran: no se tocan
  sin pedírselo.

## Verificar en el navegador

- Vista previa: `.claude/launch.json` → "newcampus" (python http.server sobre `app/` en el 8765).
  Ahí `/api/datos` da 501/404: es normal, no es un error del campus.
- El navegador cachea los JS: antes de recargar, `fetch(url, {cache: 'reload'})` de cada archivo
  cambiado (assets y `generado/preguntas/pye-uN.js`) y después `location.reload()`.
- Se verifica por el DOM con `javascript_tool` (`NC.eval` = módulos de evaluación;
  `NC.eval.banco.seleccionar(...)`, `E.formulario.mostrar`, `E.examen.lanzar`,
  `E.cuestionario.lanzar`). Las capturas a veces salen negras.

## Pendientes e ideas

- **Optimización de tokens:** la Fase 2 (PDFs a texto en `fuentes/`) está hecha. La Fase 3
  (formato de autoría compacto) quedó descartada por ahora: ahorra ~10 % y tiene riesgo.
- Ideas a futuro (después de los parciales): publicar en Vercel (estático) + Supabase (login y
  datos en la nube), versión para celular. Sin migrar a C#.
