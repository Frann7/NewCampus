# 02-DER_Extendido

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/PRACTICA/02-DER_Extendido.pdf` · 9 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Diagrama Entidad Relación
Extendido

<!-- página 2 -->

Atributo multivaluado: Es un atributo que puede almacenar más de un valor.
Por ej. una persona puede tiene muchos teléfonos
DNI
Nombre
Apellido
Teléfonos
Persona
Atributo compuesto: Es un atributo que agrupa puede almacenar más de un valor.
Por ej. La dirección de una persona puede estar compuesta por calle, nro, dpto
DNI
Nombre
Apellido
Dirección
Persona Calle
Número
Dpto.

<!-- página 3 -->

Entidad débil
Ejemplar
Número
ISBN
Título
Autor
 Libro Pertenece
(1,n) (1,1)

<!-- página 4 -->

Profesor
DNI
Nombre
Fecha ingreso
DNI
Nombre
Fecha inscripción
 Alumno
DictaCursa
Materia
Código
Nombre
(1,n)
(1,n)
(1,n)
(1,n)

<!-- página 5 -->

Profesor
Fecha ingreso
Fecha inscripción
 Alumno
Dicta
Cursa
Materia
Código
Nombre
(1,n)
(1,n)
(1,n)
(1,n)
Persona
DNI
Nombre
(T,S)
Generalización

<!-- página 6 -->

Generalización: Tipos de cobertura
        ( T ,    )
Total
o
Parcial

<!-- página 7 -->

Generalización: Tipos de cobertura
        ( T , E )
Total
o
Parcial
Exclusiva
o
Superpuesta

<!-- página 8 -->

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
Conoce(1,n) (1,n)
LenguajeProgramador
Examen

<!-- página 9 -->

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
Agregación
