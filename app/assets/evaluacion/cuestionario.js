/* ============================================================
   NEWCAMPUS - Evaluacion: 1ra etapa del parcial (cuestionario virtual)
   Imita el Cuestionario del Aula Virtual con el que la catedra toma la
   primera instancia: todas las preguntas en una pagina, se contesta en
   cualquier orden, se entrega al final y recien ahi se corrige.
     opcion     Seleccione una (incluye Verdadero / Falso)
     multiple   Seleccione una o mas de una, con puntaje parcial
     completar  huecos numericos (coma y 2 decimales) y desplegables
   No hay modo interactivo, ni pistas, ni vidas. La nota es sobre 100 y el
   informe dice que significa segun el reglamento (30 / 60).
   Cada respuesta se guarda al instante, asi se puede salir y continuar.
   ============================================================ */

(function (E) {
  "use strict";

  var CONSIGNA = { opcion: "Seleccione una:", multiple: "Seleccione una o más de una:" };

  function crearIntento(materia, ae) {
    var c = ae.config;
    var ahora = Date.now();
    ae.intento = {
      estado: "en-curso",
      config: JSON.parse(JSON.stringify(c)),
      inicio: ahora,
      fin: null,
      limite: c.conTiempo ? ahora + c.minutos * 60000 : null,
      actual: 0,
      preguntas: E.banco.seleccionar(materia, c).map(function (id) {
        return { id: id, respuesta: null, orden: null, hecho: false, fraccion: null, ok: null };
      })
    };
  }

  // Verdadero / Falso no se mezcla: en el Aula Virtual siempre va en ese orden.
  function ordenDe(r, p) {
    var n = p.opciones.textos.length;
    if (!r.orden || r.orden.length !== n) {
      var indices = [];
      for (var i = 0; i < n; i++) { indices.push(i); }
      r.orden = n === 2 ? indices : E.mezclar(indices);
    }
    return r.orden;
  }

  function puntosDe(it) { return it.preguntas.length ? 100 / it.preguntas.length : 0; }

  function respondida(r) { return r.respuesta !== null && r.respuesta !== undefined; }

  /* El enunciado trae los huecos como <span class="p-hueco">. Se cambian por
     un campo o un desplegable. armar(i, hueco, span) devuelve el elemento nuevo. */
  function enunciadoConHuecos(p, armar) {
    var caja = E.h("div", { class: "ex-enunciado", html: p.enunciado });
    Array.prototype.forEach.call(caja.querySelectorAll(".p-hueco"), function (span, i) {
      span.parentNode.replaceChild(armar(i, p.huecos[i], span), span);
    });
    return caja;
  }

  // Cabecera de cada pregunta: el recuadro de la izquierda del Aula Virtual.
  function info(numero, estado, puntaje) {
    return E.h("div", { class: "cu-info" }, [
      E.h("span", { class: "cu-info-num" }, ["Pregunta ", E.h("b", {}, String(numero))]),
      E.h("span", { class: "cu-info-estado" }, estado),
      E.h("span", { class: "cu-info-pts" }, puntaje)
    ]);
  }

  function etiquetas(materia, p) {
    return E.h("div", { class: "ex-etiquetas" }, [
      E.h("span", { class: "ev-chip" }, E.numeroDeUnidad(materia, p.unidad)),
      E.chipOrigen(p)
    ]);
  }

  E.cuestionario = {
    /* acciones: { volver(aviso), informe(ae, aviso) } */
    lanzar: function (cont, materia, ae, reiniciar, acciones) {
      var h = E.h, B = E.banco;

      E.estadoDe(ae);
      if (reiniciar || !ae.intento || ae.intento.estado !== "en-curso") { crearIntento(materia, ae); }
      var it = ae.intento;

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
      var puntos = E.nota(puntosDe(it));

      function guardar() { E.almacen.guardar(ae); }

      /* ---------- barra superior ---------- */

      var progresoTxt = h("span", { class: "ex-progreso-txt" });
      var relleno = h("span", { class: "ex-barra-relleno" });
      var tiempo = h("span", { class: "ex-tiempo" }, it.limite ? "" : "Sin límite");
      var casillas = h("div", { class: "cu-nav", "aria-label": "Navegación por el cuestionario" });

      cont.appendChild(h("div", { class: "ex-barra" }, [
        h("div", { class: "ex-barra-info" }, [
          h("span", { class: "ex-nombre" }, ae.nombre),
          h("span", { class: "ev-chip ev-chip-etapa" }, "1ra etapa · Cuestionario"),
          progresoTxt
        ]),
        h("div", { class: "ex-barra-acciones" }, [
          tiempo,
          h("button", { class: "ev-btn", type: "button", onclick: salir }, "Salir")
        ]),
        casillas,
        h("div", { class: "ex-barra-linea" }, relleno)
      ]));

      function pintarBarra() {
        var hechas = it.preguntas.filter(respondida).length;
        progresoTxt.textContent = "Respondidas " + hechas + " de " + it.preguntas.length;
        relleno.style.width = Math.round(100 * hechas / it.preguntas.length) + "%";
        Array.prototype.forEach.call(casillas.children, function (b, i) {
          b.classList.toggle("es-respondida", respondida(it.preguntas[i]));
        });
      }

      function detener() { if (reloj) { window.clearInterval(reloj); reloj = null; } }

      function tic() {
        if (cont.dataset.pantalla !== pantalla) { detener(); return; }
        var resta = it.limite - Date.now();
        tiempo.textContent = "⏱ " + E.reloj(resta);
        tiempo.classList.toggle("ex-tiempo-poco", resta < 60000);
        if (resta <= 0) { terminar("tiempo"); }
      }

      function salir() {
        guardar();
        if (!it.limite) {
          detener();
          acciones.volver("Saliste de “" + ae.nombre + "”. Tus respuestas quedaron guardadas: tocá su tarjeta para seguir.");
          return;
        }
        cerrarDialogo = E.dialogo({
          titulo: "Tenés un contador en marcha",
          texto: "Quedan " + E.reloj(it.limite - Date.now()) + ". ¿Qué querés hacer con el cuestionario?",
          botones: [
            { texto: "Cancelar" },
            { texto: "Mantener contador", accion: function () {
              detener();
              acciones.volver("Saliste de “" + ae.nombre + "”. El contador sigue corriendo: volvé antes de que llegue a cero.");
            } },
            { texto: "Entregar ahora", clase: "ev-btn-rojo", accion: function () { terminar("completa"); } }
          ]
        });
      }

      function terminar(motivo) {
        detener();
        if (cerrarDialogo) { cerrarDialogo(); }
        E.cerrarIntento(ae, motivo, motivo === "tiempo" ? it.limite : Date.now());
        acciones.informe(ae, motivo === "tiempo"
          ? "Se terminó el tiempo: se entregó lo que tenías contestado." : null);
      }

      function entregar() {
        var faltan = it.preguntas.filter(function (r) { return !respondida(r); }).length;
        cerrarDialogo = E.dialogo({
          titulo: "¿Enviar todo y terminar?",
          texto: (faltan ? "Te quedan " + faltan + (faltan === 1 ? " pregunta sin responder, que vale 0. " : " preguntas sin responder, que valen 0. ") : "Respondiste todas. ") +
                 "Una vez que entregás ya no se puede cambiar nada.",
          botones: [
            { texto: "Seguir contestando" },
            { texto: "Enviar todo y terminar", clase: "ev-btn-primario", accion: function () { terminar("completa"); } }
          ]
        });
      }

      /* ---------- cada pregunta ---------- */

      var zona = h("div", { class: "cu-lista" });
      cont.appendChild(zona);

      function cambio(r, valor) {
        r.respuesta = valor;
        guardar();
        pintarBarra();
        var est = zona.querySelector('[data-preg="' + r.id + '"] .cu-info-estado');
        if (est) { est.textContent = respondida(r) ? "Respondida" : "Sin responder aún"; }
      }

      function opciones(p, r) {
        var multiple = p.formato === "multiple";
        var nombre = "cu-" + r.id;
        var caja = h("div", { class: "cu-opciones", role: multiple ? "group" : "radiogroup" });
        ordenDe(r, p).forEach(function (orig, k) {
          var input = h("input", { type: multiple ? "checkbox" : "radio", name: nombre, value: String(orig) });
          input.checked = multiple ? (r.respuesta || []).indexOf(orig) !== -1 : r.respuesta === orig;
          input.addEventListener("change", function () {
            if (!multiple) { cambio(r, orig); return; }
            var marcadas = Array.prototype.filter.call(caja.querySelectorAll("input"), function (i) { return i.checked; })
              .map(function (i) { return parseInt(i.value, 10); });
            cambio(r, marcadas.length ? marcadas : null);
          });
          caja.appendChild(h("label", { class: "cu-op" }, [
            input,
            h("span", { class: "cu-letra" }, E.LETRAS[k].toLowerCase() + "."),
            h("span", { class: "ex-op-txt", html: p.opciones.textos[orig] })
          ]));
        });
        return caja;
      }

      function completar(p, r) {
        var valores = (r.respuesta || []).slice();
        function guardarHuecos() {
          var alguno = valores.some(function (v) { return v !== undefined && v !== null && String(v).trim() !== ""; });
          cambio(r, alguno ? valores.slice() : null);
        }
        return enunciadoConHuecos(p, function (i, hueco) {
          if (hueco.tipo === "lista") {
            var sel = h("select", { class: "cu-hueco cu-hueco-lista", "aria-label": "Hueco " + (i + 1) },
              [h("option", { value: "" }, "Elegir…")].concat(hueco.opciones.map(function (t, k) {
                return h("option", { value: String(k) }, t);
              })));
            sel.value = valores[i] !== undefined && valores[i] !== null ? String(valores[i]) : "";
            sel.addEventListener("change", function () { valores[i] = sel.value; guardarHuecos(); });
            return sel;
          }
          var entrada = h("input", { class: "cu-hueco cu-hueco-num", type: "text", inputmode: "decimal",
            autocomplete: "off", "aria-label": "Hueco " + (i + 1), size: "7" });
          entrada.value = valores[i] || "";
          entrada.addEventListener("input", function () { valores[i] = entrada.value; guardarHuecos(); });
          return entrada;
        });
      }

      it.preguntas.forEach(function (r, i) {
        var p = B.obtener(materia, r.id);
        casillas.appendChild(h("button", { class: "cu-casilla", type: "button", title: "Ir a la pregunta " + (i + 1),
          onclick: function () {
            var destino = zona.querySelector('[data-preg="' + r.id + '"]');
            if (destino) { window.scrollTo(0, destino.getBoundingClientRect().top + window.pageYOffset - 230); }
          } }, String(i + 1)));

        var tarjeta = h("section", { class: "cu-preg", "data-preg": r.id });
        tarjeta.appendChild(info(i + 1, respondida(r) ? "Respondida" : "Sin responder aún", "Puntúa como " + puntos));
        var cuerpo = h("div", { class: "cu-cuerpo" });
        tarjeta.appendChild(cuerpo);
        zona.appendChild(tarjeta);

        if (!p) {
          cuerpo.appendChild(h("p", {}, "Esta pregunta ya no está en el banco: se la cuenta como sin responder."));
          return;
        }
        cuerpo.appendChild(etiquetas(materia, p));
        if (p.formato === "completar") {
          cuerpo.appendChild(completar(p, r));
        } else {
          cuerpo.appendChild(h("div", { class: "ex-enunciado", html: p.enunciado }));
          cuerpo.appendChild(h("p", { class: "cu-consigna" }, CONSIGNA[p.formato] || CONSIGNA.opcion));
          cuerpo.appendChild(opciones(p, r));
        }
      });

      zona.appendChild(h("div", { class: "ex-acciones cu-entregar" }, [
        h("p", { class: "ae-ayuda" }, "Podés ir y volver entre preguntas. Nada se corrige hasta que entregás."),
        h("button", { class: "ev-btn ev-btn-primario", type: "button", onclick: entregar }, "Terminar intento…")
      ]));

      pintarBarra();
      E.pantallaNueva(cont);
      if (it.limite) { tic(); reloj = window.setInterval(tic, 500); }
    },

    /* ---------- revision final ----------
       acciones: { volver(aviso), lanzar(ae, reiniciar), eliminar(ae) } */
    informe: function (cont, materia, ae, acciones, aviso) {
      var h = E.h, B = E.banco;
      var it = ae.intento;
      var p = E.puntaje(it);
      var nota = p.nota || 0;
      var puntos = puntosDe(it);
      var condicion = E.condicionPrimeraEtapa(nota);

      E.vaciar(cont);
      cont.appendChild(h("button", { class: "ev-volver", type: "button", onclick: function () { acciones.volver(); } }, "← Evaluación"));
      cont.appendChild(h("p", { class: "kicker ev-kicker" }, "Revisión del cuestionario"));
      cont.appendChild(h("h1", { class: "ev-h1" }, ae.nombre));
      if (aviso) { cont.appendChild(h("div", { class: "ae-aviso ae-aviso-alerta" }, aviso)); }

      var detalle = "Correctas: " + p.correctas + " · Parcialmente correctas: " + p.parciales +
        " · Incorrectas: " + p.incorrectas + (p.sinResponder ? " · Sin responder: " + p.sinResponder : "");

      cont.appendChild(h("div", { class: "inf-resultado" }, [
        h("div", { class: "inf-nota cu-nota", "data-condicion": condicion.clave }, [
          h("span", { class: "inf-nota-num" }, E.nota(nota)),
          h("span", { class: "inf-nota-pct" }, "sobre 100")
        ]),
        h("div", { class: "inf-datos" }, [
          h("span", { class: "ev-chip", "data-estado": "terminada" }, "Terminada · " + (E.MOTIVOS[it.motivo] || "")),
          h("p", { class: "cu-condicion", "data-condicion": condicion.clave }, condicion.texto),
          h("p", {}, E.resumenConfig(materia, it.config).join(" · ")),
          h("p", {}, detalle),
          h("p", {}, "Duración: " + E.duracion(it.fin - it.inicio) + " · " + E.fecha(it.fin))
        ]),
        h("div", { class: "inf-botones" }, [
          h("button", { class: "ev-btn ev-btn-primario", type: "button", onclick: function () { acciones.lanzar(ae, true); } }, "↻ Rehacer"),
          h("button", { class: "ev-btn ev-btn-peligro", type: "button", onclick: function () { acciones.eliminar(ae); } }, "Eliminar")
        ])
      ]));

      if ((ae.historial || []).length > 1) {
        cont.appendChild(h("div", { class: "tabla-wrap" }, h("table", { class: "t full inf-historial" }, [
          h("tr", {}, [h("th", {}, "Intento"), h("th", {}, "Fecha"), h("th", {}, "Nota"), h("th", {}, "Duración"), h("th", {}, "Cómo terminó")])
        ].concat(ae.historial.map(function (x, i) {
          return h("tr", {}, [
            h("td", {}, String(ae.historial.length - i)),
            h("td", {}, E.fecha(x.fecha)),
            h("td", {}, typeof x.nota === "number" ? E.nota(x.nota) + " / 100" : x.correctas + " / " + x.total),
            h("td", {}, E.duracion(x.duracion)),
            h("td", {}, E.MOTIVOS[x.motivo] || "")
          ]);
        })))));
      }

      cont.appendChild(h("h2", { class: "inf-titulo" }, "Revisión de las preguntas"));

      it.preguntas.forEach(function (r, i) {
        var preg = B.obtener(materia, r.id);
        var fr = r.fraccion || 0;
        var estado = !r.hecho ? "Sin responder" : fr >= 1 ? "Correcta" : fr > 0 ? "Parcialmente correcta" : "Incorrecta";
        var clase = !r.hecho ? "sin-responder" : fr >= 1 ? "bien" : fr > 0 ? "parcial" : "mal";

        var tarjeta = h("section", { class: "cu-preg cu-revision inf-" + clase });
        tarjeta.appendChild(info(i + 1, estado, "Se puntúa " + E.nota(fr * puntos) + " sobre " + E.nota(puntos)));
        var cuerpo = h("div", { class: "cu-cuerpo" });
        tarjeta.appendChild(cuerpo);
        cont.appendChild(tarjeta);

        if (!preg) { cuerpo.appendChild(h("p", {}, "Esta pregunta ya no está en el banco.")); return; }
        cuerpo.appendChild(etiquetas(materia, preg));

        if (preg.formato === "completar") {
          var revision = B.corregirCuestionario(preg, r.respuesta);
          cuerpo.appendChild(enunciadoConHuecos(preg, function (k, hueco) {
            var dado = (r.respuesta || [])[k];
            var vacio = dado === undefined || dado === null || String(dado).trim() === "";
            var mostrado = vacio ? "—" : hueco.tipo === "lista" ? hueco.opciones[parseInt(dado, 10)] : dado;
            var bien = revision.huecos[k].ok;
            var correcta = hueco.tipo === "lista" ? hueco.opciones[hueco.correcta] : hueco.respuesta;
            return h("span", { class: "cu-hueco-rev " + (bien ? "es-correcta" : "es-incorrecta") }, [
              h("span", { class: "cu-hueco-dado" }, mostrado),
              h("span", { class: "cu-marca" }, bien ? " ✓" : " ✗"),
              bien ? null : h("small", { class: "cu-hueco-correcta" },
                revision.huecos[k].motivo === "formato"
                  ? " el valor está bien, pero va con coma y " + hueco.decimales + " decimales: " + correcta
                  : " correcta: " + correcta)
            ]);
          }));
        } else {
          cuerpo.appendChild(h("div", { class: "ex-enunciado", html: preg.enunciado }));
          var marcadas = preg.formato === "multiple" ? (r.respuesta || []) : (r.hecho ? [r.respuesta] : []);
          var orden = r.orden || preg.opciones.textos.map(function (_, k) { return k; });
          cuerpo.appendChild(h("div", { class: "inf-opciones" }, orden.map(function (orig, k) {
            var esCorrecta = preg.opciones.correctas.indexOf(orig) !== -1;
            var laMarcaste = marcadas.indexOf(orig) !== -1;
            return h("div", { class: "inf-op" + (esCorrecta ? " es-correcta" : "") + (laMarcaste && !esCorrecta ? " es-incorrecta" : "") }, [
              h("span", { class: "cu-letra" }, E.LETRAS[k].toLowerCase() + "."),
              h("span", { class: "ex-op-txt", html: preg.opciones.textos[orig] }),
              esCorrecta ? h("small", {}, "Correcta") : null,
              laMarcaste ? h("small", {}, esCorrecta ? "✓ La marcaste" : "✗ La marcaste") : null
            ]);
          })));
          if (preg.formato === "multiple") {
            cuerpo.appendChild(h("p", { class: "inf-meta" },
              "Varias correctas: cada correcta marcada suma 1/" + preg.opciones.correctas.length +
              " del puntaje y cada incorrecta marcada resta lo mismo."));
          }
        }

        if (preg.explicacion) {
          cuerpo.appendChild(h("div", { class: "caja caja-formula" }, [
            h("span", { class: "caja-tit" }, "Explicación"),
            h("div", { html: preg.explicacion })
          ]));
        }
      });

      E.pantallaNueva(cont);
    }
  };
})(window.NC.eval);
