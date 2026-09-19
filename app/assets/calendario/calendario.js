/* ============================================================
   NEWCAMPUS - calendario
   ------------------------------------------------------------
   Dos vistas:

     MES  - un solo mes ocupando la pantalla, con el nombre grande y una
            flecha a cada lado para pasar al anterior o al siguiente.
     ANIO - los doce meses del anio a la vez. Al pasar el mouse por arriba
            de un mes se levanta, y al hacerle clic se entra a la vista MES
            parado en ese mes.

   El dia de hoy se calcula en UTC-3 (hora de Argentina) igual que el reloj
   de la barra superior, asi no depende de como tenga configurada la zona
   horaria la computadora.

   La vista y el mes que estabas mirando quedan guardados en el navegador.
   ============================================================ */

window.NC = window.NC || {};

(function () {
  "use strict";

  var MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
               "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
  var DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];
  var DIAS_CORTO = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"];
  var DIAS_MINI = ["L", "M", "M", "J", "V", "S", "D"];

  var CLAVE = "newcampus:calendario";
  var FILAS = 6;          // siempre 6 semanas: asi el mes no cambia de alto
  var ANIO_MIN = 2000;
  var ANIO_MAX = 2099;

  /* ---------- fechas ---------- */

  // Hoy segun el reloj de Argentina (UTC-3)
  function hoy() {
    var d = new Date(Date.now() - 3 * 3600 * 1000);
    return { a: d.getUTCFullYear(), m: d.getUTCMonth(), d: d.getUTCDate() };
  }

  function diasDelMes(anio, mes) {
    return new Date(Date.UTC(anio, mes + 1, 0)).getUTCDate();
  }

  // Que dia de la semana cae el 1, contando la semana de lunes (0) a domingo (6)
  function primerDia(anio, mes) {
    return (new Date(Date.UTC(anio, mes, 1)).getUTCDay() + 6) % 7;
  }

  // Las 42 casillas de la grilla, con el numero que va en cada una y de que
  // mes es (el mes anterior y el siguiente se dibujan atenuados).
  function casillas(anio, mes) {
    var arranque = primerDia(anio, mes);
    var total = diasDelMes(anio, mes);
    var antes = diasDelMes(mes === 0 ? anio - 1 : anio, (mes + 11) % 12);
    var celdas = [];

    for (var i = 0; i < FILAS * 7; i++) {
      var n = i - arranque + 1;
      if (n < 1) { celdas.push({ n: antes + n, otro: true, semana: i % 7 }); }
      else if (n > total) { celdas.push({ n: n - total, otro: true, semana: i % 7 }); }
      else { celdas.push({ n: n, otro: false, semana: i % 7 }); }
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

    titulo = el("button", "cal-titulo");
    titulo.type = "button";
    titulo.addEventListener("click", function () {
      // el titulo es el atajo entre las dos vistas
      cambiarModo(estado.modo === "mes" ? "anio" : "mes");
    });
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

    raiz.appendChild(barra);

    cuerpo = el("div", "cal-cuerpo");
    raiz.appendChild(cuerpo);

    pane.appendChild(raiz);
    pintar(null);

    // flechas del teclado: comodo para hojear meses
    raiz.addEventListener("keydown", function (ev) {
      if (ev.key === "ArrowLeft") { mover(-1); }
      else if (ev.key === "ArrowRight") { mover(1); }
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

  /* ---------- dibujo ---------- */

  function pintar(desde) {
    if (!raiz) { return; }

    titulo.innerHTML = "";
    if (estado.modo === "mes") {
      titulo.appendChild(el("span", "cal-titulo-mes", MESES[estado.mes]));
      titulo.appendChild(el("span", "cal-titulo-anio", String(estado.anio)));
      titulo.title = "Ver todo " + estado.anio;
    } else {
      titulo.appendChild(el("span", "cal-titulo-mes", String(estado.anio)));
      titulo.title = "Volver a un solo mes";
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
    (cortos ? DIAS_MINI : DIAS_CORTO).forEach(function (d, i) {
      var c = el("span", "cal-dia-sem" + (i > 4 ? " es-finde" : ""), d);
      if (!cortos) { c.title = DIAS[i]; }
      fila.appendChild(c);
    });
    return fila;
  }

  function esHoy(anio, mes, dia) {
    var h = hoy();
    return h.a === anio && h.m === mes && h.d === dia;
  }

  function vistaMes(anio, mes) {
    var caja = el("div", "cal-mes");
    caja.appendChild(cabeceraSemana(false));

    var grilla = el("div", "cal-grilla");
    casillas(anio, mes).forEach(function (c) {
      var clase = "cal-dia";
      if (c.otro) { clase += " es-otro"; }
      if (c.semana > 4) { clase += " es-finde"; }
      if (!c.otro && esHoy(anio, mes, c.n)) { clase += " es-hoy"; }

      var d = el("div", clase);
      d.appendChild(el("span", "cal-num", String(c.n)));
      if (!c.otro && esHoy(anio, mes, c.n)) { d.appendChild(el("span", "cal-etq-hoy", "hoy")); }
      grilla.appendChild(d);
    });

    caja.appendChild(grilla);
    return caja;
  }

  function vistaAnio(anio) {
    var caja = el("div", "cal-anio");
    for (var m = 0; m < 12; m++) {
      caja.appendChild(mini(anio, m));
    }
    return caja;
  }

  function mini(anio, mes) {
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
      if (!c.otro && esHoy(anio, mes, c.n)) { clase += " es-hoy"; }
      grilla.appendChild(el("span", clase, String(c.n)));
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

  window.NC.cal = { montar: montar };
})();
