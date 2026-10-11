# Ingeniería de Software II (ing2) — cómo se escribe su contenido

Las reglas generales están en `docs/contenido.md` (raíz del repo); acá va solo lo propio de Ing. II.
El plan de carga, con lo que sube cada parte y lo que falta, está en `docs/plan-ing2.md`.

## Fuentes y alcance

- **Alcance:** el **2do parcial** (segundo cuatrimestre): los 8 patrones de la cátedra (Singleton,
  Factory Method, Abstract Factory, Adapter, Composite, Facade, Observer, Strategy), calidad y
  CMMI, métricas, gestión de cambios y Git. Docker no entra. El 1er cuatrimestre tampoco.
- **Texto extraído:** `fuentes/ing2/` (raíz del repo), con su `INDICE.md`. Primero el texto; el PDF
  (`C:\Users\Fran\Desktop\SISTEMAS 3\ING 2\SEGUNDO CUATRIMESTRE\`) solo en las páginas ⚠, que son
  los diagramas. `fuentes/ing2/PATRONES/TEORIA/` está solo en esta PC (no en el repo).
- **Parciales:** `fuentes/ing2/EXAMENES/` (2024 y 2025). Mandan sobre todo lo demás: qué se pide y
  con qué palabras.
- La unidad **Base** (`base`) no sale de un apunte de la cátedra: es lo mínimo de UML de clases y
  de C++ para poder leer el resto. Fran arranca de cero.

## Cómo se escribe

- **Cada patrón, una sección de teoría con esta forma:** Para qué sirve (el problema, sin jerga) →
  Estructura (diagrama UML + tabla "qué es cada parte") → El mismo ejemplo en C++, línea por línea
  → Cómo reconocerlo (en un enunciado / en código) → Ventajas y desventajas → Dónde se usa (2 o 3
  ejemplos: los piden) → Ejemplo 1 en C++ → **los cinco ejemplos con formato de parcial** →
  Errores y trampas (`.caja.caja-ojo`).
- **Los cinco ejemplos con formato de parcial**, en todos los patrones, con este número y este
  título:
  - 2 "dibujarlo y explicarlo": diagrama, descripción de su usabilidad y dos ejemplos; cada
    ejemplo es el caso en negrita más una o dos oraciones que digan por qué ahí va el patrón,
    nunca una frase suelta.
  - 3 "aplicarlo a un enunciado": desarme, diagrama y **justificación en tres partes** (qué
    patrón y qué frase lo pide, cómo queda armado en este caso, qué se gana).
  - 4 "identificar los patrones de un enunciado": tres párrafos con tres patrones (el de la
    sección y otros dos), tabla párrafo → necesidad → frase → patrón; la respuesta como se
    escribiría en el parcial: el patrón de la sección en las tres partes de siempre (qué patrón y
    por qué, cómo se aplica, qué se gana) y los otros dos en dos oraciones cada uno; el diagrama del
    patrón de la sección (solo ese, aunque la consigna no lo pida), y las trampas.
- **Toda respuesta modelo es una respuesta de parcial:** breve, pero completa. "Qué patrón y por
  qué" nunca son tres palabras: lleva el patrón, su tipo, cuándo se usa dicho con el caso y la
  frase del enunciado. "Cómo se aplica" nombra solo las piezas clave (una o dos oraciones), no
  una tabla con todas las clases y métodos. Ni un párrafo denso ni un listado exhaustivo: Fran
  las estudia de cero y las tiene que poder escribir (dos correcciones suyas, 11/10/2026).
  - 5 "reconocerlo en un código": C++ con los renglones que lo delatan resaltados, tabla
    renglón → parte del patrón y respuesta.
  - 6 "agregarlo a un diagrama": diagrama dado, qué hay, qué se cambia en orden, diagrama
    modificado, justificación y "a tener en cuenta".
- **Una sola descripción por patrón.** La del ejemplo 2 tiene tres oraciones: cuándo se usa, cómo
  funciona y qué se gana. Toda justificación (ejemplos 3, 4 y 6, y la sección de repaso) es esa
  misma descripción con las palabras generales cambiadas por los nombres del caso, más la frase
  del enunciado entre comillas, textual. No se inventan frases nuevas para decir lo mismo: Fran
  se pierde cuando la explicación cambia de un ejemplo a otro (11/10/2026).
- **Cada parte del patrón que se nombra, se explica.** En una respuesta modelo no va "Agencia es
  el creador" a secas: va "Agencia es el creador (la clase que necesita el pasaje pero no decide
  cuál se crea)". Una aclaración corta entre paréntesis, dicha con el caso, la primera vez que
  aparece cada parte en esa respuesta (creador, producto, fábrica abstracta, familia, adaptador,
  servicio, componente, hoja, compuesto, fachada, subsistema, notificador, suscriptor, estrategia,
  contexto). La respuesta del ejemplo 5 (código) lleva las mismas tres partes que las demás:
  qué patrón y por qué (con lo que lo delata), cómo está aplicado y qué se gana.
- **En la teoría no va el enunciado de ningún parcial** (pedido de Fran, 11/10/2026): los
  parciales quedan en Evaluación, para rendirlos sin haberlos visto. Los ejemplos salen de las
  **guías de la cátedra** (primero las que no están resueltas en la Práctica) y, si no hay,
  son inventados lo más parecidos posible. Tampoco se citan frases textuales de los parciales en
  las tablas de "cómo reconocerlo". El rótulo de cada consigna dice de dónde sale: "Guía N°1 ·
  ejercicio 1", "Práctica 03 · ejercicio 1" (de la guía, tal cual) o "Inventado · ...". Las
  marcas ★ y las guías de lectura sí dicen qué se tomó y con qué forma, sin resolverlo.
  El código inventado lleva los nombres de método de Refactoring.Guru (`GetInstance`, `Attach`,
  `Notify`, `Request`...) con las clases rebautizadas, como hace la cátedra.
- **Nombres de las partes** como en el apunte de la cátedra (Refactoring.Guru en castellano:
  Creador, Producto, Fachada, Notificador, Suscriptor, Contexto, Estrategia...) y entre paréntesis
  el nombre en inglés que aparece en el código de los parciales (`Subject`, `Observer`, `Target`).
- La teoría se escribe con **palabras propias**; del libro no se copian párrafos.
- **Todo código C++ se compila y se corre** antes de escribirlo: `g++ -std=c++14 -Wall` (MinGW 6.3,
  en el PATH; no tiene `std::thread`), con el archivo en el scratchpad. La salida que se muestra es
  la que dio.
- **Estilo del C++:** el de los parciales (el de Refactoring.Guru): atributos con guion bajo al
  final (`saldo_`), punteros crudos con `new`/`delete`, `std::string`, `std::cout`, `override`.
- **El programa de cada ejemplo va por partes** (`.cod-partes`, ver `docs/contenido.md`): una
  parte por pieza del patrón, con su título, su rol y los renglones clave resaltados
  (`data-clave`), y `data-desde` para que la numeración siga la del programa completo. Nunca un
  bloque de 60 líneas seguido de una tabla. El código de un **enunciado** (práctica, parciales)
  va entero y sin resaltar, para no regalar la respuesta.
- **Código en el HTML:** `<pre class="codigo"><code>...</code></pre>` y la salida en
  `<pre class="salida">...</pre>`. Dentro del código, `<` va como `&lt;`, `>` como `&gt;` y `&`
  como `&amp;` (`#include &lt;iostream&gt;`, `std::cout &lt;&lt; x`, `a-&gt;hablar()`).
- **Práctica:** los ejercicios de las guías de la cátedra, resueltos como se entregarían: qué
  patrón, la frase del enunciado que lo justifica, el diagrama dibujado y, si hay código, las
  señales que lo delatan.
- **Marcas de examen:** ★ (`data-examen="igual"`, `data-examen-ref="Parcial 2025 · Teoría 4"`) en
  lo que tomó un parcial casi tal cual; ◈ (`variante`) en lo que tiene la misma forma de consigna
  con otro patrón u otro caso. **La práctica también se marca** (casi todos los ejercicios son
  una consigna de parcial con otro caso). La marca dice "esto se tomó", no "esta resolución es
  de la cátedra": la cátedra no publicó ninguna resolución (se buscó en la carpeta de la materia
  y en el campus virtual el 10/10/2026).

