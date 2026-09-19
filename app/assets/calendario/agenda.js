/* ============================================================
   NEWCAMPUS - proximas fechas y recordatorios
   ------------------------------------------------------------
   Dos cosas que comparten la misma cuenta regresiva:

     AGENDA        el indice de la derecha del calendario: los parciales y
                   trabajos practicos que vienen, cuanto falta para cada uno
                   y, al tocarlos, el calendario salta a ese dia.
     RECORDATORIO  el cartel que sale al entrar al campus con lo que se
                   viene. Se puede apagar entero o materia por materia desde
                   la casilla "Notificar" de cada fila de la agenda.

   La configuracion se guarda en localStorage "newcampus:avisos":

     { activo: true, apagadas: ["bd", "emp"] }

   Se guardan las materias APAGADAS, no las encendidas: asi una materia
   nueva avisa sin tener que tocar nada.
   ============================================================ */

window.NC = window.NC || {};

(function () {
  "use strict";

  var CLAVE = "newcampus:avisos";
  var HORIZONTE = 120;      // dias hacia adelante que mira la agenda
  var EN_AGENDA = 12;       // cuantas fechas se listan
  var EN_CARTEL = 4;        // cuantas entran en el recordatorio del arranque
  var REFRESCO = 30000;     // cada cuanto se recalcula "cuanto falta"

  var DIA = 86400000;
  var HORA = 3600000;

  function EV() { return window.NC.calEventos; }

  function el(tag, clase, texto) {
    var e = document.createElement(tag);
    if (clase) { e.className = clase; }
    if (texto !== undefined) { e.textContent = texto; }
    return e;
  }

  /* ---------- configuracion de avisos ---------- */

  function config() {
    var g = null;
    try { g = JSON.parse(localStorage.getItem(CLAVE) || "null"); } catch (e) {}
    return {
      activo: !g || g.activo !== false,
      apagadas: (g && Array.isArray(g.apagadas)) ? g.apagadas : []
    };
  }

  function guardarConfig(c) {
    try { localStorage.setItem(CLAVE, JSON.stringify(c)); } catch (e) {}
  }

  function avisaDe(materia) {
    var c = config();
    return c.activo && c.apagadas.indexOf(materia) === -1;
  }

  function cambiarMateria(materia, avisar) {
    var c = config();
    var i = c.apagadas.indexOf(materia);
    if (avisar && i !== -1) { c.apagadas.splice(i, 1); }
    if (!avisar && i === -1) { c.apagadas.push(materia); }
    guardarConfig(c);
  }

  function cambiarGeneral(activo) {
    var c = config();
    c.activo = !!activo;
    guardarConfig(c);
  }

  /* ---------- cuenta regresiva ---------- */

  // El "ahora" corrido a UTC-3, para que el dia cambie a la medianoche
  // de Argentina y no a la del navegador.
  function ahoraArg() { return Date.now() - 3 * HORA; }

  function hoyISO() {
    var d = new Date(ahoraArg());
    return EV().iso(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate());
  }

  // Milisegundos hasta la medianoche en que empieza ese dia
  function faltan(fecha) {
    var p = EV().partes(fecha);
    return Date.UTC(p.anio, p.mes, p.dia) - ahoraArg();
  }

  function cuantoFalta(fecha) {
    var hoy = hoyISO();
    if (fecha === hoy) { return { texto: "Es hoy", urgente: true }; }
    if (fecha < hoy) { return { texto: "Ya pasó", pasado: true }; }

    var ms = faltan(fecha);
    var dias = Math.floor(ms / DIA);
    var horas = Math.floor((ms % DIA) / HORA);

    if (dias >= 1) {
      return {
        texto: (dias === 1 ? "Falta 1 día" : "Faltan " + dias + " días") +
               (horas ? " y " + horas + " h" : ""),
        urgente: dias <= 2
      };
    }
    if (horas >= 1) {
      return { texto: (horas === 1 ? "Falta 1 h" : "Faltan " + horas + " h"), urgente: true };
    }
    return { texto: "Falta menos de una hora", urgente: true };
  }

  // Lo que viene, de hoy en adelante
  function proximos(limite, soloConAviso) {
    var hoy = hoyISO();
    var tope = new Date(ahoraArg() + HORIZONTE * DIA);
    var hasta = EV().iso(tope.getUTCFullYear(), tope.getUTCMonth(), tope.getUTCDate());

    return EV().lista()
      .filter(function (e) {
        if (e.fecha < hoy || e.fecha > hasta) { return false; }
        return !soloConAviso || avisaDe(e.materia);
      })
      .sort(function (a, b) {
        if (a.fecha !== b.fecha) { return a.fecha < b.fecha ? -1 : 1; }
        return a.tipo === "parcial" ? -1 : 1;
      })
      .slice(0, limite || EN_AGENDA);
  }

  function fechaCorta(fecha) {
    var p = EV().partes(fecha);
    var semana = (new Date(Date.UTC(p.anio, p.mes, p.dia)).getUTCDay() + 6) % 7;
    return EV().DIAS_CORTO[semana].toLowerCase() + " " + p.dia + " " +
           EV().MESES[p.mes].slice(0, 3).toLowerCase();
  }

  /* ============================================================
     AGENDA (el indice de la derecha)
     ============================================================ */

  var panel = null;
  var reloj = null;

  function montar(contenedor) {
    panel = contenedor;
    pintar();

    if (reloj) { window.clearInterval(reloj); }
    reloj = window.setInterval(function () {
      // solo si la pestania Calendario esta a la vista
      var pane = document.querySelector('.pane[data-view="calendario"]');
      if (pane && pane.classList.contains("is-active")) { pintar(); }
    }, REFRESCO);
  }

  function pintar() {
    if (!panel || !EV()) { return; }
    panel.innerHTML = "";

    var c = config();

    var cab = el("div", "cal-agenda-cab");
    cab.appendChild(el("span", "cal-agenda-tit", "Próximas fechas"));

    var general = el("label", "cal-agenda-switch");
    general.title = "Avisarme al entrar al campus";
    var chkGeneral = document.createElement("input");
    chkGeneral.type = "checkbox";
    chkGeneral.checked = c.activo;
    chkGeneral.addEventListener("change", function () {
      cambiarGeneral(chkGeneral.checked);
      pintar();
    });
    general.appendChild(chkGeneral);
    general.appendChild(el("span", null, "Recordarme al entrar"));
    cab.appendChild(general);
    panel.appendChild(cab);

    var lista = proximos(EN_AGENDA, false);
    if (!lista.length) {
      panel.appendChild(el("p", "cal-agenda-vacio",
        "No hay parciales ni trabajos prácticos anotados. Agregalos con + Fecha."));
      return;
    }

    lista.forEach(function (e) { panel.appendChild(fila(e, c)); });
  }

  function fila(e, c) {
    var mat = EV().materia(e.materia);
    var cuenta = cuantoFalta(e.fecha);

    var caja = el("div", "cal-prox" + (e.tipo === "parcial" ? " es-parcial" : " es-tp"));
    caja.style.setProperty("--h", mat.tono);

    var ir = el("button", "cal-prox-ir");
    ir.type = "button";
    ir.title = "Ver el " + EV().largo(e.fecha) + " en el calendario";

    var arriba = el("span", "cal-prox-arriba");
    arriba.appendChild(el("span", "cal-prox-tipo",
      EV().TIPOS[e.tipo].glifo + " " + (e.tipo === "parcial" ? "Parcial" : "TP")));
    arriba.appendChild(el("span", "cal-prox-fecha", fechaCorta(e.fecha)));
    ir.appendChild(arriba);

    ir.appendChild(el("span", "cal-prox-materia", mat.nombre));
    ir.appendChild(el("span", "cal-prox-falta" + (cuenta.urgente ? " es-urgente" : ""), cuenta.texto));

    if (e.unidades.length) {
      ir.appendChild(el("span", "cal-prox-unidades", e.unidades.map(function (u) {
        return EV().unidad(e.materia, u).nombre;
      }).join(" · ")));
    }

    ir.addEventListener("click", function () {
      if (window.NC.cal && window.NC.cal.irA) { window.NC.cal.irA(e.fecha); }
    });
    caja.appendChild(ir);

    // la casilla vale para toda la materia, no solo para esta fecha
    var avisar = el("label", "cal-prox-avisar");
    var chk = document.createElement("input");
    chk.type = "checkbox";
    chk.checked = c.activo && c.apagadas.indexOf(e.materia) === -1;
    chk.disabled = !c.activo;
    chk.addEventListener("change", function () {
      cambiarMateria(e.materia, chk.checked);
      pintar();
    });
    avisar.title = "Avisarme de las fechas de " + mat.nombre + " al entrar al campus";
    avisar.appendChild(chk);
    avisar.appendChild(el("span", null, "Notificar"));
    caja.appendChild(avisar);

    return caja;
  }

  /* ============================================================
     RECORDATORIO DEL ARRANQUE
     ============================================================ */

  function recordatorio() {
    if (!EV() || !config().activo) { return; }
    var lista = proximos(EN_CARTEL, true);
    if (!lista.length) { return; }

    var viejo = document.querySelector(".cal-recordatorio");
    if (viejo) { viejo.parentNode.removeChild(viejo); }

    var caja = el("aside", "cal-recordatorio");
    caja.setAttribute("role", "status");

    var cab = el("div", "cal-recordatorio-cab");
    cab.appendChild(el("span", "cal-recordatorio-tit", "Lo que se viene"));
    var x = el("button", "cal-recordatorio-x", "✕");
    x.type = "button";
    x.title = "Cerrar";
    x.addEventListener("click", function () { caja.parentNode.removeChild(caja); });
    cab.appendChild(x);
    caja.appendChild(cab);

    lista.forEach(function (e) {
      var mat = EV().materia(e.materia);
      var cuenta = cuantoFalta(e.fecha);

      var b = el("button", "cal-recordatorio-item");
      b.type = "button";
      b.style.setProperty("--h", mat.tono);
      b.appendChild(el("span", "cal-recordatorio-tipo",
        EV().TIPOS[e.tipo].glifo + " " + (e.tipo === "parcial" ? "Parcial" : "TP")));
      b.appendChild(el("span", "cal-recordatorio-materia", mat.nombre));
      b.appendChild(el("span", "cal-recordatorio-falta" + (cuenta.urgente ? " es-urgente" : ""),
        cuenta.texto + " · " + fechaCorta(e.fecha)));
      b.addEventListener("click", function () {
        caja.parentNode.removeChild(caja);
        irAlCalendario(e.fecha);
      });
      caja.appendChild(b);
    });

    document.body.appendChild(caja);
  }

  // Cambia a la pestania Calendario y para en ese dia
  function irAlCalendario(fecha) {
    var ruta = window.NC.rutaActual ? window.NC.rutaActual("calendario") : null;
    if (ruta && window.location.hash.slice(1) !== ruta) {
      window.location.hash = ruta;
    }
    window.setTimeout(function () {
      if (window.NC.cal && window.NC.cal.irA) { window.NC.cal.irA(fecha); }
    }, 60);
  }

  window.NC.calAgenda = {
    montar: montar,
    pintar: pintar,
    recordatorio: recordatorio,
    cuantoFalta: cuantoFalta,
    proximos: proximos,
    avisaDe: avisaDe
  };
})();
