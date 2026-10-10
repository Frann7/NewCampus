# Plan para sumar Ingeniería de Software II (2do parcial)

Análisis hecho el 10/10/2026 sobre `C:\Users\Fran\Desktop\SISTEMAS 3\ING 2\SEGUNDO CUATRIMESTRE\`.
El texto de cada PDF ya está en `fuentes/ing2/` (ver su `INDICE.md`). Fran arranca de cero: todo
se explica desde cero y paso a paso. El contenido se carga **por partes, en orden**; cada parte
dice qué archivos sube y qué hay que leer para escribirla.

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

`ing2` ya está en `materias.json` como "pronto". Seis unidades:

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

## Partes

Se cargan **en este orden, una atrás de la otra** (sin día fijo: pueden ir varias el mismo día).
Cada parte termina construida ("Todo en orden"), verificada en el navegador y pusheada, y acá se
tilda. Si una parte se alarga, se recorta la práctica (menos ejercicios), nunca la teoría.

### Parte 1 — Alta de la materia y Base ☑

- `materias.json`: las 6 unidades de `ing2`. `app/contenido/ing2/CLAUDE.md` con las reglas propias.
  Convención de diagramas UML (SVG + sus estilos). README y versión.
- `base/teoria/`:
  - `00-intro` — título, bajada y cómo leer la materia (qué toma el parcial y en qué orden estudiar).
  - `01` Qué es una clase y cómo se dibuja (nombre, atributos, métodos, `+ - #`).
  - `02` Las flechas: herencia, interfaz, asociación, agregación, composición, dependencia.
  - `03` Leer una clase en C++ (`class`, `public/private/protected`, constructor, `static`).
  - `04` Herencia en C++: `virtual`, `= 0`, `override`, punteros, `->`, `new` y `delete`.
  - `05` Qué es un patrón de diseño, los 3 grupos y los 8 de la cátedra en una tabla.
- Leer: `docs/contenido.md`, un fragmento de PA como modelo, `Introducción patrones de diseño.md`.

### Parte 2 — Patrones creacionales ☑

- `crea/teoria/`: `00-intro`, `01` Singleton, `02` Factory Method, `03` Abstract Factory,
  `04` Factory Method vs. Abstract Factory (cómo no confundirlos).
- `crea/practica/`: Guía 1 ej. 2 (Singleton en C++) y ej. 4 (familias de productos); `practica 1`
  ej. 2 (ConexionDB) y ej. 3 (vehículos); `Ejercicios de patrones` (enemigos, UI multiplataforma,
  conexiones a BD); `Ejercicios_patrones_singleton_subir` (uno de los tres, los otros son iguales).
- Leer: `02 - Creacionales` (+ sus 3 páginas ⚠).

### Parte 3 — Patrones estructurales ☑

- `estr/teoria/`: `00-intro`, `01` Adapter, `02` Composite, `03` Facade.
- `estr/practica/`: Guía 2 ej. 1 (Adapter en C++), ej. 2 (Composite en PHP), ej. 3 (Facade en C#) y
  ej. 4 (libro digital); `Practica_03` (los 3); `practica 1` ej. 4 (tienda con fachada);
  `practica 2` ej. 3 (directorios) y ej. 5 (expresiones matemáticas); Guía 1 ej. 3 (TPV).
- Leer: `03 - Estructurales` (+ ⚠).

### Parte 4 — Patrones de comportamiento y "¿qué patrón es?" ☑

- `comp/teoria/`: `00-intro`, `01` Observer, `02` Strategy, `03` ¿Qué patrón es?: tabla de decisión
  de los 8, la frase que delata a cada uno en un enunciado y las señales en el código.
- `comp/practica/`: Guía 3 (los 4); `practica 2` ej. 2 (Archivo con exportadores) y ej. 6;
  integradores: Guía 1 ej. 1 (seguridad), Guía 2 ej. 5 (multimedia), `PRACTICA ADICIONAL` 1
  (expedientes) y 2 (gestión de contenido).
- Leer: `04 - Comportamiento` (+ ⚠).

### Parte 5 — Calidad, CMMI y métricas ☑

- `calidad/teoria/`: `00-intro`, `01` Qué es la calidad de software (definición, atributos,
  consecuencias de la baja calidad), `02` CMMI: qué es y los 5 niveles, `03` Cómo diagnosticar el
  nivel de una empresa y qué le falta para subir, `04` IA para mejorar la calidad (acciones hacia
  el nivel 5, agentes de IA), `05` Métricas: atributo, medida, unidad, métrica, indicador; cómo
  armar la ficha; tipos de métricas.
- `calidad/practica/`: los 2 ejercicios de `Ejercicios prácticos`, 3 casos de `Practica 2 CMMI`
  (uno por nivel) y 3 fichas de métrica armadas.
- Leer: `Calidad de software.md` p. 4-6 y 19-25, `Agentes_IA`, `Métricas.md` p. 4-6 y 10-13.

### Parte 6 — Gestión de cambios y Git ☐

- `git/teoria/`: `00-intro`, `01` Gestión de cambios, de la configuración y control de versiones
  (qué es cada una, centralizado vs. distribuido), `02` Git: los tres estados, `03` El flujo con
  comandos: `add`, `commit`, ramas, `merge`, `push` y `pull`, `04` Conflictos de merge,
  `05` Versionado semántico (corto).
- `git/practica/`: el flujo del parcial 2025 (Working Directory → develop → main, con el remoto) y
  2 variantes.
- Leer: `Gestión de cambios.md` p. 3-4, 12-16 y 19-24.

### Parte 7 — Parciales resueltos ☐

- `evaluacion/parciales/`: 2024 y 2025, una consigna por archivo, con la respuesta modelo (el
  código del 2025 también pasado a C++).
- Marcas ★ en las secciones de teoría y los ejercicios que tomaron.
- Leer: `EXAMENES/`, `docs/evaluacion.md`.

## Decidido con Fran (10/10)

- Docker no entra. El banco de autoevaluación queda para después del parcial.
- Arranca de cero: la unidad Base va, corta.
- Las partes no tienen día: se suben seguidas, y las sesiones las maneja Fran.

## Después del parcial

- Banco de autoevaluación ("¿qué patrón es este código?", "¿en qué nivel CMMI está?"), Evaluación
  simple como PA.
- Completar lo recortado de Calidad y de Gestión de cambios, si hace falta para el final.