- **Colores con significado** (clases en `docs/contenido.md`): ventajas y desventajas en
  `table.t.full.pros`; los niveles de CMMI siempre con la misma etiqueta (`.et mal` el 1, `.et ojo`
  el 2, `.et dato` el 3, `.et` el 4, `.et ok` el 5); los estados de Git, `.et mal` modificado,
  `.et ojo` preparado, `.et ok` confirmado; el grupo de un patrón, `.et` creacional, `.et dato`
  estructural, `.et vio` de comportamiento.

## Diagramas UML

El color de cada caja lo pone `uml.py` solo: gris la clase común, violeta la interfaz
(`estereo="interface"`), celeste la abstracta, que además lleva sola el rótulo «abstract» (la
cursiva del nombre no alcanza para verla), y cabecera llena la `destacada` (la clase principal
del patrón). Los símbolos `+ - #` salen en verde, rojo y ámbar.

No se dibujan a mano: se describen en `fuentes/ing2/diagramas/<unidad>.py` y
`python fuentes/uml.py fuentes/ing2/diagramas/<unidad>.py` (desde la raíz del repo) mete el SVG en
cada `<div class="pd-grafico uml" data-g="nombre"></div>` de los fragmentos. El formato está
explicado arriba de `fuentes/uml.py`. Para corregir un diagrama se cambia su descripción y se
vuelve a correr; el SVG del fragmento no se edita. El mismo diagrama puede ir en varios lugares (el
mismo `data-g`): un ejemplo que lo lee o lo pide lo **muestra de nuevo ahí**, no manda a mirarlo
más arriba. Después de generarlos se mira **cómo quedaron**
(captura): que no se pisen cajas ni líneas.

