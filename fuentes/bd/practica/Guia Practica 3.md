# Guia Practica 3

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/PRACTICA/Guia Practica 3.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |

<!-- página 1 -->

Guía de Práctica N° 3  Bases de Datos - Facultad de Ciencia y Tecnología

1

Ejercicio 1:
En un hospital quieren llevar un registro de las internaciones que se realizan en el mismo.
Cada una de las habitaciones del hospital están identificadas con un nro de habitación, y
además se conoce su capacidad máxima de camas. En cada habitación hay más de una
cama identificadas con un número de 1 a n según su ubicación dentro de la habitación.
Cuando se interna un paciente, se cargan los siguientes datos: tipo de documento,
número, nombre, apellido y fecha de nacimiento. Por cada internación se almacena un
nro de internación y la fecha de inicio de la misma. Durante la internación, el paciente
puede ser asignado a distintas camas, e inclusive de distintas habitaciones. Es necesario
almacenar el detalle desde y hasta cuando estuvo asignado el paciente a cada cama.

Ejercicio 2:
Se desea mantener una base de datos para una cadena de farmacias distribuida en
diferentes ciudades. Cada farmacia se identifica por un código de sucursal, un nombre de
fantasía, teléfono y localidad.
La empresa tiene además de los empleados propios, un grupo farmacéuticos que
supervisan cada farmacia. De todos ellos se conoce su nombre, apellido, fecha de
nacimiento y de los farmacéuticos además se tiene el nro de matrícula. Por cada ciudad
existe un único farmacéutico asignado; esto es, si en una ciudad hubiera más de una
farmacia, el mismo farmacéutico estaría afectado a todas las farmacias de esa ciudad.
Cada farmacia tiene a su vez su stock de medicamentos. Cada medicamento se identifica
por un código único de medicamento, la presentación (ampollas de 5 unidades, jarabe de
100ml, inyecciones por 10 unidades, pomada 60gr, etc.), la o las drogas que lo componen
y el laboratorio que lo comercializa. Por cada medicamento se mantiene su precio y la
cantidad en existencia del mismo. De los laboratorios se conoce su nombre, CUIT y
teléfonos.
El sistema deberá permitir consultar la base de datos de diferentes alternativas para
medicamentos compuestos por determinada droga, medicamentos de un laboratorio,
presentaciones de un medicamento, entre otras.

<!-- página 2 -->

Guía de Práctica N° 3  Bases de Datos - Facultad de Ciencia y Tecnología

2

Ejercicio 3:
Una empresa de software contrata programadores (dni, nombre, apellido, teléfono) y al
momento del ingreso estos deben explicitar que lenguajes de programación conocen. En
ese mismo momento la empresa le toma un examen a cada programador para cada
lenguaje de programación que conozca. De cada lenguaje se almacena un código, nombre
del lenguaje y el tipo (si es estructurado u orientado a objetos).
Para evaluar a los entrevistados, la empresa cuenta con exámenes ya preparados, de los
que se conoce la cantidad de ejercicios, el nivel de dificultad, la fecha de creación y el
texto del examen.
Es necesario, llevar un registro de que examen se utilizó para evaluar al programador en
cada lenguaje, como así también la calificación obtenida y en que fecha se realizó.

Ejercicio 4:
Una empresa en expansión necesita ordenar el sector de mantenimiento y reparación de
las PCs e impresoras de sus oficinas. Para hacerlo, desea incorporar el historial de los
problemas surgidos tanto de software como de hardware en los equipos, con un detalle
de fecha de reporte del problema, tipo de problema reportado, empleado que lo reportó,
estado del pedido, fecha de reparación y empleado a cargo de la misma, entre otros
datos. También necesita tener un stock actualizado de los materiales necesarios para las
reparaciones (placas, memorias,  discos, etc.) y cómo fueron asignados a las distintas
reparaciones reportadas.
Además la gerencia pretende tener un inventario actualizado de los equipos instalados en
cada oficina. Por cada equipo se tiene un nro único de inventario y una descripción. Cada
oficina pertenece a un sector de la empresa (Administración, gerencia, marketing y
mantenimiento). Los empleados están asignados a un solo sector, y se les conoce nro de
legajo, nombre, apellido y dirección (calle, nro, piso, dpto).
El sistema deberá permitir efectuar un seguimiento de los pedidos de reparación, del
estado del stock de materiales y del stock de PCs e impresoras. Además, deberá permitir
emitir estadísticas, por ejemplo de cantidad de reparaciones en un estado determinado,
por tipo de reparación y por sector, sectores con mayor cantidad de reparaciones
reportadas, pedidos con más de n días demora en resolución.
