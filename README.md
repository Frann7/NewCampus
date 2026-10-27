# NewCampus

Campus de apuntes orientado a la carrera **Analista en Sistemas de Información** (por ahora,
solo tercer año). Corre **en local**: un ejecutable levanta un servidor en tu propia máquina y
abre los apuntes en el navegador. No hay nube ni cuenta: lo único que se trae de internet son las
fórmulas (MathJax) y las tipografías. Tus datos no salen de tu máquina.

> **Versión en desarrollo (alpha).** Está a medio hacer y cambia seguido. Todavía no es una
> versión pensada para descargar y usar en serio.

## Qué tiene hasta ahora

* **Apuntes por materia y unidad**, con pestañas de **Teoría** y **Práctica**.
  Con contenido, por ahora, Probabilidad y Estadística (unidades 4 a 7) y Programación Avanzada,
  que va por **clases** (1 a 6: PHP, arreglos y cadenas, HTML y formularios, JavaScript y API REST,
  sesiones, mysqli), con el código de cada ejemplo, qué hace cada línea y qué imprime. Empezó
  Ingeniería de Software II (2do parcial): una unidad base (cómo se lee y se dibuja un diagrama
  de clases UML y lo mínimo de C++ para reconocer un patrón de diseño en un código) y los
  ocho patrones de la cátedra (creacionales, estructurales y de comportamiento), cada uno con su diagrama, su ejemplo en C++ línea por línea, cómo
  reconocerlo y una consigna de parcial resuelta, más calidad de software, CMMI, métricas y Git.
  Paradigmas y Lenguajes (parcial de autómatas): una unidad por cada ejercicio del parcial
  (AF → ER, ER → AFD mínimo con Thompson, subconjuntos y minimización, y diseñar un AF y su ER),
  con teoría corta, muchos ejemplos y cada autómata dibujado paso a paso. Bases de Datos
  (2do parcial: SQL): la teoría que toman (DDL y DML, transacción, claves), del DER a las tablas
  en 3FN, `CREATE TABLE` y consultas con `JOIN`, `GROUP BY` y fechas, con el código SQL
  coloreado y los diagramas entidad-relación dibujados con la notación de la cátedra.
  Sistemas Operativos (Práctica) tiene, por ahora, solo Evaluación: en el menú, su única entrada
  lleva directo a los parciales y a una autoevaluación con las preguntas del segundo parcial 2025
  y del probable (se elige cuál o los dos). El resto de las materias de tercer año ya están en el menú como
  "pronto".
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
    resultado de cada inciso; en principiante, cada cuenta chica. **Saltear** un ejercicio lo deja
    para después: antes de terminar se puede retomar donde quedó (al final aparece la lista de los
    salteados), y solo figura como salteado en el informe si se termina sin completarlo. Cada paso tiene, además de la **pista**, un botón **Resolver**: muestra la resolución
    de ese paso explicada (qué se pide, cada cuenta con su porqué y qué significa el resultado) y
    pasa al siguiente. Las respuestas de los pasos se muestran como se anotan en la hoja
    ("z = 0,84", "P(X ≥ 1) = 1 − P(X = 0) = 0,7769"), no como números sueltos; en los pasos de
    opciones que se escriben con fórmulas, debajo de la opción dice "En la hoja: P(X > 90) = 1 − P(X ≤ 90) = 1 − F(z)". No gasta vidas, pero el ejercicio ya no cuenta como "sin errores" y el
    informe dice qué pasos resolvió el campus. Las autoevaluaciones ya creadas lo tienen también.
    En principiante y medio, debajo del enunciado aparecen los **datos del ejercicio**: la variable
    en palabras y cada dato (media, varianza, desvío, n, p...) con la frase de donde sale.
    El **enunciado queda siempre a la vista**: en pantallas anchas va en una columna fija al
    costado de los pasos, y los pasos ya hechos se achican a un renglón (consigna y respuesta)
    que se despliega para ver su explicación; los que resolviste vos tienen además
    "📖 Ver resolución", la misma explicación completa que da Resolver (sin que cuente como resuelto por el campus). Al terminar cada inciso aparece su **Rta.**: la
    respuesta final en palabras, como se escribe en el parcial ("la probabilidad de que ... es
    0,7769, o sea un 77,69 %"). También figura en el informe. Con "← Ver el ejercicio anterior"
    se vuelven a mirar los ejercicios ya hechos, tal como quedaron (sin poder cambiarlos), y un
    botón vuelve al que está en curso.

  En el interactivo, la casilla **"Solo tal cual del parcial"** deja solo los ejercicios que están
  exactamente como vinieron en un parcial (sin los inventados parecidos ni los de finales), y deja
  elegir **qué parcial**: todos mezclados, o uno entero (2025 o 2023) en el orden del examen, cada
  ejercicio desglosado en pasos. Con un parcial elegido, las unidades y la cantidad se ponen solas.

  La casilla **"Ejercicios fundamentales (plan de urgencia)"** deja solo 4 o 5 ejercicios por
  unidad, hechos con la forma del Parcial 2025, que cubren las variantes que pueden tomar (en la
  binomial: exactamente, al menos, a lo sumo, menos de, ninguno...; en la U4, la versión que suma
  y la que integra; en la U7, intervalos con z y con t de Student). Salen todos los de las unidades
  elegidas, en cada unidad del más probable al menos probable (lo que más se repite en los
  parciales 2025 y 2023, sobre todo el 2025, en los finales y en las guías va primero). No va junto con "Solo tal cual del parcial".

  La **1ra etapa** tiene dos formatos. **En hoja** (el de ahora, por defecto): 10 preguntas de
  opción múltiple (puede haber varias correctas) y verdadero o falso, sin completar. **Virtual**:
  como el Cuestionario del Aula Virtual, con completar. Las preguntas imitan esa instancia:
  teoría, planteos, verdadero o falso y cuentas de un paso, no copias chicas de los ejercicios
  del parcial. Las viejas que se parecían demasiado quedan retiradas (`data-retirada`): no salen
  en intentos nuevos, pero los intentos guardados las siguen mostrando. La casilla **"Modo
  urgente"** deja solo las preguntas fundamentales de teoría (demostraciones de esperanza,
  varianza y covarianza, independencia, correlación, condiciones de cada modelo, la normal, la
  t), todas las de las unidades elegidas, de la más probable a la menos. Con **"Corregir cada pregunta
  al responderla"**, cada pregunta tiene un botón Comprobar: dice si está bien, marca la correcta y
  muestra la explicación, y la pregunta queda fija; al terminar sale la nota como siempre. Además, cada
  pregunta tiene **"📖 Resolver"**: muestra la respuesta correcta y la explicación sin contestar;
  la pregunta queda fija y vale 0.

  En los fundamentales del interactivo, el cuadro de datos termina con el **planteo en la hoja**:
  la variable, si es discreta o continua y el modelo con la notación de la cátedra
  (X ~ N(μ, σ), con el desvío).

  En Normal hay además una **navegación libre** opcional: casillas para saltar a cualquier
  pregunta, saltear y volver, y terminar cuando quieras. Todas las preguntas
  salen de los exámenes: cada una dice de qué parcial o final viene, con ★ o ◈, y al sortear salen
  más las de parciales.
