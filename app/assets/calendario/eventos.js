/* ============================================================
   NEWCAMPUS - fechas que carga el usuario en el calendario
   ------------------------------------------------------------
   Un evento es un parcial o un trabajo practico de una materia, en un
   dia, opcionalmente con las unidades que entran y una descripcion.

     { id, tipo:"parcial"|"tp", materia:"pye", unidades:["u4","u5"],
       fecha:"2026-09-30", nota:"", creado: <ms> }

   Se guardan en el navegador (localStorage "newcampus:eventos").

   Las materias NO se escriben aca: se leen del menu lateral de
   index.html, asi la lista es siempre la misma en todo el campus.
   Cada materia recibe un tono de color segun su lugar en ese menu.
   ============================================================ */

window.NC = window.NC || {};

(function () {
  "use strict";

  var CLAVE = "newcampus:eventos";
  var PASO_TONO = 40;          // separacion de color entre materias
  var TONO_BASE = 232;         // el indigo de la marca, para la primera

  var TIPOS = {
    parcial: { nombre: "Parcial", glifo: "★" },
    tp: { nombre: "Trabajo práctico", glifo: "✎" }
  };

  // Nombres compartidos por las dos vistas y por el detalle del dia
  var MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
               "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
  var DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];
  var DIAS_CORTO = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"];
  var DIAS_MINI = ["L", "M", "M", "J", "V", "S", "D"];

  function $$(sel, ctx) {
    return Array.prototype.slice.call((ctx || document).querySelectorAll(sel));
  }

  function texto(e) { return e ? e.textContent.replace(/\s+/g, " ").trim() : ""; }

  /* ---------- materias y unidades (salen del menu lateral) ---------- */

  function materias() {
    return $$(".materia").map(function (m, i) {
      var nombre = texto(m.querySelector(".m-nombre"));
      return {
        clave: m.getAttribute("data-materia"),
        nombre: nombre,
        corto: m.getAttribute("data-corto") || nombre.slice(0, 6),
        tono: (TONO_BASE + i * PASO_TONO) % 360,
        unidades: $$(".unidades button", m).map(function (b) {
          return {
            clave: b.getAttribute("data-unidad"),
            nombre: texto(b.querySelector(".u-num")),
            tema: texto(b.querySelector(".u-name"))
          };
        })
      };
    });
  }

  // Si una materia desaparece del menu, los eventos viejos no se rompen.
  function materia(clave) {
    var todas = materias();
    for (var i = 0; i < todas.length; i++) {
      if (todas[i].clave === clave) { return todas[i]; }
    }
    return { clave: clave, nombre: clave, corto: clave, tono: 0, unidades: [] };
  }

  function unidad(claveMateria, claveUnidad) {
    var u = materia(claveMateria).unidades;
    for (var i = 0; i < u.length; i++) {
      if (u[i].clave === claveUnidad) { return u[i]; }
    }
    return { clave: claveUnidad, nombre: claveUnidad, tema: "" };
  }

  /* ---------- guardado ---------- */

  function valido(e) {
    return e && typeof e.fecha === "string" && /^\d{4}-\d{2}-\d{2}$/.test(e.fecha) &&
           (e.tipo === "parcial" || e.tipo === "tp") && typeof e.materia === "string";
  }

  function lista() {
    var crudo = null;
    try { crudo = JSON.parse(localStorage.getItem(CLAVE) || "[]"); } catch (e) { return []; }
    if (!crudo || !crudo.length) { return []; }
    return crudo.filter(valido).map(function (e) {
      return {
        id: e.id || ("ev-" + Math.random().toString(36).slice(2)),
        tipo: e.tipo,
        materia: e.materia,
        unidades: Array.isArray(e.unidades) ? e.unidades : [],
        fecha: e.fecha,
        nota: typeof e.nota === "string" ? e.nota : "",
        creado: e.creado || 0
      };
    });
  }

  function escribir(todos) {
    try { localStorage.setItem(CLAVE, JSON.stringify(todos)); } catch (e) {}
  }

  function agregar(datos) {
    var todos = lista();
    var nuevo = {
      id: "ev-" + Date.now() + "-" + Math.random().toString(36).slice(2, 6),
      tipo: datos.tipo,
      materia: datos.materia,
      unidades: datos.unidades || [],
      fecha: datos.fecha,
      nota: datos.nota || "",
      creado: Date.now()
    };
    todos.push(nuevo);
    escribir(todos);
    return nuevo;
  }

  function actualizar(id, datos) {
    var todos = lista();
    for (var i = 0; i < todos.length; i++) {
      if (todos[i].id === id) {
        todos[i].tipo = datos.tipo;
        todos[i].materia = datos.materia;
        todos[i].unidades = datos.unidades || [];
        todos[i].fecha = datos.fecha;
        todos[i].nota = datos.nota || "";
        escribir(todos);
        return todos[i];
      }
    }
    return null;
  }

  function borrar(id) {
    escribir(lista().filter(function (e) { return e.id !== id; }));
  }

  function porId(id) {
    var todos = lista();
    for (var i = 0; i < todos.length; i++) {
      if (todos[i].id === id) { return todos[i]; }
    }
    return null;
  }

  /* ---------- consultas por fecha ---------- */

  function dosCifras(n) { return (n < 10 ? "0" : "") + n; }

  // anio, mes (0-11), dia  ->  "2026-09-30"
  function iso(anio, mes, dia) {
    return anio + "-" + dosCifras(mes + 1) + "-" + dosCifras(dia);
  }

  function partes(fecha) {
    var p = fecha.split("-");
    return { anio: +p[0], mes: +p[1] - 1, dia: +p[2] };
  }

  function ordenar(a, b) {
    if (a.fecha !== b.fecha) { return a.fecha < b.fecha ? -1 : 1; }
    if (a.tipo !== b.tipo) { return a.tipo === "parcial" ? -1 : 1; }
    return a.creado - b.creado;
  }

  function delDia(fecha) {
    return lista().filter(function (e) { return e.fecha === fecha; }).sort(ordenar);
  }

  // { "2026-09-30": [evento, ...] } para no recorrer la lista 42 veces
  function delMes(anio, mes) {
    var prefijo = anio + "-" + dosCifras(mes + 1) + "-";
    var mapa = {};
    lista().sort(ordenar).forEach(function (e) {
      if (e.fecha.indexOf(prefijo) !== 0) { return; }
      (mapa[e.fecha] = mapa[e.fecha] || []).push(e);
    });
    return mapa;
  }

  /* ---------- fechas academicas fijas (assets/calendario/fechas.js) ---------- */

  function academicas(fecha) {
    var fijas = window.NC.calFechas || [];
    return fijas.filter(function (f) {
      return f.desde <= fecha && fecha <= (f.hasta || f.desde);
    });
  }

  function hayAcademicas(anio, mes) {
    var fijas = window.NC.calFechas || [];
    var desde = iso(anio, mes, 1);
    var hasta = iso(anio, mes, 31);
    return fijas.some(function (f) {
      return (f.hasta || f.desde) >= desde && f.desde <= hasta;
    });
  }

  // "2026-09-30" -> "Miércoles 30 de septiembre de 2026"
  function largo(fecha) {
    var p = partes(fecha);
    var semana = (new Date(Date.UTC(p.anio, p.mes, p.dia)).getUTCDay() + 6) % 7;
    return DIAS[semana] + " " + p.dia + " de " + MESES[p.mes].toLowerCase() + " de " + p.anio;
  }

  window.NC.calEventos = {
    TIPOS: TIPOS,
    MESES: MESES,
    DIAS: DIAS,
    DIAS_CORTO: DIAS_CORTO,
    DIAS_MINI: DIAS_MINI,
    largo: largo,
    materias: materias,
    materia: materia,
    unidad: unidad,
    lista: lista,
    agregar: agregar,
    actualizar: actualizar,
    borrar: borrar,
    porId: porId,
    delDia: delDia,
    delMes: delMes,
    academicas: academicas,
    hayAcademicas: hayAcademicas,
    iso: iso,
    partes: partes
  };
})();
