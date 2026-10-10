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

**El parcial es el miércoles 14/10/2026.** Hay cuatro días: entra lo que se toma, y de eso lo
fundamental.

- **Entra:** `PATRONES DE DISEÑO\` (4 apuntes + las prácticas), `Calidad de software\` (apunte
  2026, 2 prácticas de CMMI, diapositivas de Agentes de IA), `Métricas.pdf`, `Gestión de cambios.pdf`
  (versión 2026, la de la raíz) y los parciales 2024 y 2025.
- **No entra:** Docker (confirmado por Fran), `Cuatrimestre 1\` (1er parcial), `[TP]\` y
  `[Resumenes]\` (de otras personas) y las copias repetidas.
- **Se deja para después del parcial:** el banco de autoevaluación (preguntas inventadas), y de los
  apuntes lo que nunca se tomó y es largo: claves SSH, gestores de dependencias, estándares de
  calidad uno por uno. De eso va, como mucho, un párrafo.

## Cómo queda en el campus

`ing2` ya está en `materias.json` como "pronto". Unidades (la numeración de la cátedra, U4 patrones
/ U5 calidad / U6 versiones, se confirma en la Parte 1):

| Clave | Nombre | Contenido |
| :-- | :-- | :-- |
| `base` | Base: UML de clases y C++ | Lo mínimo para leer un diagrama de clases y un código C++, y qué es un patrón |
| `crea` | Patrones creacionales | Singleton, Factory Method, Abstract Factory |
| `estr` | Patrones estructurales | Adapter, Composite, Facade |
| `comp` | Patrones de comportamiento | Observer, Strategy y "¿qué patrón es?" (los 8 comparados) |
| `calidad` | Calidad, CMMI y métricas | Qué es calidad, los 5 niveles de CMMI, IA en la mejora, la ficha de una métrica |
| `git` | Gestión de cambios y Git | Conceptos, los tres estados, commit, ramas, merge, remoto |

**Cada patrón es una sección de teoría con la misma forma:**
Para qué sirve (el problema, sin jerga) → Estructura (diagrama UML dibujado + tabla "qué es cada
parte") → El mismo ejemplo en C++, línea por línea → Cómo reconocerlo (en un enunciado / en código)
→ Ventajas y desventajas → Dónde se usa (2 o 3 ejemplos, los piden) → Con qué se confunde.

**La práctica de cada unidad son los ejercicios de las guías de la cátedra, resueltos paso a paso**
(el diagrama dibujado y la justificación escrita como se entregaría en el parcial). Primero los que
tienen la forma del parcial; los que repiten el mismo enunciado en varias guías se resuelven una vez.

**Reglas propias** (van al `app/contenido/ing2/CLAUDE.md` en la Parte 1):

- Todo código C++ se **compila y corre** antes de escribirlo (`g++ -std=c++14`, MinGW 6.3 en
  `C:\MinGW\bin`; sin `std::thread`).
- Los diagramas UML se dibujan en **SVG a mano**, con una convención fija (se define en la Parte 1).
- Los nombres de las partes de cada patrón, como en el apunte de la cátedra (Refactoring.Guru en
  castellano), y entre paréntesis el nombre en inglés que aparece en el código de los parciales.
- La teoría se escribe con palabras propias; del libro no se copian párrafos.

## Partes (una por sesión)

| # | Día | Qué se hace | Qué leer |
| :-- | :-- | :-- | :-- |
| 1 | sáb 10 | Alta de la materia (`materias.json`, `CLAUDE.md` de ing2, convención de diagramas UML). **Base**, corta: clase, atributo, método, herencia, interfaz, asociación/agregación/composición; de C++: `class`, `public/private/protected`, `virtual`, `= 0`, `override`, punteros y `->`, `new/delete`, `static`; qué es un patrón y los 3 grupos. **Creacionales**: los 3 + práctica | `docs/estructura.md`, `docs/contenido.md`, un fragmento de PA como modelo, `Introducción patrones de diseño.md`, `02 - Creacionales` (+ sus 3 páginas ⚠). Práctica: Guía 1 ej. 2 y 4, `practica 1` ej. 2 y 3, `Ejercicios de patrones`, `Ejercicios_patrones_singleton_subir` |
| 2 | dom 11 | **Estructurales**: los 3 + práctica | `03 - Estructurales` (+ ⚠). Práctica: Guía 2 ej. 1 a 4, `Practica_03`, `practica 1` ej. 4, `practica 2` ej. 1, 3 y 5, Guía 1 ej. 3 |
| 3 | dom 11 / lun 12 | **Comportamiento**: los 2 + práctica. **"¿Qué patrón es?"**: tabla de decisión de los 8, frases que delatan a cada uno en un enunciado y señales en el código, enunciados integradores | `04 - Comportamiento` (+ ⚠). Práctica: Guía 3, `practica 2` ej. 2 y 6, Guía 1 ej. 1, Guía 2 ej. 5, `PRACTICA ADICIONAL` |
| 4 | lun 12 | **Calidad, CMMI y métricas** y **Git**: solo lo que se toma. CMMI: los 5 niveles, cómo diagnosticar, qué falta para subir, acciones con IA. Métrica: los 5 campos y 3 fichas armadas. Git: tres estados y la secuencia de comandos con ramas y remoto | `Calidad de software.md` p. 4-6 y 19-25, `Agentes_IA`, `Métricas.md` p. 4-6 y 10-13, `Gestión de cambios.md` p. 3-4, 12-16 y 19-24. Práctica: los 2 ejercicios de CMMI y 3 casos de `Practica 2 CMMI` |
| 5 | mar 13 | **Parciales 2024 y 2025 resueltos** en Evaluación (respuesta modelo de cada consigna, con el código del 2025 también en C++) y marcas ★ en lo que tomaron | `EXAMENES/`, `docs/evaluacion.md` |

Cada parte deja su unidad con teoría y práctica, construida, verificada y pusheada. Si una parte se
alarga, se recorta la práctica (menos ejercicios), nunca la teoría de un patrón.

## Decidido con Fran (10/10)

- Docker no entra. El banco de autoevaluación queda para después del parcial.
- Arranca de cero: la unidad Base va, corta.

## Después del parcial

- Banco de autoevaluación ("¿qué patrón es este código?", "¿en qué nivel CMMI está?"), Evaluación
  simple como PA.
- Completar lo recortado de Calidad y de Gestión de cambios, si hace falta para el final.