* **Qué entró en el examen**: cada ejercicio de la guía y cada sección de teoría puede venir marcada
  con ★ (tal cual como lo tomaron en un parcial) o ◈ (el mismo tema con un cambio, o algo que
  solo tomaron en finales), diciendo en qué examen apareció y qué cambia. La marca se ve en la tarjeta y en el índice lateral, y una barra de filtro
  deja a la vista solo lo marcado, para estudiar primero lo que ya tomaron.
* **Evaluación de Programación Avanzada**, más simple que la de PyE: el **Parcial PHP**
  transcripto, con la respuesta y la explicación de cada pregunta, y autoevaluaciones que son
  ese parcial entero como en el Aula Virtual (las 20 preguntas en orden, con cuenta regresiva de
  40 minutos que se puede cambiar, nota sobre 100 y la revisión explicada). Sin etapas, modos ni
  elección de clases.
* **Evaluación de Ingeniería de Software II**: las **preguntas fundamentales de teoría** (14
  preguntas de CMMI, Git, métricas, agentes de IA y calidad, de la más probable a la menos, cada una con la
  respuesta corta para aprender y la explicación desde cero), **9 casos cortos de CMMI** (cinco
  empresas para identificar el nivel, una por nivel, y cuatro para decir cómo subir al siguiente),
  los parciales 2024, 2025 y 2026 resueltos y
  autoevaluaciones **por temas**: se eligen las unidades (base, creacionales, estructurales, de
  comportamiento, calidad y CMMI, Git) y corre todas las preguntas de esos temas, con cuenta
  regresiva, nota sobre 100 y la explicación de cada una. Son 67 preguntas con la forma de las
  consignas del parcial: qué patrón aplica un código en C++, qué patrón pide un enunciado, las
  partes de cada diagrama, en qué nivel de CMMI está una empresa, la ficha de una métrica, la
  secuencia de comandos de Git y el versionado semántico. Además, al armar la autoevaluación se
  puede elegir el modo **Ejercicios de parcial**: ocho ejercicios de patrones con las formas de
  consigna de los parciales (dibujar y explicar dos patrones, identificar los patrones de un
  enunciado, reconocer el patrón de un código, agregar patrones a un diagrama y un integrador que
  mezcla dos formas), y se elige cuáles hacer. Cada uno se desglosa en pasos con pista y
  resolución: unos de elegir y otros de **escribir la palabra clave** (el nombre de una parte del
  diagrama, de la interfaz o del método, o la palabra que define al patrón; no importan las
  mayúsculas ni las tildes, y vale el nombre en inglés). Al final de cada parte queda la
  respuesta como se escribe en la hoja. Cada patrón aparece en al menos dos formas. Sin vidas ni
  niveles, y con el tiempo libre o con contador. El tercer modo es **Practicar diagramas**: el
  diagrama UML de cada uno de los ocho patrones con la estructura ya dibujada (cajas, flechas,
  rombos, estereotipos) y los nombres tapados con un número. Se escribe de qué patrón es y,
  paso a paso, el nombre de cada clase, los atributos y los métodos con sus tipos; el dibujo se
  va completando a medida que se acierta. Cada paso tiene pista y resolución, el diagrama se
  puede saltear, y salen mezclados para no saber cuál viene.
