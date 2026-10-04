# PA_Clase_11_resuelta

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 1/PRACTICA/PA_Clase_11_resuelta.pdf` · 6 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Encabezado y objetivo (igual a la guía) |
| 2 | Ej. 1: enunciado y comienzo del código (resuelve estaciones según `$mes`, no el día de la semana) |
| 3 | Ej. 1: casos 5 a 12 y default |
| 4 | Ej. 1: cierre; ej. 2 (while, `echo ($c*2)."<br/>"`); ej. 3 (do...while), comienzo |
| 5 | Ej. 3: cierre; ej. 4 (for, cuadrado); ej. 5 (continue, arranca en `$i = 0`); ej. 6, comienzo |
| 6 | Ej. 6: cierre (break; arranca en `$i = 0` con `$i < 10`) |

<!-- página 1 -->

Guía Práctica de Ejercicios Nº 2
En esta segunda clase investigaremos las estructuras de control y los iteradores en PHP.
Analizaremos su sintaxis, su funcionamiento y desarrollaremos algunos ejemplos de su
funcionamiento.
Objetivo: Comprender el funcionamiento básico de los iteradores y de las estructuras de
control en PHP.
Introducción: en todo lenguaje de programación  encontramos distintas estructuras, ya
sean de control o de interacción, que permiten cambiar el flujo de ejecución de nuestros
programas basándose en la evaluación de una o mas condiciones. En base a ésto es que se hace
necesario dar un repaso de su funcionamiento y de la sintaxis que PHP utiliza  para declarar cada
una de ellas.
Estructuras que estudiaremos en esta unidad.
Estructuras
• if – else:
• switch/case
• while
• do-while
• for
• break
• continue

<!-- página 2 -->

EJERCICIOS
1) – Realice un nuevo script PHP que permita determinar el día de la semana utilizando la
estructura switch para tal fin, deberá declarar e inicializar una variable de tipo entera para guardar
el número de día de la semana que comienza con el día Domingo y termina con el día Sábado
(Domingo = 0, Lunes = 1, Martes = 2, etc.). Deberá ir mostrando los resultados de cada operación
en pantalla y también deberá documentar cada operación.
<?php
$mes = 4;
// Se consulta por los meses del año correspondientes a cada
Estación
switch ($mes) {
case 1:
            echo “Estamos en Verano”;
            break;
case 2:
            echo “Estamos en Verano”;
            break;
        case 3:
             echo “Estamos en Verano u Otoño”;
            break;
        case 4:
             echo “Estamos en Otoño”;
            break;
        case 5:
             echo “Estamos en Otoño”;

<!-- página 3 -->

            break;
        case 6:
             echo “Estamos en Otoño o Invierno”;
            break;
case 7:
             echo “Estamos en Invierno”;
            break;
    case 8:
             echo “Estamos en Invierno”;
            break;
     case 9:
             echo “Estamos en Invierno o Primavera”;
            break;
case 10:
             echo “Estamos en Primavera”;
            break;
case 11:
             echo “Estamos en Primavera”;
            break;
case 12:
             echo “Estamos en Primavera o Verano”;
            break;
default:
            echo “Número de mes incorrecto.”;

<!-- página 4 -->

}
?>
2) – Realice un nuevo script PHP que recorra números del 1 al 100  y que calcule el doble
de cada uno de ellos. Utilice la sentencia while para recorrer los mismos. Deberá ir mostrando los
resultados de cada operación en pantalla y también deberá documentar cada operación.
<?php
$c = 1;
// Se recorren los números que van del 1 al 100 con while
while ($c <= 100) {
echo ($c*2).”<br/>”;
$c++;
}
?>
3) – Escriba un nuevo script PHP que realice la misma tarea del punto anterior pero que
utilice la sentencia do .. while para recorrer los mismos. Deberá ir mostrando los resultados de
cada operación en pantalla y también deberá documentar cada operación.
<?php
$c = 1;
// Se recorren los números que van del 1 al 100 con do .. while
do {
echo ($c*2).”<br/>”;
$c++;
} while ($c <= 100);

<!-- página 5 -->

?>
4) – Realice un nuevo script PHP que recorra números del 1 al 100  y que calcule el
cuadrado de cada uno de ellos. Utilice la sentencia for para recorrer los mismos. Deberá ir
mostrando los resultados de cada operación en pantalla y también deberá documentar cada
operación.
<?php
for ($c = 1; $c <= 100; $c++) {
echo ($c*$c).”<br/>”;
}
?>
5) Realizar un script que muestra los números del 1 al 10 utilizando un ciclo for() pero sin
mostrar los números 4, 5 y 6 utilizando la sentencia continue.
<?php
for ($i = 0; $i <= 10; $i++) {
if ($i > 3 && $i <= 6) {
continue;
}
echo “Numero: “.$i;
}
?>
6) Realizar un script que muestra los números del 1 al 10 utilizando un ciclo for() pero si el
numero es mayor a 4 se termine el ciclo, utilizando la sentencia break.
<?php
for ($i = 0; $i < 10; $i++) {

<!-- página 6 -->

if ($i > 4 ) {
break;
}
echo “Numero: “.$i;
}
?>
