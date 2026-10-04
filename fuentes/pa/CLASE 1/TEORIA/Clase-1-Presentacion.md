# Clase-1-Presentacion

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 1/TEORIA/Clase-1-Presentacion.pdf` · 20 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Temario: etiquetas, variables, estructuras de control (if-else, switch, while, do...while, for) |
| 2 | Portada de sección "Etiquetas en PHP" (solo el título; no hace falta el PDF) |
| 3 | Etiquetas `<?php` y `?>`: lo de afuera no lo procesa PHP |
| 4 | Comentarios de una línea (`//`, `#`) y de bloque (`/* */`) |
| 5 | Portada de sección "Variables en PHP" (solo el título; no hace falta el PDF) |
| 6 | Variables: `$`, reglas de nombres, mayúsculas; ejemplos |
| 7 | Las variables no se tipan; ejemplo color/número con concatenación |
| 8 | Portada de sección "Operadores" (solo el título; no hace falta el PDF) |
| 9 | Lista de operadores (incluye `===`) |
| 10 | Portada "Estructuras de control" (solo el título) |
| 11 | Estructuras de control: condicionales e iterativas |
| 12 | Condicionales: if-else, switch-case |
| 13 | Sintaxis de if-else |
| 14 | Sintaxis de if anidado (else if) |
| 15 | Sintaxis de switch-case |
| 16 | Iterativas: while, do...while, for |
| 17 | Definición de estructuras iterativas (incluye foreach) |
| 18 | Sintaxis de while |
| 19 | Sintaxis de do...while (con `while{condicion}`) |
| 20 | Sintaxis de for (con `;`, bien escrita) |

<!-- página 1 -->

TEMAS A DESARROLLAR
Etiquetas en PHP
Variables
Estructuras de Control
Estructuras Condicionales
If-else
switch - case
Estructuras Iterativas
while()
do...while()
for

<!-- página 2 -->

Etiquetas en PHP

<!-- página 3 -->

Etiquetas en PHP
Cuando PHP procesa un fichero reconoce las etiquetas de apertura y de cierre, <?php y ?>, para
definir los límites de la ejecución del código PHP. El contenido fuera de las etiquetas es ignorado por el
analizador PHP, permitiendo a PHP integrarse de manera transparente en diversos tipos de documentos.
<?php
        echo “Este código es procesado por php.”;
?>
Esto no es procesado por php.

<!-- página 4 -->

Comentar código en PHP
Existen dos formas de comentar código: comentarios de una sola línea y comentarios de bloque.
Los comentarios de una sola línea se utilizan para agregar explicaciones breves a una línea del código y
se indican con // o #.  Los comentarios de bloque son útiles para comentarios más extensos y se
delimitan por /* y */.
<?php
// comentario de una línea. # comentario de una línea.
/* comentario
    de varias líneas
*/

<!-- página 5 -->

Variables en PHP

<!-- página 6 -->

Variables en PHP
En PHP las variables se identifican con un signo de dólar $, seguido del nombre del identificador.
Pueden utilizarse letras (az, AZ), números y el carácter de subrayado. Su nombre puede comenzar con
una letra o un guión bajo pero no con un número. Además, el nombre de una variable es sensible a
mayúsculas y minúsculas.
Ejemplo:
$color = 'rojo';
$numero = 5;
$_arreglo = array();

<!-- página 7 -->

Variables en PHP
En PHP las variables NO DEBEN SER TIPADAS antes de comenzar a utilizarlas. Solamente las
declaro asignándoles un valor y las utilizo.
Ejemplo:
<?php
$color = 'rojo';
$numero = 5;
echo 'Mi color favorito es el:  '.$color;
echo 'Mi número favorito es el: '.$numero;
?>

<!-- página 8 -->

Operadores

<!-- página 9 -->

Operadores en PHP
De asignación: =
Aritméticos: +,  - ,  * ,  /  ,  % ,  ++ ,  --
De comparación: ==, === , != , < , > , <= ,  >=
Lógicos: and (&&) , or (||) , not (!)
De cadena . (concatenación),  = (asignación)

<!-- página 10 -->

Estructuras de control

<!-- página 11 -->

Estructuras de control
Permiten controlar el flujo de datos a lo largo de la ejecución de un script. PHP dispone de una serie
de estructuras de control diferentes y aunque algunas de ellas pueden parecer redundantes, simplifican
notablemente el desarrollo de los scripts.
Encontramos dos tipos de estructuras de control:
Estructuras condicionales.
Estructuras iteractivas.

<!-- página 12 -->

Estructuras condicionales
If-else
switch-case

<!-- página 13 -->

 if – else
Permite determinar que acciones tomar dada o no cierta condición. Su sintaxis:
if (condición){
 opción o sentencia verdadera;
}else{
 opción o sentencia falsa;
}

<!-- página 14 -->

 if – else
Podemos anidar distintas estructuras if. Su sintaxis:
if (condicion1){
 opción o sentencia verdadera;
}else if(condicion2){
 opción o sentencia verdadera (condición2);
   }else{
 opción o sentencia falsa (condición1);
   }
}

<!-- página 15 -->

switch - case
Compara que se cumpla una u otra condición. Su sintaxis:
switch ($variable){
case condicion1:
//ejecución de la acción
break;
case condicion2:
//ejecución de la acción
break;
default:
//la acción que se ejecutará por defecto
break;
}

<!-- página 16 -->

Estructuras iteractivas
while
do...while
for

<!-- página 17 -->

Estructuras iteractivas
Este tipo de estructuras hacen posible la ejecución de una o mas líneas de código un número
determinado de veces. Como construcciones iterativas podemos encontrar while(), do....while(), for() y
foreach().

<!-- página 18 -->

while()
Su sintaxis es la siguiente:
while(condicion){
Sentencia_1;
Sentencia_2;
sentencia_n;
}

<!-- página 19 -->

do...while()
Su sintaxis es la siguiente:
do{
Sentencia_1;
Sentencia_2;
sentencia_n;
}while{condicion}

<!-- página 20 -->

for()
Su sintaxis es la siguiente:
for  (inicio; condición; incremento){
Sentencia_1;
Sentencia_2;
Sentencia_n;
}
