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
- **Parciales:** `fuentes/ing2/EXAMENES/` (2024, 2025 y 2026). Mandan sobre todo lo demás: qué se
  pide y con qué palabras. El de 2026 está transcripto de fotos de la hoja de un compañero: su
  nombre y su DNI no se copian.
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

Los esquemas que no son de clases van en `<div class="pd-grafico esq" data-g="nombre"></div>` y
los genera `python fuentes/ing2/esquemas.py`, con el mismo criterio: no se dibujan a mano, se
corrigen en el script. **Primero los diagramas del apunte** (pedido de Fran, 29/10/2026: "no
creamos diagramas, eso no es la idea"): si el apunte trae un diagrama de un tema, se usa ese,
**redibujado igual** (mismas cajas, textos y flechas; si está en inglés, con la traducción entre
paréntesis), no uno inventado. El script le pone debajo a cada esquema un **rótulo de origen**:
"Diagrama del apunte de ..., pág. N" (página impresa) en verde, o "No está en el apunte: ..." en
ámbar para los propios (ciclo de vida de una métrica, pasos para definir procesos, diagnóstico de
CMMI, grafos de complejidad, comandos de Git hasta el remoto). Un cuadro del apunte que se copia
lleva el mismo rótulo a mano (`<p class="pd-pie esq-origen apunte">`). Los diagramas que trae
cada apunte (revisados página por página el 29/10/2026, imágenes y figuras dibujadas):
Calidad de software, pág. 12 (proceso con sus tres dimensiones) y 21 (pirámide y progreso
lineal de CMMI); Métricas, pág. 4 (la ficha con el ejemplo y el mapa proceso/producto/proyecto);
Gestión de cambios, pág. 5 (versionado; ramas y merge), 9 (SVN y Git), 12 (deltas e
instantáneas), 14 (las tres secciones) y 22 (SemVer, que va como tabla).

## Evaluación

- Parciales 2024, 2025 y 2026 en `evaluacion/parciales/`, una consigna por archivo, con `pd-resultados`
  (la respuesta modelo) y `pd-explicacion`. La cátedra no publicó respuestas: son propias, y así
  se avisa en la nota de cada parcial. Las respuestas modelo de patrones siguen el mismo criterio
  que la teoría: tres partes breves (qué patrón y por qué, cómo se aplica, qué se gana), con la
  frase del enunciado, cada parte del patrón explicada y todo dicho con el caso. Cuando la
  consigna pide "el propósito dentro del sistema", se dice para qué le sirve a esa empresa.
- **Preguntas fundamentales de teoría** en `evaluacion/parciales/2026-preguntas-fundamentales/`:
  no es un parcial, pero va como una tarjeta más de Parciales. Rehecha el 29/10/2026 a pedido de
  Fran, para el recuperatorio: **toda la teoría en preguntas con la forma de las del parcial 2026**
  (definir, cuadro comparativo, representar gráficamente). Diecinueve, por tema y de lo básico a lo
  específico: CMMI (los cinco niveles con el ejemplo del apunte, y un caso de nivel 2 para
  identificar y llevar al siguiente, explicado desde las definiciones), mejora de procesos (PI,
  BPI y SPI; los tres elementos; proyecto de mejora contra proyecto de software), calidad, métricas
  (definición y elementos con un ejemplo, ciclo de vida, tipos, complejidad ciclomática), gestión
  de cambios y Git (los cuatro conceptos, SVN y Git, los tres estados, ramas y merge, y desde el
  30/10/2026 por qué usar control de versiones y su evolución, características de Git, claves SSH
  con init, clone y ramas, y conflictos de merge: el profe dijo que de teoría estudien Git) y al final
  Facade en un código, resuelto como la Práctica 1 de 2026. **Sin** agentes de IA ni versionado
  semántico como preguntas sueltas (decisión de Fran). Todo cuadro o diagrama que esté en la teoría
  va en la respuesta. **Un solo nombre para cada cosa** (los niveles se llaman siempre Inicial,
  Gestionado, Definido, Cuantitativamente gestionado y En optimización continua). Cada una lleva
  `pd-resultados` con el rótulo "Respuesta" (corta, pero completa: responde cada parte de la
  consigna, en su orden) y `pd-explicacion` con "Explicación desde cero" (rápida, sin dar nada por
  sabido, con las trampas al final). Todo sale de la teoría de la unidad: si el apunte cambia, se
  revisan.
- **CMMI: 9 casos cortos** en `evaluacion/parciales/2026-cmmi-casos/` (otra tarjeta de Parciales,
  pedida por Fran el 13/10/2026 para cubrir las dos formas de consigna): casos 1 a 5, una empresa
  en cada nivel para identificarlo, justificar y decir los riesgos; casos 6 a 9, uno por escalón
  para proponer tres acciones. Van **desordenados** y el título es el nombre de la empresa, para
  que no se adivine el nivel. Las pistas, los riesgos y las acciones son los de la sección 4 de la
  teoría de calidad; el riesgo del Nivel 5 (dejar de sostener la mejora) es deducción, el apunte no
  lo da. **El riesgo de no avanzar se escribe siempre igual**, en una oración: "Como no [lo que
  define al nivel siguiente], [qué le pasa por no tenerlo]" (pedido de Fran, 13/10/2026: le costaba
  armarlo desde las definiciones). Las cuatro oraciones están en "CMMI en una hoja" (sección 7 de calidad).
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
- **Ejercicios de parcial** (modo "Ejercicios de parcial" del formulario): un ejercicio completo
  por archivo, en la carpeta de su unidad, con id `ing2-<unidad>-e-fundamental-NN-<forma>`,
  `data-tipo="ejercicio"`, `data-fundamental="NN"` (el orden en que salen, entre todas las
  unidades) y `data-rotulo` con el nombre de sus partes ("Patrón", "Párrafo", "Parte", "Punto").
  `data-titulo` es como se ofrece en el formulario ("Forma de consigna · patrones").
  Formato: el de "Ejercicio completo" de `FORMATO.md`. Los pasos son de opciones o de escribir
  la palabra clave (`data-texto`, con el nombre en inglés como alternativa): nombres de las
  partes, de la interfaz y del método, el grupo del patrón, la palabra de la definición. Cada
  parte (`data-inciso="1"`, `"2"`...) cierra con su `p-rta`: la respuesta como va en la hoja, en
  las tres partes de siempre y con la misma descripción del patrón que la teoría. Los diagramas
  propios están en `fuentes/ing2/diagramas/evaluacion.py`, angostos a propósito (van en una
  columna); los generales de cada patrón se reusan con su mismo `data-g`.
  Hay ocho, y cada patrón aparece en al menos dos formas: 01 dibujar y explicar (Factory Method
  y Facade), 02 enunciado (Composite, Abstract Factory, Strategy), 03 código (Adapter),
  04 agregar a un diagrama (Singleton y Observer), 05 dibujar y explicar (Observer y Strategy),
  06 enunciado (Singleton, Adapter, Factory Method), 07 código (Composite), 08 integrador
  (Abstract Factory en un enunciado y Adapter sobre un diagrama). Los cuatro primeros no tienen
  pasos de escribir y no se les agregan (cambiaría la cantidad de pasos de intentos guardados).

