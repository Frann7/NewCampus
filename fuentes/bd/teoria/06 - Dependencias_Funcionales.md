# 06 - Dependencias_Funcionales

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/APUNTES DE LA MATERIA/06 - Dependencias_Funcionales.pdf` · 9 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

BASES DE DATOS Dependencias Funcionales
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 1
Definición.
Una Dependencia Funcional es una restricción que se establece entre dos
conjuntos de atributos de la base de datos. Supongamos que nuestro esquema de
base de datos relacional tiene n atributos A1, A2, . . ., A n; pensemos que la base de
datos completa está descripta por un único esquema de relación universal R = { A1,
A2, . . ., An }
No sugerimos que vamos a almacenar la base de datos como una única tabla
universal; usamos este concepto sólo en el desarrollo de la teoría forma de las
dependencias de datos.
Definición. Una dependencia funcional, denotada por X → Y, entre dos
conjuntos de atributos X e Y que son subconjuntos de R, especifica un
restricción en las posibles tuplas que pueden formar un estado de
relación r de R. La restricción dice que dos tuplas t1 y t2 en r que
cumplen que t1[X] = t2[X], deben cumplir también que t1[Y] = t2[Y].
Esto significa que los valores del componente Y de una tupla de r dependen
de, o están determinados por, los valores del componente X;
alternativamente, los valores del componente X de una tupla únicamente (o
funcionalmente) determinan los valores del componente Y. Decimos
también que existe una dependencia funcional de X hacia Y, o que Y es
funcionalmente dependiente de X. La abreviatura de dependencia funcional
es DF. El conjunto de atributos X recibe el nombre de lado izquierdo de la DF,
mientras que Y es el lado derecho.
Por tanto, X determina funcionalmente a Y si para toda instancia r del
esquema de la relación R, no es posible que r tenga dos tuplas que coincidan
en los atributos de X y no lo hagan en los atributos de Y. Observe lo siguiente:
 Si una restricción de R indica que no puede haber más de una tupla con
un valor X concreto en cualquier instancia de relación r(R), es decir, que
X es una clave candidata de R, se cumple que X → Y para cualquier
subconjunto de atributos Y de R (ya que la restricción de clave implica
que dos tuplas en cualquier estado legal r(R) no tendrán el mismo valor X)
 Si X → Y en R, esto no supone que Y → X en R.

<!-- página 2 -->

BASES DE DATOS Dependencias Funcionales
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 2
Una dependencia funcional es una propiedad de la semántica o significado de los
atributos. Los diseñadores de la base de datos utilizarán su comprensión de la
semántica de los atributos de R (esto es, cómo se relacionan unos con otros) para
especificar las dependencias funcionales que deben mantenerse en todos los
estados de relación (extensiones) r de R. Siempre que la semántica de dos
conjuntos de atributos de R indique que debe mantenerse una dependencia
funcional, la especificamos como una restricción. Las extensiones de relación r(R)
que satisfacen la restricción de dependencia funcional reciben el nombre de
estados de relación legales (o extensiones legales) de R. Por tanto, el uso
fundamental de las dependencias funcionales es describir más en profundidad un
esquema de relación R especificando restricciones de sus atributos que siempre
deben cumplirse. Ciertas DF pueden especificarse sin hacer referencia a una
relación específica. Por ejemplo, {Provincia, NumPermisoConducir} → DNI debe
mantenerse para cualquier adulto que viva en Argentina. También es posible que
ciertas dependencias funcionales puedan dejar de existir en el mundo real si
cambia la relación. Por ejemplo, en Estados Unidos la DF CódigoPostal → CodÁrea
se utiliza como una relación entre los códigos postales y los códigos de los números
telefónicos, pero con la proliferación de los códigos de área telefónica ya no es tan
cierta.
Sea el esquema de relación
EMPLEADO_PROYECTO(DNI, NumPro, Horas, NombreE, NombrePro, UbicaciónPro)
desde el punto de vista de la semántica de los atributos sabemos que deben
mantenerse las siguientes dependencias funcionales:
a. DNI → NombreE
b. NumPro → {NombrePro, UbicaciónPro}
c. {DNI, NumPro} → Horas
Estas dependencias funcionales especifican que (a) el valor del Documento
Nacional de Identidad de un empleado (DNI) determina de forma inequívoca su
nombre (NombreE), (b) el valor de un número de proyecto (NumPro) determina de
forma única el nombre del mismo (NombrePro) y su ubicación (UbicaciónPro), y (c)
una combinación de valores DNI y NumPro determina el número de horas
semanales que el empleado ha trabajado en el proyecto (Horas). Alternativamente,
decimos que NombreE está determinado funcionalmente por (o es funcionalmente
dependiente de) DNI, o que dado un DNI concreto, conocemos el valor de NombreE,
etc.

<!-- página 3 -->

BASES DE DATOS Dependencias Funcionales
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 3
Una dependencia funcional es una propiedad del esquema de relación R, y no un
estado de relación legal particular r de R. Por consiguiente, una DF no puede ser
inferida automáticamente a partir de una extensión de relación r, sino que alguien
que conozca la semántica de los atributos de R debe definirla explícitamente. Por
ejemplo, el siguiente cuadro muestra un estado particular del esquema de relación
IMPARTIR. Aunque a primera vista pudiéramos pensar que Texto → Curso, no
podemos confirmarlo a menos que sepamos que se cumple para todos los estados
legales posibles de IMPARTIR. Sin embargo, basta con demostrar un único ejemplo
en contra para desautorizar una dependencia funcional. Por ejemplo, ya que 'Smith'
enseña tanto 'Estructuras de datos' como 'Administración de datos', podemos
concluir que Profesor no determina funcionalmente a Curso.
Un estado de relación IMPARTIR con una posible dependencia funcional
TEXTO→CURSO. Sin embargo, PROFESOR → CURSO no es posible.
IMPARTIR
Profesor Curso Texto
Smith Estructuras de datos Bartram
Smith Administración de datos Martin
Hall Compiladores Hoffman
Brown Estructuras de datos Horowitz

<!-- página 4 -->

BASES DE DATOS Dependencias Funcionales
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 4
Reglas de inferencia para las dependencias funcionales
Decimos que F es el conjunto de dependencias funcionales especificadas en un
esquema de relación R. Habitualmente, el diseñador del esquema especifica las
dependencias funcionales que son semánticamente obvias; sin embargo, es
habitual que otras muchas dependencias funcionales se encuentren en todas las
instancias de relación legales entre los conjuntos de atributos que pueden
derivarse y satisfacen las dependencias de F. Esas otras dependencias pueden
inferirse o deducirse de las DF de F. En la vida real, es imposible especificar todas
las dependencias funcionales posibles para una situación concreta. Por ejemplo, si
cada departamento tiene un director, de manera que NúmeroDpto determina de
forma única DniDirector (NúmeroDpto → DniDirector), y un director tiene un único
número de teléfono TeléfonoDirector (DniDirector → TeléfonoDirector), entonces
ambas dependencias juntas suponen que NúmeroDpto → TeléfonoDirector. Esto es
una DF inferida y no tiene que declararse explícitamente. Por tanto, formalmente
es útil definir un concepto llamado clausura (closure) que incluye todas las posibles
dependencias que pueden inferirse de un conjunto F dado.
Definición. Formalmente, el conjunto de todas las dependencias que incluyen
F, junto con las dependencias que pueden inferirse de F, reciben el nombre
de clausuras de F; está designada mediante F+.
Por ejemplo, suponga que especificamos el siguiente conjunto F de dependencias
funcionales obvias en el siguiente esquema de relación
EMP_DPTO(DNI, NombreE, FechaNac, Dirección, NúmeroDpto, NombreDpto,
DniDirector)
F = {Dni → {NombreE, FechaNac, Dirección, NúmeroDpto},
NúmeroDpto → {NombreDpto, DniDirector} }
Las siguientes son algunas de las dependencias funcionales adicionales que se
pueden inferir de F:
Dni → {NombreDpto, DniDirector}
Dni → Dni
NúmeroDpto → NombreDpto

<!-- página 5 -->

BASES DE DATOS Dependencias Funcionales
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 5
Una DF X → Y es inferida de un conjunto de dependencias F especificado en R si
X → Y se cumple en todo estado de relación legal r de R; es decir, siempre que r
satisfaga todas las dependencias en F, X → Y también se cumple en r. La clausura
F+ de F es el conjunto de todas las dependencias funcionales que pueden inferirse
de F. Para determinar una manera sistemática de inferir dependencias, debemos
descubrir un conjunto de reglas de inferencia que puedan usarse para deducir
nuevas dependencias a partir de un conjunto de dependencias concreto. A
continuación vamos a considerar algunas de estas reglas de inferencia. Usamos la
notación F |= X → Y para indicar que la dependencia funcional X → Y se infiere del
conjunto de dependencias funcionales F.
Axiomas de Amstrong
Conjunto de dependencias, que permite encontrar otras dependencias implicadas
por ellas, las cuales son consistentes y completas. Los axiomas de Armstrong son
consistentes y completos. Los Axiomas de Armstrong son más bien reglas de
inferencia. Estas reglas permiten deducir todas las dependencias funcionales que
tienen lugar a un conjunto dado de atributos que se dan a partir del conocimiento
del problema.
Reflexividad
Los valores de X y Y que son un conjunto de atributos Y están incluidos o son
iguales a los conjuntos de atributos X, entonces se cumplen que Y depende
funcionalmente de X.
Es decir que matemáticamente es: X → X
Si Y ⊆ X,   (X → Y)  (Y → X)
Por ejemplo:
(Cod_Pais → Cod_Cap) ( Cod_Cap → Cod_Pais)
Siendo Cod_Pais el código del Pais y Cod_Cap el código de la Capital del País.

<!-- página 6 -->

BASES DE DATOS Dependencias Funcionales
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 6
Aumentatividad
Si el conjunto de atributos Y depende funcionalmente de X, entonces dicha
dependencia se mantiene aunque se añada un atributo a ambos conjuntos. Es
decir, si:
(X → Y)
(XZ → YZ)
Por ejemplo si:
dni → nombre
dni, dirección → nombre, dirección
Si con dni se determina el nombre de una persona, entonces con dni más la
dirección también se determina el nombre o su dirección.
Transitividad
Si Y depende funcionalmente de X y Z depende funcionalmente de Y, entonces se
verifica que Z depende funcionalmente de X. Por lo tanto, si:
( X → Y ) y ( Y → Z )
( X → Z )
Por ejemplo:
FechaDeNacimiento → Edad
Edad → Puede_Conducir
FechaDeNacimiento → Puede_Conducir
Entonces tenemos que FechaDeNacimiento determina a Edad y la Edad determina
a Conducir, indirectamente. Por tanto podemos saber a través de
FechaDeNacimiento si Puede_Conducir.
Aditividad
Si Y depende funcionalmente de X y también se cumple que Z depende
funcionalmente de X, eso implica que Y y Z dependen funcionalmente de X. por
tanto:
(X → Y) y (X → Z) entonces (X → Y Z)

<!-- página 7 -->

BASES DE DATOS Dependencias Funcionales
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 7
PseudoTransitividad
Si se cumple que:
(X → Y) y (WY → Z) entonces (WX → Z)
La demostración de esta regla se la obtiene aplicando:
(X → Y), por aumentación (WX → WY) (WY → Z)
y ahora tras aplicar la transitividad (WX → Z)
Por ejemplo:
(DNI → Nombre) y (Nombre, Nom_Empresa → Sueldo)
(DNI, Nom_Empresa → Sueldo)
Descomposición
Si el conjunto de atributos Y depende funcionalmente de X y también se
cumple que los valores del conjunto de atributos Z están incluidos en los valores
de Y, entonces se tiene que cumplir que Z depende funcionalmente de X. Por lo
tanto:
Si (X → Y Z) entonces se cumplen (X → Y) y (X → Z)
Por ejemplo:
(DNI → nombre  dirección)
(DNI → nombre)  (DNI → dirección)
Este conjunto de reglas nos permite abordar y resolver una serie de
problemas fundamentales que luego nos conducirán al establecimiento de
algoritmos de diseño que sean sencillos y fiables.
Estos problemas fundamentales, son:
 Cierre de un conjunto de dependencias.
 Equivalencia lógica de esquemas.
 Deducción de dependencias.
 Cierre de un descriptor respecto de un conjunto de dependencias.
 Cálculo de las claves de un esquema

<!-- página 8 -->

BASES DE DATOS Dependencias Funcionales
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 8
Tipos de Dependencias Funcionales
Dependencia Funcional Completa
Un atributo B de R tiene dependencia funcional completa de un atributo A de una
relación R, si tiene dependencia funcional de A pero no tiene dependencia
funcional de ningún subconjunto de A.
Definición: En una dependencia funcional X → Y, cuando X es un conjunto de
atributos, decimos que la dependencia funcional es completa, si sólo depende de
X, y no de ningún subconjunto de X.
Formato:
A ⇒ B
“A determina funcionalmente a B”
DNI.Empleado ⇒ Sueldo
El DNI del empleado determina el sueldo.
El sueldo no depende de ningún subconjunto del DNI que es la clave primaria.
Dependencia Funcional Multivaluada
“Sea A,B,C tres subconjuntos distintos de atributos de una tabla T, se dice que A
tiene una dependencia Multivaluada con B, que A multidetermina a B, o que B
depende multivaluadamente de A.”. Existen casos de relaciones en los que un
atributo puede determinar a otro restringiendo su rango de valores válidos. A este
tipo de dependencias se les conoce como dependencias multivaluadas.
Formato:
A→→B
“A multidetermina a B“
Dependencia entre atributos de una relación (por ejemplo: A, B y C), tal que para
cada valor de A hay un conjunto de valores para B y un conjunto de valores para C.
Sin embargo, el conjunto de valores de B y C son independientes uno del otro.

<!-- página 9 -->

BASES DE DATOS Dependencias Funcionales
FCYT – BASES DE DATOS AÑO 2017 Hoja N° 9
Dependencia Funcional Transitiva
Sean A, B y C atributos de un esquema de relación R; si C tiene dependencia
funcional de B y B tiene dependencia funcional de A, entonces C tiene
dependencia funcional transitiva de A. Formato:
A→B, B →C
“A determina B y si B determina C entonces A determina a C“
Ejemplo: Ciudades(ciudad, población, superficie, renta, país, continente)
ciudad → país,
país → continente.
ciudad →continente.
Además, país → ciudad. Es decir, cada ciudad pertenece a un país y cada país a un
continente, pero en cada país puede haber muchas ciudades. En este caso
continente tiene una dependencia funcional transitiva con respecto a ciudad, a
través de país. Es decir, cada ciudad está en un país, pero también en un
continente.
