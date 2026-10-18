# Bases de Datos (bd) — cómo se escribe su contenido

Las reglas generales están en `docs/contenido.md` (raíz del repo); acá va solo lo propio de BD.
El contexto completo de la materia (exámenes, clases grabadas, qué dijeron los profes) está en
`C:\Users\Fran\Desktop\SISTEMAS 3\BD\CONTEXTO-CAMPUS.md`, fuera del repo.

## Fuentes y alcance

- **Alcance:** el **2do parcial** (SQL y scripts), el **27/10/2026**. El 1er parcial (archivos,
  DER, normalización) ya se rindió: entra solo como repaso, en lo que el 2do parcial y los finales
  vuelven a tomar. Pedido de Fran: poco tiempo, teoría fundamental para lectura rápida y foco en
  las resoluciones del parcial 2025 y sus variantes; práctica solo con lo fundamental.
- **Fuentes:**
  - Apuntes y guías en `C:\Users\Fran\Desktop\SISTEMAS 3\BD\`, en texto en `fuentes/bd/`
    (`fuentes/bd/INDICE.md`).
  - **Clases grabadas** (playlist de YouTube "no listado" que subió un compañero): 13/08
    programación de BD (DDL y DML, CREATE TABLE), 18/08 álgebra relacional y SQL, 25/08 JOIN y
    agregación (Guía 9 resuelta), 15/09 transacciones (diapositivas de la cátedra), 06/10 TP y
    consultas (Guía 10 resuelta). Lo que se sacó de cada una está en el `CONTEXTO-CAMPUS.md`.
- **Regla para la teoría (pedido de Fran, 18/10):** en las preguntas de teoría va solo lo que está
  en la teoría de la cátedra (apuntes o diapositivas de clase) **y** tiene forma de pregunta de
  parcial. Lo demás se saca; si hace falta para la práctica, se explica en la práctica.
- **Motor:** SQL Server. No se verifica ejecutando en el SQL Server de Fran (no quiere): el SQL se
  revisa a mano y con chequeos de paréntesis, regla del `GROUP BY` y palabras reservadas (por eso
  no hay tabla `Plan`).
- **Forma del parcial** (2025 y lo que adelantaron los profes el 06/10 para 2026): teoría
  (transacción; DDL y DML, "la toman siempre"), un DER dado para pasar a tablas en 3FN, un
  `CREATE TABLE` y 5 o 6 consultas: seguro una con fechas, probablemente una con `LEFT JOIN`.
- **Unidades:** `u1` Teoría del 2do parcial · `u2` Del DER a las tablas en 3FN · `u3` SQL: crear
  tablas · `u4` SQL: consultas.
- **En la teoría y en la práctica no va el enunciado de ningún examen:** quedan en Evaluación.

## Cómo se escribe el SQL (como los profes)

- `CREATE TABLE` con las claves al final y con nombre: `CONSTRAINT PK_Tabla PRIMARY KEY (...)`,
  `CONSTRAINT FK_Tabla_Otra FOREIGN KEY (...) REFERENCES Otra(...)`, `CONSTRAINT UQ_Tabla_Col
  UNIQUE (...)`. El script `constraints.py` que lo hizo está descripto en el contexto.
- Consultas: `INNER JOIN ... ON` FK = PK con alias cortos; `LEFT JOIN` + `COUNT(columna de la
  derecha)` para que aparezcan los ceros, y `LEFT JOIN ... IS NULL` o `NOT EXISTS` para "los que
  no tienen"; subconsultas con `=` (un valor, con `TOP 1`), `IN`, en el `FROM` con alias.
- Fechas: "este año/mes" con `YEAR(f) = YEAR(GETDATE())` (nunca el año fijo); antigüedad con
  `DATEDIFF(YEAR, f, GETDATE())`; "últimos 12 meses" con `f >= DATEADD(MONTH, -12, GETDATE())`.
- `AVG(x * 1.0)` para que no dé entero; nada de `SELECT *` en las resoluciones.
- Los profes escriben en minúscula y con prefijo de tabla en los campos (`socio_nombre`); en el
  campus queda en mayúscula y sin prefijo (se aclara que es opcional).
- Modelo relacional como la cátedra: `Tabla (Atributo (PK), Otro, Ref (FK))`, en
  `<pre class="codigo" data-lang="texto">`. Nombres sin tildes; intermedias con guion bajo.

## Diagramas

Los DER se describen en `fuentes/bd/diagramas/der.py` (formato arriba de `fuentes/der.py`, con la
notación de la cátedra: círculo lleno = identificador) y van en el fragmento como
`<div class="pd-grafico der" data-g="nombre"></div>`. `python fuentes/der.py
fuentes/bd/diagramas/der.py` mete los SVG.

## Evaluación

- `"evaluacion": {"tipo": "simple"}` sin banco de preguntas. Parciales: el 2025 resuelto, las 7
  preguntas fundamentales de teoría y dos parciales de práctica inventados (gimnasio, hotel), con
  un inciso d) de `LEFT JOIN`. Finales: los dos, resueltos (los DER se resuelven con el modelo
  relacional, sin dibujarlos).
- Marcas: ★ en lo tomado tal cual en un parcial; ◈ en las variantes y en lo que avisaron en clase
  (fechas, `LEFT JOIN`).

## Pendientes e ideas

- La diapositiva de **durabilidad** no se llegó a ver en la grabación del 15/09: si Fran consigue la
  presentación "Transacciones y concurrencia", contrastar la Unidad 1, sección 3.
- La clase del 15/09 no tenía transcripción en YouTube (se subió el 15/10); se leyeron solo las
  diapositivas. Volver a mirarla si aparece la transcripción.
- Completar las tablas "página → qué hay" de los `.md` de `fuentes/bd/`.
- No se cargaron las consultas con `CASE`, `UNION` o dos subconsultas encadenadas (G9 4 y 20;
  G10 9 y 21): no aparecieron en los exámenes, y de la misma tabla dos veces (G10 9) los profes
  dijeron que no creen que entre.
