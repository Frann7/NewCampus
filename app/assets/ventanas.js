/* ============================================================
   NEWCAMPUS - ventanas duplicadas
   ------------------------------------------------------------
   Manteniendo apretada una pestania (Teoria / Practica / Evaluacion)
   se saca una COPIA de ese apartado en una ventana aparte, para poder
   leer dos partes del mismo apunte al mismo tiempo. Lo mismo con los
   botones de la ruta recomendada: la copia abre ese mismo destino
   (NC.ventanas.sostener). Y con las unidades del menu de materias: la
   copia es solo esa unidad, con sus pestanias Teoria y Practica.

   La copia es la misma index.html abierta como:

       index.html?panel=1#<materia>/<unidad>/<pestania>

   El "panel=1" lo lee app.js: marca el <html> con la clase "es-panel",
   que esconde el menu de materias y la fila de pestanias. Queda el
   apartado con su indice y su material de catedra, nada mas.

   Reglas:
   - La ventana original NO se mueve: sacar una copia no cambia de pestania.
   - Tope de MAXIMO copias abiertas a la vez (para no llenar la memoria).
   - Las copias no laten al servidor: el que mantiene vivo a NewCampus.exe
     es siempre la ventana principal. Cerrar una copia no cierra nada.
   - Si se cierra la ventana principal, cada copia se cierra sola (revisa
     a su "padre" cada REVISAR_PADRE milisegundos).
   ============================================================ */

window.NC = window.NC || {};

