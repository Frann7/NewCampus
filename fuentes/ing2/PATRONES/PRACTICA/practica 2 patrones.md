# practica 2 patrones

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/SEGUNDO CUATRIMESTRE/PATRONES DE DISEÑO/PRACTICA/practica 2 patrones.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |

<!-- página 1 -->

Ingeniería de Software II
Patrones de Diseño
Parte 2

En esta guía práctica estudiaremos algunos patrones de diseño y aplicaremos los conceptos vistos
utilizando diagramas de clases en UML.
Cuando corresponda r eescriba el diagrama de clases implementando el patrón  correspondiente para
solucionar el problema mencionado.

Ejercicio 1:
Supongamos que tenemos un sistema que vende libros.  Se desea vincular al sistema una clase
de tipo libro digi tal con un funcionamiento diferente al que se est á manejando. Se debe
adaptar la nueva clase sin que afecte la lógica de la aplicación.
Se adjunta una parte del diagrama de UML:

Ejercicio 2:

Se posee una clase Archivo, la cual cuenta con los siguientes atributos:
 Nombre
 Tamaño
 Contenido

Además se cuentan ya con 3 tipos de clases, las cuales exportan a diferentes formatos (CSV,
XLS,PDF).
Se desea que cuando se modifique el contenido del archivo, automáticamente se invoquen a los 3
exportadores para publicar los cambios inmediatamente en el sistema.

Ejercicio 3:

Considere la clase Archivo del ejercicio 2, se desea modelar ahora una estructura de directorios, en
donde un archivo puede contener más archivos (suponemos que un directorio es un tipo especial de
archivo).
Realice un diagrama de clases implementando el patrón Composite, para resolver éste problema.

Libro
+agregarstock()
Administrable
<<interface>>
+agregarstock()
+eliminarstock()
+vender()
+nombre
+isbn
+eliminarstcok()
+vender()
+vender()
Libro digital

<!-- página 2 -->

Ejercicio 4:
Diga que patrón se está utilizando en este ejemplo e indique cuáles son las partes de la  estructura del
patrón

Ejercicio 5:
Se quiere construir un editor de expresiones matemáticas. Especificar el diagrama de clases que
permita representar expresiones válidas haciendo uso de patrones.
Una expresión válida estará formada o bien por un númer o o bien por la suma/resta/división
/multiplicación de dos expresiones.
Ejemplo de expresiones válidas:
4
                                                       3+8
14*(3+5)

Ejercicio 6:

Se quiere desarrollar una aplicación de gestión de stock de un negocio que vende diferentes
familias de productos. Se necesita crear por ahora productos de música (CD,DVD) y
productos de computación (pc, notebook, tablet).
Se requiere crear diariamente una lista única de productos en oferta para publicar via web.
