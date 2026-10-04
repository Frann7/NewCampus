# Clase-4-Presentacion

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 4/TEORIA/Clase-4-Presentacion.pdf` · 18 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Portada: ¿Cómo el navegador representa una página web? |
| 2 | El navegador pide el índice y los recursos (link, img, script) antes de renderizar |
| 3 | Los cinco pasos del renderizado (lista) |
| 4 | Construcción del DOM: nodos (Node) en forma de árbol |
| 5 | Construcción del CSSOM y del árbol de renderizado |
| 6 | Fase de diseño (reflujo) y fase de pintura |
| 7 | ⚠ ver el PDF: diagrama HTML parser → DOM, CSS parser → CSSOM → Style → Render Tree → Layout → Painting → Display (sin texto) |
| 8 | Portada «Algo de JavaScript» (solo título y logo; no hace falta el PDF) |
| 9 | DOM: qué es y por qué actualizarlo es costoso |
| 10 | ⚠ ver el PDF: árbol DOM de ejemplo (html → head: title, meta, meta; body: h1, p → a, ul → li ×3) (sin texto) |
| 11 | getElementById y .value (comillas tipográficas en el código) |
| 12 | getElementsByTagName, Array.from y forEach; ⚠ en el PDF el id repetido "nombre" está subrayado |
| 13 | Clases en JS: constructor, init y DOMContentLoaded (esquema FormPersonas) |
| 14 | Portada «Apis Rest» (solo título y logo; no hace falta el PDF) |
| 15 | API REST: definición y características (cliente-servidor, sin estado, formato liviano) |
| 16 | JSON: definición y ejemplo |
| 17 | fetch con then/catch y propiedades del objeto Response |
| 18 | APIs REST gratuitas para practicar (jsonplaceholder, pokeapi, freepublicapis, georef) |

<!-- página 1 -->

¿Cómo el navegador representa
una página web?

<!-- página 2 -->

¿Cómo el navegador representa una página web?
Para acceder a un sitio web el navegador solicita su archivo indice (index.html, index.php, etc) que
contiene el código HTML de la página.
Este código podrá tener referencias que indicarán al navegador que debe solicitar otros archivos
necesarios para el sitio. Por ejemplo cuando escribimos <link href="/css/styles.css” rel="stylesheet"> el
navegador interpreta que debe realizar una nueva petición para descargar el archivo styles.css).
Ocurrirá lo mismo con la etiqueta <img src=””> y <script>.
Una vez realizadas todas las peticiones de recursos necesarias comenzará el proceso de
renderizado para mostrar en pantalla el sitio web.

<!-- página 3 -->

¿Cómo el navegador representa una página web?
El proceso de renderizado y presentación se realizará en cinco pasos:
→ Construcción de DOM.
→ Construcción de CSSOM.
→ Construcción del árbol de renderizado.
→ Fase de diseño.
→ Fase de pintura.

<!-- página 4 -->

¿Cómo el navegador representa una página web?
Construcción del DOM
El navegador recibe un documento HTML que es básicamente un archivo de texto con un
encabezado de respuesta Content-Type = text/html; charset=UTF-8.
Cuando el navegador lee el documento HTML, al encontrar un elemento HTML, crea un objeto JS
llamado Node. Finalmente, todos los elementos HTML se convertirán en Node .
Una vez que el navegador ha creado nodos a partir del documento HTML, debe crear una
estructura "similar a un árbol" de estos objetos de nodo.
El DOM (Document Object Model) es una API web de alto nivel proporcionada por el navegador
para representar una página web y exponerla para que los desarrolladores manipulen sus elementos.

<!-- página 5 -->

¿Cómo el navegador representa una página web?
Construcción del CSSOM
Después de construir el DOM, el navegador lee todos los CSS y construye un CSSOM (modelo de
objetos CSS), una estructura similar a un árbol.
Cada nodo de este árbol contiene información de estilo que se copiará al elemento DOM al que
apunta.
Construcción del árbol de renderizado
DOM y CSSOM se combinan para formar un árbol de renderizado que contiene los nodos que
deben mostrarse en la página. Desde la raíz del árbol se recorre cada nodo visible y se aplica la regla
CSSOM correspondiente.
Finalmente, se genera el árbol de renderizado con los nodos visibles, su contenido y estilo.

<!-- página 6 -->

¿Cómo el navegador representa una página web?
Fase de Diseño
En esta fase se calcula la posición exacta de los nodos y su tamaño respecto a la ventana gráfica
del navegador. De esta forma, se genera un modelo de caja que conoce las posiciones y el tamaño
exacto. Este proceso también se conoce como diseño o reflujo .
Fase de Pintura
Como conocemos los nodos visibles, su estilo y geometría, toda esta información se utiliza para
renderizar los nodos desde el árbol de renderizado a píxeles reales en la pantalla. Este proceso se
conoce como "Pintado" y utiliza la capa de interfaz de usuario.

<!-- página 7 -->

¿Cómo el navegador representa una página web?

<!-- página 8 -->

Algo de JavaScript

<!-- página 9 -->

Dom – Document Object Model
Es la representación en un conjunto estándar de objetos de la interfaz gráfica de nuestra aplicación.
A través del DOM los programas en javascript pueden acceder y modificar el contenido, estructura y
estilo de los documentos HTML.
Cada vez que el estado de la aplicación cambia, también lo hará su interfaz.
Esto implica actualizar el DOM, lo cual es una tarea costosa en cuanto a rendimiento.
Cuantos más cambios de estado sean necesario reflejar en él, más lento irá nuestra web.

<!-- página 10 -->

Dom – Document Object Model

<!-- página 11 -->

JavaScript
Si tenemos el siguiente elemento html:
<input type=”text” id=”nombre” name=”nombre” value=”Fede”>
Podemos seleccionarlo desde javascript de la siguiente manera:
let nombre = document.getElementById (‘nombre’);
console.log(nombre.value)

<!-- página 12 -->

JavaScript
Si tenemos los siguientes elementos html:
<input type=”text” id=”nombre” name=”nombre” value=”Fede”>
<input type=”text” id=”correo” name=”nombre” value=”Fede”>
<input type=”text” id=”nombre” name=”nombre” value=”Fede”>
Podemos seleccionarlos desde javascript de la siguiente manera:
const inputs = document.getElementsByTagName('input'); ← colección de objetos HTML
const arrayDeNodos = Array.from(inputs); ← array de objetos HTML.
        arrayDeNodos.forEach(cadaInput => { console.log(cadaInput); });

<!-- página 13 -->

JavaScript - Clases
class FormPersonas {
   constructor() { //codigo }
init() { //codigo }
}
window.addEventListener('DOMContentLoaded', () => {
        new FormPersonas().init();
});

<!-- página 14 -->

Apis Rest

<!-- página 15 -->

Api Rest
Es un conjunto de reglas que permiten que distintas aplicaciones se comuniquen entre sí a través de internet.
Usa el protocolo HTTP y se basa en el estilo de arquitectura REST (Transferencia de Estado Representacional),
facilitando el intercambio de datos en formato JSON de forma simple y rápida.
Características
Cliente-Servidor: separa a quien pide la información (como una app móvil o web) de quien la almacena y
procesa (el servidor)
Sin estado (Stateless): el servidor no guarda datos de la sesión del usuario entre una petición y otra; cada
solicitud viaja con toda la información necesaria para entenderse.
Formato ligero: los datos viajan comúnmente como texto en formato JSON, que es fácil de leer para cualquier
lenguaje de programación

<!-- página 16 -->

JSON
JSON (JavaScript Object Notation o Notación de Objetos de JavaScript) es un formato de texto ligero y sencillo
que sirve para guardar e intercambiar datos.
{
  "id": 1024,
  "nombre": "Juan Pérez",
  "edad": 30,
  "empleado_activo": true,
  "puesto": "Desarrollador Web",
  "habilidades": [
    "JavaScript",
    "Python",
    "SQL"
  ]
}

<!-- página 17 -->

Consumir Api Rest
Para consumir  un api rest podemos hacer uso de la función: fetch. fetch() no devuelve directamente los datos
finales, sino un objeto Response.
fetch(url)
.then(response => response.json())

.then(data => console.log(data))

.catch(error => console.error("Error:", error));
Ese objeto incluye información como:
● response.ok → si la petición fue exitosa (true/false)
● response.status → código HTTP, por ejemplo 200, 404,
500
● response.json() → convierte la respuesta a JSON
● response.text() → devuelve el texto crudo
● response.blob() → devuelve archivos binarios

<!-- página 18 -->

 Api Rest
A continuacion dejamos algunas apis rest gratuitas para consumir y practicar.
→ https://jsonplaceholder.typicode.com/
→ https://pokeapi.co/
→ https://www.freepublicapis.com/
→ https://datosgobar.github.io/georef-ar-api/