* **Índice lateral con subíndices**: en la práctica, cada ejercicio abierto lista debajo sus
  pasos e incisos, y tocar uno lleva directo a ese inciso.
* **Tareas**: un tablero con tres columnas, **Pendientes**, **En proceso** y **Hecho**, en el
  menú lateral arriba de las materias, junto al Calendario, y también en la fila de pestañas,
  después de Evaluación (uno solo para todo el campus). Cada tarea es un cuadrito:
  se agrega al pie de su columna, se edita con el lápiz (o doble clic), se borra con la ✕ y se pasa
  de columna con las flechas o arrastrándola; arrastrando también se reordena. Al agregarla o
  editarla, entre Cancelar y Agregar se elige si es de una **materia**: toma su color (el mismo
  que en el calendario) y lleva su nombre; si se deja en "Sin materia" es una tarea general. Entran hasta **25
  tareas por columna** (con la columna llena no se agrega ni se mueve nada a ella) y hasta 300
  caracteres por tarea.
* **Calendario** (en el menú lateral y en la fila de pestañas): un mes a pantalla completa con flechas para navegar, o el año entero.
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
* **Visor de PDFs** de cátedra en ventanas movibles. Mientras hacés una autoevaluación, abajo a
  la derecha aparece el material de las unidades que entran en ella (por ejemplo, la hoja de
  fórmulas de la U4 o la Tabla IC-PH de la U7); al salir vuelve el de Evaluación.
* **Ventanas duplicadas**: manteniendo apretada una pestaña sale una copia de ese apartado en
  otra ventana, para leer dos partes a la vez. Manteniendo apretada una **unidad del menú** sale
  una copia de solo esa unidad, con sus pestañas Teoría y Práctica: sirve, por ejemplo, para
  consultar otra unidad en medio de una autoevaluación sin salir de ella.
* **Cronómetro de estudio**: en la barra de arriba, al lado del reloj. Le ponés los minutos que
  quieras (o elegís uno de los sugeridos), la cuenta regresiva aparece en ese mismo lugar, y cuando
  llega a cero sale un cartel para cortar, repetir el mismo tiempo o poner otro. Pensado para
  trabajar de a tandas: 30 minutos de estudio, 5 de descanso.
* **Contenido al costado o centrado**: por defecto los apuntes van pegados al menú. El botón
  chico ⇤ ⇥ de arriba, al lado del modo claro/oscuro, los centra cuando sobra lugar (pantalla
  ancha o menú plegado); se recuerda.
* **Menú de materias plegable**: la manija redonda en el borde del menú (o Ctrl+B) lo esconde para
  dejar toda la pantalla a los apuntes, y se recuerda entre visitas.
* **Animaciones suaves**: los apartados y las secciones entran subiendo unos píxeles, los botones
  rebotan al apretarlos y las tarjetas se levantan al pasar el mouse. Son solo de movimiento (nada
  depende de que corran) y se apagan si el sistema pide reducir el movimiento.
* Modo claro / oscuro, y arriba a la derecha tres medidores juntos y separados entre sí: la hora de
  Argentina, el tiempo que llevás en la página y el cronómetro.

## Tus datos (no se pierden al actualizar)

Lo que cargás vos —fechas del calendario, autoevaluaciones y sus informes, las tareas, el
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

## Actualizaciones

Si bajaste el campus con `git clone`, **`NewCampus.exe` se fija solo si hay cambios nuevos** cada
vez que lo abrís (con internet y si no había otro NewCampus abierto). Si los hay, sale un cartel
con la lista de lo nuevo: "¿Querés actualizar ahora?".

* **Sí:** hace `git pull` y, si la actualización trae un `NewCampus.exe` nuevo, abre ese y se cierra
  el viejo. Al abrir, un globito junto al reloj dice cuántos cambios se bajaron.
