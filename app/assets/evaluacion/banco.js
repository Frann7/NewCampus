/* ============================================================
   NEWCAMPUS - Evaluacion: banco de preguntas
   Convierte el HTML de contenido/<materia>/evaluacion/preguntas/<unidad>.html
   en objetos. El formato esta explicado arriba de preguntas/u4.html.
   ============================================================ */

(function (E) {
  "use strict";

  var cache = {};   // materia -> { lista: [...], porId: {...} }

  // Nivel mas avanzado en el que aparece cada paso. Un paso se muestra si su
  // rango es menor o igual al del nivel elegido.
  var RANGO = { avanzado: 1, medio: 2, principiante: 3 };

  function html(el) { return el ? el.innerHTML.trim() : ""; }

  function hijo(el, clase) { return el.querySelector(":scope > ." + clase); }

  function leerOpciones(el) {
    var ul = hijo(el, "p-opciones");
    if (!ul) { return null; }
    var textos = [], correcta = -1;
    Array.prototype.forEach.call(ul.querySelectorAll(":scope > li"), function (li, i) {
      textos.push(html(li));
      if (li.hasAttribute("data-correcta")) { correcta = i; }
    });
    return { textos: textos, correcta: correcta };
  }

  function leerPaso(li) {
    return {
      nivel: RANGO[li.getAttribute("data-nivel")] ? li.getAttribute("data-nivel") : "avanzado",
      consigna: html(hijo(li, "p-consigna")),
      respuesta: li.getAttribute("data-respuesta"),
      tolerancia: li.getAttribute("data-tolerancia"),
      opciones: leerOpciones(li),
      pista: html(hijo(li, "p-pista")),
      explicacion: html(hijo(li, "p-explicacion"))
    };
  }

  function cargar(materia) {
    if (cache[materia]) { return cache[materia]; }
    var fuentes = (window.Apuntes.preguntas || {})[materia] || {};
    var lista = [], porId = {};

    Object.keys(fuentes).sort().forEach(function (unidad) {
      var t = document.createElement("template");
      t.innerHTML = fuentes[unidad];
      Array.prototype.forEach.call(t.content.querySelectorAll("article.preg"), function (a) {
        var pasos = hijo(a, "p-pasos");
        var p = {
          id: a.getAttribute("data-id"),
          tipo: a.getAttribute("data-tipo") === "practica" ? "practica" : "teoria",
          unidad: unidad,
          enunciado: html(hijo(a, "p-enunciado")),
          pregunta: html(hijo(a, "p-pregunta")),
          opciones: leerOpciones(a),
          pista: html(hijo(a, "p-pista")),
          explicacion: html(hijo(a, "p-explicacion")),
          pasos: pasos ? Array.prototype.map.call(pasos.querySelectorAll(":scope > li"), leerPaso) : []
        };
        if (!p.id || porId[p.id]) { return; }
        lista.push(p);
        porId[p.id] = p;
      });
    });

    cache[materia] = { lista: lista, porId: porId };
    return cache[materia];
  }

  // Convierte lo que escribio el usuario: acepta coma o punto, y fracciones "3/4".
  function numero(texto) {
    var s = String(texto || "").replace(/\s/g, "").replace(/,/g, ".");
    var frac = s.match(/^(-?\d*\.?\d+)\/(-?\d*\.?\d+)$/);
    if (frac) { return parseFloat(frac[1]) / parseFloat(frac[2]); }
    return /^-?\d*\.?\d+(e-?\d+)?$/i.test(s) ? parseFloat(s) : NaN;
  }

  E.banco = {
    obtener: function (materia, id) { return cargar(materia).porId[id] || null; },

    // Cuantas preguntas de cada tipo hay en esas unidades.
    disponibles: function (materia, unidades) {
      var r = { teoria: 0, practica: 0 };
      cargar(materia).lista.forEach(function (p) {
        if (unidades.indexOf(p.unidad) !== -1) { r[p.tipo]++; }
      });
      return r;
    },

    // Devuelve la lista ordenada de ids para un intento nuevo.
    seleccionar: function (materia, c) {
      var pool = cargar(materia).lista.filter(function (p) { return c.unidades.indexOf(p.unidad) !== -1; });
      var teoria = E.mezclar(pool.filter(function (p) { return p.tipo === "teoria"; }));
      var practica = E.mezclar(pool.filter(function (p) { return p.tipo === "practica"; }));
      var elegidas;

      if (c.teoria && c.practica && c.reparto === "mezcla") {
        elegidas = E.mezclar(teoria.concat(practica)).slice(0, c.cantMezcla);
      } else {
        elegidas = (c.teoria ? teoria.slice(0, c.cantTeoria) : [])
          .concat(c.practica ? practica.slice(0, c.cantPractica) : []);
      }

      if (c.teoria && c.practica && c.orden !== "aleatorio") {
        var primero = c.orden;   // "teoria" o "practica"
        elegidas.sort(function (a, b) { return (a.tipo === primero ? 0 : 1) - (b.tipo === primero ? 0 : 1); });
      } else {
        elegidas = E.mezclar(elegidas);
      }
      return elegidas.map(function (p) { return p.id; });
    },

    // Pasos de una pregunta de practica que corresponden al nivel elegido.
    pasosDelNivel: function (pregunta, nivel) {
      return pregunta.pasos.filter(function (paso) { return RANGO[paso.nivel] <= RANGO[nivel]; });
    },

    numero: numero,

    // Tolerancia: la indicada en el paso o un 1 % del valor (minimo 0,0005).
    comprobarNumero: function (texto, paso) {
      var dado = numero(texto), esperado = numero(paso.respuesta);
      if (isNaN(dado) || isNaN(esperado)) { return false; }
      var tol = paso.tolerancia ? numero(paso.tolerancia) : Math.max(Math.abs(esperado) * 0.01, 0.0005);
      return Math.abs(dado - esperado) <= tol + 1e-12;
    }
  };
})(window.NC.eval);
