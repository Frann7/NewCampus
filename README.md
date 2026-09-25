# NewCampus

Campus de apuntes orientado a la carrera **Analista en Sistemas de Información** (por ahora,
solo tercer año). Corre **en local**: un ejecutable levanta un servidor en tu propia máquina y
abre los apuntes en el navegador. No hay nube ni cuenta: lo único que se trae de internet son las
fórmulas (MathJax) y las tipografías. Tus datos no salen de tu máquina.

> **Versión en desarrollo (alpha).** Está a medio hacer y cambia seguido. Todavía no es una
> versión pensada para descargar y usar en serio.

## Qué tiene hasta ahora

* **Apuntes por materia y unidad**, con pestañas de **Teoría** y **Práctica**.
  Con contenido, por ahora, solo Probabilidad y Estadística (unidades 4 a 7); el resto de las
  materias de tercer año ya están en el menú como "pronto".
* **Evaluación**: **parciales y finales** de la cátedra transcriptos, en dos listas. Algunos traen
  cada ejercicio con resultados y explicación detallada desplegables; otros están solo transcriptos,
  para usarlos como práctica. Y **autoevaluaciones** que armás vos, con su informe final. Primero
  se elige **qué etapa del parcial** se simula: la **1ra, el cuestionario virtual** (opción única,
  varias correctas, verdadero o falso y completar con coma y 2 decimales, corregido al entregar
  sobre 100 puntos y con lo que esa nota significa según el reglamento), o la **2da, el escrito**,
  que se practica de tres maneras:
  * **Normal, como en el parcial:** preguntas de teoría y práctica con opciones.
  * **Normal, fáciles y guiadas:** las mismas, más fáciles: con pistas y la práctica en todos sus pasos; si te equivocás, volvés a intentar (sin vidas ni nivel, que son del interactivo).
  * **Interactivo:** un **ejercicio de parcial completo** (reales de los exámenes mezclados con
    inventados de la misma forma) que se va desglosando en partes: en avanzado se pide el
    resultado de cada inciso; en principiante, cada cuenta chica. Se puede saltear un ejercicio
    entero.

  En Normal hay además una **navegación libre** opcional: casillas para saltar a cualquier
  pregunta, saltear y volver, y terminar cuando quieras. Todas las preguntas
  salen de los exámenes: cada una dice de qué parcial o final viene, con ★ o ◈, y al sortear salen
  más las de parciales.
* **Qué entró en el examen**: cada ejercicio de la guía y cada sección de teoría puede venir marcada
  con ★ (tal cual como lo tomaron en un parcial) o ◈ (el mismo tema con un cambio, o algo que
  solo tomaron en finales), diciendo en qué examen apareció y qué cambia. La marca se ve en la tarjeta y en el índice lateral, y una barra de filtro
  deja a la vista solo lo marcado, para estudiar primero lo que ya tomaron.
* **Índice lateral con subíndices**: en la práctica, cada ejercicio abierto lista debajo sus
  pasos e incisos, y tocar uno lleva directo a ese inciso.
* **Ruta recomendada**: una pestaña por materia, al lado del Calendario, con lo fundamental para
  el parcial dividido en partes (teoría, práctica, parciales y autoevaluación en el orden en que
  conviene hacerlos). Cada paso se tacha y queda guardado en el navegador, con la cuenta de cada
  parte y el progreso total. Cada paso tiene un botón que lleva directo a donde hay que ir: la
  sección de teoría o el primer ejercicio recomendado (ya desplegados), el parcial en ese
  ejercicio, o el formulario de autoevaluación completo con lo que recomienda la ruta (solo falta
  guardar). Mantenerlo apretado lo abre en una ventana aparte, como las pestañas. Se escribe en
  `app/contenido/<materia>/ruta/`.
* **Calendario**: un mes a pantalla completa con flechas para navegar, o el año entero.
  Se le anotan **parciales y trabajos prácticos** (materia, unidades que entran, día y una
  descripción); el día con parcial se pinta entero del color de la materia, y si ese día cae más de
  una, la casilla se parte en franjas. Al abrir un día, la ficha dice **cuánto falta** para ese día.
  Trae cargados los feriados, las mesas de examen y los días
  sin actividad.
