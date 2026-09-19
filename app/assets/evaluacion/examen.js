/* ============================================================
   NEWCAMPUS - Evaluacion: autoevaluacion en curso
   NORMAL:      enunciado completo + opciones. Corrige al responder o al final.
   INTERACTIVO: pistas con la lamparita y vidas: cada error resta una y se puede
                reintentar; sin vidas, la autoevaluacion termina.
                En practica pide el ejercicio paso a paso segun el nivel.
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
      vidas: c.modo === "interactivo" ? c.fallos : null,
      actual: 0,
      preguntas: E.banco.seleccionar(materia, c).map(function (id) {
        return { id: id, hecho: false, ok: null, elegida: null, orden: null,
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
      function esLaUltima() { return it.actual >= it.preguntas.length - 1; }

      /* ---------- barra superior ---------- */

      var progresoTxt = h("span", { class: "ex-progreso-txt" });
      var relleno = h("span", { class: "ex-barra-relleno" });
      var tiempo = h("span", { class: "ex-tiempo" }, it.limite ? "" : "Sin límite");
      var vidas = c.modo === "interactivo" ? h("span", { class: "ex-vidas" }) : null;

      cont.appendChild(h("div", { class: "ex-barra" }, [
        h("div", { class: "ex-barra-info" }, [
          h("span", { class: "ex-nombre" }, ae.nombre),
          h("span", { class: "ev-chip" }, E.MODOS[c.modo] + (c.modo === "interactivo" ? " · " + E.NIVELES[c.nivel] : "")),
          progresoTxt
        ]),
        h("div", { class: "ex-barra-acciones" }, [
          vidas,
          tiempo,
          h("button", { class: "ev-btn", type: "button", onclick: salir }, "Salir")
        ]),
        h("div", { class: "ex-barra-linea" }, relleno)
      ]));

      var zona = h("div", { class: "ex-zona" });
      cont.appendChild(zona);

      function pintarBarra() {
        var hechas = it.preguntas.filter(function (r) { return r.hecho; }).length;
        progresoTxt.textContent = "Pregunta " + (it.actual + 1) + " de " + it.preguntas.length;
        relleno.style.width = Math.round(100 * hechas / it.preguntas.length) + "%";
        if (vidas) {
          vidas.textContent = E.textoVidas(it.vidas);
          vidas.classList.toggle("ex-vidas-pocas", it.vidas <= 2);
        }
      }

      function textoQuedan(n) { return n === 1 ? "te queda 1 vida" : "te quedan " + n + " vidas"; }

      // Resta una vida. Devuelve false si fue la ultima (y ya termino la autoevaluacion).
      function perderVida() {
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
        if (esLaUltima()) { terminar("completa"); return; }
        it.actual++;
        guardar();
        pintar();
        window.scrollTo(0, 0);
      }

      /* ---------- piezas comunes ---------- */

      function botonSiguiente() {
        return h("button", { class: "ev-btn ev-btn-primario", type: "button", onclick: siguiente },
          esLaUltima() ? "Terminar y ver informe" : "Siguiente pregunta →");
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
          devolucion.appendChild(cartel("caja-ojo ex-cartel", "No es esa. Perdiste una vida: " + textoQuedan(it.vidas) + "."));
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

      function pintarPasos(tarjeta, p, r, pasos) {
        tarjeta.appendChild(h("div", { class: "ex-enunciado ex-enunciado-fijo", html: p.enunciado }));
        var lista = h("ol", { class: "ex-pasos" });
        tarjeta.appendChild(lista);
        var actual = null;

        pasos.forEach(function (paso, k) {
          if (k > r.paso) { return; }
          var ep = r.pasos[k] = r.pasos[k] || { ok: null, fallos: 0, pistas: 0, dada: null, orden: null, descartadas: [] };
          var li = h("li", { class: "ex-paso" + (k < r.paso ? " es-bien" : " es-actual") }, [
            h("div", { class: "ex-paso-cab" }, "Paso " + (k + 1) + " de " + pasos.length),
            h("div", { class: "ex-paso-consigna", html: paso.consigna })
          ]);
          lista.appendChild(li);
          if (k < r.paso) { pasoHecho(li, paso, ep); } else { actual = li; pasoActual(li, paso, ep, k, r); }
        });

        if (r.paso >= pasos.length) {
          tarjeta.appendChild(cartel(r.ok ? "caja-resp" : "caja-formula",
            r.ok ? "¡Ejercicio completo sin errores!" : "¡Ejercicio completo! (con " + r.fallos + (r.fallos === 1 ? " fallo)" : " fallos)"), p.explicacion));
          tarjeta.appendChild(h("div", { class: "ex-acciones" }, botonSiguiente()));
        }
        return actual;
      }

      function pasoHecho(li, paso, ep) {
        var textoRespuesta = paso.opciones
          ? h("span", { html: paso.opciones.textos[paso.opciones.correcta] })
          : h("b", {}, paso.respuesta);
        li.appendChild(h("div", { class: "ex-paso-resultado" },
          ["✓ ", textoRespuesta, ep.fallos ? h("small", {}, " · " + ep.fallos + (ep.fallos === 1 ? " fallo" : " fallos")) : null]));
        if (paso.explicacion) { li.appendChild(h("div", { class: "ex-paso-explicacion", html: paso.explicacion })); }
      }

      function pasoActual(li, paso, ep, k, r) {
        var zonaPista = h("div");
        var devolucion = h("div", { class: "ex-devolucion" });
        var lampara = botonPista(paso.pista, ep, zonaPista);

        function resolver() {
          ep.ok = true;
          r.paso = k + 1;
          var pasos = B.pasosDelNivel(B.obtener(materia, r.id), c.nivel);
          if (r.paso >= pasos.length) {
            r.hecho = true;
            r.ok = r.fallos === 0;
          }
          guardar();
          pintarBarra();
          pintar(true);
        }

        // devuelve false si era la ultima vida
        function fallo() {
          ep.fallos++;
          r.fallos++;
          if (!perderVida()) { return false; }
          E.vaciar(devolucion);
          devolucion.appendChild(cartel("caja-ojo ex-cartel", "No da. Revisá la cuenta. Perdiste una vida: " + textoQuedan(it.vidas) + "."));
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

        if (lampara) { li.appendChild(h("div", { class: "ex-herramientas" }, lampara)); }
        li.appendChild(zonaPista);
        li.appendChild(respuesta);
        li.appendChild(devolucion);
      }

      /* ---------- pregunta actual ---------- */

      function pintar(mismaPregunta) {
        if (it.actual >= it.preguntas.length) { terminar("completa"); return; }
        pintarBarra();
        var r = it.preguntas[it.actual];
        var p = B.obtener(materia, r.id);
        E.vaciar(zona);

        if (!p) {
          r.hecho = true; r.ok = false;
          zona.appendChild(h("div", { class: "ex-tarjeta" }, [
            cartel("caja-ojo", "Esta pregunta ya no está en el banco", "<p>Se la cuenta como no respondida bien.</p>"),
            h("div", { class: "ex-acciones" }, botonSiguiente())
          ]));
          return;
        }

        var pasos = c.modo === "interactivo" && p.tipo === "practica" ? B.pasosDelNivel(p, c.nivel) : [];
        var etiquetas = [
          h("span", { class: "ev-chip ev-chip-" + p.tipo }, E.TIPOS[p.tipo]),
          h("span", { class: "ev-chip" }, E.numeroDeUnidad(materia, p.unidad))
        ];
        if (pasos.length) { etiquetas.push(h("span", { class: "ev-chip" }, "Nivel " + E.NIVELES[c.nivel].toLowerCase())); }
        var tarjeta = h("div", { class: "ex-tarjeta" }, h("div", { class: "ex-etiquetas" }, etiquetas));
        zona.appendChild(tarjeta);

        var actual = null;
        if (c.modo === "normal") { pintarNormal(tarjeta, p, r); }
        else if (pasos.length) { actual = pintarPasos(tarjeta, p, r, pasos); }
        else { pintarOpcionesInteractivas(tarjeta, p, r); }

        E.tipografiar(zona);
        if (mismaPregunta && actual) {
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
