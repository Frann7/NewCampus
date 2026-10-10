# Plan para sumar Ingeniería de Software II (2do parcial)

Análisis hecho el 10/10/2026 sobre `C:\Users\Fran\Desktop\SISTEMAS 3\ING 2\SEGUNDO CUATRIMESTRE\`.
El texto de cada PDF ya está en `fuentes/ing2/` (ver su `INDICE.md`). **Una parte = una sesión
nueva**; cada parte dice qué leer y qué deja hecho. Fran arranca de cero: todo se explica desde
cero y paso a paso.

## Qué toma el parcial

| | 2024 (23/10) | 2025 (8/10) |
| :-- | :-- | :-- |
| Patrones desde un **enunciado**, justificando | ej. 1: alarmas con sensores agrupados (Composite) | Práctica 1: Muebles Express (Strategy + Factory Method + Observer) |
| **Dibujar el UML** de un patrón y explicar para qué sirve | ej. 2: Singleton + 2 ejemplos de uso | Teoría 4 (20 pts): Abstract Factory y Adapter, descriptos sin nombrarlos |
| **Aplicar** patrones sobre un diagrama dado | ej. 3: farmacia (Singleton + Observer) | — |
| Patrón desde **código**, diciendo qué lo delata | ej. 4: Facade en C++ | Práctica 2: Facade en PHP |
| **CMMI**: en qué nivel está una empresa, riesgos, acciones para subir | — | Teoría 1 y 2 (15 pts), con IA en las acciones |
| **Git**: pasos del Working Directory a develop y a main, con el remoto | — | Teoría 3 (5 pts) |
| **Métrica**: atributo, medida, unidad, indicador, métrica | — | Teoría 5 (10 pts) |

- En 2025 la Teoría valió 50 y **20 de esos 50 eran dibujar patrones**: entre eso y la Práctica,
  los patrones son ~70 % del parcial. CMMI + Git + métrica son ~30 % y son los puntos más baratos.
- Este año (dicho por la cátedra): parecido al 2025, cambian las preguntas teóricas, el código es
  en **C++**, y los patrones son los 8 de los apuntes: Factory Method, Abstract Factory, Singleton,
  Adapter, Composite, Facade, Observer, Strategy.
- Las guías repiten siempre los mismos enunciados (libro digital, GestorUsuarios de instancia única,
  alerta + tabla de auditoría, carpetas que contienen archivos): son la mejor pista de qué cae.

## Lo que hay que saber hacer (el foco)

1. Leer un enunciado y decir qué patrón va y **por qué** (qué frase lo delata).
2. Dibujar de memoria el **UML de la estructura** de cada uno de los 8 y nombrar sus partes.
3. Leer código **C++** y reconocer el patrón por sus señales.
4. Diagnosticar el **nivel CMMI** de una empresa y proponer acciones para subir.
5. Armar la **ficha de una métrica** con sus 5 campos.
6. Escribir la **secuencia de comandos Git** de un flujo con ramas.

## Qué entra y qué no

- **Entra:** `PATRONES DE DISEÑO\` (4 apuntes + 11 prácticas), `Calidad de software\` (apunte 2026,
  2 prácticas de CMMI, diapositivas de Agentes de IA), `Métricas.pdf`, `Gestión de cambios.pdf`
  (versión 2026, la de la raíz) y los parciales 2024 y 2025.
- **No entra:** `Cuatrimestre 1\` (1er parcial), `[TP]\` y `[Resumenes]\` (de otras personas),
  y las copias repetidas. **Docker** (7 diapositivas 2026) queda afuera salvo que la cátedra diga
  que entra.
- Los PDFs **no se copian a `app/pdf/`**: la teoría de patrones es un libro pago.

## Cómo queda en el campus

`ing2` ya está en `materias.json` como "pronto". Unidades propuestas (la numeración de la cátedra,
U4 patrones / U5 calidad / U6 versiones, se confirma en la Parte 1):

| Clave | Nombre | Contenido |
| :-- | :-- | :-- |
| `base` | Base: UML de clases y C++ | Lo mínimo para leer un diagrama de clases y un código C++, y qué es un patrón |
| `crea` | Patrones creacionales | Singleton, Factory Method, Abstract Factory |
| `estr` | Patrones estructurales | Adapter, Composite, Facade |
| `comp` | Patrones de comportamiento | Observer, Strategy y "¿qué patrón es?" (los 8 comparados) |
| `calidad` | Calidad de software y CMMI | Calidad, CMMI, IA en la mejora de procesos |
| `metricas` | Métricas | Los 5 conceptos, ciclo de vida, tipos |
| `git` | Gestión de cambios y Git | Conceptos, Git, ramas y merge, versionado semántico |

**Cada patrón es una sección de teoría con la misma forma:**
Para qué sirve (el problema, sin jerga) → Estructura (diagrama UML dibujado + tabla "qué es cada
parte") → El mismo ejemplo en C++, línea por línea → Cómo reconocerlo (en un enunciado / en código)
→ Ventajas y desventajas → Dónde se usa (2 o 3 ejemplos, los piden) → Con qué se confunde.

**Reglas propias** (van al `app/contenido/ing2/CLAUDE.md` en la Parte 1):

- Todo código C++ se **compila y corre** antes de escribirlo (`g++ -std=c++14`, MinGW 6.3 en
  `C:\MinGW\bin`; sin `std::thread`).
- Los diagramas UML se dibujan en **SVG a mano**, con una convención fija (se define en la Parte 1).
- Los nombres de las partes de cada patrón, como en el apunte de la cátedra (Refactoring.Guru en
  castellano), y entre paréntesis el nombre en inglés que aparece en el código de los parciales.
- La teoría se escribe con palabras propias; del libro no se copian párrafos.

## Partes (una por sesión)

| # | Qué se hace | Qué leer |
| :-- | :-- | :-- |
| 1 | Alta de la materia (`materias.json`, `CLAUDE.md` de ing2, convención de diagramas UML) y unidad **Base**: clase, atributo, método, herencia, interfaz, asociación/agregación/composición; de C++: `class`, `public/private/protected`, `virtual`, `= 0`, `override`, punteros y `->`, `new/delete`, `static`; qué es un patrón y los 3 grupos | `docs/estructura.md`, `docs/contenido.md`, `Introducción patrones de diseño.md`, un fragmento de PA como modelo |
| 2 | **Creacionales**: teoría de los 3 + práctica | `02 - Creacionales` (+ sus 3 páginas ⚠), Guía 1, `Ejercicios de patrones`, `Ejercicios_patrones_singleton_subir`, `practica 1` |
| 3 | **Estructurales**: teoría de los 3 + práctica | `03 - Estructurales` (+ ⚠), Guía 2, `Practica_03`, `practica 2` ej. 1, 3 y 5 |
| 4 | **Comportamiento** + **"¿qué patrón es?"**: tabla de decisión de los 8, frases que delatan a cada uno, enunciados integradores | `04 - Comportamiento` (+ ⚠), Guía 3, `PRACTICA ADICIONAL`, `practica 2` ej. 2 y 6 |
| 5 | **Calidad y CMMI**: teoría + los 7 casos de diagnóstico + acciones con IA | `Calidad de software.md`, sus 2 prácticas, `Agentes_IA` |
| 6 | **Métricas** y **Git** (son cortas, van juntas) | `Métricas.md`, `Gestión de cambios.md` p. 3-4 y 12-26 |
| 7 | **Evaluación**: parciales 2024 y 2025 transcriptos y resueltos, marcas ★ en lo que tomaron, y banco de autoevaluación | `EXAMENES/`, `docs/evaluacion.md`, `FORMATO.md` |

Las partes 2 a 6 dejan teoría y práctica de su unidad, construidas, verificadas y pusheadas. Si la
fecha aprieta: 5 y 6 se pueden hacer antes que 3 y 4 (son ~30 puntos en dos sesiones cortas), y la
7 se reduce a los dos parciales resueltos.

## A confirmar con Fran

- **Fecha del parcial** (define el orden y si entra todo).
- **Unidad Base**: propuesta porque los parciales piden dibujar UML y leer C++, y no hay apunte
  de eso en el 2do cuatrimestre. Si ya lo maneja, se achica a un repaso de una pantalla.
- **Banco de autoevaluación**: a diferencia de PA, acá hay que **inventar** preguntas (el parcial
  nunca se repite): "¿qué patrón es este código?", "¿qué patrón pide este enunciado?", "¿en qué
  nivel CMMI está?". Propuesta: Evaluación simple, como PA.
- **Docker**: ¿entra?
