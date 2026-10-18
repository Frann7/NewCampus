# Guia Practica 2

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/BD/PRACTICA/Guia Practica 2.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |

<!-- página 1 -->

Guía de Práctica N° 2  Bases de Datos - Facultad de Ciencia y Tecnología

1

Ejercicio 1:
Se necesita un sistema para llevar el control de proveedores, clientes, productos y ventas.
Un proveedor tiene CUIT, nombre, dirección, teléfono y página web. Un cliente también
tiene CUIT, nombre, dirección, pero puede tener varios teléfonos. La dirección de
entiende por calle, número, localidad y provincia.
Un producto tiene identificador único, nombre y descripción, y se sabe quién es el
proveedor del mismo.
Por razones de contabilidad, se debe registrar la información de cada venta con un id,
fecha, cliente, descuento y monto total. Además se debe guardar el precio al momento de
la venta, la cantidad vendida y el monto total por cada producto de la venta.

Ejercicio 2:
Una empresa cuenta con varias fábricas para la elaboración de productos alimenticios. Se
necesita diseñar una base de datos para contener la información sobre las fábricas, los
productos,  los clientes y los pedidos que realizan. Actualmente cuentan con los siguientes
datos registrados en distintos documentos:
Por cada cliente: Número de cliente (único), dirección de envío, saldo, límite de crédito
(puede ser distinto para cada cliente, pero en ningún caso debe superar los $50.000
pesos) y un descuento (puede variar de acuerdo al volumen de compras que realiza y si es
buen pagador o no).
De los productos se conoce: Número de artículo (único), descripción del artículo, fábricas
que los distribuyen y la existencia de ese artículo en cada fábrica.
Para cada pedido: Número de pedido, número de cliente, fecha del pedido, fecha de
entrega, y en el detalle, se indica número de artículo y cantidad por cada línea que
conforma el pedido.
Además se ha determinado que se debe almacenar la información de las fábricas: Número
de fábrica (único), nombre, teléfono de contacto, dirección y localidad. Es imprescindible
conocer que artículos provee cada fábrica.
Realice un Diagrama ER para una base de datos que represente dicha información.

<!-- página 2 -->

Guía de Práctica N° 2  Bases de Datos - Facultad de Ciencia y Tecnología

2

Ejercicio 3:
Diseñar un diagrama ER representativo del siguiente problema referido a información
sobre todas las rutas del país, sabiendo que se deben cumplir las siguientes
especificaciones:
Las rutas se clasifican en distintas categorías (Autopistas, autovías, ruta nacional, ruta
provincial, etc.).
Las rutas se dividen en tramos. Un tramo siempre pertenece a una única ruta y una ruta
está compuesta por varios tramos. En el tramo se indica el km de la ruta donde comienza.
Un tramo puede pasar por varias localidades, interesando conocer el Km de la ruta en la
que se encuentra. De las localidades se conoce su nombre y un código único.
Para los tramos que suponen principio o final de ruta, interesa saber si es que la ruta
concluye físicamente o es que confluye en otra ruta. En este caso, interesa conocer con
qué ruta confluye y en qué tramo.

Ejercicio 4:
Obtener el diagrama ER para un sistema de control de vuelos adaptado a las siguientes
reglas de gestión:
De cada aeropuerto se conoce su código, nombre, ciudad y país.
En cada aeropuerto pueden aterrizar diversos modelos de aviones (el modelo de un avión
determina su capacidad, es decir, el número de plazas).
En cada aeropuerto existe una colección de programas de vuelo. En cada programa de
vuelo se indica el número de vuelo, línea aérea, y día de la semana que vuela. Los
números de vuelo son únicos para todo el mundo.
Cada programa de vuelo despega de un aeropuerto y aterriza en otro.
Cada vuelo realizado pertenece a un cierto programa de vuelo. Para cada vuelo se quiere
conocer su fecha, plazas vacías y el modelo de avión utilizado.
Cada programa de vuelo puede tener además escalas técnicas en distintos aeropuertos,
siendo de interés conocer el orden en que se van dando dichas escalas.
