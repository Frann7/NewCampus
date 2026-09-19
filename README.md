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
  descripción); el día con parcial se pinta entero del color de la materia. Trae cargados los
  feriados, las mesas de examen y los días sin actividad.
* **Próximas fechas**: el índice de la derecha del calendario, con cuántos días y horas faltan
  para cada parcial, y un **recordatorio al entrar** que se enciende o apaga por materia.
* **Índice lateral** de la sección que estás leyendo, con seguimiento del scroll.
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

Los apuntes se escriben en `app/contenido/<materia>/<unidad>/<teoria|practica>.html` y después
se corre, dentro de `app/`:

```bash
python construir.py
```

Eso arma `app/generado/apuntes.js`, que es el único archivo que carga la página.
Nunca se edita `generado/` a mano.

## Material de cátedra

Los PDFs de la cátedra que usa el visor viven en `app/pdf/<materia>/`, una sola copia por
archivo. Son material de la facultad, subido acá solo para estudiar.

## Versiones

`0.x.y-alpha` mientras esté en desarrollo. La `1.0.0` queda reservada para cuando esté terminado.

---

by Abasto Franco
