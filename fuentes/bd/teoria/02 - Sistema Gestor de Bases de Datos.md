# 02 - Sistema Gestor de Bases de Datos

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/APUNTES DE LA MATERIA/02 - Sistema Gestor de Bases de Datos.pdf` · 8 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |

<!-- página 1 -->

Bases de Datos - Apuntes Hoja Nº 1
Sistema Gestión De Bases De Datos
Un Sistema de Gestión de Bases de Datos (SGBD) es el conjunto de programas que
permiten definir, manipular y utilizar la información que contienen las bases de datos,
realizar todas las tareas de administración necesarias para mantenerlas operativas,
mantener su integridad, confidencialidad y seguridad. Una BD nunca se accede o manipula
directamente sino a través del SGBD. Se puede considerar al SGBD como el interfaz entre
el usuario y la BD.
El funcionamiento del SGBD está muy interrelacionado con el del Sistema Operativo,
especialmente con el sistema de comunicaciones. El SGBD utilizará las facilidades del
sistema de comunicaciones para recibir las peticiones del usuario (que puede estar
utilizando una terminal físicamente remota) y para devolverle los resultados.
Funciones de un SGBD
Un SGBD debe proporcionar un amplio surtido de funcionalidades para poder cumplir
adecuadamente su misión. Normalmente se clasifican en definición, manipulación y
utilización.
•Función de definición : Permite describir los elementos de datos, sus estructuras,
sus interrelaciones y sus validaciones a nivel externo, lógico e interno. Esta función
es realizada por una parte del SGBD denominada lenguaje de definición de datos
(LDD o DDL, Data Definición Lenguaje).
•Función de manipulación : Permite buscar, añadir, suprimir y modificar los datos
de la BD. Esta función es realizada por una parte del SGBD denominada lenguaje
de manipulación de datos (LMD o DML, Data Manipulación Lenguaje).
•Función de utilización: Incluye otras funcionalidades tales como: modificar la
capacidad de los registros, cargar archivos, realizar copias de seguridad, arranque,
protección frente a accesos no autorizados, gestión de la concurrencia, estadísticas
de utilización, etc.
El sistema de gestión de la base de datos (SGBD) es una aplicación que permite a los
usuarios definir, crear y mantener la base de datos, y proporciona acceso controlado a la
misma.

<!-- página 2 -->

Bases de Datos - Apuntes Hoja Nº 2
SGBD: es una agrupación de programas que sirven para definir, construir y manipular una
base de datos.
 En la manipulación de una base de datos, los SGBD deben incluir un control de
concurrencia, o sea, deben permitir a varios usuarios tener acceso “simultáneo” a la
base de datos. Controlar la concurrencia implica que si varios usuarios acceden a la
base de datos, la actualización de los datos se haga de forma controlada para que no
haya problemas.
 Un SGBD también debe encargase de cumplir las reglas de integridad y redundancias.
 Otra función importante en un SGBD es su capacidad de realizar copias de seguridad y
de recuperación de datos.
 Restricción de accesos no autorizados.
 Suministrar múltiples interfaces de usuario.
 Representar relaciones complejas entre los datos.
 Un SGBD debe incluir por lo menos las siguientes funciones:
 Definición de los Datos . El SGBD debe ser capaz de aceptar las definiciones de
datos en versión fuente y convertirlas en la versión objeto. El SGBD debe incluir
componentes procesadores para cada uno de los lenguajes de definición de
datos (LDD).
 Manipulación de los Datos . El SGBD debe atender las solicitudes de los
usuarios para extraer, actualizar, adicionar o suprimir datos. El SGBD debe
incluir un componente procesador del Lenguaje de manipulación de datos
(LMD).
 Seguridad e Integridad de los Datos. El SGBD debe supervisar las solicitudes de
los usuarios y rechazar los intentos de violar las medidas de seguridad e
integridad definidas por el Administrador de la Base de Datos DBA.
 Recuperación y concurrencia de los datos . El principal objetivo de la
implantación de una base de datos es poner a disposición de un gran número
de usuarios en conjunto integrado de datos, estos datos podrán ser
manipulados por los diferentes usuarios y es ahora cuando se debe garantizar
la coherencia de los datos después de las diversas manipulaciones.
 Diccionario de Datos.
 Desempeño. El SGBD debe ejecutar todas las funciones en la forma eficiente.

<!-- página 3 -->

Bases de Datos - Apuntes Hoja Nº 3
Componentes de un Sistema de Gestión de Base de Datos.
Un Sistema de Gestión de Base de Datos se divide en módulos que tratan cada una de las
responsabilidades del sistema general. Los componentes funcionales de un SGBD
incluyen:
 Procesador de Consultas. Traduce sentencias en un lenguaje de consultas a
instrucciones de bajo nivel que entiende el gestor de la base de datos.
 Gestor de la Base de Datos. Proporciona la interface entre los datos de
bajo nivel almacenados en la base de datos y los programas de aplicación y
las consultas que se hacen en el sistema.
 Gestor de Archivos. Gestiona la asignación de espacio en la memoria del
disco y de las estructuras de datos usadas para representar la información
almacenada en disco.
 Pre compilador del Lenguaje de Manipulación de Datos DML. Convierte las
sentencias en DML incorporadas en un programa de aplicación en llamadas
normales a procedimientos en el lenguaje principal.
 Compilador del Lenguaje de Definición de Datos DDL. Convierte sentencias
en DDL en un conjunto de tablas metadatos o “datos sobre datos”.
 Gestor del Diccionario de Datos. Almacena metadatos sobre la estructura
de la base de datos
 Componentes del Gestor de la Base de Datos
Los principales componentes del gestor de la base de datos son los
siguientes:
 Control de autorización . Este módulo comprueba que el usuario
tiene los permisos necesarios para llevar a cabo la operación que
solicita.
 Procesador de comandos . Una vez que el sistema ha comprobado
los permisos del usuario, se pasa el control al procesador de
comandos.
 Control de la integridad. Cuando una operación cambia los datos de
la base de datos, este módulo debe comprobar que la operación a
realizar satisface todas las restricciones de integridad necesarias.
Optimizador de consultas. Este módulo determina la estrategia
óptima para la ejecución de las consultas.

<!-- página 4 -->

Bases de Datos - Apuntes Hoja Nº 4
 Gestor de transacciones . Este módulo realiza el procesamiento de
las transacciones.
 Planificador (Schedule). Este módulo es el responsable de asegurar
que las operaciones que se realizan concurrentemente sobre la base
de datos tienen lugar sin conflictos.
 Gestor de recuperación. Este módulo garantiza que la base de datos
permanece en un estado consistente en caso de que se produzca
algún fallo.
 Gestor de buffers . Este módulo es el responsable de transferir los
datos entre memoria principal y los dispositivos de almacenamiento
secundario. A este módulo también se le denomina gestor de datos.
Clasificación de los Sistemas de Gestión de Base de Datos
Los sistemas de Gestión de Base de Datos se clasifican según:
 Modelo lógico en el que se basan:
Modelo Jerárquico.
Modelo de Red.
Modelo Relacional.
Modelo Orientado a Objetos.
 Número de usuarios
Mono usuario.
Multiusuario.
 Número de sitios
Centralizados.
Distribuidos.
 Ámbito de aplicación
Propósito General.
Propósito Específico

<!-- página 5 -->

Bases de Datos - Apuntes Hoja Nº 5
Qué aporta a un Sistema Integrado de Gestión un DBMS?
Los SMBD le permiten incorporar al SIG todas las características que describen los
diferentes elementos analizados permitiendo:
•Ingresar
•Recuperar
•Cambiar
•Comparar
•Administrar y
•Distribuir información.
Lenguajes e interfaces de los SGBD
 Los SGBD (Sistema de Gestión de Base de Datos) son un tipo de software muy
específico, dedicados a servir de interfaz entre la base de datos, el usuario y las
aplicaciones que lo utilizan. Se compone de lenguajes de definición, manipulación,
consulta y seguridad de datos.
 El propósito general de los SGBD es el de manejar de manera clara, sencilla y
ordenada un conjunto de datos.
 Existen diferentes objetivos que deben cumplir los SGBD, de los cuales se han
enumerado los siguientes:
 Hacer transparente al usuario los detalles del almacenamiento físico de los datos,
mediante varios niveles de abstracción de la Proveer al usuario la seguridad de que
sus datos no podrán ser accedidos, ni manipulados por quien no tenga permiso
para ello. Debido a esto, debe poseer un complejo sistema que maneje grupos,
usuarios y permisos para las diferentes actividades que se pueden realizar dentro
del mismo.
 Mantener la integridad de los datos.
 Proporcionar una manera eficiente de realizar copias de seguridad de la
información almacenada en ellos, y permitir a partir de estas copias restaurar los
datos.
 Controlar el acceso concurrente de los usuarios.
 Facilitar el manejo de grandes volúmenes de información.

<!-- página 6 -->

Bases de Datos - Apuntes Hoja Nº 6
Existen dos tipos de SGBD:
•SGBD Multidimensionales: estos aportan mucha performance al DW en cuanto a la
velocidad de respuesta, ya que los datos son almacenados en forma
multidimensional, sin embargo son difíciles de gestionar y de mantener.
•SGBD Relacionales: estos son cada vez más potentes y poseen una interfaz gráfica
más avanzada
Comunicación entre el usuario y el SGBD
Como los usuarios de un SGBD pueden tener distintos privilegios y distintos
conocimientos informáticos, es necesario disponer de diferentes lenguajes e
interfaces para cada tipo de usuarios. En esta sección vamos a ver los distintos
lenguajes e interfaces que emplean los SGBD.
Lenguaje de definición de datos
Una vez que se ha finalizado la tarea de diseño de la base de datos, y que se ha
seleccionado un SGBD para su implementación, el primer paso consiste en la
especificación del esquema conceptual de la base de datos.
El esquema conceptual de la base de datos se especifica mediante una serie de
definiciones expresadas en un Lenguaje de definición de datos (DDL, Data Definición
Lenguaje). El SGBD contará con un compilador de DDL cuya función será procesar las
sentencias en DDL para identificar las descripciones de los elementos de los esquemas y
guardar la descripción del esquema en el diccionario de datos.
El diccionario de datos es un archivo que contiene metadatos, es decir, datos acerca de
los datos. Este archivo se consulta cada vez que se leen o modifican los datos del Sistema
de base de datos.
Lenguaje de manipulación de datos
Una vez que se han compilado los esquemas de la base de datos, y que ya se han
introducido datos en la base de datos, los usuarios necesitarán algún mecanismo para
obtener información de la base de datos. Las operaciones más comunes de manipulación
son la consulta, inserción, eliminación y modificación de datos. Para ello, todos los SGBD
ofrecen un Lenguaje de manipulación de datos (DML , Data Manipulación Lenguaje).

<!-- página 7 -->

Bases de Datos - Apuntes Hoja Nº 7
En general existen dos tipos de DML:
•Procedimentales. Requieren que el usuario (normalmente será un programador)
especifique qué datos desea y cómo hay que obtenerlos. Esto quiere decir que hay
que especificar todas las operaciones de acceso a datos llamando a los
procedimientos necesarios para obtener la información requerida. Estos lenguajes
acceden a un registro, lo procesan y basándose en los resultados obtenidos,
acceden a otro registro, que también deben procesar. Así se va accediendo a
registros y se van procesando hasta que se obtienen los datos deseados. Las
sentencias de un LMD procedimental deben estar embebidas en un lenguaje de
alto nivel, ya que se necesitan sus estructuras (bucles, condicionales, etc.) para
obtener y procesar cada registro individual. A este lenguaje se le denomina
lenguaje anfitrión. Las bases de datos jerárquicas y de red utilizan LMD
procedimentales.
•No procedimentales . Un LMD no procedimental se puede utilizar de manera
independiente para especificar operaciones complejas sobre la base de datos de
forma concisa. En muchos SGBD se pueden introducir interactivamente
instrucciones del LMD desde un terminal o bien embeberlas en un lenguaje de
programación de alto nivel.
Lenguajes de cuarta generación
 No existe consenso sobre lo que es un lenguaje de cuarta generación ( 4GL ). Lo
que en un lenguaje de tercera generación ( 3GL ) como COBOL, FORTRAN, Pascal o
C requiere cientos de líneas de código, tan solo necesita de diez o veinte líneas en
un 4GL. Comparado con un 3GL, que es procedimental, un 4GL es un lenguaje no
procedimental: el usuario define qué se debe hacer, no cómo debe hacerse. Los
4GL se apoyan en
 unas herramientas de mucho más alto nivel denominadas herramientas de cuarta
generación. El usuario no debe definir los pasos a seguir en un programa para
realizar una determinada tarea, tan sólo debe definir una serie de parámetros que
estas herramientas utilizarán para generar un programa de aplicación. Se dice que
los 4GL pueden mejorar la productividad de los programadores en un factor de 10,
aunque se limita el tipo de problemas que pueden resolver.
Los lenguajes SQL y QBE son ejemplos de 4GL pero hay otros tipos de 4GL incluidos
habitualmente en los SGBD:

<!-- página 8 -->

Bases de Datos - Apuntes Hoja Nº 8
 Un generador de formularios es una herramienta interactiva que permite
crear rápidamente formularios de pantalla para introducir o visualizar
datos. Los generadores de formularios permiten que el usuario defina el
aspecto de la pantalla, qué información se debe visualizar y en qué lugar de
la pantalla debe visualizarse.
 Un generador de informes es una herramienta para crear informes a partir
de los datos almacenados en la base de datos. Se parece a un lenguaje de
consultas en que permite al usuario hacer preguntas sobre la base de datos
y obtener información de ella para un informe. Sin embargo, en el
generador de informes se tiene un mayor control sobre el aspecto de la
salida. Se puede dejar que el generador determine automáticamente el
aspecto de la salida o se puede diseñar ésta para que tenga el aspecto que
desee el usuario final.
 Un generador de gráficos es una herramienta para obtener datos de la
base de datos y visualizarlos en un gráfico mostrando tendencias y
relaciones entre datos. Normalmente se pueden diseñar distintos tipos
Interfaces para SGBD
 Normalmente, mientras que los programadores utilizan el DML para la creación de
consultas, los usuarios de un SGBD utilizan un lenguaje de consulta de alto nivel.
Para la mayoría de los usuarios se suelen definir interfaces de usuario amigables
para la interacción con la base de datos. A continuación vamos a ver los tipos de
interfaces que hay:
 Interfaces basadas en menús. Presentan al usuario una lista de opciones en forma
de menús que guían al usuario en la petición de consultas. De esta forma no es
necesario conocer la sintaxis de un lenguaje de consulta, pues permiten la creación
de la consulta eligiendo las opciones que presenta la interfaz.
 Interfaces basadas en formularios . Estas interfaces presentan un formulario al
usuario en el que se rellenan los huecos del formulario para la modificación de los
datos, o bien para especificar los parámetros de la consulta.
 Interfaces de lenguaje natural . Estas interfaces aceptan la especificación de una
consulta descrita en términos de un idioma concreto y construyen expresiones
DML a partir de dicha especificación.
 Interfaces gráficas . Suelen presentar al usuario los esquemas en forma de
diagrama, y las consultas se especifican
