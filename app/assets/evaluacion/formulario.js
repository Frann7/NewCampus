/* ============================================================
   NEWCAMPUS - Evaluacion: formulario de una autoevaluacion
   Crea una autoevaluacion nueva. Una vez guardada no se edita: se juega,
   se rehace o se borra desde su tarjeta. Las opciones se habilitan en cadena:
   unidades -> tipo de enunciado -> cantidad -> orden.
   ============================================================ */

(function (E) {
  "use strict";

  var POR_DEFECTO = {
    modo: "normal", nivel: "medio", fallos: 3, verRespuesta: true,
    unidades: [], teoria: false, practica: false,
    reparto: "separado", cantTeoria: 5, cantPractica: 3, cantMezcla: 8,
    orden: "aleatorio", conTiempo: false, minutos: 30
  };

  var AYUDA_NIVEL = {
    principiante: "Divide cada ejercicio en muchos pasos chicos, cuenta por cuenta.",
    medio: "Divide cada ejercicio en los pasos intermedios importantes.",
    avanzado: "Solo pide las partes principales del ejercicio."
  };

  var PLANTILLA =
    '<fieldset class="ae-paso">' +
    '  <legend><span class="ae-num">1</span>Nombre</legend>' +
    '  <input class="ae-input" name="nombre" maxlength="60" autocomplete="off" placeholder="Ej: Repaso de la Unidad 5 antes del parcial">' +
    '  <p class="ae-ayuda">Obligatorio. Con este nombre la vas a encontrar guardada.</p>' +
    '</fieldset>' +

    '<fieldset class="ae-paso">' +
    '  <legend><span class="ae-num">2</span>Modo</legend>' +
    '  <div class="ae-modos">' +
    '    <label class="ae-modo"><input type="radio" name="modo" value="normal">' +
    '      <span class="ae-modo-tit">Normal</span>' +
    '      <span class="ae-modo-desc">Enunciado completo y opciones, como en un examen.</span></label>' +
    '    <label class="ae-modo"><input type="radio" name="modo" value="interactivo">' +
    '      <span class="ae-modo-tit">Interactivo</span>' +
    '      <span class="ae-modo-desc">Te guía por partes: pistas, cuentas paso a paso y reintentos.</span></label>' +
    '  </div>' +
    '  <div class="ae-sub" data-solo-interactivo hidden>' +
    '    <div class="ae-campo">' +
    '      <span class="ae-etq">Nivel</span>' +
    '      <div class="ae-segmentos">' +
    '        <label><input type="radio" name="nivel" value="principiante"><span>Principiante</span></label>' +
    '        <label><input type="radio" name="nivel" value="medio"><span>Medio</span></label>' +
    '        <label><input type="radio" name="nivel" value="avanzado"><span>Avanzado</span></label>' +
    '      </div>' +
    '      <p class="ae-ayuda" data-ayuda-nivel></p>' +
    '    </div>' +
    '    <div class="ae-campo">' +
    '      <label class="ae-etq">Vidas (fallos permitidos)</label>' +
    '      <div class="ae-linea"><input class="ae-input ae-corto" type="number" name="fallos" min="1" max="200"> <span>para toda la autoevaluación (de 1 a 200)</span></div>' +
    '      <p class="ae-ayuda">Cada respuesta equivocada te quita una vida y podés volver a intentar. Si te quedás sin vidas, la autoevaluación termina.</p>' +
    '    </div>' +
    '  </div>' +
    '</fieldset>' +

    '<fieldset class="ae-paso">' +
    '  <legend><span class="ae-num">3</span>Contenido</legend>' +
    '  <div class="ae-campo">' +
    '    <span class="ae-etq">Unidades</span>' +
    '    <div class="ae-caja-unidades" data-unidades></div>' +
    '  </div>' +
    '  <fieldset class="ae-campo" data-bloque="tipos">' +
    '    <span class="ae-etq">Tipo de enunciado</span>' +
    '    <div class="ae-tipos">' +
    '      <label class="ae-chip"><input type="checkbox" name="teoria"><span><b>Teoría</b><small data-disp="teoria"></small></span></label>' +
    '      <label class="ae-chip"><input type="checkbox" name="practica"><span><b>Práctica</b><small data-disp="practica"></small></span></label>' +
    '    </div>' +
    '    <p class="ae-motivo">Elegí al menos una unidad para habilitar esto.</p>' +
    '  </fieldset>' +
    '</fieldset>' +

    '<fieldset class="ae-paso">' +
    '  <legend><span class="ae-num">4</span>Cantidad y orden</legend>' +
    '  <fieldset class="ae-campo" data-bloque="cantidad">' +
    '    <span class="ae-etq">Cantidad de preguntas</span>' +
    '    <label class="ae-opcion"><input type="radio" name="reparto" value="separado"><span>Por separado</span></label>' +
    '    <div class="ae-cantidades">' +
    '      <label class="ae-cant">Teoría <input class="ae-input ae-corto" type="number" name="cantTeoria" min="1"> <small data-de="teoria"></small></label>' +
    '      <label class="ae-cant">Práctica <input class="ae-input ae-corto" type="number" name="cantPractica" min="1"> <small data-de="practica"></small></label>' +
    '    </div>' +
    '    <label class="ae-opcion" data-opcion-mezcla><input type="radio" name="reparto" value="mezcla"><span>Mezcla de ambas</span></label>' +
    '    <div class="ae-cantidades">' +
    '      <label class="ae-cant">Total <input class="ae-input ae-corto" type="number" name="cantMezcla" min="1"> <small data-de="mezcla"></small></label>' +
    '    </div>' +
    '    <p class="ae-motivo">Marcá Teoría, Práctica o ambas para elegir la cantidad.</p>' +
    '    <p class="ae-ayuda" data-ayuda-mezcla hidden>La mezcla necesita Teoría y Práctica marcadas.</p>' +
    '  </fieldset>' +
    '  <fieldset class="ae-campo" data-bloque="orden">' +
    '    <label class="ae-etq">Orden de las preguntas</label>' +
    '    <select class="ae-input ae-select" name="orden">' +
    '      <option value="aleatorio">Aleatorio</option>' +
    '      <option value="teoria">Primero teoría</option>' +
    '      <option value="practica">Primero práctica</option>' +
    '    </select>' +
    '    <p class="ae-motivo">El orden solo tiene sentido con Teoría y Práctica marcadas.</p>' +
    '  </fieldset>' +
    '</fieldset>' +

    '<fieldset class="ae-paso">' +
    '  <legend><span class="ae-num">5</span>Corrección y tiempo</legend>' +
    '  <fieldset class="ae-campo" data-bloque="correccion">' +
    '    <label class="ae-check"><input type="checkbox" name="verRespuesta"><span>Mostrar la respuesta correcta después de cada pregunta</span></label>' +
    '    <p class="ae-ayuda">Desactivado: respondés de corrido y en el informe final ves cuáles hiciste bien y qué elegiste.</p>' +
    '    <p class="ae-motivo">En modo interactivo la corrección siempre es inmediata.</p>' +
    '  </fieldset>' +
    '  <div class="ae-campo">' +
    '    <span class="ae-etq">Tiempo</span>' +
    '    <label class="ae-opcion"><input type="radio" name="tiempo" value="libre"><span>Sin límite</span></label>' +
    '    <label class="ae-opcion"><input type="radio" name="tiempo" value="contador"><span>Con contador de</span>' +
    '      <input class="ae-input ae-corto" type="number" name="minutos" min="1" max="240"><span>minutos (máximo 240 = 4 horas)</span></label>' +
    '    <p class="ae-ayuda">Al llegar a cero se termina. Si querés salir antes, te pregunta si terminarla o dejar el contador corriendo.</p>' +
    '  </div>' +
    '</fieldset>' +

    '<div class="ae-resumen" data-resumen></div>' +
    '<div class="ae-errores" data-errores hidden></div>' +
    '<div class="ae-pie">' +
    '  <p class="ae-ayuda ae-pie-nota">Una vez guardada, la configuración ya no se puede cambiar.</p>' +
    '  <span class="ae-pie-espacio"></span>' +
    '  <button type="button" class="ev-btn" data-accion="guardar">Guardar</button>' +
    '  <button type="submit" class="ev-btn ev-btn-primario" data-accion="lanzar">Guardar y empezar</button>' +
    '</div>';

  var MAX_MINUTOS = 240;   // 4 horas

  function entero(v) { var n = parseInt(v, 10); return isNaN(n) ? 0 : n; }

  E.formulario = {
    /* acciones: { volver(aviso), lanzar(ae, reiniciar) } */
    mostrar: function (cont, materia, acciones) {
      var h = E.h;
      var c = Object.assign({}, POR_DEFECTO);

      E.vaciar(cont);
      cont.appendChild(h("button", { class: "ev-volver", type: "button", onclick: function () { acciones.volver(); } }, "← Evaluación"));
      cont.appendChild(h("p", { class: "kicker ev-kicker" }, "Autoevaluación"));
      cont.appendChild(h("h1", { class: "ev-h1" }, "Nueva autoevaluación"));

      var form = h("form", { class: "ae-form", novalidate: true, html: PLANTILLA });
      cont.appendChild(form);

      function campo(nombre) { return form.elements[nombre]; }
      function bloque(nombre) { return form.querySelector('[data-bloque="' + nombre + '"]'); }

      // Unidades de la materia
      var cajaUnidades = form.querySelector("[data-unidades]");
      E.unidades(materia).forEach(function (u) {
        cajaUnidades.appendChild(h("label", { class: "ae-chip" }, [
          h("input", { type: "checkbox", name: "unidad", value: u.id }),
          h("span", {}, [h("b", {}, u.num), h("small", {}, u.nombre)])
        ]));
      });

      // Cargar valores
      campo("nombre").value = "";
      form.querySelector('[name="modo"][value="' + c.modo + '"]').checked = true;
      form.querySelector('[name="nivel"][value="' + c.nivel + '"]').checked = true;
      campo("fallos").value = c.fallos;
      form.querySelectorAll('[name="unidad"]').forEach(function (i) { i.checked = c.unidades.indexOf(i.value) !== -1; });
      campo("teoria").checked = c.teoria;
      campo("practica").checked = c.practica;
      form.querySelector('[name="reparto"][value="' + c.reparto + '"]').checked = true;
      campo("cantTeoria").value = c.cantTeoria;
      campo("cantPractica").value = c.cantPractica;
      campo("cantMezcla").value = c.cantMezcla;
      campo("orden").value = c.orden;
      campo("verRespuesta").checked = c.verRespuesta;
      form.querySelector('[name="tiempo"][value="' + (c.conTiempo ? "contador" : "libre") + '"]').checked = true;
      campo("minutos").value = c.minutos;

      function leer() {
        var marcado = function (sel) { var el = form.querySelector(sel + ":checked"); return el ? el.value : null; };
        return {
          modo: marcado('[name="modo"]'),
          nivel: marcado('[name="nivel"]'),
          fallos: entero(campo("fallos").value),
          verRespuesta: campo("verRespuesta").checked,
          unidades: Array.prototype.filter.call(form.querySelectorAll('[name="unidad"]'), function (i) { return i.checked; })
            .map(function (i) { return i.value; }),
          teoria: campo("teoria").checked,
          practica: campo("practica").checked,
          reparto: marcado('[name="reparto"]'),
          cantTeoria: entero(campo("cantTeoria").value),
          cantPractica: entero(campo("cantPractica").value),
          cantMezcla: entero(campo("cantMezcla").value),
          orden: campo("orden").value,
          conTiempo: marcado('[name="tiempo"]') === "contador",
          minutos: entero(campo("minutos").value)
        };
      }

      function sincronizar() {
        var v = leer();
        var interactivo = v.modo === "interactivo";
        var disp = E.banco.disponibles(materia, v.unidades);

        form.querySelector("[data-solo-interactivo]").hidden = !interactivo;
        form.querySelector("[data-ayuda-nivel]").textContent = AYUDA_NIVEL[v.nivel];

        // unidades -> tipos
        var hayUnidad = v.unidades.length > 0;
        bloque("tipos").disabled = !hayUnidad;
        ["teoria", "practica"].forEach(function (t) {
          form.querySelector('[data-disp="' + t + '"]').textContent =
            hayUnidad ? disp[t] + (disp[t] === 1 ? " disponible" : " disponibles") : "";
        });

        // tipos -> cantidad
        var hayTipo = hayUnidad && (v.teoria || v.practica);
        var ambos = hayUnidad && v.teoria && v.practica;
        bloque("cantidad").disabled = !hayTipo;

        var radioMezcla = form.querySelector('[name="reparto"][value="mezcla"]');
        radioMezcla.disabled = !ambos;
        form.querySelector("[data-opcion-mezcla]").classList.toggle("ae-apagado", hayTipo && !ambos);
        form.querySelector("[data-ayuda-mezcla]").hidden = !(hayTipo && !ambos);
        if (!ambos && v.reparto === "mezcla") {
          form.querySelector('[name="reparto"][value="separado"]').checked = true;
          v.reparto = "separado";
        }
        var mezcla = v.reparto === "mezcla";
        campo("cantTeoria").disabled = mezcla || !v.teoria;
        campo("cantPractica").disabled = mezcla || !v.practica;
        campo("cantMezcla").disabled = !mezcla;
        [["cantTeoria", disp.teoria, "teoria"], ["cantPractica", disp.practica, "practica"],
         ["cantMezcla", disp.teoria + disp.practica, "mezcla"]].forEach(function (x) {
          campo(x[0]).max = x[1];
          if (x[1] > 0 && entero(campo(x[0]).value) > x[1]) { campo(x[0]).value = x[1]; }   // no pedir mas de las que hay
          campo(x[0]).closest(".ae-cant").classList.toggle("ae-apagado", campo(x[0]).disabled);
          form.querySelector('[data-de="' + x[2] + '"]').textContent = "de " + x[1];
        });

        // tipos -> orden
        bloque("orden").disabled = !ambos;

        // modo -> correccion
        bloque("correccion").disabled = interactivo;

        campo("minutos").disabled = !v.conTiempo;

        form.querySelector("[data-resumen]").textContent = hayTipo
          ? "Resumen: " + E.resumenConfig(materia, v).join(" · ")
          : "Completá los pasos para ver el resumen.";
      }

      function validar(v, nombre) {
        var errores = [];
        var disp = E.banco.disponibles(materia, v.unidades);
        if (!nombre) { errores.push("Poné un nombre: es obligatorio."); }
        if (v.modo === "interactivo" && (v.fallos < 1 || v.fallos > 200)) {
          errores.push("Las vidas van de 1 a 200.");
        }
        if (!v.unidades.length) { errores.push("Elegí al menos una unidad."); }
        else if (!v.teoria && !v.practica) { errores.push("Marcá Teoría, Práctica o ambas."); }
        else {
          var revisar = function (cant, max, que) {
            if (max === 0) { errores.push("No hay preguntas de " + que + " en las unidades elegidas."); }
            else if (cant < 1 || cant > max) { errores.push("La cantidad de " + que + " tiene que ir de 1 a " + max + "."); }
          };
          if (v.teoria && v.practica && v.reparto === "mezcla") { revisar(v.cantMezcla, disp.teoria + disp.practica, "la mezcla"); }
          else {
            if (v.teoria) { revisar(v.cantTeoria, disp.teoria, "teoría"); }
            if (v.practica) { revisar(v.cantPractica, disp.practica, "práctica"); }
          }
        }
        if (v.conTiempo && (v.minutos < 1 || v.minutos > MAX_MINUTOS)) { errores.push("El contador va de 1 a 240 minutos (4 horas)."); }
        return errores;
      }

      function guardar(lanzar) {
        var v = leer();
        var nombre = campo("nombre").value.trim();
        var errores = validar(v, nombre);
        var caja = form.querySelector("[data-errores]");
        campo("nombre").classList.toggle("ae-invalido", !nombre);

        if (errores.length) {
          E.vaciar(caja);
          caja.appendChild(h("b", {}, "Falta completar:"));
          caja.appendChild(h("ul", {}, errores.map(function (e) { return h("li", {}, e); })));
          caja.hidden = false;
          if (!nombre) { campo("nombre").focus(); }
          return;
        }

        var nueva = { id: "ae-" + Date.now().toString(36), materia: materia, creada: Date.now(),
                      nombre: nombre, config: v, historial: [], intento: null };
        if (!E.almacen.guardar(nueva)) {
          window.alert("No se pudo guardar: el navegador no deja usar su almacenamiento en esta página.");
          return;
        }
        if (lanzar) { acciones.lanzar(nueva, false); }
        else { acciones.volver("Se guardó “" + nombre + "”. Tocá su tarjeta cuando quieras empezar."); }
      }

      form.addEventListener("change", sincronizar);
      form.addEventListener("input", sincronizar);
      form.addEventListener("submit", function (ev) { ev.preventDefault(); guardar(true); });
      form.querySelector('[data-accion="guardar"]').addEventListener("click", function () { guardar(false); });

      sincronizar();
      E.pantallaNueva(cont);
      campo("nombre").focus();
    }
  };
})(window.NC.eval);
