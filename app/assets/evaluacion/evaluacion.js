/* ============================================================
   NEWCAMPUS - Evaluacion: pestania y navegacion
   app.js llama a NC.eval.montar(pane, materia) la primera vez que se abre
   la pestania. Desde aca se pasa entre pantallas:
     inicio -> parcial | formulario nuevo | examen -> informe
   Una autoevaluacion guardada no se edita: su tarjeta lleva a las preguntas
   (sin empezar o en curso) o al informe (terminada).
   ============================================================ */

(function (E) {
  "use strict";

  var ABIERTAS_KEY = "newcampus:evaluacion-secciones";

  function seccionesAbiertas() {
    try { return JSON.parse(localStorage.getItem(ABIERTAS_KEY) || "{}") || {}; } catch (e) { return {}; }
  }

  function guardarSeccion(id, abierta) {
    var s = seccionesAbiertas();
    s[id] = abierta;
    try { localStorage.setItem(ABIERTAS_KEY, JSON.stringify(s)); } catch (e) {}
  }

  var ALTO_BARRA = 110;   // barra superior fija de la pagina

  function irA(el) {
    window.scrollTo(0, Math.max(0, el.getBoundingClientRect().top + window.pageYOffset - ALTO_BARRA));
  }

  // Lo que muestra la tarjeta viene del indice (construir.py lo saca del
  // meta.json de cada examen), asi la lista se dibuja sin cargar nada.
  // El tipo lo pone construir.py segun la carpeta: parciales/ o finales/.
  function fichasExamen(materia, tipo) {
    var fichas = ((window.Apuntes.indice || {}).examenes || {})[materia] || [];
    return fichas.filter(function (f) { return f.tipo === tipo; })
      .sort(function (a, b) {
        return a.id < b.id ? 1 : -1;    // los mas nuevos primero
      });
  }

  E.montar = function (pane, materia) {
    var h = E.h;
    var cont = h("div", { class: "ev" });
    pane.appendChild(cont);
    // Los bancos de preguntas son chicos y los necesita todo el apartado
    // (armar, rendir, corregir): se traen una vez al entrar.
    E.banco.asegurar(materia, function () { inicio(); });

    var acciones = {
      volver: function (aviso) { inicio(aviso); },
      abrir: function (id) {
        var ae = E.almacen.obtener(id);
        if (!ae) { inicio(); return; }
        if (E.estadoDe(ae).clave === "terminada") { acciones.informe(ae); }
        else { acciones.lanzar(ae, false); }
      },
      nueva: function () { E.formulario.mostrar(cont, materia, acciones); },
      // Cada etapa del parcial tiene su pantalla: la 1ra es un cuestionario
      // (cuestionario.js) y la 2da el examen de siempre (examen.js / informe.js).
      lanzar: function (ae, reiniciar) {
        if (E.etapaDe(ae.config) === "1") { E.cuestionario.lanzar(cont, materia, ae, reiniciar, acciones); }
        else { E.examen.lanzar(cont, materia, ae, reiniciar, acciones); }
      },
      informe: function (ae, aviso) {
        if (E.etapaDe(ae.config) === "1") { E.cuestionario.informe(cont, materia, ae, acciones, aviso); }
        else { E.informe.mostrar(cont, materia, ae, acciones, aviso); }
      },
      // La usan la ✕ de la tarjeta y el boton del informe final: en los dos
      // casos se pregunta primero y despues se vuelve a las tarjetas.
      eliminar: function (ae) {
        E.dialogo({
          titulo: "¿Seguro que querés eliminar esta autoevaluación?",
          texto: "“" + ae.nombre + "” se borra con su progreso y su historial. No se puede deshacer.",
          botones: [
            { texto: "Cancelar" },
            { texto: "Eliminar", clase: "ev-btn-rojo", accion: function () {
              E.almacen.borrar(ae.id);
              inicio("Se eliminó “" + ae.nombre + "”.");
            } }
          ]
        });
      }
    };

    /* ---------- desplegable ---------- */

    function seccion(id, icono, titulo, resumen, construirCuerpo) {
      var abierta = !!seccionesAbiertas()[id];
      var chev = h("span", { class: "ev-seccion-chev" }, E.flecha(abierta));
      var cuerpo = h("div", { class: "ev-seccion-cuerpo" });
      cuerpo.hidden = !abierta;
      var cab = h("button", { class: "ev-seccion-cab", type: "button", "aria-expanded": String(abierta) }, [
        h("span", { class: "ev-seccion-icono" }, icono),
        h("span", { class: "ev-seccion-textos" }, [
          h("span", { class: "ev-seccion-titulo" }, titulo),
          h("span", { class: "ev-seccion-resumen" }, resumen)
        ]),
        chev
      ]);
      var caja = h("section", { class: "ev-seccion" + (abierta ? " is-open" : "") }, [cab, cuerpo]);
      cab.addEventListener("click", function () {
        abierta = !abierta;
        caja.classList.toggle("is-open", abierta);
        cuerpo.hidden = !abierta;
        chev.textContent = E.flecha(abierta);
        cab.setAttribute("aria-expanded", String(abierta));
        guardarSeccion(id, abierta);
      });
      construirCuerpo(cuerpo);
      return caja;
    }

    /* ---------- pantallas ---------- */

    function inicio(aviso) {
      E.vaciar(cont);
      var parciales = fichasExamen(materia, "parcial");
      var finales = fichasExamen(materia, "final");
      var guardadas = E.almacen.listar(materia);
      var enCurso = guardadas.filter(function (a) { return E.estadoDe(a).clave === "en-curso"; }).length;

      cont.appendChild(h("h1", { class: "ev-h1" }, "Evaluación"));
      cont.appendChild(h("p", { class: "pane-intro" },
        "Parciales, finales y autoevaluaciones de " + E.nombreMateria(materia) + "."));
      if (aviso) { cont.appendChild(h("div", { class: "ae-aviso" }, aviso)); }

      cont.appendChild(seccionExamenes("parciales", "📄", "Parciales", "parcial", parciales));
      cont.appendChild(seccionExamenes("finales", "🎓", "Finales", "final", finales));

      cont.appendChild(seccion("autoevaluacion", "🧠", "Autoevaluación",
        guardadas.length
          ? guardadas.length + (guardadas.length === 1 ? " guardada" : " guardadas") + (enCurso ? " · " + enCurso + " en curso" : "")
          : "Armá tu primera autoevaluación",
        function (cuerpo) {
          var tarjetas = h("div", { class: "ev-tarjetas" });
          tarjetas.appendChild(h("button", { class: "ev-tarjeta ev-tarjeta-nueva", type: "button", onclick: acciones.nueva }, [
            h("span", { class: "ev-mas" }, "+"),
            h("span", { class: "ev-tarjeta-titulo" }, "Nueva autoevaluación")
          ]));
          guardadas.forEach(function (ae) { tarjetas.appendChild(tarjetaAutoevaluacion(ae)); });
          cuerpo.appendChild(tarjetas);
        }));

      E.pantallaNueva(cont);
    }

    // Parciales y finales se listan igual: cambia el rotulo y de donde salen.
    function seccionExamenes(id, icono, titulo, palabra, fichas) {
      var plural = palabra === "parcial" ? "parciales" : "finales";
      var resumen = fichas.length === 1 ? "1 " + palabra + " transcripto"
        : fichas.length ? fichas.length + " " + plural + " transcriptos"
        : "Todavía no hay " + plural + " cargados";
      return seccion(id, icono, titulo, resumen,
        function (cuerpo) {
          if (!fichas.length) {
            cuerpo.appendChild(h("p", { class: "ev-vacio" },
              "Cuando se transcriba un " + palabra + " va a aparecer acá."));
            return;
          }
          cuerpo.appendChild(h("div", { class: "ev-tarjetas" }, fichas.map(function (d) {
            return h("button", { class: "ev-tarjeta", type: "button", onclick: function () { verExamen(d); } }, [
              h("span", { class: "ev-tarjeta-fecha" }, d.fecha),
              h("span", { class: "ev-tarjeta-titulo" }, d.titulo),
              h("span", { class: "ev-tarjeta-detalle" }, d.detalle),
              d.temas ? h("span", { class: "ev-tarjeta-temas" }, d.temas) : null
            ]);
          })));
        });
    }

    // La tarjeta es un div (no un boton) porque adentro lleva sus propios botones.
    function tarjetaAutoevaluacion(ae) {
      var estado = E.estadoDe(ae);
      var terminada = estado.clave === "terminada";
      var accionTexto = { "nueva": "Tocá para empezar →", "en-curso": "Tocá para continuar →", "terminada": "Tocá para ver el informe →" };

      var tarjeta = h("div", { class: "ev-tarjeta ev-tarjeta-ae", role: "button", tabindex: "0",
        "aria-label": ae.nombre + ": " + estado.texto }, [
        h("button", { class: "ev-borrar", type: "button", title: "Eliminar autoevaluación", "aria-label": "Eliminar", onclick: function (ev) {
          ev.stopPropagation();
          acciones.eliminar(ae);
        } }, "✕"),
        h("span", { class: "ev-chip", "data-estado": estado.clave }, estado.texto),
        h("span", { class: "ev-tarjeta-titulo" }, ae.nombre),
        h("span", { class: "ev-tarjeta-detalle" }, E.resumenConfig(materia, ae.config).join(" · ")),
        h("span", { class: "ev-tarjeta-estado" }, estado.clave === "nueva" ? "" : estado.detalle),
        h("span", { class: "ev-tarjeta-pie" }, [
          h("span", {}, accionTexto[estado.clave]),
          terminada ? h("button", { class: "ev-btn ev-btn-chico", type: "button", onclick: function (ev) {
            ev.stopPropagation();
            acciones.lanzar(ae, true);
          } }, "↻ Rehacer") : null
        ])
      ]);

      tarjeta.addEventListener("click", function () { acciones.abrir(ae.id); });
      tarjeta.addEventListener("keydown", function (ev) {
        if ((ev.key === "Enter" || ev.key === " ") && ev.target === tarjeta) { ev.preventDefault(); acciones.abrir(ae.id); }
      });
      return tarjeta;
    }

    function verExamen(ficha) {
      var html = ((window.Apuntes.examenes || {})[materia] || {})[ficha.id];
      if (!html) {
        // todavia no se cargo: se trae y se vuelve a entrar
        E.vaciar(cont);
        cont.appendChild(h("p", { class: "ev-vacio" }, "Abriendo el examen…"));
        window.Apuntes.cargar(ficha.archivo, function (llego) {
          if (llego) { verExamen(ficha); }
          else { inicio("No pude abrir el examen. Corré python construir.py en app/."); }
        });
        return;
      }
      E.vaciar(cont);
      cont.appendChild(h("button", { class: "ev-volver", type: "button", onclick: function () { inicio(); } }, "← Evaluación"));
      cont.appendChild(h("div", { html: html }));

      // Los titulos se guardan ANTES de que MathJax reemplace las formulas:
      // asi el indice muestra "E(X²) - μ²" y no el texto ya renderizado.
      var limpiar = window.NC.limpiarTitulo || function (t) { return t; };
      Array.prototype.forEach.call(cont.querySelectorAll(".pd-cuerpo > h4, .pd-cuerpo > .paso"), function (t) {
        t.dataset.tocTitulo = limpiar(t.textContent);
      });

      // al abrir o cerrar una explicacion, el indice de la derecha se rearma:
      // asi aparecen (o desaparecen) sus partes debajo del ejercicio
      Array.prototype.forEach.call(cont.querySelectorAll(".parcial-desp"), function (desp) {
        desp.addEventListener("toggle", function () {
          if (window.NC.reconstruirIndice) { window.NC.reconstruirIndice(); }
        });
      });

      E.pantallaNueva(cont);
    }
  };
})(window.NC.eval);
