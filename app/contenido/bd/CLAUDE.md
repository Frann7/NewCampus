# Bases de Datos (bd) — cómo se escribe su contenido

Las reglas generales están en `docs/contenido.md` (raíz del repo); acá va solo lo propio de BD.

## Fuentes y alcance

- **Alcance:** el **2do parcial** (SQL y scripts). El 1er parcial (archivos, DER, normalización) ya
  se rindió: entra solo como repaso, en lo que el 2do parcial y los finales vuelven a tomar.
  Pedido de Fran (18/10/2026): poco tiempo, teoría fundamental para lectura rápida y foco en las
  resoluciones del parcial 2025 y sus variantes; práctica solo con ejercicios fundamentales.
- **Fuentes:** `C:\Users\Fran\Desktop\SISTEMAS 3\BD\`, en texto en `fuentes/bd/`
  (`fuentes/bd/INDICE.md`). **No hay apunte de SQL ni de transacciones**: la definición de
  transacción y ACID es la estándar, apoyada en los módulos del SGBD que nombra el apunte; la
  sintaxis SQL sale del script de Northwind, de las guías 9 a 12 y del TP final. No se usa nada de
  SQL que no aparezca ahí, salvo `DATEADD`, que pide el "últimos 12 meses" del parcial.
- **Motor:** SQL Server (T-SQL). Fran no quiere que se verifique ejecutando en su SQL Server: el SQL
  se revisa a mano (paréntesis, regla del `GROUP BY`, palabras reservadas: por eso no hay tabla
  `Plan`).
- **Exámenes:** 2do parcial 2025 (veterinaria), final 26/09/2025 (editorial) y un final sin fecha
  (electrodomésticos). El parcial 2025 tiene esta forma, que manda sobre todo lo demás:
  1. Teoría: Transacción (definición y propiedades).
  2. Teoría: DDL y DML, para qué sirven y sus sentencias.
  3. Dado el DER, el modelo relacional en 3FN con PK y FK.
  4. `CREATE TABLE` de una tabla con sus claves.
  5. Tres listados: a) filas en un estado, con JOIN y ORDER BY; b) cantidad por cliente con
     COUNT, ordenada por país, provincia, ciudad; c) total facturado de los últimos 12 meses por
     año y mes. El final del 26/09/2025 tomó los mismos tres.
- **Unidades:** `u1` Teoría del 2do parcial · `u2` Del DER a las tablas en 3FN · `u3` SQL: crear
  tablas · `u4` SQL: consultas.
- **En la teoría y en la práctica no va el enunciado de ningún examen:** quedan en Evaluación.

## Cómo se escribe

- Teoría corta: cada pregunta de examen con su **"Para escribir en la hoja"** (`.caja.caja-resp`)
  arriba, y después la explicación, dos ejemplos y las trampas.
- Ejemplos sobre el zoológico (G9) y el club náutico (G10); cada ejemplo repite las tablas que usa.
  La receta de los listados (`u4/teoria/06`) usa un taller mecánico inventado.
- SQL con alias de tabla cortos (`t`, `p`, `a`), `INNER JOIN ... ON` (FK = PK), palabras clave en
  mayúscula, `--` para comentarios. Modelo relacional como la cátedra:
  `Tabla (Atributo (PK), Otro, Ref (FK))`, en `<pre class="codigo" data-lang="texto">`.
- Nombres sin tildes en tablas y columnas; tablas intermedias con guion bajo (`Turno_Servicio`).
- El coloreo de SQL lo hace `app/resaltado.py` (lenguaje `sql`, se detecta solo).

## Diagramas

Los DER se describen en `fuentes/bd/diagramas/der.py` (formato arriba de `fuentes/der.py`, con la
notación de la cátedra: círculo lleno = identificador) y van en el fragmento como
`<div class="pd-grafico der" data-g="nombre"></div>`. `python fuentes/der.py
fuentes/bd/diagramas/der.py` mete los SVG.

## Evaluación

- `"evaluacion": {"tipo": "simple"}` sin banco de preguntas. Parciales: el 2025 resuelto, las 10
  preguntas fundamentales de teoría y dos parciales de práctica inventados (gimnasio, hotel) con
  la misma forma. Finales: los dos, resueltos (los ejercicios de DER se resuelven con el modelo
  relacional, sin dibujar el DER).
- Marcas: ★ en lo tomado tal cual en un parcial (DDL/DML, transacción, claves del 1er parcial
  2024); ◈ en las variantes (formas de los ejercicios 3, 4 y 5) y en lo que solo tomaron finales.

## Pendientes e ideas

- Si aparece un apunte de la cátedra sobre SQL o transacciones, contrastar la Unidad 1, sección 3,
  y la sintaxis de las unidades 3 y 4.
- Completar las tablas "página → qué hay" de los `.md` de `fuentes/bd/`.
- No se resolvieron las consultas con `LEFT JOIN`, `NOT IN` o subconsultas de las guías (G9 4, 15,
  16, 17, 20; G10 6, 16, 17, 20): no aparecieron en los exámenes.
