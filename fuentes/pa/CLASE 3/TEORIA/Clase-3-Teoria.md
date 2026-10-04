# Clase-3-Teoria

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 3/TEORIA/Clase-3-Teoria.pdf` · 6 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Qué es HTML (hipertexto, marcado, elementos y etiquetas) y el ejemplo sencillo de documento |
| 2 | Estructura del documento: head (title, meta charset/name, link) y body |
| 3 | Fin del ejemplo de body; formularios: contenedor de controles; primer form (text + submit) |
| 4 | Atributo method: GET (características, ejemplo y URL resultante); comienzo de POST |
| 5 | POST: no cifra; ejemplo y solicitud HTTP; atributo action |
| 6 | Procesar en PHP: $_GET, $_POST, $_REQUEST; scripts con print_r y echo |

<!-- página 1 -->

Guía Básica del lenguaje PHP
Objetivo: Comprender el funcionamiento básico del lenguaje PHP.
Sitio oficial: http://www.php.net
ALGO DE HTML
HTML, que significa Lenguaje de Marcado de Hipertextos (HyperText Markup Language),
es la pieza más básica para la construcción de la web y se usa para definir el sentido y estructura
del contenido en una página web. Además de HTML se utilizan otras tecnologías para describir la
apariencia/presentación de una página web (CSS) o su funcionalidad (JavaScript).
"Hipertexto" se refiere a los enlaces que conectan las páginas web entre sí, ya sea dentro
de un mismo sitio web o entre diferentes sitios web.
HTML usa "marcado" (markup en inglés)  para anotar textos, imágenes y otro contenido
para ser mostrado en un navegador web. El marcado en HTML incluye "elementos" especiales
tales como <title>, <body>, <header>, <footer>, <article>, <section>, <p>, <div>, <span>, <img>,
<aside>, <audio>, <nav>, <output>, <video>, <ul>, <ol>, <li>, y muchos otros más.
Un elemento HTML se separa de otro texto en un documento por medio de "etiquetas", las
cuales consisten en elementos rodeados por "<" y ">".
Un ejemplo sencillo:
<!DOCTYPE html>
<html>
<head>
<title>Programación Avanzada</title>
</head>
<body>
<h1>Práctica de Programación Avanzada</h1>
<p>Éste es un ejemplo sencillo de un párrafo.</p>
</body>
</html>

<!-- página 2 -->

Estructura de un documento HTML
La estructura de un documento HTML consta principalmente de dos partes: el head y el
body.  Es  head es  la  parte  del  documento  que  primero  llega  al  navegador  web  y  contiene
instrucciones que le indican cómo debe mostrar el contenido (que llegará luego en el body).
Ejemplo head:
<!DOCTYPE html>
<html lang="es">
<head>
<title>Programación Avanzada</title>
<meta charset="UTF-8">
<meta name="title" content="Título de la WEB">
<meta name="description" content="Site Programación Avanzada">
<link href="/styles.css" rel="stylesheet" type="text/css"/>
</head>
<body>
….....
Note que todo el contenido del encabezado del documento se delimita dentro de las
etiquetas de apertura y cierre: <head> </head>.
El contenido (la parte visible del documento) se describe dentro de las etiquetas: <body>
</body>. Su contenido es mucho mas extenso ya que se incluye todo lo que debe mostrarse en la
página web:
<!DOCTYPE html>
<html lang="es">
<head>
<title>Programación Avanzada</title>
<meta charset="UTF-8">
<meta name="title" content="Título de la WEB">
<meta name="description" content="Site Programación Avanzada">
<link href="/styles.css" rel="stylesheet" type="text/css"/>
</head>

<!-- página 3 -->

<body>
<h1>Práctica de Programación Avanzada</h1>
<p>Éste es un ejemplo sencillo de un párrafo.</p>
</body>
 </html>
Existen muchas etiquetas que dan distintas funcionalidades y formatos al texto encerrado
entre ellas. De todas ellas solamente analizaremos la etiqueta <form> </form>.
Formularios HTML
Los formularios sirven para recolectar información proporcionada por los visitantes del sitio,
la cual luego es enviada al servidor. Para su funcionamiento el formulario en HTML debe ser
acompañado de un código del lado servidor que se encargará de recibir y procesar la información
como el autor vea conveniente.
Un formulario  <form> es básicamente un  contenedor de controles . Cada control en un
formulario está pensado para recolectar información ingresada por los usuarios, en formas que
pueden ir desde líneas de texto a subida de archivos, pasando por opciones, fechas, contraseñas
y otras más.
Una vez que los usuarios han rellenado el formulario con los datos, pueden  enviarlo de
regreso al servidor para que un script administre la información recolectada.
<form action="procesoFormulario.php" method=”post”>
<input type="text" name ="nombre" >
<input type="submit" value="Enviar el formulario">
</form>

<!-- página 4 -->

Atributos de un Formulario
Method = get / post
El atributo  method especifica cómo enviar los datos de formulario. Existen dos métodos
para enviar los datos desde el navegador hacia el servidor: get y post. Cuando se utiliza el método
get, los datos del formulario se envían como variables de URL anexándose a la misma de la forma
nombre=valor.
Algunas características:
Agrega datos de formulario a la URL en pares de nombre / valor.
La longitud de una URL es limitada (aproximadamente 3000 caracteres).
No se debe utilizar GET para enviar datos confidenciales! (será visible en la URL).
Útil para envíos de formularios donde un usuario desea marcar el resultado.
Ejemplo:
<form action="procesoFormulario.php" method=”get”>
Nombre: <input type="text" name ="nombre" >
Apellido: <input type="text" name ="apellido" >
<input type="submit" value="Enviar el formulario">
</form>
Al enviar el formulario la URL quedará de la siguiente forma:
http://localhost/procesoFormulario.php?nombre=Federico&apellido=Bonnet
Cuando  definimos  un  formulario  para  que  envíe  sus  datos  por  el  método  post
(method=post), éstos no se agregan a la URL sino que se anexan en el cuerpo de la solicitud
HTTP. De esta forma no tenemos límite en el tamaño y tipo de datos a enviar y no se exponen los
datos en la URL (por lo cual una contraseña no quedaría expuesta), pero ésto no quiere decir

<!-- página 5 -->

que los datos se cifren solamente no son expuesto en la barra de navegación.
Ejemplo:
<form action="procesoFormulario.php" method=”post”>
Nombre: <input type="text" name ="nombre" >
Apellido: <input type="text" name ="apellido" >
<input type="submit" value="Enviar el formulario">
</form>
Los datos se envían de la siguiente forma:
POST / HTTP/1.1
Host: localhost
Content-Type: application / x-www-form-urlencoded
Content-Length: 30
nombre=Federico & apellido=Bonnet
action
El atributo action determina el nombre del script al cual enviaremos los datos recabados
por el formulario a ser procesados. En nuestro ejemplo:
<form action="procesoFormulario.php" method=”get”>
Nombre: <input type="text" name ="nombre" >
Apellido: <input type="text" name ="apellido" >
<input type="submit" value="Enviar el formulario">
</form>
El script procesoFormulario.php será el encargado de recibir los datos enviados desde el
navegador a través del formulario. Deberemos programar en éste todas las instrucciones para
administrar esa información.

<!-- página 6 -->

Procesar los datos en PHP
Para procesar los datos provenientes de un formulario con PHP lo primero que deberemos
hacer es recuperar lo mismo. Para ésto PHP define una serie de arreglos que, dependiendo del
método que se utilizó en el formulario para enviar los datos, nos permitirán recuperar los mismos.
Estos arreglos son: $_GET, $_POST y $_REQUEST.
Si en el formulario definió: method=get, los datos los recuperará desde: $_GET.
Si en el formulario definió: method=post, los datos los recuperará desde: $_POST.
Ya sea que que utilice method=get o method=post, los datos siempre estarán disponibles en el
arreglo: $_REQUEST.
Un ejemplo:
<?php
print_r ( $_GET );
echo ( $_GET[ 'nombre' ] );
echo ( $_GET[ 'apellido' ] );
?>
<?php
print_r ( $_POST );
echo ( $_POST[ 'nombre' ] );
echo ( $_POST[ 'apellido' ] );
?>
