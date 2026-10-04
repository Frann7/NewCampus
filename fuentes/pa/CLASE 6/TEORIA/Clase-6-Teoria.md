# Clase-6-Teoria

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 6/TEORIA/Clase-6-Teoria.pdf` · 4 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Conexión a base de datos: PHP y los SGBD, la extensión mysqli (MySQL 4.1+), una conexión por script |
| 2 | Crear una conexión: `new mysqli` con sus 4 parámetros, `connect_errno` / `connect_error`, `exit`; empieza "Realizar una consulta" |
| 3 | Ejemplo completo (`query`, `num_rows`, `while` + `fetch_assoc`, `print_r`, `close`); `$resultado` es un apuntador al socket. El `echo “<br>”` tiene comillas tipográficas (no compila tal cual) |
| 4 | Tabla de ejemplo `personas`, arreglos que da `fetch_assoc` (claves y documentos no coinciden con la tabla), cerrar la conexión. El texto sale completo |

<!-- página 1 -->

Guía Básica del lenguaje PHP
Objetivo: Comprender el funcionamiento básico del lenguaje PHP.
Sitio oficial: http://www.php.net
CONEXIÓN A BASE DE DATOS
PHP es un lenguaje de programación del lado servidor. Como tal, permite la conexión a
distintos Sistemas Gestores de Base de Datos (SGBD) existentes en el mercado. En el caso de
este taller estudiaremos la extensión mysqli, la cual permite conectar nuestra aplicación son el
SGBD MySql / MariaDb.
MYSQLI
Representa una conexión entre PHP y una base de datos MySQL/MARIADB. Permite
acceder a la funcionalidad proporcionada por MySQL 4.1 y posterior. Esta clase mysqli se puede
instanciar de muchas maneras y las conexiones debemos realizarlas en cada script en el que
utilicemos o debamos hacer algún tipo de consulta.
Con el fin de establecer comunicación con el servidor que contiene la base de datos
MySQL, primero necesitas abrir una conexión con el mismo. Toda la comunicación entre el PHP y
el servidor de datos se realiza a través de esta conexión.

<!-- página 2 -->

Crear una conexión:
Para crear una conexión, se inicializa un objeto de la clase MySQLi pasando cuatro
argumentos al constructor:
$mysqli = new mysqli( 'Host', 'usuarioDB', 'contraseñaDB', 'BasedeDatos' );
if ($mysqli->connect_errno)
{
echo "No se pudo establecer la conexión.";
echo "Error número: " . $mysqli->connect_errno;
echo "Error descripción: " . $mysqli->connect_error ;
exit;
}
Los parámetros que solicita el constructor son los siguientes:
Host: dirección IP o nombre (fqdn) del servidor MySql/MariaDb.
UsuarioDB: usuario del SGBD con el cual queremos establecer la conexión.
 ContraseñaDB: contraseña asociada al usuario del SGBD.
BasedeDatos: nombre de la Base de Datos a la cual nos queremos conectar.
Al establecer la conexión se crea un socket el cual es direccionado por la variable $mysqli
mediante el cual podremos enviar consultas al SGBD y obtener los resultados que de estas se
generen.
Realizar una consulta:
Para realizar una consulta (query) sobre una Base de Datos deberemos, luego de
establecida la conexión, escribir la instrucción sql y enviársela al Sistema Gestor a fin de que ésta
la ejecute. Luego el resultado podremos obtenerlo a través de la misma variable ($mysqli).
Vemos ésto con un ejemplo:

<!-- página 3 -->

<?php
$mysqli = new mysqli('127.0.0.1', 'root', '', 'Personal');
$sql = ' SELECT * FROM personas';
if ( $resultado = $mysqli->query($sql) )
{
if ( $resultado->num_rows > 0 )
 {
 while ( $persona = $resultado->fetch_assoc() )
{
print_r ( $persona );
echo “<br>”;
}
}
}
$mysqli->close();
?>
En el código se ve como se establece la conexión ( new mysqli() ), se genera la consulta
SQL (la cual el guardada en la variable $sql), se envía ésta mediante el método:
$mysqli->query($sql) y se obtienen los datos en la variable $resultado.
Ahora bien, la variable  $resultado no tiene almacenados los datos, sino que es un
apuntador  a  un  socket desde  donde  accederemos  a  ellos.  Para  realizar  esta  tarea
transformaremos el contenido del socket en alguna estructura que nos sea más fácil de manipular.
Para esto utilizamos el método: $resultado->fetch_assoc(), el cuál tomará cada fila de la
consulta y creará un arreglo asociativo (el cual asignamos a la variable $persona) con todos los
campos recuperados de la consulta. Este arreglo tendrá como índice los nombres de las columnas
definidas en la tabla que consultamos (en nuestro caso personas).
Dado el código anterior imaginemos que la tabla donde se almacenan los datos tiene la

<!-- página 4 -->

siguiente estructura:
IdPersona Documento Apellido Nombres
1 22333444 García Gabriel
2 11222333 Bonnet Federico
3 44555666 Aramburu Exequiel
Al  momento  de  ejecutar:  $resultado->fetch_assoc(),  obtendremos  en  la  variable
$resultado un array() con la siguiente estructura:
Array (
[idPersona] => 1
[documento] => 11222333
[apellido] => García
[nombre] => Gabriel
)
Como esta función se ejecuta dentro de un bucle while(), obtendremos un arreglo por cada
fila existente en la tabla:
Array ( [idPersona] => 1 [documento] => 11222333 [apellido] => García [nombre] => Gabriel )
Array ( [idPersona] => 2 [documento] => 22333444 [apellido] => Bonnet [nombre] => Federico )
Array ( [idPersona] => 3 [documento] => 33222555 [apellido] => Aramburu [nombre] => Exequiel )
Cerrar la conexión:
Una vez que accedimos a los datos y trabajamos con ellos es necesario cerrar la conexión
de manera tal que se liberen los datos de memoria y se borren los apuntadores creados.
$mysqli = new mysqli( 'Host', 'usuarioDB', 'contraseñaDB', 'BasedeDatos' );
// conjunto de acciones
$mysqli->close();
