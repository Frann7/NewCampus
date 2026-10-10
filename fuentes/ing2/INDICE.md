# Ing. de Software II — índice de las fuentes en texto

Cada `.md` es el texto de un archivo de
`C:\Users\Fran\Desktop\SISTEMAS 3\ING 2\SEGUNDO CUATRIMESTRE\` (la ruta exacta está arriba de cada
uno). Primero el texto; el PDF solo en las páginas **⚠** o si algo no cierra
(`python fuentes/pagina.py "<PDF>" N`). Solo entra el **segundo cuatrimestre** (2do parcial).

- **Los diagramas UML no están en el texto.** En la teoría de patrones son las páginas ⚠ (vacías)
  de cada `.md`; en las prácticas, las páginas que dicen "el siguiente diagrama" traen una imagen.
- **`PATRONES/TEORIA/` no se sube al repo** (`.gitignore`): son recortes del libro *Sumérgete en
  los patrones de diseño* (Refactoring.Guru), que es pago. Queda solo en esta PC; si falta, se
  regenera con `extraer.py`.
- En la carpeta de origen hay copias repetidas (`Ingeniería de software 2\Cuatrimestre 2\`,
  `TEORIA EXTRA\` y la raíz): acá hay una sola de cada una, la **versión 2026** cuando hay dos.
- No se extrae: `Cuatrimestre 1\` (UML, ágiles, RUP: 1er parcial), `[TP]\` (trabajo en grupo, con
  nombres de compañeros), `[Resumenes]\` (resúmenes de otros alumnos) y las fotos de exámenes.

## Exámenes

| Archivo | Qué es |
| :-- | :-- |
| `EXAMENES/Parcial 2 2025.md` | Parcial del 8/10/2025, transcripto de las fotos. Teoría (50 pts): CMMI, Git, UML de 2 patrones, métrica. Práctica: patrones desde un enunciado y desde código PHP |
| `EXAMENES/Parcial 2 2024.md` | Parcial del 23/10/2024 (4 ejercicios, todos de patrones). ⚠ ej. 3: el diagrama (Usuario, Cliente, Farmacéutico, Medicamento) está en `EXAMENES\Parcial 2.jpg`. El código del ej. 4 (C++) sigue en la pág. 2 |

## Patrones de diseño

| Archivo | Qué es |
| :-- | :-- |
| `PATRONES/TEORIA/Introducción patrones de diseño.md` | Qué es un patrón, historia (GoF), críticas, clasificación y catálogo de los 8 que da la cátedra (6 p.) |
| `PATRONES/TEORIA/02 - Creacionales - Patrones de diseño.md` | Factory Method (p. 2-9), Abstract Factory (10-17), Singleton (18-21). ⚠ 6, 15, 20: pseudocódigo/estructura en imagen |
| `PATRONES/TEORIA/03 - Estructurales - Patrones de diseño.md` | Adapter (p. 2-8), Composite (9-14), Facade (15-20). ⚠ 6, 12, 18 |
| `PATRONES/TEORIA/04 - Comportamiento - Patrones de diseño.md` | Observer (p. 2-8), Strategy (9-14). ⚠ 6, 12 |
| `PATRONES/PRACTICA/Guia Nº1 Ejercicios - Patrones crecionales.md` | 6 ej.: Singleton + Observer sobre un diagrama, Singleton en C++, TPV (Adapter), familias de productos (Abstract Factory), libro digital (Adapter). ⚠ 1, 3, 4: diagramas |
| `PATRONES/PRACTICA/Guia Nº2 Ejercicios - Patrones estructurales.md` | 5 ej.: Adapter en C++, Composite en PHP, Facade en C#, libro digital, multimedia (Composite + Facade + Adapter) |
| `PATRONES/PRACTICA/Guia Nº3 Ejercicios - Patrones de comportamiento.md` | 4 ej.: ejemplos de Observer y Strategy, UML de Observer, Strategy en PHP, Observer en C++ |
| `PATRONES/PRACTICA/practica 1 patrones.md` | Parte 1: 4 ej. sobre diagramas (docente único, ConexionDB, vehículos, tienda con fachada) |
| `PATRONES/PRACTICA/practica 2 patrones.md` | Parte 2: 6 ej. (libro digital, Archivo con exportadores, directorios, expresiones matemáticas, familias de productos). ⚠ ej. 4: imagen |
| `PATRONES/PRACTICA/Practica_integral_patrones1.md` | Partes 1, 2 y 3 juntas (2023): repite las dos anteriores y la adicional. ⚠ diagramas en imagen |
| `PATRONES/PRACTICA/PRACTICA ADICIONAL DE PATRONES.md` | 2 enunciados integradores sobre un diagrama: expedientes y gestión de contenido (Composite + Singleton + Observer + Factory). ⚠ diagramas |
| `PATRONES/PRACTICA/Practica_03_patrones_subir.md` | 3 ej.: Adapter (gráficos), Facade (tienda en línea), Composite (empleados) |
| `PATRONES/PRACTICA/Ejercicios de patrones.md` | 3 enunciados de creacionales (enemigos, UI multiplataforma, conexiones a BD) |
| `PATRONES/PRACTICA/Ejercicios_patrones_singleton_subir.md` | 3 ej. de Singleton (configuración, registro de eventos, administrador de BD) |
| `PATRONES/PRACTICA/Ej. Patrones de Diseño.md` | El ej. 1 de la Guía 1, suelto |

## Calidad, métricas y gestión de cambios

| Archivo | Qué es |
| :-- | :-- |
| `CALIDAD/Calidad de software.md` | Apunte 2026 (24 p.): definición, consecuencias de la baja calidad, atributos, estándares, técnicas, mejora de procesos (PI), **CMMI** (p. 19-22: niveles, beneficios, equipos), ejemplo práctico por nivel y con IA (p. 23-25) |
| `CALIDAD/IS2 - Calidad de Software - Ejercicios prácticos.md` | 2 ejercicios de diagnóstico CMMI (nivel 1; del nivel 2 al 5) |
| `CALIDAD/Practica 2  CMMI.md` | 5 casos para diagnosticar el nivel y proponer cómo subir (clínica, universidad, servicios, banco, fábrica de software) |
| `CALIDAD/Ingenieria_de_Software_II_Agentes_IA.md` | Diapositivas 2026 (9): qué es un agente de IA para programar, Codex, Claude Code, OpenCode, responsabilidad del desarrollador |
| `CALIDAD/Ingenieria_de_Software_II_Docker.md` | Diapositivas 2026 (7): qué es Docker, imagen/contenedor, vs. máquinas virtuales, Kubernetes |
| `TEORIA/Métricas.md` | Apunte (16 p.): definición y **atributo / medida / unidad / métrica / indicador** (p. 4), ciclo de vida (6), ventajas, tipos de métricas (9-12), CMMI (13), complejidad ciclomática (14-15), IA (16) |
| `CALIDAD/Gestión de cambios.md` | Apunte 2026 (30 p.): gestión de cambios vs. configuración vs. control de versiones (p. 3-4), problemas sin control de versiones (7-8), centralizado vs. distribuido (9-11), **Git**: tres estados y flujo básico (12-16), claves SSH (17-18), init/clone, commit, ramas, PR, merge y conflictos (19-22), **versionado semántico** (23-26), gestores de dependencias (27-30) |
