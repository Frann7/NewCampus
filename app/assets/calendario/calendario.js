/* ============================================================
   NEWCAMPUS - calendario
   ------------------------------------------------------------
   Dos vistas:

     MES  - un solo mes ocupando la pantalla, con el nombre grande y una
            flecha a cada lado para pasar al anterior o al siguiente.
            Cada dia muestra lo que tiene anotado y, al tocarlo, abre el
            detalle (assets/calendario/detalle.js).
     ANIO - los doce meses del anio a la vez. Al pasar el mouse por arriba
            de un mes se levanta, y al hacerle clic se entra a la vista MES
            parado en ese mes. Los dias con algo anotado quedan subrayados.

   Lo que se ve en cada dia sale de dos lados:
     · assets/calendario/fechas.js   feriados y mesas, fijos
     · assets/calendario/eventos.js  parciales y trabajos practicos del usuario

   El dia de hoy se calcula en UTC-3 (hora de Argentina) igual que el reloj
   de la barra superior, asi no depende de como tenga configurada la zona
   horaria la computadora.

   La vista y el mes que estabas mirando quedan guardados en el navegador.
   ============================================================ */

window.NC = window.NC || {};

(function () {
  "use strict";

  var CLAVE = "newcampus:calendario";
  var FILAS = 6;          // siempre 6 semanas: asi el mes no cambia de alto
  var ANIO_MIN = 2000;
  var ANIO_MAX = 2099;
  var CHIPS_POR_DIA = 2;  // cuantos eventos entran en el cuadrito antes del "+N"

  function EV() { return window.NC.calEventos; }

  /* ---------- fechas ---------- */

  // Hoy segun el reloj de Argentina (UTC-3)
  function hoy() {
    var d = new Date(Date.now() - 3 * 3600 * 1000);
    return { a: d.getUTCFullYear(), m: d.getUTCMonth(), d: d.getUTCDate() };
  }

  // Que dia de la semana cae el 1, contando la semana de lunes (0) a domingo (6)
  function primerDia(anio, mes) {
    return (new Date(Date.UTC(anio, mes, 1)).getUTCDay() + 6) % 7;
  }

  // Las 42 casillas de la grilla. Cada una sabe su fecha completa, asi el
  // mes anterior y el siguiente tambien pueden mostrar lo que tienen anotado.
  function casillas(anio, mes) {
    var arranque = primerDia(anio, mes);
    var celdas = [];
    for (var i = 0; i < FILAS * 7; i++) {
      var d = new Date(Date.UTC(anio, mes, 1 + i - arranque));
      var a = d.getUTCFullYear(), m = d.getUTCMonth(), n = d.getUTCDate();
      celdas.push({
        n: n,
        anio: a,
        mes: m,
        semana: i % 7,
        otro: m !== mes || a !== anio,
        fecha: EV().iso(a, m, n)
      });
    }
    return celdas;
  }

  /* ---------- estado ---------- */

  var HOY = hoy();
  var estado = { modo: "mes", anio: HOY.a, mes: HOY.m };

  (function recordar() {
    var g = null;
    try { g = JSON.parse(localStorage.getItem(CLAVE) || "null"); } catch (e) {}
    if (!g) { return; }
    if (g.modo === "mes" || g.modo === "anio") { estado.modo = g.modo; }
    if (typeof g.anio === "number" && g.anio >= ANIO_MIN && g.anio <= ANIO_MAX) { estado.anio = g.anio; }
    if (typeof g.mes === "number" && g.mes >= 0 && g.mes <= 11) { estado.mes = g.mes; }
  })();

  function guardar() {
    try { localStorage.setItem(CLAVE, JSON.stringify(estado)); } catch (e) {}
  }

  /* ---------- armado ---------- */

  function el(tag, clase, texto) {
    var e = document.createElement(tag);
    if (clase) { e.className = clase; }
    if (texto !== undefined) { e.textContent = texto; }
    return e;
  }

  var raiz = null;        // el <div class="cal"> montado
  var titulo = null;
  var cuerpo = null;

  function montar(pane) {
    raiz = el("div", "cal");

    var barra = el("div", "cal-barra");

    var nav = el("div", "cal-nav");
    nav.appendChild(flecha("anterior", "‹"));

    // Ancho fijo por CSS: si el titulo se encogiera con los meses cortos,
    // la flecha se correria debajo del puntero entre dos clics.
    titulo = el("div", "cal-titulo");
    nav.appendChild(titulo);

    nav.appendChild(flecha("siguiente", "›"));
    barra.appendChild(nav);

    var modos = el("div", "cal-modos");
    [["mes", "Mes"], ["anio", "Año"]].forEach(function (m) {
      var b = el("button", "cal-modo", m[1]);
      b.type = "button";
      b.setAttribute("data-modo", m[0]);
      b.addEventListener("click", function () { cambiarModo(m[0]); });
      modos.appendChild(b);
    });
    barra.appendChild(modos);

    var hoyBtn = el("button", "cal-hoy", "Hoy");
    hoyBtn.type = "button";
    hoyBtn.title = "Volver al mes de hoy";
    hoyBtn.addEventListener("click", function () {
      var h = hoy();
      var adelante = (h.a * 12 + h.m) >= (estado.anio * 12 + estado.mes);
      estado.anio = h.a;
      estado.mes = h.m;
      pintar(adelante ? "der" : "izq");
    });
    barra.appendChild(hoyBtn);

    var agregar = el("button", "cal-agregar", "+ Fecha");
    agregar.type = "button";
    agregar.title = "Anotar un parcial o un trabajo práctico";
    agregar.addEventListener("click", function () {
      var h = hoy();
      // si estas mirando otro mes, se propone el dia 1 de ese mes
      var fecha = (h.a === estado.anio && h.m === estado.mes)
        ? EV().iso(h.a, h.m, h.d)
        : EV().iso(estado.anio, estado.mes, 1);
      abrirDia(fecha);
    });
    barra.appendChild(agregar);

    raiz.appendChild(barra);

    cuerpo = el("div", "cal-cuerpo");
    raiz.appendChild(cuerpo);

    pane.appendChild(raiz);
    pintar(null);

    // flechas del teclado: comodo para hojear meses
    raiz.addEventListener("keydown", function (ev) {
      if (ev.target && ev.target.tagName === "INPUT") { return; }
      if (ev.key === "ArrowLeft") { mover(-1); }
      else if (ev.key === "ArrowRight") { mover(1); }
    });

    // si anotas algo desde una ventana duplicada, esta se entera
    window.addEventListener("storage", function (ev) {
      if (ev.key === "newcampus:eventos") { refrescar(); }
    });
  }

  function flecha(cual, glifo) {
    var b = el("button", "cal-flecha cal-flecha-" + cual);
    b.type = "button";
    b.appendChild(el("span", "cal-flecha-glifo", glifo));
    b.addEventListener("click", function () { mover(cual === "anterior" ? -1 : 1); });
    return b;
  }

  function tituloFlechas() {
    var MESES = EV().MESES;
    var anterior = raiz.querySelector(".cal-flecha-anterior");
    var siguiente = raiz.querySelector(".cal-flecha-siguiente");
    if (estado.modo === "mes") {
      var prev = (estado.mes + 11) % 12;
      var sig = (estado.mes + 1) % 12;
      anterior.title = MESES[prev] + " " + (estado.mes === 0 ? estado.anio - 1 : estado.anio);
      siguiente.title = MESES[sig] + " " + (estado.mes === 11 ? estado.anio + 1 : estado.anio);
    } else {
      anterior.title = String(estado.anio - 1);
      siguiente.title = String(estado.anio + 1);
    }
    anterior.setAttribute("aria-label", anterior.title);
    siguiente.setAttribute("aria-label", siguiente.title);
  }

  // Un paso para adelante o para atras: en vista MES cambia de mes,
  // en vista ANIO cambia de anio.
  function mover(paso) {
    if (estado.modo === "mes") {
      var total = estado.anio * 12 + estado.mes + paso;
      var anio = Math.floor(total / 12);
      if (anio < ANIO_MIN || anio > ANIO_MAX) { return; }
      estado.anio = anio;
      estado.mes = total - anio * 12;
    } else {
      if (estado.anio + paso < ANIO_MIN || estado.anio + paso > ANIO_MAX) { return; }
      estado.anio += paso;
    }
    pintar(paso > 0 ? "der" : "izq");
  }

  function cambiarModo(modo) {
    if (estado.modo === modo) { return; }
    estado.modo = modo;
    pintar(null);
  }

  function abrirDia(fecha) {
    if (window.NC.calDetalle) { window.NC.calDetalle.abrir(fecha); }
  }

  // Redibuja sin animacion, conservando la vista (lo llama detalle.js
  // despues de agregar, editar o borrar).
  function refrescar() { if (raiz) { pintar(null); } }

  /* ---------- dibujo ---------- */

  function pintar(desde) {
    if (!raiz || !EV()) { return; }
    var MESES = EV().MESES;

    titulo.innerHTML = "";
    if (estado.modo === "mes") {
      titulo.appendChild(el("span", "cal-titulo-mes", MESES[estado.mes]));
      titulo.appendChild(el("span", "cal-titulo-anio", String(estado.anio)));
    } else {
      titulo.appendChild(el("span", "cal-titulo-mes", String(estado.anio)));
    }

    Array.prototype.forEach.call(raiz.querySelectorAll(".cal-modo"), function (b) {
      b.classList.toggle("is-activo", b.getAttribute("data-modo") === estado.modo);
    });
    tituloFlechas();

    cuerpo.innerHTML = "";
    var vista = estado.modo === "mes" ? vistaMes(estado.anio, estado.mes) : vistaAnio(estado.anio);
    cuerpo.appendChild(vista);

    // El deslizamiento solo acompania el cambio; lo que dice en que mes estas
    // es el titulo, que ya esta escrito antes de que la animacion arranque.
    if (desde) {
      var clase = desde === "der" ? "cal-entra-der" : "cal-entra-izq";
      vista.classList.add(clase);
      vista.addEventListener("animationend", function () { vista.classList.remove(clase); });
    }

    guardar();
  }

  function cabeceraSemana(cortos) {
    var fila = el("div", "cal-semana");
    (cortos ? EV().DIAS_MINI : EV().DIAS_CORTO).forEach(function (d, i) {
      var c = el("span", "cal-dia-sem" + (i > 4 ? " es-finde" : ""), d);
      if (!cortos) { c.title = EV().DIAS[i]; }
      fila.appendChild(c);
    });
    return fila;
  }

  function esHoy(c) {
    var h = hoy();
    return h.a === c.anio && h.m === c.mes && h.d === c.n;
  }

  /* ---------- vista MES ---------- */

  function vistaMes(anio, mes) {
    var caja = el("div", "cal-mes");
    caja.appendChild(cabeceraSemana(false));

    var porFecha = EV().delMes(anio, mes);
    var grilla = el("div", "cal-grilla");

    casillas(anio, mes).forEach(function (c) {
      grilla.appendChild(cuadroDia(c, porFecha[c.fecha] || EV().delDia(c.fecha)));
    });

    caja.appendChild(grilla);

    var leyenda = leyendaDelMes(anio, mes);
    if (leyenda) { caja.appendChild(leyenda); }
    return caja;
  }

  function cuadroDia(c, eventos) {
    var fijas = EV().academicas(c.fecha);

    var d = el("button", "cal-dia");
    d.type = "button";
    if (c.otro) { d.classList.add("es-otro"); }
    if (c.semana > 4) { d.classList.add("es-finde"); }
    if (esHoy(c)) { d.classList.add("es-hoy"); }
    if (fijas.length) { d.classList.add("tiene-fija", "es-" + fijas[0].tipo); }

    var cab = el("span", "cal-dia-cab");
    cab.appendChild(el("span", "cal-num", String(c.n)));
    if (esHoy(c)) { cab.appendChild(el("span", "cal-etq-hoy", "hoy")); }
    d.appendChild(cab);

    fijas.forEach(function (f) {
      d.appendChild(el("span", "cal-marca cal-marca-" + f.tipo, f.corto || f.titulo));
    });

    eventos.slice(0, CHIPS_POR_DIA).forEach(function (e) {
      d.appendChild(chip(e));
    });
    if (eventos.length > CHIPS_POR_DIA) {
      d.appendChild(el("span", "cal-mas", "+" + (eventos.length - CHIPS_POR_DIA) + " más"));
    }

    var resumen = eventos.map(function (e) {
      return EV().TIPOS[e.tipo].nombre + " de " + EV().materia(e.materia).nombre;
    }).concat(fijas.map(function (f) { return f.titulo; }));

    d.title = resumen.length ? resumen.join(" · ") : "Anotar algo este día";
    d.setAttribute("aria-label", EV().largo(c.fecha) + (resumen.length ? ". " + resumen.join(". ") : ""));
    d.addEventListener("click", function () { abrirDia(c.fecha); });

    return d;
  }

  function chip(e) {
    var mat = EV().materia(e.materia);
    var c = el("span", "cal-ev");
    c.style.setProperty("--h", mat.tono);
    c.appendChild(el("span", "cal-ev-glifo", EV().TIPOS[e.tipo].glifo));
    c.appendChild(el("span", "cal-ev-txt", mat.corto));
    return c;
  }

  // Abajo del mes, que materia es cada color
  function leyendaDelMes(anio, mes) {
    var porFecha = EV().delMes(anio, mes);
    var vistas = {};
    var orden = [];
    Object.keys(porFecha).forEach(function (f) {
      porFecha[f].forEach(function (e) {
        if (vistas[e.materia]) { return; }
        vistas[e.materia] = true;
        orden.push(EV().materia(e.materia));
      });
    });
    if (!orden.length) { return null; }

    var caja = el("div", "cal-leyenda");
    orden.forEach(function (m) {
      var item = el("span", "cal-leyenda-item");
      item.style.setProperty("--h", m.tono);
      item.appendChild(el("span", "cal-leyenda-punto"));
      item.appendChild(el("span", null, m.nombre));
      caja.appendChild(item);
    });
    return caja;
  }

  /* ---------- vista ANIO ---------- */

  function vistaAnio(anio) {
    var caja = el("div", "cal-anio");
    for (var m = 0; m < 12; m++) {
      caja.appendChild(mini(anio, m));
    }
    return caja;
  }

  function mini(anio, mes) {
    var MESES = EV().MESES;
    var porFecha = EV().delMes(anio, mes);

    var b = el("button", "cal-mini");
    b.type = "button";
    b.title = "Ver " + MESES[mes] + " " + anio;
    b.appendChild(el("span", "cal-mini-tit", MESES[mes]));
    b.appendChild(cabeceraSemana(true));

    var grilla = el("span", "cal-mini-grilla");
    casillas(anio, mes).forEach(function (c) {
      var clase = "cal-mini-dia";
      if (c.otro) { clase += " es-otro"; }
      if (c.semana > 4) { clase += " es-finde"; }
      if (esHoy(c)) { clase += " es-hoy"; }

      var d = el("span", clase, String(c.n));
      var eventos = porFecha[c.fecha];
      if (!c.otro && eventos && eventos.length) {
        d.classList.add("con-evento");
        d.style.setProperty("--h", EV().materia(eventos[0].materia).tono);
      } else if (!c.otro && EV().academicas(c.fecha).length) {
        d.classList.add("con-fija");
      }
      grilla.appendChild(d);
    });
    b.appendChild(grilla);

    if (anio === HOY.a && mes === HOY.m) { b.classList.add("es-mes-de-hoy"); }

    b.addEventListener("click", function () {
      estado.mes = mes;
      estado.anio = anio;
      estado.modo = "mes";
      pintar(null);
    });
    return b;
  }

  window.NC.cal = { montar: montar, refrescar: refrescar };
})();
