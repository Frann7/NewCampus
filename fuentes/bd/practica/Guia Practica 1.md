# Guia Practica 1

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/PRACTICA/Guia Practica 1.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |

<!-- página 1 -->

Guía de Práctica N° 1  Bases de Datos - Facultad de Ciencia y Tecnología

1

El objetivo del presente trabajo es simular un archivo secuencial indexado en memoria,
cumpliendo las siguientes características:
El área de datos del archivo se representa en un arreglo de registros. Cada registro
(elemento del arreglo) está compuesto por campo clave, un campo genérico de datos y
uno para contener direcciones.
Los registros se agrupan en bloques de n registros. Los registros se encuentran ubicados
en orden ascendente de su clave y cuando la misma es cero se supone un elemento vacío
del arreglo. Este arreglo de registros está dividido en dos partes, la primera, llamada el
área primaria de datos, cuyo tamaño está dado por la variable PMAX, y la de Overflow,
que inicia en PMAX+1 = OVER, y que llega hasta OMAX (dimensión del arreglo).
La parte indexada se implementa a través de una tabla de dos columnas. La primera
columna se denomina CLAVE y contiene la clave de menor valor que tiene el bloque o
grupo de registros en que se divide el arreglo. La segunda columna se denomina DIR y
contiene la dirección del bloque asociado a la clave.
Se deben desarrollar dos algoritmos, uno para consultas y otro para inserción de registros
en la estructura generada, respetando el funcionamiento de un archivo secuencial
indexado.
1) Para la función de consulta, recibe como entrada la CLAVE que desea consultar y como
salida los datos del Registro.
2) Para la inserción, se tienen como entradas la CLAVE y los datos del Registro, y deben
tener en cuenta las siguientes consideraciones:
 Los registros dentro de cada bloque deben estar en orden ascendente por su clave.
 Si la inserción corresponde al último registro del bloque y el número de los mismos
es igual o mayor a n/2 iniciar un nuevo bloque conservando todas las
características del archivo definido. Si la inserción corresponde en un espacio
intermedio del bloque, y no hay espacio en el mismo, se supone n, ubicar el
registro en el área de Overflow y poner en el último registro del bloque la dirección
del mismo.
 Escribir mensajes para reorganizar el archivo cuando no se tiene más lugar para
abrir un nuevo bloque (se supera PMAX) y para cuando no se tiene más lugar en el
área de Overflow (se supera OMAX))

Son valores dados: n (número de registros por bloque), OVER (Comienzo del área de
Overflow), OMAX (Fin del arreglo)

<!-- página 2 -->

Guía de Práctica N° 1  Bases de Datos - Facultad de Ciencia y Tecnología

2
