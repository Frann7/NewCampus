# Clase-5-Teoria

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 5/TEORIA/Clase-5-Teoria.pdf` · 6 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Sesiones: qué es una sesión (id, cookie, archivo), session_start(), session_id(), $_SESSION. Código con errata: `$_SESSION['nombre]` sin cerrar la comilla (está así en el PDF) |
| 2 | Recuperar la sesión desde otro script (index.php → home.php). Asegurando formularios: ¿los datos vienen siempre del formulario? |
| 3 | Formulario + procesoFormulario.php (INSERT con mysqli; errata `'apellido'` sin $) y el ataque con cURL (empieza) |
| 4 | Fin del ataque cURL (bucle de 1000000000000 POST). Utilización de tokens: form.php con rand(5, 1500) y campo hidden (errata `$token; =`) |
| 5 | procesoFormulario.php compara $_POST['token'] con $_SESSION['token']; límite del token (bots). Utilización de captcha (intro) |
| 6 | Formulario con captcha (`<img src="imgRnd.png">` + campo token) y el mismo procesoFormulario.php |

<!-- página 1 -->

Guía Básica del lenguaje PHP
Objetivo: Comprender el funcionamiento básico del lenguaje PHP.
Sitio oficial: http://www.php.net
SESSIONES EN PHP
Una sesión es una técnica que permite identificar de manera única a un usuario
(navegador) en nuestra aplicación web. La idea es sencilla, cuando un usuario accede a nuestro
sitio creamos para éste un código único y se lo enviamos a su navegador para que lo almacene
(como una cookie). Luego, cuando nuestro usuario acceda a otra página de nuestra aplicación,
recuperamos este id para saber que es quien dice ser.
Sesiones en PHP
Para crear una sesión PHP nos provee la función:
<?php
session_start();
?>
Esta función crea una sesión identificada por un código ( session_id() ) y utiliza este código
para reconocer la conexión existente entre el navegador y el servidor. El servidor almacena éste
código en un archivo mientras que el navegador como una cookie.
Además de identificar el usuario, PHP crea un arreglo llamado $_SESSION[] donde
podremos guardar información para luego recuperar:
<?php
session_start();
$_SESSION['nombre] = 'Federico';
$_SESSION['apellido] = 'Bonnet';
?>

<!-- página 2 -->

Una vez creada la sesión podremos recuperar la información desde otro script.
Imaginemos que desde un navegador accedemos primero al script: index.php y luego a home.php.
El usuario accede al script Index.php el cual tiene el siguiente código:
<?php
session_start(); creamos la sesión.
$_SESSION['nombre] = 'Federico'; Asignamos el nombre al array.
$_SESSION['apellido] = 'Bonnet'; Asignamos el nombre al array.
?>
Luego el usuario accede al script home.php el cual tiene el siguiente código:
<?php
session_start(); recuperamos la sesión creada en el script anterior.
echo $_SESSION['nombre]; Mostramos el valor asignado en el script anterior.
echo $_SESSION['apellido]; Mostramos el valor asignado en el script anterior.
?>
Esta es una forma sencilla que nos proveen las sesiones para almacenar información de
cada usuario que accede a nuestro sitio. Recuerde que por cada usuario que acceda se creará
una sesión y se podrán almacenar datos asociados exclusivamente a esa sesión.
ASEGURANDO FORMULARIOS
Cuando  recibimos  los  datos  provenientes  de  un  formulario  en  un  script  PHP
(procesoFormulario.php) previamente declarado en el action del formulario, podemos procesar los
mismos desde alguno de los arreglos: $_GET, $_POST o $_REQUEST. En una primer instancia
estaríamos seguros de que la información recibida proviene del origen que nosotros definimos (el
formulario HTML). ¿Pero es esto siempre así?.

<!-- página 3 -->

Analicemos el siguiente formulario:
<form action="http://ejemplo.com/procesoFormulario.php" method=”post”>
<input type="text" name ="nombre" >
<input type="text" name ="apellido" >
<input type="submit" value="Enviar el formulario">
</form>
y su correspondiente script PHP (procesoFormulario.php):
<?php
$nombre = $_POST['nombre'];
$apellido = $_POST['apellido'];
$sql=” INSERT INTO personas VALUES (null,'$nombre','apellido')”;
$mysqli = new mysqli("localhost", "root", "toto", "basedatos");
$mysqli->query($sql);
?>
Nuestro script recibe los datos (apellido y nombre) completados desde le formularios e
inserta los mismos en la tabla personas de una base de datos llamada: basedatos. Hasta el
momento todo normal. Pero que pasaría si un atacante desde otro servidor ejecuta el siguiente
código PHP?
<?php
$url="http://ejemplo.com/procesoFormulario.php";
for($i=1;$i<=1000000000000;$i++)
{
        $nombre='Federico';
            $apellido='Bonnet';
$fields=['nombre'=>$nombre,'apellido'=>$apellido];
$campos_string = http_build_query($fields);
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL, $url);
curl_setopt($ch,CURLOPT_POST, true);
curl_setopt($ch,CURLOPT_POSTFIELDS, $campos_string);

<!-- página 4 -->

curl_setopt($ch,CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($ch);
curl_close($ch);
}
?>
Este código ejecuta 1000000000000 veces el bucle y en cada ejecución enviá un post
(haciéndose pasar por nuestro formulario) al script  http://ejemplo.com/procesoFormulario.php
simulando enviar datos desde nuestro formulario. De esta forma insertaría 1000000000000
registros en nuestra base de datos.
Es por esta razón que deberemos, en nuestro script procesoForm.php,  poder reconocer
solamente los datos que provengan de nuestro formulario y los demás descartarlos.
Utilización de tokens
Una manera sencilla de solucionar ésto es asignar a cada formulario un token único y
validar en nuestro script PHP que éste token sea válido. Veamos ésto con un ejemplo:
Analicemos nuestro formulario form.php:
<?php
session_start();
$token; = rand(5, 1500);
$_SESSION ['token'] = $token;
?>
<form action="http://ejemplo.com/procesoFormulario.php" method=”post”>
<input type=”hidden” name=”token” value=”<?php echo $token?>”>
<input type="text" name ="nombre" >
<input type="text" name ="apellido" >
<input type="submit" value="Enviar el formulario">
</form>

<!-- página 5 -->

En éste código generamos un número aleatorio entre 5 y 1500 que utilizaremos como
identificador de nuestro formulario. Luego agregamos éste código en un campo oculto del mismo
(como un type=”hidden”) y almacenamos el mismo código en una sesion.
Con  este  pequeño  cambio  podremos  ahora  validar  en  nuestro  script
procesoFormulario.php el código recibido desde el formulario con el código almacenado en la
sesion, si coinciden puedo tener certeza de que los datos provienen de este formulario:
Analicemos el script procesoFormulario.php:
<?php
session_start();
if ( $_POST ['token'] == $_SESSION [ 'token' ] )
{
// proceso los datos del Formulario.
}else{
// descarto todo los datos.
}
?>
Si bien esta técnica presenta una primer barrera de seguridad, no soluciona el total de los
problemas. En internet existen infinidad de boots que pueden llegar a leer información de nuestro
formulario (inclusive el token) y utilizar éste para enviar datos antes que nuestro usuario lo haga.
Para dar un grado más de seguridad se implementa ésta técnica con imágenes las cuáles son
más difíciles de leer por los boots. A esto se lo conoce como captcha.
Utilización de captcha
Esta técnica genera un código aleatorio para identificar el formulario, guarda éste en una
sesión del servidor y con dicho código genera una imagen la cual es incrustada en el formulario.
Luego se pide al usuario que ingrese en otro campo el código mostrado en la imagen.
Nuestro código ahora quedaría de la siguiente forma:

<!-- página 6 -->

<?php
session_start();
$token; = rand(5, 1500);
$_SESSION ['token'] = $token;
?>
<form action="http://ejemplo.com/procesoFormulario.php" method=”post”>
<input type="text" name ="nombre" >
<input type="text" name ="apellido" >
<img src=”imgRnd.png”>
<input type=”text” name=”token” value=””>
<input type="submit" value="Enviar el formulario">
</form>
De ésta forma la etiqueta img muestra la imagen con el código aleatorio creado en la
sesion y pedimos al usuario que escriba dicho código en la etiqueta name=”token”.
Analicemos el script procesoFormulario.php:
<?php
session_start();
if ( $_POST ['token'] == $_SESSION [ 'token' ] )
{
// proceso los datos del Formulario.
}else{
// descarto todo los datos.
}
?>
