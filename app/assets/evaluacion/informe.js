/* ============================================================
   NEWCAMPUS - Evaluacion: informe final
   Resultado, por que termino, historial de intentos y el repaso de cada
   pregunta: cual era la correcta, que elegiste y la explicacion.
   ============================================================ */

(function (E) {
  "use strict";

  function plural(n, uno, varios) { return n + " " + (n === 1 ? uno : varios); }

  E.informe = {
    /* acciones: { volver(aviso), lanzar(ae, reiniciar), eliminar(ae) } */
    mostrar: function (cont, materia, ae, acciones, aviso) {
      var h = E.h, B = E.banco;
      var it = ae.intento, c = it.config;
      var interactivo = E.guiado(c);   // pistas, vidas y pasos: estilo guiado o interactivo
      var p = E.puntaje(it);
      var porcentaje = p.total ? Math.round(100 * p.correctas / p.total) : 0;

      E.vaciar(cont);
      cont.appendChild(h("button", { class: "ev-volver", type: "button", onclick: function () { acciones.volver(); } }, "← Evaluación"));
      cont.appendChild(h("p", { class: "kicker ev-kicker" }, "Informe final"));
      cont.appendChild(h("h1", { class: "ev-h1" }, ae.nombre));
      if (aviso) { cont.appendChild(h("div", { class: "ae-aviso ae-aviso-alerta" }, aviso)); }

      /* ---------- resultado ---------- */

      var detalle = interactivo
        ? "Al primer intento: " + p.correctas + " · Con errores: " + p.incorrectas
        : "Correctas: " + p.correctas + " · Incorrectas: " + p.incorrectas;
      if (p.sinResponder) { detalle += " · Sin responder: " + p.sinResponder; }
      if (p.salteadas) { detalle += " · Salteados: " + p.salteadas; }

      cont.appendChild(h("div", { class: "inf-resultado" }, [
        h("div", { class: "inf-nota" }, [
          h("span", { class: "inf-nota-num" }, p.correctas + " / " + p.total),
          h("span", { class: "inf-nota-pct" }, porcentaje + " %")
        ]),
        h("div", { class: "inf-datos" }, [
          h("span", { class: "ev-chip", "data-estado": "terminada" }, "Terminada · " + (E.MOTIVOS[it.motivo] || "")),
          h("p", {}, E.resumenConfig(materia, c).join(" · ")),
          h("p", {}, detalle + (interactivo ? " · Vidas restantes: " + it.vidas : "")),
          h("p", {}, "Duración: " + E.duracion(it.fin - it.inicio) + " · " + E.fecha(it.fin))
        ]),
        h("div", { class: "inf-botones" }, [
          h("button", { class: "ev-btn ev-btn-primario", type: "button", onclick: function () { acciones.lanzar(ae, true); } }, "↻ Rehacer"),
          h("button", { class: "ev-btn ev-btn-peligro", type: "button", onclick: function () { acciones.eliminar(ae); } }, "Eliminar")
        ])
      ]));

      /* ---------- historial ---------- */

      if ((ae.historial || []).length > 1) {
        cont.appendChild(h("div", { class: "tabla-wrap" }, h("table", { class: "t full inf-historial" }, [
          h("tr", {}, [h("th", {}, "Intento"), h("th", {}, "Fecha"), h("th", {}, "Resultado"), h("th", {}, "Duración"), h("th", {}, "Cómo terminó")])
        ].concat(ae.historial.map(function (x, i) {
          return h("tr", {}, [
            h("td", {}, String(ae.historial.length - i)),
            h("td", {}, E.fecha(x.fecha)),
            h("td", {}, x.correctas + " / " + x.total),
            h("td", {}, E.duracion(x.duracion)),
            h("td", {}, E.MOTIVOS[x.motivo] || "")
          ]);
        })))));
      }

      /* ---------- repaso pregunta por pregunta ---------- */

      cont.appendChild(h("h2", { class: "inf-titulo" }, "Repaso de las preguntas"));

      it.preguntas.forEach(function (r, i) {
        var preg = B.obtener(materia, r.id);
        var clase = r.salteado || !r.hecho ? "sin-responder" : (r.ok ? "bien" : "mal");
        var veredicto = r.salteado ? "Salteado" : !r.hecho ? "Sin responder"
          : r.ok ? (interactivo ? "✓ Al primer intento" : "✓ Correcta")
          : (interactivo ? "Resuelta con " + plural(r.fallos, "fallo", "fallos") : "✗ Incorrecta");

        var item = h("div", { class: "inf-item inf-" + clase });
        cont.appendChild(item);
        item.appendChild(h("div", { class: "inf-item-cab" }, [
          h("span", { class: "inf-item-num" }, String(i + 1)),
          preg ? h("span", { class: "ev-chip ev-chip-" + preg.tipo }, E.TIPOS[preg.tipo]) : null,
          preg ? h("span", { class: "ev-chip" }, E.numeroDeUnidad(materia, preg.unidad)) : null,
          preg ? E.chipOrigen(preg) : null,
          h("span", { class: "inf-veredicto" }, veredicto)
        ]));

        if (!preg) {
          item.appendChild(h("p", {}, "Esta pregunta ya no está en el banco."));
          return;
        }

        item.appendChild(h("div", { class: "ex-enunciado", html: preg.enunciado }));
        var pasos = interactivo && (preg.tipo === "practica" || preg.tipo === "ejercicio")
          ? B.pasosDelNivel(preg, c.nivel) : [];

        if (pasos.length) {
          // Ejercicio interactivo: como te fue en cada paso
          item.appendChild(h("ol", { class: "inf-pasos" }, pasos.map(function (paso, k) {
            var ep = r.pasos[k];
            var respuesta = paso.opciones
              ? h("span", { html: paso.opciones.textos[paso.opciones.correcta] })
              : h("b", {}, paso.respuesta);
            var como = !ep || !ep.ok
              ? (ep && ep.fallos ? "No lo resolviste (" + plural(ep.fallos, "fallo", "fallos") + ")" : "No llegaste a este paso")
              : (ep.fallos ? "Bien con " + plural(ep.fallos, "fallo", "fallos") : "Bien al primer intento");
            if (ep && ep.pistas) { como += " · usaste la pista"; }
            return h("li", { class: ep && ep.ok && !ep.fallos ? "bien" : "mal" }, [
              paso.inciso ? h("span", { class: "ex-paso-cab" }, "Inciso " + paso.inciso + ")") : null,
              h("div", { html: paso.consigna }),
              h("div", { class: "inf-paso-dato" }, ["Respuesta: ", respuesta, h("small", {}, " — " + como)])
            ]);
          })));
        } else {
          // Opciones: marca la correcta y las que elegiste
          if (preg.pregunta) { item.appendChild(h("div", { class: "ex-pregunta", html: preg.pregunta })); }
          var orden = r.orden || preg.opciones.textos.map(function (_, k) { return k; });
          item.appendChild(h("div", { class: "inf-opciones" }, orden.map(function (orig, k) {
            var esCorrecta = orig === preg.opciones.correcta;
            var laElegiste = orig === r.elegida || (r.descartadas || []).indexOf(orig) !== -1;
            return h("div", { class: "inf-op" + (esCorrecta ? " es-correcta" : "") + (laElegiste && !esCorrecta ? " es-incorrecta" : "") }, [
              h("span", { class: "ex-letra" }, E.LETRAS[k]),
              h("span", { class: "ex-op-txt", html: preg.opciones.textos[orig] }),
              esCorrecta ? h("small", {}, "Correcta") : null,
              laElegiste ? h("small", {}, esCorrecta ? "Tu respuesta" : "Elegiste esta") : null
            ]);
          })));
          if (interactivo && r.pistas) { item.appendChild(h("p", { class: "inf-meta" }, "Usaste la pista")); }
        }

        if (preg.explicacion) {
          item.appendChild(h("div", { class: "caja caja-formula" }, [
            h("span", { class: "caja-tit" }, "Explicación"),
            h("div", { html: preg.explicacion })
          ]));
        }
      });

      E.pantallaNueva(cont);
    }
  };
})(window.NC.eval);