* **No:** abre la versión que tenés; la próxima vez vuelve a preguntar.
* Tus datos no se tocan: están fuera del repositorio (ver arriba).
* Si algo falla (por ejemplo, cambiaste a mano un archivo que la actualización también cambia),
  no se toca nada: se abre la versión que tenías y el cartel dice lo que pasó.

Hace falta tener [Git](https://git-scm.com/download/win) instalado. Si bajaste el campus como
ZIP, no se puede actualizar solo: bajalo de nuevo o clonalo con git.

## Qué necesitás para correrlo

| Para | Necesitás |
| :--- | :--- |
| Usarlo | Windows con .NET Framework 4 (ya viene instalado), un navegador predeterminado y conexión a internet para las fórmulas |
| Actualizarse solo | Git, y haber bajado el campus con `git clone` |
| Editar los apuntes | Python 3 (para `app/construir.py`) |
| Recompilar el ejecutable | `csc.exe` del .NET Framework 4 (el comando está arriba de `app/lanzador/NewCampus.cs`) |

Doble clic en `NewCampus.exe`: levanta el servidor en `http://localhost:47800` y abre el
navegador. Antes revisa que esté todo lo necesario y, si falta algo, lo dice en un solo
cartel con lo que hay que instalar: un navegador, la conexión a internet (las fórmulas se cargan
de ahí) o Python 3 si faltan los apuntes generados (y si Python está, los genera solo). También
revisa que esté cada archivo que nombra `app/generado/indice.js`: lo que falte lo vuelve a sacar
de git y, si no alcanza, lo arma con Python; si igual falta, lo dice en el cartel. El .NET
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

* **0.57.0-alpha** — SO Práctica: la autoevaluación suma las 20 preguntas del **segundo parcial
  probable**, y en el formulario se elige con qué parcial practicar (o los dos). En una materia
  sin unidades, los temas para elegir son las carpetas de su banco, con el nombre del parcial.
* **0.56.0-alpha** — SO Práctica: **autoevaluación** con las 20 preguntas del segundo parcial 2025
  como cuestionario del Aula Virtual (opción múltiple, V/F y emparejar con desplegables, con sus
  capturas), nota sobre 100 y la explicación de cada una en la revisión. Arreglado: en una materia
  sin unidades, "Nueva autoevaluación" fallaba al leer la entrada Evaluación del menú como unidad.
* **0.55.0-alpha** — Sistemas Operativos (Práctica), solo Evaluación: el **primer parcial 2026** y
  el **segundo parcial 2025** (20 preguntas del Aula Virtual cada uno, con sus capturas de htop,
  lscpu, df y RAID) resueltos pregunta por pregunta, y un **segundo parcial probable** de 20
  preguntas nuevas con la misma forma (dibujos de RAID 4, 6 y 10 y de htop, salidas de free, lscpu
  y df). Una materia que tiene evaluaciones pero no apuntes ya no queda como "pronto": su entrada
  del menú abre la Evaluación.
* **0.54.3-alpha** — Bases de Datos, parcial 2025, ejercicio 5: cada consulta se explica renglón
  por renglón en el mismo orden en que está escrita, con lo que hace cada uno sobre los datos de
  ejemplo, y antes se aclara que País, Provincia y Ciudad son tablas propias (por la 3FN) y cómo se
  encadenan los JOIN.
* **0.54.2-alpha** — Bases de Datos, parcial 2025: el ejercicio 3 trae un repaso de los tipos de
  atributo (multivaluado y compuesto, dibujados como la cátedra), de dónde va cada clave según la
  relación y qué quiere decir (PK)(FK); los ejercicios 4 y 5 explican SQL desde cero, palabra por
  palabra, con cada consulta armada de a una pieza sobre datos de ejemplo y su resultado.
* **0.54.1-alpha** — Paradigmas y Lenguajes: el ejercicio 3 (diseñar un autómata) se responde
  siempre con un **AFND**, en la práctica de la Unidad 4 y en los cinco parciales: sin estado
  muerto (una flecha que falta es que la cadena muere, mostrado con un ejemplo) y adivinando donde
  simplifica. La teoría de la U4 lo explica y suma la versión AFND de "termina con" y "contiene".
* **0.54.0-alpha** — Ingeniería de Software II, para el recuperatorio: el **parcial 2026** resuelto
  (el Composite con su UML, CMMI, métricas, PI y SPI, el ciclo de vida de una métrica, Strategy y
  la arquitectura de SVN y Git), una sección nueva de teoría, **CMMI en una hoja** (niveles,
  pistas, riesgos, acciones y cómo se responde), el cuadro de PI y SPI con objetivo, ámbito y
  ejemplo, y diez diagramas nuevos en la teoría de calidad y Git (ciclo de vida de una métrica,
  SVN y Git, cómo se definen los procesos y sus tres elementos, el diagnóstico de CMMI, el grafo de
  la complejidad ciclomática, los comandos de Git y una rama con su merge), generados por
  `fuentes/ing2/esquemas.py`.
* **0.53.2-alpha** — Bases de Datos, Unidad 2: cómo se normaliza paso a paso, con la dependencia
  funcional y los dos ejemplos de la cátedra (el alquiler de películas y la factura), y cinco
  ejercicios nuevos resueltos como en clase: normalizar las tablas de la Guía 4 y la biblioteca de
  la Guía 5 de punta a punta, con su DER. La transacción queda con las tres propiedades de la
  presentación de la cátedra.
* **0.53.1-alpha** — Bases de Datos, ajustado a las clases grabadas: la teoría queda solo con lo
  de la cátedra que se toma (la transacción, con la definición de sus diapositivas), los
  `CREATE TABLE` con las claves con nombre (`CONSTRAINT PK_...`), y en consultas `LEFT JOIN`,
  `DATEDIFF`, subconsultas y la práctica de las guías 9 y 10 como la resolvieron los profes. Las
  preguntas fundamentales pasan a 7 y los parciales de práctica suman un inciso con `LEFT JOIN`.
* **0.53.0-alpha** — **Bases de Datos**: alta de la materia con el 2do parcial (SQL), en cuatro
  unidades: teoría del 2do parcial (qué es SQL, DDL y DML, transacción y ACID, claves, archivo
  indexado), del DER a las tablas en 3FN, `CREATE TABLE` y consultas (de `SELECT` a los tres
  listados del parcial). Teoría corta con la respuesta para la hoja y práctica de las guías 9 y 10.
  En Evaluación, el 2do parcial 2025 resuelto, las 10 preguntas fundamentales de teoría, dos
  parciales de práctica inventados y dos finales resueltos. El código SQL se colorea solo (también
  el de Programación Avanzada) y los DER los dibuja `fuentes/der.py`.
* **0.52.2-alpha** — Paradigmas y Lenguajes: las expresiones regulares se leen mejor. Cada nivel
  de paréntesis tiene su color (el que abre y el que cierra iguales), la `|` va separada y la `*`
  arriba, como en la hoja; en las respuestas, más grandes.
* **0.52.1-alpha** — Paradigmas y Lenguajes, técnicas para la hoja: la tablita de entradas y
  salidas para eliminar estados (y la cuenta para elegir cuál va primero, con el ejemplo de la
  Unidad 2 rehecho en ese orden), la lista de flechas con letra para los mueve, dos atajos de la
  minimización y "pensar por ramas" en la Unidad 4.
* **0.52.0-alpha** — **Paradigmas y Lenguajes**: alta de la materia con el parcial de autómatas
  (TOPIC 1 y 2 de la cátedra), en cuatro unidades: lenguajes, autómatas y ER; de AF a ER; de ER a
  AFD mínimo; diseñar AF y ER. Teoría corta para leer rápido y práctica resuelta paso a paso
  (autómatas inventados con la forma del parcial y 12 ejercicios del TP I). En Evaluación, los
  parciales y recuperatorios 2023 y 2025 resueltos y un parcial inventado para practicar. Los
  autómatas los dibuja y los comprueba `fuentes/automatas.py` (cada ER y cada paso se prueba con
  todas las cadenas hasta largo 8).
* **0.51.2-alpha** — Ingeniería de Software II, pregunta fundamental de CMMI con IA: cada acción
  empieza por lo que define a su nivel, y la explicación separa el Nivel 4 (los datos para
  controlar y predecir) del 5 (los datos para cambiar el proceso).
* **0.51.1-alpha** — Ingeniería de Software II, CMMI: los riesgos de no avanzar de nivel, más cortos
  y armados desde la definición del nivel siguiente ("Como no..., ..."), con la tabla de los
  cuatro casos en la pregunta fundamental 2 y la forma de escribirlos en la teoría.
* **0.51.0-alpha** — Ingeniería de Software II: **CMMI en 9 casos cortos**, junto a los parciales.
  Una empresa en cada uno de los cinco niveles para identificarlo, justificar y decir los riesgos,
  y un caso por cada escalón para proponer cómo subir.
* **0.50.3-alpha** — Ingeniería de Software II, preguntas fundamentales: revisadas las 14 respuestas
  contra su consigna; la de conflictos de merge ahora empieza por la definición.
* **0.50.2-alpha** — Ingeniería de Software II, preguntas fundamentales: reordenadas de la más básica
  a la más específica dentro de cada tema (primero los cinco niveles de CMMI, después diagnosticar),
  y con un solo nombre para cada nivel en todas las explicaciones.
* **0.50.1-alpha** — Ingeniería de Software II, preguntas fundamentales: se suma la de agentes de IA
  para programación (material nuevo de 2026), en el sexto lugar.
* **0.50.0-alpha** — Ingeniería de Software II: **preguntas fundamentales de teoría**, junto a
  los parciales. Trece preguntas de CMMI, Git, métricas y calidad con otros casos que el parcial
  2025, cada una con la respuesta para aprender y la explicación desde cero.
* **0.49.0-alpha** — Ingeniería de Software II: modo **Practicar diagramas** en las
  autoevaluaciones. Los ocho diagramas de patrones con los nombres tapados, para completar
  escribiendo el patrón, las clases, los atributos y los métodos.
* **0.48.0-alpha** — Ingeniería de Software II, ejercicios de parcial: cuatro ejercicios más
  (las mismas formas de consigna con los patrones rotados, y un integrador), pasos de **escribir
  la palabra clave** y, en el formulario, la elección de qué ejercicios hacer.
* **0.47.0-alpha** — Ingeniería de Software II: autoevaluaciones con **ejercicios de parcial**.
  El formulario suma el paso Modo (preguntas cortas o ejercicios) y hay cuatro ejercicios
  fundamentales de patrones, paso a paso, con la respuesta modelo de cada parte.
* **0.46.12-alpha** — Ingeniería de Software II, Abstract Factory: el segundo ejemplo de "dibujarlo
  y explicarlo" pasa a ser una casa de ropa de fútbol, escrito con la misma forma que el de la
  mueblería (el del videojuego tampoco se entendía).
* **0.46.11-alpha** — Ingeniería de Software II, Abstract Factory: en "dibujarlo y explicarlo", el
  segundo ejemplo (la interfaz gráfica multiplataforma) se cambió por uno más sencillo, un
  videojuego con mundos.
* **0.46.10-alpha** — Ingeniería de Software II, parciales 2024 y 2025 resueltos: las respuestas
  modelo de los siete ejercicios de patrones se reescribieron con el criterio de la teoría (tres
  partes breves, la frase del enunciado, cada parte del patrón explicada y todo dicho con el
  caso). En la Teoría 4 de 2025, el propósito de cada patrón queda explicado para la empresa del
  enunciado; en la Práctica 1, cada patrón lleva su justificación completa.
* **0.46.9-alpha** — Ingeniería de Software II: en todas las respuestas de los ejemplos de patrones,
  cada parte que se nombra (creador, producto, notificador, contexto...) lleva una aclaración
  corta de qué es, dicha con las clases del caso. La respuesta de "reconocerlo en un código" pasa
  a las mismas tres partes que las demás.
* **0.46.8-alpha** — Ingeniería de Software II: la respuesta de "identificar los patrones de un
  enunciado" queda como se escribiría en el parcial: el patrón de la sección en tres partes breves
  (qué patrón y por qué, cómo se aplica, qué se gana) y los otros dos en dos oraciones, sin la
  tabla de clases y métodos.
* **0.46.7-alpha** — Ingeniería de Software II: en "identificar los patrones de un enunciado", la
  respuesta del patrón de la sección va por partes (qué patrón, la frase que lo pide, por qué, cómo
  queda armado con sus clases, atributos y métodos, y qué se gana), seguida de su diagrama. Los
  otros dos patrones quedan en una línea cada uno.
* **0.46.6-alpha** — Ingeniería de Software II: el ejemplo "identificar los patrones de un enunciado"
  de cada patrón suma el diagrama UML de ese patrón aplicado al enunciado (solo el de la sección).
* **0.46.5-alpha** — Ingeniería de Software II: una sola descripción por patrón. La del ejemplo
  "dibujarlo y explicarlo" tiene tres oraciones (cuándo se usa, cómo funciona, qué se gana) y las
  justificaciones de los demás ejemplos son esas mismas oraciones con los nombres del caso, en
  lugar de explicar el patrón con otras palabras cada vez.
* **0.46.4-alpha** — Ingeniería de Software II, Factory Method: aclarado que el Producto va como
  interfaz en la estructura general y como clase abstracta cuando el enunciado da atributos
  comunes a todos los productos, y cómo cambia la línea en cada caso.
* **0.46.3-alpha** — Ingeniería de Software II: en los diagramas UML, las clases abstractas llevan
  el rótulo «abstract» arriba del nombre, además de la cursiva, para que no se lean como clases
  comunes. (La 0.46.2 se retiró.)
* **0.46.1-alpha** — Ingeniería de Software II: tampoco usan consignas de parcial los ejemplos de
  teoría de la unidad base, de calidad (diagnóstico de CMMI, tres acciones con IA, ficha de una
  métrica) y de Git (el flujo entre dos ramas). Son casos muy parecidos, con otra empresa y otras
  ramas; los parciales quedan en Evaluación.
* **0.46.0-alpha** — Ingeniería de Software II, teoría de patrones: los ejemplos ya no usan los
  enunciados de los parciales (quedan en Evaluación, para rendirlos sin haberlos visto) sino los
  más parecidos de las guías de la cátedra o inventados muy parecidos. Cada patrón suma un quinto
  ejemplo, "identificar los patrones de un enunciado" (tres párrafos con tres patrones, como en
  2025), y la justificación de "aplicarlo a un enunciado" va en tres partes: qué patrón y qué
  frase lo pide, cómo queda armado y qué se gana.
* **0.45.1-alpha** — Ingeniería de Software II: en "dibujarlo y explicarlo", los dos ejemplos de
  cada patrón ya no son una frase: cada uno trae el caso y una línea que dice por qué ahí va el
  patrón.
* **0.45.0-alpha** — Ingeniería de Software II: la teoría de los ocho patrones termina con los
  mismos cuatro ejemplos con formato de parcial, uno por cada forma en que lo pueden tomar:
  dibujarlo y explicarlo, aplicarlo a un enunciado, reconocerlo en un código C++ y agregarlo a un
  diagrama que ya existe. Son 22 ejemplos nuevos (17 diagramas y 7 programas compilados) más los
  10 de parciales reales, reordenados.
* **0.44.2-alpha** — Ingeniería de Software II, unidad base: explicado por qué lo estático se
  nombra con `Clase::` y no con un objeto y un punto, y por qué `int Alumno::cantidad_ = 0;` no es
  una asignación a un atributo privado sino la línea que lo crea.
* **0.44.1-alpha** — Ingeniería de Software II: los ejemplos que leen o piden un diagrama lo
  muestran ahí mismo, en vez de mandar a buscarlo más arriba (7 lugares de la teoría).
* **0.44.0-alpha** — Ingeniería de Software II: autoevaluaciones por temas. Banco de 67 preguntas
  (patrones en código C++ y en enunciados, partes de los diagramas, niveles de CMMI, fichas de
  métricas, comandos de Git, versionado semántico). La evaluación simple ahora deja elegir los
  temas cuando el banco tiene más de una unidad.
* **0.43.0-alpha** — Teoría y práctica más visuales, en todas las materias: títulos con su barra
  de color (azul la explicación, celeste los ejemplos, ámbar los errores), tablas con encabezado y
  primera columna de color, cajas con borde, código en el texto en celeste. En Ingeniería de
  Software II, además: diagramas UML con color (violeta las interfaces, celeste las clases
  abstractas, cabecera llena la clase principal, y `+ - #` en verde, rojo y ámbar), ventajas y
  desventajas en verde y rojo, la escalera de los cinco niveles de CMMI, el flujo de los tres
  estados de Git y etiquetas de color para niveles, estados y grupos de patrones.
* **0.42.1-alpha** — Ingeniería de Software II: marcas de parcial (★ y ◈) en 32 ejercicios de
  práctica, con la consigna de parcial a la que corresponde cada uno.
* **0.42.0-alpha** — El código se ve con colores (palabras clave, tipos, funciones, textos,
  comentarios) y con número de línea en los bloques largos, en todas las materias; lo pone
  `construir.py` al armar el campus, sin nada que corra en el navegador. En Ingeniería de
  Software II el programa de cada ejemplo va partido en partes numeradas, cada una con su título,
  su rol en el patrón y los renglones importantes resaltados.
* **0.41.0-alpha** — Ingeniería de Software II: los parciales 2024 y 2025 transcriptos y resueltos
  en Evaluación (respuesta modelo y explicación de cada consigna, con el código del 2025 también en
  C++). Una materia sin banco de preguntas ya no muestra la sección Autoevaluación.
* **0.40.0-alpha** — Ingeniería de Software II, Unidad 6: gestión de cambios y control de
  versiones, Git (los tres estados, los comandos, conflictos de merge) y versionado semántico, con
  la pregunta de Git del parcial 2025 resuelta y todas las secuencias probadas en un repositorio.
* **0.39.0-alpha** — Ingeniería de Software II, Unidad 5: calidad de software, mejora de procesos,
  CMMI (los cinco niveles y un método de cuatro preguntas para diagnosticar una empresa), IA para
  mejorar los procesos y métricas (la ficha de cinco campos), con las tres preguntas teóricas del
  parcial 2025 resueltas; y los siete casos de CMMI de la cátedra más tres fichas de métricas.
* **0.38.0-alpha** — Ingeniería de Software II, Unidad 4C: Observer y Strategy, la sección "¿Qué
  patrón es?" (los ocho comparados: frases de los enunciados, señales en el código, firma de cada
  diagrama, y el enunciado del parcial 2025 resuelto) y 8 ejercicios, con los integradores.
