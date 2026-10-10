# Practica_integral_patrones1

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/SEGUNDO CUATRIMESTRE/PATRONES DE DISEÑO/PRACTICA/Practica_integral_patrones1.pdf` · 6 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 |  |

<!-- página 1 -->

Ingeniería del software 2                                                    2023                                                    1

Patrones de Diseño
Parte 1

En esta guía práctica estudiaremos algunos patrones de diseño y aplicaremos los
conceptos vistos utilizando diagramas de clases en UML.
Para cada uno de los ejercicios modifique el diagrama de clases implementando el
patrón correspondiente para resolver cada uno de los problemas.

Ejercicio 1:
Se desea modelar el diagrama de clases de un sistema de alumnado, en el cual los
alumnos son evaluados por un y sólo un docente. Se debe implementar un patrón
para permitir esto, mencionamos a continuación las clases a utilizar.

Ejercicio 2:
Se desea modelar la parte de conexión a base de datos de un sistema, para ello se
necesita que sólo se pueda crear una instancia de un objeto llamado ConexionDB, el
cual también debe requerirse que solamente se pueda crear un solo objeto,
adjuntamos el diagrama de clases que existe actualmente:

<!-- página 2 -->

Ingeniería del software 2                                                    2023                                                    2

Ejercicio 3:
Se desea modelar un sistema de gestión automotor para una concesionaria,
necesitamos resolver un problema que tiene que ver co n la creación de los objetos,
adjuntamos parte del diagrama de clases:

Ejercicio 4:
Actualmente se desean implementar mejoras en un sistema de gestión para una
tienda que vende distintos tipos de productos (revistas, cds, libros), se desea
implementar una interface fácil y de simple acceso para que una clase Cliente pueda
interactuar de forma fácil para realizar compras y reclamos, adjuntamos parte de un
diagrama de clases:

<!-- página 3 -->

Ingeniería del software 2                                                    2023                                                    3

Patrones de Diseño
Parte 2

En esta guía práctica estudiaremo s algunos patrones de diseño y aplicaremos los
conceptos vistos utilizando diagramas de clases en UML.
Para cada uno de los ejercicios modifique el diagrama de clases implementando el
patrón correspondiente para resolver cada uno de los problemas.

Ejercicio 1:
Supongamos que tenemos un sistema que vende libros. Se desea vincular al sistema
una clase  de tipo libro digital con un funcionamiento diferente al que se está
manejando. Se debe adaptar la nueva clase sin que afecte la lógica de la aplicación.
Se adjunta una parte del diagrama de UML:

Ejercicio 2:
Se posee una clase Archivo, la cual cuenta con los siguientes atributos:
 Nombre
 Tamaño
 Contenido
Además se cuentan ya con 3 tipos de clases, las cuales exportan a diferentes formatos
(CSV, XLS, PDF).
Se desea que cuando se modifique el contenido del archivo, automáticamente se
invoquen a los 3 exportadores para publicar los cambios inmediatamente en el
sistema.

<!-- página 4 -->

Ingeniería del software 2                                                    2023                                                    4

Ejercicio 3:
Considere la clase Archivo del ejercicio 2, se desea modelar ahora una estr uctura de
directorios, en donde un archivo puede contener más archivos (suponemos que un
directorio es un tipo especial de archivo).
Realice un diagrama de clases implementando el patrón Composite, para resolver éste
problema.

Ejercicio 4:
Diga que patrón se está utilizando en este ejemplo e indique cuáles son las partes de
la estructura del patrón.

Ejercicio 5:
Se quiere construir un editor de expresiones matemáticas. Especificar el diagrama de
clases que permita representar expresiones válidas haciendo uso de patrones.
Una expresión válida estará formada o bien por un número o bien por la
suma/resta/división/multiplicación de dos expresiones.

Ejemplo de expresiones válidas:
 4
 3+8
 14*(3+5)

<!-- página 5 -->

Ingeniería del software 2                                                    2023                                                    5

Patrones de Diseño
Parte 3 ‘Adicionales’

Ejercicio 1.
El siguiente diagrama de clases modela el funcionamiento de un sistema de gestión de
expedientes para un organismo público del estado. El objetivo del diagrama es
modelar el funcionamiento del módulo de envío y recepción de expedientes entre
distintos organismos.

Se solicita modelar en un nuevo diagrama de clases la resolución de los siguientes
problemas (indicando que patrón y justificando en cada caso el porqué de la elección
de ese patrón):
1- Debido a que se cuenta con múltiples organismos y los mismos  se encuentran en
una estructura de jerarquía, se necesita modelar dicho requerimiento, en el cual un
organismo puede tener organismos hijos y organismos padres.
2- Se desea crear una clase para mantener la seguridad de los usuarios, llamada
GestorUsuarios, dicha clase tendrá métodos para realizar el login del sistema, cambiar
la contraseña del usuario, dar de baja y dar de alta usuarios, por motivos de
performance se desea crear una sola instancia de dicha clase.
3- Se necesita implementar mecanismos de au ditoría sobre los movimientos que se
realizan de expedientes, para esto es necesario que cada vez que se realice un
movimiento, se envíe una alerta al administrador y se registre éste suceso en una
tabla de auditoría. Es deseable a futuro implementar nuevos mecanismos de alerta.

<!-- página 6 -->

Ingeniería del software 2                                                    2023                                                    6
Ejercicio 2.
El siguiente diagrama modela la parte de un sistema encargada de la gestión de
diverso tipo de contenido.
Se brinda la posibilidad a los usuarios de realizar publicaciones, permitiendo adjuntar
a las mismas distintos t ipos de archivos, cada uno de ellos con un tamaño máximo
permitido distinto.

A continuación, se nos solicita realizar las siguientes modificaciones:
1- Se desea agregar la posibilidad de adjuntar archivos de tipo JPG, TXT y de poder
agregar nuevos tipos de archivo en el futuro.
2- Se desea poder organizar la estructura de archivos en carpetas, en donde una
carpeta es un tipo de archivo que contiene más archivos.
3- Se desean implementar notificaciones, de manera tal que cada vez que se cree una
notificación, se envíe un mail al administrador del sistema y se notifique dicho suceso
en una tabla de auditoría.
4. Se desea implementar un Gestor de Contenido, cuyo rol será el encargado de
realizar las publicaciones, así como también se permitirá su ed ición y borrado lógico,
se nos ha planteado la necesidad de contar con una sola instancia de esta clase como
máximo.