- **Practicar diagramas** (tercer modo del formulario): un archivo por patrón,
  `ing2-<unidad>-d-<patron>.html`, con `data-practica="diagrama"`. El enunciado muestra el
  diagrama general del patrón (el mismo `data-g` de la teoría: si cambia allá, hay que revisar los
  `data-oculta` de acá) y los pasos, todos de escribir, piden el patrón, las clases, los atributos
  y los métodos; las alternativas aceptan el nombre sin tipos, el de Refactoring.Guru en inglés y
  el del código de los parciales. No se preguntan los nombres de relleno (`hacerAlgo`,
  `operacionA`). Formato en `FORMATO.md` ("Diagrama para completar").

## Pendientes e ideas

- **Recuperatorio del 2do parcial** (Fran sacó 38 en el del 14/10/2026: sabía el Composite, CMMI y
  Strategy; le faltaron métricas, PI y SPI y los diagramas de teoría). El 19/10/2026 se cargó el
  parcial 2026 resuelto, la sección "CMMI en una hoja" y los esquemas de teoría que faltaban. La
  fecha del recuperatorio no se sabe todavía.

- **Ejercicios de parcial que faltan** (plan acordado el 12/10/2026): la teoría quedó como
  preguntas fundamentales en Parciales (13/10/2026, decisión de Fran: para leer y aprender, no
  como autoevaluación); si después las quiere interactivas, son los ejercicios de CMMI, Git y
  métricas. De patrones faltan más ejercicios por forma de
  consigna (un código en PHP como el del Parcial 2025, los otros patrones en cada forma).
  También quedó propuesto un estilo "como en el parcial" (escribir en la hoja y autocorregirse
  contra la respuesta modelo). En esta PC no hay `php`: un código en PHP no se puede correr acá.

- De los apuntes quedó en un párrafo o afuera lo que nunca se tomó: gestores de
  dependencias, la especificación completa de SemVer, los "juegos" de complejidad ciclomática
  (su código está en imagen) y Docker (confirmado que no entra).
- De las guías de patrones quedaron sin resolver por separado los ejercicios que repiten otro
  (Práctica 03 ej. 1 a 3, Guía 1 ej. 1 y 6, `practica 2` ej. 6): están mencionados dentro del
  ejercicio al que se parecen.
