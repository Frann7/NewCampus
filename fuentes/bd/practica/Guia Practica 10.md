# Guia Practica 10

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/PRACTICA/Guia Practica 10.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |

<!-- página 1 -->

Guía de Práctica N° 10 Bases de Datos - Facultad de Ciencia y Tecnología
1
Información del Club Náutico
Un club náutico desea tener informatizados los datos correspondientes a sus
instalaciones, empleados, socios y embarcaciones que se encuentran en dicho club. El club
está organizado de la siguiente forma:
Los socios pertenecientes al club vienen definidos por su nombre, dirección, DNI y fecha
de ingreso al club.
Las embarcaciones viene definidas por matrícula, nombre, tipo y dimensiones.
Los amarres tienen como datos de interés el número de amarre, la lectura del medidor de
agua y luz, y si tienen o no servicios de mantenimiento contratados.
Por otro lado hay que tener en cuenta que una embarcación pertenece a un socio,
mientras que un socio puede tener varias embarcaciones. Una embarcación ocupará un
amarre y un amarre está ocupado por una sola embarcación. Es importante la fecha en
que una embarcación fue asignada a un amarre.
Los socios pueden ser propietarios de amarres, siendo de interés la fecha de adquisición.
Hay que tener en cuenta que un amarre pertenece a un único socio y que no hay ninguna
relación directa entre la fecha en la que se compra un amarre y en la que una
embarcación se asigna al amarre.
El club náutico está dividido en varias zonas definidas por una letra, el tipo de barco que
contiene, la profundidad y el ancho de los amarres. Una zona tendrá varios amarres y una
amarres pertenece a una sola zona.
En cuanto a los empleados, estos vienen definidos por su código, nombre y teléfono. Un
empleado está asignado a varias zonas y/o a amarres individuales. Además, en una zona
puede haber más de un empleado asignado.
Número
LecturaAgua
LecturaLuz
Mantenimiento
FechaDesde
FechaDesde
(1,1)
(1,n)
(1,n)
(1,1) (1,1)
(1,1) (1,1)
(1,1)
R4
(1,n)
(1,n) (1,n)
(1,n)
Amarre
TipoEmbarcación
Empleado Zona
Embarcación
R1
R2
Letra
Profundidad
AnchoAmarres
DNI
Nombre
Dirección
FechaIngreso
Código
Nombre
Teléfono
Código
Descripción
Socio
R3
(1,n)
(1,n)
R5
R6
R7
Matrícula
Nombre
Dimensión

<!-- página 2 -->

Guía de Práctica N° 10 Bases de Datos - Facultad de Ciencia y Tecnología
2
A partir del diagrama, crear las tablas en 3FN y resolver las siguientes consultas con SQL:
1. Listado completo de socios.
2. Seleccionar todos los socios que ingresaron este año.
3. Seleccionar un listado de las embarcaciones ordenadas por matrícula.
4. Listado de nombre de socio, dni, y cantidad de embarcaciones que posee.
5. Identificar a que zona pertenece un amarre dado.
6. Listado de amarres disponibles, indicando la zona a la que pertenece.
7. Indicar el nombre y teléfono del propietario de una embarcación conocida su
matrícula.
8. Seleccionar los 10 socios con mayor antigüedad.
9. Listado de amarres ocupados por embarcaciones de terceros.
10. Calcular cantidad promedio de amarres por socio.
11. Nombre de los socios cuyos amarres tengan un consumo de luz superior al dado.
12. Calcular la cantidad total de amarres.
13. Calcular la cantidad de amarres por zona.
14. Indicar la zona con más cantidad de amarres.
15. Indicar los empleados asignados a la zona del punto anterior.
16. Listado de socios que no son propietarios de amarres.
17. Listado de socios que no son propietarios de embarcaciones.
18. Cantidad de amarres con servicio de mantenimiento contratado.
19. Listado de amarres a cargo de un empleado dado.
20. Listado de empleados que no tienen amarres asignados.
21. Listado de embarcaciones (matrícula, nombre, nombre del dueño, nombre del
dueño del amarre) que se encuentran en amarres asignados a un empleado
indicado.
22. Listado de empleados, indicando la cantidad de amarres que tiene a cargo cada
uno, ordenando por este criterio de mayor a menor.
