/* ============================================================
   NEWCAMPUS - detalle de un dia del calendario
   ------------------------------------------------------------
   La ventana sobrepuesta que sale al hacer clic en un dia. Tiene dos
   pantallas dentro de la misma ficha:

     DETALLE   lo que hay ese dia: fechas academicas fijas (feriados,
               mesas) y los parciales / trabajos practicos cargados,
               cada uno con sus botones de editar y eliminar.
     FORMULARIO  para agregar una fecha nueva o corregir una que ya esta.

   Se cierra con la ✕, con Escape o tocando fuera de la ficha.
   Despues de cada cambio se le avisa al calendario para que se redibuje.
   ============================================================ */

window.NC = window.NC || {};

(function () {
  "use strict";

  var EV = null;               // window.NC.calEventos, se toma al abrir
  var capa = null;             // la capa oscura que tapa la pagina
  var ficha = null;
  var cuerpo = null;
  var cabecera = null;

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

  function avisar() {
    if (window.NC.cal && window.NC.cal.refrescar) { window.NC.cal.refrescar(); }
  }

  /* ---------- la ficha ---------- */

  function cerrar() {
    if (!capa) { return; }
    document.removeEventListener("keydown", porTecla, true);
    if (capa.parentNode) { capa.parentNode.removeChild(capa); }
    capa = ficha = cuerpo = cabecera = null;
  }

  function porTecla(ev) {
    if (ev.key === "Escape") { ev.stopPropagation(); cerrar(); }
  }

  function abrirFicha() {
    if (capa) { cerrar(); }

    capa = el("div", "cal-capa");
    capa.addEventListener("mousedown", function (ev) {
      if (ev.target === capa) { cerrar(); }   // tocar fuera de la ficha
    });

    ficha = el("div", "cal-ficha");
    ficha.setAttribute("role", "dialog");
    ficha.setAttribute("aria-modal", "true");

    cabecera = el("div", "cal-ficha-cab");
    cuerpo = el("div", "cal-ficha-cuerpo");

    ficha.appendChild(cabecera);
    ficha.appendChild(cuerpo);
    capa.appendChild(ficha);
    document.body.appendChild(capa);

    document.addEventListener("keydown", porTecla, true);
  }

  function titular(titulo, bajada) {
    cabecera.innerHTML = "";
    var textos = el("div", "cal-ficha-tit");
    textos.appendChild(el("span", "cal-ficha-dia", titulo));
    if (bajada) { textos.appendChild(el("span", "cal-ficha-sub", bajada)); }
    cabecera.appendChild(textos);
    cabecera.appendChild(boton("cal-ficha-x", "✕", cerrar));
  }

  /* ============================================================
     PANTALLA 1: que hay este dia
     ============================================================ */

  function abrir(fecha) {
    EV = window.NC.calEventos;
    if (!EV) { return; }
    abrirFicha();
    pintarDia(fecha);
  }

  function pintarDia(fecha) {
    var p = EV.partes(fecha);
    titular(EV.largo(fecha).replace(/^./, function (c) { return c.toUpperCase(); }),
            null);

    cuerpo.innerHTML = "";

    var fijas = EV.academicas(fecha);
    fijas.forEach(function (f) {
      var caja = el("div", "cal-fija cal-fija-" + f.tipo);
      caja.appendChild(el("span", "cal-fija-etq", etiquetaFija(f.tipo)));
      caja.appendChild(el("strong", "cal-fija-tit", f.titulo));
      if (f.detalle) { caja.appendChild(el("p", "cal-fija-txt", f.detalle)); }
      if (f.desde !== (f.hasta || f.desde)) {
        caja.appendChild(el("p", "cal-fija-txt", "Del " + EV.largo(f.desde) + " al " + EV.largo(f.hasta) + "."));
      }
      cuerpo.appendChild(caja);
    });

    var eventos = EV.delDia(fecha);
    if (!eventos.length && !fijas.length) {
      cuerpo.appendChild(el("p", "cal-vacio", "No hay nada anotado este día."));
    }

    eventos.forEach(function (e) { cuerpo.appendChild(tarjeta(e)); });

    var pie = el("div", "cal-ficha-pie");
    pie.appendChild(boton("cal-btn cal-btn-primario", "+ Agregar fecha", function () {
      pintarFormulario(null, fecha);
    }));
    cuerpo.appendChild(pie);
  }

  function etiquetaFija(tipo) {
    return tipo === "feriado" ? "Feriado"
      : tipo === "mesas" ? "Mesas de examen"
      : "Sin actividad";
  }

  function tarjeta(e) {
    var mat = EV.materia(e.materia);
    var tipo = EV.TIPOS[e.tipo];

    var caja = el("div", "cal-tarjeta");
    caja.style.setProperty("--h", mat.tono);

    var cab = el("div", "cal-tarjeta-cab");
    var chapa = el("span", "cal-tarjeta-tipo");
    chapa.appendChild(el("span", "cal-tarjeta-glifo", tipo.glifo));
    chapa.appendChild(document.createTextNode(tipo.nombre));
    cab.appendChild(chapa);
    caja.appendChild(cab);

    caja.appendChild(el("strong", "cal-tarjeta-materia", mat.nombre));

    if (e.unidades.length) {
      var us = el("div", "cal-tarjeta-unidades");
      e.unidades.forEach(function (u) {
        var datos = EV.unidad(e.materia, u);
        var chip = el("span", "cal-chip-unidad", datos.nombre);
        if (datos.tema) { chip.title = datos.tema; }
        us.appendChild(chip);
      });
      caja.appendChild(us);
    }

    if (e.nota) { caja.appendChild(el("p", "cal-tarjeta-nota", e.nota)); }

    var acciones = el("div", "cal-tarjeta-acciones");
    acciones.appendChild(boton("cal-btn cal-btn-chico", "Editar", function () {
      pintarFormulario(e, e.fecha);
    }));
    acciones.appendChild(boton("cal-btn cal-btn-chico cal-btn-borrar", "Eliminar", function () {
      confirmarBorrado(e);
    }));
    caja.appendChild(acciones);

    return caja;
  }

  function confirmarBorrado(e) {
    var mat = EV.materia(e.materia);
    var texto = EV.TIPOS[e.tipo].nombre + " de " + mat.nombre + ", " + EV.largo(e.fecha) + ".";
    var borrar = function () {
      var fecha = e.fecha;
      EV.borrar(e.id);
      avisar();
      pintarDia(fecha);
    };

    if (window.NC.eval && window.NC.eval.dialogo) {
      window.NC.eval.dialogo({
        titulo: "¿Eliminar esta fecha?",
        texto: texto + " Se borra del calendario y no se puede deshacer.",
        botones: [{ texto: "Cancelar" }, { texto: "Eliminar", clase: "ev-btn-rojo", accion: borrar }]
      });
    } else if (window.confirm("¿Eliminar esta fecha?\n\n" + texto)) { borrar(); }
  }

  /* ============================================================
     PANTALLA 2: alta y edicion
     ============================================================ */

  function campo(etiqueta, ayuda) {
    var c = el("div", "cal-campo");
    c.appendChild(el("span", "cal-campo-etq", etiqueta));
    if (ayuda) { c.appendChild(el("span", "cal-campo-ayuda", ayuda)); }
    return c;
  }

  function pintarFormulario(evento, fecha) {
    var editando = !!evento;
    titular(editando ? "Editar fecha" : "Nueva fecha",
            editando ? null : EV.largo(fecha));

    cuerpo.innerHTML = "";
    var form = el("form", "cal-form");

    /* --- tipo --- */
    var cTipo = campo("Qué es");
    var tipos = el("div", "cal-opciones");
    var tipoElegido = evento ? evento.tipo : "parcial";

    Object.keys(EV.TIPOS).forEach(function (clave) {
      var b = boton("cal-opcion", "", function () {
        tipoElegido = clave;
        Array.prototype.forEach.call(tipos.children, function (x) {
          x.classList.toggle("is-elegida", x.getAttribute("data-tipo") === clave);
        });
      });
      b.setAttribute("data-tipo", clave);
      b.appendChild(el("span", "cal-opcion-glifo", EV.TIPOS[clave].glifo));
      b.appendChild(document.createTextNode(EV.TIPOS[clave].nombre));
      b.classList.toggle("is-elegida", clave === tipoElegido);
      tipos.appendChild(b);
    });
    cTipo.appendChild(tipos);
    form.appendChild(cTipo);

    /* --- materia --- */
    var cMateria = campo("Materia");
    var select = el("select", "cal-select");
    var vacia = el("option", null, "Elegí una materia");
    vacia.value = "";
    select.appendChild(vacia);

    EV.materias().forEach(function (m) {
      var o = el("option", null, m.nombre);
      o.value = m.clave;
      select.appendChild(o);
    });
    select.value = evento ? evento.materia : "";
    cMateria.appendChild(select);
    form.appendChild(cMateria);

    /* --- unidades (se habilitan al elegir materia) --- */
    var cUnidades = campo("Unidades que entran", "opcional");
    var caja = el("div", "cal-unidades");
    cUnidades.appendChild(caja);
    form.appendChild(cUnidades);

    function pintarUnidades() {
      caja.innerHTML = "";
      var clave = select.value;
      if (!clave) {
        caja.appendChild(el("p", "cal-unidades-aviso", "Elegí primero la materia."));
        return;
      }
      var mat = EV.materia(clave);
      if (!mat.unidades.length) {
        caja.appendChild(el("p", "cal-unidades-aviso", "Esta materia todavía no tiene unidades cargadas en el campus."));
        return;
      }
      mat.unidades.forEach(function (u) {
        var et = el("label", "cal-unidad");
        var chk = document.createElement("input");
        chk.type = "checkbox";
        chk.value = u.clave;
        if (evento && evento.materia === clave && evento.unidades.indexOf(u.clave) !== -1) {
          chk.checked = true;
        }
        et.appendChild(chk);
        et.appendChild(el("span", "cal-unidad-num", u.nombre));
        et.appendChild(el("span", "cal-unidad-tema", u.tema));
        caja.appendChild(et);
      });
    }

    select.addEventListener("change", pintarUnidades);
    pintarUnidades();

    /* --- fecha --- */
    var cFecha = campo("Día");
    var entrada = document.createElement("input");
    entrada.type = "date";
    entrada.className = "cal-fecha";
    entrada.value = evento ? evento.fecha : fecha;
    cFecha.appendChild(entrada);
    form.appendChild(cFecha);

    /* --- descripcion --- */
    var cNota = campo("Descripción", "opcional");
    var nota = el("textarea", "cal-nota");
    nota.rows = 3;
    nota.placeholder = "Ej: entra todo lo visto hasta la clase del 15, se puede usar la tabla.";
    nota.value = evento ? evento.nota : "";
    cNota.appendChild(nota);
    form.appendChild(cNota);

    var error = el("p", "cal-error", "");
    error.hidden = true;
    form.appendChild(error);

    /* --- pie --- */
    var pie = el("div", "cal-ficha-pie");
    pie.appendChild(boton("cal-btn", "Cancelar", function () {
      pintarDia(evento ? evento.fecha : fecha);
    }));
    pie.appendChild(boton("cal-btn cal-btn-primario", editando ? "Guardar cambios" : "Agregar", function () {
      guardar();
    }));
    form.appendChild(pie);

    form.addEventListener("submit", function (ev) { ev.preventDefault(); guardar(); });
    cuerpo.appendChild(form);

    function guardar() {
      var datos = {
        tipo: tipoElegido,
        materia: select.value,
        unidades: Array.prototype.slice.call(caja.querySelectorAll("input:checked")).map(function (c) { return c.value; }),
        fecha: entrada.value,
        nota: nota.value.trim()
      };

      if (!datos.materia) { return fallar("Elegí de qué materia es."); }
      if (!/^\d{4}-\d{2}-\d{2}$/.test(datos.fecha)) { return fallar("Poné el día."); }

      if (editando) { EV.actualizar(evento.id, datos); }
      else { EV.agregar(datos); }

      avisar();
      pintarDia(datos.fecha);
    }

    function fallar(texto) {
      error.textContent = texto;
      error.hidden = false;
    }
  }

  window.NC.calDetalle = { abrir: abrir, cerrar: cerrar };
})();
