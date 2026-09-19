/* ============================================================
   NEWCAMPUS - navegacion
   Ruta: #<materia>/<unidad>/<pestania>   ej: #pye/u4/teoria
   ============================================================ */

/* Registro de apuntes. Tiene que existir antes que generado/indice.js.

   El indice dice QUE hay y en que archivo esta; el contenido de cada unidad
   llega despues, cuando la abris, en su propio .js. Se carga con un <script>
   y no con fetch() para que el apunte tambien funcione abierto con file://. */
window.Apuntes = window.Apuntes || {
  cache: {},        // "pye/u5/practica" -> html
  parciales: {},    // "pye" -> { "2025-segundo-parcial": html }
  preguntas: {},    // "pye" -> { "u5": html del banco de preguntas }
  indice: { panes: {}, parciales: {}, preguntas: {} },
  pedidos: {},      // archivo -> lista de avisos esperando, o true si ya llego

  registrarIndice: function (i) { this.indice = i; },
  registrarPane: function (vista, html) { this.cache[vista] = html; },
  registrarParcial: function (materia, id, html) {
    (this.parciales[materia] = this.parciales[materia] || {})[id] = html;
  },
  registrarPreguntas: function (materia, unidad, html) {
    (this.preguntas[materia] = this.preguntas[materia] || {})[unidad] = html;
  },

  /* Trae una pieza de generado/ una sola vez. avisar(true/false) al terminar. */
  cargar: function (archivo, avisar) {
    if (!archivo) { avisar(false); return; }
    var estado = this.pedidos[archivo];
    if (estado === true) { avisar(true); return; }
    if (estado) { estado.push(avisar); return; }   // ya se esta trayendo

    var esperando = this.pedidos[archivo] = [avisar];
    var registro = this;

    function terminar(ok) {
      registro.pedidos[archivo] = ok ? true : null;
      esperando.forEach(function (f) { f(ok); });
    }

    var s = document.createElement("script");
    s.src = "generado/" + archivo;
    s.onload = function () { terminar(true); };
    s.onerror = function () { terminar(false); };
    document.head.appendChild(s);
  }
};

window.NC = window.NC || {};

