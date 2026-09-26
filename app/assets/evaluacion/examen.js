/* ============================================================
   NEWCAMPUS - Evaluacion: autoevaluacion en curso (2da etapa)
   NORMAL, estilo parcial:  enunciado completo + opciones. Corrige al responder
                o al final.
   NORMAL, estilo guiado:   preguntas faciles: pistas con la lamparita, y si te
                equivocas volves a intentar (sin vidas). En practica pide el
                ejercicio en todos sus pasos.
   INTERACTIVO: un ejercicio de parcial completo, desglosado en pasos por
                inciso segun el nivel, con pistas y vidas. Saltear un
                ejercicio lo deja para despues: se retoma donde quedo antes
                de terminar, y solo figura como salteado si se termina la
                autoevaluacion sin completarlo. Cada paso tiene ademas "Resolver": muestra la
                resolucion paso a paso y pasa al siguiente (no gasta vidas,
                pero el ejercicio ya no cuenta como sin errores). Los intentos
                guardados antes de este boton no tienen "resueltos": cuenta 0.
   En normal, la navegacion libre agrega casillas para ir a cualquier pregunta
   y deja terminar cuando se quiera. En el interactivo y el guiado se pueden
   volver a mirar los ejercicios ya hechos (solo lectura) y volver al actual.
   Cada respuesta se guarda al instante, asi se puede salir y continuar.
   Con contador, salir pregunta: terminar, mantener el contador o cancelar.
   ============================================================ */

