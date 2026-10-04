# PA-Clase-6

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 6/TEORIA/PA-Clase-6.pdf` · 4 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Guía Nº 6: objetivo y resumen de funciones de mysqli (`mysqli_connect`, `mysqli_connect_error`, `mysqli_errno`, `mysqli_query`, `mysqli_close`) y de mysqli_result (`mysqli_fetch_array`) |
| 2 | Ejercicio 1: crear con phpMyAdmin la base `DB_Comentarios` y la tabla `comentarios` (campos y tipos) |
| 3 | Ejercicios 2 (archivo de conexión: localhost, root, sin contraseña), 3 (alta; dice "punto 3" por "punto 2"), 4 (listado y link "Ver los Comentarios") y comienzo del 5 |
| 4 | Final del ejercicio 5: link o botón que ejecute `borrarComentario.php` |

<!-- página 1 -->

Guía Práctica de Ejercicios Nº 6
En esta clase repasaremos conceptos referidos a las bases de datos y de que manera
podemos hacer uso de ellas desde PHP. Estudiaremos las formas que tenemos para conectar
nuestra aplicación a un Sistema Gestor de Bases de Datos como lo es MySql y repasaremos las
funciones que nos provee la librería para el poder hacer altas, bajas y modificaciones de los datos.
Objetivo: Profundizar y comprender el acceso a bases de datos desde aplicaciones escritas en
PHP.
Resumen de los métodos de la clase mysqlli:
mysqli_connect(): Abrir una nueva conexión al servidor MySQL .
mysqli_connect_error(): Devuelve una cadena descriptiva del último error de conexión.
mysqli_errno(): Devuelve el código de error para la función invocada más reciente.
mysqli_query(): Ejecuta una consulta en la base de datos.
mysqli_close(): Cierra una conexión de base de datos previamente abierta.
Resumen de los métodos de la clase  mysqli_result:
mysqli_fetch_array(): Extrae la fila de resultados un array asociativo, numérico, o ambas.

<!-- página 2 -->

EJERCICIOS
Utilizar los conceptos de programación de base de datos
Para desarrollar ésta práctica deberemos de hacer uso de todos los script desarrollados en
la práctica 4. El objetivo es el realizar los script necesarios para conectarnos a la base de datos,
escribir los datos y mostrarlos.
1) – Creación de la Base de datos
Haciendo uso de PhpMyAdmin, cree una base de datos de nombre DB_Comentarios.
Dicha base de datos deberá contener una sola tabla de nombre comentarios con los siguientes
campos:
comentarios
id_comentario: INTEGER, not null, autoincrement
nombre: VARCHAR(100)
asunto: VARCHAR (150)
correo: VARCHAR (100)
comentario: VARCHAR (250)
El campo id_comentario deberá ser definido como clave primaria de la tabla al momento de
crear la misma.

<!-- página 3 -->

2) – Creación de un archivo de conexión:
Crear un script en PHP que permite establecer una conexión con el servidor MySQL. Las
credenciales de acceso deberán ser las siguientes;
Servidor: localhost
Usuario: root
Password: (sin contraseña)
Utilice para ésto las clases mysqlli y mysqli_result de PHP.
3) – Script de alta de comentarios:
Realice un script en PHP que permita tomar los datos del formulario y escribir dichos
comentarios en la tabla comentarios de la base de datos creada en el punto 1. Recuerde que el
nombre del script a crear deberá coincidir con el declarado en el atributo action de la etiqueta
form.
Para establecer la conexión a la base de datos utilice el archivo de conexión desarrollado
en el punto 3.
4) – Script para listar los comentarios.
Escriba un script en PHP que genere un listado de todos los comentarios guardados en la
base de datos.
Dicho script deberá ser ejecutado mediante el link “Ver los Comentarios”  incluido en la
página de inicio del sitio. Para ésto deberá modificar la etiqueta <a>  para que apunte al mismo.
5) – Script para borrar comentarios.
Modifique el script del punto 4 de manera tal que permita eliminar algún comentario en

<!-- página 4 -->

particular. Agregue para esto un botón o link a cada comentario listado que al presionarlo ejecute
el script borrarComentario.php, el cual deberá contener el código necesario para realizar tal tarea.
