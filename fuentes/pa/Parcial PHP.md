# Parcial PHP

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/Parcial PHP.pdf` · 6 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Preg. 1 (siglas de XAMPP, emparejar), 2 (array asociativo), 3 (funciones de cadenas, emparejar). Los desplegables solo muestran la opción elegida |
| 2 | Preg. 4 (funciones mysqli, emparejar), 5 (if anidados: valores de $a, $b, $c) |
| 3 | Preg. 6 (for), 7 ($_SESSION, $_GET, $_POST, emparejar), 8 (array indexado) |
| 4 | Preg. 9 (continue), 10 (sort, V/F), 11 (input tipo text), 12 (if con true) |
| 5 | Preg. 13 (break n, V/F), 14 (estructuras para recorrer arreglos, dos correctas), 15 (qué es PHP), 16 ($_REQUEST, V/F) |
| 6 | Preg. 17 (date + explode), 18 (while sin incremento), 19 (nombre de variable no válido), 20 (var_dump, V/F) |

<!-- página 1 -->

Pregunta 1
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 2
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 3
Sin responder
aún
Se puntúa como
0 sobre 5,00
El nombre del aplicativo XAMPP es un acrónimo que significa:
XSignifica que funciona en diferentes sistemas operativos
AServidor Web Apache
MBase de datos Mysql/MariaDB
PLenguaje de programación PHP
PLenguaje de programación Perl
Seleccione una:
Cual es la salida del siguiente script PHP:
<?php
$mineral = array(
'dorado' => 'negro',
'plateado' => 'Plata',
'brillante' => 'Diamante',
'negro' => 'Carbón'
);
echo $mineral['negro'];
?>
a. negro
b. dorado
c. Ninguna de las anteriores
d. Carbón
Quitar mi elección
Indique la correcta opción para cada definición :
Función que permite separar (dividir) una cadena de texto indicándole el carácter separador como
parámetro. explode()
Función que nos permite convertir una cadena de texto que se recibe como parámetro a mayúsculas. strtoupper()
Función que permite juntar los elementos de un arreglo en una cadena de texto. implode()
Función que permite obtener una porción de texto de una cadena que se le pasa como parámetro a la
misma. substr()
Función que permite convertir una cadena de texto que se recibe como parámetro a minúsculas. strtolower()
Tiempo restante 0:39:12

<!-- página 2 -->

Pregunta 4
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 5
Sin responder
aún
Se puntúa como
0 sobre 5,00
Seleccione la definición correcta para cada función:
Crea una conexión a un servidor de base de datos MySQL o derivados de ella.mysqli_connect()
Nos permite enviar una consulta sobre la base de datos seleccionada y
asociada al identificador de conexión pasado como parámetro. mysqli_query()
Nos devuelve una matriz que corresponde a la fila recuperada y
luego mueve el puntero interno hacia adelante. mysqli_fetch_array()
Seleccione una:
¿Cuáles son los valores para las variables $a, $b y $c teniendo en cuenta que el siguiente script tiene como salida la
cadena Hola, Mundo!?
<?php
$string = "Hola, Mundo!";
$a = ?;
$b = ?;
$c = ?;
if ($a) {
if ($b && !$c) {
              echo "Adios mundo cruel!";
              } else if (!$b && !$c) {
                      echo "Nada por aquí";
                      }
        } else {
if (!$b) {
if (!$a && (!$b && $c))
                                                    {
    echo "Hola, mundo!";
    } else {
                    echo "Adios mundo!";
                  }
} else {
    echo "No exactamente";
    }
}
?>
a. False, True, True
b. True, True, False
c. False, True, False
d. False, False, True
Quitar mi elección

<!-- página 3 -->

Pregunta 6
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 7
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 8
Sin responder
aún
Se puntúa como
0 sobre 5,00
Seleccione una:
¿Cuál es la salida del siguiente script?
<?php
$i = 5;
 for ($i = 1; $i <= 5; $i++)
{ echo $i." ";}
 ?>
a. 4 5
b. 1 2 3 4 5
c. 5 4 3 2 1
d. 5
e. 0 1 2 3 4
Quitar mi elección
Indique la correcta opción para cada definición :
Es un array asociativo que contiene variables de sesión disponibles para el script actual. $_SESSION
ES un array asociativo de variables pasado al script actual vía parámetros URL. $_GET
Es un array asociativo de variables pasadas al script actual a través del método HTTP POST.$_POST
Seleccione una:
Cual es la salida de siguiente script PHP:
<?php
$dias_semana = array('Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves',
'Viernes', 'Sábado');
echo $dias_semana[1];
?>
a. Domingo
b. Lunes
c. Ninguno de los anteriores
d. Hola mundo!!
e. Martes
Quitar mi elección

<!-- página 4 -->

Pregunta 9
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 10
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 11
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 12
Sin responder
aún
Se puntúa como
0 sobre 5,00
Seleccione una:
Cual es la salida del siguiente script PHP:
<?php
  for ($i = 0; $i < 10; $i++) {
    if ($i > 3 && $i < 6) {
                            continue;
                          }
        echo $i." ";
}
?>
a. 0 1 2 3 4
b. 0 1 2 3 4 5 6 7 8 9
c. 0 1 2 3 6 7 8 9
d. 0 1 2 3
e. 0 1 2 7 8 9
Seleccione una:
¿La función sort() nos brinda la posibilidad de ordenar un arreglo que le pasamos como parámetro, modificando al mismo
a nivel de
claves?
Verdadero
Falso
Seleccione una:
El componente HTML "INPUT" tipo text:
a. Nos permite el ingreso de una cadena de texto pero no vemos los caracteres que ingresamos.
b. Nos permite ingresar una cadena de texto pero no es visible dentro del formulario.
c. Nos permite ingresar una cadena de texto.
d. Nos permite ingresar un archivo para ser enviado al servidor.
Seleccione una:
¿El siguiente código Php es correcto y tiene como salida "INGRESA"?
<?php
$a=true;
if ($a) {
echo "INGRESA";
}
?>
a. Si es correcto
b. No, porque es falso por defecto .
c. Emite un error, porque la estructura de control IF no posee condición para evaluar

<!-- página 5 -->

Pregunta 13
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 14
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 15
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 16
Sin responder
aún
Se puntúa como
0 sobre 5,00
Seleccione una:
La siguiente afirmación es correcta:
En el lenguaje Php la sentencia break acepta un argumento numérico opcional el cual indica de cuantas estructuras
anidadas encerradas se debe salir(ej: break 2).
Verdadero
Falso
Seleccione una o más de una:
Indique con qué estructuras de control se pueden recorrer arreglos en PHP.(Seleccione dos respuestas)
a. else if
b. if
c. switch
d. var_dump
e. foreach
f. for
g. r_array
h. trim
Seleccione una:
Indique la definición más correcta para PHP (PHP HyperText PreProcessor).
a. PHP es un lenguaje de programación compilado que se ejecuta del lado del cliente.
b. PHP es un lenguaje de programación interpretado que se ejecuta del lado del cliente.
c. PHP es un lenguaje de programación interpretado que se ejecuta del lado del servidor.
d. PHP es un lenguaje de programación compilado que se ejecuta del lado del servidor.
Seleccione una:
$_REQUEST es un array asociativo que por defecto posee el contenido de $_GET, $_POST y $_SESSION.
Verdadero
Falso

<!-- página 6 -->

Pregunta 17
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 18
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 19
Sin responder
aún
Se puntúa como
0 sobre 5,00
Pregunta 20
Sin responder
aún
Se puntúa como
0 sobre 5,00
Seleccione una:
Cual es la salida del siguiente script PHP:
<?php
$fecha = date('Y-m-d');
$arreglo_fecha = explode("-", $fecha);
$fecha_nueva = $arreglo_fecha[2]."/".$arreglo_fecha[1]."/".$arreglo_fecha[0];
echo $fecha_nueva;
?>
a. 2017-05-23
b. 2017
c. 23/05/2017
d. 2017/23/05
e. 23-05-2017
Seleccione una:
Cual es la salida del siguiente script PHP:
<?php
$i = 0;
while ($i < 10) {
                echo $i;
}
?>
a. Bucle infinito
b. 0 1 2 3 4 5 6 7 8 9
c. 0 1 2 3 4 5 6 7 8 9 10
d. 0 1 2 3 4
Seleccione una:
¿Cuál de los siguientes es un nombre de variable NO válido en PHP?
a. $variable10
b. $miVariable
c. $_10
d. $10_variable
Seleccione una:
La función var_dump(), vuelca información sobre una variable, mostrando su estructura, su tipo y valor.
Verdadero
Falso
