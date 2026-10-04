# PA-Clase-2

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 2/PRACTICA/PA-Clase-2.pdf` · 4 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Guía práctica (encabezado "Nº 3"): objetivo y funciones de la unidad (foreach, array, sort, asort, rsort, strtoupper, strtolower, substr) |
| 2 | Funciones: explode() e implode() |
| 3 | Ejercicios 1 a 7 (arreglo $dias_semana, var_dump, foreach, print_r, sort, rsort, $persona, date) |
| 4 | Ejercicios 7 (fin) a 11 (strtoupper, trim y strlen, substr, implode) |

<!-- página 1 -->

Guía Práctica de Ejercicios Nº 3
En esta tercera clase aprenderemos el manejo de arreglos, el uso de funciones y la
utilización de cadenas (strings) en PHP. También se analizarán funciones que nos permiten
realizar tareas como: mostrar el contenido de una arreglo, diferencias entre arreglos, pasar a
mayúsculas una cadena, obtener el largo de un string, entre otras.
Objetivo:  Profundizar y comprender el funcionamiento básico de la Web y PHP.
Construcciones y Funciones que estudiaremos en esta unidad:
foreach: nos brinda la posibilidad de iterar de forma sencilla matrices.
array() nos permite crear un arreglo.
sort() nos brinda la posibilidad de ordenar un arreglo que le pasamos como parámetro,
modificando al mismo a nivel de claves.
asort() nos brinda la posibilidad de ordenar un arreglo que le pasamos como parámetro
permitiendo mantener la asociación de las claves que contenga el arreglo.
rsort() nos brinda la posibilidad de ordenar un arreglo que le pasamos como parámetro
(igual a sort()), pero ordenando los elementos de forma descendente.
strtoupper() función que nos permite convertir una cadena de texto que se recibe como
parámetro a mayúsculas.
strtolower() permite convertir una cadena de texto que se recibe como parámetro a
minúsculas.
substr() permite obtener una porción de texto de una cadena que se le pasa como
parámetro a la misma.

<!-- página 2 -->

explode() permite separar (dividir) una cadena de texto indicándole el carácter separador
como parámetro.
implode()  permite juntar los elementos de un arreglo en una cadena de texto.

<!-- página 3 -->

EJERCICIOS
1) - Realice un script que defina un arreglo de nombre $dias_semana y al cual debemos
asignar cada uno de los días de la misma comenzando por el Domingo. Luego utilice la función
var_dump() para mostrar su contenido.
2) - Edite el script anterior y agregue una nueva sentencia que muestre el contenido del
arreglo con la construcción foreach.
3) - Edite el script del punto 2 y agregue la función print_r() para ver el contenido y la
estructura del arreglo $dias_semana.
4) - Edite el script del punto 2 y ordene el arreglo de forma ascendente y muestre en
pantalla el contenido del mismo. Utilice la función sort().
5) - Edite el script del punto 2 y ordene el arreglo de forma descendiente y muestre en
pantalla el contenido del mismo.
6) - Realice un nuevo script que defina un arreglo asociativo de nombre $persona y al cual
debemos asignar los siguiente valores y mostrarlos en pantalla:
Clave: tipo_documento, Valor: DNI
Clave: numero_documento, Valor: 22.122.122
Clave: apellidos, Valor: Torvalds
Clave: nombres, Valor: Linus
Clave: domicilio, Valor: San Martín 200
Clave: telefono, Valor: 4333093
Clave: edad, Valor: 42
7) - Escriba un script PHP que utilice la función date('Y-m-d') para obtener la fecha actual y

<!-- página 4 -->

utilizando la función explode() cambie el formato de la fecha a dd/mm/yyyy, muestre la fecha con
formato por pantalla.
8) - Escriba un script PHP que utilice la función strtoupper() para convertir una cadena a
mayúsculas y mostrarla por pantalla. La misma cadena convertirla a minúsculas para luego
mostrarla por pantalla.
9) - Escriba un script PHP que utilice la función trim() para quitar los espacios en blanco de
una cadena. La misma se define con el siguiente texto: “   Programación Avanzada – Taller de
PHP ”. De la cadena anterior se pide mostrar el largo de la misma por pantalla con la función
strlen() antes y después de utilizar la función trim().
10) - Escriba un script PHP que permita crear una cadena a partir de otra utilizando la
función substr(). La cadena inicial es: “Programación Avanzada – Taller de PHP” y la cadena
resultante deberá ser “Programación PHP”. Puede utilizar el operador de concatenación.
11) - Escriba un script PHP que permita crear una cadena a partir de un arreglo que
contiene el día, el mes y el año actual. Utilice la función implode() del lenguaje. Debe crear el
arreglo y asignarle el día, el mes y el año actual para luego crear la cadena.
