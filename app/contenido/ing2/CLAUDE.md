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
  ejemplos: los piden) → Con qué se confunde (`.caja.caja-ojo`).
- **Nombres de las partes** como en el apunte de la cátedra (Refactoring.Guru en castellano:
  Creador, Producto, Fachada, Notificador, Suscriptor, Contexto, Estrategia...) y entre paréntesis
  el nombre en inglés que aparece en el código de los parciales (`Subject`, `Observer`, `Target`).
- La teoría se escribe con **palabras propias**; del libro no se copian párrafos.
- **Todo código C++ se compila y se corre** antes de escribirlo: `g++ -std=c++14 -Wall` (MinGW 6.3,
  en el PATH; no tiene `std::thread`), con el archivo en el scratchpad. La salida que se muestra es
  la que dio.
- **Estilo del C++:** el de los parciales (el de Refactoring.Guru): atributos con guion bajo al
  final (`saldo_`), punteros crudos con `new`/`delete`, `std::string`, `std::cout`, `override`.
- **Código en el HTML:** `<pre class="codigo"><code>...</code></pre>` y la salida en
  `<pre class="salida">...</pre>`. Dentro del código, `<` va como `&lt;`, `>` como `&gt;` y `&`
  como `&amp;` (`#include &lt;iostream&gt;`, `std::cout &lt;&lt; x`, `a-&gt;hablar()`).
- **Práctica:** los ejercicios de las guías de la cátedra, resueltos como se entregarían: qué
  patrón, la frase del enunciado que lo justifica, el diagrama dibujado y, si hay código, las
  señales que lo delatan.
- **Marcas de examen:** ★ (`data-examen="igual"`, `data-examen-ref="Parcial 2025 · Teoría 4"`) en
  lo que tomó un parcial; `variante` si fue en otro lenguaje o con un cambio.

## Diagramas UML

No se dibujan a mano: se describen en `fuentes/ing2/diagramas/<unidad>.py` y
`python fuentes/uml.py fuentes/ing2/diagramas/<unidad>.py` (desde la raíz del repo) mete el SVG en
cada `<div class="pd-grafico uml" data-g="nombre"></div>` de los fragmentos. El formato está
explicado arriba de `fuentes/uml.py`. Para corregir un diagrama se cambia su descripción y se
vuelve a correr; el SVG del fragmento no se edita. Después de generarlos se mira **cómo quedaron**
(captura): que no se pisen cajas ni líneas.

## Evaluación

- Parciales 2024 y 2025 en `evaluacion/parciales/`, una consigna por archivo, con `pd-resultados`
  (la respuesta modelo) y `pd-explicacion`. La cátedra no publicó respuestas: son propias, y así
  se avisa en la nota de cada parcial.
- No hay banco de preguntas: por eso la pestaña muestra solo los Parciales
  (`"evaluacion": {"tipo": "simple"}` en `materias.json`).

## Pendientes e ideas

- **Banco de autoevaluación** (después del parcial): preguntas del tipo "¿qué patrón es este
  código?", "¿qué patrón pide este enunciado?", "¿en qué nivel de CMMI está?". Hay que inventarlas
  (el parcial no se repite); Evaluación simple, como PA.
- De los apuntes quedó en un párrafo o afuera lo que nunca se tomó: claves SSH, gestores de
  dependencias, la especificación completa de SemVer, los "juegos" de complejidad ciclomática
  (su código está en imagen) y Docker (confirmado que no entra).
- De las guías de patrones quedaron sin resolver por separado los ejercicios que repiten otro
  (Práctica 03 ej. 1 a 3, Guía 1 ej. 1 y 6, `practica 2` ej. 6): están mencionados dentro del
  ejercicio al que se parecen.
