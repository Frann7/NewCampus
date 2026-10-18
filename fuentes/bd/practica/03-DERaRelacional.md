# 03-DERaRelacional

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/PRACTICA/03-DERaRelacional.pdf` · 18 página(s) · texto extraído con pypdf.
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
| 15 |  |
| 16 |  |
| 17 |  |
| 18 |  |

<!-- página 1 -->

DER a Modelo Relacional

<!-- página 2 -->

El Modelo Relacional fue propuesto por E. F. Codd en el año 1970.
Basado en la lógica de predicados y en la teoría de conjuntos.
Modelo Relacional
campo1 campo2 campo3 campo4 ...

} Tupla
Relación     {

<!-- página 3 -->

Entidades: Cada entidad pasa a ser una relación o tabla.
Atributos: Cada atributo es un campo o columna.
Ej. la entidad Persona...
DNI
Nombre
Apellido
Persona
DNI Nombre Apellido
... ... ...

Persona
Persona (DNI, Nombre, Apellido)

<!-- página 4 -->

Atributos compuestos: Cada uno de los atributos componentes, pasan a ser un atributo
Por ej. dirección, compuesto por calle, nro, piso, dpto
... Calle Nro Piso Dpto

Persona (DNI, Nombre, Apellido, Calle, Nro, Piso, Dpto)
DNI
Nombre
Apellido
Dirección
Persona Calle
Número
Dpto.

<!-- página 5 -->

Atributos multivaluados: En este caso la correspondencia es una nueva relación o tabla.
Por ej. una persona puede tiene muchos teléfonos
DNI
Nombre
Apellido
Teléfonos
Persona
DNI Numero
... ...

Persona_telefonos
DNI Nombre Apellido
... ... ...

Persona
Persona (DNI, Nombre, Apellido)
Persona_telefonos (DNI, Numero)

<!-- página 6 -->

Interralación: Puede tener distintas correspondencias dependiendo de la cardinalidad
Empleado DepartamentoDirige
(0,1) (1,1)
Codigo Nombre
...

Departamento
DNI Nombre Apellido
... ... ...

Empleado
Empleado(DNI, Nombre, Apellido)
Departamento (Codigo, Nombre)
DNI
Nombre
Apellido
Codigo
Nombre

<!-- página 7 -->

Interralación: Puede tener distintas correspondencias dependiendo de la cardinalidad
Empleado DepartamentoDirige
(0,1) (1,1)
Codigo Nombre DNI_dirige
... ...

Departamento
DNI Nombre Apellido
... ... ...

Empleado
Empleado(DNI, Nombre, Apellido)
Departamento (Codigo, Nombre, DNI_dirige)
DNI
Nombre
Apellido
Codigo
Nombre

<!-- página 8 -->

Interralación: Puede tener distintas correspondencias dependiendo de la cardinalidad
Empleado DepartamentoTrabaja
en
(1,1) (1,n)
Codigo Nombre
...

Departamento
DNI Nombre Apellido
... ... ...

Empleado
Empleado(DNI, Nombre, Apellido)
Departamento (Codigo, Nombre)
DNI
Nombre
Apellido
Codigo
Nombre

<!-- página 9 -->

Interralación: Puede tener distintas correspondencias dependiendo de la cardinalidad
Empleado DepartamentoTrabaja
en
(1,1) (1,n)
Codigo Nombre
...

Departamento
DNI Nombre Apellido Codigo_dpto
... ... ...

Empleado
Empleado(DNI, Nombre, Apellido, Codigo_dpto)
Departamento (Codigo, Nombre)
DNI
Nombre
Apellido
Codigo
Nombre

<!-- página 10 -->

Interralación: Puede tener distintas correspondencias dependiendo de la cardinalidad
Empleado ProyectoTrabaja
en
(1,n) (1,n)
Codigo Nombre
...

Proyecto
DNI Nombre Apellido
... ... ...

Empleado
Empleado(DNI, Nombre, Apellido)
Proyecto (Codigo, Nombre)
DNI
Nombre
Apellido
Codigo
Nombre

<!-- página 11 -->

Interralación: Puede tener distintas correspondencias dependiendo de la cardinalidad
Empleado ProyectoTrabaja
en
(1,n) (1,n)
Codigo Nombre
...

Proyecto
DNI Nombre Apellido
... ... ...

Empleado
Empleado(DNI, Nombre, Apellido)
Proyecto (Codigo, Nombre)
Empleado_Proyecto (DNI, Codigo_p)
DNI Codigo_p
...

Empleado_Proyecto
DNI
Nombre
Apellido
Codigo
Nombre

<!-- página 12 -->

Atributo en una interralación:
Empleado ProyectoTrabaja
en
(1,n) (1,n)
Codigo Nombre
...

Proyecto
DNI Nombre Apellido
... ... ...

Empleado
Empleado(DNI, Nombre, Apellido)
Proyecto (Codigo, Nombre)
Empleado_Proyecto (DNI, Codigo_p, Horas)
DNI Codigo_p Horas
...

Empleado_Proyecto
horas
DNI
Nombre
Apellido
Codigo
Nombre

<!-- página 13 -->

Entidad Débil: Al igual que cualquier otra entidad, se corresponde con una nueva tabla pero teniendo
en cuenta que parte de su clave es la clave de la entidad fuerte.
Ejemplar
Número
ISBN
Título
Autor
 Libro Pertenece
(1,n) (1,1)
ISBN Numero
...

Ejemplar
Libro(ISBN, Titulo, Autor)
Ejemplar (ISBN, Numero)
ISBN Titulo Autor
...

Empleado_Proyecto

<!-- página 14 -->

Generalización: Puede tener distintas correspondencias dependiendo de la cobertura:
Cliente
Límite créditoSueldo
Empleado
Persona
DNI
Nombre
Calle
(t,e)
Persona (DNI, nombre, calle, sueldo, limite_credito, tipo)
Limitado a cobertura exclusiva. Puede ser total o parcial.
Hay atributos que no se usan.

<!-- página 15 -->

Generalización: Puede tener distintas correspondencias dependiendo de la cobertura:
Cliente
Límite créditoSueldo
Empleado
Persona
DNI
Nombre
Calle
(t,s)
Persona (DNI, nombre, calle, sueldo, limite_credito, es_cliente, es_empleado)
Puede ser total o parcial y superpuesta o exclusiva.
Hay más atributos que no se usan.

<!-- página 16 -->

Generalización: Puede tener distintas correspondencias dependiendo de la cobertura:
Cliente
Límite créditoSueldo
Empleado
Persona
DNI
Nombre
Calle
(t,e)
Empleado (DNI, nombre, calle, sueldo)
Cliente (DNI, nombre, calle, limite_credito)
En caso de cobertura superpuesta hay redundancia de datos, lo que puede traer inconsistencias.
En casa de cobertura parcial, no tengo donde almacenar una persona que no sea cliente ni
empleado.

<!-- página 17 -->

Generalización: Puede tener distintas correspondencias dependiendo de la cobertura:
Cliente
Límite créditoSueldo
Empleado
Persona
DNI
Nombre
Calle
(t,s)
Persona (DNI, nombre, calle)
Empleado (DNI, sueldo)
Cliente (DNI, limite_credito)
RECOMENDADA

<!-- página 18 -->

Agregación: Se plantea una relación o tabla entre todas las entidades que intervienen:
Código
Nombre
Tipo
DNI
Nombre
Apellido
Teléfono
Código
Cant. ejercicios
Dificultad
Fecha creación
Contenido
Conoce(1,n)
(1,n)
Calificación
    Fecha
(1,n)
Lenguaje
Evaluación
              (1,1)
Programador
Evalúa
Examen
Programador (DNI, Nombre, Apellido)
Lenguaje (Codigo, Nombre, Tipo)
Examen (Codigo, CantEj, Dif, Fec, Contenido)
Evaluacion (DNI, codLeng, CodExa, Calif, Fecha)