* **0.37.0-alpha** — Ingeniería de Software II, Unidad 4B: Adapter, Composite y Facade (teoría con
  diagramas y C++ compilado, y las consignas de los parciales resueltas) y 8 ejercicios de las
  guías resueltos, con código en C++, PHP y C#.
* **0.36.0-alpha** — Ingeniería de Software II, Unidad 4A: Singleton, Factory Method y Abstract
  Factory (teoría con diagramas y C++ compilado) y 7 ejercicios de las guías resueltos.
* **0.35.0-alpha** — Ingeniería de Software II: alta de la materia y unidad Base (la clase y cómo
  se dibuja, las seis relaciones de un diagrama de clases, leer una clase en C++, herencia y
  punteros, qué es un patrón de diseño). Los diagramas UML se generan con `fuentes/uml.py`.
* **0.34.2-alpha** — `NewCampus.exe` revisa al arrancar que estén todas las piezas de los apuntes
  y recupera las que falten; un `construir.py` corrido en otra PC ya no traba la actualización.
* **0.34.1-alpha** — Tareas y Calendario vuelven también a la fila de pestañas (Teoría · Práctica
  · Evaluación · Tareas · Calendario), sin dejar el menú lateral; desde ahí, Teoría, Práctica y
  Evaluación llevan a la última unidad abierta.
