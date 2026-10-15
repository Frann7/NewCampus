# Traductores-Compiladores

Fuente: `C:/Users/Fran/AppData/Local/Temp/claude/C--Users-Fran-Desktop-NewCampus/196b4912-5fa9-4a20-89f0-578e09e99c9b/scratchpad/pyl-pdf/TOPIC 1/Traductores-Compiladores.pdf` · 16 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |
| 9 |  |
| 10 |  |
| 11 |  |
| 12 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 13 |  |
| 14 |  |
| 15 |  |
| 16 |  |

<!-- página 1 -->

1
Introducción
Traductores - Compilador
Paradigmas y Lenguajes

<!-- página 2 -->

2
Evolución de los Lenguajes de
programación
◼ 1940
◼ “que funcione”
◼ prelingual: previo a los lenguajes conocidos
◼ 1950
◼ ensambladores
◼ cálculo numérico (FORTRAN)
◼ “explotación de la potencia de la máquina”
◼ 1960
◼ COBOL, LISP, ALGOL, BASIC
◼ estructuras de datos
◼ recursividad
◼ “aumento de la expresividad”
◼ 1970
◼ reducción de la dependencia de la máquina: portabilidad
◼ aumento de la correctitud de los programas
◼ PASCAL, ALGOL 68, C
◼ 1980:
◼ “reducción/manejo de la complejidad”
◼ MODULA 2, ADA (introduce paralelismo(ejecutar con varios procesadores)-> programación concurrente
(aplicaciones militares)), SMALLTALK(primer lenguaje de O.O. puro), MIRANDA.
◼ 1990
◼ paralelo, distribuido(un programa es dividido en varias computadoras, división de tareas a través de la red. Ej.:
cliente - servidor)
◼ lenguajes visuales
◼ 2000
◼ programación WEB/interacción entre varios lenguajes

<!-- página 3 -->

3
Clasificación por Paradigmas
◼ Programación Imperativa
◼ Programación Estructurada
◼ Programación Funcional
◼ Programación Orientada a Objetos
◼ Programación Lógica

<!-- página 4 -->

4
Clasificación por Nivel
◼ Nivel de Abstracción
◼ Bajo: instrucciones simples. El manejo de la memoria
es explícito. Ej.: ensambladores
◼ Alto: manejan estructuras de control que hacen
menor referencia a la forma de tratamiento en la
computadora. Acceso a memoria explícita.
◼ Muy alto: nivel de abstracción mayor. Máquinas
totalmente abstractas. Máquina virtual. El acceso a
memoria es implícito.

<!-- página 5 -->

5
Clasificación por Generación
◼ Generaciones
◼ 1ª generación: lenguaje máquina
◼ 2ª generación: lenguaje ensamblador
◼ 3ª generación: lenguajes procedurales (imperativos)
◼ 4ª generación: lenguajes de aplicación: Ej. SQL.
Lenguajes declarativos: especifican qué se quiere hacer y no
cómo se debe hacer
◼ 5ª generación: técnicas de inteligencia artificial y lenguajes de
inferencia
◼ 6ª generación: redes neuronales: simulan el comportamiento de
las neuronas del cerebro humano.

<!-- página 6 -->

6
Traductores
◼ Traductor: (Translator)
◼ Es un programa que toma como entrada un programa
escrito en un lenguaje (programa fuente) y lo convierte
a un programa equivalente (en cuanto a su significado)
escrito en otro lenguaje (programa objeto)

<!-- página 7 -->

7
Traductores
◼ Compilador: programa que transforma un programa escrito en
un lenguaje de alto nivel (por ejemplo Pascal, C, Java,
Smalltalk, etc), en otro programa equivalente escrito en un
lenguaje de bajo nivel (normalmente Ensamblador).
◼ Ensamblador: convierte de bajo nivel a bajo nivel
(ASSEMBLER a lenguaje máquina).
◼ Preprocesador: convierte de alto nivel a alto nivel.
◼ Intérprete: convierte y ejecuta instrucción por instrucción. Ej.:
BASIC, PERL, SMALLTALK, PHP

<!-- página 8 -->

8
Traductores
◼ Comparación entre compilador e intérprete

<!-- página 9 -->

9
Traductores
◼ Objetivos de la traducción
◼ Conversión del programa
◼ Detección de errores
◼ Tipos de errores
◼ Léxicos: en los componentes atómicos del lenguaje
◼ Sintácticos: en la estructura del programa
◼ Semánticos: en cuanto al significado del programa
- de tipo / declaración
- lógicos
- conceptuales (aplicación de conceptos)
- de comprensión del problema / requerimientos
- Otros (dependientes de la arquitectura / S.O. /
configuración

<!-- página 10 -->

10
Traductores
◼ Herramientas del entorno de la traducción (IDE)
◼ Editores de estructura (inteligentes)
◼ Impresores estéticos
◼ Verificadores estáticos
◼ Depuradores (debugger)
◼ Ayuda sensible al contexto
◼ Perfiladores (profiler)

<!-- página 11 -->

11
Sistema de procesamiento de un
lenguaje

<!-- página 12 -->

12
Compilación

<!-- página 13 -->

13
Fases de la Compilación
◼ Fase: división conceptual del proceso de compilación
Análisis Léxico
Análisis Sintáctico
Análisis Semántico
Generación de código intermedio
Optimización
Generador de código
Programa fuente
Programa objeto
Análisis
Síntesis
Administrador de la
Tabla de Símbolos
Manejador de Errores

<!-- página 14 -->

14
Fases: ejemplo de Compilación

<!-- página 15 -->

15
Fases
Ventajas de la división en fases:
Reduce la complejidad del proceso
Independencia de la arquitectura, S.O. y léxico (portabilidad,
compiladores “cruzados”)
Conocimientos, técnicas y herramientas especializadas
Compiladores de compiladores
Generadores de analizadores léxicos: LEX
Generadores de analizadores sintácticos: YACC
Dispositivos de traducción
Pasada:
División física de la compilación. Compila por partes, dejando archivos con
representaciones intermedias. La mayoría de los compiladores actuales
son de una sola pasada.

<!-- página 16 -->

16
Traductores, Compiladores
Fin