* **Próximas fechas**: el índice de la derecha del calendario, agrupado por mes y con filtro por
  tipo, que dice cuántos días y horas faltan para cada fecha y te lleva a ella con un clic.
  Al entrar al campus avisa arriba a la derecha: un aviso por materia, con todas sus fechas, de la
  más próxima a la más lejana. Se encienden o apagan **por materia**.
* **Todo plegable**: cada sección de teoría y cada ejercicio de práctica se abre y se cierra, así
  entrás a una unidad y ves la lista de lo que hay en vez de un muro de texto.
* **Índice lateral** de la sección que estás leyendo, con seguimiento del scroll: el texto te lleva
  al título y la flechita de al lado pliega o despliega esa sección, igual que desde la página.
* **Visor de PDFs** de cátedra en ventanas movibles.
* **Ventanas duplicadas**: manteniendo apretada una pestaña sale una copia de ese apartado en
  otra ventana, para leer dos partes a la vez.
* **Cronómetro de estudio**: en la barra de arriba, al lado del reloj. Le ponés los minutos que
  quieras (o elegís uno de los sugeridos), la cuenta regresiva aparece en ese mismo lugar, y cuando
  llega a cero sale un cartel para cortar, repetir el mismo tiempo o poner otro. Pensado para
  trabajar de a tandas: 30 minutos de estudio, 5 de descanso.
* **Menú de materias plegable**: la manija redonda en el borde del menú (o Ctrl+B) lo esconde para
  dejar toda la pantalla a los apuntes, y se recuerda entre visitas.
* **Animaciones suaves**: los apartados y las secciones entran subiendo unos píxeles, los botones
  rebotan al apretarlos y las tarjetas se levantan al pasar el mouse. Son solo de movimiento (nada
  depende de que corran) y se apagan si el sistema pide reducir el movimiento.
* Modo claro / oscuro, y arriba a la derecha tres medidores juntos y separados entre sí: la hora de
  Argentina, el tiempo que llevás en la página y el cronómetro.

## Tus datos (no se pierden al actualizar)

Lo que cargás vos —fechas del calendario, autoevaluaciones y sus informes, la ruta tachada, el
menú plegado— **no está en la carpeta del repositorio**. `NewCampus.exe` lo guarda en un archivo
de tu computadora:

```
%LOCALAPPDATA%\NewCampus\datos.json      (por ejemplo C:\Users\<vos>\AppData\Local\NewCampus)
```

Por eso:

* **`git pull` o bajar una versión nueva no toca tus datos.** Cada persona tiene su propio archivo
  en su propia PC, y nunca se sube a GitHub.
* No dependen del navegador ni del puerto: si cambiás de navegador, borrás sus datos o el campus
  abre en otro puerto, al abrirlo con `NewCampus.exe` vuelve a cargar todo desde ese archivo.
* Cada vez que se guarda, la versión anterior queda en `datos.anterior.json`, al lado, por si hace
  falta volver atrás.
* Para llevarte tus datos a otra PC, copiá `datos.json` a la misma carpeta de la otra.
* La primera vez que abrís una versión con este archivo, se crea solo con lo que ya tenías en el
  navegador.

Si abrís el campus sin `NewCampus.exe` (otro servidor, o doble clic en `index.html`), los datos
quedan solo en el navegador.

## Qué necesitás para correrlo

| Para | Necesitás |
| :--- | :--- |
| Usarlo | Windows con .NET Framework 4 (ya viene instalado), un navegador predeterminado y conexión a internet para las fórmulas |
| Editar los apuntes | Python 3 (para `app/construir.py`) |
| Recompilar el ejecutable | `csc.exe` del .NET Framework 4 (el comando está arriba de `app/lanzador/NewCampus.cs`) |

