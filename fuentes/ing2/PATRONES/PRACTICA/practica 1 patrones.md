# practica 1 patrones

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/SEGUNDO CUATRIMESTRE/PATRONES DE DISEÑO/PRACTICA/practica 1 patrones.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |

<!-- página 1 -->

Ingeniería de Software II
Patrones de Diseño
Parte 1

En esta guía práctica estudiaremos algunos patrones de diseño y aplicaremos los conceptos
vistos utilizando diagramas de clases en UML.
Para cada uno de los ejercicios modifique el diagrama de clases implementando el patrón
correspondiente para resolver cada uno de los problemas.

Ejercicio 1:
Se desea modelar el diagrama de clases de un sistema de alumnado, en el cual los alumnos son
evaluados por un y sólo un docente. Se debe implementar  un patrón para permitir esto,
mencionamos a continuación las clases a utilizar.

Estudiante
-materiasAprobadas: Long
Profesor
+numeroLegajo: Long
+evaluarAlumno(Alumno)
Persona
-Apellido: String
-Nombre: String
-fechaNacimiento: Date

Ejercicio 2:

Se desea modelar la parte de conexión a base de datos de un sistema, para ello se necesita
que sólo se pueda crear una instancia de un objeto llamado ConexionDB , el cual también debe
requerirse que solamente se pueda crear un solo objeto, adjuntamos el diagrama de clases
que existe actualmente:
ConexionDB
-usuario: String
-password: String
-host: String
+Resultado obtenerResultado(Sentencia)
Sentencia
-consulta: String
Resultado
-cantidadFilas: Long

<!-- página 2 -->

Ejercicio 3:
Se desea modelar un sistema  de gestión automotor para una concesionaria, necesitamos
resolver un problema que tiene que ver con la creación de los objetos, adjuntamos parte del
diagrama de clases:
Vehículo
-nombre: String
-fechaCreacion: Date
-marca: String
Auto CamionetaMotocicleta

Ejercicio 4:
Actualmente se desean implementar mejoras en un sistema de gestión para una tienda que
vende distintos tipos de productos (revistas, cds, libros), se desea implementar una interface
fácil y de simple  acceso para que una clase Cliente  pueda interactu ar de forma fácil para
realizar compras y reclamos, adjuntamos parte de un diagrama de clases:
LibroCDRevistaCliente
Producto
