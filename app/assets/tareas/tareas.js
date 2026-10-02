/* ============================================================
   NEWCAMPUS - tareas
   ------------------------------------------------------------
   Un tablero de tres columnas: Pendientes, En proceso y Hecho.
   Uno solo para todo el campus (no depende de la materia ni de la
   unidad), igual que el calendario.

   Cada tarea es un cuadrito con texto. Se agrega al pie de cada
   columna, se edita con el lapiz (o doble clic), se borra con la X y
   se pasa de columna con las flechas o arrastrandola; arrastrando
   tambien se reordena dentro de la misma columna.

   Una tarea puede ser de una materia (se elige al agregarla o editarla)
   y toma su color, el mismo que en el calendario. Sin materia, es una
   tarea general.

   Tope de MAXIMO tareas por columna y de MAX_TEXTO caracteres por
   tarea, para que el tablero no crezca sin fin: con la columna llena
   no se agrega ni se mueve nada a ella.

   Se guarda en el navegador (localStorage "newcampus:tareas"):
     { v: 1, columnas: { pendiente: [{ id, texto, materia, creado }], proceso: [...], hecho: [...] } }
   (materia es la clave del menu, "pye"; no esta si la tarea es general)
   ============================================================ */

window.NC = window.NC || {};

(function () {
  "use strict";

  var CLAVE = "newcampus:tareas";
  var MAXIMO = 25;        // tareas por columna
  var MAX_TEXTO = 300;    // caracteres por tarea

  var COLUMNAS = [
    { id: "pendiente", nombre: "Pendientes" },
    { id: "proceso", nombre: "En proceso" },
    { id: "hecho", nombre: "Hecho" }
  ];

  /* ---------- datos ---------- */

  function vacio() {
    var c = {};
    COLUMNAS.forEach(function (col) { c[col.id] = []; });
    return c;
  }

  // Lo guardado se revisa entero: una tarea rota o una columna de mas no
  // tienen que romper el tablero.
  function leer() {
    var g = null;
    try { g = JSON.parse(localStorage.getItem(CLAVE) || "null"); } catch (e) {}
    var c = vacio();
    if (!g || !g.columnas) { return c; }
    COLUMNAS.forEach(function (col) {
      var lista = g.columnas[col.id];
      if (!Array.isArray(lista)) { return; }
      lista.forEach(function (t) {
        if (!t || typeof t.texto !== "string" || !t.texto.trim()) { return; }
        if (c[col.id].length >= MAXIMO) { return; }
        var tarea = {
          id: typeof t.id === "string" ? t.id : nuevoId(),
          texto: t.texto.slice(0, MAX_TEXTO),
          creado: typeof t.creado === "number" ? t.creado : Date.now()
        };
        if (typeof t.materia === "string" && t.materia) { tarea.materia = t.materia; }
        c[col.id].push(tarea);
      });
    });
    return c;
  }

  function guardar() {
    try { localStorage.setItem(CLAVE, JSON.stringify({ v: 1, columnas: columnas })); } catch (e) {}
  }

  function nuevoId() {
    return "t" + Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
  }

  // Donde esta una tarea: { col, i }
  function ubicar(id) {
    for (var k = 0; k < COLUMNAS.length; k++) {
      var lista = columnas[COLUMNAS[k].id];
      for (var i = 0; i < lista.length; i++) {
        if (lista[i].id === id) { return { col: COLUMNAS[k].id, i: i }; }
      }
    }
    return null;
  }

  function nombreDe(colId) {
    return COLUMNAS.filter(function (c) { return c.id === colId; })[0].nombre;
  }

  function llena(colId) { return columnas[colId].length >= MAXIMO; }

  /* ---------- acciones ---------- */

  function agregar(colId, texto, materia) {
    texto = limpiar(texto);
    if (!texto || llena(colId)) { return false; }
    var tarea = { id: nuevoId(), texto: texto, creado: Date.now() };
    if (materia) { tarea.materia = materia; }
    columnas[colId].push(tarea);
    guardar();
    return true;
  }

  function editar(id, texto, materia) {
    texto = limpiar(texto);
    var u = ubicar(id);
    if (!u || !texto) { return; }
    var tarea = columnas[u.col][u.i];
    tarea.texto = texto;
    if (materia) { tarea.materia = materia; } else { delete tarea.materia; }
    guardar();
  }

  /* ---------- materias ----------
     Salen del menu lateral, igual que en el calendario (calendario/eventos.js),
     con el mismo tono de color para cada una. */

  function materias() {
    return window.NC.calEventos ? window.NC.calEventos.materias() : [];
  }

  function materiaDe(clave) {
    if (!clave || !window.NC.calEventos) { return null; }
    return window.NC.calEventos.materia(clave);
  }

  function borrar(id) {
    var u = ubicar(id);
    if (!u) { return; }
    columnas[u.col].splice(u.i, 1);
    guardar();
  }

  // Mueve la tarea a la columna destino, en la posicion pos (al final si no
  // se dice). Dentro de la misma columna solo la reordena.
  function mover(id, destino, pos) {
    var u = ubicar(id);
    if (!u) { return false; }
    if (u.col !== destino && llena(destino)) { avisarLlena(destino); return false; }
    var tarea = columnas[u.col].splice(u.i, 1)[0];
    var lista = columnas[destino];
    if (typeof pos !== "number" || pos > lista.length) { pos = lista.length; }
    if (u.col === destino && u.i < pos) { pos--; }
    lista.splice(pos, 0, tarea);
    guardar();
    return true;
  }

  function limpiar(texto) {
    return String(texto || "").replace(/\s+$/g, "").replace(/^\s+/g, "").slice(0, MAX_TEXTO);
  }

  function avisarLlena(colId) {
    dialogo("La columna " + nombreDe(colId) + " está llena",
      "Entran hasta " + MAXIMO + " tareas por columna. Borrá o mové alguna para hacer lugar.",
      [{ texto: "Aceptar", clase: "ev-btn-primario" }]);
  }

  // El cartel de confirmacion de la evaluacion; si no estuviera, el del navegador.
  function dialogo(titulo, texto, botones) {
    if (window.NC.eval && window.NC.eval.dialogo) {
      window.NC.eval.dialogo({ titulo: titulo, texto: texto, botones: botones });
      return;
    }
    var accion = botones.filter(function (b) { return b.accion; })[0];
    if (!accion) { window.alert(titulo + "\n\n" + texto); return; }
    if (window.confirm(titulo + "\n\n" + texto)) { accion.accion(); }
  }

  /* ---------- armado ---------- */

  function el(tag, clase, texto) {
    var e = document.createElement(tag);
    if (clase) { e.className = clase; }
    if (texto !== undefined) { e.textContent = texto; }
    return e;
  }

  function boton(clase, texto, titulo, fn) {
    var b = el("button", clase, texto);
    b.type = "button";
    if (titulo) { b.title = titulo; b.setAttribute("aria-label", titulo); }
    b.addEventListener("click", fn);
    return b;
  }

  var columnas = vacio();
  var raiz = null;
  var tablero = null;
  var editando = null;     // id de la tarea que se esta editando
  var agregando = null;    // columna con el formulario de alta abierto
  var arrastre = null;     // { id, col } mientras se arrastra una tarea

  function montar(pane) {
    columnas = leer();
    raiz = el("div", "tr tex2jax_ignore");

    var barra = el("div", "tr-barra");
    barra.appendChild(el("div", "tr-titulo", "Tareas"));
    raiz.appendChild(barra);

    tablero = el("div", "tr-tablero");
    raiz.appendChild(tablero);
    pane.appendChild(raiz);
    dibujar();

    // Una ventana copia (o la principal, si se cambia en la copia) se entera
    // de lo que cambio la otra.
    window.addEventListener("storage", function (ev) {
      if (ev.key !== CLAVE || editando || agregando) { return; }
      columnas = leer();
      dibujar();
    });
  }

  function dibujar() {
    if (!tablero) { return; }
    tablero.innerHTML = "";
    COLUMNAS.forEach(function (col, k) { tablero.appendChild(columna(col, k)); });
  }

  function columna(col, k) {
    var lista = columnas[col.id];
    var caja = el("section", "tr-col");
    caja.setAttribute("data-col", col.id);
    caja.setAttribute("aria-label", col.nombre);

    var cab = el("div", "tr-col-cab");
    cab.appendChild(el("span", "tr-col-nombre", col.nombre));
    var cuenta = el("span", "tr-cuenta" + (llena(col.id) ? " is-llena" : ""), lista.length + " / " + MAXIMO);
    cuenta.title = lista.length + " de " + MAXIMO + " tareas";
    cab.appendChild(cuenta);
    caja.appendChild(cab);

    var ul = el("ul", "tr-lista");
    lista.forEach(function (t) { ul.appendChild(tarjeta(t, col.id, k)); });
    caja.appendChild(ul);
    prepararSoltar(ul, col.id);

    if (agregando === col.id) {
      caja.appendChild(formAlta(col.id));
    } else if (llena(col.id)) {
      caja.appendChild(el("p", "tr-llena", "Columna llena: entran hasta " + MAXIMO + " tareas."));
    } else {
      caja.appendChild(boton("tr-agregar", "+ Agregar tarea", "", function () {
        agregando = col.id;
        editando = null;
        dibujar();
      }));
    }
    return caja;
  }

  function tarjeta(t, colId, k) {
    var li = el("li", "tr-tarea");
    li.setAttribute("data-id", t.id);

    if (editando === t.id) {
      li.classList.add("is-editando");
      li.appendChild(campoTexto(t.texto, t.materia || "", "Guardar", function (texto, materia) {
        editando = null;
        if (texto) { editar(t.id, texto, materia); }
        dibujar();
      }, function () { editando = null; dibujar(); }));
      return li;
    }

    li.draggable = true;
    var mat = materiaDe(t.materia);
    if (mat) {
      li.classList.add("con-materia");
      li.style.setProperty("--h", mat.tono);
      var chip = el("span", "tr-chip", mat.corto);
      chip.title = mat.nombre;
      li.appendChild(chip);
    }
    var texto = el("p", "tr-texto", t.texto);
    texto.addEventListener("dblclick", function () { empezarEdicion(t.id); });
    li.appendChild(texto);

    var acciones = el("div", "tr-acciones");
    var anterior = COLUMNAS[k - 1], siguiente = COLUMNAS[k + 1];
    if (anterior) {
      acciones.appendChild(boton("tr-btn", "←", "Pasar a " + anterior.nombre, function () {
        if (mover(t.id, anterior.id)) { dibujar(); }
      }));
    }
    if (siguiente) {
      acciones.appendChild(boton("tr-btn", "→", "Pasar a " + siguiente.nombre, function () {
        if (mover(t.id, siguiente.id)) { dibujar(); }
      }));
    }
    acciones.appendChild(boton("tr-btn", "✎", "Editar", function () { empezarEdicion(t.id); }));
    acciones.appendChild(boton("tr-btn tr-btn-borrar", "✕", "Borrar", function () {
      dialogo("¿Borrar esta tarea?", t.texto, [
        { texto: "Cancelar" },
        { texto: "Borrar", clase: "ev-btn-rojo", accion: function () { borrar(t.id); dibujar(); } }
      ]);
    }));
    li.appendChild(acciones);

    li.addEventListener("dragstart", function (ev) {
      arrastre = { id: t.id, col: colId };
      li.classList.add("is-arrastrada");
      try {
        ev.dataTransfer.effectAllowed = "move";
        ev.dataTransfer.setData("text/plain", t.id);
      } catch (e) {}
    });
    li.addEventListener("dragend", function () {
      arrastre = null;
      li.classList.remove("is-arrastrada");
      sacarHueco();
    });
    return li;
  }

  function empezarEdicion(id) {
    editando = id;
    agregando = null;
    dibujar();
  }

  // La materia elegida queda puesta para la siguiente tarea que se cargue
  // seguida; al cerrar el formulario vuelve a "Sin materia".
  var materiaAlta = "";

  function formAlta(colId) {
    var caja = el("div", "tr-alta");
    caja.appendChild(campoTexto("", materiaAlta, "Agregar", function (texto, materia) {
      materiaAlta = materia;
      if (texto) { agregar(colId, texto, materia); }
      // queda abierto para cargar otra seguida, salvo que se haya llenado
      if (llena(colId) || !texto) { agregando = null; materiaAlta = ""; }
      dibujar();
    }, function () { agregando = null; materiaAlta = ""; dibujar(); }));
    return caja;
  }

  // Un textarea con Cancelar, la materia y Guardar/Agregar. Enter confirma,
  // Shift+Enter baja de renglon y Escape cancela. aceptar(texto, materia).
  function campoTexto(inicial, materia, rotulo, aceptar, cancelar) {
    var caja = el("div", "tr-campo");
    var area = el("textarea", "tr-area");
    area.value = inicial;
    area.maxLength = MAX_TEXTO;
    area.rows = 2;
    area.placeholder = "Escribí la tarea…";
    caja.appendChild(area);

    var pie = el("div", "tr-campo-pie");
    var resta = el("span", "tr-resta");
    pie.appendChild(resta);
    pie.appendChild(boton("ev-btn ev-btn-chico", "Cancelar", "", cancelar));

    var elegir = el("select", "tr-materia");
    elegir.title = "Materia de la tarea";
    elegir.setAttribute("aria-label", "Materia de la tarea");
    var ninguna = el("option", "", "Sin materia");
    ninguna.value = "";
    elegir.appendChild(ninguna);
    var hayElegida = false;
    materias().forEach(function (m) {
      var o = el("option", "", m.nombre);
      o.value = m.clave;
      if (m.clave === materia) { hayElegida = true; }
      elegir.appendChild(o);
    });
    elegir.value = hayElegida ? materia : "";
    function pintarMateria() {
      var m = materiaDe(elegir.value);
      elegir.classList.toggle("con-materia", !!m);
      if (m) { elegir.style.setProperty("--h", m.tono); } else { elegir.style.removeProperty("--h"); }
    }
    elegir.addEventListener("change", function () { pintarMateria(); area.focus(); });
    pintarMateria();
    pie.appendChild(elegir);

    function confirmar() { aceptar(limpiar(area.value), elegir.value); }
    var ok = boton("ev-btn ev-btn-chico tr-ok", rotulo, "", confirmar);
    pie.appendChild(ok);
    caja.appendChild(pie);

    function ajustar() {
      area.style.height = "auto";
      area.style.height = area.scrollHeight + 2 + "px";
      var quedan = MAX_TEXTO - area.value.length;
      resta.textContent = quedan <= 50 ? quedan + " caracteres" : "";
      ok.disabled = !limpiar(area.value);
    }
    area.addEventListener("input", ajustar);
    area.addEventListener("keydown", function (ev) {
      if (ev.key === "Enter" && !ev.shiftKey) {
        ev.preventDefault();
        if (limpiar(area.value)) { confirmar(); }
      } else if (ev.key === "Escape") {
        ev.preventDefault();
        cancelar();
      }
    });
    window.setTimeout(function () {
      ajustar();
      area.focus();
      area.setSelectionRange(area.value.length, area.value.length);
    }, 0);
    return caja;
  }

  /* ---------- arrastrar y soltar ----------
     Mientras se arrastra, una linea (el "hueco") marca donde va a caer la
     tarea. Sobre una columna llena no se puede soltar (salvo que la tarea ya
     sea de esa columna: ahi solo se reordena). */

  var hueco = null;

  function sacarHueco() {
    if (hueco && hueco.parentNode) { hueco.parentNode.removeChild(hueco); }
    $$(".tr-col.is-encima, .tr-col.is-rechaza").forEach(function (c) {
      c.classList.remove("is-encima", "is-rechaza");
    });
  }

  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  // Cuantas tareas (sin contar la que se arrastra) quedan arriba del puntero
  function posicion(ul, y) {
    var tareas = $$(".tr-tarea", ul);
    var pos = 0;
    for (var i = 0; i < tareas.length; i++) {
      var r = tareas[i].getBoundingClientRect();
      if (y > r.top + r.height / 2) { pos = i + 1; }
    }
    return pos;
  }

  function prepararSoltar(ul, colId) {
    var caja = ul.parentNode;
    function permitido() { return arrastre && (arrastre.col === colId || !llena(colId)); }

    function encima(ev) {
      if (!arrastre) { return; }
      if (!permitido()) {
        sacarHueco();
        caja.classList.add("is-rechaza");
        return;
      }
      ev.preventDefault();
      try { ev.dataTransfer.dropEffect = "move"; } catch (e) {}
      $$(".tr-col.is-encima").forEach(function (c) { if (c !== caja) { c.classList.remove("is-encima"); } });
      caja.classList.add("is-encima");
      if (!hueco) { hueco = el("li", "tr-hueco"); }
      var pos = posicion(ul, ev.clientY);
      var tareas = $$(".tr-tarea", ul);
      if (pos >= tareas.length) { ul.appendChild(hueco); } else { ul.insertBefore(hueco, tareas[pos]); }
    }

    function soltar(ev) {
      if (!arrastre || !permitido()) { return; }
      ev.preventDefault();
      // la posicion cuenta tambien la tarea que se arrastra si es de esta
      // columna, igual que la lista: mover() la corrige
      var pos = posicion(ul, ev.clientY);
      var id = arrastre.id;
      arrastre = null;
      sacarHueco();
      if (mover(id, colId, pos)) { dibujar(); }
    }

    caja.addEventListener("dragover", encima);
    caja.addEventListener("drop", soltar);
    caja.addEventListener("dragleave", function (ev) {
      if (ev.relatedTarget && caja.contains(ev.relatedTarget)) { return; }
      caja.classList.remove("is-encima", "is-rechaza");
      if (hueco && hueco.parentNode === ul) { ul.removeChild(hueco); }
    });
  }

  window.NC.tareas = {
    montar: montar,
    maximo: MAXIMO
  };
})();
