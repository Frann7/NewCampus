# PA-Clase-5

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 5/PRACTICA/PA-Clase-5.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Objetivo (seguridad y validación en formularios) y funciones: session_start, $_SESSION, captcha, ctype_digit, ctype_alpha, ctype_alnum |
| 2 | Ejercicios: 1) captcha en el formulario de contacto; 2) validar código y datos con ctype_; 3) pantalla de error |

<!-- página 1 -->

Guía Práctica de Ejercicios Nº 4
En esta sexta clase estudiaremos conceptos de seguridad y validación de datos en
formulario. El caso puntual a analizar es el de la utilización de captcha en el formulario.
Estudiaremos de qué manera esta técnica puede ayudarnos a mitigar ataque a nuestros
formularios..
Por último estudiaremos algunas funciones que nos permitirán analizar el tipo de datos que
nos llegan desde el formulario evitando así cualquier tipo de datos que puedan atentar con
nuestras bases de datos.
Objetivo:  Revisar conceptos de seguridad y de validación de datos en formularios web.
Funciones con las que trabajaremos.
session_start(): crea una sessión o reanuda una sesion ya establecida.
$_SESSION[]: arreglo que nos permite almacenar datos en una sesion.
captcha: técnica que nos permite autenticar un formulario.
ctype_digit(): devuelve true si el dato pasado como parámetro es un números.
ctype_alpha(): devuelve true si los datos pasados como parámetro son caracteres.
ctype_alnum(): devuelve true si los datos pasados como parámetro son caracteres y
números.

<!-- página 2 -->

EJERCICIOS
Aplicar seguridad al formulario de contacto
En ésta práctica daremos seguridad a través del uso de captcha al formulario de contacto
desarrollado en las clases anteriores.
1) – Aplicación de captcha.
Solicite a la cátedra los script necesarios para incrustar un código verificador al formulario.
Modifique el código del mismo para que pueda incluirse la imagen del captcha y un campo de
texto que permita ingresar los caracteres.
2) – Validación del formulario.
Modifique el script que agrega los datos al formulario de manera tal que se valide primero
el código verificador y luego, haciendo uso de las funciones ctype_, que valide los datos recibidos
desde el form antes de ser guardados en la base de datos.
3) – Pantalla de error.
En caso de que alguna de las pruebas de validación no sea pasada, diseñe una página
que muestre el error que ha ocurrido y que permita volver al formulario para cargar los datos
nuevamente.
