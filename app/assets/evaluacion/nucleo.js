/* ============================================================
   NEWCAMPUS - Evaluacion: nucleo
   Utilidades compartidas, guardado de autoevaluaciones y puntaje.
   Todos los archivos de assets/evaluacion/ cuelgan de window.NC.eval

     nucleo.js      <- este: utilidades + datos
     banco.js       lee las preguntas de contenido/<materia>/evaluacion/preguntas/
     formulario.js  pantalla de configuracion de una autoevaluacion
     examen.js      autoevaluacion en curso, 2da etapa (escrito)
     informe.js     informe final, 2da etapa
     cuestionario.js  1ra etapa (cuestionario virtual): en curso e informe
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
    // se va la autoevaluacion de la pantalla: el material de catedra vuelve al de Evaluacion
    var ae = window.NC && window.NC.materialAutoeval;
    if (ae && ae.cont === el && window.NC.actualizarLanzador) {
      window.setTimeout(window.NC.actualizarLanzador, 0);
    }
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
  E.TIPOS = { teoria: "Teoría", practica: "Práctica", ejercicio: "Ejercicio de parcial" };
  E.MODOS = { normal: "Normal", interactivo: "Interactivo" };

  /* Los modos de la 2da etapa:
       normal + estilo "parcial"  enunciado y opciones, como en el examen
       normal + estilo "guiado"   las mismas preguntas, faciles: con pistas y la
                                  practica en todos sus pasos. Sin vidas ni nivel:
                                  si te equivocas, volves a intentar.
       interactivo                un ejercicio de parcial completo, desglosado en
                                  pasos segun el nivel, con vidas
     "Guiado" (pistas + pasos) es comun al estilo guiado y al interactivo; el nivel
     y las vidas son solo del interactivo. */
  E.guiado = function (c) {
    return !!c && (c.modo === "interactivo" || (c.modo === "normal" && c.estilo === "guiado"));
  };
  E.conVidas = function (c) { return !!c && c.modo === "interactivo"; };
  // El estilo guiado siempre desglosa en todos los pasos (son las "faciles").
  E.nivelDe = function (c) { return c.modo === "interactivo" ? c.nivel : "principiante"; };
  E.nombreModo = function (c) {
    if (c.modo === "interactivo") { return "Interactivo · " + E.NIVELES[c.nivel]; }
    if (c.estilo === "guiado") { return "Normal · fáciles y guiadas"; }
    return "Normal";
  };
  E.NIVELES = { principiante: "Principiante", medio: "Medio", avanzado: "Avanzado" };

  /* El parcial de la catedra tiene dos instancias, y cada autoevaluacion
     simula una sola. La 1ra es el cuestionario del Aula Virtual; la 2da, el
     escrito con problemas y teoria. Las guardadas antes de esto son de la 2da. */
  E.ETAPAS = { "1": "1ra etapa · Cuestionario virtual", "2": "2da etapa · Escrito" };
  E.etapaDe = function (c) { return c && c.etapa === "1" ? "1" : "2"; };

  // Origen de una pregunta: el mismo lenguaje que las marcas de teoria y practica.
  E.ORIGENES = {
    parcial: { glifo: "★", texto: "Parcial" },
    final:   { glifo: "◈", texto: "Final" }
  };
  E.chipOrigen = function (p) {
    var o = E.ORIGENES[p.origen] || E.ORIGENES.parcial;
    return E.h("span", { class: "ev-chip ev-chip-origen", "data-origen": p.origen, title: p.fuente || "" },
      o.glifo + " " + o.texto);
  };

  // Nota con coma y dos decimales, como la muestra el Aula Virtual: 72,50
  E.nota = function (n) { return (Math.round(n * 100) / 100).toFixed(2).replace(".", ","); };

  /* Lo que significa la nota de la 1ra instancia, segun el reglamento:
     de 30 a 59 seguis para regularizar; con 60 o mas pasas a la 2da instancia. */
  E.condicionPrimeraEtapa = function (nota) {
    if (nota >= 60) { return { clave: "accede", texto: "Con 60 o más accedés a la 2da instancia escrita." }; }
    if (nota >= 30) { return { clave: "regular", texto: "Entre 30 y 59 seguís en condiciones de regularizar, pero no accedés a la 2da instancia." }; }
    return { clave: "no", texto: "Con menos de 30 esta instancia no alcanza ni para regularizar." };
  };

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
    entregada: "La entregaste con preguntas sin responder",
    "sin-vidas": "Te quedaste sin vidas"
  };

  // Datos guardados con versiones anteriores de NewCampus.
  /* Antes de los ejercicios completos, "interactivo" eran las preguntas del
     banco con pistas y vidas: eso hoy es Normal en estilo guiado. Las guardadas
     con el esquema viejo (sin v: 2) se pasan a lo que eran. */
  function migrarModo(c) {
    if (!c) { return; }
    if (!c.etapa) { c.etapa = "2"; }
    if (!c.v) {
      if (c.modo === "interactivo") { c.modo = "normal"; c.estilo = "guiado"; }
      if (!c.estilo) { c.estilo = "parcial"; }
      c.v = 2;
    }
  }

  function normalizar(ae) {
    if (ae) { migrarModo(ae.config); }
    var it = ae && ae.intento;
    if (!it) { return ae; }
    migrarModo(it.config);
    if (it.estado === "finalizada") { it.estado = "terminada"; it.motivo = "completa"; }
    if (it.estado === "tiempo-agotado") { it.estado = "terminada"; it.motivo = "tiempo"; }
    if (E.conVidas(it.config) && typeof it.vidas !== "number") {
      var usados = it.preguntas.reduce(function (s, p) { return s + (p.fallos || 0); }, 0);
      it.vidas = Math.max(0, it.config.fallos - usados);
    }
    (ae.historial || []).forEach(function (x) {
      if (!x.motivo) { x.motivo = x.estado === "tiempo-agotado" ? "tiempo" : "completa"; }
    });
    return ae;
  }
  E.almacen.normalizar = normalizar;

  /* En modo normal: bien / mal. En interactivo: al primer intento / con errores.
     En la 1ra etapa cada pregunta tiene una fraccion (0 a 1, hay puntaje parcial)
     que se calcula al entregar; la nota es sobre 100. */
  E.puntaje = function (intento) {
    var r = { correctas: 0, incorrectas: 0, parciales: 0, sinResponder: 0, salteadas: 0,
              total: intento.preguntas.length, nota: null };
    var suma = 0;
    intento.preguntas.forEach(function (p) {
      if (p.salteado) { r.salteadas++; return; }
      if (!p.hecho) { r.sinResponder++; return; }
      if (typeof p.fraccion === "number") {
        suma += p.fraccion;
        if (p.fraccion >= 1) { r.correctas++; } else if (p.fraccion > 0) { r.parciales++; } else { r.incorrectas++; }
        return;
      }
      if (p.ok) { r.correctas++; } else { r.incorrectas++; }
    });
    if (E.etapaDe(intento.config) === "1" && r.total) { r.nota = 100 * suma / r.total; }
    return r;
  };

  /* La 1ra etapa se corrige recien al entregar, como el Aula Virtual. Esto
     tambien corre si el contador vencio mientras no estabas: lo contestado
     hasta ahi se califica igual, y lo que quedo vacio vale 0. */
  function calificarCuestionario(ae) {
    ae.intento.preguntas.forEach(function (r) {
      var p = E.banco.obtener(ae.materia, r.id);
      r.hecho = r.respuesta !== null && r.respuesta !== undefined;
      r.fraccion = p && r.hecho ? E.banco.corregirCuestionario(p, r.respuesta).fraccion : 0;
      r.ok = r.fraccion >= 1;
    });
  }

  E.cerrarIntento = function (ae, motivo, fin) {
    var it = ae.intento;
    if (E.etapaDe(it.config) === "1") { calificarCuestionario(ae); }
    it.estado = "terminada";
    it.motivo = motivo;
    it.fin = fin || Date.now();
    var p = E.puntaje(it);
    ae.historial = ae.historial || [];
    ae.historial.unshift({
      fecha: it.fin, motivo: motivo, correctas: p.correctas, total: p.total, nota: p.nota,
      duracion: it.fin - it.inicio
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
    var primera = E.etapaDe(it.config) === "1";
    if (it.estado === "en-curso") {
      var respondidas = it.preguntas.filter(function (r) { return r.respuesta !== null && r.respuesta !== undefined; }).length;
      var partes = [primera ? "Respondidas " + respondidas + " de " + p.total
                            : "Pregunta " + Math.min(it.actual + 1, p.total) + " de " + p.total];
      if (it.limite) { partes.push("quedan " + E.reloj(it.limite - Date.now())); }
      if (E.conVidas(it.config)) { partes.push("❤ " + (it.vidas === 1 ? "queda 1" : "quedan " + it.vidas)); }
      return { clave: "en-curso", texto: "En curso", detalle: partes.join(" · ") };
    }
    return { clave: "terminada", texto: "Terminada",
             detalle: (E.MOTIVOS[it.motivo] || "Terminada") + " · " +
               (primera ? "Nota " + E.nota(p.nota) + " / 100" : p.correctas + " / " + p.total) };
  };

  E.textoVidas = function (n) { return "❤ " + n + (n === 1 ? " vida" : " vidas"); };

  E.resumenConfig = function (materia, c) {
    var partes = [];
    var cant = 0;
    if (E.etapaDe(c) === "1") {
      partes.push("1ra etapa · Cuestionario");
      cant = c.cantCuestionario;
    } else {
      partes.push("2da etapa · " + E.nombreModo(c));
      if (c.modo === "interactivo") { cant = c.cantEjercicios; }
      else if (c.teoria && c.practica && c.reparto === "mezcla") { cant = c.cantMezcla; }
      else { cant = (c.teoria ? c.cantTeoria : 0) + (c.practica ? c.cantPractica : 0); }
    }
    partes.push(cant + (c.modo === "interactivo" && E.etapaDe(c) === "2"
      ? (cant === 1 ? " ejercicio" : " ejercicios")
      : (cant === 1 ? " pregunta" : " preguntas")));
    partes.push(c.unidades.map(function (u) { return E.numeroDeUnidad(materia, u); }).join(", "));
    if (E.etapaDe(c) === "2" && E.conVidas(c)) { partes.push(c.fallos + (c.fallos === 1 ? " vida" : " vidas")); }
    if (E.etapaDe(c) === "2" && c.modo === "normal" && c.navLibre) { partes.push("navegación libre"); }
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
