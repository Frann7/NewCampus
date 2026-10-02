# Estructura del proyecto y flujo de trabajo

> Las rutas de este documento son relativas a `app/` (salvo que digan otra cosa).


**NewCampus**: una interfaz web de apuntes universitarios, pensada para varias materias.
Vive en `C:\Users\Fran\Desktop\NewCampus\` y se distribuye como zip.

```
NewCampus/
├── NewCampus.exe         ← doble clic: levanta el servidor local y abre el navegador
└── app/
    ├── index.html        ← esqueleto: pestañas, reloj, firma. Casi nunca se toca:
    │                        el menú de materias lo dibuja app.js solo.
    ├── construir.py      ← junta contenido/ en generado/apuntes.js
    ├── (docs/ en la raíz: la documentación por tema)
    ├── assets/           ← estilos.css, app.js (navegación, índice, visor de PDF), logo.svg
    │   ├── ventanas.js   ← sacar una pestaña a otra ventana manteniéndola apretada
    │   ├── cronometro.js ← el cronómetro de estudio de la barra de arriba
    │   ├── calendario/   ← pestaña Calendario: fechas (fijas) · eventos (del usuario)
    │   │                    · detalle (ficha del día) · agenda (próximas fechas y
    │   │                    recordatorios) · calendario (las dos vistas)
    │   ├── tareas/       ← pestaña Tareas: el tablero (tareas.js + .css)
    │   └── evaluacion/   ← pestaña Evaluación, un archivo por responsabilidad:
    │                        nucleo · banco · formulario · examen · informe · evaluacion (+ .css)
    ├── contenido/        ← LOS APUNTES SE EDITAN ACÁ
    │   ├── materias.json ← el menú lateral y el material de cátedra
    │   └── <materia>/
    │       ├── <unidad>/<teoria|practica>/               una CARPETA por pestaña:
    │       │      00-intro.html                            el título y la bajada
    │       │      01-....html, 02-....html                 un archivo por ejercicio o sección
    │       └── evaluacion/
    │           ├── parciales/<año>-<nombre>/             meta.json + un archivo por ejercicio
    │           ├── finales/<fecha>-final/               igual que un parcial
    │           └── preguntas/<unidad>/<id>.html         un archivo por pregunta
    │                        (el formato está en preguntas/FORMATO.md)
    ├── generado/         ← GENERADO. NO EDITAR. indice.js (lo unico que carga
    │                        la pagina al arrancar) + una pieza por unidad
    ├── pdf/<materia>/    ← PDFs de cátedra, una sola copia por materia
    └── lanzador/         ← código fuente de NewCampus.exe (C#) y su ícono
```

**Regla de oro del flujo de trabajo:**

1. Los apuntes se editan **solamente** en `contenido/`, y **un archivo por ejercicio o por
   sección**. Nunca vuelvas a juntar una unidad en un solo archivo: abrir 4 KB para corregir un
   ejercicio en vez de 80 KB es lo que hace que agregar contenido no se vuelva impagable.
2. Después de cada edición corrés `python construir.py` dentro de `app/`.
   No hay botón de actualizar en la página: la construcción la corrés vos.
3. Nunca edites `generado/apuntes.js`: se pisa en la próxima construcción.
4. Cada vez que se agrega o se cambia una funcionalidad, **se actualiza el `README.md`**
   de la raíz en el mismo commit. Es la cara del repositorio: tiene que decir siempre lo
   que la aplicación hace hoy.

Los fragmentos se escriben **al margen, sin `<section>` ni sangría**: `construir.py` los pega en
orden de nombre, los indenta y los envuelve en el `<section class="pane" data-view="...">` que
espera la página, sacando el `data-view` de la carpeta.

El número con el que arranca cada nombre es su **orden**, no el número del ejercicio (hay unidades
con dos guías y numeración repetida). Para meter algo entre el 03 y el 04 alcanza con llamarlo
`03b-...`; para reordenar, renombrar.

Cada `.bloque` de teoría y cada `.ej` de práctica se convierte **solo** en un desplegable: app.js
le arma la cabecera con el `.kicker`/`.tag` y el `<h2>`, y esconde el resto. Los fragmentos de
`contenido/` se siguen escribiendo igual que siempre, sin envoltorios. Arriba del todo quedan
**Abrir todo** y **Cerrar todo**. En el índice de la derecha, cada sección lleva su propia flechita:
**la flecha pliega y despliega** (lo mismo que desde la página) y **el texto solo lleva** al título,
sin abrir nada.

**Marcas de examen.** El fragmento puede decir que ese ejercicio (o esa sección de teoría) ya fue
tomado, con atributos en su elemento raíz (`.ej` o `.bloque`):

```html
<div class="ej" data-examen="igual"
     data-examen-ref="Parcial 2023 · ej. 4"
     data-examen-nota="Qué cambia respecto del examen (opcional).">
```

* `data-examen="igual"` &rarr; ★, tal cual como lo tomaron **en un parcial**; cambian los números y nada más.
* `data-examen="variante"` &rarr; ◈, el mismo tema con un cambio (otra fórmula, un inciso de más),
  **o algo que solo tomaron en finales**. Lo de final nunca es dorado: el dorado es para preparar
  el parcial. Si un tema aparece en un parcial y también en finales, manda el parcial.
* Sin atributo: no apareció en los exámenes que están cargados. **No** quiere decir que no pueda
  caer, y la leyenda que dibuja app.js lo aclara.

app.js pone el chip en la cabecera, el glifo en el índice de la derecha, la nota arriba del cuerpo
al abrir la sección, y una barra de filtro **Todo / ★ Tomados / ◈ Variantes y finales** que esconde el resto.
La marca se escribe **mirando los exámenes transcriptos**, nunca de memoria: si se suma un parcial
nuevo hay que repasar las marcas.

Al arrancar, la página solo carga `generado/indice.js`, que dice qué hay y en qué archivo está.
El contenido de cada unidad llega en su propia pieza cuando la abrís (con un `<script>`, no con
`fetch()`, para que también funcione con `file://`). Para analizar o editar un tema, leé
únicamente su fragmento de `contenido/`.

## Cosas que rompen el proyecto (no las hagas)

* **Fórmulas:** MathJax con `\( ... \)` y `\[ ... \]`. **Nunca** `$`, porque hay precios en el texto.
* **Los apuntes no se cargan con `fetch()`**: cada pieza de `generado/` entra con un `<script>`, que es lo único que `file://` deja hacer. Los únicos `fetch()` son el latido a `api/ping` y el número de corrida.
* **Nada de `<` crudo** en el texto: usá `&lt;` o `\leq` dentro de la fórmula.
* **Las fórmulas se tipografían al abrir, no antes.** MathJax mide mal lo que está oculto, así que
  el cuerpo de una sección cerrada no se toca. Y la marca de "esto ya se tipografió" **no puede
  llamarse `data-mjx...`**: MathJax ignora cualquier elemento que tenga un atributo así (se llama
  `data-tipografiado`).
* **Nada que comunique un estado por transición o animación CSS.** Hay entornos donde se congelan.
  Si algo indica abierto/cerrado/activo, el valor final tiene que quedar aplicado por JS o por
  una clase, no por un `transform` animado.
* No agregues dependencias ni frameworks. Es HTML, CSS y JS a mano, más MathJax por CDN.
* Ante la duda, la versión más corta. Sin agregados innecesarios.

## Para agregar una materia o una unidad nueva

**No se toca `index.html`.** Todo el menú sale de `contenido/materias.json`:

1. Crear los fragmentos en `contenido/<materia>/<unidad>/<teoria|practica>/`.
2. En `contenido/materias.json`, agregar la materia (o la unidad, si la materia ya está) con su
   `nombre`, su `corto` —el nombre que entra en el cuadrito de un día del calendario— y el `num` y
   `nombre` de cada unidad. El orden de la lista es el del menú, y define el color en el calendario.
3. Si tiene PDFs de cátedra: copiarlos **una sola vez** a `pdf/<materia>/`, listarlos en el `pdf` de
   esa materia y decir en `material` a qué unidades se les muestran (`evaluacion` es la pestaña).
4. Correr `python construir.py`.

Una materia **sin apuntes todavía** aparece como "pronto" sola, sin hacer nada: alcanza con que esté
en la lista. Una unidad que tenga apuntes pero no esté en `materias.json` la marca como REVISAR.
