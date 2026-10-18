# 01-DER

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/PRACTICA/01-DER.pdf` · 17 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |
| 9 |  |
| 10 |  |
| 11 |  |
| 12 |  |
| 13 |  |
| 14 |  |
| 15 |  |
| 16 |  |
| 17 |  |

<!-- página 1 -->

Bases de datos
Diagrama Entidad-Relación

<!-- página 2 -->



<!-- página 3 -->

El diseño de una base de datos se realiza en tres fases:
● Diseño conceptual
● Diseño lógico
● Diseño físico

<!-- página 4 -->

● Diseño conceptual
 Diagrama Entidad Relación (DER)

<!-- página 5 -->

Diagrama Entidad Relación
● Entidades
Alumno

<!-- página 6 -->

Diagrama Entidad Relación
● Entidades
● Atributos
Alumno
Legajo
Nombre
Apellido

<!-- página 7 -->

Diagrama Entidad Relación
● Entidades
● Atributos
● Identificador
○ Unicidad
○ Minimalidad
Alumno
Legajo
Nombre
Apellido

<!-- página 8 -->

Diagrama Entidad Relación
● Entidades
● Atributos
● Identificador
○ Unicidad
○ Minimalidad
Alumno
Legajo
Nombre
Apellido
Materia
Código
Nombre

<!-- página 9 -->

Diagrama Entidad Relación
● Entidades
● Atributos
● Identificador
○ Unicidad
○ Minimalidad
● Relaciones
Alumno
Legajo
Nombre
Apellido
Materia
Cursa
Código
Nombre

<!-- página 10 -->

Diagrama Entidad Relación
● Entidades
● Atributos
● Identificador
○ Unicidad
○ Minimalidad
● Relaciones
Alumno
Legajo
Nombre
Apellido
Materia
Cursa
Código
Nombre
Fecha inscripción

<!-- página 11 -->

Diagrama Entidad Relación
Empleado DepartamentoDirige
(0,1) (1,1)

<!-- página 12 -->

Diagrama Entidad Relación
Empleado DepartamentoDirige
Empleado DepartamentoTrabaja
en
(0,1) (1,1)
(1,1) (1,n)

<!-- página 13 -->

Diagrama Entidad Relación
Empleado DepartamentoDirige
Empleado DepartamentoTrabaja
en
Empleado ProyectoTrabaja
en
(0,1) (1,1)
(1,1) (1,n)
(1,n) (1,m)

<!-- página 14 -->

Diagrama Entidad Relación
Pasos a seguir:
1. Identificar Tipos de Entidad y las relaciones que existen entre ellos.
2. Identificar los atributos para cada elemento.
3. Definir identificadores para los tipos de entidad.
4. Definir restricciones de pertenencia y cardinalidad.

<!-- página 15 -->

Ejercicio
Una empresa de software desea contratar nuevos programadores. De los candidatos se
conoce su dni, nombre, apellido y teléfono.
Para realizar las entrevistas, eligen a sus empleados con mayor experiencia. Entre otras, se
les pregunta a los candidatos, qué lenguajes de programación conocen y cuántos años de
experiencia tienen con cada uno ellos, lo que es fundamental para luego concretar las
contrataciones.
De cada lenguaje de programación se almacena un código, nombre del lenguaje y el tipo (si
es estructurado u orientado a objetos).
Por último, también se quiere saber quién fue el empleado que entrevistó a cada candidato.
De los entrevistadores se sabe, legajo, nombre, apellido, fecha de ingreso a la empresa.

<!-- página 16 -->

Programador Lenguaje
Empleado

<!-- página 17 -->

Programador LenguajeConoce
EmpleadoEntrevista
Experiencia
Código
Nombre
Tipo
Legajo
Nombre
Apellido
Fecha ingreso
DNI
Nombre
Apellido
Telefono
(1,1)
(0,N)
(1,n) (0,n)
