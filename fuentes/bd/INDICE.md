# BD — índice de las fuentes en texto

Cada `.md` es el texto de un PDF de `C:\Users\Fran\Desktop\SISTEMAS 3\BD\` (`teoria/` = `APUNTES DE
LA MATERIA`, `practica/` = `PRACTICA`), sacado con `fuentes/extraer.py`. Los DER de las guías son
dibujos sin texto: `python fuentes/pagina.py "<PDF>" 1`.

| Tema | Archivo | Qué es |
| :-- | :-- | :-- |
| 2do parcial | `teoria/02 - Sistema Gestor de Bases de Datos.md` | SGBD: funciones (definición = DDL, manipulación = DML, utilización), componentes (gestor de transacciones, planificador, gestor de recuperación), lenguajes, 4GL |
| 2do parcial | `teoria/02 - Sistema de Gestión de Bases de Datos - Primer parcial.md` | Diapositivas: lenguajes del SGBD, SQL dual (p. 20), tipos de datos de SQL Server (p. 27), 1FN/2FN/3FN con la factura (p. 34-36) |
| 2do parcial | `teoria/03 - Teoria_Bases_de_Datos_cap._1.md` | SQL como lenguaje de 4ta generación, autocontenido/huésped, navegacional o de conjuntos (p. 11-13) |
| 1er parcial | `teoria/01 - Archivos.md` | Organizaciones de archivos; el indexado en p. 5-8 (lo toman los finales) |
| 1er parcial | `teoria/04 - Teoria_Bases_de_Datos_cap._2.md` | MER: identificador (unicidad y minimalidad, p. 6), cardinalidades, generalización |
| 1er parcial | `teoria/05`, `06`, `07` | Normalización, dependencias funcionales, FNBC y siguientes |
| 1er parcial | `practica/01-DER.md`, `02-DER_Extendido.md`, `Guia Practica 1` a `5` | DER y DER extendido |
| 2do parcial | `practica/03-DERaRelacional.md` | Las reglas DER &rarr; modelo relacional (la generalización recomendada, p. 17) |
| 2do parcial | `practica/Guia Practica 9.md` | Zoológico: tablas en 3FN y 20 consultas SQL |
| 2do parcial | `practica/Guia Practica 10.md` | Club náutico: tablas en 3FN y 22 consultas SQL |
| 2do parcial | `practica/Guia Practica 11 JJOO.md` | Olimpiadas (una sola tabla, datos en `PRACTICA/olimpiadas_*.sql`): 21 consultas |
| 2do parcial | `practica/Guia Practica 12.md` | Northwind (script de la cátedra en `PRACTICA/northwind.rar`): 17 consultas |

No hay apunte de la cátedra sobre sintaxis SQL ni sobre transacciones (ACID): la sintaxis sale del
script de Northwind (`CREATE TABLE` + `ALTER TABLE ... ADD CONSTRAINT ... FOREIGN KEY`), de las
guías 9 a 12 y del TP final del grupo (`TP FINAL/Entrega TP/*.sql`: `BEGIN TRAN`, `COMMIT`,
`IDENTITY`, `TOP`, `YEAR`, `MONTH`, `GETDATE`). Exámenes: fotos en `[ EXAMENES ]` (sin texto).