Doble clic en `NewCampus.exe`: levanta el servidor en `http://localhost:47800` y abre el
navegador. Antes revisa que esté todo lo necesario y, si falta algo, lo dice en un solo
cartel con lo que hay que instalar: un navegador, la conexión a internet (las fórmulas se cargan
de ahí) o Python 3 si faltan los apuntes generados (y si Python está, los genera solo). El .NET
Framework 4 no lo puede revisar el propio `.exe`: si faltara, Windows avisa antes de abrirlo.
Escucha **solo en localhost** y rechaza cualquier pedido que no venga de esa misma PC.
Cuando cerrás la pestaña, el servidor se apaga solo; también podés cerrarlo desde el ícono que
queda junto al reloj de Windows.

## Cómo se edita

Los apuntes se escriben en `app/contenido/<materia>/<unidad>/<teoria|practica>/`, **un archivo por
ejercicio o sección** (`01-....html`, `02-....html`), y después se corre, dentro de `app/`:

```bash
python construir.py
```

Eso arma `app/generado/`: un `indice.js` chiquito con lo que hay, y un archivo por unidad que la
página se trae **solo cuando abrís esa unidad**. Nunca se edita `generado/` a mano.

El menú de materias no se escribe a mano: sale de `app/contenido/materias.json`. Para sumar una
unidad alcanza con crear su carpeta, nombrarla ahí y volver a construir.

## Material de cátedra

Los PDFs de la cátedra que usa el visor viven en `app/pdf/<materia>/`, una sola copia por
archivo. Son material de la facultad, subido acá solo para estudiar.
La excepción es `formulas-u4.pdf`, una hoja de repaso con las fórmulas de la Unidad 4 que no es
de la cátedra; se genera desde `app/pdf/pye/fuentes/formulas-u4.html` imprimiéndolo a PDF con
Chrome (`chrome --headless --print-to-pdf`).

## Versiones

`0.x.y-alpha` mientras esté en desarrollo. La `1.0.0` queda reservada para cuando esté terminado.
La versión actual se lee al pie del menú lateral.

* **0.11.0-alpha** — los datos del usuario se guardan en un archivo de la PC, fuera del
  repositorio (no se pierden al actualizar ni al cambiar de navegador o de puerto); menú de
  materias plegable y animaciones.
* **0.10.0-alpha** — pestaña Ruta recomendada; Unidad 7 (distribuciones muestrales, TLC, intervalos de confianza y tamaño
  de muestra) con teoría, práctica resuelta, banco de autoevaluación y la Tabla IC-PH en el visor;
  teoría de la U6 y práctica de la U6 rehechas con el formato de la U5 (desarme del enunciado y
  cada paso explicado), con toda la guía de la U6 resuelta.
* **0.9.0-alpha** — autoevaluación de la 2da etapa en tres maneras: normal, guiada e interactiva
  con ejercicios de parcial completos desglosados por nivel (se pueden saltear); navegación libre
  en el modo normal; `NewCampus.exe` avisa qué falta instalar; teoría de la U6 reorganizada con
  gráficos y guías "Cómo leer esta unidad" en las U4, U5 y U6.
* **0.8.0-alpha** — autoevaluación por etapa del parcial: la 1ra etapa (cuestionario del Aula
  Virtual) con su propio banco y corrección con puntaje parcial; todas las preguntas marcadas con
  su examen de origen y sorteo que prioriza parciales; finales de febrero y julio de 2026
  resueltos.
* **0.7.0-alpha** — finales transcriptos además de los parciales, marcas ★ / ◈ en teoría y
  práctica con filtro por lo que ya tomaron, banco de autoevaluación de 38 preguntas sacadas de los
  exámenes, cronómetro de estudio en la barra superior, y cuenta regresiva en la ficha del día del
  calendario.
* **0.6.0-alpha** — calendario con parciales, trabajos prácticos y recordatorios; contenido partido
  en fragmentos y cargado por unidad; menú lateral automático; teoría y práctica plegables.
* **0.5.0-alpha** — primera versión publicada: apuntes, evaluación con parciales y autoevaluaciones,
  calendario, ventanas duplicadas.

---

by Abasto Franco