(function () {
  "use strict";

  var MARCA = "nc-copia-";     // nombre que llevan las ventanas que sacamos
  var MAXIMO = 4;              // copias abiertas a la vez
  var MS_GRACIA = 240;         // antes de esto no pasa absolutamente nada: es un clic
  var MS_SOSTENER = 800;       // recien acá sale la copia
  var REVISAR_PADRE = 2000;    // cada cuanto la copia mira si vive la principal

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  function el(tag, clase, texto) {
    var e = document.createElement(tag);
    if (clase) { e.className = clase; }
    if (texto !== undefined) { e.textContent = texto; }
    return e;
  }

  function cartel(titulo, texto) {
    if (window.NC.eval && window.NC.eval.dialogo) {
      window.NC.eval.dialogo({ titulo: titulo, texto: texto, botones: [{ texto: "Entendido", clase: "ev-btn-primario" }] });
    } else {
      window.alert(titulo + "\n\n" + texto);
    }
  }

  /* ============================================================
     LADO COPIA: lo que corre adentro de la ventana duplicada
     ============================================================ */

  function initCopia() {
    var fila = $(".topbar-row");
    if (!fila) { return; }

    var chip = document.createElement("div");
    chip.className = "panel-chip";
    chip.appendChild(el("span", "panel-chip-etq", "copia"));
    var txt = el("span", "panel-chip-txt", "");
    chip.appendChild(txt);
    fila.insertBefore(chip, fila.firstChild);

    function rotular() {
      var activo = $(".tab.is-active");         // app.js ya pinto la navegacion
      var unidad = $("#crumb-unidad");
      var nombre = activo ? (activo.dataset.nombre || activo.textContent.trim()) : "Copia";
      var donde = unidad && unidad.textContent !== nombre ? unidad.textContent : "";
      // la copia de una unidad se nombra por la unidad: las pestanias se ven abajo
      txt.textContent = window.NC.esPanelUnidad && donde ? donde.split(" — ")[0] : nombre;
      if (activo) { chip.setAttribute("data-tab", activo.getAttribute("data-tab")); }
      document.title = nombre + (donde ? " - " + donde : "") + " | NewCampus";
    }

    rotular();
    window.addEventListener("hashchange", rotular);
    // cambiar de pestania no dispara hashchange (app.js usa replaceState)
    $$(".tab").forEach(function (t) {
      t.addEventListener("click", function () { window.setTimeout(rotular, 0); });
    });

    // Se cierra sola cuando se cierra la ventana principal. Recargar la
    // principal no la afecta: la referencia sigue siendo la misma ventana.
    // Solo vale para las copias que salieron de una pestania: si alguien abre
    // a mano la direccion con ?panel=1, la pagina se queda tranquila.
    if (window.name.indexOf(MARCA) !== 0) { return; }
    window.setInterval(function () {
      var padre = null;
      try { padre = window.opener; } catch (e) { padre = null; }
      if (!padre || padre.closed) { window.close(); }
    }, REVISAR_PADRE);
  }

  /* ============================================================
     LADO PRINCIPAL: mantener apretado para sacar una copia
     ============================================================ */

  var abiertas = [];           // ventanas duplicadas vivas
  var recienSacada = false;    // para que el clic posterior no cambie de pestania
  var pendiente = null;        // direccion que quedo esperando para reintentar

  function vivas() {
    abiertas = abiertas.filter(function (w) {
      try { return w && !w.closed; } catch (e) { return false; }
    });
    return abiertas;
  }

  function geometria(indice) {
    var pant = window.screen || {};
    var anchoPant = pant.availWidth || window.outerWidth || 1440;
    var altoPant = pant.availHeight || window.outerHeight || 900;

    var ancho = Math.min(1180, Math.max(640, Math.round(anchoPant * 0.58)));
    var alto = Math.max(460, altoPant - 70);
    var desfase = (indice % 4) * 34;

    return {
      w: ancho,
      h: alto,
      x: Math.max(0, anchoPant - ancho - 24 - desfase),
      y: Math.max(0, 20 + desfase)
    };
  }

  // La copia de una pestania: el mismo apartado que se esta viendo.
  function urlDeTab(tab) {
    var ruta = window.NC.rutaActual ? window.NC.rutaActual(tab) : null;
    return ruta ? "index.html?panel=1#" + ruta : null;
  }

  // La copia de una unidad del menu: solo esa unidad, con Teoria y Practica.
  function urlDeUnidad(b) {
    var materia = b.closest(".materia");
    var ruta = materia && window.NC.rutaDeUnidad
      ? window.NC.rutaDeUnidad(materia.getAttribute("data-materia"), b.getAttribute("data-unidad"))
      : null;
    return ruta ? "index.html?panel=1&unidad=1#" + ruta : null;
  }

  // Abre la ventana. Devuelve null si el navegador la bloqueo.
  function abrirCopia(url) {
    if (!url) { return null; }

    var g = geometria(vivas().length);
    try {
      return window.open(
        url,
        MARCA + Date.now(),
        "popup=yes,width=" + g.w + ",height=" + g.h + ",left=" + g.x + ",top=" + g.y
      );
    } catch (e) { return null; }
  }

  // "tope" | "bloqueada" | "ok".
  // Chrome deja abrir ventanas un rato despues de que apretaste, asi que la
  // copia sale sola al llenarse la barra. Si igual la bloquea, se reintenta al
  // soltar el boton, que es un gesto tuyo y ahi no la puede bloquear.
  function pedirCopia(url, ultimoIntento) {
    if (vivas().length >= MAXIMO) {
      cartel("Ya tenés " + MAXIMO + " ventanas duplicadas",
             "El tope es de " + MAXIMO + " copias abiertas a la vez para no cargar la máquina. " +
             "Cerrá alguna de las que ya sacaste y volvé a mantener apretada la pestaña.");
      return "tope";
    }

    var w = abrirCopia(url);
    if (w) {
      abiertas.push(w);
      try { w.focus(); } catch (e) {}
      return "ok";
    }

    if (ultimoIntento) {
      cartel("El navegador bloqueó la ventana",
             "Chrome bloquea las ventanas nuevas hasta que se las permitís. Tocá el ícono de la barra de " +
             "direcciones (\"Se bloqueó una ventana emergente\"), permitilas en este sitio y volvé a intentar.");
    }
    return "bloqueada";
  }

  // Barra de progreso de la pulsacion. Dos tiempos:
  //   0 .. MS_GRACIA      no se dibuja nada. Un clic normal entra entero aca,
  //                       asi que cambiar de pestania no muestra ningun amague.
  //   MS_GRACIA .. MS_SOSTENER   se llena la barra; al llenarse sale la copia.
  // Se dibuja con el tiempo real que paso, no con una transicion de CSS, asi
  // marca siempre lo mismo aunque la maquina vaya lenta.
  function prepararPestania(t) {
    if (t.dataset.nombre === undefined) { t.dataset.nombre = t.textContent.trim(); }
    prepararSostener(t, function () { return urlDeTab(t.getAttribute("data-tab")); },
      "Clic para abrirla acá. Mantené apretado para sacarla en otra ventana.");
  }

  // Cualquier boton que al mantenerlo apretado saque una copia. obtenerUrl()
  // dice que abrir en la ventana nueva.
  function prepararSostener(t, obtenerUrl, ayuda) {
    t.setAttribute("data-sostenible", "");
    if (ayuda) { t.title = ayuda; }

    var barra = el("span", "tab-carga");
    t.appendChild(barra);

    var reloj = null;
    var cuadro = null;
    var desde = 0;

    function soltar() {
      if (reloj) { window.clearTimeout(reloj); reloj = null; }
      if (cuadro) { window.cancelAnimationFrame(cuadro); cuadro = null; }
      t.classList.remove("sosteniendo");
      barra.style.width = "0%";
    }

    function pintar() {
      var paso = Date.now() - desde;
      if (paso < MS_GRACIA) { cuadro = window.requestAnimationFrame(pintar); return; }

      t.classList.add("sosteniendo");
      var p = Math.min(1, (paso - MS_GRACIA) / (MS_SOSTENER - MS_GRACIA));
      barra.style.width = (p * 100).toFixed(1) + "%";
      if (p < 1) { cuadro = window.requestAnimationFrame(pintar); }
    }

    t.addEventListener("pointerdown", function (ev) {
      if (ev.button !== 0 || t.disabled) { return; }
      soltar();
      desde = Date.now();
      pintar();
      reloj = window.setTimeout(function () {
        soltar();
        recienSacada = true;
        // por si el clic nunca llega (se solto afuera del boton)
        window.setTimeout(function () { recienSacada = false; }, 1500);
        var url = obtenerUrl();
        pendiente = pedirCopia(url, false) === "bloqueada" ? url : null;
      }, MS_SOSTENER);
    });

    t.addEventListener("pointerup", function () {
      soltar();
      if (pendiente) {
        var url = pendiente;
        pendiente = null;
        pedirCopia(url, true);
      }
    });

    ["pointerleave", "pointercancel", "blur"].forEach(function (e) {
      t.addEventListener(e, soltar);
    });
  }

  function initPrincipal() {
    var tabs = $$(".tab");
    if (!tabs.length) { return; }
    tabs.forEach(prepararPestania);

    $$(".unidades button").forEach(function (b) {
      prepararSostener(b, function () { return urlDeUnidad(b); },
        "Clic para abrirla acá. Mantené apretado para abrir solo esta unidad en otra ventana.");
    });

    // El clic que viene despues de sacar una copia no tiene que cambiar de
    // pestania. Va en captura sobre el documento para adelantarse al oyente
    // que app.js puso en el propio boton.
    document.addEventListener("click", function (ev) {
      if (!recienSacada) { return; }
      if (!ev.target.closest || !ev.target.closest("[data-sostenible]")) { return; }
      recienSacada = false;
      ev.preventDefault();
      ev.stopPropagation();
    }, true);
  }

  /* ---------- tema compartido entre ventanas ---------- */

  window.addEventListener("storage", function (ev) {
    if (ev.key === "apuntes:tema" && window.NC.aplicarTema) {
      window.NC.aplicarTema(ev.newValue);
    }
  });

  /* ---------- arranque ---------- */

  document.addEventListener("DOMContentLoaded", function () {
    // corre despues de app.js: la navegacion ya esta pintada
    if (window.NC.esPanel) { initCopia(); } else { initPrincipal(); }
  });

  window.NC.ventanas = {
    maximo: MAXIMO,
    duplicar: function (tab) { return pedirCopia(urlDeTab(tab), true); },
    sostener: function (boton, obtenerUrl) {
      if (window.NC.esPanel) { return; }      // una copia no saca copias
      prepararSostener(boton, obtenerUrl, "Clic para ir. Mantené apretado para abrirlo en otra ventana.");
    },
    abiertas: function () { return vivas().length; }
  };
})();