(function () {
  "use strict";

  // La ruta por defecto sale del indice (ver rutaPorDefecto): la primera
  // materia que tenga apuntes.
  var STORE_KEY = "apuntes:ruta";
  var THEME_KEY = "apuntes:tema";
  var MATERIAS_KEY = "apuntes:materias";

  // Los desplegables muestran el estado cambiando el caracter de la flecha,
  // no rotandola por CSS: asi siempre se ve, corra o no la transicion.
  var FLECHA_ABIERTA = "▼";   // ▼
  var FLECHA_CERRADA = "▶";   // ▶

  var state = { materia: '', unidad: '', tab: 'teoria' };

  /* ---------- modo copia (ventana duplicada) ----------
     index.html?panel=1#pye/u5/teoria abre una COPIA de un solo apartado:
     sin menu de materias ni fila de pestanias, pero con su indice y su
     material de catedra. La marca va en <html> antes de dibujar nada para
     que no se vea el salto. Quien saca las copias es assets/ventanas.js. */

  var PANEL = /[?&]panel=1(?:&|$)/.test(window.location.search);
  window.NC.esPanel = PANEL;
  if (PANEL) { document.documentElement.classList.add("es-panel"); }

  /* ---------- utilidades ---------- */

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  // La pestania Evaluacion es una sola por materia, no depende de la unidad.
  var EVALUACION = "evaluacion";
  // El calendario no depende ni de la materia ni de la unidad: es uno solo.
  var CALENDARIO = "calendario";

  function paneId(s) {
    if (s.tab === CALENDARIO) { return CALENDARIO; }
    return s.tab === EVALUACION ? s.materia + "/" + EVALUACION : s.materia + "/" + s.unidad + "/" + s.tab;
  }

  // Pestanias que valen para toda la materia y no para una unidad puntual
  function esGlobal(tab) { return tab === EVALUACION || tab === CALENDARIO; }

  // La ruta del hash siempre lleva las tres partes, asi se recuerda la unidad.
  function rutaDe(s) { return s.materia + "/" + s.unidad + "/" + s.tab; }

  // Lo que EXISTE lo dice el indice; el contenido puede no estar cargado todavia.
  function existePane(s) {
    if (s.tab === CALENDARIO) { return !!(window.NC.cal && window.NC.cal.montar); }
    var panes = window.Apuntes.indice.panes || {};
    if (s.tab === EVALUACION) {
      var prefijo = s.materia + "/";
      return Object.keys(panes).some(function (k) { return k.indexOf(prefijo) === 0; });
    }
    return Object.prototype.hasOwnProperty.call(panes, paneId(s));
  }

  // Trae la pieza de la unidad si todavia no esta. Evaluacion y Calendario no
  // tienen pieza propia: se arman con JS.
  function asegurarPane(id, avisar) {
    if (id === CALENDARIO || id.split("/")[1] === EVALUACION) { avisar(true); return; }
    if (window.Apuntes.cache[id]) { avisar(true); return; }
    window.Apuntes.cargar((window.Apuntes.indice.panes || {})[id], avisar);
  }

  function estaEnPantalla(id) {
    return !!document.querySelector('.pane[data-view="' + id + '"]');
  }

  /* ---------- apuntes ----------
     Cada unidad viaja en su propio generado/panes/*.js y se trae cuando la
     abris. Una vez traida queda en Apuntes.cache y en el documento, asi que
     volver a ella es instantaneo. */

  function insertarPane(id) {
    var partes = id.split("/");

    if (id === CALENDARIO) {
      if (estaEnPantalla(id)) { return true; }
      if (!window.NC.cal || !window.NC.cal.montar) { return false; }
      var hoja = document.createElement("section");
      hoja.className = "pane";
      hoja.setAttribute("data-view", id);
      $("#contenido").appendChild(hoja);
      window.NC.cal.montar(hoja);          // assets/calendario/calendario.js
      return true;
    }

    if (partes[1] === EVALUACION) {
      if (estaEnPantalla(id)) { return true; }
      if (!window.NC.eval || !window.NC.eval.montar) { return false; }
      var seccion = document.createElement("section");
      seccion.className = "pane";
      seccion.setAttribute("data-view", id);
      $("#contenido").appendChild(seccion);
      window.NC.eval.montar(seccion, partes[0]);   // assets/evaluacion/evaluacion.js
      return true;
    }

    var html = window.Apuntes.cache[id];
    if (!html || estaEnPantalla(id)) { return estaEnPantalla(id); }
    var cont = $("#contenido");
    if (!cont) { return false; }
    cont.insertAdjacentHTML("beforeend", html);

    var pane = document.querySelector('.pane[data-view="' + id + '"]');
    if (pane) { prepararSecciones(pane); }
    return estaEnPantalla(id);
  }

  function limpiarAvisos() {
    $$(".aviso-carga").forEach(function (e) { e.parentNode.removeChild(e); });
  }

  function aviso(texto, clase) {
    var cont = $("#contenido");
    if (!cont) { return; }
    limpiarAvisos();
    var caja = document.createElement("div");
    caja.className = "aviso-carga" + (clase ? " " + clase : "");
    caja.textContent = texto;
    cont.appendChild(caja);
  }

  /* ---------- tema claro / oscuro ---------- */

  function aplicarTema(tema) {
    if (tema === "dark" || tema === "light") {
      document.documentElement.setAttribute("data-theme", tema);
    } else {
      document.documentElement.removeAttribute("data-theme");
    }
    var btn = $("#theme-btn");
    if (btn) {
      btn.textContent = tema === "dark" ? "Modo claro" : "Modo oscuro";
    }
  }

  // las ventanas duplicadas escuchan el cambio de tema para seguir a la principal
  window.NC.aplicarTema = aplicarTema;

  function temaGuardado() {
    try { return localStorage.getItem(THEME_KEY); } catch (e) { return null; }
  }

  function initTema() {
    var t = temaGuardado();
    if (!t) {
      t = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }
    aplicarTema(t);
    var btn = $("#theme-btn");
    if (btn) {
      btn.addEventListener("click", function () {
        var actual = document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
        var nuevo = actual === "dark" ? "light" : "dark";
        aplicarTema(nuevo);
        try { localStorage.setItem(THEME_KEY, nuevo); } catch (e) {}
      });
    }
  }

  /* ---------- indice desplegable de la seccion abierta ---------- */

  var TOC_KEY = "apuntes:indice";
  var enlacesTOC = [];   // [{a, h}] del pane activo, en orden de aparicion

  // Los titulos pueden traer LaTeX. Lo pasamos a texto legible para el indice.
  function limpiarTitulo(txt) {
    return txt
      .replace(/\\[()[\]]/g, "")
      .replace(/\\chi/g, "χ").replace(/\\lambda/g, "λ").replace(/\\mu/g, "μ")
      .replace(/\\sigma/g, "σ").replace(/\\rho/g, "ρ").replace(/\\alpha/g, "α")
      .replace(/\\beta/g, "β").replace(/\\Gamma/g, "Γ").replace(/\\infty/g, "∞")
      .replace(/\\leq/g, "<=").replace(/\\geq/g, ">=").replace(/\\cdot/g, "*")
      .replace(/\^\{?2\}?/g, "²")
      .replace(/\^\{([^}]*)\}/g, "$1")
      .replace(/\\[a-zA-Z]+/g, "")
      .replace(/[{}$]/g, "")
      .replace(/\s+/g, " ")
      .trim();
  }

  window.NC.limpiarTitulo = limpiarTitulo;

  // Se cachea la primera vez, antes de que MathJax reemplace el contenido.
  function tituloDe(h) {
    if (!h.dataset.tocTitulo) { h.dataset.tocTitulo = limpiarTitulo(h.textContent); }
    return h.dataset.tocTitulo;
  }

  // Si el titulo pertenece a un ejercicio, devuelve su numero de guia ("6.", "P1.1")
  // leyendolo de la etiqueta del ejercicio. Si no, devuelve "".
  function numeroDeEjercicio(h) {
    var ej = h.closest ? h.closest(".ej") : null;
    if (!ej) { return ""; }
    var tag = ej.querySelector(".tag");
    if (!tag) { return ""; }

    if (!tag.dataset.numEj) {
      var texto = tag.textContent;
      var m = texto.match(/Ej(?:ercicio)?\.?\s*(\d+)/i);
      if (!m) { tag.dataset.numEj = "-"; }
      // los de la guia "Parte 1" se marcan aparte para no chocar con la numeracion principal
      else { tag.dataset.numEj = (/Parte\s*1/i.test(texto) ? "P1." : "") + m[1] + "."; }
    }
    return tag.dataset.numEj === "-" ? "" : tag.dataset.numEj;
  }

  var ALTO_BARRA = 96;   // alto de la barra superior fija

  function irAlTitulo(h) {
    abrirSeccionDe(h);        // si estaba plegada, se abre
    var y = h.getBoundingClientRect().top + window.pageYOffset - ALTO_BARRA;
    window.scrollTo(0, Math.max(0, y));
    marcarTOCActual();
  }

  function construirTOC(pane) {
    var toc = $("#toc");
    var panel = $("#toc-panel");
    if (!toc || !panel) { return; }

    toc.innerHTML = "";
    enlacesTOC = [];

    // Si la seccion no tiene indice (el calendario, por ejemplo) no alcanza con
    // esconder el panel: hay que soltarle la columna al contenido.
    function vacio(si) {
      panel.classList.toggle("is-empty", si);
      var marco = $(".content-wrap");
      if (marco) { marco.classList.toggle("sin-indice", si); }
    }

    if (!pane) { vacio(true); return; }

    // h2 = secciones / ejercicios ; h3 = subtemas dentro de cada uno.
    // En los parciales, la explicacion detallada que este ABIERTA suma sus partes
    // (los incisos y sus subtitulos) para poder leerla parte por parte.
    var titulos = $$("h2, h3, .pd-explicacion[open] > .pd-cuerpo > .paso, .pd-explicacion[open] > .pd-cuerpo > h4", pane)
      .filter(function (h) {
        // un h3 de una seccion cerrada no se puede leer: tampoco se lista
        if (h.tagName !== "H3") { return true; }
        var seccion = h.closest(".es-seccion");
        return !seccion || seccionAbierta(seccion);
      });
    if (titulos.length < 2) { vacio(true); return; }
    vacio(false);

    var base = pane.getAttribute("data-view").replace(/\//g, "-");

    titulos.forEach(function (h, i) {
      if (!h.id) { h.id = base + "-h" + i; }
      var a = document.createElement("a");
      a.href = "#" + h.id;
      a.className = h.tagName === "H2" ? "lvl-2"
        : h.tagName === "H3" ? "lvl-3"
        : h.classList.contains("paso") ? "lvl-3 lvl-paso" : "lvl-4";

      // los h2 de ejercicio llevan adelante el numero de la guia
      var num = h.tagName === "H2" ? numeroDeEjercicio(h) : "";
      if (num) {
        var badge = document.createElement("span");
        badge.className = "toc-num";
        badge.textContent = num;
        a.appendChild(badge);
        a.appendChild(document.createTextNode(tituloDe(h)));
      } else {
        a.textContent = tituloDe(h);
      }

      a.addEventListener("click", function (ev) {
        ev.preventDefault();
        irAlTitulo(h);
      });
      toc.appendChild(a);
      enlacesTOC.push({ a: a, h: h });
    });

    marcarTOCActual();
  }

  // Resalta en el indice el titulo que se esta leyendo
  function marcarTOCActual() {
    if (!enlacesTOC.length) { return; }
    var actual = enlacesTOC[0];
    for (var i = 0; i < enlacesTOC.length; i++) {
      // 150px = alto aproximado de la barra superior fija
      if (enlacesTOC[i].h.getBoundingClientRect().top <= 150) { actual = enlacesTOC[i]; }
      else { break; }
    }
    enlacesTOC.forEach(function (e) { e.a.classList.remove("is-current"); });
    actual.a.classList.add("is-current");
  }

  function initTOC() {
    var panel = $("#toc-panel");
    var btn = $("#toc-toggle");
    if (!panel || !btn) { return; }

    var guardado = null;
    try { guardado = localStorage.getItem(TOC_KEY); } catch (e) {}
    // por defecto abierto en pantallas anchas, plegado en angostas
    var plegado = guardado !== null
      ? guardado === "cerrado"
      : window.innerWidth < 1280;
    function pintarTOC(cerrado) {
      panel.classList.toggle("is-collapsed", cerrado);
      btn.setAttribute("aria-expanded", String(!cerrado));
      var chev = $(".chev", btn);
      if (chev) { chev.textContent = cerrado ? FLECHA_CERRADA : FLECHA_ABIERTA; }
    }

    pintarTOC(plegado);

    btn.addEventListener("click", function () {
      var ahora = !panel.classList.contains("is-collapsed");
      pintarTOC(ahora);
      try { localStorage.setItem(TOC_KEY, ahora ? "cerrado" : "abierto"); } catch (e) {}
    });

    var pendiente = false;
    window.addEventListener("scroll", function () {
      if (pendiente) { return; }
      pendiente = true;
      window.requestAnimationFrame(function () {
        pendiente = false;
        marcarTOCActual();
      });
    }, { passive: true });
  }

  /* ---------- menu de materias (desplegar / plegar) ---------- */

  // { pye: true/false }. Si una materia no figura, vale el default:
  // abierta si es la materia que estas viendo, cerrada si no.
  var materiasAbiertas = (function () {
    try { return JSON.parse(localStorage.getItem(MATERIAS_KEY) || "{}") || {}; }
    catch (e) { return {}; }
  })();

  function guardarMaterias() {
    try { localStorage.setItem(MATERIAS_KEY, JSON.stringify(materiasAbiertas)); } catch (e) {}
  }

  function estaAbierta(mat) {
    return Object.prototype.hasOwnProperty.call(materiasAbiertas, mat)
      ? !!materiasAbiertas[mat]
      : mat === state.materia;
  }

  function sincronizarMaterias() {
    $$(".materia").forEach(function (m) {
      var mat = m.getAttribute("data-materia");
      var abierta = estaAbierta(mat);
      m.classList.toggle("is-open", abierta);
      var btn = $(".materia-btn", m);
      if (btn) { btn.setAttribute("aria-expanded", String(abierta)); }
      var chev = $(".chev", m);
      if (chev) { chev.textContent = abierta ? FLECHA_ABIERTA : FLECHA_CERRADA; }
    });
  }

  /* ------------------------------------------------------------
     SECCIONES PLEGABLES
     Una unidad entera de corrido es un chorizo. Cada bloque de teoria
     y cada ejercicio de practica se convierte en un desplegable: se ve
     la lista de titulos y abris el que vas a leer.

     La conversion se hace en el documento, no en el contenido: los
     fragmentos de contenido/ se siguen escribiendo como siempre.

     Cabecera = boton, cuerpo = div con hidden (igual que Evaluacion).
     No se usa <details>: MathJax no entra a un <summary> y los titulos
     con formulas quedaban sin tipografiar.

     Las formulas del cuerpo se tipografian al ABRIR. MathJax mide mal
     lo que esta oculto, asi que lo cerrado no se toca.
     ------------------------------------------------------------ */

  function seccionAbierta(seccion) { return seccion.classList.contains("is-open"); }

  function abrirSeccion(seccion, abrir) {
    if (seccionAbierta(seccion) === abrir) { return; }
    var cuerpo = $(":scope > .seccion-cuerpo", seccion);
    var cab = $(":scope > .seccion-cab", seccion);
    var chev = $(".seccion-chev", cab);

    seccion.classList.toggle("is-open", abrir);
    cuerpo.hidden = !abrir;
    cab.setAttribute("aria-expanded", String(abrir));
    if (chev) { chev.textContent = abrir ? FLECHA_ABIERTA : FLECHA_CERRADA; }

    if (abrir) { tipografiarPartes([cuerpo]); }
    construirTOC($(".pane.is-active"));      // los h3 solo cuentan si esta abierta
  }

  function armarSeccion(caja) {
    var titulo = $(":scope > h2", caja);
    if (!titulo) { return null; }            // sin titulo no hay nada que plegar

    caja.classList.add("es-seccion");

    var cab = document.createElement("button");
    cab.type = "button";
    cab.className = "seccion-cab";
    cab.setAttribute("aria-expanded", "false");

    var chev = document.createElement("span");
    chev.className = "seccion-chev";
    chev.textContent = FLECHA_CERRADA;

    var textos = document.createElement("div");
    textos.className = "seccion-tit";
    // el rotulo (kicker / tag) y el titulo pasan a ser la cabecera
    var rotulo = $(":scope > .kicker, :scope > .tag", caja);
    if (rotulo) { textos.appendChild(rotulo); }
    textos.appendChild(titulo);

    cab.appendChild(chev);
    cab.appendChild(textos);

    var cuerpo = document.createElement("div");
    cuerpo.className = "seccion-cuerpo";
    cuerpo.hidden = true;
    while (caja.firstChild) { cuerpo.appendChild(caja.firstChild); }

    caja.appendChild(cab);
    caja.appendChild(cuerpo);
    cab.addEventListener("click", function () { abrirSeccion(caja, !seccionAbierta(caja)); });

    return caja;
  }

  function prepararSecciones(pane) {
    var secciones = [];
    $$(":scope > .bloque, :scope > .ej", pane).forEach(function (c) {
      if (armarSeccion(c)) { secciones.push(c); }
    });
    if (secciones.length < 2) {
      secciones.forEach(function (s) { abrirSeccion(s, true); });   // una sola: abierta
      return;
    }

    // Abrir todo / Cerrar todo, arriba de la primera seccion
    var barra = document.createElement("div");
    barra.className = "pane-controles";

    var cuenta = document.createElement("span");
    cuenta.className = "pane-controles-cuenta";
    cuenta.textContent = secciones.length +
      (pane.getAttribute("data-view").indexOf("/practica") > 0 ? " ejercicios" : " secciones");
    barra.appendChild(cuenta);

    function boton(texto, abrir) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "pane-control";
      b.textContent = texto;
      b.addEventListener("click", function () {
        secciones.forEach(function (s) { abrirSeccion(s, abrir); });
      });
      return b;
    }
    barra.appendChild(boton("Abrir todo", true));
    barra.appendChild(boton("Cerrar todo", false));

    secciones[0].parentNode.insertBefore(barra, secciones[0]);
  }

  // Abre la seccion que contenga a ese titulo (la usa el indice de la derecha)
  function abrirSeccionDe(el) {
    var seccion = el.closest ? el.closest(".es-seccion") : null;
    if (seccion) { abrirSeccion(seccion, true); }
    return seccion;
  }

  /* ---------- MathJax bajo demanda ---------- */

  // Evaluacion cambia de pantalla sin cambiar de pane: rearma el indice cuando lo pide.
  window.NC.reconstruirIndice = function () { construirTOC($(".pane.is-active")); };

  // Cada parte se tipografia una sola vez. Lo que esta adentro de una seccion
  // cerrada NO se toca: MathJax mide mal lo que no esta a la vista.
  function tipografiarPartes(partes) {
    if (!window.MathJax || !window.MathJax.typesetPromise) { return; }
    // OJO: la marca NO puede llamarse data-mjx*, MathJax ignora lo que la tenga
    var nuevas = partes.filter(function (p) { return p && p.dataset.tipografiado !== "1"; });
    if (!nuevas.length) { return; }
    nuevas.forEach(function (p) { p.dataset.tipografiado = "1"; });

    window.MathJax.typesetPromise(nuevas).then(function () {
      // al renderizar las formulas cambian las alturas: recalculamos el indice
      marcarTOCActual();
    }).catch(function () {
      nuevas.forEach(function (p) { p.dataset.tipografiado = ""; });
    });
  }

  // Lo que se ve de un pane: los titulos de todas las secciones, el cuerpo de
  // las abiertas y todo lo que no sea seccion (la intro, los pendientes).
  function tipografiar(pane) {
    if (!pane) { return; }
    var partes = [];
    Array.prototype.forEach.call(pane.children, function (hijo) {
      if (!hijo.classList.contains("es-seccion")) { partes.push(hijo); return; }
      partes.push($(":scope > .seccion-cab > .seccion-tit", hijo));
      if (seccionAbierta(hijo)) { partes.push($(":scope > .seccion-cuerpo", hijo)); }
    });
    tipografiarPartes(partes);
  }

  /* ============================================================
     MATERIAL DE CATEDRA: botones flotantes + ventanas de PDF
     ============================================================ */

  var ventanas = {};        // id -> elemento de la ventana abierta
  var zTope = 500;

  var MIN_ANCHO = 280;
  var MIN_ALTO = 200;

  // Bordes por los que se puede agarrar, con el cursor que le corresponde a cada uno.
  var BORDES = [
    { dir: "n",  cursor: "ns-resize" },
    { dir: "s",  cursor: "ns-resize" },
    { dir: "e",  cursor: "ew-resize" },
    { dir: "w",  cursor: "ew-resize" },
    { dir: "nw", cursor: "nwse-resize" },
    { dir: "ne", cursor: "nesw-resize" },
    { dir: "sw", cursor: "nesw-resize" },
    { dir: "se", cursor: "nwse-resize" }
  ];

  // Limpieza de una version anterior que guardaba la posicion de cada ventana.
  // Ahora cada vez que se abre arranca en su lugar por defecto.
  try { localStorage.removeItem("apuntes:pdf-ventanas"); } catch (e) {}

  // Si la pestania esta oculta o minimizada, el navegador informa 0 de alto y
  // de ancho. En ese caso usamos una medida razonable para no armar la ventana
  // del tamanio minimo pegada al angulo.
  function anchoVista() { return window.innerWidth || document.documentElement.clientWidth || 1280; }
  function altoVista() { return window.innerHeight || document.documentElement.clientHeight || 800; }

  function geoPorDefecto(indice) {
    var ancho = Math.min(620, Math.max(300, anchoVista() - 80));
    var alto = Math.min(820, Math.max(240, altoVista() - 120));
    var desfase = indice * 32;
    return {
      x: Math.max(12, anchoVista() - ancho - 26 - desfase),
      y: Math.max(70, 84 + desfase),
      w: ancho,
      h: alto
    };
  }

  // No deja que la ventana se escape de la pantalla
  function acotar(g) {
    g.w = Math.max(MIN_ANCHO, Math.min(g.w, anchoVista() - 16));
    g.h = Math.max(MIN_ALTO, Math.min(g.h, altoVista() - 16));
    g.x = Math.max(0, Math.min(g.x, anchoVista() - g.w));
    g.y = Math.max(0, Math.min(g.y, altoVista() - g.h));
    return g;
  }

  // Nueva geometria al arrastrar un borde. "dir" son las letras del borde
  // agarrado (n / s / e / w o su combinacion en las esquinas).
  // Los lados n y w mueven la esquina de arriba a la izquierda dejando quieto
  // el lado opuesto, que es como se comporta cualquier ventana del sistema.
  function redimensionar(inicio, dx, dy, dir) {
    var g = { x: inicio.x, y: inicio.y, w: inicio.w, h: inicio.h };

    if (dir.indexOf("e") !== -1) {
      g.w = Math.min(Math.max(inicio.w + dx, MIN_ANCHO), anchoVista() - inicio.x);
    }
    if (dir.indexOf("w") !== -1) {
      var derecha = inicio.x + inicio.w;
      g.w = Math.min(Math.max(inicio.w - dx, MIN_ANCHO), derecha);
      g.x = derecha - g.w;
    }
    if (dir.indexOf("s") !== -1) {
      g.h = Math.min(Math.max(inicio.h + dy, MIN_ALTO), altoVista() - inicio.y);
    }
    if (dir.indexOf("n") !== -1) {
      var abajo = inicio.y + inicio.h;
      g.h = Math.min(Math.max(inicio.h - dy, MIN_ALTO), abajo);
      g.y = abajo - g.h;
    }
    return g;
  }

  function aplicarGeo(v, g) {
    v.style.left = g.x + "px";
    v.style.top = g.y + "px";
    v.style.width = g.w + "px";
    v.style.height = g.h + "px";
  }

  function traerAlFrente(v) {
    zTope += 1;
    v.style.zIndex = zTope;
  }

  function botonAccion(texto, titulo, clase) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "pdf-accion" + (clase ? " " + clase : "");
    b.title = titulo;
    b.setAttribute("aria-label", titulo);
    b.textContent = texto;
    return b;
  }

  function crearVentana(doc, indice) {
    var capa = $("#pdf-capa");
    if (!capa) { return null; }

    var v = document.createElement("div");
    v.className = "pdf-ventana";

    // --- cabecera ---
    var cab = document.createElement("div");
    cab.className = "pdf-cabecera";

    var tit = document.createElement("div");
    tit.className = "pdf-titulo";
    tit.textContent = doc.titulo;
    cab.appendChild(tit);

    var acciones = document.createElement("div");
    acciones.className = "pdf-acciones";

    var bAparte = botonAccion("↗", "Abrir en una pestania nueva");
    bAparte.addEventListener("click", function () {
      window.open(doc.archivo, "_blank");
    });

    var bMin = botonAccion("–", "Minimizar (queda como esta para cuando lo vuelvas a abrir)");
    bMin.addEventListener("click", function () { minimizarVentana(doc.id); });

    var bMax = botonAccion("❐", "Maximizar / restaurar");
    bMax.addEventListener("click", function () { alternarMaximizar(v, doc); });

    var bCerrar = botonAccion("✕", "Cerrar del todo (la proxima vez se abre como nueva)", "cerrar");
    bCerrar.addEventListener("click", function () { cerrarVentana(doc.id); });

    acciones.appendChild(bAparte);
    acciones.appendChild(bMin);
    acciones.appendChild(bMax);
    acciones.appendChild(bCerrar);
    cab.appendChild(acciones);

    // --- cuerpo ---
    var cuerpo = document.createElement("div");
    cuerpo.className = "pdf-cuerpo";

    // <object> en vez de <iframe>: si el navegador no puede incrustar el PDF
    // (puede pasar abriendo el apunte con file://), muestra solo el contenido
    // de adentro, que es el cartel con el boton para abrirlo aparte.
    // FitH = el PDF entra a lo ancho, que es como se lee comodo en una ventana angosta.
    var marco = document.createElement("object");
    marco.setAttribute("type", "application/pdf");
    marco.setAttribute("data", doc.archivo + "#view=FitH");
    marco.setAttribute("title", doc.titulo);

    var fallback = document.createElement("div");
    fallback.className = "pdf-fallback";
    var txtFall = document.createElement("div");
    txtFall.textContent = "Tu navegador no puede mostrar el PDF incrustado aca.";
    var linkFall = document.createElement("a");
    linkFall.href = doc.archivo;
    linkFall.target = "_blank";
    linkFall.rel = "noopener";
    linkFall.textContent = "Abrir " + doc.titulo;
    fallback.appendChild(txtFall);
    fallback.appendChild(linkFall);
    marco.appendChild(fallback);

    cuerpo.appendChild(marco);

    v.appendChild(cab);
    v.appendChild(cuerpo);

    // los 8 bordes para redimensionar
    BORDES.forEach(function (b) {
      var borde = document.createElement("div");
      borde.className = "pdf-borde pdf-borde-" + b.dir;
      v.appendChild(borde);
      hacerRedimensionable(v, borde, b.dir, b.cursor);
    });

    capa.appendChild(v);

    aplicarGeo(v, acotar(geoPorDefecto(indice)));
    traerAlFrente(v);

    v.addEventListener("pointerdown", function () { traerAlFrente(v); });
    hacerArrastrable(v, cab);

    // doble clic en la cabecera = maximizar, como cualquier ventana
    cab.addEventListener("dblclick", function () { alternarMaximizar(v, doc); });

    return v;
  }

  function gestoComun(v, elemento, alMover, cursor) {
    elemento.addEventListener("pointerdown", function (ev) {
      if (ev.button !== 0) { return; }
      if (v.classList.contains("maximizada")) { return; }
      ev.preventDefault();

      var r = v.getBoundingClientRect();
      var inicio = { px: ev.clientX, py: ev.clientY, x: r.left, y: r.top, w: r.width, h: r.height };

      document.body.classList.add("pdf-gesto");
      // el cursor se fija en todo el documento para que no titile al salirse del borde
      document.body.style.cursor = cursor;
      elemento.classList.add("arrastrando");

      function mover(e) {
        alMover(inicio, e.clientX - inicio.px, e.clientY - inicio.py);
      }

      // Los listeners van en window, no en el elemento: asi el gesto sigue
      // funcionando aunque el puntero se salga del borde o del navegador.
      function soltar() {
        window.removeEventListener("pointermove", mover);
        window.removeEventListener("pointerup", soltar);
        window.removeEventListener("pointercancel", soltar);
        document.body.classList.remove("pdf-gesto");
        document.body.style.cursor = "";
        elemento.classList.remove("arrastrando");
      }

      window.addEventListener("pointermove", mover);
      window.addEventListener("pointerup", soltar);
      window.addEventListener("pointercancel", soltar);
    });
  }

  function hacerArrastrable(v, cab) {
    gestoComun(v, cab, function (inicio, dx, dy) {
      aplicarGeo(v, acotar({ x: inicio.x + dx, y: inicio.y + dy, w: inicio.w, h: inicio.h }));
    }, "grabbing");
  }

  function hacerRedimensionable(v, borde, dir, cursor) {
    gestoComun(v, borde, function (inicio, dx, dy) {
      aplicarGeo(v, redimensionar(inicio, dx, dy, dir));
    }, cursor);
  }

  function alternarMaximizar(v, doc) {
    if (v.classList.contains("maximizada")) {
      v.classList.remove("maximizada");
      aplicarGeo(v, acotar(v._geoPrevia || geoPorDefecto(0)));
    } else {
      var r = v.getBoundingClientRect();
      v._geoPrevia = { x: Math.round(r.left), y: Math.round(r.top), w: Math.round(r.width), h: Math.round(r.height) };
      v.classList.add("maximizada");
      aplicarGeo(v, { x: 8, y: 8, w: anchoVista() - 16, h: altoVista() - 16 });
    }
    traerAlFrente(v);
  }

  // CERRAR: saca la ventana del documento. Se descarga el PDF de memoria y se
  // pierde donde estaba, asi que la proxima vez se abre como nueva.
  function cerrarVentana(id) {
    var v = ventanas[id];
    if (!v) { return; }
    v.parentNode.removeChild(v);
    delete ventanas[id];
    pintarLanzador();
  }

  // MINIMIZAR: la esconde pero la deja armada, con su tamanio y su posicion.
  function minimizarVentana(id) {
    var v = ventanas[id];
    if (!v) { return; }
    v.classList.add("minimizada");
    pintarLanzador();
  }

  function restaurarVentana(id) {
    var v = ventanas[id];
    if (!v) { return; }
    v.classList.remove("minimizada");
    traerAlFrente(v);
    pintarLanzador();
  }

  function estaMinimizada(id) {
    return !!ventanas[id] && ventanas[id].classList.contains("minimizada");
  }

  // El boton del lanzador cicla: cerrada -> abierta -> minimizada -> abierta...
  function alternarVentana(doc, indice) {
    if (!ventanas[doc.id]) {
      var v = crearVentana(doc, indice);
      if (v) { ventanas[doc.id] = v; }
    } else if (estaMinimizada(doc.id)) {
      restaurarVentana(doc.id);
    } else {
      minimizarVentana(doc.id);
    }
    pintarLanzador();
  }

  function pintarLanzador() {
    $$(".pdf-item").forEach(function (item) {
      var id = item.getAttribute("data-doc");
      var cargada = !!ventanas[id];
      var minimizada = estaMinimizada(id);

      item.classList.toggle("con-estado", cargada);

      var b = $(".pdf-btn", item);
      if (!b) { return; }
      b.classList.toggle("is-abierto", cargada && !minimizada);
      b.classList.toggle("is-minimizado", minimizada);
      b.title = !cargada ? "Abrir"
        : (minimizada ? "Volver a mostrarlo donde estaba" : "Minimizar");
    });
  }

  function actualizarLanzador() {
    var cont = $("#pdf-lanzador");
    if (!cont) { return; }

    var lista = materialDeLaUnidad();
    cont.innerHTML = "";

    if (!lista || !lista.length) {
      cont.hidden = true;
      document.body.classList.remove("con-lanzador");
      return;
    }
    cont.hidden = false;
    document.body.classList.add("con-lanzador");

    var tit = document.createElement("div");
    tit.className = "pdf-lanzador-tit";
    tit.textContent = "Material de catedra";
    cont.appendChild(tit);

    lista.forEach(function (doc, i) {
      var item = document.createElement("div");
      item.className = "pdf-item";
      item.setAttribute("data-doc", doc.id);

      // la x de descartar va a la izquierda para que las pastillas no se
      // muevan de lugar cuando aparece o desaparece
      var x = document.createElement("button");
      x.type = "button";
      x.className = "pdf-btn-x";
      x.textContent = "✕";
      x.title = "Cerrar del todo " + doc.titulo;
      x.addEventListener("click", function () { cerrarVentana(doc.id); });

      var b = document.createElement("button");
      b.type = "button";
      b.className = "pdf-btn";

      var icono = document.createElement("span");
      icono.className = "pdf-icono";
      icono.textContent = doc.sigla;

      var txt = document.createElement("span");
      txt.className = "pdf-txt";
      txt.textContent = doc.titulo;

      b.appendChild(icono);
      b.appendChild(txt);
      b.addEventListener("click", function () { alternarVentana(doc, i); });

      item.appendChild(x);
      item.appendChild(b);
      cont.appendChild(item);
    });

    pintarLanzador();

    // le avisamos al indice cuanto alto le come el lanzador
    document.body.style.setProperty("--alto-lanzador", Math.ceil(cont.getBoundingClientRect().height) + "px");
  }

  // Si achicas el navegador, las ventanas vuelven adentro de la pantalla
  window.addEventListener("resize", function () {
    Object.keys(ventanas).forEach(function (id) {
      var v = ventanas[id];
      if (v.classList.contains("maximizada")) {
        aplicarGeo(v, { x: 8, y: 8, w: anchoVista() - 16, h: altoVista() - 16 });
      } else {
        var r = v.getBoundingClientRect();
        aplicarGeo(v, acotar({ x: r.left, y: r.top, w: r.width, h: r.height }));
      }
    });
  });

  /* ------------------------------------------------------------
     MENU LATERAL
     No se escribe a mano: sale de contenido/materias.json, que
     construir.py deja en generado/indice.js. Para sumar una unidad
     alcanza con crear su carpeta, nombrarla ahi y construir.
     Una materia sin apuntes todavia se muestra como "pronto".
     ------------------------------------------------------------ */

  function materiasDelIndice() {
    return (window.Apuntes.indice || {}).materias || [];
  }

  function construirMenu() {
    var caja = $("#materias");
    if (!caja) { return; }
    caja.innerHTML = "";

    materiasDelIndice().forEach(function (m) {
      var disponible = !!(m.unidades && m.unidades.length);

      var bloque = document.createElement("div");
      bloque.className = "materia";
      bloque.setAttribute("data-materia", m.clave);
      bloque.setAttribute("data-corto", m.corto || m.nombre);

      var btn = document.createElement("button");
      btn.className = "materia-btn";
      btn.type = "button";
      if (!disponible) { btn.disabled = true; }

      var nombre = document.createElement("span");
      nombre.className = "m-nombre";
      nombre.textContent = m.nombre;
      btn.appendChild(nombre);

      var marca = document.createElement("span");
      if (disponible) {
        marca.className = "chev";
        marca.textContent = FLECHA_CERRADA;
      } else {
        marca.className = "pill-soon";
        marca.textContent = "pronto";
      }
      btn.appendChild(marca);
      bloque.appendChild(btn);

      if (disponible) {
        var lista = document.createElement("ul");
        lista.className = "unidades";
        m.unidades.forEach(function (u) {
          var li = document.createElement("li");
          var bu = document.createElement("button");
          bu.type = "button";
          bu.setAttribute("data-unidad", u.clave);
          bu.setAttribute("data-titulo", u.nombre ? u.num + " — " + u.nombre : u.num);

          var num = document.createElement("span");
          num.className = "u-num";
          num.textContent = u.num;

          var tema = document.createElement("span");
          tema.className = "u-name";
          tema.textContent = u.nombre || "";

          bu.appendChild(num);
          bu.appendChild(tema);
          li.appendChild(bu);
          lista.appendChild(li);
        });
        bloque.appendChild(lista);
      }

      caja.appendChild(bloque);
    });
  }

  // La primera materia con apuntes: es donde se para el campus si no hay
  // nada guardado ni nada en la direccion.
  function rutaPorDefecto() {
    var conApuntes = materiasDelIndice().filter(function (m) {
      return m.unidades && m.unidades.length;
    })[0];
    if (!conApuntes) { return { materia: "", unidad: "", tab: "teoria" }; }
    return { materia: conApuntes.clave, unidad: conApuntes.unidades[0].clave, tab: "teoria" };
  }

  /* ------------------------------------------------------------
     MATERIAL DE CATEDRA
     Que PDFs muestra cada unidad como boton flotante. Tambien sale
     de materias.json: "pdf" es el catalogo de la materia (una sola
     copia de cada archivo) y "material" dice a que unidades se les
     muestra cada uno ("evaluacion" es la pestania).
     ------------------------------------------------------------ */

  function materialDeLaUnidad() {
    var ficha = null;
    materiasDelIndice().forEach(function (m) {
      if (m.clave === state.materia) { ficha = m; }
    });
    if (!ficha || !ficha.pdf || !ficha.material) { return null; }

    var donde = esGlobal(state.tab) ? state.tab : state.unidad;
    var pedidos = ficha.material[donde] || [];
    var lista = pedidos.map(function (id) {
      return ficha.pdf.filter(function (d) { return d.id === id; })[0];
    }).filter(Boolean);
    return lista.length ? lista : null;
  }

  /* ---------- render ---------- */

  function render() {
    if (!existePane(state)) {
      // si la pestania pedida no existe, se cae a teoria
      var alt = Object.assign({}, state, { tab: "teoria" });
      if (existePane(alt)) { state = alt; }
      else { state = rutaPorDefecto(); }
    }

    var id = paneId(state);
    pintarNavegacion(id);

    // La unidad llega en su propio archivo: puede tardar un instante. El numero
    // de pedido evita que una unidad lenta se dibuje encima de otra mas nueva.
    var mio = ++pedido;
    asegurarPane(id, function (llego) {
      if (mio !== pedido) { return; }
      if (!llego || !insertarPane(id)) {
        aviso("No encuentro los apuntes de esta unidad. Corré python construir.py en app/.", "error");
        return;
      }
      mostrarPane(id);
    });
  }

  var pedido = 0;

  function mostrarPane(id) {
    limpiarAvisos();
    // el detalle de un dia del calendario no tiene que quedar flotando
    // encima de otra pestania
    if (window.NC.calDetalle) { window.NC.calDetalle.cerrar(); }

    var activo = null;
    $$(".pane").forEach(function (p) {
      var on = p.getAttribute("data-view") === id;
      p.classList.toggle("is-active", on);
      if (on) { activo = p; }
    });

    construirTOC(activo);
    tipografiar(activo);
    window.scrollTo(0, 0);
  }

  function pintarNavegacion(id) {
    // materias del sidebar (respeta si el usuario la plego a mano)
    sincronizarMaterias();

    // unidades del sidebar
    $$(".unidades button").forEach(function (b) {
      b.classList.toggle("is-active", !esGlobal(state.tab) &&
        b.getAttribute("data-unidad") === state.unidad &&
        b.closest(".materia").getAttribute("data-materia") === state.materia);
    });

    // pestanias
    $$(".tab").forEach(function (t) {
      t.classList.toggle("is-active", t.getAttribute("data-tab") === state.tab);
      var destino = { materia: state.materia, unidad: state.unidad, tab: t.getAttribute("data-tab") };
      t.disabled = !existePane(destino);
      t.style.opacity = t.disabled ? ".45" : "";
    });

    // migas de pan
    var btnUnidad = document.querySelector(
      '.materia[data-materia="' + state.materia + '"] .unidades button[data-unidad="' + state.unidad + '"]'
    );
    var nombreMateria = document.querySelector('.materia[data-materia="' + state.materia + '"] .m-nombre');
    $("#crumb-materia").textContent = nombreMateria ? nombreMateria.textContent : "";
    $("#crumb-unidad").textContent = state.tab === EVALUACION ? "Evaluación"
      : state.tab === CALENDARIO ? "Calendario"
      : (btnUnidad ? btnUnidad.getAttribute("data-titulo") : "");

    actualizarLanzador();

    // guardar y sincronizar hash
    // Una copia no pisa el "ultimo apartado abierto": eso lo manda la ventana principal.
    var ruta = rutaDe(state);
    if (!PANEL) { try { localStorage.setItem(STORE_KEY, ruta); } catch (e) {} }
    if (window.location.hash.slice(1) !== ruta) {
      history.replaceState(null, "", "#" + ruta);
    }
  }

  function ir(parcial) {
    state = Object.assign({}, state, parcial);
    render();
  }

  // Ruta de lo que se esta viendo, opcionalmente cambiandole la pestania.
  // La usa ventanas.js para saber que abrir en la copia.
  window.NC.rutaActual = function (tab) {
    return rutaDe(tab ? Object.assign({}, state, { tab: tab }) : state);
  };

  /* ---------- eventos ---------- */

  function initEventos() {
    // El boton de la materia SOLO despliega y pliega. No cambia lo que estas
    // leyendo: para eso hay que clickear una unidad.
    $$(".materia-btn").forEach(function (b) {
      if (b.disabled) { return; }
      b.addEventListener("click", function () {
        var mat = b.closest(".materia").getAttribute("data-materia");
        materiasAbiertas[mat] = !estaAbierta(mat);
        guardarMaterias();
        sincronizarMaterias();
      });
    });

    $$(".unidades button").forEach(function (b) {
      b.addEventListener("click", function () {
        // desde Evaluacion o Calendario, elegir una unidad lleva a su teoria
        ir({
          materia: b.closest(".materia").getAttribute("data-materia"),
          unidad: b.getAttribute("data-unidad"),
          tab: esGlobal(state.tab) ? "teoria" : state.tab
        });
      });
    });

    $$(".tab").forEach(function (t) {
      t.addEventListener("click", function () {
        if (t.disabled) { return; }
        ir({ tab: t.getAttribute("data-tab") });
      });
    });

    window.addEventListener("hashchange", function () {
      var partes = window.location.hash.slice(1).split("/");
      if (partes.length === 3) {
        state = { materia: partes[0], unidad: partes[1], tab: partes[2] };
        render();
      }
    });
  }

  /* ---------- reloj y tiempo en la pagina ----------
     Hora de Argentina (UTC-3) calculada sobre UTC, asi no depende de como
     tenga configurada la zona horaria la computadora.
     Abajo, cuanto tiempo se lleva con NewCampus abierto. El conteo es de ESTA
     corrida del .exe: se guarda junto al numero de corrida que informa el
     servidor, asi recargar la pagina lo sigue sumando pero cerrar NewCampus lo
     descarta. Tambien vuelve a cero a las 99 horas o con el boton. */

  var TIEMPO_KEY = "newcampus:tiempo";
  var TOPE_SESION = 99 * 3600;   // 99 horas en segundos

  function dos(n) { return (n < 10 ? "0" : "") + n; }

  // Numero que NewCampus.exe genera al arrancar. Sin servidor (file://) no hay
  // corrida que recordar y el contador arranca de cero cada vez.
  function pedirCorrida(cb) {
    if (window.location.protocol === "file:" || !window.fetch) { return; }
    fetch("api/estado", { cache: "no-store" })
      .then(function (r) { return r.json(); })
      .then(function (j) { if (j && j.instancia) { cb(j.instancia); } })
      .catch(function () {});
  }

  function comoReloj(segundos) {
    return dos(Math.floor(segundos / 3600)) + ":" + dos(Math.floor(segundos / 60) % 60) + ":" + dos(segundos % 60);
  }

  function initReloj() {
    var hora = $("#reloj-hora");
    var tiempo = $("#reloj-tiempo");
    var reset = $("#reloj-reset");
    // Las copias no cuentan tiempo: si no, cada ventana abierta sumaria aparte.
    if (!hora || !tiempo || PANEL) { return; }

    var acumulado = 0;
    var corrida = null;
    var ultimo = Date.now();

    function guardar() {
      if (!corrida) { return; }   // sin servidor no se guarda nada
      try {
        localStorage.setItem(TIEMPO_KEY, JSON.stringify({ corrida: corrida, segundos: Math.round(acumulado) }));
      } catch (e) {}
    }

    pedirCorrida(function (id) {
      corrida = id;
      var guardado = null;
      try { guardado = JSON.parse(localStorage.getItem(TIEMPO_KEY) || "null"); } catch (e) {}
      // misma corrida = recargaste la pagina, se sigue sumando lo que ya llevabas
      if (guardado && guardado.corrida === id && typeof guardado.segundos === "number") {
        acumulado += guardado.segundos;
      }
      guardar();
      pintar();
    });

    function pintar() {
      // UTC-3: se le restan 3 horas al reloj universal
      var d = new Date(Date.now() - 3 * 3600 * 1000);
      hora.textContent = dos(d.getUTCHours()) + ":" + dos(d.getUTCMinutes()) + ":" + dos(d.getUTCSeconds());
      tiempo.textContent = comoReloj(Math.floor(acumulado));
    }

    // Se mide por diferencia de tiempo real: si el navegador frena el intervalo
    // (pestania en segundo plano) el conteo igual queda bien.
    window.setInterval(function () {
      var ahora = Date.now();
      acumulado += (ahora - ultimo) / 1000;
      ultimo = ahora;
      if (acumulado >= TOPE_SESION) { acumulado = 0; }
      pintar();
      if (Math.floor(acumulado) % 5 === 0) { guardar(); }
    }, 1000);

    window.addEventListener("pagehide", guardar);
    pintar();

    if (reset) {
      reset.addEventListener("click", function () {
        var reiniciar = function () { acumulado = 0; ultimo = Date.now(); guardar(); pintar(); };
        if (window.NC.eval && window.NC.eval.dialogo) {
          window.NC.eval.dialogo({
            titulo: "¿Reiniciar el tiempo en la página?",
            texto: "El contador vuelve a 00:00:00. No afecta a los apuntes ni a las autoevaluaciones.",
            botones: [{ texto: "Cancelar" }, { texto: "Reiniciar", clase: "ev-btn-primario", accion: reiniciar }]
          });
        } else if (window.confirm("¿Reiniciar el tiempo en la página?")) { reiniciar(); }
      });
    }
  }

  /* ---------- latido ----------
     Mientras la pagina este abierta le avisa al servidor local de NewCampus.exe.
     Cuando se cierra la pestania dejan de llegar avisos y el .exe se apaga solo. */

  function initLatido() {
    // Solo late la ventana principal. Cerrar una copia no apaga nada; cerrar la
    // principal si, y cada copia se cierra sola detras (ver assets/ventanas.js).
    if (PANEL) { return; }
    if (window.location.protocol === "file:" || !window.fetch) { return; }

    function latir() { fetch("api/ping", { method: "POST" }).catch(function () {}); }
    latir();
    window.setInterval(latir, 10000);

    window.addEventListener("pagehide", function () {
      if (navigator.sendBeacon) { navigator.sendBeacon("api/adios", ""); }
    });
  }

  /* ---------- arranque ---------- */

  function rutaInicial() {
    var h = window.location.hash.slice(1).split("/");
    if (h.length === 3) { return { materia: h[0], unidad: h[1], tab: h[2] }; }
    try {
      var g = (localStorage.getItem(STORE_KEY) || "").split("/");
      if (g.length === 3) { return { materia: g[0], unidad: g[1], tab: g[2] }; }
    } catch (e) {}
    return rutaPorDefecto();
  }

  // MathJax carga con async: si termina despues del primer render,
  // tipografiamos el panel que ya este abierto.
  document.addEventListener("mathjax-listo", function () {
    tipografiar(document.querySelector(".pane.is-active"));
  });

  document.addEventListener("DOMContentLoaded", function () {
    construirMenu();          // antes que nada: el resto lee el menu del documento
    initTema();
    initTOC();
    initEventos();
    initReloj();
    initLatido();
    state = rutaInicial();
    render();
    // recordatorio de parciales y trabajos practicos (solo la ventana principal)
    if (!PANEL && window.NC.calAgenda) { window.NC.calAgenda.recordatorio(); }
  });
})();
