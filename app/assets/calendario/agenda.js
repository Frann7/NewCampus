/* ============================================================
   NEWCAMPUS - proximas fechas y recordatorios
   ------------------------------------------------------------
   Tres cosas que comparten la misma cuenta regresiva:

     AGENDA        el indice de la derecha del calendario. Filas cortas,
                   agrupadas por mes, con un filtro arriba (todo / parciales
                   / practicos). Al tocar una fila el calendario salta a ese
                   dia.
     RECORDATORIOS el bloque desplegable del final: una casilla por materia
                   (no por fecha, que era lo que alargaba la lista) mas el
                   interruptor general. Nada se aplica hasta tocar Aceptar.
     AVISOS        al entrar al campus, un aviso por materia arriba a la
                   derecha con TODAS las fechas que esa materia tiene por
                   delante, unos segundos cada uno, y se van solos.

   Configuracion de avisos en localStorage "newcampus:avisos":

     { activo: true, apagadas: ["bd", "emp"] }

   Se guardan las materias APAGADAS, no las encendidas: asi una materia
   nueva avisa sin tener que tocar nada.
   El filtro y si el bloque de recordatorios quedo abierto van en
   "newcampus:agenda".
   ============================================================ */

window.NC = window.NC || {};

(function () {
  "use strict";

  var CLAVE = "newcampus:avisos";
  var CLAVE_VISTA = "newcampus:agenda";
  var HORIZONTE = 365;      // dias hacia adelante que mira la agenda
  var EN_AGENDA = 40;       // tope de filas listadas
  var MAX_AVISOS = 12;      // tope de materias que avisan al entrar
  var EN_AVISO = 5;         // fechas que entran en el aviso de una materia
  var DURA_AVISO = 4000;    // cuanto dura en pantalla un aviso de una sola fecha
  var REFRESCO = 30000;     // cada cuanto se recalcula "cuanto falta"

  var DIA = 86400000;
  var HORA = 3600000;

  // Los desplegables cambian el caracter de la flecha, no la rotan por CSS
  var FLECHA_ABIERTA = "▼";
  var FLECHA_CERRADA = "▶";

  function EV() { return window.NC.calEventos; }

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

  /* ---------- como quedo la vista ---------- */

  var vista = (function () {
    var g = null;
    try { g = JSON.parse(localStorage.getItem(CLAVE_VISTA) || "null"); } catch (e) {}
    return {
      filtro: (g && /^(todo|parcial|tp)$/.test(g.filtro)) ? g.filtro : "todo",
      avisosAbierto: !!(g && g.avisosAbierto)
    };
  })();

  function guardarVista() {
    try { localStorage.setItem(CLAVE_VISTA, JSON.stringify(vista)); } catch (e) {}
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

  /* Las casillas no escriben nada al toque: van a un borrador y recien se
     aplican con el boton Aceptar. Mientras tanto, lo que manda para los
     recordatorios sigue siendo lo ultimo aceptado. */

  var borrador = null;      // null = no hay cambios sin aplicar

  function mostrado() { return borrador || config(); }
  function hayCambios() { return !!borrador; }

  function abrirBorrador() {
    if (!borrador) {
      var c = config();
      borrador = { activo: c.activo, apagadas: c.apagadas.slice() };
    }
    return borrador;
  }

  function cambiarMateria(materia, avisar) {
    var b = abrirBorrador();
    var i = b.apagadas.indexOf(materia);
    if (avisar && i !== -1) { b.apagadas.splice(i, 1); }
    if (!avisar && i === -1) { b.apagadas.push(materia); }
  }

  function cambiarGeneral(activo) {
    abrirBorrador().activo = !!activo;
  }

  function aplicar() {
    if (!borrador) { return; }
    guardarConfig(borrador);
    borrador = null;
  }

  function descartar() { borrador = null; }

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

  // corto = la version que entra en una fila de la agenda ("10 d 6 h")
  function cuantoFalta(fecha, corto) {
    var hoy = hoyISO();
    if (fecha === hoy) { return { texto: corto ? "hoy" : "Es hoy", urgente: true }; }
    if (fecha < hoy) { return { texto: corto ? "pasó" : "Ya pasó", pasado: true }; }

    var ms = faltan(fecha);
    var dias = Math.floor(ms / DIA);
    var horas = Math.floor((ms % DIA) / HORA);

    if (dias >= 1) {
      return {
        texto: corto
          ? dias + " d" + (horas ? " " + horas + " h" : "")
          : (dias === 1 ? "Falta 1 día" : "Faltan " + dias + " días") + (horas ? " y " + horas + " h" : ""),
        urgente: dias <= 2
      };
    }
    if (horas >= 1) {
      return {
        texto: corto ? horas + " h" : (horas === 1 ? "Falta 1 h" : "Faltan " + horas + " h"),
        urgente: true
      };
    }
    return { texto: corto ? "menos de 1 h" : "Falta menos de una hora", urgente: true };
  }

  // Lo que viene, de hoy en adelante
  function proximos(limite, soloConAviso, tipo) {
    var hoy = hoyISO();
    var tope = new Date(ahoraArg() + HORIZONTE * DIA);
    var hasta = EV().iso(tope.getUTCFullYear(), tope.getUTCMonth(), tope.getUTCDate());

    return EV().lista()
      .filter(function (e) {
        if (e.fecha < hoy || e.fecha > hasta) { return false; }
        if (tipo && tipo !== "todo" && e.tipo !== tipo) { return false; }
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

  // Encabezado de grupo: "Septiembre" y, si no es de este anio, con el anio
  function tituloMes(fecha) {
    var p = EV().partes(fecha);
    var esteAnio = new Date(ahoraArg()).getUTCFullYear();
    return EV().MESES[p.mes] + (p.anio !== esteAnio ? " " + p.anio : "");
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

    panel.appendChild(el("span", "cal-agenda-tit", "Próximas fechas"));
    panel.appendChild(filtros());

    var lista = proximos(EN_AGENDA, false, vista.filtro);

    if (!lista.length) {
      panel.appendChild(el("p", "cal-agenda-vacio", vista.filtro === "todo"
        ? "No hay nada anotado. Agregá un parcial o un trabajo práctico con + Fecha."
        : "No hay nada de eso anotado."));
    } else {
      var grupo = null;
      var mesActual = "";
      lista.forEach(function (e) {
        var mes = tituloMes(e.fecha);
        if (mes !== mesActual) {
          mesActual = mes;
          panel.appendChild(el("span", "cal-agenda-mes", mes));
          grupo = el("div", "cal-agenda-grupo");
          panel.appendChild(grupo);
        }
        grupo.appendChild(fila(e));
      });
    }

    panel.appendChild(bloqueAvisos());
  }

  function filtros() {
    var caja = el("div", "cal-agenda-filtros");
    [["todo", "Todo"], ["parcial", "Parciales"], ["tp", "Prácticos"]].forEach(function (f) {
      var b = boton("cal-filtro", f[1], function () {
        vista.filtro = f[0];
        guardarVista();
        pintar();
      });
      b.classList.toggle("is-activo", vista.filtro === f[0]);
      caja.appendChild(b);
    });
    return caja;
  }

  // Una fila = el nombre arriba, el dia y cuanto falta abajo
  function fila(e) {
    var mat = EV().materia(e.materia);
    var cuenta = cuantoFalta(e.fecha, true);

    var b = el("button", "cal-prox" + (e.tipo === "parcial" ? " es-parcial" : " es-tp"));
    b.type = "button";
    b.style.setProperty("--h", mat.tono);
    b.title = EV().TIPOS[e.tipo].nombre + " de " + mat.nombre + " · " + EV().largo(e.fecha) +
      (e.unidades.length ? " · " + e.unidades.map(function (u) {
        return EV().unidad(e.materia, u).nombre;
      }).join(", ") : "");

    var arriba = el("span", "cal-prox-arriba");
    arriba.appendChild(el("span", "cal-prox-glifo", EV().TIPOS[e.tipo].glifo));
    arriba.appendChild(el("span", "cal-prox-materia", mat.nombre));
    b.appendChild(arriba);

    var abajo = el("span", "cal-prox-abajo");
    abajo.appendChild(el("span", "cal-prox-fecha", fechaCorta(e.fecha)));
    abajo.appendChild(el("span", "cal-prox-falta" + (cuenta.urgente ? " es-urgente" : ""), cuenta.texto));
    b.appendChild(abajo);

    b.addEventListener("click", function () {
      if (window.NC.cal && window.NC.cal.irA) { window.NC.cal.irA(e.fecha); }
    });
    return b;
  }

  /* ---------- bloque de recordatorios ---------- */

  function bloqueAvisos() {
    var c = mostrado();
    var caja = el("div", "cal-avisos");

    var cab = el("button", "cal-avisos-cab");
    cab.type = "button";
    cab.setAttribute("aria-expanded", String(vista.avisosAbierto));
    cab.appendChild(el("span", "cal-avisos-chev", vista.avisosAbierto ? FLECHA_ABIERTA : FLECHA_CERRADA));
    cab.appendChild(el("span", "cal-avisos-tit", "Recordatorios"));
    cab.appendChild(el("span", "cal-avisos-estado", c.activo ? "activados" : "apagados"));
    cab.addEventListener("click", function () {
      vista.avisosAbierto = !vista.avisosAbierto;
      guardarVista();
      pintar();
    });
    caja.appendChild(cab);

    if (!vista.avisosAbierto) { return caja; }

    var cuerpo = el("div", "cal-avisos-cuerpo");
    cuerpo.appendChild(el("p", "cal-avisos-ayuda",
      "Al entrar al campus te aviso cuánto falta para lo que viene."));

    cuerpo.appendChild(casilla("Recordarme al entrar", c.activo, false, function (marcada) {
      cambiarGeneral(marcada);
    }, "cal-avisos-general"));

    // Una casilla por materia, no por fecha: el aviso siempre fue por materia.
    var vistas = {};
    proximos(EN_AGENDA, false, "todo").forEach(function (e) {
      if (vistas[e.materia]) { return; }
      vistas[e.materia] = true;
      var mat = EV().materia(e.materia);
      cuerpo.appendChild(casilla(mat.nombre, c.apagadas.indexOf(e.materia) === -1, !c.activo,
        function (marcada) { cambiarMateria(e.materia, marcada); }, "cal-avisos-materia", mat.tono));
    });

    if (!Object.keys(vistas).length) {
      cuerpo.appendChild(el("p", "cal-avisos-ayuda", "Todavía no hay materias con fechas anotadas."));
    }

    if (hayCambios()) { cuerpo.appendChild(barraCambios()); }
    caja.appendChild(cuerpo);
    return caja;
  }

  // Solo la casilla marca y desmarca: el texto de al lado no hace nada.
  function casilla(texto, marcada, apagada, alCambiar, clase, tono) {
    var fila = el("span", "cal-casilla " + (clase || ""));
    if (tono !== undefined) { fila.style.setProperty("--h", tono); }

    var chk = document.createElement("input");
    chk.type = "checkbox";
    chk.checked = marcada;
    chk.disabled = !!apagada;
    chk.setAttribute("aria-label", texto);
    chk.addEventListener("change", function () {
      alCambiar(chk.checked);
      pintar();
    });

    fila.appendChild(chk);
    fila.appendChild(el("span", "cal-casilla-txt", texto));
    return fila;
  }

  function barraCambios() {
    var barra = el("div", "cal-agenda-cambios");
    barra.appendChild(el("span", "cal-agenda-cambios-txt", "Cambios sin aplicar"));

    var botones = el("div", "cal-agenda-cambios-btns");
    botones.appendChild(boton("cal-btn cal-btn-chico", "Descartar", function () { descartar(); pintar(); }));
    botones.appendChild(boton("cal-btn cal-btn-chico cal-btn-primario", "Aceptar", function () { aplicar(); pintar(); }));
    barra.appendChild(botones);
    return barra;
  }

  /* ============================================================
     AVISOS DEL ARRANQUE
     ------------------------------------------------------------
     Uno por materia, arriba a la derecha, unos segundos cada uno y se
     van solos. Cada aviso lista TODAS las fechas que esa materia tiene
     por delante, no solo la mas proxima: si no, las otras no se veian
     en ningun lado.

     El que se esta viendo se cierra por reloj, no por el fin de una
     animacion: si el navegador no corre animaciones, igual pasa al
     siguiente.
     ============================================================ */

  // Agrupa lo que viene por materia, conservando el orden por fecha
  function porMateria(lista) {
    var vistas = {};
    var salida = [];
    lista.forEach(function (e) {
      if (!vistas[e.materia]) {
        vistas[e.materia] = { materia: e.materia, eventos: [] };
        salida.push(vistas[e.materia]);
      }
      vistas[e.materia].eventos.push(e);
    });
    return salida;
  }

  // Un aviso con tres fechas necesita mas tiempo en pantalla que uno con una
  function duracion(cuantas) {
    return Math.min(DURA_AVISO + (cuantas - 1) * 900, DURA_AVISO * 2);
  }

  var relojAviso = null;

  function limpiarAvisos() {
    if (relojAviso) { window.clearTimeout(relojAviso); relojAviso = null; }
    var pila = document.querySelector(".cal-avisos-pila");
    if (pila && pila.parentNode) { pila.parentNode.removeChild(pila); }
  }

  function recordatorio() {
    if (!EV() || !config().activo) { return; }
    var cola = porMateria(proximos(EN_AGENDA, true, "todo")).slice(0, MAX_AVISOS);
    if (!cola.length) { return; }

    limpiarAvisos();
    var pila = el("div", "cal-avisos-pila");
    document.body.appendChild(pila);

    (function siguiente(i) {
      if (i >= cola.length) { limpiarAvisos(); return; }

      var aviso = cartel(cola[i]);
      pila.appendChild(aviso);

      relojAviso = window.setTimeout(function () {
        if (aviso.parentNode) { aviso.parentNode.removeChild(aviso); }
        siguiente(i + 1);
      }, duracion(Math.min(cola[i].eventos.length, EN_AVISO)));
    })(0);
  }

  function cartel(item) {
    var mat = EV().materia(item.materia);

    var caja = el("aside", "cal-aviso");
    caja.setAttribute("role", "status");
    caja.style.setProperty("--h", mat.tono);

    var x = boton("cal-aviso-x", "✕", limpiarAvisos);
    x.title = "No mostrar el resto";
    caja.appendChild(x);

    caja.appendChild(el("span", "cal-aviso-materia", mat.nombre));

    item.eventos.slice(0, EN_AVISO).forEach(function (e) {
      var cuenta = cuantoFalta(e.fecha, false);

      var fila = el("button", "cal-aviso-fila");
      fila.type = "button";
      fila.title = "Ver el " + EV().largo(e.fecha) + " en el calendario";
      fila.appendChild(el("span", "cal-aviso-tipo",
        EV().TIPOS[e.tipo].glifo + " " + (e.tipo === "parcial" ? "Parcial" : "Trabajo práctico")));
      fila.appendChild(el("span", "cal-aviso-falta" + (cuenta.urgente ? " es-urgente" : ""),
        cuenta.texto + " · " + fechaCorta(e.fecha)));
      fila.addEventListener("click", function () {
        limpiarAvisos();
        irAlCalendario(e.fecha);
      });
      caja.appendChild(fila);
    });

    var resto = item.eventos.length - EN_AVISO;
    if (resto > 0) {
      caja.appendChild(el("span", "cal-aviso-mas",
        resto === 1 ? "y 1 fecha más de esta materia" : "y " + resto + " fechas más de esta materia"));
    }

    return caja;
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
