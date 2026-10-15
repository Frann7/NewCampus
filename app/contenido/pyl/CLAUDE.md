# Paradigmas y Lenguajes (pyl) — cómo se escribe su contenido

Las reglas generales están en `docs/contenido.md` (raíz del repo); acá va solo lo propio de PyL.

## Fuentes y alcance

- **Alcance:** el **parcial de autómatas** (TOPIC 1 y TOPIC 2 de la cátedra). Programación
  Funcional (TOPIC 3) no entra: queda para después (ver Pendientes).
- **Fuentes:** `C:\Users\Fran\Desktop\SISTEMAS 3\PYL\`, en texto en `fuentes/pyl/` (raíz del repo,
  `fuentes/pyl/INDICE.md` dice qué es cada una). Las diapositivas casi no tienen texto: la teoría
  es corta y la práctica sale de los exámenes y del Trabajo Práctico I (`TOPIC 1/Practica_I`).
- **Exámenes:** parcial y recuperatorio 2023 (PDF) y 2025 (fotos). Los cuatro tienen la misma
  forma, que manda sobre todo lo demás:
  1. (20) Dado un autómata, pasar a ER.
  2. (60) Dada una ER, pasar a autómata determinístico mínimo.
  3. (20) Hacer un AFD o AFND (y a veces la ER) para un lenguaje descripto con palabras.
- **Las unidades del campus son esos tres ejercicios** (decisión de Fran, 14/10/2026), más una base:
  `u1` Lenguajes, autómatas y ER · `u2` De AF a ER · `u3` De ER a AFD mínimo · `u4` Diseñar AF y ER.
- **En la teoría y en la práctica no va el enunciado de ningún examen:** quedan en Evaluación,
  para rendirlos sin haberlos visto. Los ejemplos son inventados, con la misma forma.

## Cómo se escribe

- **Teoría bien concisa, para leer rápido** (pedido de Fran: el parcial es solo práctica). Cada
  sección: qué es (dos o tres renglones) → cómo se hace (pasos numerados, cortos) → **muchos
  ejemplos** (mínimo dos: uno chico y uno con forma de parcial) → errores y trampas
  (`.caja.caja-ojo`). Nada de párrafos largos: el detalle va en los ejemplos.
- **Práctica:** cada ejercicio resuelto entero, con `.paso` por etapa y el dibujo de cada etapa.
  Al final, la respuesta en `.caja.caja-resp` y una tabla **"Probamos con cadenas"** (cadena,
  ¿la acepta?, por qué): es lo que se hace en la hoja para no entregar un autómata roto.
- **Notación (la de la cátedra):** ER con `|` (unión), concatenación sin punto, `*`, `ε` y
  paréntesis; prioridad `*` → concatenación → `|`. Estados `q0, q1...` en los autómatas dados;
  en la construcción de subconjuntos, `A, B, C...` (con su conjunto de estados al lado) y `∅`
  para el estado muerto; particiones `P1, P2...`.
- **Thompson como la cátedra:** en la concatenación el final de Nr y el inicial de Ns son el mismo
  estado; la clausura lleva las cuatro ε (entrar, salir, volver y saltear). Los estados se numeran
  de izquierda a derecha (lo hace el script).
- **AF → ER como la cátedra:** sacar los estados muertos, agregar `i` y `f` con ε, eliminar los
  intermedios de a uno con la regla α β* γ y juntar paralelas con `|`. En cada paso se dibuja el
  autómata que queda: la transición nueva en verde (`nueva`) y el estado que sigue en celeste
  (`marcados`).
- **Estado muerto:** en las tablas va siempre (`∅`); en los dibujos del AFD mínimo también, punteado.
  Cuando la consigna dice "AFD o AFND" se puede dibujar sin él, y se aclara.
- `00-intro.html` de cada unidad: título, bajada y "Cómo leer esta unidad" (`data-abierta`):
  qué ejercicio del parcial es y cuántos puntos vale.

## Diagramas

No se dibujan a mano: cada autómata se describe en `fuentes/pyl/diagramas/` (`teoria.py` para la
teoría de las cuatro unidades, `u2.py`, `u3.py` y `u4.py` para las prácticas, `evaluacion.py` para
los exámenes y `practica-parcial.py` para el parcial inventado), con el formato explicado arriba de
`fuentes/automatas.py`, y va en el fragmento como `<div class="pd-grafico af" data-g="nombre"></div>`.

- `python fuentes/automatas.py fuentes/pyl/diagramas/u3.py` mete los SVG en los fragmentos.
- `python fuentes/automatas.py --verificar fuentes/pyl/diagramas/u3.py` prueba cada dibujo que
  tenga `er` y `sigma` (o `cumple`) con todas las cadenas hasta largo 8. **Todo dibujo de una
  resolución lleva su `er`**, también los pasos intermedios de AF → ER (el lenguaje no cambia
  de paso a paso): así un error de una transición salta solo.
- `python fuentes/automatas.py --resolver "ER"` imprime Thompson, la tabla de subconjuntos
  (mueve y ε-clausura de cada estado), las particiones y el AFD mínimo. **Las tablas de
  ER → AFD se copian de ahí**, no se calculan a mano. `thompson("ER")` en el archivo de
  diagramas dibuja el AFN-ε con la misma numeración.

## Evaluación

- `"evaluacion": {"tipo": "simple"}` sin banco de preguntas: la pestaña muestra solo los parciales
  (decisión de Fran: el parcial es dibujar en la hoja).
- Exámenes en `evaluacion/parciales/`, una consigna por archivo con `pd-resultados` y
  `pd-explicacion`. La cátedra no publicó resoluciones: son resoluciones propias, verificadas con
  el script. Más un parcial inventado para practicar, con la misma forma.
- **Marcas:** ◈ (`variante`, `data-examen-ref="Parciales 2023-2025 · ej. N"`) en los ejercicios de
  práctica con la forma de una consigna del parcial; ★ (`igual`) en un ejercicio del TP I que
  tomaron tal cual (el 80, recuperatorio 2023: no se resuelve en la práctica, se manda a Evaluación).

## Pendientes e ideas

- Programación Funcional (TOPIC 3): cargarla cuando se acerque su evaluación.
- Completar las tablas "página → qué hay" de los `.md` de `fuentes/pyl/`.
