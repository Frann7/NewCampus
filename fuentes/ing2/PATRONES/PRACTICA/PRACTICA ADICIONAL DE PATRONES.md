# PRACTICA ADICIONAL DE PATRONES

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/SEGUNDO CUATRIMESTRE/PATRONES DE DISEÑO/PRACTICA/PRACTICA ADICIONAL DE PATRONES.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |

<!-- página 1 -->

1

PRACTICA ADICIONAL DE PATRONES
Ejercicio 1.
El siguiente diagrama de clases modela el funcionamiento de un sistema de gestión d e
expedientes para un organismo público del estado. El objetivo del diagrama es modelar e l
funcionamiento del módulo de envío y recepción de expedientes entre distintos organismos.

Se solicita modelar en un nuevo diagrama de clases la resolución de los siguientes problemas
(indicando que patrón y justificando en cada caso el porqué de la elección de ese patrón):
1- Debido a que se cuenta con múltiples organismos y los mismos se encuentran en una
estructura de jerarquía, se necesita modelar dicho requerimiento, en el cual u n
organismo puede tener organismos hijos y organismos padres.

2- Se desea crear una clase para mantener la seguridad de los usuarios, llamad a
GestorUsuarios, dicha clase tendrá métodos para realizar el login del sistema, cambiar
la contraseña del usuario, dar de baja y dar de alta usuarios, por motivo s de
performance se desea crear una sola instancia de dicha clase.

3- Se necesita implementar mecani smos de auditoría sobre los movimientos que s e
realizan de expedientes, para esto es necesario que cada vez que se realice u n
movimiento, se envíe una alerta al administrador y se registre éste suceso en un a
tabla de auditoría. Es deseable a futuro implementar nuevos mecanismos de alerta.

<!-- página 2 -->

2

Ejercicio 2.
El siguiente diagrama modela la parte de un sistema encargada de la gestión de diverso tipo
de contenido.
Se brinda la posibilidad a los usuarios de realizar publicaciones, permitiendo adjuntar a las
mismas distintos tipo s de  archivos, cada uno de ellos con un tamaño máximo permitido
distinto.

A continuación, se nos solicita realizar las siguientes modificaciones:
1- Se desea agregar la posibilidad de adjuntar archivos de tipo JPG, TXT y de poder
agregar nuevos tipos de archivo en el futuro.
2-  Se desea poder organizar la estructura de archivos en carpetas, en donde una
carpeta es un tipo de archivo que contiene más archivos.
3- Se desean implementar notificaciones, de manera tal que cada vez que se cree una
notificación, se envíe un mail al administrador del sistema y se notifique dicho suceso en
una tabla de auditoría.
4. Se desea implementar un Gestor de Contenido, cuyo rol será el encargado de realizar
las publicaciones, así como también se permitirá su edición y borrado lógico, se nos  ha
planteado la necesidad de contar con una sola instancia de esta clase como máximo.
