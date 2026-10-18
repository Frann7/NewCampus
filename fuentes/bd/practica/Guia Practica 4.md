# Guia Practica 4

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/PRACTICA/Guia Practica 4.pdf` · 1 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |

<!-- página 1 -->

Guía de Práctica N° 4 Bases de Datos - Facultad de Ciencia y Tecnología
1
Normalizar los siguientes conjuntos de datos
Ejercicio1: una base de datos de una biblioteca que incluye las siguientes tablas:
Libros (ID Libro, Título, ID Autor, Año Publicación, ID Editor, Género)
Autores (ID Autor, Nombre, Nacionalidad)
Editorial (ID Editorial, Nombre, Dirección)
Prestamos (ID Préstamo, ID Libro, ID Miembro, Nombre, Dirección, Teléfono, Fecha Préstamo, Fecha
Devolución)
Reserva (ID Reserva, ID Libro, ID Miembro, Nombre, Dirección, Teléfono, Fecha Reserva)
Multas (ID Multa, ID Préstamo, Monto, Fecha)
Comentarios (ID Comentario, ID Libro, Nombre Autor, ID Miembro, Nombre Miembro, Comentario,
Fecha)
Ejercicio 2:
Equipos (ID Equipo, Nombre, Ciudad, Fecha inscripción)
Jugadores (ID Jugador, Nombre, Apellido, Edad, ID Equipo, Nombre Equipo, Nacionalidad)
Partidos (ID Partido, Equipo Local, Equipo Visitante, Fecha, Nombre Estadio, Capacidad)
Partido_Arbitros (ID Partido, ID Árbitro, Nombre, Apellido, Nacionalidad)
Goles (ID Gol, ID Partido, ID Jugador, Nombre Jugador, Minuto)
Tarjetas (ID Tarjeta, ID Partido, Fecha, ID Jugador, Tipo, Minuto)
Ejercicio 3:
Empleados (ID Empleado, Nombre, Apellido, Fecha de Nacimiento, Dirección, Teléfonos, ID
Departamento, Nombre Departamento, ID Categoría, Nombre)
Departamento (ID Departamento, Nombre, Descripción)
Categorías (ID Categoría, Nombre, Descripción, Básico)
Conceptos (ID Concepto, Descripción, Monto)
Licencias (ID Licencia, ID Empleado, Nombre, Apellido, Fecha, Motivo)
Sueldos (ID Sueldo, ID Empleado, Fecha de Pago, Importe Bruto, Importe Descuentos, Importe Neto, ID
Concepto, Monto)
Ejercicio 4:
Guía (ID Guía, Número, Fecha, Empresa Origen, Nombre, Dirección, ID Ciudad, Empresa destino,
Nombre, Dirección, ID Ciudad, Paquetes)
Ciudad (ID Ciudad, Nombre)
Distancias (ID Ciudad Origen, ID Ciudad Destino, Kilómetros)
Paquetes (ID Paquete, Descripción, Tipo, Valor Flete)
Repartidor (ID Repartidor, Nombre, Apellido, ID Paquete entregado)