## Evaluación

- Parciales 2024 y 2025 en `evaluacion/parciales/`, una consigna por archivo, con `pd-resultados`
  (la respuesta modelo) y `pd-explicacion`. La cátedra no publicó respuestas: son propias, y así
  se avisa en la nota de cada parcial. Las respuestas modelo de patrones siguen el mismo criterio
  que la teoría: tres partes breves (qué patrón y por qué, cómo se aplica, qué se gana), con la
  frase del enunciado, cada parte del patrón explicada y todo dicho con el caso. Cuando la
  consigna pide "el propósito dentro del sistema", se dice para qué le sirve a esa empresa.
- **Banco de autoevaluación** en `evaluacion/preguntas/<unidad>/` (una carpeta por unidad del
  menú, un archivo por pregunta, ids `ing2-u0-NN`, `ing2-u4a-NN`, `ing2-u4b-NN`, `ing2-u4c-NN`,
  `ing2-u5-NN`, `ing2-u6-NN`: el orden alfabético de los ids es el orden en que salen). Evaluación
  simple (`"evaluacion": {"tipo": "simple"}` en `materias.json`) con elección de temas. Formato:
  `app/contenido/pye/evaluacion/preguntas/FORMATO.md`, 1ra etapa (`opcion`, `multiple`,
  `completar` con desplegables o número).
- Las preguntas son **inventadas** (el parcial no se repite) y copian la forma de sus consignas;
  la fuente lo dice ("Inventada · estilo Parcial 2025, Práctica 2"). Todo programa de C++ de una
  pregunta va completo, compilado y corrido, sin comentarios ni nombres que delaten el patrón.
  Las opciones de un desplegable van siempre en el mismo orden (alfabético) dentro de la pregunta.

## Pendientes e ideas

- De los apuntes quedó en un párrafo o afuera lo que nunca se tomó: claves SSH, gestores de
  dependencias, la especificación completa de SemVer, los "juegos" de complejidad ciclomática
  (su código está en imagen) y Docker (confirmado que no entra).
- De las guías de patrones quedaron sin resolver por separado los ejercicios que repiten otro
  (Práctica 03 ej. 1 a 3, Guía 1 ej. 1 y 6, `practica 2` ej. 6): están mencionados dentro del
  ejercicio al que se parecen.
