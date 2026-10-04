# PA-Clase-2-Resuelta

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 2/PRACTICA/PA-Clase-2-Resuelta.pdf` · 7 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Mismo encabezado que la guía: objetivo y funciones de la unidad |
| 2 | Funciones: explode() e implode() |
| 3 | Resueltos 1 a 3 (en el 2 la línea del array está cortada en el PDF) |
| 4 | Resueltos 4 (sort), 5 (rsort) y enunciado del 6 |
| 5 | Resueltos 6 ($persona) y 7 (date + explode) |
| 6 | Resueltos 8 (strtoupper/strtolower), 9 (trim, sin los espacios del enunciado) y 10 (substr) |
| 7 | Resuelto 11 (implode con fecha fija) |

<!-- página 1 -->

Guía Práctica de Ejercicios Nº 3
En esta tercera clase aprenderemos el manejo de arreglos, el uso de funciones y la
utilización de cadenas (strings) en PHP. También se analizarán funciones que nos permiten
realizar tareas como: mostrar el contenido de una arreglo, obtener su diferencia, pasar a
mayúsculas una cadena, obtener el largo de un strings, entre otras cosas.
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
<?php
$dias_semana = array('Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado');
var_dump ($dias_semana);
?>
2) - Edite el script anterior y agregue una nueva sentencia que muestre el contenido del
arreglo con la construcción foreach.
<?php
$dias_semana = array('Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado
foreach ($dias_semana as $un_dia) {
echo $un_dia.”<br />”;
}
?>
3) - Edite el script del punto 2 y agregue la función print_r() para ver el contenido y la
estructura del arreglo $dias_semana.
<?php
$dias_semana = array('Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado');
foreach ($dias_semana as $un_dia) {
echo $un_dia.”<br />”;
 }
print_r($dias_semana);
?>
4) - Edite el script del punto 2 y ordene el arreglo de forma ascendente y muestre en
pantalla el contenido del mismo. Utilice la función sort().
<?php

<!-- página 4 -->

$dias_semana = array('Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado');
foreach ($dias_semana as $un_dia) {
echo $un_dia.”<br />”;
}
print_r($dias_semana);
echo “<br />”;
sort($dias_semana);
foreach ($dias_semana as $un_dia) {
echo $un_dia.”<br />”;
}
?>
5) - Edite el script del punto 2 y ordene el arreglo de forma descendiente y muestre en
pantalla el contenido del mismo.
<?php
$dias_semana = array('Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado');
foreach ($dias_semana as $un_dia) {
echo $un_dia.”<br />”;
}
print_r($dias_semana);
echo “<br />”;
rsort($dias_semana);
foreach ($dias_semana as $un_dia) {
echo $un_dia.”<br />”;
}
?>
6) - Realice un nuevo script que defina un arreglo asociativo de nombre $persona y al cual
debemos asignar los siguiente valores y mostrarlos en pantalla:
Clave: tipo_documento, Valor: DNI
Clave: numero_documento, Valor: 22.122.122
Clave: apellidos, Valor: Torvalds
Clave: nombres, Valor: Linus
Clave: domicilio, Valor: San Martín 200

<!-- página 5 -->

Clave: telefono, Valor: 4333093
Clave: edad, Valor: 42
<?php
$persona = array(
'tipo_documento' => 'DNI',
'numero_documento' => '22122122',
'apellidos' => 'Torvalds',
'nombres' => 'Linus',
'domicilio' => 'San Martín 200',
'telefono' => '4333093',
'edad' => 42);
foreach ($persona as $dato_persona) {
echo $dato_persona.”<br />”;
}
?>
7) - Escriba un script PHP que utilice la función date('Y-m-d') para obtener la fecha actual y
utilizando la función explode() cambie el formato de la fecha a dd/mm/yyyy, muestre la fecha con
formato por pantalla.
<?php
$fecha = date('Y-m-d');
$arreglo_fecha = explode(“-”, $fecha);
$fecha_nueva = $arreglo_fecha[2].”/”.$arreglo_fecha[1].”/”.$arreglo_fecha[0];
echo $fecha_nueva;
?>
8) - Escriba un script PHP que utilice la función strtoupper() para convertir una cadena a
mayúsculas y mostrarla por pantalla. La misma cadena convertirla a minúsculas para luego
mostrarla por pantalla.
<?php

<!-- página 6 -->

$cadena = “Cadena de texto a convertir”;
$cadena_en_mayusculas = strtoupper($cadena);
echo $cadena_en_mayusculas;
$cadena_en_minusculas = strtolower($cadena);
echo $cadena_en_minusculas;
?>
9) - Escriba un script PHP que utilice la función trim() para quitar los espacios en blanco de
una cadena. La misma se define con el siguiente texto: “   Programación Avanzada – Taller de
PHP ”. De la cadena anterior se pide mostrar el largo de la misma por pantalla con la función
strlen() antes y después de utilizar la función trim().
<?php
$cadena = “Programación Avanzada – Taller de PHP”;
echo strlen($cadena);
echo “</br>”;
$cadena_nueva = trim($cadena);
echo strlen($cadena_nueva);
?>
10) - Escriba un script PHP que permita crear una cadena a partir de otra utilizando la
función substr(). La cadena inicial es: “Programación Avanzada – Taller de PHP” y la cadena
resultante deberá ser “Programación PHP”. Puede utilizar el operador de concatenación.
<?php
$cadena = “Programación Avanzada – Taller de PHP”;
$primera_subcadena = substr($cadena, 0, 12);
$segunda_subcadena = substr($cadena, -4);
echo $primera_subcadena . $segunda_subcadena;
?>
11) - Escriba un script PHP que permita crear una cadena a partir de un arreglo que

<!-- página 7 -->

contiene el día, el mes y el año actual. Utilice la función implode() del lenguaje. Debe crear el
arreglo y asignarle el dia, el mes y el año actual para luego crear la cadena.
<?php
$dia = “06”;
$mes = “09”;
$anio = “2012”;
$fecha = array($dia, $mes, $anio);
$fecha_de_cadena = implode(“/”, $fecha);
echo $fecha_de_cadena;
?>
