# NewCampus

Campus de apuntes orientado a la carrera **Analista en Sistemas de Información** (por ahora,
solo tercer año). Corre **en local**: un ejecutable levanta un servidor en tu propia máquina y
abre los apuntes en el navegador. No hay nube, no hay cuenta, no sale nada a internet.

> **Versión en desarrollo (alpha).** Está a medio hacer y cambia seguido. Todavía no es una
> versión pensada para descargar y usar en serio.

## Qué tiene hasta ahora

* **Apuntes por materia y unidad**, con pestañas de **Teoría** y **Práctica**.
  Con contenido, por ahora, solo Probabilidad y Estadística (unidades 4, 5 y 6); el resto de las
  materias de tercer año ya están en el menú como "pronto".
* **Evaluación**: parciales de la cátedra transcriptos, cada ejercicio con resultados y
  explicación detallada desplegables; y **autoevaluaciones** que armás vos, en modo normal o
  interactivo (con pistas, vidas y resolución paso a paso), con su informe final.
* **Calendario**: un mes a pantalla completa con flechas para navegar, o el año entero.
  Se le anotan **parciales y trabajos prácticos** (materia, unidades que entran, día y una
  descripción); el día con parcial se pinta entero del color de la materia, y si ese día cae más de
  una, la casilla se parte en franjas. Trae cargados los feriados, las mesas de examen y los días
  sin actividad.
* **Próximas fechas**: el índice de la derecha del calendario, agrupado por mes y con filtro por
  tipo, que dice cuántos días y horas faltan para cada fecha y te lleva a ella con un clic.
  Al entrar al campus avisa arriba a la derecha: un aviso por materia, con todas sus fechas, unos
  segundos cada uno. Se encienden o apagan **por materia**.
* **Todo plegable**: cada sección de teoría y cada ejercicio de práctica se abre y se cierra, así
  entrás a una unidad y ves la lista de lo que hay en vez de un muro de texto.
* **Índice lateral** de la sección que estás leyendo, con seguimiento del scroll: al tocar un título
  abre la sección que corresponda.
* **Visor de PDFs** de cátedra en ventanas movibles.
* **Ventanas duplicadas**: manteniendo apretada una pestaña sale una copia de ese apartado en
  otra ventana, para leer dos partes a la vez.
* Modo claro / oscuro, reloj de Argentina y contador de tiempo de uso.

Lo que cargás vos —autoevaluaciones, fechas del calendario, recordatorios— se guarda en el
navegador de esa máquina, no en ningún servidor.

## Qué necesitás para correrlo

| Para | Necesitás |
| :--- | :--- |
| Usarlo | Windows con .NET Framework 4 (ya viene instalado) y un navegador |
| Editar los apuntes | Python 3 (para `app/construir.py`) |
| Recompilar el ejecutable | `csc.exe` del .NET Framework 4 (el comando está arriba de `app/lanzador/NewCampus.cs`) |

Doble clic en `NewCampus.exe`: levanta el servidor en `http://localhost:47800` y abre el
navegador. Escucha **solo en localhost** y rechaza cualquier pedido que no venga de esa misma PC.
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

## Versiones

`0.x.y-alpha` mientras esté en desarrollo. La `1.0.0` queda reservada para cuando esté terminado.
La versión actual se lee al pie del menú lateral.

* **0.6.0-alpha** — calendario con parciales, trabajos prácticos y recordatorios; contenido partido
  en fragmentos y cargado por unidad; menú lateral automático; teoría y práctica plegables.
* **0.5.0-alpha** — primera versión publicada: apuntes, evaluación con parciales y autoevaluaciones,
  calendario, ventanas duplicadas.

---

by Abasto Franco
