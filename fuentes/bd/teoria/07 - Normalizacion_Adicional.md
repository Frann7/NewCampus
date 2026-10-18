# 07 - Normalizacion_Adicional

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/APUNTES DE LA MATERIA/07 - Normalizacion_Adicional.pdf` · 10 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

BASES DE DATOS Normalización Adicional
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 1
FORMA NORMAL BOYCE-CODD
La forma normal de Boyce-Codd requiere que no existan dependencias funcionales
no triviales de los atributos que no sean un conjunto de la clave candidata. En base
de datos un atributo determinante es un atributo del que depende funcionalmente
de manera completa algún otro atributo. Todo determinante es una clave
candidata.
Como una tabla está en Forma Normal de Boyce-Codd si solo existen dependencias
funcionales elementales que dependan de la clave primaria o de cualquier clave
alternativa. Si la clave primaria está formada por un solo atributo y está en 3FN,
ésta a su vez está en FNBC. Cómo en una tabla en 3FN, todos los atributos
dependen de una clave, de la clave completa y de ninguna otra cosa excepto de la
clave (excluyendo dependencias triviales).
Definición: Se dice que una tabla está en FNBC si y solo si está en 3FN y cada
dependencia funcional no trivial tiene una clave candidata como determinante.
En términos menos formales, una tabla está en FNBC si está 3FN y los únicos
determinantes son claves candidatas.
La 2FN y la 3FN eliminan las dependencias parciales y las dependencias transitivas
de la clave primaria. Pero este tipo de dependencias todavía pueden existir sobre
otras claves candidatas, si éstas existen. La BCFN es más fuerte que la 3FN, por lo
tanto, toda relación en BCFN está en 3FN.
La violación de la BCFN es poco frecuente ya que se da bajo ciertas condiciones que
raramente se presentan. Se debe comprobar si una relación viola la BCFN si tiene
dos o más claves candidatas compuestas que tienen al menos un atributo en
común.
Un ejemplo típico para mostrar una tabla que, estando en 3FN, mantiene
dependencias funcionales, puede ser una tabla que posee los atributos Dirección,
Código Postal y Ciudad, deduciendo que a ciudades diferentes le corresponden
códigos postales distintos.

<!-- página 2 -->

BASES DE DATOS Normalización Adicional
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 2
Tabla en tercera forma normal
CPost Dir Ciudad
2000 Las Flores N°17 Rosario
4400 Av. Bolívar Nº72 Salta
En este caso hay dependencia entre el Código Postal y la Ciudad, ya que, conocido
el Código Postal se puede conocer la Ciudad, y conocida la Dirección y la Ciudad, se
conoce el Código Postal.
Para transformar la tabla en una tabla en FNBC se crea una tabla de Códigos
Postales y Ciudades, eliminando de la tabla original la Ciudad, obteniéndose dos
tablas, una con los atributos Dirección y Código Postal y otra con el Código Postal
y la Ciudad
Tabla en forma normal de Boyce-Codd
CodPostal Dir
2000 Las Flores N°17
4400 Av. Bolívar Nº72
Tabla en forma normal de Boyce-Codd
CodPostal Ciudad
2000 Rosario
4400 Salta
En la mayoría de los casos, las relaciones en 3FN estarán en FNBC. Para Validar
esto se deben ubicar todos los determinantes existentes en la relación así como
todas las claves candidatas, se comparan ambos conjuntos y si encuentra que hay
algún determinante que no resulta ser clave candidata se demuestra que no está
en FNBC. Se comprueba que la relación está en 1FN, todos los atributos son
atómicos. También está en 2FN ya que no hay dependencias funcionalmente
completas entre atributos que no sean clave (formen parte de la clave). Y
finalmente se verifica que no hay ningún atributo que dependa de forma transitiva
de la clave Primaria, luego está en 3FN. Usualmente se considera aceptable tener
relaciones que lleguen sólo hasta la FNBC.

<!-- página 3 -->

BASES DE DATOS Normalización Adicional
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 3
La definición de la 3FN no produce diseños satisfactorios cuando se dan las
siguientes condiciones, o lo que es lo mismo, cuando una relación NO ESTE EN
FNBC concurrirán las siguientes circunstancias:
 Existen varias claves candidatas.
 Las claves candidatas son compuestas.
 Las claves candidatas se encubren, tienen al menos un atributo en común.
No hay un teorema sobre la división de la relación, el motivo es que no se puede
asegurar que al descomponer una relación en dos para conseguir la FNBC el
significado de las relaciones obtenidas se corresponda semánticamente a lo que
representa la relación inicial. En otras palabras, se puede tomar una decisión
equivocada al descomponer ya que puede que perdamos parte de la semántica de
la relación anterior.

<!-- página 4 -->

BASES DE DATOS Normalización Adicional
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 4
CUARTA FORMA NORMAL (4FN)
Se dice que una tabla que está en forma normal de Boyce-Codd y de la cual se
eliminan las dependencias multivaluadas y se generan todas las relaciones externas
con otras tablas u otras bases de datos; es una tabla en 4 Forma Normal
Definición: Una relación está en 4FN si ya está en la FNBC y además no existen
dependencias multivaluadas. Es decir, no se aceptan atributos que dependan
de un multivalor.
Veamos un primer ejemplo:
FIGURA COLOR TAMAÑO
Esfera Rojo Grande
Esfera Verde Grande
Cubo Blanco Grande
Cubo Azul Grande
Pirámide Blanco Mediano
Pirámide Blanco Grande
Pirámide Rojo Grande
La Figura determina valores múltiples de Color, Tamaño y Color, Tamaño. Todas
estas son independientes entre sí si estuvieran separadas. Sin embargo se repiten:
Esfera grande, Pirámide blanco y Pirámide grande. Estas repeticiones entre la figura
y el tamaño hace que no esté en 4 Forma Normal.
La solución al planteamiento anterior, es realizar dos tablas en la que se encuentre
en una de ellas: La figura y el color. Y en otra de ellas: La figura y el tamaño.
T_COLOR(FIGURA, COLOR)
T_TAMAÑO(FIGURA,TAMAÑO)
Al hablar de dependencia funcional multivaluadas o de múltiples valores, se refiere
a la existencia de la relación que pudiera darse por ejemplo dados tres atributos de
una tabla, si para cada valor del primer atributo existen múltiples valores en el
segundo atributo y no hay ninguna relación entre el tercer atributo y el primero, a
no ser a través del segundo atributo.

<!-- página 5 -->

BASES DE DATOS Normalización Adicional
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 5
Estas dependencias multivaluadas de la clave con los atributos que no forman
parte de la misma son dependencias triviales, por lo que algunos autores dicen que
no existen dependencias multivaluadas en 4FN.
Las dependencias multivaluadas sólo se presentan si existen tres atributos y
cuando lo hacen es a pares, es decir ocurre que Y es multidependiente de X y Z es
también multidependiente de X.
Consideremos que los atributos de una tabla “Transporte” son Conductor, Tipo de
Vehículo y Tipo de Carga, formando los tres campos la clave primaria. A cada
Conductor se le puede asignar un Vehículo u otro y cada Vehículo puede
transportar varios Tipos de Carga.
Tabla que NO está en cuarta forma normal
Transporte
Conductor Tipo Vehículo Tipo Carga
Juan Camioneta Perecederos
Marcos Camioneta Perecederos
Juan Camioneta Muebles
Marcos Camioneta Muebles
Juan Camión Mudanza
Marcos Camión Mudanza
Bajo estas condiciones, los Conductores son independientes de la carga; el Tipo de
Vehículos depende del Conductor y el Tipo de Vehículo depende de la Carga.
En este caso hay dependencias funcionales multivaluadas, ya que algunos atributos
que forman la clave dependen de otro atributo que también la forman.
Para conseguir que esta tabla esté en 4FN se necesita crear dos nuevas tablas en
lugar de la tabla actual, manteniendo en cada una de ellas una dependencia
múltiple. La primera tabla tendrá los atributos conductor y tipo de vehículo y la
segunda, tipo de vehículo y tipo de carga. De este modo la tabla en 4FN debido a
que la clave primaria de ambas tablas son todos los campos que la forman.

<!-- página 6 -->

BASES DE DATOS Normalización Adicional
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 6
Resultado:
Tabla en cuarta forma normal
Tipo Vehículo Tipo Carga
Camioneta Perecederos
Camioneta Muebles
Camión Mudanza
Tabla en cuarta forma normal
Conductor Tipo Vehículo
Juan Camioneta
Marcos Camioneta
Juan Camión
Marcos Camión
En las relaciones varios-con-varios, entidades independientes no pueden ser
almacenadas en la misma tabla.
La 4FN es en cierto modo bastante compleja de identificar, hay que tener muy
claro sobre todo el significado de lo que representa la relación analizada.
Algo que es vital y que se aplica para cualquier estado de la normalización es que
se debe tener siempre en cuenta el significado semántico de las relaciones, de lo
contrario se puede caer en el error de descomponer o diseñar una base de datos
que esté correcta.
Una relación está en cuarta forma normal (4FN) si está en FNBC y todas las
dependencias multivaluadas en ella son de hecho dependencias funcionales.

<!-- página 7 -->

BASES DE DATOS Normalización Adicional
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 7
QUINTA FORMA NORMAL: 5FN
Una relación está en Quinta Forma Normal (5FN) o Forma Normal de Proyección-
Unión, si está en 4FN y las únicas dependencias que existen son las dependencias
de unión de una tabla con sus proyecciones relacionándose entre las distintas
proyecciones mediante la clave primaria o cualquier clave alternativa. La 5FN se
emplea cuando en una misma tabla tenemos mucha información redundante, con
pocos atributos o cuando una tabla posee una gran cantidad de atributos y se hace
por ello inmanejable.
Una Proyección es una sub-tabla de la tabla principal, que se obtiene de seleccionar
una o varias columnas de la tabla principal. Se incluyen todas las filas y algunas
columnas.
Una Unión es una tabla resultante de efectuar la operación JOIN entre dos tablas
dadas, las cuales deben coincidir en al menos un atributo.
1° CASO
Cuando una tabla (en 4FN), tiene un gran número de atributos que dificultan su
gestión, se divide dicha tabla en dos o más tablas que estarán vinculas por la clave
primaria de la tabla inicial (join). De esta manera se logra agrupar los atributos de
acuerdo a la conveniencia del diseñador.
Tabla CLIENTES en 4FN
ID-Cliente DNI Nombre Dirección Teléfono Email
25 26280460 Victor Alem 364 4318025 victor@gmail.com
26 18604988 Carlos Salta 804 4243987 carlos@hotmail.com
27 29800143 Luis Perú 450 4228000 luis@yahoo.com
28 16302240 Juan Carbó 900 4312744 juan@gmail.com
5FN
Tabla CLIENTES_PRINCIPAL
ID-Cliente DNI Nombre
25 26280460 Victor
26 18604988 Carlos
27 29800143 Luis
28 16302240 Juan

<!-- página 8 -->

BASES DE DATOS Normalización Adicional
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 8
Tabla CLIENTES_UBICACIÓN
ID_Cliente Dirección Teléfono Email
25 Alem 364 4318025 victor@gmail.com
26 Salta 804 4243987 carlos@hotmail.com
27 Perú 450 4228000 luis@yahoo.com
28 Carbó 900 4312744 juan@gmail.com
2° CASO
Sea la siguiente tabla en 4FN
Psiquiatra Obra_Social Condición
Dr. Hernández IOSPER Ansiedad
Dr. Hernández IOSPER Depresión
Dr. Bran OSDE OCD
Dr. Bran OSDE Ansiedad
Dr. Bran OSDE Depresión
Dr. Cárdenas OSDE Esquizofrenia
Dr. Cárdenas IOSPER Ansiedad
Dr. Cárdenas IOSPER Demencia
Dr. Cárdenas GALENO Trastorno de conversión
El psiquiatra puede ofrecer tratamiento con reintegro a los pacientes que sufren de
la condición dada y que tienen cobertura de su Obra Social. En ausencia de
cualquier regla que restrinja las combinaciones válidas posibles de psiquiatra, obra
social y condición, la tabla de tres atributos Psiquiatra-Obra_social-Condición es
necesaria para modelar la situación correctamente.
El resultado de aplicar la 5FN son tres tablas en donde se aplicó la Proyección y la
Unión (Join), ya que para obtener información Psiquiatra-Obra_Social-Condición se
debe consultar y vincular las tres tablas.

<!-- página 9 -->

BASES DE DATOS Normalización Adicional
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 9
5FN
Psiquiatra Condición
Dr. Hernandez Ansiedad
Dr. Hernandez Depresión
Dr. Bran OCD
Dr. Bran Ansiedad
Dr. Bran Depresión
Dr. Cárdenas Esquizofrenia
Dr. Cárdenas Ansiedad
Dr. Cárdenas Demencia
Dr. Cárdenas Trastorno de conversión
Obra_Social Condición
IOSPER Ansiedad
IOSPER Depresión
IOSPER Demencia
OSDE OCD
OSDE Ansiedad
OSDE Depresión
OSDE Trastorno emocional
OSDE Esquizofrenia
IOSPER Demencia
GALENO Trastorno de conversión
Psiquiatra Obra_Social
Dr. Hernandez IOSPER
Dr. Bran OSDE
Dr. Cárdenas OSDE
Dr. Cárdenas IOSPER
Dr. Cárdenas GALENO
Una relación está en 5FN si está en 4FN y además no existen restricciones
impuestas por el creador de la BD. Una restricción de este tipo puede ser por
ejemplo que una tabla se divida en subtablas. Esta forma normal tiene poca
aplicación práctica porque dificulta el diseño ya que genera un número enorme de
tablas.

<!-- página 10 -->

BASES DE DATOS Normalización Adicional
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 10
Definición formal : Un esquema de relaciones R está en 5FN con respecto a un
conjunto D de dependencias funcionales, de valores múltiples y de producto, si
para todas las dependencias de productos en D se cumple por lo menos una de
estas condiciones:
 (R1, R2, R3, ... Rn) es una dependencia de producto trivial.
 Toda Ri es una superclave de R.
La quinta forma normal se refiere a dependencias que son extrañas. Tiene que ver
con tablas que pueden dividirse en subtablas, pero que no pueden reconstruirse.
