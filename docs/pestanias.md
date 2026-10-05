# Calendario, Tareas, ventanas duplicadas, lanzador y barra superior

> Las rutas de este documento son relativas a `app/` (salvo que digan otra cosa).


**Tareas y Calendario están en dos lugares**: como entradas fijas del menú lateral, arriba de
"MATERIAS" (`.nav-fija` en `index.html`), y en la fila de pestañas, después de Evaluación
(Teoría · Práctica · Evaluación · Tareas · Calendario). Los dos llevan a las mismas rutas propias
`#tareas` y `#calendario`; las viejas (`#pye/u7/tareas`) se reescriben a las nuevas (`leerRuta` en
`app.js`). Mientras se ven, las migas no muestran materia, la fila de pestañas sigue a la vista con
Tareas o Calendario marcada (y su entrada del menú también), y Teoría, Práctica y Evaluación llevan
a la última materia y unidad, que siguen en el state. Para que eso sobreviva a una recarga en
`#tareas`, `apuntes:ruta` guarda siempre las tres partes (`pa/c2/tareas`).

**Calendario** (uno solo, no depende de la materia ni de la unidad): `assets/calendario/`.
Vista **Mes** (el mes ocupando la pantalla, flechas a los costados, el día de hoy marcado) y vista
**Año** (los doce meses; al hacer clic en uno se entra a su vista Mes). La semana empieza el lunes y
"hoy" se calcula en UTC-3, igual que el reloj. La vista y el mes quedan guardados en el navegador.

En cada día se ven dos cosas:

* **Fechas académicas fijas** (feriados, mesas de examen, días sin actividad). Se cargan a mano en
  `assets/calendario/fechas.js`, que tiene el formato explicado arriba de todo. Van marcadas con una
  franja de color a la izquierda del día.
* **Parciales y trabajos prácticos** que anota el usuario con el botón **+ Fecha** o tocando un día.
  Se elige materia (de las del menú lateral, estén disponibles o no), unidades si la materia tiene
  (el rótulo usa el término de la materia: "Clases" en PA, sacado del `num` de materias.json),
  el día y una descripción opcional; después se pueden editar y eliminar. Cada materia tiene su color,
  sacado de su lugar en el menú (`--h`, el tono; el nombre corto sale de `data-corto`).

Tocar un día abre su **ficha**: lo que hay ese día, con los botones de editar y eliminar, y abajo
**+ Agregar fecha** y **Aceptar** (que la cierra); el formulario de alta tiene Cancelar y Agregar. Se guardan en el `localStorage` (`newcampus:eventos`).

El día con **parcial** se pinta entero del color de la materia, para que no se pueda pasar por alto;
el que solo tiene **trabajo práctico** queda apenas teñido. Si ese día cae más de una materia, la
casilla se parte en franjas horizontales, una por materia.

No puede haber dos fechas del mismo tipo, de la misma materia y el mismo día: el formulario avisa
y manda a editar la que ya está.

A la derecha del calendario está la **agenda**: filas cortas agrupadas por mes, con filtro por tipo
(todo / parciales / prácticos), cuántos días y horas faltan —se recalcula solo— y, al tocarlas, el
calendario salta a ese día. Al final hay un desplegable **Recordatorios** con una casilla por
materia (no por fecha) y el interruptor general; **solo la casilla marca y desmarca**, y los cambios
no se aplican hasta tocar **Aceptar**. Con eso encendido, al entrar al campus salen los
**avisos**: arriba a la derecha, uno por materia con **todas** las fechas que esa materia tiene por
delante, ordenados de la más próxima a la más lejana, unos segundos cada uno y se van solos; la ✕
corta la tanda y tocar una fecha lleva a ese día.
(`newcampus:avisos` guarda las materias APAGADAS, así una materia nueva avisa sin tocar nada; el
filtro va en `newcampus:agenda`.)

**Tareas** (una sola, como el Calendario): `assets/tareas/`. Un tablero de tres columnas
(Pendientes, En proceso, Hecho) con tareas de texto que se agregan, editan, borran y se pasan de
columna con las flechas o arrastrándolas. Cada tarea puede llevar una materia (`materia`, la clave
del menú) y toma el tono de esa materia que usa el calendario (`NC.calEventos`); sin materia es
general. Tope de 25 tareas por columna (`MAXIMO`) y 300
caracteres por tarea (`MAX_TEXTO`). Se guardan en `newcampus:tareas`.

**Ventanas duplicadas** (`assets/ventanas.js`): manteniendo apretada una pestaña 0,8 s sale una **copia**
de ese apartado en otra ventana (`index.html?panel=1#<materia>/<unidad>/<pestaña>`). Con Tareas y
Calendario, de la pestaña o del menú lateral, la copia es `index.html?panel=1#tareas`. La copia no
tiene menú de materias ni pestañas, pero sí su índice y su material; la ventana original no se mueve.
Máximo 4 copias a la vez. Las copias **no laten** al servidor (no cuentan tiempo ni pisan el último
apartado abierto) y se cierran solas cuando se cierra la ventana principal.

**Cómo se abre:** `NewCampus.exe` levanta un servidor local (`http://localhost:47800`, solo
accesible desde esa PC) y abre el navegador. La página manda un latido cada 10 segundos:
cuando se cierra la pestaña el servidor se apaga solo. También se puede cerrar desde el ícono
junto al reloj. Abrir `index.html` con doble clic sigue funcionando para leer.
Si cambiás `lanzador/NewCampus.cs`, el comando para recompilar está arriba de ese archivo.

**Arriba a la derecha** hay un reloj de Argentina (UTC-3) y, debajo, el tiempo que se lleva con la
página abierta. Ese contador es **de cada corrida del .exe**: se guarda junto al número de corrida
que informa `api/estado`, así recargar la página lo sigue sumando pero cerrar NewCampus lo descarta.
También vuelve a cero a las 99 horas o con su botón. El último apartado abierto sí se recuerda
entre corridas.

**La barra de arriba a la derecha** son tres `.medidor` dentro de una sola caja `.medidores`,
separados por una línea: la hora de Argentina, el tiempo en la página y el cronómetro. Cada uno
lleva un `.medidor-etq` (el rótulo chiquito) y un `.medidor-valor`. El botón de tema queda **fuera**
de esa caja a propósito: no es un medidor, y antes se confundía con ellos. En las ventanas
duplicadas la caja entera no se muestra (`html.es-panel .medidores`), igual que pasaba con el reloj:
un cronómetro por ventana no se sabría cuál manda.