* **0.34.0-alpha** — Programación Avanzada: teoría y práctica de las 6 clases, el Parcial PHP
  resuelto y su autoevaluación. Tareas y Calendario pasan al menú lateral.
* **0.33.1-alpha** — tareas: arrastrar una hasta abajo de su columna la deja última (quedaba
  anteúltima) y la copia que sigue al mouse ya no sale atenuada.
* **0.33.0-alpha** — las tareas pueden ser de una materia, con su color.
* **0.32.0-alpha** — pestaña Tareas (pendientes, en proceso y hecho); se saca la Ruta
  recomendada.
* **0.31.0-alpha** — 1ra etapa: botón Resolver en cada pregunta.
* **0.30.0-alpha** — 1ra etapa: opción de corregir cada pregunta al responderla.
* **0.29.0-alpha** — 1ra etapa en hoja (sin completar) y modo urgente con las preguntas de
  teoría más probables; planteo en la hoja en los fundamentales.
* **0.28.0-alpha** — ejercicios fundamentales (plan de urgencia) en el interactivo, con la t de
  Student; cuestionario de la 1ra etapa rehecho al estilo del Aula Virtual.
* **0.27.0-alpha** — "En la hoja" en los pasos de opciones que se anotan con fórmulas (153 pasos).
* **0.26.0-alpha** — cuadro de datos del ejercicio en el interactivo (principiante y medio); la ruta
  suma el parcial 2025 entero en el interactivo.
