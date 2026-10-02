# Cómo se escribe el contenido (cualquier materia)

> Las rutas de este documento son relativas a `app/` (salvo que digan otra cosa).
> Lo propio de cada materia (fuentes, notación, alcance) está en `app/contenido/<materia>/CLAUDE.md`.

## Cómo explicar

* **Exhaustivo e impecable.** La prioridad número uno es la claridad absoluta.
* **Nunca des nada por sabido.** Asumí que es la primera vez que veo el tema. Si usás una fórmula
  o un símbolo, explicá de dónde sale y qué significa.
* **Resolvé vos el ejercicio completo.** No me pidas que yo haga el paso siguiente. Yo pregunto después.
* **Anticipate a las dudas.** Si un paso matemático es engañoso, frená y explicá el procedimiento
  asumiendo que me voy a trabar ahí.
* **Prohibido el "chorizo" de texto.** Listas, viñetas, subtítulos y muchos saltos de línea.
* **Separá la lógica matemática de la ejecución en la calculadora.**
* Hablame en español rioplatense, sin lenguaje coloquial excesivo.

## Cómo se escribe la teoría

> **Regla de oro: nada se usa antes de estar explicado en general.**
>
> Si en un ejercicio aparece una herramienta, un atajo o una notación, primero tiene que estar
> explicada **en abstracto** —qué es, por qué funciona, cuándo conviene, con su fórmula y un
> ejemplo numérico chiquito suelto— y recién después aplicada al caso. Nunca al revés, y nunca
> un *"vamos por el complemento"* sin haber dicho antes qué es el complemento.
>
> Lo general va en la sección más temprana que corresponda (en la Unidad 5, las herramientas
> transversales están en la sección 1) y el punto de uso la referencia: *"la herramienta que
> vimos en la sección 1"*.
>
> Si algo se resuelve por el camino largo porque el corto todavía no se explicó, **decilo**:
> mostrá cómo quedaría por el camino corto, verificá que da lo mismo y apuntá a la sección donde
> se explica. De molde sirven el *complemento* y la *notación científica* de
> `u5/teoria/01-...`, aplicados después en la Binomial.
>
> Lo mismo vale para los **resultados que no se entienden solos** (un \(1 \times 10^{-10}\), un
> número gigante): explicá cómo se leen y **cómo se escriben en la respuesta**, no los dejes
> pelados.

> **Cada unidad guía al lector.** `00-intro.html` lleva una sección "Cómo leer esta unidad" con
> `data-abierta` (la app la abre sola): qué entró en los exámenes, en qué orden leer y qué dejar
> para después. Si el tema es visual, cada concepto e inciso lleva su gráfico SVG con las clases
> `.pd-grafico` (definidas en `assets/estilos.css`, siguen el tema claro/oscuro). Las curvas se
> calculan con un script, no se dibujan a ojo; cada gráfico va en
> `<div class="pd-grafico" data-g="nombre">` para poder regenerarlo.
> **Los gráficos son para entender, no una instrucción.** La cátedra resuelve los ejercicios con
> cuentas y la guía no pide gráficos: el texto nunca dice que el alumno "tiene que dibujar". Solo
> se habla de graficar en los incisos que lo piden con todas las letras (las propiedades de la
> curva normal "con los gráficos necesarios", "representar gráficamente…").

* Basada íntegramente en el PDF teórico de la cátedra, pero traducida a algo digerible.
  Resumí de a poco.
* Cada concepto y cada fórmula general va acompañado de un **ejemplo práctico numérico**.
* **Mínimo 2 ejemplos por apartado.** Uno simple y uno con formato de parcial real.
* En cada ejemplo, siempre estas dos cosas antes de calcular:
  1. **"Por qué este modelo"** — recorriendo las condiciones una por una.
  2. **"Desarme del enunciado"** — una tabla que mapea cada frase textual del enunciado a su símbolo:

     | Frase del enunciado | Qué significa | La cuenta | A dónde va |
     | :--- | :--- | :--- | :--- |
     | "se seleccionan tres artículos" | cantidad de pruebas | — | \(n = 3\) |
     | "probabilidad del 20%" | probabilidad de éxito | \(20 \div 100\) | \(p = 0{,}20\) |

* Si un modelo tiene fórmulas propias de Esperanza y Varianza, explicá **de dónde salen**
  (no son fórmulas distintas: son la definición general resuelta una vez para ese caso).

## Cómo se escribe la práctica

