# Guia Practica 9

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/PRACTICA/Guia Practica 9.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |

<!-- página 1 -->

Guía de Práctica N° 9 Bases de Datos - Facultad de Ciencia y Tecnología
1
Información del zoológico
En un zoológico, las distintas especies de animales están alojados organizados en zonas
dentro del parque. Además de la zona en la que se encuentra cada especie, se conoce un
código, su nombre, nombre científico y una descripción de la especie.
Las zonas son identificadas por un código, nombre y extensión de la misma en m2.
De los empleados se conoce su número de legajo, nombre, dirección, teléfono y fecha de
ingreso. Un empleado puede ser cuidador o guía. Los cuidadores tienen asignados una o
más especies, conociéndose la fecha en que se hace cargo de cada especie.
Por otro lado, los guías son quienes se encargan de acompañar a los visitantes a través de
los distintos itinerarios que hay para recorrer el parque. De estos itinerarios se conoce un
código, duración. longitud y la cantidad máxima de visitantes que permite. También se
conoce cuáles zonas del parque son visitadas por cada itinerario. Un guía puede participar
en más de un itinerario, y un itinerario puede ser recorrido por más de un guía. Para cada
uno de estos casos se sabe la hora en que se realiza.

<!-- página 2 -->

Guía de Práctica N° 9 Bases de Datos - Facultad de Ciencia y Tecnología
2
A partir del diagrama, crear las tablas en 3FN y luego resolver las siguientes consultas con
SQL:
1. Listado completo de especies.
2. Listado de especies ubicadas en una zona dada.
3. Nombre y teléfono de los cuidadores a cargo de una especie dada.
4. Listado de todos los empleados del parque indicando quienes son guías y quienes
cuidadores.
5. Listado de guías definidos para un itinerario ordenados por hora.
6. Detalle de cada zona, extensión y cantidad de especies que aloja.
7. Guías que entraron a trabajar en el último mes.
8. Empleados con más de 10 años de antigüedad.
9. Nombre de la especie y fecha en la que se hizo cargo de la misma cada cuidador.
10. Promedio de duración de todos los itinerarios.
11. Nombre de la zona de mayor extensión.
12. Listado de itinerarios que recorren una zona dada.
13. Cantidad de itinerarios que visitan cada zona.
14. Indicar por cada itinerario la relación longitud sobre duración, ordenados de mayor
a menor siendo los mayores los más exigentes.
15. Indicar los itinerarios cuya duración este por encima del promedio.
16. Listado de itinerarios que pueden visitar determinada especie.
17. Listado de empleados que no tengan especies a cargo ni lleven ningún itinerario.
18. Listado de cuidadores y la cantidad de especies a cargo tiene cada uno.
19. Cuidadores con más de 5 especies a cargo.
20. Nombre de la especie con mayor número de cuidadores.
