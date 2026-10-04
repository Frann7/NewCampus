# PA-Clase-3

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 3/PRACTICA/PA-Clase-3.pdf` · 4 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Objetivo de la guía (figura como Nº 4); definición de $_GET, $_POST y $_REQUEST (GET, POST y COOKIE) |
| 2 | Ejercicio 1 (index.php). ⚠ ver el PDF: captura de la página de inicio (textos, dos enlaces con íconos) |
| 3 | Enlaces del ej. 1; ejercicio 2 (formContacto.php, POST). ⚠ ver el PDF: captura del formulario (Nombre, Asunto, Correo, Cometario, Restablecer, Enviar, Volver) |
| 4 | Ejercicios 3 (procesoForm.php con $_POST) y 4 (pasar a GET). ⚠ ver el PDF: captura de la salida con datos de ejemplo |

<!-- página 1 -->

Guía Práctica de Ejercicios Nº 4
En esta cuarta clase repasaremos conceptos referidos al lenguaje utilizado para escribir
páginas web: HTML.
Veremos la estructura que debe cumplir una página web y haremos uso de algunas de las
etiquetas mas populares. Luego nos centraremos en la creación de formularios: estudiaremos los
métodos de envío, los componentes y de que manera podemos recuperar la información desde
nuestra aplicación PHP para poder hacer uso de ella
Objetivo:  Profundizar y comprender conceptos referidos a la creación de formularios HTML.
Variables de PHP con las que trabajaremos.
$_GET arreglo cuyo contenido es el par nombre/valor de cada uno de los elementos que
forman parte del formulario. Este arreglo es generado cuando el formulario es enviado por
GET.
$_POST arreglo cuyo contenido es el par nombre/valor de cada uno de los elementos que
forman parte del formulario. Este arreglo es generado cuando el formulario es enviado por
POST.
$_REQUEST arreglo asociativo cuyo contenido son los valores de $_GET, $_POST y
$_COOKIES. Este arreglo es generado cuando el formulario es por cualquiera de los dos
métodos $_GET y $_POST.

<!-- página 2 -->

EJERCICIOS
Utilizar los conceptos de programación HTML.
La práctica tiene como objetivo desarrollar un pequeño sitio web en el que se le ofrezca al
navegante la posibilidad de escribir comentarios y poder leerlos posteriormente.
En esta primer etapa nos dedicaremos al desarrollo de todas las páginas web que
componen el sitio y, en clases posteriores, haremos que todos los datos sean escritos y leídos
desde una base de datos.
1) – Escriba el código HTML necesario para desarrollar una página web de inicio al portal.
El nombre de dicho archivo deberá ser index.php y deberá presentar lo siguiente:

<!-- página 3 -->

El sitio deberá contener dos enlaces:
• Agregar Comentario
• Ver los Comentarios
Al hacer click en “Agregar Comentario” nos deberá mostrar el formulario presentado en el
punto 2.
El enlace “Ver los Comentarios” nos deberá mostrar todos los comentarios enviados. Éste
punto lo desarrollaremos en la clase 5.
2) – Escriba el código HTML necesario para desarrollar el formulario presentado a
continuación:
Guarde el archivo con el nombre formContacto.php y dicho formulario deberá enviar los
datos por el método post. El enlace “volver” nos deberá llevar nuevamente al archivo index.html.
Al presionar el botón “Enviar”, los datos del formulario deberán ser enviados a un script php

<!-- página 4 -->

de nombre procesoForm.php el cual deberá mostrar la información como se indica en el punto 3.
3) – Escriba el código HTML y PHP necesario para mostrar los datos recibidos del
formulario del punto 2.  Guarde el script con el nombre procesoForm.php y asegúrese de ser el
mismo nombre declarado en el campo “action” declarado en el formulario.
Utilice para recuperar los datos el arreglo $_POST de PHP
4) – Modifique el formulario del punto 2 de manera tal que los datos se envíen por el
método GET. Haga también los cambios necesarios en el script php procesoForm.php para que
los datos puedan ser mostrados en pantalla.
