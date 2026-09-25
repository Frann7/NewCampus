/* ============================================================
   NEWCAMPUS - datos del usuario en un archivo de la PC
   ------------------------------------------------------------
   El calendario, las autoevaluaciones, la ruta tachada, el menu plegado...
   se guardan en el navegador (localStorage). Solo en el navegador se perderian
   al cambiar de navegador, al borrar sus datos o si NewCampus.exe abre en otro
   puerto (para el navegador cada puerto es un sitio distinto).

   Por eso NewCampus.exe los guarda tambien en un archivo de la computadora,
   fuera del repositorio (%LOCALAPPDATA%\NewCampus\datos.json):
   - al abrir, este script copia ese archivo al navegador ANTES de que corra
     el resto (por eso va primero en index.html y el pedido es sincronico);
   - cada vez que se guarda algo, se manda el conjunto al archivo (agrupado,
     medio segundo despues del ultimo cambio);
   - si el archivo todavia no existe (la primera vez despues de actualizar),
     se sube lo que ya habia en el navegador: nadie pierde nada.

   Sin NewCampus.exe (abriendo con otro servidor o con doble clic en el
   index.html) no hace nada: todo sigue funcionando solo con el navegador.
   ============================================================ */

(function () {
  "use strict";

  var URL = "api/datos";
  var PREFIJOS = ["newcampus:", "apuntes:"];
  // lo que cambia a cada rato y es de cada corrida: no vale la pena guardarlo
  var FUERA = { "newcampus:tiempo": true };
  // cuando cambio algo por ultima vez en ESTE navegador: si es mas nuevo que el
  // archivo (por ejemplo, una ventana copia que abre medio segundo despues de un
  // cambio que todavia no se mando), no se pisa lo del navegador con el archivo
  var MARCA = "newcampus:datos-cambio";

  var ls;
  try { ls = window.localStorage; } catch (e) { return; }
  if (!ls || !window.XMLHttpRequest) { return; }

  function esNuestra(clave) {
    if (!clave || FUERA[clave]) { return false; }
    for (var i = 0; i < PREFIJOS.length; i++) {
      if (clave.indexOf(PREFIJOS[i]) === 0) { return true; }
    }
    return false;
  }

  function recolectar() {
    var datos = {};
    for (var i = 0; i < ls.length; i++) {
      var clave = ls.key(i);
      if (esNuestra(clave)) { datos[clave] = ls.getItem(clave); }
    }
    return datos;
  }

  // 1. Traer el archivo. Pedido sincronico: el resto de la pagina lee
  //    localStorage apenas arranca, y tiene que encontrar los datos ya puestos.
  var respuesta = null;
  try {
    var x = new XMLHttpRequest();
    x.open("GET", URL, false);
    x.setRequestHeader("X-NewCampus", "1");
    x.send(null);
    if (x.status === 200) { respuesta = JSON.parse(x.responseText); }
  } catch (e) { respuesta = null; }

  if (!respuesta || respuesta.app !== "NewCampus") { return; }   // no hay NewCampus.exe

  var setOriginal = Storage.prototype.setItem;
  var removeOriginal = Storage.prototype.removeItem;
  var clearOriginal = Storage.prototype.clear;

  var contenido = respuesta.existe && respuesta.contenido;
  var datosArchivo = contenido && contenido.datos;
  var marcaLocal = ls.getItem(MARCA) || "";
  var marcaArchivo = (contenido && contenido.guardado) || "";
  var localMasNuevo = marcaLocal !== "" && marcaLocal > marcaArchivo;
  if (datosArchivo && typeof datosArchivo === "object" && !localMasNuevo) {
    // El archivo manda: se sacan las claves nuestras que no esten y se ponen las suyas.
    Object.keys(recolectar()).forEach(function (clave) {
      if (!Object.prototype.hasOwnProperty.call(datosArchivo, clave)) { removeOriginal.call(ls, clave); }
    });
    Object.keys(datosArchivo).forEach(function (clave) {
      if (esNuestra(clave) && typeof datosArchivo[clave] === "string") {
        try { setOriginal.call(ls, clave, datosArchivo[clave]); } catch (e) {}
      }
    });
  }

  // 2. Mandar al archivo cada vez que algo cambie.
  var reloj = null;

  function enviar(alCerrar) {
    reloj = null;
    var cuerpo = JSON.stringify({
      app: "NewCampus",
      version: 1,
      guardado: ls.getItem(MARCA) || new Date().toISOString(),
      datos: recolectar()
    });
    try {
      window.fetch(URL, {
        method: "POST",
        headers: { "Content-Type": "application/json", "X-NewCampus": "1" },
        body: cuerpo,
        // al cerrar la pestania el pedido tiene que sobrevivir (hasta 64 KB)
        keepalive: !!alCerrar && cuerpo.length < 60000
      }).catch(function () {});
    } catch (e) {}
  }

  function programar() {
    try { setOriginal.call(ls, MARCA, new Date().toISOString()); } catch (e) {}
    if (reloj) { window.clearTimeout(reloj); }
    reloj = window.setTimeout(enviar, 500);
  }

  Storage.prototype.setItem = function (clave, valor) {
    setOriginal.call(this, clave, valor);
    if (this === ls && esNuestra(String(clave))) { programar(); }
  };
  Storage.prototype.removeItem = function (clave) {
    removeOriginal.call(this, clave);
    if (this === ls && esNuestra(String(clave))) { programar(); }
  };
  Storage.prototype.clear = function () {
    clearOriginal.call(this);
    if (this === ls) { programar(); }
  };

  // lo que quede pendiente al cerrar o recargar, se manda igual
  window.addEventListener("pagehide", function () {
    if (reloj) { window.clearTimeout(reloj); enviar(true); }
  });

  // 3. La primera vez (todavia no hay archivo) se sube lo que habia en el
  //    navegador; y si lo del navegador era mas nuevo, tambien.
  if (!respuesta.existe || localMasNuevo) { enviar(false); }

  window.NC = window.NC || {};
  window.NC.datos = { archivo: true, guardarAhora: function () { enviar(false); } };
})();