* Los ejercicios de la guía, resueltos enteros.
* **La fórmula se repite explícitamente en cada inciso, antes de reemplazar los números.**
  Es para memorizarla visualmente. No la des por escrita más arriba.
* Abundantes saltos de línea.
* Texto que explica el *porqué* de cada paso, no solo la cuenta.
* Al final de cada ejercicio, el resultado contrastado con la hoja de resultados de la cátedra.

## Verificación contra la cátedra

* Antes de dar un resultado, buscá el PDF de "Resultados" de esa guía y verificá.
* Tu procedimiento tiene que llegar **matemáticamente** al resultado de la cátedra.
* Si no coincide, **no lo maquilles**: resolvelo bien, marcá la diferencia en una caja de aviso
  dentro del ejercicio y explicá de dónde sale el error si podés reconstruirlo.
  (Ya pasó tres veces y las tres eran errores de la hoja oficial.)
* Los ZIP/PDF de práctica de la cátedra mandan sobre los PDF de teoría.

## Cuando Fran hace una consulta

Si te pregunto *"¿por qué en el ejercicio X esto es así?"*:

1. Me contestás en el chat.
2. **Y además** vas al archivo de `contenido/` correspondiente, buscás ese ejercicio y
   **ampliás la explicación ahí mismo**, redactada como parte del apunte.
3. Corrés `python construir.py` dentro de `app/`.

Nunca agregues un bloque de "pregunta / respuesta". La duda se disuelve dentro del texto,
como si siempre hubiera estado explicada.

## Clases de CSS disponibles

Usá estas y no inventes otras, así el diseño se mantiene consistente:

| Clase | Para qué |
| :--- | :--- |
| `.bloque` | tarjeta de una sección de teoría |
| `.ej` | tarjeta de un ejercicio de práctica |
| `.tag` | etiqueta del ejercicio (`Ejercicio 6 · Hipergeometrica`) |
| `.enunciado` | el enunciado textual, en gris |
| `.paso` | rótulo de paso (`<span class="paso">Paso 1 — ...</span>`) |
| `.caja.caja-formula` | fórmula destacada |
| `.caja.caja-ejemplo` | enunciado de un ejemplo |
| `.caja.caja-ojo` | trampa, error típico, advertencia |
| `.caja.caja-resp` | respuesta / resultado oficial |
| `.caja.caja-calc` | qué se tipea en la calculadora |
| `.caja-tit` | título dentro de una caja (`<span class="caja-tit">`) |
| `.tabla-wrap` + `table.t` | tablas (agregá `.full` para ancho completo) |
| `.kicker` | rótulo chiquito arriba del `<h2>` |

El índice lateral se arma solo con los `<h2>` y `<h3>` del pane, y les pone adelante el número
de ejercicio leyéndolo del `.tag`.

## Fuentes de cátedra en texto

Los PDFs de cátedra se pasan a texto **una sola vez por materia**, antes de escribir su primer
contenido, y quedan en `fuentes/<materia>/` (en el repo):

1. `python fuentes/extraer.py fuentes/<materia> "<carpeta de PDFs>"` (desde la raíz del repo; pypdf,
   sin leer los PDFs con el modelo). Arma un `.md` por PDF con `<!-- página N -->` antes de cada
   página, y extrae una sola vez las copias exactas. Si se vuelve a correr, el índice escrito no se
   pierde.
2. Arriba de cada `.md`, completar la tabla "página → qué hay" y marcar **⚠ ver el PDF** en las
   páginas donde el texto no alcanza (tablas, fórmulas rotas, gráficos, escaneos). Para eso se
   miran solo las páginas dudosas, no el PDF entero: `python fuentes/pagina.py "<PDF>" 3 7` las
   pasa a PNG y se abren con Read (en esta PC Read no abre PDFs: falta pdftoppm).
3. Un `fuentes/<materia>/INDICE.md`: qué archivo es de qué unidad o examen.

Después, al escribir: **primero el texto extraído** (ubicar con el índice o con Grep la página y
leer solo ese rango); el PDF, solo en las páginas marcadas ⚠ o si algo no cierra. El PDF nunca
se borra: el texto es un atajo para leer menos, no un reemplazo.

## Antes de escribir

1. Leer **solo las fuentes de esa unidad** (el texto extraído si existe; el PDF, en las páginas que hagan falta).
2. Leer **uno o dos fragmentos** de `contenido/` del mismo tipo como modelo de formato, no la unidad entera.
3. Recién ahí escribir.
