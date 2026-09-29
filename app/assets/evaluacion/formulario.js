/* ============================================================
   NEWCAMPUS - Evaluacion: formulario de una autoevaluacion
   Crea una autoevaluacion nueva. Una vez guardada no se edita: se juega,
   se rehace o se borra desde su tarjeta. Las opciones se habilitan en cadena:
   etapa -> (todo lo demas) ; unidades -> tipo de enunciado -> cantidad -> orden.

   Lo primero es la ETAPA del parcial que se simula, y hasta elegirla todo lo
   demas queda bloqueado: las dos etapas no se parecen en nada.
     1ra  cuestionario del Aula Virtual: sin modo interactivo, sin tipos,
          se corrige al entregar sobre 100 puntos
     2da  escrito, en tres maneras:
            normal, estilo "parcial"   enunciado y opciones
            normal, estilo "guiado"    faciles: con pistas y todos los pasos, sin vidas
            interactivo                un ejercicio de parcial completo, por partes,
                                       con nivel y vidas
          En normal se puede sumar la navegacion libre (saltear y volver).
   Los pasos que no corresponden a la etapa elegida se esconden (data-etapa)
   y los numeros de los pasos se recalculan.
   ============================================================ */

(function (E) {
  "use strict";

  var POR_DEFECTO = {
    etapa: null, cantCuestionario: 10, formato1: "hoja", urgente1: false, corregirYa: false,
    modo: "normal", estilo: "parcial", navLibre: false, cantEjercicios: 2,
    nivel: "medio", fallos: 3, verRespuesta: true,
    unidades: [], teoria: false, practica: false,
    reparto: "separado", cantTeoria: 5, cantPractica: 3, cantMezcla: 8,
    orden: "aleatorio", conTiempo: false, minutos: 30, soloParcial: false, parcial: "",
    fundamentales: false
  };

  var AYUDA_NIVEL = {
    principiante: "Muchos pasos chicos: cada suma, cada resta, cada valor de tabla.",
    medio: "Cada inciso en sus resultados intermedios importantes.",
    avanzado: "Solo el resultado de cada inciso, como en el parcial."
  };

  var BLOQUEADO = '<p class="ae-motivo">Elegí primero la etapa del parcial.</p>';

  var PLANTILLA =
    '<fieldset class="ae-paso ae-paso-etapa">' +
    '  <legend><span class="ae-num"></span>Etapa del parcial</legend>' +
    '  <p class="ae-ayuda ae-ayuda-arriba">El parcial tiene dos instancias y se preparan distinto. Elegí cuál querés simular: el resto del formulario se acomoda a esa etapa.</p>' +
    '  <div class="ae-modos">' +
    '    <label class="ae-modo"><input type="radio" name="etapa" value="1">' +
    '      <span class="ae-modo-tit">Primera etapa · respuesta corta</span>' +
    '      <span class="ae-modo-desc">Ahora es en hoja: 10 preguntas de opción múltiple o verdadero o falso, más de teoría que de cuentas, y puede haber varias correctas. También está el formato del Aula Virtual. Se corrige al entregar, sobre 100 puntos.</span></label>' +
    '    <label class="ae-modo"><input type="radio" name="etapa" value="2">' +
    '      <span class="ae-modo-tit">Segunda etapa · escrito</span>' +
    '      <span class="ae-modo-desc">Problemas y teoría a desarrollar, como el escrito. Se puede hacer en modo normal o interactivo, paso a paso.</span></label>' +
    '  </div>' +
    '  <div class="ae-sub" data-etapa="1" hidden>' +
    '    <div class="ae-campo">' +
    '      <span class="ae-etq">Formato</span>' +
    '      <div class="ae-segmentos">' +
    '        <label><input type="radio" name="formato1" value="hoja"><span>En hoja</span></label>' +
    '        <label><input type="radio" name="formato1" value="virtual"><span>Virtual</span></label>' +
    '      </div>' +
    '      <p class="ae-ayuda" data-ayuda-formato1></p>' +
    '    </div>' +
    '    <p class="ae-ayuda ae-ayuda-arriba">Según el reglamento de la cátedra, la nota de esta instancia decide qué sigue: <b>de 30 a 59</b> seguís en condiciones de regularizar; <b>con 60 o más</b> pasás a la 2da instancia escrita. En la nota del parcial pesa un 40&nbsp;%.</p>' +
    '  </div>' +
    '</fieldset>' +

    '<fieldset class="ae-paso" data-tras-etapa>' +
    '  <legend><span class="ae-num"></span>Nombre</legend>' + BLOQUEADO +
    '  <input class="ae-input" name="nombre" maxlength="60" autocomplete="off" placeholder="Ej: Repaso de la Unidad 5 antes del parcial">' +
    '  <p class="ae-ayuda">Obligatorio. Con este nombre la vas a encontrar guardada.</p>' +
    '</fieldset>' +

    '<fieldset class="ae-paso" data-tras-etapa data-etapa="2">' +
    '  <legend><span class="ae-num"></span>Modo</legend>' +
    '  <div class="ae-modos">' +
    '    <label class="ae-modo"><input type="radio" name="modo" value="normal">' +
    '      <span class="ae-modo-tit">Normal</span>' +
    '      <span class="ae-modo-desc">Preguntas sueltas sacadas de los parciales: teoría y práctica, con opciones.</span></label>' +
    '    <label class="ae-modo"><input type="radio" name="modo" value="interactivo">' +
    '      <span class="ae-modo-tit">Interactivo</span>' +
    '      <span class="ae-modo-desc">Un ejercicio de parcial completo, con todos sus incisos, que se va desglosando en partes. Cuanto más fácil el nivel, más pasos.</span></label>' +
    '  </div>' +
    '  <div class="ae-sub" data-modo="normal">' +
    '    <div class="ae-campo">' +
    '      <span class="ae-etq">Estilo</span>' +
    '      <div class="ae-segmentos">' +
    '        <label><input type="radio" name="estilo" value="parcial"><span>Como en el parcial</span></label>' +
    '        <label><input type="radio" name="estilo" value="guiado"><span>Fáciles y guiadas</span></label>' +
    '      </div>' +
    '      <p class="ae-ayuda" data-ayuda-estilo></p>' +
    '    </div>' +
    '    <div class="ae-campo">' +
    '      <label class="ae-check"><input type="checkbox" name="navLibre"><span>Navegación libre: saltear preguntas y volver atrás</span></label>' +
    '      <p class="ae-ayuda">Opcional. Aparecen las casillas numeradas para ir a cualquier pregunta, y podés terminar cuando quieras. Si la corrección es al final, podés cambiar lo que contestaste hasta terminar.</p>' +
    '    </div>' +
    '  </div>' +
    '  <div class="ae-sub" data-modo="interactivo">' +
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

    '<fieldset class="ae-paso" data-tras-etapa>' +
    '  <legend><span class="ae-num"></span>Contenido</legend>' + BLOQUEADO +
    '  <div class="ae-campo" data-etapa="2" data-modo="interactivo">' +
    '    <label class="ae-check"><input type="checkbox" name="soloParcial"><span>Solo tal cual del parcial</span></label>' +
    '    <p class="ae-ayuda">Solo ejercicios que están exactamente como vinieron en un parcial: sin los inventados parecidos ni los de finales.</p>' +
    '    <div class="ae-linea" data-elegir-parcial hidden><span>¿Qué parcial?</span>' +
    '      <select class="ae-input ae-select" name="parcial"><option value="">Todos, mezclados</option></select></div>' +
    '    <p class="ae-ayuda" data-ayuda-parcial hidden></p>' +
    '  </div>' +
    '  <div class="ae-campo" data-etapa="2" data-modo="interactivo">' +
    '    <label class="ae-check"><input type="checkbox" name="fundamentales"><span>Ejercicios fundamentales (plan de urgencia)</span></label>' +
    '    <p class="ae-ayuda">4 o 5 ejercicios por unidad, con la forma del Parcial 2025, que cubren las variantes que pueden tomar. Salen todos los de las unidades que elijas, en el orden en que conviene estudiarlos.</p>' +
    '  </div>' +
    '  <div class="ae-campo" data-etapa="1">' +
    '    <label class="ae-check"><input type="checkbox" name="urgente1"><span>Modo urgente: solo las preguntas fundamentales</span></label>' +
    '    <p class="ae-ayuda">Las de teoría que más probablemente tomen (demostraciones, propiedades, condiciones de cada modelo, características de la normal, la t) y alguna cuenta rápida. Salen todas las de las unidades que elijas, de la más probable a la menos.</p>' +
    '  </div>' +
    '  <div class="ae-campo">' +
    '    <span class="ae-etq">Unidades</span>' +
    '    <div class="ae-caja-unidades" data-unidades></div>' +
    '    <p class="ae-ayuda" data-unidades-fijas hidden>Las pone el parcial elegido.</p>' +
    '  </div>' +
    '  <p class="ae-ayuda" data-modo="interactivo" data-etapa="2" data-disp-ejercicios></p>' +
    '  <fieldset class="ae-campo" data-bloque="tipos" data-etapa="2" data-modo="normal">' +
    '    <span class="ae-etq">Tipo de enunciado</span>' +
    '    <div class="ae-tipos">' +
    '      <label class="ae-chip"><input type="checkbox" name="teoria"><span><b>Teoría</b><small data-disp="teoria"></small></span></label>' +
    '      <label class="ae-chip"><input type="checkbox" name="practica"><span><b>Práctica</b><small data-disp="practica"></small></span></label>' +
    '    </div>' +
    '    <p class="ae-motivo">Elegí al menos una unidad para habilitar esto.</p>' +
    '  </fieldset>' +
    '</fieldset>' +

    '<fieldset class="ae-paso" data-tras-etapa>' +
    '  <legend><span class="ae-num"></span>Cantidad</legend>' + BLOQUEADO +
    '  <fieldset class="ae-campo" data-bloque="cuestionario" data-etapa="1">' +
    '    <label class="ae-cant">Preguntas <input class="ae-input ae-corto" type="number" name="cantCuestionario" min="1"> <small data-de="cuestionario"></small></label>' +
    '    <p class="ae-ayuda" data-ayuda-cuestionario></p>' +
    '    <p class="ae-motivo">Elegí al menos una unidad para habilitar esto.</p>' +
    '  </fieldset>' +
    '  <fieldset class="ae-campo" data-bloque="ejercicios" data-etapa="2" data-modo="interactivo">' +
    '    <label class="ae-cant">Ejercicios <input class="ae-input ae-corto" type="number" name="cantEjercicios" min="1"> <small data-de="ejercicio"></small></label>' +
    '    <p class="ae-ayuda" data-ayuda-ejercicios></p>' +
    '    <p class="ae-motivo">Elegí al menos una unidad para habilitar esto.</p>' +
    '  </fieldset>' +
    '  <fieldset class="ae-campo" data-bloque="cantidad" data-etapa="2" data-modo="normal">' +
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
    '  <fieldset class="ae-campo" data-bloque="orden" data-etapa="2" data-modo="normal">' +
    '    <label class="ae-etq">Orden de las preguntas</label>' +
    '    <select class="ae-input ae-select" name="orden">' +
    '      <option value="aleatorio">Aleatorio</option>' +
    '      <option value="teoria">Primero teoría</option>' +
    '      <option value="practica">Primero práctica</option>' +
    '    </select>' +
    '    <p class="ae-motivo">El orden solo tiene sentido con Teoría y Práctica marcadas.</p>' +
    '  </fieldset>' +
    '</fieldset>' +

    '<fieldset class="ae-paso" data-tras-etapa>' +
    '  <legend><span class="ae-num"></span>Corrección y tiempo</legend>' + BLOQUEADO +
    '  <div class="ae-campo" data-etapa="1">' +
    '    <label class="ae-check"><input type="checkbox" name="corregirYa"><span>Corregir cada pregunta al responderla</span></label>' +
    '    <p class="ae-ayuda" data-ayuda-corregirya></p>' +
    '  </div>' +
    '  <fieldset class="ae-campo" data-bloque="correccion" data-etapa="2">' +
    '    <label class="ae-check"><input type="checkbox" name="verRespuesta"><span>Mostrar la respuesta correcta después de cada pregunta</span></label>' +
    '    <p class="ae-ayuda">Desactivado: respondés de corrido y en el informe final ves cuáles hiciste bien y qué elegiste.</p>' +
    '    <p class="ae-motivo">En el estilo guiado y en el interactivo la corrección siempre es inmediata.</p>' +
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
    /* inicial (opcional, lo manda la ruta recomendada): { nombre, config }.
       El formulario aparece completo y solo falta guardar. */
    mostrar: function (cont, materia, acciones, inicial) {
      var h = E.h;
      var c = Object.assign({}, POR_DEFECTO, (inicial && inicial.config) || {});

      E.vaciar(cont);
      cont.appendChild(h("button", { class: "ev-volver", type: "button", onclick: function () { acciones.volver(); } }, "← Evaluación"));
      cont.appendChild(h("p", { class: "kicker ev-kicker" }, "Autoevaluación"));
      cont.appendChild(h("h1", { class: "ev-h1" }, "Nueva autoevaluación"));

      if (inicial) {
        cont.appendChild(h("div", { class: "caja caja-ojo" }, [
          h("span", { class: "caja-tit" }, "Armada por la ruta recomendada"),
          h("p", {}, "Ya esta todo elegido. Revisalo si queres y toca Guardar, o Guardar y comenzar.")
        ]));
      }
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
      campo("nombre").value = (inicial && inicial.nombre) || "";
      if (c.etapa) { form.querySelector('[name="etapa"][value="' + c.etapa + '"]').checked = true; }
      campo("cantCuestionario").value = c.cantCuestionario;
      form.querySelector('[name="formato1"][value="' + (c.formato1 === "virtual" ? "virtual" : "hoja") + '"]').checked = true;
      campo("urgente1").checked = !!c.urgente1;
      campo("corregirYa").checked = !!c.corregirYa;
      form.querySelector('[name="modo"][value="' + c.modo + '"]').checked = true;
      form.querySelector('[name="estilo"][value="' + c.estilo + '"]').checked = true;
      campo("navLibre").checked = c.navLibre;
      campo("cantEjercicios").value = c.cantEjercicios;
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
      campo("soloParcial").checked = !!c.soloParcial;
      campo("fundamentales").checked = !!c.fundamentales && !c.soloParcial;
      // los parciales enteros que hay en el banco, para elegir uno
      var parciales = E.banco.parciales(materia);
      parciales.forEach(function (x) {
        campo("parcial").appendChild(h("option", { value: x.nombre },
          x.nombre + " completo (" + x.ejercicios + (x.ejercicios === 1 ? " ejercicio)" : " ejercicios)")));
      });
      campo("parcial").value = c.parcial && parciales.some(function (x) { return x.nombre === c.parcial; }) ? c.parcial : "";
      function parcialElegido(v) {
        if (v.modo !== "interactivo" || !v.soloParcial || !v.parcial) { return null; }
        return parciales.filter(function (x) { return x.nombre === v.parcial; })[0] || null;
      }

      function leer() {
        var marcado = function (sel) { var el = form.querySelector(sel + ":checked"); return el ? el.value : null; };
        return {
          etapa: marcado('[name="etapa"]'),
          cantCuestionario: entero(campo("cantCuestionario").value),
          formato1: marcado('[name="formato1"]') || "hoja",
          urgente1: campo("urgente1").checked,
          corregirYa: campo("corregirYa").checked,
          modo: marcado('[name="modo"]'),
          estilo: marcado('[name="estilo"]'),
          navLibre: campo("navLibre").checked,
          cantEjercicios: entero(campo("cantEjercicios").value),
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
          minutos: entero(campo("minutos").value),
          soloParcial: campo("soloParcial").checked,
          parcial: campo("parcial").value,
          fundamentales: campo("fundamentales").checked
        };
      }

      function sincronizar() {
        var v = leer();

        // Un parcial entero: sus unidades y su cantidad de ejercicios quedan fijas.
        var entero_ = parcialElegido(v);
        // "tal cual del parcial" y "fundamentales" no van juntas: una apaga a la otra
        campo("fundamentales").disabled = v.soloParcial;
        campo("soloParcial").disabled = v.fundamentales;
        var fund = v.modo === "interactivo" && v.fundamentales;
        form.querySelector("[data-elegir-parcial]").hidden = !(v.modo === "interactivo" && v.soloParcial);
        form.querySelectorAll('[name="unidad"]').forEach(function (i) {
          if (entero_) { i.checked = entero_.unidades.indexOf(i.value) !== -1; }
          i.disabled = !!entero_;
        });
        campo("cantEjercicios").disabled = !!entero_;
        if (entero_) { campo("cantEjercicios").value = entero_.ids.length; }
        var ayudaParcial = form.querySelector("[data-ayuda-parcial]");
        ayudaParcial.hidden = !entero_;
        ayudaParcial.textContent = entero_
          ? "Se hace el " + entero_.nombre + " entero y en el orden del examen, cada ejercicio desglosado en pasos: " +
            entero_.ejercicios + " ejercicios, de " + entero_.unidades.map(function (u) { return E.numeroDeUnidad(materia, u); }).join(", ") +
            (entero_.partidos.length ? " (el " + entero_.partidos.join(" y el ") + " va en dos partes, a y b, porque son de unidades distintas)" : "") +
            ". Las unidades y la cantidad se ponen solas."
          : "";
        v = leer();

        var disp = E.banco.disponibles(materia, v.unidades, v.etapa !== "1" && v.soloParcial, v.etapa !== "1" && fund,
          { hoja: v.formato1 === "hoja", urgente: v.urgente1 });

        // etapa -> todo lo demas. Lo de la otra etapa se esconde.
        Array.prototype.forEach.call(form.querySelectorAll("[data-tras-etapa]"), function (f) {
          f.disabled = !v.etapa;
        });
        // antes de elegir se ven los pasos de la 2da (bloqueados), para que se note lo que viene
        Array.prototype.forEach.call(form.querySelectorAll("[data-etapa]"), function (el) {
          el.hidden = el.getAttribute("data-etapa") !== (v.etapa || "2");
        });
        // y dentro de la 2da, lo de cada modo
        Array.prototype.forEach.call(form.querySelectorAll("[data-modo]"), function (el) {
          if (el.getAttribute("data-etapa") && el.hidden) { return; }
          el.hidden = el.getAttribute("data-modo") !== v.modo;
        });
        var n = 0;
        Array.prototype.forEach.call(form.querySelectorAll(".ae-paso"), function (f) {
          if (!f.hidden) { f.querySelector(".ae-num").textContent = String(++n); }
        });
        var primera = v.etapa === "1";
        var interactivo = !primera && v.modo === "interactivo";
        var guiado = !primera && E.guiado(v);

        // 1ra etapa: unidades -> cantidad del cuestionario
        bloque("cuestionario").disabled = !v.unidades.length;
        campo("cantCuestionario").max = disp.cuestionario;
        if (disp.cuestionario > 0 && entero(campo("cantCuestionario").value) > disp.cuestionario) {
          campo("cantCuestionario").value = disp.cuestionario;
        }
        // modo urgente: salen todas las urgentes de esas unidades
        campo("cantCuestionario").disabled = v.urgente1;
        if (v.urgente1) { campo("cantCuestionario").value = disp.cuestionario; v.cantCuestionario = disp.cuestionario; }
        form.querySelector('[data-de="cuestionario"]').textContent = v.urgente1
          ? "(todas las urgentes)" : "de " + disp.cuestionario;
        form.querySelector("[data-ayuda-corregirya]").textContent = v.corregirYa
          ? "Cada pregunta tiene un botón Comprobar: te dice si está bien, cuál es la correcta y por qué. Una vez comprobada ya no se cambia."
          : "Como en el examen: contestás todo, entregás, y recién ahí ves la corrección de cada pregunta.";
        form.querySelector("[data-ayuda-formato1]").textContent = v.formato1 === "virtual"
          ? "Como el Cuestionario del Aula Virtual: opción única, varias correctas, verdadero o falso y completar con coma y 2 decimales."
          : "Como ahora en la hoja: opción múltiple (puede haber varias correctas) y verdadero o falso. Sin completar.";
        form.querySelector("[data-ayuda-cuestionario]").textContent = (v.urgente1
          ? "Salen todas las urgentes de las unidades elegidas: " + disp.cuestionario + "."
          : v.formato1 === "virtual" ? "El cuestionario virtual traía 8 preguntas de 12 o 14 puntos."
          : "En hoja son 10 preguntas.") + " Acá cada pregunta vale lo mismo y la nota se lleva a 100.";

        form.querySelector("[data-ayuda-nivel]").textContent = AYUDA_NIVEL[v.nivel];
        form.querySelector("[data-ayuda-estilo]").textContent = v.estilo === "guiado"
          ? "Preguntas fáciles: con pistas, la práctica en todos sus pasos, y si te equivocás volvés a intentar."
          : "Enunciado y opciones: respondés y se corrige, como en el examen.";

        // interactivo: unidades -> cantidad de ejercicios
        var hayUnidadI = v.unidades.length > 0;
        bloque("ejercicios").disabled = !hayUnidadI;
        campo("cantEjercicios").max = disp.ejercicio;
        if (disp.ejercicio > 0 && entero(campo("cantEjercicios").value) > disp.ejercicio) {
          campo("cantEjercicios").value = disp.ejercicio;
        }
        // fundamentales: salen todos los de las unidades elegidas
        if (fund) {
          campo("cantEjercicios").disabled = true;
          campo("cantEjercicios").value = disp.ejercicio;
          v.cantEjercicios = disp.ejercicio;
        }
        form.querySelector('[data-de="ejercicio"]').textContent = entero_
          ? "(el parcial entero)" : fund ? "(todos los fundamentales)" : "de " + disp.ejercicio;
        form.querySelector("[data-unidades-fijas]").hidden = !entero_;
        form.querySelector("[data-disp-ejercicios]").textContent = entero_
          ? ""
          : hayUnidadI
          ? (v.soloParcial ? "Ejercicios completos tal cual del parcial en esas unidades: "
             : fund ? "Ejercicios fundamentales en esas unidades: "
                           : "Ejercicios completos disponibles en esas unidades: ") + disp.ejercicio + "." +
            (fund && !disp.ejercicio ? " En esas unidades todavía no hay fundamentales." : "") +
            (v.soloParcial && !disp.ejercicio ? " En esas unidades no hay ejercicios de parcial: sacá la casilla o sumá otra unidad." : "")
          : "Elegí las unidades y se cuentan los ejercicios disponibles.";
        form.querySelector("[data-disp-ejercicios]").hidden = !!entero_;
        form.querySelector("[data-ayuda-ejercicios]").textContent = (entero_
          ? "Son los ejercicios del " + entero_.nombre + ", en el orden del examen."
          : fund
          ? "Salen todos, unidad por unidad y del más probable al menos probable: primero lo que más se repite en los parciales 2025 y 2023, los finales y las guías."
          : v.soloParcial
          ? "Ejercicios de los parciales, tal cual, mezclados."
          : "Se mezclan ejercicios reales de los parciales y finales con otros inventados con la misma forma.") +
          " Si uno no lo querés hacer ahora, lo salteás y lo retomás antes de terminar.";

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
        bloque("correccion").disabled = guiado;

        campo("minutos").disabled = !v.conTiempo;

        var completo = primera || interactivo ? hayUnidad : hayTipo;
        form.querySelector("[data-resumen]").textContent = !v.etapa
          ? "Elegí la etapa del parcial para empezar."
          : completo ? "Resumen: " + E.resumenConfig(materia, v).join(" · ")
          : "Completá los pasos para ver el resumen.";
      }

      function validar(v, nombre) {
        var errores = [];
        var fund = v.etapa !== "1" && v.modo === "interactivo" && v.fundamentales;
        var disp = E.banco.disponibles(materia, v.unidades, v.etapa !== "1" && v.soloParcial, fund,
          { hoja: v.formato1 === "hoja", urgente: v.urgente1 });
        var deParcial = v.soloParcial ? " tal cual del parcial" : fund ? " fundamentales" : "";
        if (!v.etapa) { return ["Elegí la etapa del parcial que querés simular."]; }
        if (!nombre) { errores.push("Poné un nombre: es obligatorio."); }
        if (v.etapa === "1") {
          if (!v.unidades.length) { errores.push("Elegí al menos una unidad."); }
          else if (!disp.cuestionario) { errores.push("No hay preguntas de 1ra etapa en las unidades elegidas."); }
          else if (!v.urgente1 && (v.cantCuestionario < 1 || v.cantCuestionario > disp.cuestionario)) {
            errores.push("La cantidad de preguntas tiene que ir de 1 a " + disp.cuestionario + ".");
          }
          if (v.conTiempo && (v.minutos < 1 || v.minutos > MAX_MINUTOS)) { errores.push("El contador va de 1 a 240 minutos (4 horas)."); }
          return errores;
        }
        if (E.conVidas(v) && (v.fallos < 1 || v.fallos > 200)) {
          errores.push("Las vidas van de 1 a 200.");
        }
        if (v.modo === "interactivo") {
          if (!v.unidades.length) { errores.push("Elegí al menos una unidad."); }
          else if (!disp.ejercicio) { errores.push("No hay ejercicios completos" + deParcial + " en las unidades elegidas."); }
          else if (!parcialElegido(v) && !fund && (v.cantEjercicios < 1 || v.cantEjercicios > disp.ejercicio)) {
            errores.push("La cantidad de ejercicios tiene que ir de 1 a " + disp.ejercicio + ".");
          }
          if (v.conTiempo && (v.minutos < 1 || v.minutos > MAX_MINUTOS)) { errores.push("El contador va de 1 a 240 minutos (4 horas)."); }
          return errores;
        }
        if (!v.unidades.length) { errores.push("Elegí al menos una unidad."); }
        else if (!v.teoria && !v.practica) { errores.push("Marcá Teoría, Práctica o ambas."); }
        else {
          var revisar = function (cant, max, que) {
            if (max === 0) { errores.push("No hay preguntas de " + que + deParcial + " en las unidades elegidas."); }
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

      function disp1(v) {
        return E.banco.disponibles(materia, v.unidades, false, false, { hoja: v.formato1 === "hoja", urgente: v.urgente1 }).cuestionario;
      }

      function guardar(lanzar) {
        var v = leer();
        var nombre = campo("nombre").value.trim();
        var errores = validar(v, nombre);
        var caja = form.querySelector("[data-errores]");
        campo("nombre").classList.toggle("ae-invalido", !!v.etapa && !nombre);

        if (errores.length) {
          E.vaciar(caja);
          caja.appendChild(h("b", {}, "Falta completar:"));
          caja.appendChild(h("ul", {}, errores.map(function (e) { return h("li", {}, e); })));
          caja.hidden = false;
          if (v.etapa && !nombre) { campo("nombre").focus(); }
          return;
        }

        if (v.etapa === "1") {
          v.modo = "normal"; v.teoria = false; v.practica = false; v.verRespuesta = false; v.soloParcial = false;
          // en la 1ra etapa "fundamentales" es el modo urgente
          v.fundamentales = v.urgente1;
          if (v.urgente1) { v.cantCuestionario = disp1(v); }
        } else { v.urgente1 = false; v.formato1 = "hoja"; v.corregirYa = false; }
        if (v.modo === "interactivo") { v.teoria = false; v.practica = false; v.navLibre = false; }
        // "tal cual del parcial" y el parcial entero son del interactivo
        if (v.etapa !== "1" && v.modo !== "interactivo") { v.soloParcial = false; v.fundamentales = false; }
        if (!v.soloParcial) { v.parcial = ""; }
        if (v.soloParcial) { v.fundamentales = false; }
        if (v.fundamentales) { v.cantEjercicios = E.banco.disponibles(materia, v.unidades, false, true).ejercicio; }
        var pe = parcialElegido(v);
        if (pe) { v.cantEjercicios = pe.ids.length; v.unidades = pe.unidades.slice(); }
        v.v = 2;   // esquema de modos nuevo (ver E.guiado en nucleo.js)
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
    }
  };
})(window.NC.eval);
