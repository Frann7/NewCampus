# 04 - Teoria_Bases_de_Datos_cap._2

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/APUNTES DE LA MATERIA/04 - Teoria_Bases_de_Datos_cap._2.pdf` · 14 página(s) · texto extraído con pypdf.
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
| 9 |  |
| 10 |  |
| 11 |  |
| 12 |  |
| 13 |  |
| 14 |  |

<!-- página 1 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría   Capítulo 2 Pág. Nro. 1
Capítulo 2  -  Modelado Conceptual con MER
2.1.- El Diseño Conceptual en el Proceso de Desarrollo de Software.
Consideremos el Ciclo de Vida Clásico de un producto Software. Dentro del desarrollo, las primeras
etapas son las que cobran mayor importancia, ya que en ellas se debe centrar la mayor cantidad de
esfuerzo, para asegurar una mayor calidad del producto.
Figura 2.1.- Ciclo de Vida Clásico
Dentro de estas etapas, se encuentra el diseño. El diseño como actividad se puede entender en distintos
niveles de abstracción, separándolo en diseño conceptual, diseño lógico y diseño físico.
El diseño conceptual es de un alto nivel de abstracción, y puede confundirse su inicio con el término de la
etapa de análisis, ya que permite visualizar de mejor manera un problema. Además este diseño no está
necesariamente asociado a priori con una plataforma de implementación, sino que más cercano a la
realidad, al problema a solucionar.
El diseño lógico se acerca más a la implementación del producto en una plataforma computacional,
integrando consideraciones para la plataforma específica en cuestión.
Finalmente el diseño físico es una especificación tal que representa exactamente la implementación del
producto.

<!-- página 2 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría   Capítulo 2 Pág. Nro. 2
2.2.- El Diseño de Bases de Datos.
En el siguiente diagrama se puede apreciar el proceso de diseño de bases de datos. Los requisitos de
datos constituyen un componente de los requisitos de un producto y son una entrada al diseño
conceptual.
Figura 2.2.- Proceso de Diseño de Bases de Datos

<!-- página 3 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría   Capítulo 2 Pág. Nro. 3
2.2.1.- Diseño Conceptual.
Recibe como entrada la especificación de requerimientos y su resultado es el esquema conceptual de la
base de datos, que es una descripción de alto nivel de la estructura de la base de datos, independiente
del software que se use para manipularla.
Modelos Conceptuales: MER, Modelos OO, Formalismo Individual.
2.2.2.- Diseño Lógico.
Recibe como entrada el esquema conceptual y da como resultado un esquema lógico, que es una
descripción de la estructura de la base de datos que puede procesar el software DBMS.
Modelos Lógicos: Relacional, de Redes, Jerárquico.
2.2.3.- Diseño Físico.
Recibe como entrada el esquema lógico y da como resultado un esquema físico, que es una descripción
de la implementación de una base de datos en la memoria secundaria, describe las estructuras de
almacenamiento y los métodos usados para tener un acceso efectivo a los datos.
Modelos Físicos: Modelo Unificador, Memoria de Elementos.
2.3.- Modelo de Datos.
Dentro de la problemática del diseño de bases de datos, los modelos de datos cumplen un importante rol,
pues son las herramientas que nos permiten generar los esquemas de bases de datos, los que regirán su
estructura.
Un modelo de datos define las reglas por las cuales los datos son estructurados. Esta estructuración, sin
embargo, no da una interpretación completa acerca del significado de los datos y de la forma en que
serán usados. Las operaciones permitidas sobre datos deben ser definidas. Muchos modelos
conceptuales, como el MER, no incluían operaciones en sus definiciones preliminares, por lo que fueron
propuestas en estudios posteriores.
Se define el modelo de datos M consistente de dos partes:
G: un conjunto de reglas generadoras de esquemas.
O: un conjunto de operaciones.
El conjunto de reglas G expresa las propiedades estáticas de un modelo de datos y corresponden a lo
que se denomina generalmente Data Definition Language (DDL). Este define las estructuras permitidas
para el modelo de datos M, es decir, generan esquemas.
El conjunto G se puede dividir en dos:
o Gs: reglas generadoras de las estructuras permitidas.
o Gc: reglas generadoras de las restricciones del modelo.
Así, Gs genera las categorías y estructuras para un modelo, y Gc las restricciones.
Utilizando esta última notación, un esquema S consiste de dos partes: una estructura Ss y restricciones
Sc, donde Sc es una lista explícita de restricciones que deben ser satisfechas en todo momento.

<!-- página 4 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría   Capítulo 2 Pág. Nro. 4
Un modelo de datos también puede tener restricciones que son inherentes a él, las que generalmente se
incorporan en Ss (la estructura).
Las reglas de generación G son generadoras de un conjunto de esquemas S, en el que cada uno de ellos
define estructuras y restricciones particulares para los datos. Hay muchas bases de datos D en términos
de la ocurrencia del esquema S, pero todos tienen la misma estructura genérica y obedecen a las
mismas restricciones definidas en S.
 En resumen:
Figura 2.3.- Modelo de Datos
Las propiedades dinámicas de un modelo de datos son expresadas por un conjunto de operaciones O,
las que generalmente son llamadas Data Manipulation Language (DML). Estas propiedades definen las
acciones permitidas para una base de datos, tal que transforme la ocurrencia Di en la ocurrencia Dj.

<!-- página 5 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría   Capítulo 2 Pág. Nro. 5
2.4.- El Modelo Entidad Relación.
A continuación se definen los elementos del modelo entidad relación y sus extensiones más usadas.
Además se incluye su representación gráfica.
2.4.1.- Dominio.
Conjunto de valores de un mismo tipo.
Ejemplo: nombres de personas, DNI válidos, estados civiles.
2.4.2.- Atributo.
Elemento de un Dominio. Aporta mediante su rótulo, la semántica de los valores del Dominio al que está
asociado.
Ejemplo: DNI, nombre, departamento, edad, tipo proyecto.
2.4.3.- Atributo Compuesto.
Corresponde a grupos de atributos que tienen afinidad en cuanto a su significado o a su uso .
Ejemplo: Dirección = calle + número + ciudad

<!-- página 6 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría                        Capítulo 2 Pág. Nro. 6
2.4.4.- Tipo de Entidad.
Los Tipos de Entidad representan clases de objetos de la realidad. Además se componen de atributos,
los cuales representan las características de un tipo de entidad.

Ejemplo: Persona, Proceso, Factura, Guía de Despacho, Cliente, Producto.
2.4.5.- Identificador de un tipo de entidad.
Un atributo I, posiblemente compuesto, de un tipo de entidad TE, es un Identificador de TE si y sólo si
satisface las siguientes 2 propiedades independientes del tiempo.
a. Unicidad. En cualquier momento dado, no existen dos elementos en TE con el mismo valor de
I.
b. Minimalidad. Si I es compuesto, no será posible eliminar ningún atributo componente de I sin
destruir la propiedad de unicidad.

Ejemplo: para un tipo de entidad Persona, el identificador puede ser DNI.
2.4.6.- Tipo de Interrelación.
Los Tipos de interrelación representan agregaciones de dos o más entidades (interrelaciones binarias o
n-arias) no necesariamente diferentes. El Identificador de un Tipo de Interrelación, se forma a partir de los
identificadores de los tipos de entidad que relaciona.

Ejemplo: Tipo de Entidad 1 es Empleado, Tipo de Entidad 2 es Departamento, Tipo de Interrelación es
Trabaja para.

<!-- página 7 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría                        Capítulo 2 Pág. Nro. 7
2.5.- Modelo Entidad Relación: Extensiones
2.5.1.- Cardinalidad de Asignación.
Caracteriza a los atributos de un tipo de entidad y a los tipos de interrelación.
Las definición aquí utilizada corresponde a la realizada por Tardieu.
Cardinalidad de atributo con respecto a un tipo de entidad.
Para los atributos, la cardinalidad mínima indica el número mínimo de valores de un atributo asociado
con cada caso (ocurrencia) de una entidad o interrelación. La cardinalidad máxima indica el número
máximo de valores para un atributo asociado a cada caso de una entidad o interrelación.
Se define la Cardinalidad del Atributo A con respecto al tipo de entidad TE como:
Card(A,TE)=( mínimo, máximo), con mínimo, máximo  {0,...,n} y mínimo    máximo.
donde un elemento de A debe part icipar al menos mínimo veces, y a lo más máximo veces en cada
ocurrencia de TE.

Ejemplo: el atributo teléfono del tipo de entidad Persona puede tener cardinalidad (0,3)
2.5.1.1.- Cardinalidad de tipo de entidad con respecto a un tipo de interrelación.
Para los tipos de interrelación la cardinalidad máxima (mínima) establece el menor (mayor) número de
correspondencias en cada una de los tipos de entidad involucradas en la interrelación.
Se define la Cardinalidad del Tipo de Entidad TE con respecto al tipo de interrelación R como:
Card(TE,R) = (mínimo, máximo), con mínimo, máximo  {0,...,n} y mínimo  máximo.
donde toda ocurrencia de TE debe participar al menos mínimo veces, y a lo más máximo veces en R.

Ejemplo: Cada entidad de Provincia participa en la relación Pertenece exactamente una  vez, mientras
que cada entidad de Región participa en la relación Pertenece a lo menos una vez. Esto es, cada a cada
región pertenecen a lo menos una provincia, mientras que toda provincia debe pertenecer a sólo una
región.

<!-- página 8 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría                        Capítulo 2 Pág. Nro. 8
 2.5.2.- Identificador de un tipo de entidad.
Sea TE un tipo de entidad, sean A1, A2..., An atributos monovalentes obligatorios de TE, sean TE1,
TE2..., TEm otros tipos de ent idad vinculados a TE por R1, R2..., Rm, tipos de interrelación (binarias)
obligatorias. Considérese un posible identificador
I = {a1, a2..., an, TE1, TE2..., TEm}, n = 0, m = 0, n + m = 1.
El valor del identificador para un caso particular te del tipo de entidad TE se define como el conjunto de
todos los valores de los atributos ai (i = 1,2, ..., n) y todos los casos de los tipos de entidad TEj (j = 1,2, ...,
m) vinculadas con te.
Cada entidad puede tener múltiples identificadores alternativos.
Ejemplo: En una biblioteca, se tiene para cada libro uno o más ejemplares. Cada libro tiene un código
único, mientras que para diferenciar a un ejemplar de otro, se le agrega un correlativo. Para esta
situación, se puede tener un esquema como el siguiente, donde e l tipo de entidad Libro tiene como
atributos código, título y año edición, mientras que Ejemplar tiene como atributos número de ejemplar y
ubicación.

2.5.2.1.- Clasificación de los tipos de entidad según sus identificadores.
o Tipo de Entidad Fuerte: Tipo de entidad con identificador interno. Por ejemplo el tipo de entidad
Libro.
o Tipo de Entidad Débil: Tipo de entidad con identificador externo o mix to. Por ejemplo el tipo de
entidad Ejemplar.
2.5.3.- Estructura de Generalización.
Un tipo de entidad TE (tipo de entidad genérica) es una generalización de un grupo de tipos de entidades
STE1 , STE2 , ..., STEn (tipos de entidad subconjunto) si cada ent idad de los tipos de entidad STE1 ,
STE2 , ..., STEn es también una entidad del tipo de entidad TE. (Lo opuesto a la generalización se
denomina especialización.)
Además cada atributo, interrelación o generalización definida para un tipo de entidad genéric a, será
heredado por todas las entidades subconjunto de la generalización.

<!-- página 9 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría                        Capítulo 2 Pág. Nro. 9
Ejemplo: el Tipo de entidad Persona es una generalización de cliente y empleado, en un Banco.

2.5.3.1.-Cobertura.
Las jerarquías de generalización presentan la propiedad de cobertura. La cobertura puede ser parcial  o
total y exclusiva o superpuesta. La cobertura parcial o total permite especificar una restricción entre el
tipo de entidad genérica y sus tipos de entidad subconjunto, donde todos los elementos del tipo de
entidad genérico deben pertenecer a alguno de s us tipos de entidad subconjunto (si es total), o no (si es
parcial). La cobertura exclusiva o superpuesta permite especificar una restricción entre los tipos de
entidad subconjunto, donde los elementos que pertenecen a un tipo de entidad subconjunto pueden
pertenecer también a otro tipo de entidad subconjunto (si es superpuesto) o no (si es exclusiva).

Ejemplo:
Consideremos el caso de un banco cua lquiera y una política respecto a las personas a considerar, y su
calidad de empleados y clientes.
Caso cobertura total y exclusiva: Todas las personas son empleados o clientes del banco, pero no ambas
cosas simultáneamente. En este caso hablamos de cober tura total (todas las personas están clasificadas
como empleados o clientes) y exclusiva (sí una persona se clasifica como empleado, no puede
clasificarse como cliente y al contrario ocurre lo mismo).

<!-- página 10 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría   Capítulo 2 Pág. Nro. 10
Caso cobertura total y superpuesta : Todas las personas son empleados o clientes del banco,
permitiéndose que un empleado sea a su vez cliente. En este caso hablamos de cobertura total (todas
las personas están clasificadas como empleados o clientes) y superpuesta (no existe restricción con
respecto a la exclusividad).
Caso cobertura parcial y exclusiva : Hay personas, algunas de las cuales son empleados o clientes del
banco, pero no ambas cosas simultáneamente. En este caso hablamos de cobertura parcial (no todas las
personas están clasificadas como empleados o clientes) y exclusiva (sí una persona se clasifica como
empleado, no puede clasificarse como cliente y al contrario ocurre lo mismo).
Caso cobertura parcial y superpuesta : Algunas personas son empleados o clientes del banco, pudiendo
ser ambas cosas. En este caso hablamos de cobertura parcial (no todas las personas están clasificadas
como empleados o clientes) y sobrepuesta (si una persona se clasifica como empleado también puede
clasificarse como cliente).

<!-- página 11 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría   Capítulo 2 Pág. Nro. 11
2.5.4.- Agregación de Tipos de Entidad.
Un tipo de interrelación y los tipos de entidad que relaciona, puede ser manejado como un tipo de entidad
en un nivel de abstracción mayor, lo que posibilita que se pueda interrelacionar con otros tipos de
entidad. Este mecanismo es conocido como Estructura de Agregación o Agregación de Tipos de Entidad,
en aquellas extensiones del MER que la incorporan.
Ejemplo: En una organización se manejan pedidos, los que incluyen productos solicitados por clientes.
Cada pedido debe ser asignado a un empleado.
2.5.5.- Roles de Tipos de Entidad en Tipos de Interrelación.
Un Rol de un Tipo de Entidad en un Tipo de Interrelación es la función que aquel cumple dentro de ésta.
La definición de roles permite atribuirle a un tipo de entidad su semántica dentro de la agregación,
aportándole mayor expresividad al esquema y permitiendo disminuir ambigüedades en la definición de
cardinalidades (esto cobra mayor importancia en aquellos tipos de interrelación que involucran a un
mismo tipo de entidad más de una vez).

<!-- página 12 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría   Capítulo 2 Pág. Nro. 12
Ejemplo:
2.5.6.- Tipos de Interrelaciones Exclusivas con respecto a un Tipo de Entidad.
Sea TE un tipo de entidad y sea un conjunto de tipos de interrelación RE= {R1,...,Rn} tales que TE  Ri, i
en {1,...,n}, RE se dice exclusivo con respecto a TE, si cada ocurrencia de TE sólo puede estar presente
a lo más en un Ri, i en {1,...,n}.
Observación: En este caso la cardinalidad mínima de TE con respecto a Ri, con i en {1,...,n} debe ser 0.
Ejemplo: Consideremos el caso de una organización donde se desarrollan proyectos, los cuales pueden
ser asignados a empleados de la organización, o a una empresa contratista, pero no a ambos.
2.6.- Restricciones en MER extendido.
Las restricciones estáticas especifican los estados posibles de la base de datos modelada en un
esquema dado. En un esquema MER la principal restricción estática está dada por la estructura
(pertenencia de un atributo a un tipo de entidad o interrelación, tipos de entidad que relaciona un tipo de
interrelación), y también se pueden especificar las siguientes.
o Dominio.
o Cardinalidad de atributo con respecto a un tipo de entidad.
o Cardinalidad de un tipo de entidad con respecto a un tipo de interrelación.
o Identificadores.
o Cobertura.
o Tipos de Interrelación Exclusivas con respecto a un Tipo de Entidad.

<!-- página 13 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría   Capítulo 2 Pág. Nro. 13
2.7.- Estrategia para modelar con MER.
Se debe hacer uso de los conceptos de abstracción básicos: clasificación, agregación y generalización.
Para ello se pueden seguir los procesos siguientes.
1. Identificar Tipos de Entidad y las relaciones que existen entre ellos.
2. Descomponer un tipo de entidad en dos o más tipos de entidad, relacionados o no, o participando
en una estructura de generalización.
3. Descomponer un tipo de interrelación en varias.
4. Identificar atributos para cada elemento.
5. Definir identificadores para los tipos de entidad.
6. Definir restricciones de cardinalidad y cobertura.
7. Verificar que el esquema resultante es correcto con respecto a la especificación (representa toda la
realidad descrita).
8. Verificar que el esquema es correcto con respecto al buen uso del modelo.
9. Analizar modificaciones al esquema.
2.8.- Ejemplo.
Consideremos el caso de un campeonato juvenil (menores de 25 años) de fútbol. Existen distintos
aspectos a considerar para este caso.
o Hay equipos de a lo menos 11 jugadores.
o Cada jugador puede participar en un equipo solamente.
o En cada partido juegan dos equipos.
o En cada partido participan 3 colegiados: un arbitro, un arbitro de banda derecha y un arbitro de
banda izquierda.
o Cada jugador tiene asignadas posiciones en las que puede jugar en un partido.
o Cada jugador de un equipo participa en un partido en una posición, que debe ser alguna para las
cuales está preparado.
o No necesariamente todas las posiciones deben ser ocupadas en un partido (puede haber más de
once posiciones).
 2.8.1.- Esquema MER.
Sea el siguiente esquema MER una posible representación de la realidad descrita:

<!-- página 14 -->

Bases de Datos  -  Modelado Conceptual con MER
Bases de Datos – Apuntes de Teoría   Capítulo 2 Pág. Nro. 14
Los nombres de los tipos de interrelación han sido abreviados para mayor legibilidad del esquema. A
continuación se detalla su significado.
L: Local V: Visita P: Pertenece
J: Juega O: Ocupa H: habilitado para
I: Arbitro Banda Izquierda D: Arbitro Banda Derecha A: Arbitro.
Se definen los atributos de los tipos de entidad a continuación.
Tipo de Entidad Atributo Dominio
Equipo nombre equipo Nombres de equipos de fútbol
Jugador dni
nombre
fecha de nacimiento
números documentos válidos
Nombres de Persona
Fechas posteriores a 1971
Partido fecha
hora
Fechas del año 1996
Horas entre las 10:00 y las 21:30
Colegiado dni
nombre
números documentos válidos
Nombres de Persona
Posición número
función
enteros mayores que cero
Funciones de Jugadores
JuegaPartido
(es Agregación )
Jugador
Partido
Jugador
Partido
Las restricciones que no se han definido explícitamente en el esquema ni en la documentación posterior,
se presentan a continuación:
a. Un equipo no puede participar en un mismo partido como visita y local a la vez.
b. Un jugador sólo puede jugar en un partido ocupando una posición en la que está habilitado.
c. Un jugador sólo puede jugar en un partido si su equipo participa en él como local o visita.
d. De los jugadores que participan en un partido, a lo menos 11 pertenecen al equipo local y 11 al
equipo visitante.
e. En un mismo partido, deben estar asignados colegiados distintos para cada rol.
