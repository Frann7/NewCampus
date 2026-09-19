/* ============================================================
   NEWCAMPUS - Evaluacion: nucleo
   Utilidades compartidas, guardado de autoevaluaciones y puntaje.
   Todos los archivos de assets/evaluacion/ cuelgan de window.NC.eval

     nucleo.js      <- este: utilidades + datos
     banco.js       lee las preguntas de contenido/<materia>/evaluacion/preguntas/
     formulario.js  pantalla de configuracion de una autoevaluacion
     examen.js      pantalla de la autoevaluacion en curso
     informe.js     pantalla del informe final
     evaluacion.js  pestania Evaluacion: inicio, parciales y navegacion entre pantallas
   ============================================================ */

window.NC = window.NC || {};
window.NC.eval = window.NC.eval || {};

(function (E) {
  "use strict";

  /* ---------- DOM ---------- */

  // h("div", {class: "x", onclick: fn}, [hijos]) . "html" asigna innerHTML.
  E.h = function (tag, attrs, hijos) {
    var el = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      var v = attrs[k];
      if (v === null || v === undefined || v === false) { return; }
      if (k.slice(0, 2) === "on") { el.addEventListener(k.slice(2), v); }
      else if (k === "html") { el.innerHTML = v; }
      else if (v === true) { el.setAttribute(k, ""); }
      else { el.setAttribute(k, v); }
    });
    [].concat(hijos === undefined ? [] : hijos).forEach(function (c) {
      if (c === null || c === undefined || c === false) { return; }
      el.appendChild(typeof c === "object" ? c : document.createTextNode(String(c)));
    });
    return el;
  };

  // Vacia un contenedor. Cada vaciado cambia data-pantalla: asi el contador de
  // una autoevaluacion sabe que ya no esta en pantalla y se detiene.
  E.vaciar = function (el) {
    el.dataset.pantalla = String((parseInt(el.dataset.pantalla, 10) || 0) + 1);
    if (window.MathJax && window.MathJax.typesetClear) {
      try { window.MathJax.typesetClear([el]); } catch (e) {}
    }
    el.innerHTML = "";
  };

  // Si MathJax todavia no cargo, app.js tipografia el pane activo cuando termine.
  E.tipografiar = function (el) {
    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise([el]).catch(function () {});
    }
  };

  // Cambio de pantalla dentro de la pestania: arriba de todo e indice nuevo.
  E.pantallaNueva = function (cont) {
    E.tipografiar(cont);
    if (window.NC.reconstruirIndice) { window.NC.reconstruirIndice(); }
    window.scrollTo(0, 0);
  };

  // Flecha de desplegable: se cambia el caracter, nunca se rota por CSS.
  E.flecha = function (abierto) { return abierto ? "▼" : "▶"; };

  /* ---------- varios ---------- */

  E.mezclar = function (lista) {
    var a = lista.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  };

  E.reloj = function (ms) {
    var s = Math.max(0, Math.ceil(ms / 1000));
    return Math.floor(s / 60) + ":" + ("0" + (s % 60)).slice(-2);
  };

  E.duracion = function (ms) {
    var s = Math.max(0, Math.round(ms / 1000));
    var m = Math.floor(s / 60);
    return m ? m + " min " + ("0" + (s % 60)).slice(-2) + " s" : s + " s";
  };

  E.fecha = function (ms) {
    var d = new Date(ms);
    return d.toLocaleDateString("es-AR") + " " +
      d.toLocaleTimeString("es-AR", { hour: "2-digit", minute: "2-digit" });
  };

  E.LETRAS = "ABCDEFGHIJ";
  E.TIPOS = { teoria: "Teoría", practica: "Práctica" };
  E.MODOS = { normal: "Normal", interactivo: "Interactivo" };
  E.NIVELES = { principiante: "Principiante", medio: "Medio", avanzado: "Avanzado" };

  /* ---------- materia y unidades (se leen del menu lateral: una sola fuente) ---------- */

  E.unidades = function (materia) {
    var botones = document.querySelectorAll('.materia[data-materia="' + materia + '"] .unidades button');
    return Array.prototype.map.call(botones, function (b) {
      return {
        id: b.getAttribute("data-unidad"),
        num: b.querySelector(".u-num").textContent.trim(),
        nombre: b.querySelector(".u-name").textContent.trim()
      };
    });
  };

  E.numeroDeUnidad = function (materia, id) {
    var u = E.unidades(materia).filter(function (x) { return x.id === id; })[0];
    return u ? u.num : id;
  };

  E.nombreMateria = function (materia) {
    var el = document.querySelector('.materia[data-materia="' + materia + '"] .m-nombre');
    return el ? el.textContent.trim() : materia;
  };

  /* ---------- guardado (localStorage del navegador) ---------- */

  var CLAVE = "newcampus:autoevaluaciones";

  function leerTodo() {
    try { return JSON.parse(localStorage.getItem(CLAVE) || "[]") || []; } catch (e) { return []; }
  }

  function escribirTodo(lista) {
    try { localStorage.setItem(CLAVE, JSON.stringify(lista)); return true; } catch (e) { return false; }
  }

  E.almacen = {
    listar: function (materia) {
      return leerTodo()
        .filter(function (a) { return a.materia === materia; })
        .map(normalizar)
        .sort(function (a, b) { return b.modificada - a.modificada; });
    },
    obtener: function (id) {
      return normalizar(leerTodo().filter(function (a) { return a.id === id; })[0] || null);
    },
    guardar: function (ae) {
      var lista = leerTodo().filter(function (a) { return a.id !== ae.id; });
      ae.modificada = Date.now();
      lista.push(ae);
      return escribirTodo(lista);
    },
    borrar: function (id) {
      escribirTodo(leerTodo().filter(function (a) { return a.id !== id; }));
    }
  };

  /* ---------- intentos, estado y puntaje ---------- */

  // Por que termino un intento. Todos quedan en estado "terminada".
  E.MOTIVOS = {
    completa: "La completaste",
    tiempo: "Se terminó el tiempo",
    abandonada: "La terminaste antes de completarla",
    "sin-vidas": "Te quedaste sin vidas"
  };

  // Datos guardados con versiones anteriores de NewCampus.
  function normalizar(ae) {
    var it = ae && ae.intento;
    if (!it) { return ae; }
    if (it.estado === "finalizada") { it.estado = "terminada"; it.motivo = "completa"; }
    if (it.estado === "tiempo-agotado") { it.estado = "terminada"; it.motivo = "tiempo"; }
    if (it.config.modo === "interactivo" && typeof it.vidas !== "number") {
      var usados = it.preguntas.reduce(function (s, p) { return s + (p.fallos || 0); }, 0);
      it.vidas = Math.max(0, it.config.fallos - usados);
    }
    (ae.historial || []).forEach(function (x) {
      if (!x.motivo) { x.motivo = x.estado === "tiempo-agotado" ? "tiempo" : "completa"; }
    });
    return ae;
  }
  E.almacen.normalizar = normalizar;

  // En modo normal: bien / mal. En interactivo: al primer intento / con errores.
  E.puntaje = function (intento) {
    var r = { correctas: 0, incorrectas: 0, sinResponder: 0, total: intento.preguntas.length };
    intento.preguntas.forEach(function (p) {
      if (!p.hecho) { r.sinResponder++; }
      else if (p.ok) { r.correctas++; }
      else { r.incorrectas++; }
    });
    return r;
  };

  E.cerrarIntento = function (ae, motivo, fin) {
    var it = ae.intento;
    it.estado = "terminada";
    it.motivo = motivo;
    it.fin = fin || Date.now();
    var p = E.puntaje(it);
    ae.historial = ae.historial || [];
    ae.historial.unshift({
      fecha: it.fin, motivo: motivo, correctas: p.correctas, total: p.total, duracion: it.fin - it.inicio
    });
    ae.historial = ae.historial.slice(0, 10);
    E.almacen.guardar(ae);
  };

  // Estado legible. Si tenia contador y se vencio mientras no estabas, la cierra ahora.
  E.estadoDe = function (ae) {
    var it = ae.intento;
    if (it && it.estado === "en-curso" && it.limite && Date.now() >= it.limite) {
      E.cerrarIntento(ae, "tiempo", it.limite);
    }
    if (!it) {
      return { clave: "nueva", texto: "Sin empezar", detalle: "Tocá para empezar" };
    }
    var p = E.puntaje(it);
    if (it.estado === "en-curso") {
      var partes = ["Pregunta " + Math.min(it.actual + 1, p.total) + " de " + p.total];
      if (it.limite) { partes.push("quedan " + E.reloj(it.limite - Date.now())); }
      if (it.config.modo === "interactivo") { partes.push("❤ " + (it.vidas === 1 ? "queda 1" : "quedan " + it.vidas)); }
      return { clave: "en-curso", texto: "En curso", detalle: partes.join(" · ") };
    }
    return { clave: "terminada", texto: "Terminada",
             detalle: (E.MOTIVOS[it.motivo] || "Terminada") + " · " + p.correctas + " / " + p.total };
  };

  E.textoVidas = function (n) { return "❤ " + n + (n === 1 ? " vida" : " vidas"); };

  E.resumenConfig = function (materia, c) {
    var partes = [];
    partes.push(E.MODOS[c.modo] + (c.modo === "interactivo" ? " · " + E.NIVELES[c.nivel] : ""));
    var cant = 0;
    if (c.teoria && c.practica && c.reparto === "mezcla") { cant = c.cantMezcla; }
    else { cant = (c.teoria ? c.cantTeoria : 0) + (c.practica ? c.cantPractica : 0); }
    partes.push(cant + (cant === 1 ? " pregunta" : " preguntas"));
    partes.push(c.unidades.map(function (u) { return E.numeroDeUnidad(materia, u); }).join(", "));
    if (c.modo === "interactivo") { partes.push(c.fallos + (c.fallos === 1 ? " vida" : " vidas")); }
    partes.push(c.conTiempo ? c.minutos + " min" : "Sin límite");
    return partes;
  };

  /* ---------- cartel de confirmacion ----------
     E.dialogo({ titulo, texto, botones: [{ texto, clase, accion }] })
     Escape o clic afuera cierran sin hacer nada. Devuelve la funcion que lo cierra. */

  E.dialogo = function (op) {
    var h = E.h;
    var capa = h("div", { class: "ev-dialogo-capa" });
    var botones = h("div", { class: "ev-dialogo-botones" });
    var caja = h("div", { class: "ev-dialogo", role: "dialog", "aria-modal": "true" }, [
      h("p", { class: "ev-dialogo-titulo" }, op.titulo),
      op.texto ? h("p", { class: "ev-dialogo-texto" }, op.texto) : null,
      botones
    ]);
    capa.appendChild(caja);

    function cerrar() {
      if (capa.parentNode) { capa.parentNode.removeChild(capa); }
      document.removeEventListener("keydown", tecla);
    }
    function tecla(ev) { if (ev.key === "Escape") { cerrar(); } }

    op.botones.forEach(function (b) {
      botones.appendChild(h("button", { class: "ev-btn " + (b.clase || ""), type: "button", onclick: function () {
        cerrar();
        if (b.accion) { b.accion(); }
      } }, b.texto));
    });
    capa.addEventListener("click", function (ev) { if (ev.target === capa) { cerrar(); } });
    document.addEventListener("keydown", tecla);
    document.body.appendChild(capa);
    botones.firstChild.focus();
    return cerrar;
  };
})(window.NC.eval);