(function (E) {
  "use strict";

  function crearIntento(materia, ae) {
    var c = ae.config;
    var ahora = Date.now();
    ae.intento = {
      estado: "en-curso",
      config: JSON.parse(JSON.stringify(c)),   // copia: el informe no cambia si despues editas
      inicio: ahora,
      fin: null,
      limite: c.conTiempo ? ahora + c.minutos * 60000 : null,
      vidas: E.conVidas(c) ? c.fallos : null,
      actual: 0,
      preguntas: E.banco.seleccionar(materia, c).map(function (id) {
        return { id: id, hecho: false, ok: null, elegida: null, orden: null, salteado: false,
                 fallos: 0, pistas: 0, descartadas: [], paso: 0, pasos: [] };
      })
    };
  }

  function ordenDe(registro, cantidad) {
    if (!registro.orden || registro.orden.length !== cantidad) {
      var indices = [];
      for (var i = 0; i < cantidad; i++) { indices.push(i); }
      registro.orden = E.mezclar(indices);
    }
    return registro.orden;
  }

  E.examen = {
    /* acciones: { volver(aviso), informe(ae, aviso) } */
    lanzar: function (cont, materia, ae, reiniciar, acciones) {
      var h = E.h, B = E.banco;

      E.estadoDe(ae);   // si tenia contador vencido, lo cierra antes de decidir
      if (reiniciar || !ae.intento || ae.intento.estado !== "en-curso") { crearIntento(materia, ae); }
      var it = ae.intento, c = it.config;

      if (!it.preguntas.length) {
        ae.intento = null;
        E.almacen.guardar(ae);
        acciones.volver("“" + ae.nombre + "” no tiene preguntas disponibles en el banco para esa configuración.");
        return;
      }
      E.almacen.guardar(ae);

      E.vaciar(cont);
      var pantalla = cont.dataset.pantalla;
      var reloj = null;
      var cerrarDialogo = null;

      function guardar() { E.almacen.guardar(ae); }
      var libre = c.modo === "normal" && !!c.navLibre;
      // Interactivo y guiado: ver un ejercicio ya hecho sin salir del actual.
      // No se guarda ni cambia nada: es solo lo que se muestra. (En el normal
      // "como en el parcial" no, porque mostraria la correccion antes del final.)
      var puedeRevisar = !libre && E.guiado(c);
      var revisar = null;   // indice del ejercicio ya hecho que se esta mirando
      function pendientes() { return it.preguntas.filter(function (r) { return !r.hecho && !r.salteado; }); }
      // con navegacion libre "la ultima" es cuando no queda ninguna otra por hacer
      function esLaUltima() {
        if (libre) { return pendientes().filter(function (r) { return r !== it.preguntas[it.actual]; }).length === 0; }
        if (conSaltear) { return otrasSinHacer().length === 0 && salteadas().length === 0; }
        return it.actual >= it.preguntas.length - 1;
      }

      // Interactivo: saltear es "dejar para despues".
      var conSaltear = c.modo === "interactivo";
      function otrasSinHacer() {
        return it.preguntas.filter(function (r, i) { return i !== it.actual && !r.hecho && !r.salteado; });
      }
      // indices de los salteados que todavia se pueden retomar (sin el actual)
      function salteadas() {
        var s = [];
        it.preguntas.forEach(function (r, i) { if (i !== it.actual && r.salteado && !r.hecho) { s.push(i); } });
        return s;
      }
      // Volver a un salteado: deja de estarlo y sigue donde quedo.
      function retomar(i) {
        it.preguntas[i].salteado = false;
        revisar = null;
        irA(i);
      }

      /* ---------- barra superior ---------- */

      var progresoTxt = h("span", { class: "ex-progreso-txt" });
      var relleno = h("span", { class: "ex-barra-relleno" });
      var tiempo = h("span", { class: "ex-tiempo" }, it.limite ? "" : "Sin límite");
      var vidas = E.conVidas(c) ? h("span", { class: "ex-vidas" }) : null;
      var casillas = libre ? h("div", { class: "cu-nav", "aria-label": "Ir a una pregunta" }) : null;

      cont.appendChild(h("div", { class: "ex-barra" }, [
        h("div", { class: "ex-barra-info" }, [
          h("span", { class: "ex-nombre" }, ae.nombre),
          h("span", { class: "ev-chip" }, E.nombreModo(c)),
          progresoTxt
        ]),
        h("div", { class: "ex-barra-acciones" }, [
          vidas,
          tiempo,
          libre ? h("button", { class: "ev-btn", type: "button", onclick: terminarLibre }, "Terminar") : null,
          h("button", { class: "ev-btn", type: "button", onclick: salir }, "Salir")
        ]),
        casillas,
        h("div", { class: "ex-barra-linea" }, relleno)
      ]));

      var zona = h("div", { class: "ex-zona" });
      cont.appendChild(zona);

      if (casillas) {
        it.preguntas.forEach(function (r, i) {
          casillas.appendChild(h("button", { class: "cu-casilla", type: "button", title: "Ir a la pregunta " + (i + 1),
            onclick: function () { irA(i); } }, String(i + 1)));
        });
      }

      function irA(i) {
        it.actual = i;
        guardar();
        pintar();
        window.scrollTo(0, 0);
      }

      function pintarBarra() {
        var hechas = it.preguntas.filter(function (r) { return r.hecho || r.salteado; }).length;
        var cual = c.modo === "interactivo" ? "Ejercicio " : "Pregunta ";
        progresoTxt.textContent = revisar !== null
          ? "Revisando " + cual.toLowerCase() + (revisar + 1) + " · en curso: " + (it.actual + 1) + " de " + it.preguntas.length
          : cual + (it.actual + 1) + " de " + it.preguntas.length;
        if (casillas) {
          Array.prototype.forEach.call(casillas.children, function (b, i) {
            b.classList.toggle("es-respondida", it.preguntas[i].hecho);
            b.classList.toggle("is-actual", i === it.actual);
          });
        }
        relleno.style.width = Math.round(100 * hechas / it.preguntas.length) + "%";
        if (vidas) {
          vidas.textContent = E.textoVidas(it.vidas);
          vidas.classList.toggle("ex-vidas-pocas", it.vidas <= 2);
        }
      }

      function textoQuedan(n) { return n === 1 ? "te queda 1 vida" : "te quedan " + n + " vidas"; }

      // Lo que se dice despues de un error: en el interactivo cuesta una vida;
      // en el estilo guiado no hay vidas, se vuelve a intentar.
      function textoError(inicio) {
        return E.conVidas(c)
          ? inicio + " Perdiste una vida: " + textoQuedan(it.vidas) + "."
          : inicio + " Probá de nuevo.";
      }

      // Resta una vida. Devuelve false si fue la ultima (y ya termino la autoevaluacion).
      function perderVida() {
        if (!E.conVidas(c)) { guardar(); return true; }
        it.vidas = Math.max(0, it.vidas - 1);
        guardar();
        pintarBarra();
        if (it.vidas === 0) { terminar("sin-vidas"); return false; }
        return true;
      }

      function detener() { if (reloj) { window.clearInterval(reloj); reloj = null; } }

      function tic() {
        if (cont.dataset.pantalla !== pantalla) { detener(); return; }   // se cambio de pantalla
        var resta = it.limite - Date.now();
        tiempo.textContent = "⏱ " + E.reloj(resta);
        tiempo.classList.toggle("ex-tiempo-poco", resta < 60000);
        if (resta <= 0) { terminar("tiempo"); }
      }

      // Sin contador se sale y listo. Con contador hay que decidir que pasa con el reloj.
      function salir() {
        guardar();
        if (!it.limite) {
          detener();
          acciones.volver("Saliste de “" + ae.nombre + "”. Tu progreso quedó guardado: tocá su tarjeta para seguir.");
          return;
        }
        cerrarDialogo = E.dialogo({
          titulo: "Tenés un contador en marcha",
          texto: "Quedan " + E.reloj(it.limite - Date.now()) + ". ¿Qué querés hacer con la autoevaluación?",
          botones: [
            { texto: "Cancelar", accion: function () {} },
            { texto: "Mantener contador", accion: function () {
              detener();
              acciones.volver("Saliste de “" + ae.nombre + "”. El contador sigue corriendo: volvé antes de que llegue a cero.");
            } },
            { texto: "Terminar", clase: "ev-btn-rojo", accion: function () { terminar("abandonada"); } }
          ]
        });
      }

      function terminar(motivo) {
        detener();
        if (cerrarDialogo) { cerrarDialogo(); }
        E.cerrarIntento(ae, motivo, motivo === "tiempo" ? it.limite : Date.now());
        if (motivo === "abandonada") {
          acciones.volver("“" + ae.nombre + "” quedó terminada. Tocá su tarjeta para ver el informe o rehacerla.");
          return;
        }
        acciones.informe(ae, motivo === "tiempo" ? "Se terminó el tiempo: la autoevaluación terminó."
          : motivo === "sin-vidas" ? "Te quedaste sin vidas: la autoevaluación terminó." : null);
      }

      function siguiente() {
        if (conSaltear) {
          // la proxima sin hacer (dando la vuelta); si no queda ninguna, la
          // pantalla de los salteados (un salteado en curso, con la lista)
          var total = it.preguntas.length;
          for (var m = 1; m <= total; m++) {
            var q = (it.actual + m) % total;
            if (!it.preguntas[q].hecho && !it.preguntas[q].salteado) { irA(q); return; }
          }
          var quedan = salteadas();
          if (quedan.length) { irA(quedan[0]); return; }
          // se salteo el ultimo que quedaba: se muestra, para retomarlo o terminar
          if (it.preguntas[it.actual].salteado && !it.preguntas[it.actual].hecho) { irA(it.actual); return; }
          terminar("completa");
          return;
        }
        if (esLaUltima()) { terminar("completa"); return; }
        if (libre) {
          // la proxima sin hacer, dando la vuelta si hace falta
          var n = it.preguntas.length;
          for (var k = 1; k <= n; k++) {
            var j = (it.actual + k) % n;
            if (!it.preguntas[j].hecho) { irA(j); return; }
          }
        }
        it.actual++;
        guardar();
        pintar();
        window.scrollTo(0, 0);
      }

      // Terminar cuando uno quiera (navegacion libre). Si quedan sin hacer, avisa.
      function terminarLibre() {
        var faltan = pendientes().length;
        if (!faltan) { terminar("completa"); return; }
        cerrarDialogo = E.dialogo({
          titulo: "¿Terminar ahora?",
          texto: (faltan === 1 ? "Te queda 1 pregunta sin responder" : "Te quedan " + faltan + " preguntas sin responder") +
                 ": en el informe van a figurar como sin responder.",
          botones: [
            { texto: "Seguir respondiendo" },
            { texto: "Terminar", clase: "ev-btn-primario", accion: function () { terminar("entregada"); } }
          ]
        });
      }

      // Barra de abajo de cada pregunta con navegacion libre: ir y volver sin responder.
      function navegacion() {
        if (!libre) { return null; }
        var r = it.preguntas[it.actual];
        return h("div", { class: "ex-nav" }, [
          h("button", { class: "ev-btn", type: "button", disabled: it.actual === 0 ? true : null,
            onclick: function () { irA(it.actual - 1); } }, "← Anterior"),
          h("span", { class: "ex-nav-espacio" }),
          it.actual < it.preguntas.length - 1
            ? h("button", { class: "ev-btn", type: "button", onclick: function () { irA(it.actual + 1); } },
                r.hecho ? "Siguiente →" : "Saltear →")
            : null
        ]);
      }

      // Interactivo: el ejercicio entero se puede dejar para otro momento.
      function botonSaltear(r) {
        if (c.modo !== "interactivo" || r.hecho) { return null; }
        return h("button", { class: "ev-btn ex-saltear", type: "button", onclick: function () {
          cerrarDialogo = E.dialogo({
            titulo: "¿Saltear este ejercicio?",
            texto: "Lo dejás para después: antes de terminar la autoevaluación podés volver y seguir donde lo dejaste. " +
                   "Si terminás sin completarlo, en el informe figura como salteado y no suma ni resta.",
            botones: [
              { texto: "Seguir con el ejercicio" },
              { texto: "Saltear el ejercicio", clase: "ev-btn-primario", accion: function () {
                r.salteado = true;
                guardar();
                siguiente();
              } }
            ]
          });
        } }, "Saltear ejercicio →");
      }

      /* ---------- piezas comunes ---------- */

      function botonSiguiente() {
        if (revisar !== null) {
          return h("button", { class: "ev-btn ev-btn-primario", type: "button", onclick: volverAlActual },
            c.modo === "interactivo" ? "Volver al ejercicio en curso →" : "Volver a la pregunta en curso →");
        }
        var texto = esLaUltima() ? "Terminar y ver informe"
          : conSaltear && !otrasSinHacer().length ? "Ver los salteados →" : "Siguiente pregunta →";
        return h("button", { class: "ev-btn ev-btn-primario", type: "button", onclick: siguiente }, texto);
      }

      // Un salteado en pantalla: retomarlo, o seguir. Si ya no queda nada sin
      // hacer, la lista de los salteados que faltan y la opcion de terminar.
      function pintarSalteado(tarjeta, p, r, idx) {
        tarjeta.appendChild(h("div", { class: "ex-enunciado", html: p.enunciado }));
        var donde = r.paso ? " Ibas por el paso " + (r.paso + 1) + ": seguís desde ahí." : "";
        tarjeta.appendChild(cartel("caja-ojo", "Lo salteaste",
          "<p>Lo dejaste para después." + donde + " Si terminás la autoevaluación sin completarlo, en el informe figura como salteado.</p>"));
        var acciones = h("div", { class: "ex-acciones" });
        acciones.appendChild(h("button", { class: "ev-btn ev-btn-primario", type: "button",
          onclick: function () { retomar(idx); } }, "Retomar este ejercicio"));
        if (revisar !== null) { acciones.appendChild(botonSiguiente()); }
        else if (otrasSinHacer().length) { acciones.appendChild(botonSiguiente()); }
        tarjeta.appendChild(acciones);

        // no queda nada sin hacer: lo que falta son salteados
        if (revisar === null && !otrasSinHacer().length) {
          var otros = salteadas();
          var caja = h("div", { class: "caja caja-formula ex-salteados" }, [
            h("span", { class: "caja-tit" }, "Terminaste los demás ejercicios"),
            h("p", {}, otros.length
              ? "Además de este, te quedan salteados:"
              : "Este es el único que te queda. Retomalo, o terminá: va a figurar como salteado.")
          ]);
          if (otros.length) {
            caja.appendChild(h("div", { class: "ex-salteados-lista" }, otros.map(function (i) {
              return h("button", { class: "ev-btn", type: "button", onclick: function () { retomar(i); } },
                "Retomar el ejercicio " + (i + 1));
            })));
          }
          caja.appendChild(h("div", { class: "ex-acciones" },
            h("button", { class: "ev-btn", type: "button", onclick: function () { terminar("completa"); } },
              "Terminar y ver informe (los salteados quedan como salteados)")));
          tarjeta.appendChild(caja);
        }
      }

      /* ---------- revisar lo ya hecho ---------- */

      // los que se pueden mirar: hechos o salteados, menos el que esta en curso
      function vistos() {
        var v = [];
        it.preguntas.forEach(function (r, i) { if (i !== it.actual && (r.hecho || r.salteado)) { v.push(i); } });
        return v;
      }
      function sePuedeVer(i) { return vistos().indexOf(i) !== -1; }

      function verEjercicio(i) {
        revisar = sePuedeVer(i) ? i : null;
        pintar();
        window.scrollTo(0, 0);
      }
      function volverAlActual() { verEjercicio(it.actual); }

      // Arriba de la tarjeta: ir al anterior; y mientras se revisa, moverse
      // entre los ya hechos o volver al que esta en curso.
      function navRevision(idx) {
        if (!puedeRevisar) { return null; }
        var cual = c.modo === "interactivo" ? "ejercicio" : "pregunta";
        var v = vistos();
        if (revisar === null) {
          if (!v.length) { return null; }
          // el mas cercano para atras (o el primero, si todos quedan adelante)
          var atras = v.filter(function (i) { return i < it.actual; });
          var ir = atras.length ? atras[atras.length - 1] : v[0];
          var haySalteados = conSaltear && salteadas().length;
          return h("div", { class: "ex-revision" }, [
            h("button", { class: "ev-btn", type: "button", onclick: function () { verEjercicio(ir); } },
              "← Ver " + (cual === "ejercicio" ? "los ejercicios anteriores" : "las preguntas anteriores") +
              (haySalteados ? " (y los salteados)" : ""))
          ]);
        }
        var pos = v.indexOf(idx);
        var salteado = it.preguntas[idx].salteado;
        return h("div", { class: "ex-revision es-revisando" }, [
          h("span", { class: "ex-revision-txt" },
            "Estás revisando " + (cual === "ejercicio" ? "el ejercicio " : "la pregunta ") + (idx + 1) +
            (salteado ? ", que salteaste" : ", ya hecho") + ". " +
            (cual === "ejercicio" ? "Tu ejercicio en curso es el " : "Tu pregunta en curso es la ") + (it.actual + 1) + "."),
          h("span", { class: "ex-nav-espacio" }),
          h("button", { class: "ev-btn", type: "button", disabled: pos <= 0 ? true : null,
            onclick: function () { verEjercicio(v[pos - 1]); } }, "← Anterior"),
          pos < v.length - 1
            ? h("button", { class: "ev-btn", type: "button", onclick: function () { verEjercicio(v[pos + 1]); } }, "Siguiente →")
            : null,
          h("button", { class: "ev-btn ev-btn-primario", type: "button", onclick: volverAlActual },
            "Volver " + (cual === "ejercicio" ? "al ejercicio en curso" : "a la pregunta en curso"))
        ]);
      }

      function cartel(clase, titulo, cuerpoHtml) {
        return h("div", { class: "caja " + clase }, [
          h("span", { class: "caja-tit" }, titulo),
          cuerpoHtml ? h("div", { html: cuerpoHtml }) : null
        ]);
      }

      function botonPista(pistaHtml, registro, destino) {
        if (!pistaHtml) { return null; }
        var caja = cartel("caja-ejemplo ex-pista", "Pista", pistaHtml);
        caja.hidden = true;
        destino.appendChild(caja);
        return h("button", { class: "ex-lampara", type: "button", title: "Ver una pista", onclick: function () {
          if (caja.hidden && !registro.pistaVista) { registro.pistas++; registro.pistaVista = true; guardar(); }
          caja.hidden = !caja.hidden;
          E.tipografiar(caja);
        } }, "💡 Pista");
      }

      // Botones de opciones. alElegir(indiceOriginal, boton)
      function listaOpciones(opciones, registro, alElegir) {
        var caja = h("div", { class: "ex-opciones" });
        ordenDe(registro, opciones.textos.length).forEach(function (orig, k) {
          var b = h("button", { class: "ex-op", type: "button", "data-orig": orig }, [
            h("span", { class: "ex-letra" }, E.LETRAS[k]),
            h("span", { class: "ex-op-txt", html: opciones.textos[orig] })
          ]);
          b.addEventListener("click", function () { alElegir(orig, b); });
          caja.appendChild(b);
        });
        return caja;
      }

      function marcarOpciones(lista, correcta, elegida, descartadas) {
        Array.prototype.forEach.call(lista.children, function (b) {
          var orig = parseInt(b.getAttribute("data-orig"), 10);
          b.disabled = true;
          b.classList.toggle("es-correcta", orig === correcta);
          b.classList.toggle("es-incorrecta", orig !== correcta && (orig === elegida || (descartadas || []).indexOf(orig) !== -1));
        });
      }

      function letraDe(registro, orig) { return E.LETRAS[registro.orden.indexOf(orig)]; }

      function enunciado(tarjeta, p) {
        tarjeta.appendChild(h("div", { class: "ex-enunciado", html: p.enunciado }));
        if (p.pregunta) { tarjeta.appendChild(h("div", { class: "ex-pregunta", html: p.pregunta })); }
      }

      /* ---------- NORMAL ---------- */

      function pintarNormal(tarjeta, p, r) {
        enunciado(tarjeta, p);
        if (libre && !c.verRespuesta) { pintarNormalCambiable(tarjeta, p, r); return; }
        var seleccion = null;
        var lista = listaOpciones(p.opciones, r, function (orig, boton) {
          if (r.hecho) { return; }
          seleccion = orig;
          Array.prototype.forEach.call(lista.children, function (b) { b.classList.toggle("is-sel", b === boton); });
          boton.blur();
          btn.disabled = false;
        });
        tarjeta.appendChild(lista);
        var devolucion = h("div", { class: "ex-devolucion" });
        var pie = h("div", { class: "ex-acciones" });
        var btn = h("button", { class: "ev-btn ev-btn-primario", type: "button", disabled: true }, "Responder");
        tarjeta.appendChild(devolucion);
        tarjeta.appendChild(pie);

        function corregir() {
          marcarOpciones(lista, p.opciones.correcta, r.elegida);
          devolucion.appendChild(r.ok
            ? cartel("caja-resp", "¡Correcto!", p.explicacion)
            : cartel("caja-ojo", "Incorrecto. La respuesta correcta es la " + letraDe(r, p.opciones.correcta), p.explicacion));
          E.vaciar(pie);
          pie.appendChild(botonSiguiente());
          E.tipografiar(devolucion);
        }

        btn.addEventListener("click", function () {
          if (seleccion === null) { return; }
          r.elegida = seleccion;
          r.ok = seleccion === p.opciones.correcta;
          r.hecho = true;
          guardar();
          pintarBarra();
          if (c.verRespuesta) { corregir(); } else { siguiente(); }
        });

        if (r.hecho) { corregir(); } else { pie.appendChild(btn); }
      }

      /* Navegacion libre sin correccion inmediata: como la 1ra instancia, se
         marca una opcion y queda guardada; se puede cambiar hasta terminar. */
      function pintarNormalCambiable(tarjeta, p, r) {
        var lista = listaOpciones(p.opciones, r, function (orig, boton) {
          r.elegida = orig;
          r.ok = orig === p.opciones.correcta;
          r.hecho = true;
          guardar();
          pintarBarra();
          Array.prototype.forEach.call(lista.children, function (b) { b.classList.toggle("is-sel", b === boton); });
          boton.blur();
          E.vaciar(pie);
          pie.appendChild(h("span", { class: "ae-ayuda" }, "Guardada. Podés cambiarla hasta terminar."));
          pie.appendChild(botonSiguiente());
        });
        tarjeta.appendChild(lista);
        var pie = h("div", { class: "ex-acciones" });
        tarjeta.appendChild(pie);
        if (r.hecho) {
          var b = lista.querySelector('[data-orig="' + r.elegida + '"]');
          if (b) { b.classList.add("is-sel"); }
          pie.appendChild(h("span", { class: "ae-ayuda" }, "Guardada. Podés cambiarla hasta terminar."));
          pie.appendChild(botonSiguiente());
        }
      }

      /* ---------- INTERACTIVO: una pregunta con opciones ---------- */

      function pintarOpcionesInteractivas(tarjeta, p, r) {
        enunciado(tarjeta, p);
        var zonaPista = h("div");
        var devolucion = h("div", { class: "ex-devolucion" });
        var pie = h("div", { class: "ex-acciones" });
        var lampara = botonPista(p.pista, r, zonaPista);

        var lista = listaOpciones(p.opciones, r, function (orig, boton) {
          if (r.hecho || boton.disabled) { return; }
          E.vaciar(devolucion);
          if (orig === p.opciones.correcta) {
            r.hecho = true; r.ok = r.fallos === 0; r.elegida = orig;
            guardar();
            pintarBarra();
            resuelta();
            return;
          }
          r.fallos++;
          r.descartadas.push(orig);
          boton.disabled = true;
          boton.classList.add("es-incorrecta");
          if (!perderVida()) { return; }
          devolucion.appendChild(cartel("caja-ojo ex-cartel", textoError("No es esa.")));
        });

        function resuelta() {
          marcarOpciones(lista, p.opciones.correcta, r.elegida, r.descartadas);
          E.vaciar(devolucion);
          devolucion.appendChild(r.ok
            ? cartel("caja-resp", "¡Correcto al primer intento!", p.explicacion)
            : cartel("caja-formula", "¡Correcto! (con " + r.fallos + (r.fallos === 1 ? " fallo)" : " fallos)"), p.explicacion));
          if (lampara) { lampara.disabled = true; }
          pie.appendChild(botonSiguiente());
          E.tipografiar(devolucion);
        }

        if (lampara) { tarjeta.appendChild(h("div", { class: "ex-herramientas" }, lampara)); }
        tarjeta.appendChild(zonaPista);
        tarjeta.appendChild(lista);
        tarjeta.appendChild(devolucion);
        tarjeta.appendChild(pie);

        r.descartadas.forEach(function (orig) {
          var b = lista.querySelector('[data-orig="' + orig + '"]');
          if (b) { b.disabled = true; b.classList.add("es-incorrecta"); }
        });
        if (r.hecho) { resuelta(); }
      }

      /* ---------- INTERACTIVO: ejercicio de practica paso a paso ---------- */

      /* El enunciado va en su propia columna, que queda fija al costado mientras
         se avanza: los pasos se van acumulando y el enunciado no se pierde de
         vista. En pantallas angostas va arriba, como antes (evaluacion.css). */
      function pintarPasos(tarjeta, p, r, pasos) {
        var col = h("div", { class: "ex-pasos-col" });
        tarjeta.appendChild(h("div", { class: "ex-con-enunciado" }, [
          h("aside", { class: "ex-enunciado-lado" }, [
            h("div", { class: "ex-enunciado-tit" }, "Enunciado"),
            h("div", { class: "ex-enunciado ex-enunciado-fijo", html: p.enunciado })
          ]),
          col
        ]));
        var lista = h("ol", { class: "ex-pasos" });
        col.appendChild(lista);
        var actual = null;

        pasos.forEach(function (paso, k) {
          if (k > r.paso) { return; }
          var ep = r.pasos[k] = r.pasos[k] || { ok: null, fallos: 0, pistas: 0, dada: null, orden: null, descartadas: [] };
          var nuevoInciso = paso.inciso && (k === 0 || pasos[k - 1].inciso !== paso.inciso);
          if (nuevoInciso) { lista.appendChild(h("li", { class: "ex-inciso" }, "Inciso " + paso.inciso + ")")); }
          var cab = (paso.inciso ? "Inciso " + paso.inciso + ") · " : "") + "Paso " + (k + 1) + " de " + pasos.length;
          var li;
          if (k < r.paso) {
            li = h("li", { class: "ex-paso es-bien" });
            pasoHecho(li, paso, ep, cab, k === r.paso - 1);
          } else {
            li = h("li", { class: "ex-paso es-actual" }, [
              h("div", { class: "ex-paso-cab" }, cab),
              h("div", { class: "ex-paso-consigna", html: paso.consigna })
            ]);
            actual = li;
            pasoActual(li, paso, ep, k, r);
          }
          lista.appendChild(li);
          // termino el inciso (su ultimo paso en este nivel): la respuesta final en palabras
          if (k < r.paso && finDeInciso(pasos, k) && p.rtas && p.rtas[paso.inciso]) {
            lista.appendChild(h("li", { class: "ex-rta" }, [
              h("span", { class: "ex-rta-tit" }, "Rta. inciso " + paso.inciso + ")"),
              h("div", { html: p.rtas[paso.inciso] })
            ]));
          }
        });

        if (r.paso >= pasos.length) {
          var detalle = [];
          if (r.fallos) { detalle.push(r.fallos + (r.fallos === 1 ? " fallo" : " fallos")); }
          if (r.resueltos) { detalle.push(r.resueltos + (r.resueltos === 1 ? " paso resuelto" : " pasos resueltos")); }
          col.appendChild(cartel(r.ok ? "caja-resp" : "caja-formula",
            r.ok ? "¡Ejercicio completo sin errores!" : "¡Ejercicio completo! (con " + detalle.join(" y ") + ")", p.explicacion));
          col.appendChild(h("div", { class: "ex-acciones" }, botonSiguiente()));
        } else if (c.modo === "interactivo") {
          col.appendChild(h("div", { class: "ex-acciones" }, botonSaltear(r)));
        }
        return actual;
      }

      function finDeInciso(pasos, k) {
        return !!pasos[k].inciso && (k === pasos.length - 1 || pasos[k + 1].inciso !== pasos[k].inciso);
      }

      function respuestaDe(paso) {
        return paso.opciones
          ? h("span", { html: paso.opciones.textos[paso.opciones.correcta] })
          : h("b", {}, paso.respuesta);
      }

      // Lo que muestra "Resolver". Si el paso no trae su resolucion escrita,
      // se arma con lo que tiene: que se pide, como se piensa y la cuenta.
      function resolucionDe(paso) {
        var cuerpo = h("div", { class: "ex-resolucion-cuerpo" });
        if (paso.resolucion) {
          cuerpo.appendChild(h("div", { html: paso.resolucion }));
        } else {
          cuerpo.appendChild(h("p", {}, [h("strong", {}, "Qué se pide: "), h("span", { html: paso.consigna })]));
          if (paso.pista) { cuerpo.appendChild(h("p", {}, [h("strong", {}, "Cómo se piensa: "), h("span", { html: paso.pista })])); }
          if (paso.explicacion) { cuerpo.appendChild(h("p", {}, [h("strong", {}, "La cuenta: "), h("span", { html: paso.explicacion })])); }
        }
        cuerpo.appendChild(h("p", { class: "ex-resolucion-resp" }, [h("strong", {}, "Respuesta: "), respuestaDe(paso)]));
        return cuerpo;
      }

      // Un paso ya hecho es un renglon compacto (consigna y respuesta) que se
      // despliega para ver la explicacion, o la resolucion si lo hizo el boton
      // Resolver. ultimo: el paso que se acaba de hacer, que queda abierto.
      function pasoHecho(li, paso, ep, cab, ultimo) {
        if (ep.resuelto) { li.classList.add("es-resuelto"); }
        var cuerpo = ep.resuelto
          ? h("div", { class: "ex-resolucion" }, [h("div", { class: "ex-resolucion-tit" }, "Resolución paso a paso"), resolucionDe(paso)])
          : (paso.explicacion ? h("div", { class: "ex-paso-explicacion", html: paso.explicacion }) : null);
        // Resuelto por uno mismo: igual se puede leer la resolucion completa, como
        // si se hubiera tocado Resolver (sin marcarlo como resuelto por el campus).
        var zonaRes = null, verRes = null;
        if (!ep.resuelto) {
          zonaRes = h("div", { class: "ex-resolucion", hidden: true },
            h("div", { class: "ex-resolucion-tit" }, "Resolución paso a paso"));
          verRes = h("button", { class: "ex-paso-verres", type: "button",
            title: "Ver cómo se resuelve este paso, explicado", onclick: function (ev) {
              ev.preventDefault();      // es un boton dentro del renglon: que no lo pliegue
              ev.stopPropagation();
              if (!zonaRes.dataset.lleno) { zonaRes.appendChild(resolucionDe(paso)); zonaRes.dataset.lleno = "1"; }
              zonaRes.hidden = !zonaRes.hidden;
              if (!zonaRes.hidden) { det.open = true; E.tipografiar(zonaRes); }
              verRes.textContent = zonaRes.hidden ? "📖 Ver resolución" : "Ocultar resolución";
            } }, "📖 Ver resolución");
        }
        var det = h("details", { class: "ex-paso-log" }, [
          h("summary", {}, [
            h("div", { class: "ex-paso-cab" }, [cab, cuerpo
              ? h("span", { class: "ex-paso-ver", "data-que": ep.resuelto ? "la resolución" : "la explicación" }) : null,
              verRes]),
            h("div", { class: "ex-paso-consigna", html: paso.consigna }),
            h("div", { class: "ex-paso-resultado" }, [ep.resuelto ? "Resuelto: " : "✓ ", respuestaDe(paso),
              ep.fallos ? h("small", {}, " · " + ep.fallos + (ep.fallos === 1 ? " fallo" : " fallos")) : null])
          ]),
          cuerpo,
          zonaRes
        ]);
        if (ultimo) { det.open = true; if (ep.resuelto) { liResuelto = li; } }
        li.appendChild(det);
      }

      var liResuelto = null;   // el paso recien resuelto con el boton, para llevar la vista ahi

      function pasoActual(li, paso, ep, k, r) {
        var zonaPista = h("div");
        var devolucion = h("div", { class: "ex-devolucion" });
        var lampara = botonPista(paso.pista, ep, zonaPista);

        function resolver() {
          ep.ok = true;
          r.paso = k + 1;
          var pasos = B.pasosDelNivel(B.obtener(materia, r.id), E.nivelDe(c));
          if (r.paso >= pasos.length) {
            r.hecho = true;
            r.ok = r.fallos === 0 && !r.resueltos;
          }
          guardar();
          pintarBarra();
          pintar(true);
        }

        // Boton "Resolver": el campus hace el paso, muestra como y sigue.
        var botonResolver = h("button", { class: "ex-resolver", type: "button",
          title: "Ver la resolución de este paso, explicada, y pasar al siguiente", onclick: function () {
            ep.resuelto = true;
            r.resueltos = (r.resueltos || 0) + 1;
            resolver();
          } }, "📖 Resolver");

        // devuelve false si era la ultima vida
        function fallo() {
          ep.fallos++;
          r.fallos++;
          if (!perderVida()) { return false; }
          E.vaciar(devolucion);
          devolucion.appendChild(cartel("caja-ojo ex-cartel", textoError("No da. Revisá la cuenta.")));
          return true;
        }

        var respuesta;
        if (paso.opciones) {
          respuesta = listaOpciones(paso.opciones, ep, function (orig, boton) {
            if (boton.disabled) { return; }
            if (orig === paso.opciones.correcta) { resolver(); return; }
            ep.descartadas.push(orig);
            boton.disabled = true;
            boton.classList.add("es-incorrecta");
            fallo();
          });
          ep.descartadas.forEach(function (orig) {
            var b = respuesta.querySelector('[data-orig="' + orig + '"]');
            if (b) { b.disabled = true; b.classList.add("es-incorrecta"); }
          });
        } else {
          var entrada = h("input", { class: "ae-input ex-entrada", type: "text", inputmode: "decimal",
            autocomplete: "off", placeholder: "Tu resultado (ej: 0,25)" });
          var comprobar = function () {
            if (!entrada.value.trim()) { entrada.focus(); return; }
            if (isNaN(B.numero(entrada.value))) {
              E.vaciar(devolucion);
              devolucion.appendChild(cartel("caja-ojo ex-cartel", "Escribí solo el número (podés usar coma o una fracción como 3/4)."));
              return;
            }
            if (B.comprobarNumero(entrada.value, paso)) { ep.dada = entrada.value; resolver(); }
            else if (fallo()) { entrada.select(); }
          };
          entrada.addEventListener("keydown", function (ev) { if (ev.key === "Enter") { ev.preventDefault(); comprobar(); } });
          respuesta = h("div", { class: "ex-linea-respuesta" }, [
            entrada,
            h("button", { class: "ev-btn ev-btn-primario", type: "button", onclick: comprobar }, "Comprobar")
          ]);
        }

        li.appendChild(h("div", { class: "ex-herramientas" }, [lampara, botonResolver]));
        li.appendChild(zonaPista);
        li.appendChild(respuesta);
        li.appendChild(devolucion);
      }

      /* ---------- pregunta actual ---------- */

      function pintar(mismaPregunta) {
        if (it.actual >= it.preguntas.length) { terminar("completa"); return; }
        if (revisar !== null && !sePuedeVer(revisar)) { revisar = null; }
        pintarBarra();
        var idx = revisar !== null ? revisar : it.actual;
        var r = it.preguntas[idx];
        var p = B.obtener(materia, r.id);
        E.vaciar(zona);
        liResuelto = null;
        var navRev = navRevision(idx);
        if (navRev) { zona.appendChild(navRev); }

        if (!p) {
          r.hecho = true; r.ok = false;
          zona.appendChild(h("div", { class: "ex-tarjeta" }, [
            cartel("caja-ojo", "Esta pregunta ya no está en el banco", "<p>Se la cuenta como no respondida bien.</p>"),
            h("div", { class: "ex-acciones" }, botonSiguiente())
          ]));
          return;
        }

        var conPasos = E.guiado(c) && (p.tipo === "practica" || p.tipo === "ejercicio");
        var pasos = conPasos ? B.pasosDelNivel(p, E.nivelDe(c)) : [];
        var etiquetas = [
          h("span", { class: "ev-chip ev-chip-" + p.tipo }, E.TIPOS[p.tipo]),
          h("span", { class: "ev-chip" }, E.numeroDeUnidad(materia, p.unidad)),
          E.chipOrigen(p)
        ];
        if (pasos.length && c.modo === "interactivo") { etiquetas.push(h("span", { class: "ev-chip" }, "Nivel " + E.NIVELES[c.nivel].toLowerCase())); }
        var tarjeta = h("div", { class: "ex-tarjeta" + (revisar !== null ? " es-revision" : "") }, h("div", { class: "ex-etiquetas" }, etiquetas));
        zona.appendChild(tarjeta);

        var actual = null;
        if (r.salteado) { pintarSalteado(tarjeta, p, r, idx); }
        else if (!E.guiado(c)) { pintarNormal(tarjeta, p, r); }
        else if (pasos.length) { actual = pintarPasos(tarjeta, p, r, pasos); }
        else { pintarOpcionesInteractivas(tarjeta, p, r); }
        var nav = navegacion();
        if (nav) { tarjeta.appendChild(nav); }

        E.tipografiar(zona);
        var barraFija = document.querySelector(".ex-barra");
        if (barraFija) {
          tarjeta.style.setProperty("--ex-tope",
            ((parseFloat(window.getComputedStyle(barraFija).top) || 0) + barraFija.offsetHeight + 14) + "px");
        }
        if (mismaPregunta && liResuelto) {
          // recien resuelto con el boton: primero se lee la resolucion
          // debajo de la barra fija de la autoevaluacion (vidas, ejercicio N de M)
          var barra = document.querySelector(".ex-barra");
          var tapa = barra ? barra.getBoundingClientRect().bottom : 90;
          window.scrollBy(0, liResuelto.getBoundingClientRect().top - tapa - 12);
        } else if (mismaPregunta && actual) {
          actual.scrollIntoView({ block: "center" });
          var entrada = actual.querySelector(".ex-entrada");
          if (entrada) { entrada.focus({ preventScroll: true }); }
        }
      }

      pintar();
      if (window.NC.reconstruirIndice) { window.NC.reconstruirIndice(); }
      window.scrollTo(0, 0);
      if (it.limite) { tic(); reloj = window.setInterval(tic, 500); }
    }
  };
})(window.NC.eval);
