# Clase-2-Presentacion

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 2/TEORIA/Clase-2-Presentacion.pdf` · 21 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Temas: arreglos, mostrar su contenido, multidimensionales, recorrerlos, string |
| 2 | Portada de sección: Arreglos en PHP (solo el título) |
| 3 | Qué es un arreglo; crearlo con array() y con [] |
| 4 | Características: sin tipo ni tamaño, claves numéricas o de texto, vectores y matrices |
| 5 | Ejemplos: $colores, $persona (asociativo), $cosas (claves mezcladas) |
| 6 | Arreglos dentro de arreglos: $personas[] = $persona1 |
| 7 | Portada de sección: Mostrar el contenido de los arreglos |
| 8 | echo con el índice ($color[2]: la variable no coincide con $colores) |
| 9 | print_r() y su salida |
| 10 | var_dump(): tipo y tamaño de cada elemento |
| 11 | Portada de sección: Arreglos multidimensionales |
| 12 | Multidimensional: $personas con dos arreglos asociativos |
| 13 | print_r($personas[1]) (la salida está mal transcripta) |
| 14 | Portada de sección: Recorrer arreglos (solo el título) |
| 15 | Recorrer con for (el for de la diapositiva tiene las partes cambiadas) |
| 16 | Recorrer con foreach clave => valor ($auto) |
| 17 | foreach anidado sobre $autos |
| 18 | Portada de sección: String (solo el título) |
| 19 | String: comillas simples y dobles, sustitución de variables |
| 20 | Cadenas simples (literales) y complejas (escapes y variables) |
| 21 | Acceder a un carácter con índice: $texto[2] |

<!-- página 1 -->

TEMAS A DESARROLLAR
Arreglos en PHP.
Mostrar el contenido de un arreglo.
Arreglos multidimensionales.
Recorrer Arreglos.
String

<!-- página 2 -->

Arreglos en PHP

<!-- página 3 -->

Arreglos en PHP
Un arreglo es una colección ordenada de elementos compuestos por un valor y referenciado por
una clave única que lo identifica dentro del arreglo.
$arreglo = array();
Para definir un arreglo en php utilizamos array() lo cual establece la variable para almacenar datos
compuestos. También podemos definir un arreglo haciendo uso de los corchetes []:
$arreglo = ['rojo','azul'];

<!-- página 4 -->

Arreglos en PHP
En PHP no es necesario definir el tipo de dato que contendrá el arreglo ni su tamaño.
Un arreglo en PHP puede almacenar datos de distinto tipo.
PHP utiliza números para indexar un arreglo de manera predeterminada, pero también se pueden
utilizar letras o palabras como índices.
Un arreglo puede contener otros arreglos, objetos, números, o una combinación de todos los
anteriores.
Podemos definir arreglos unidimensionales(vectores), bidimensionales(matrices) o con las
dimensiones que necesitemos.

<!-- página 5 -->

Arreglos en PHP
Veamos algunos ejemplos:
$colores = array( 'rojo', 'azul', 'amarillo' );
$persona = array(
'documento'=>22444555,
'apellido'=>'Gomez',
'nombre'=>'Martín'
);

Veamos algunos ejemplos:
$cosas= array(
0=>22444555,
'apellido'=>'Gomez',
1=>'Martín'
);

<!-- página 6 -->

Arreglos en PHP
$persona1 = array(
'documento'=>22444555,
'apellido'=>'Gomez',
'nombre'=>'Martín'
);
$persona2 = array(
'documento'=>55222333,
'apellido'=>'Lopez',
'nombre'=>'Analía'
);

Podemos almacenar arreglos en otros arreglos:
$personas = array();
$personas[]=$persona1;
$personas[]=$persona2;

<!-- página 7 -->

Mostrar el contenido de los
arreglos

<!-- página 8 -->

Mostrar el contenido de los arreglos
Para mostrar el contenido de un arreglo podemos utilizar el constructor echo indicando el nombre
del arreglo y su índice.
<?php
$colores= array('rojo','azul','verde');
echo $color[2];
?>
La salida será: verde

<!-- página 9 -->

Mostrar el contenido de los arreglos
Existen dos funciones más que nos permiten mostrar no solo el contenido de los arreglos sino
también los tipos de datos que tienen  almacenados. Estas funciones son print_r() y var_dump().
Ejemplo de print_r():
<?php
$colores= array('rojo','azul','verde');
print_r ( $color );
?>
La salida será:
Array (
[0] => rojo
[1] => azul
[2] => verde
)

<!-- página 10 -->

Mostrar el contenido de los arreglos
A diferencia de print_r(), var_dump() muestra la estructura del arreglo junto con el tipo y el tamaño
del dato almacenado en cada elemento del mismo.
El mismo ejemplo con var_dump();
<?php
$colores= array('rojo','azul','verde');
var_dump( $color );
?>
La salida será:
array(3) {
[0]=> string(4) "rojo"
[1]=> string(4) "azul"
[2]=> string(5) "verde"
}

<!-- página 11 -->

Arreglos multidimensionales

<!-- página 12 -->

Arreglos multidimensionales
En PHP un arreglo puede contener todo tipos de datos, inclusive otros arreglos por lo que la
creación de arreglos multidimensionales es muy sencilla. Simplemente bastará con asignar un arreglo
como el valor del elemento de otro arreglo.
Ejemplo:
<?php
$personas= array();
$persona1= array( 'documento'=>22333444, 'apellido'=>'Bonnet',' nombres'=>'Federico');
$persona2= array( 'documento'=>11222333, 'apellido'=>'Aramburu',' nombres'=>'Exequiel');
$personas[] = $persona1;
$personas[] = $persona2;
?>

<!-- página 13 -->

Arreglos multidimensionales
Ejemplo:
<?php
$personas= array();
$persona1= array( 'documento'=>22333444, 'apellido'=>'Bonnet',' nombres'=>'Federico');
$persona2= array( 'documento'=>11222333, 'apellido'=>'Aramburu',' nombres'=>'Exequiel');
$personas[] = $persona1;
$personas[] = $persona2;
?>
Mostrar los elementos:
<?php
print_r( $personas [1]) ;
?>
La salida será:
Array(
 'documento'=>11222333,
'apellido'=>'Aramburu',
'nombres'=>'Exequiel'
)

<!-- página 14 -->

Recorrer Arreglos

<!-- página 15 -->

Recorrer Arreglos
Mostrar los elementos:
Si el arreglo tiene la misma cantidad de filas que de columnas y si sus índices son todos numéricos,
podemos utilizar la función for() para mostrar sus elementos:
<?php
$colores = array ( 'rojo', 'azul', 'verde');
for ($i=0; $i++; $i< count($colores) ){
echo $colores[i];
}

<!-- página 16 -->

Recorrer Arreglos
Si el arreglo tiene sus índices compuestos por nombres o letras, podemos utilizar la función
foreach() para mostrar sus elementos:
<?php
$auto = array ( 'color'=>'rojo', 'marcar'=>'Chevrolet', 'año'=>'1969'  );
foreach ( $auto as $clave=>$valor ){
echo $clave.'=>';
echo $valor;
}
?>
La salida será:
Color=>rojo
Marca => Chevrolet
Año => 1969

<!-- página 17 -->

Recorrer Arreglos
Si el arreglo es multidimensional:
<?php
$autos[ ] = array ( 'color'=>'negro', 'marcar'=>'Chevrolet', 'Modelo'=>'Camaro', 'Año'=>'1969' );
$autos[ ] = array ( 'color'=>'rojo', 'marcar'=>'Ford', 'año'=>'1969' );
foreach ( $autos as $unAuto){
foreach ( $unAuto as $atributos ){
echo $atributos;
}
}
?>

<!-- página 18 -->

String

<!-- página 19 -->

String
En PHP un string es cualquier conjunto de caracteres entrecomillados. PHP considera como
cadena todo lo que encuentre entre un par de comillas, por eso todas las cadenas deben comenzar y
terminar con el mismo tipo de comillas, simples o dobles.
<?php
$nombre = ” Martín ” ;
echo “ Saludos, $nombre” // Muestra: “Saludos, Martín”
echo ' Saludos, $nombre ' // Muestra: “Saludos, $nombre\n”
?>

<!-- página 20 -->

String
Las comillas simples representan "cadenas simples," donde todos los caracteres son utilizados
literalmente.
echo ' Saludos, $nombre ' // Muestra: “Saludos, $nombre\n”

Las comillas dobles encapsulan "cadenas complejas" que permiten las secuencias de escape (para
insertar caracteres especiales) y para la sustitución de variables (integran el valor de una variable
directamente en una cadena).
$nombre = ” Martín ” ;
echo “ Saludos, $nombre” // Muestra: “Saludos, Martín”

<!-- página 21 -->

String
Una particularidad de los string en PHP es que podemos obtener caracteres particulares tratando
los índices como si fueran array():
<?php
$texto = “Esta es la cadena de texto que utilizaremos en el ejemplo”;
echo $texto [2];
}
?>
