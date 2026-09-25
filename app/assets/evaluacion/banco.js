/* ============================================================
   NEWCAMPUS - Evaluacion: banco de preguntas
   Convierte el HTML de contenido/<materia>/evaluacion/preguntas/<unidad>/
   en objetos. El formato esta en preguntas/FORMATO.md.

   Hay preguntas de las dos etapas del parcial:
     etapa "2"  escrito: teoria / practica, modo normal o interactivo
     etapa "1"  cuestionario virtual: opcion, multiple o completar
   ============================================================ */

(function (E) {
  "use strict";

  var cache = {};   // materia -> { lista: [...], porId: {...} }

  // Nivel mas avanzado en el que aparece cada paso. Un paso se muestra si su
  // rango es menor o igual al del nivel elegido.
  var RANGO = { avanzado: 1, medio: 2, principiante: 3 };
  var TIPOS_2DA = ["teoria", "practica", "ejercicio"];

  function html(el) { return el ? el.innerHTML.trim() : ""; }

  function hijo(el, clase) { return el.querySelector(":scope > ." + clase); }

  function leerOpciones(el) {
    var ul = hijo(el, "p-opciones");
    if (!ul) { return null; }
    var textos = [], correcta = -1, correctas = [];
    Array.prototype.forEach.call(ul.querySelectorAll(":scope > li"), function (li, i) {
      textos.push(html(li));
      if (li.hasAttribute("data-correcta")) { correcta = i; correctas.push(i); }
    });
    // correcta: la unica (opcion); correctas: todas (multiple)
    return { textos: textos, correcta: correcta, correctas: correctas };
  }

  function leerPaso(li) {
    return {
      nivel: RANGO[li.getAttribute("data-nivel")] ? li.getAttribute("data-nivel") : "avanzado",
      inciso: li.getAttribute("data-inciso") || "",   // solo en los ejercicios completos
      consigna: html(hijo(li, "p-consigna")),
      respuesta: li.getAttribute("data-respuesta"),
      tolerancia: li.getAttribute("data-tolerancia"),
      opciones: leerOpciones(li),
      pista: html(hijo(li, "p-pista")),
      explicacion: html(hijo(li, "p-explicacion")),
      resolucion: html(hijo(li, "p-resolucion"))   // lo que muestra el boton Resolver
    };
  }

  // Huecos de un "completar", en el orden en que aparecen en el enunciado.
  function leerHuecos(a) {
    return Array.prototype.map.call(a.querySelectorAll(".p-hueco"), function (el) {
      if (el.hasAttribute("data-respuesta")) {
        return { tipo: "numero", respuesta: el.getAttribute("data-respuesta"),
                 decimales: parseInt(el.getAttribute("data-decimales"), 10) || 2 };
      }
      var opciones = [], correcta = -1;
      Array.prototype.forEach.call(el.children, function (op, i) {
        opciones.push(op.textContent.trim());
        if (op.hasAttribute("data-correcta")) { correcta = i; }
      });
      return { tipo: "lista", opciones: opciones, correcta: correcta };
    });
  }

  // Ejercicio completo: la respuesta final en palabras de cada inciso
  // (<div class="p-rta" data-inciso="b">), por letra.
  function leerRtas(a) {
    var rtas = {};
    Array.prototype.forEach.call(a.querySelectorAll(":scope > .p-rta"), function (el) {
      var letra = el.getAttribute("data-inciso");
      if (letra) { rtas[letra] = el.innerHTML.trim(); }
    });
    return rtas;
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
        var fuente = a.querySelector(".p-fuente");
        var etapa = a.getAttribute("data-etapa") === "1" ? "1" : "2";
        var p = {
          id: a.getAttribute("data-id"),
          etapa: etapa,
          // teoria / practica: preguntas del modo Normal; ejercicio: un ejercicio
          // de parcial completo, para el modo Interactivo
          tipo: TIPOS_2DA.indexOf(a.getAttribute("data-tipo")) !== -1 ? a.getAttribute("data-tipo") : "teoria",
          formato: etapa === "1" ? a.getAttribute("data-formato") : null,
          huecos: etapa === "1" ? leerHuecos(a) : [],
          origen: a.getAttribute("data-origen") === "final" ? "final" : "parcial",
          fuente: fuente ? fuente.textContent.trim() : "",
          unidad: unidad,
          enunciado: html(hijo(a, "p-enunciado")),
          pregunta: html(hijo(a, "p-pregunta")),
          opciones: leerOpciones(a),
          pista: html(hijo(a, "p-pista")),
          explicacion: html(hijo(a, "p-explicacion")),
          pasos: pasos ? Array.prototype.map.call(pasos.querySelectorAll(":scope > li"), leerPaso) : [],
          rtas: leerRtas(a)
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

  /* Los bancos llegan en generado/preguntas/*.js, uno por unidad, y se traen
     cuando entras a Evaluacion. avisar() corre cuando ya estan todos. */
  function asegurar(materia, avisar) {
    var archivos = ((window.Apuntes.indice || {}).preguntas || {})[materia] || {};
    var cargados = window.Apuntes.preguntas[materia] || {};
    var faltan = Object.keys(archivos).filter(function (u) { return !cargados[u]; });
    if (!faltan.length) { avisar(); return; }

    var pendientes = faltan.length;
    faltan.forEach(function (unidad) {
      window.Apuntes.cargar(archivos[unidad], function () {
        pendientes -= 1;
        if (!pendientes) { delete cache[materia]; avisar(); }
      });
    });
  }

  /* Mezcla dando ventaja a lo que tomaron en parciales: una pregunta de
     parcial tiene el doble de chances de quedar adelante que una de final.
     (Cada una saca un numero al azar elevado a 1/peso y se ordena por eso.) */
  var PESO = { parcial: 2, final: 1 };
  function mezclarPorOrigen(lista) {
    return lista.map(function (p) { return { p: p, clave: Math.pow(Math.random(), 1 / PESO[p.origen]) }; })
      .sort(function (a, b) { return b.clave - a.clave; })
      .map(function (x) { return x.p; });
  }

  function etapaDe(c) { return c.etapa === "1" ? "1" : "2"; }

  function delPool(materia, c) {
    return cargar(materia).lista.filter(function (p) {
      return p.etapa === etapaDe(c) && c.unidades.indexOf(p.unidad) !== -1;
    });
  }

  /* ---------- correccion de la 1ra etapa ----------
     Devuelve { fraccion: 0..1, huecos } con los criterios del Aula Virtual:
       opcion     todo o nada
       multiple   cada correcta marcada suma 1/C, cada incorrecta marcada resta 1/C (min 0)
       completar  la parte de huecos bien; los numeros van con coma y N decimales */

  function revisarHueco(hueco, dado) {
    dado = dado === undefined || dado === null ? "" : String(dado).trim();
    if (dado === "") { return { ok: false, motivo: "vacio" }; }
    if (hueco.tipo === "lista") {
      return parseInt(dado, 10) === hueco.correcta ? { ok: true } : { ok: false, motivo: "valor" };
    }
    var valor = numero(dado), esperado = numero(hueco.respuesta);
    var mismoValor = !isNaN(valor) && Math.abs(valor - esperado) < 1e-9;
    var formato = new RegExp("^-?\\d+,\\d{" + hueco.decimales + "}$").test(dado);
    if (mismoValor && formato) { return { ok: true }; }
    return { ok: false, motivo: mismoValor ? "formato" : "valor" };
  }

  function corregirCuestionario(p, resp) {
    if (p.formato === "completar") {
      var huecos = p.huecos.map(function (hu, i) { return revisarHueco(hu, (resp || [])[i]); });
      var bien = huecos.filter(function (x) { return x.ok; }).length;
      return { fraccion: p.huecos.length ? bien / p.huecos.length : 0, huecos: huecos };
    }
    if (p.formato === "multiple") {
      var C = p.opciones.correctas.length;
      var suma = (resp || []).reduce(function (s, i) {
        return s + (p.opciones.correctas.indexOf(i) !== -1 ? 1 : -1);
      }, 0);
      return { fraccion: C ? Math.max(0, suma / C) : 0 };
    }
    return { fraccion: resp === p.opciones.correcta ? 1 : 0 };
  }

  E.banco = {
    asegurar: asegurar,
    obtener: function (materia, id) { return cargar(materia).porId[id] || null; },

    // Cuantas preguntas hay en esas unidades: las de 2da etapa por tipo, y las de 1ra.
    disponibles: function (materia, unidades) {
      var r = { teoria: 0, practica: 0, ejercicio: 0, cuestionario: 0 };
      cargar(materia).lista.forEach(function (p) {
        if (unidades.indexOf(p.unidad) === -1) { return; }
        if (p.etapa === "1") { r.cuestionario++; } else { r[p.tipo]++; }
      });
      return r;
    },

    // Devuelve la lista ordenada de ids para un intento nuevo.
    seleccionar: function (materia, c) {
      var pool = delPool(materia, c);
      if (etapaDe(c) === "1") {
        return mezclarPorOrigen(pool).slice(0, c.cantCuestionario).map(function (p) { return p.id; });
      }
      if (c.modo === "interactivo") {
        // reales e inventados mezclados, con ventaja para lo de parciales
        return mezclarPorOrigen(pool.filter(function (p) { return p.tipo === "ejercicio"; }))
          .slice(0, c.cantEjercicios).map(function (p) { return p.id; });
      }
      var teoria = mezclarPorOrigen(pool.filter(function (p) { return p.tipo === "teoria"; }));
      var practica = mezclarPorOrigen(pool.filter(function (p) { return p.tipo === "practica"; }));
      var elegidas;

      if (c.teoria && c.practica && c.reparto === "mezcla") {
        elegidas = mezclarPorOrigen(teoria.concat(practica)).slice(0, c.cantMezcla);
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
    corregirCuestionario: corregirCuestionario,

    // Tolerancia: la indicada en el paso o un 1 % del valor (minimo 0,0005).
    comprobarNumero: function (texto, paso) {
      var dado = numero(texto), esperado = numero(paso.respuesta);
      if (isNaN(dado) || isNaN(esperado)) { return false; }
      var tol = paso.tolerancia ? numero(paso.tolerancia) : Math.max(Math.abs(esperado) * 0.01, 0.0005);
      return Math.abs(dado - esperado) <= tol + 1e-12;
    }
  };
})(window.NC.eval);