* **0.25.0-alpha** — en el interactivo se puede hacer un parcial entero (2025 o 2023) en su orden;
  "Solo tal cual del parcial" queda solo para el interactivo.
* **0.24.0-alpha** — centrar el contenido pasa a ser opcional (botón arriba); por defecto va al
  costado.
* **0.23.0-alpha** — respuestas de los pasos escritas como se anotan en la hoja (503 pasos).
* **0.22.0-alpha** — "Ver resolución" en los pasos ya hechos del interactivo.
* **0.21.0-alpha** — casilla "Solo tal cual del parcial" al armar una autoevaluación.
* **0.20.0-alpha** — saltear un ejercicio del interactivo lo deja para después: se retoma donde
  quedó antes de terminar.
* **0.19.0-alpha** — `NewCampus.exe` avisa cuando hay actualizaciones y se actualiza solo
  (git pull y, si hace falta, reinicio con el `.exe` nuevo).
* **0.18.0-alpha** — en el interactivo (y el guiado) se pueden revisar los ejercicios ya hechos.
* **0.17.0-alpha** — en una autoevaluación, el material de cátedra es el de sus unidades.
* **0.16.0-alpha** — respuesta final en palabras al terminar cada inciso del interactivo
  (y en el informe).
* **0.15.0-alpha** — en el interactivo, el enunciado queda fijo en una columna al costado y los
  pasos hechos se pliegan a un renglón.
* **0.14.0-alpha** — botón Resolver en cada paso del modo interactivo (y de las guiadas), con
  una resolución detallada escrita para cada paso de los ejercicios de las U4 a U7.
* **0.13.0-alpha** — mantener apretada una unidad del menú abre una copia de solo esa unidad
  (Teoría y Práctica) en otra ventana.
* **0.12.0-alpha** — guía de la tabla de la normal en la teoría de la U6 (sección 11: dónde está
  cada cosa en el PDF, cómo se busca al derecho y al revés, errores típicos), y cada búsqueda en la
  tabla de la U6 muestra el pedazo de la tabla con la fila, la columna y el cruce marcados.
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
