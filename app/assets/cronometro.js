/* ============================================================
   NEWCAMPUS - cronometro de estudio
   ------------------------------------------------------------
   Al lado del reloj, en la misma caja de medidores. Le ponés los
   minutos que quieras, arranca la cuenta regresiva EN ESE MISMO LUGAR
   (no aparece una barra nueva) y cuando llega a cero sale un cartel
   sobrepuesto avisando, con tres salidas: terminar, repetir el mismo
   tiempo, o poner otro.

   Para lo que esta pensado: "estudio 30 minutos sin parar, despues me
   tomo 5". Por eso el cartel del final deja encadenar el siguiente sin
   tener que volver a buscar el boton.

   Se cuenta contra una marca de tiempo absoluta (cuando termina), no
   sumando de a un segundo: si el navegador frena el intervalo porque la
   pestania quedo en segundo plano, la cuenta igual sale bien.

   Queda en sessionStorage: recargar la pagina no te lo borra, cerrar
   NewCampus si. Es la misma idea que el contador de tiempo en la
   pagina, que tampoco sobrevive al cierre.
   ============================================================ */

(function () {
  "use strict";

  var CLAVE = "newcampus:crono";
  var SUGERIDOS = [5, 10, 15, 20, 25, 30, 45, 60];
  var POR_DEFECTO = 30;
  var MAX_MINUTOS = 600;          // 10 horas, por si se va la mano
  var POCO = 60 * 1000;           // ultimo minuto: la cuenta avisa
  var LATIDO = 500;               // cada cuanto se repinta

  var caja = null;
  var reloj = null;
  var fin = 0;                    // cuando termina, en ms
  var minutos = POR_DEFECTO;      // los ultimos elegidos, para "otra vez"
  var tituloOriginal = document.title;

  function el(tag, clase, texto) {
    var e = document.createElement(tag);
    if (clase) { e.className = clase; }
    if (texto !== undefined) { e.textContent = texto; }
    return e;
  }

  function boton(clase, texto, alTocar) {
    var b = el("button", clase, texto);
    b.type = "button";
    b.addEventListener("click", alTocar);
    return b;
  }

  function dos(n) { return (n < 10 ? "0" : "") + n; }

  // mm:ss, y h:mm:ss recien cuando pasa de una hora
  function comoCuenta(ms) {
    var s = Math.max(0, Math.ceil(ms / 1000));
    var hs = Math.floor(s / 3600);
    var m = Math.floor((s % 3600) / 60);
    return hs ? hs + ":" + dos(m) + ":" + dos(s % 60) : m + ":" + dos(s % 60);
  }

  function enPalabras(m) {
    if (m < 60) { return m + (m === 1 ? " minuto" : " minutos"); }
    var hs = Math.floor(m / 60);
    var resto = m % 60;
    return hs + (hs === 1 ? " hora" : " horas") + (resto ? " y " + resto + " min" : "");
  }

  /* ---------- lo que queda guardado ---------- */

  function guardar() {
    try {
      if (fin) { sessionStorage.setItem(CLAVE, JSON.stringify({ fin: fin, minutos: minutos })); }
      else { sessionStorage.removeItem(CLAVE); }
    } catch (e) {}
  }

  /* Devuelve true si habia uno corriendo y todavia le queda tiempo.
     Si vencio mientras la pagina estaba cerrada o recargando, no tiene
     sentido avisar tarde: se vuelve al estado apagado y se limpia lo
     guardado, para que no quede dando vueltas en la proxima carga. */
  function recuperar() {
    var g = null;
    try { g = JSON.parse(sessionStorage.getItem(CLAVE) || "null"); } catch (e) {}
    if (!g || typeof g.fin !== "number") { return false; }
    if (g.fin <= Date.now()) {
      try { sessionStorage.removeItem(CLAVE); } catch (e) {}
      return false;
    }
    fin = g.fin;
    minutos = g.minutos || POR_DEFECTO;
    return true;
  }

  /* ---------- las dos caras del medidor ---------- */

  function pintarApagado() {
    caja.innerHTML = "";
    caja.classList.remove("es-corriendo");
    caja.appendChild(boton("crono-iniciar", "⏱ Iniciar cronómetro", function () {
      elegir("¿Cuánto querés estudiar?", null, arrancar);
    }));
  }

  function pintarCorriendo() {
    caja.innerHTML = "";
    caja.classList.add("es-corriendo");
    caja.appendChild(el("span", "medidor-etq", "Cronómetro"));

    var valor = el("span", "medidor-valor");
    var cuenta = el("span", "crono-cuenta", comoCuenta(fin - Date.now()));
    valor.appendChild(cuenta);

    var x = boton("medidor-btn crono-cancelar", "✕", confirmarCancelar);
    x.title = "Cancelar el cronómetro";
    x.setAttribute("aria-label", "Cancelar el cronómetro");
    valor.appendChild(x);

    caja.appendChild(valor);
    latir(cuenta);
  }

  function latir(cuenta) {
    if (reloj) { window.clearInterval(reloj); }
    reloj = window.setInterval(function () {
      var queda = fin - Date.now();
      if (queda <= 0) { terminar(); return; }
      cuenta.textContent = comoCuenta(queda);
      // poco tiempo: cambia el color y el peso, no una animacion
      cuenta.classList.toggle("es-poco", queda <= POCO);
    }, LATIDO);
  }

  function parar() {
    if (reloj) { window.clearInterval(reloj); reloj = null; }
  }

  /* ---------- arrancar, cancelar, terminar ---------- */

  function arrancar(m) {
    minutos = m;
    fin = Date.now() + m * 60 * 1000;
    guardar();
    pintarCorriendo();
  }

  function apagar() {
    parar();
    fin = 0;
    guardar();
    pintarApagado();
  }

  function confirmarCancelar() {
    var queda = comoCuenta(fin - Date.now());
    cartel({
      titulo: "¿Cancelás el cronómetro?",
      texto: "Todavía te quedan " + queda + " de " + enPalabras(minutos) +
             ". Si lo cancelás, se pierde la cuenta.",
      botones: [
        { texto: "Seguir" },
        { texto: "Cancelar el cronómetro", clase: "crono-btn-rojo", accion: apagar }
      ]
    });
  }

  function terminar() {
    parar();
    fin = 0;
    guardar();
    pintarApagado();

    // si estabas en otra ventana, que se note en la pestania
    document.title = "⏰ Terminó el cronómetro";

    cartel({
      titulo: "⏰ Terminó: " + enPalabras(minutos),
      texto: "Podés cortar acá, repetir el mismo tiempo o poner otro. " +
             "Si venías estudiando, un descanso corto ahora rinde más que seguir de largo.",
      alCerrar: function () { document.title = tituloOriginal; },
      botones: [
        { texto: "Terminar" },
        { texto: "Otro tiempo", accion: function () {
          elegir("¿Cuánto dura el próximo?", minutos, arrancar);
        } },
        { texto: "Otra vez " + minutos + " min", clase: "crono-btn-primario", accion: function () {
          arrancar(minutos);
        } }
      ]
    });
  }

  /* ---------- carteles sobrepuestos ----------
     Se usan las clases del dialogo de Evaluacion para que se vean igual,
     pero el cartel se arma aca: este necesita cerrarse con un aviso y el
     de elegir el tiempo lleva campos adentro. */

  function capaNueva(alCerrar) {
    var capa = el("div", "ev-dialogo-capa crono-capa");
    var cuadro = el("div", "ev-dialogo");
    cuadro.setAttribute("role", "dialog");
    cuadro.setAttribute("aria-modal", "true");
    capa.appendChild(cuadro);

    function cerrar() {
      if (capa.parentNode) { capa.parentNode.removeChild(capa); }
      document.removeEventListener("keydown", tecla, true);
      if (alCerrar) { alCerrar(); }
    }
    function tecla(ev) { if (ev.key === "Escape") { ev.stopPropagation(); cerrar(); } }

    capa.addEventListener("mousedown", function (ev) { if (ev.target === capa) { cerrar(); } });
    document.addEventListener("keydown", tecla, true);
    document.body.appendChild(capa);
    return { capa: capa, cuadro: cuadro, cerrar: cerrar };
  }

  function cartel(op) {
    var v = capaNueva(op.alCerrar);
    v.cuadro.appendChild(el("p", "ev-dialogo-titulo", op.titulo));
    if (op.texto) { v.cuadro.appendChild(el("p", "ev-dialogo-texto", op.texto)); }

    var fila = el("div", "ev-dialogo-botones");
    op.botones.forEach(function (b) {
      fila.appendChild(boton("ev-btn " + (b.clase || ""), b.texto, function () {
        v.cerrar();
        if (b.accion) { b.accion(); }
      }));
    });
    v.cuadro.appendChild(fila);
    fila.lastChild.focus();
  }

  // Elegir minutos: los sugeridos de un toque, o los que se te canten.
  function elegir(titulo, anterior, alElegir) {
    var v = capaNueva(null);
    v.cuadro.classList.add("crono-elegir");
    v.cuadro.appendChild(el("p", "ev-dialogo-titulo", titulo));
    v.cuadro.appendChild(el("p", "ev-dialogo-texto",
      "Elegí uno de estos o poné los minutos que quieras."));

    var elegido = anterior || POR_DEFECTO;

    var chips = el("div", "crono-chips");
    SUGERIDOS.forEach(function (m) {
      var b = boton("crono-chip", m + " min", function () { listo(m); });
      b.setAttribute("data-minutos", String(m));
      chips.appendChild(b);
    });
    v.cuadro.appendChild(chips);

    var linea = el("div", "crono-libre");
    var etq = el("label", "crono-libre-etq", "O los minutos que quieras:");
    etq.setAttribute("for", "crono-minutos");
    var entrada = document.createElement("input");
    entrada.type = "number";
    entrada.id = "crono-minutos";
    entrada.className = "crono-input";
    entrada.min = "1";
    entrada.max = String(MAX_MINUTOS);
    entrada.step = "1";
    entrada.value = String(elegido);
    linea.appendChild(etq);
    linea.appendChild(entrada);
    v.cuadro.appendChild(linea);

    var error = el("p", "crono-error", "");
    error.hidden = true;
    v.cuadro.appendChild(error);

    var fila = el("div", "ev-dialogo-botones");
    fila.appendChild(boton("ev-btn", "Cancelar", v.cerrar));
    fila.appendChild(boton("ev-btn crono-btn-primario", "Empezar", function () { desdeElCampo(); }));
    v.cuadro.appendChild(fila);

    entrada.addEventListener("keydown", function (ev) {
      if (ev.key === "Enter") { ev.preventDefault(); desdeElCampo(); }
    });
    entrada.focus();
    entrada.select();

    function desdeElCampo() {
      var m = Math.floor(Number(entrada.value));
      if (!m || m < 1 || m > MAX_MINUTOS) {
        error.textContent = "Poné un número entre 1 y " + MAX_MINUTOS + " minutos.";
        error.hidden = false;
        entrada.focus();
        return;
      }
      listo(m);
    }

    function listo(m) {
      v.cerrar();
      alElegir(m);
    }
  }

  /* ---------- arranque ---------- */

  function iniciar() {
    caja = document.getElementById("crono");
    // Las copias de ventana no llevan cronometro: seria uno por ventana y
    // no se sabria cual manda. Igual que el contador de tiempo en la pagina.
    if (!caja || window.NC && window.NC.esPanel) {
      if (caja) { caja.hidden = true; }
      return;
    }
    if (recuperar()) { pintarCorriendo(); } else { pintarApagado(); }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", iniciar);
  } else {
    iniciar();
  }
})();
