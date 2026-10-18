# Guia Practica 5

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/PRACTICA/Guia Practica 5.pdf` · 3 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |

<!-- página 1 -->

Guía de Práctica N° 5 Bases de Datos - Facultad de Ciencia y Tecnología
1
Ejercicio 1:
Una biblioteca almacena información de los libros que toman en préstamo sus lectores.
Por cada libro se guarda un identificador único, el título y los datos de la editorial
(nombre, dirección y teléfono). Además se sabe a qué género pertenece (código y
descripción). La biblioteca dispone de varios locales a los que llama sucursales. Por cada
una tiene un identificador, nombre y dirección. Se dispone de una o varias copias de cada
libro, que se encuentran distribuidas por las sucursales. Les interesa saber por cada libro,
el número de copias asignadas a cada sucursal. Un ejemplar de un libro se puede
encontrar en un momento determinado físicamente en la sucursal a la que está asignado
o bien puede estar prestado a un lector. De éste último sabemos cuál es el número de su
tarjeta de socio (no hay dos lectores con el mismo número de tarjeta), su nombre,
dirección y teléfono. Van guardando que libros ha tomado prestado cada lector, de que
sucursal lo ha tomado y la fecha de préstamo y devolución. Como también suelen hacer
consultas por autores, quieren almacenar los autores de cada libro. Ocurre que hay
autores diferentes que se llaman igual, así que además del nombre se almacenan con un
código único y su nacionalidad.
Ejercicio 2:
Diseñar un diagrama E/R que represente la siguiente información sobre un mundial de
futbol. Para cada equipo participante se conoce el código con el cual se identifica, nombre
del país, el grupo en el que participa y color de la camiseta. Además es fundamental que
se pueda saber a cada momento la cantidad de partidos jugados, goles a favor y goles en
contra. Para cada partido jugado entre dos equipos (pueden jugar entre sí más de una vez
si pasan la fase de grupos) se almacena la fecha en la que se jugó, el resultado y los
árbitros que dirigieron el partido (incluidos jueces de línea, etc.). De los árbitros se conoce
su nombre, edad y nacionalidad. Para cada jugador de cada equipo, se guarda su número
de identidad nacional, nombre, fecha de nacimiento, los clubes a los que ha pertenecido
dicho jugador, y los goles marcados en el mundial. Cuando finaliza el mundial todo ha
debido pasar por un control antidopaje obligatorio. Además, los jugadores pueden ser
requeridos para realizar uno o más controles adicionales. En cada control se registra la
fecha y el lugar en el que se realizó. Por cuestiones de organización se desea guardar
información sobre los hoteles en los que se aloja cada equipo. Los equipos jugarán los
partidos en diferentes sedes, por lo que se alojarán en distintos hoteles. En un mismo
hotel solo se alojará un único equipo en todo el mundial. Cada hotel se identifica con un
código, nombre, dirección y un teléfono. Cada equipo reserva un número concreto de
habitaciones en cada hotel. Este dato también es de interés.

<!-- página 2 -->

Guía de Práctica N° 5 Bases de Datos - Facultad de Ciencia y Tecnología
2
Ejercicio 3:
La empresa La Barcaza S.A. se dedica a administrar flotas de barcos de cargos. Los barcos
no pertenecen a la empresa, sino a algún dueño que le encarga a la empresa, la
administración de su barco. Es necesario contar con información de cada dueño,
mínimamente su nombre y tipo y número de documento. Además, todo barco tiene una
denominación y una bandera, es decir un país en el cual se encuentra registrado. Cada
barco tiene un historial de viajes, cada viaje tiene un puerto de origen y otro de destino,
una fecha de inicio y, si finalizó el viaje, una fecha de finalización. Cada barco tiene, por ser
de carga, varias bodegas por lo que es necesario registrar cada ingreso y egreso de
productos de las mismas. Los productos, según las normas de comercio internacional,
tienen una codificación denominada nomenclatura y una descripción. Cada nomenclatura
tiene diferentes clasificaciones, pero a esta empresa, por el momento solo le interesa su
clasificación entre producto primario y manufactura. La empresa tiene dos tipos de
empleados, los tripulantes de cada barco (que deben ser como mínimo 6) y los
supervisores de carga, que controlan la carga y descarga de los productos de las bodegas.
Cada empleado tiene su número de legajo, nombre, edad y sexo. La empresa cuenta con
un servicio de localización GPS, que cada intervalos regulares de tiempo, envía el
posicionamiento de cada barco (fecha, hora, barco, latitud, longitud). Los requerimientos
más urgentes para la empresa son: poder determinar las fechas en que la cantidad de un
determinado producto en bodegas de un barco, fue menor a cierto límite. Determinar el
barco más cercano a cierto puerto en un determinado momento. Determinar la
trayectoria de un barco en un intervalo de tiempo. Cuántos viajes empezaron de un país y
terminaron en otro.
Ejercicio 4:
Las distintas sedes de la Facultad de Ciencia y Tecnología de la UADER desean ofrecer a
sus alumnos un servicio de colectivos para el traslado desde la localidad donde residen a
su centro de estudios. Para gestionarlo nos piden que diseñemos un esquema E/R que
registre la siguiente información:
Para cada sede que ofrece este servicio se desea guardar el código que la identifica, su
nombre, su dirección y localidad, y cuáles son los colectivos que ha contratado. Para cada
alumno universitario que usa el servicio de colectivos se almacena su número de libreta
universitaria, su nombre, las materias en las que está matriculado, la localidad donde
reside, y la sede en donde cursa. Además figura para cada alumno en que colectivos
puede viajar y para cada uno de ellos en qué fecha realizó la inscripción.

<!-- página 3 -->

Guía de Práctica N° 5 Bases de Datos - Facultad de Ciencia y Tecnología
3
Para cada colectivo contratado se dispondrá de su matrícula, número de asientos, nombre
de la empresa (hay colectivos que no pertenecen a ninguna empresa), y las paradas que
realiza para recoger y dejar a los alumnos que lo utilizan. Además, como cada sede
contrata los colectivos de forma exclusiva, cada colectivo está a disposición de una única
sede. De cada localidad incluida en el servicio de colectivos se tiene su código
identificativo, nombre, provincia y las paradas que realizan los diferentes colectivos en la
misma (puede haber más de una). Por cada parada de la localidad se almacena un número
único, la calle y la altura en la que está situada (ej Av. Ramírez al 2400). Una misma parada
puede ser utilizada por más de un colectivo. Distintas localidades pueden tener calles con
el mismo nombre.
Ejercicio 5:
Se quiere modelar la realidad relativa a una clínica odontológica. La clínica está compuesta
por varios locales de atención, identificados por su nombre, de los cuales se conoce
además, su dirección dada por la ciudad donde se ubica, la calle y el número. En cada local
existen varios consultorios que se identifican por un número dentro del local y en cada
consultorio existe cierto equipamiento. Dicho equipamiento se identifica globalmente
mediante un número serie, se conoce el tipo (torno, laser, etc.) e interesa mantener
registro de la última fecha en que se realizó mantenimiento. La clínica posee dos planes
diferentes de afiliación: individual y grupal. De los afiliados se conoce DNI, el nombre y
uno o más teléfonos. Para los afiliados grupales interesa saber el nombre del convenio de
afiliación y el porcentaje de rebaja que se debe aplicar a la cuota mensual. En la clínica se
realizan tratamientos, los cuales se identifican por su nombre y tienen un costo asociado.
Los odontólogos que trabajan en la clínica se identifican por su nombre. De ellos se
conoce su especialidad principal dentro de la odontología y los diferentes tratamientos
que pueden realizar. Los odontólogos trabajan en diferentes locales y cada odontólogo
puede tener distintos horarios de atención en cada local. De cada horario de atención se
conoce el día de la semana, la hora de comienzo y la hora de finalización. (Ej. lunes de
16:00 a 18:30). Los afiliados se atienden con determinados odontólogos en determinado
local y además los odontólogos les realizan tratamientos. Para que un paciente pueda
recibir tratamiento de un odontólogo debe ser atendido previamente por este. Interesa
mantener la historia clínica de cada afiliado, la cual consiste por un lado, en un registro de
cada consulta indicando la fecha de consulta, el odontólogo y el local, y por otro, interesa
saber: fecha de inicio, si el tratamiento ha finalizado o no y la identificación del
odontólogo que lo realizó, teniendo en cuenta que como política de la clínica un
odontólogo solo puede practicar un tratamiento por vez a cada afiliado. El inicio de un
tratamiento siempre se hace de una consulta.
