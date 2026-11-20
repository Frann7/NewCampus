# Matemática Discreta (md) — cómo se escribe su contenido

Las reglas generales de teoría y práctica están en `docs/contenido.md` (raíz del repo); acá va
solo lo propio de Matemática Discreta.

## Fuentes y alcance

- **Siete unidades**, una por PDF de teoría de la cátedra (diapositivas de 2025 y 2026):
  U1 Combinatoria, U2 Lenguajes y máquinas de estados finitos (MEF), U3 Álgebras booleanas,
  U4 Relaciones de recurrencia, U5 El sistema de los enteros, U6 Anillos y aritmética modular,
  U7 Grupos y teoría de la codificación.
- **Manda el PDF de la cátedra** (`fuentes/md/`, con su `INDICE.md`): de ahí sale la teoría, con
  su notación y su orden. El **Grimaldi** (y el Johnsonbaugh en U1) es apoyo: para lo que la
  diapositiva da muy escueto. **Criterio del contribuidor:** lo importante es lo de los PDFs de
  la cátedra (teoría, guías complementarias, actividades de vacaciones, parciales); los
  ejercicios del libro no se resuelven todos "por las dudas": hay algunos hechos como apoyo
  (U3: Grimaldi 15.1 ej. 1–13, sugeridos en la última diapositiva; U4: la selección del cap. 10;
  sueltos en U1, U2 y U5). Los libros están solo en la PC del contribuidor (`fuentes/md/LIBROS/`,
  fuera del repo). Del libro no se copian párrafos: se explica con palabras propias.
- **Tres parciales:** el 1ro toma U2 y U3 (en 2026 **no** entró combinatoria; otros años sí), el
  2do U4 y U5, el 3ro U6 y U7. Cada uno tiene su **guía complementaria**, que son ejercicios con
  forma de parcial. Las "Actividades de vacaciones" traen un **recuperatorio** (actividad B: Boole
  y MEF) y tres de recurrencia.
- **Exámenes cargados:** Parcial 1 2026 y Parcial 2 2026 (transcriptos en `fuentes/md/Examenes/`,
  de fotos que no están en el repo; no se copian nombres ni lo escrito a mano). Finales: todavía
  no hay.

## Cómo se escribe

- **Teoría (cada sección):** Para qué sirve → Definición (con la notación de la cátedra) → Qué
  significa cada símbolo (tabla) → De dónde sale (la demostración o el razonamiento, cuando la
  cátedra la da o el parcial la puede pedir) → Ejemplos (mínimo 2: uno simple y uno con forma de
  parcial, sacado de la guía complementaria o parecido). En cada ejemplo, el **Desarme del
  enunciado** (Frase / Qué significa / La cuenta / A dónde va) y cada paso explicado.
- **Se explica desde cero:** quien estudia no vio nunca el tema. Toda notación (\(\Sigma^{*}\),
  \(\nu\), \(\omega\), \(\prod M\), \(a \mid b\), \(\mathbb{Z}_n\), \(\varphi(n)\)...) se explica
  antes de usarla, y las demostraciones se hacen renglón por renglón, diciendo qué propiedad se
  usa en cada uno.
- **Práctica:** los ejercicios de la selección de la cátedra (libro) y los de la guía
  complementaria, resueltos enteros, un archivo por ejercicio. La técnica se repite en cada
  inciso (la fórmula, la regla del método). Al final, el resultado **contrastado con las
  soluciones del libro** (los capítulos vienen "con soluciones") o, en la complementaria, con una
  verificación propia; si no coincide, caja `.caja-ojo` y se explica.
- **Orden de la práctica:** primero los del libro, en el orden de las secciones (lo básico), y
  después la complementaria (lo de parcial). El `00-intro.html` de la práctica dice qué hacer si
  hay poco tiempo.
- **Número en el índice lateral:** como hay varias fuentes con la numeración repetida, cada
  `.tag` lleva el número a mano: `<span class="tag" data-num-ej="10.2-3.">Grimaldi 10.2 &middot;
  Ej. 3 &middot; ...</span>` (sección y ejercicio del libro) y `data-num-ej="C-4."` en la guía
  complementaria; si la guía tiene varios bloques numerados desde 1 en la misma unidad, una letra
  por bloque (U2: `CL-` lenguajes, `CM-` máquinas; U5: `CD-` divisibilidad, `CM-` mcd, `CT-` TFA).
  Actividades de vacaciones: `V-A.`, `V-B.`...
- **Números verificados con Python** (scratchpad) antes de escribirlos: conteos, recurrencias
  (calcular los primeros términos con la relación y con la fórmula cerrada), mcd y coeficientes de
  Bézout, inversos módulo \(n\), tablas de verdad, distancias de un código. Las MEF se prueban
  simulándolas con cadenas.
- **Marcas de examen:** ★ (`data-examen="igual"`) si lo tomaron casi tal cual en un parcial
  (Parcial 1 2026, Parcial 2 2026 o el recuperatorio de las Actividades de vacaciones); ◈
  (`variante`) si es la misma forma de consigna con otro caso. Se marcan mirando
  `fuentes/md/Examenes/`, nunca de memoria. La guía complementaria **no** es un examen: sola no
  da ★.

## Notación (la de la cátedra)

- MEF: \(M = (S, I, O, \nu, \omega)\), \(\nu\) la función de estado siguiente y \(\omega\) la de
  salida; la tabla con columnas \(\nu\) y \(\omega\) por cada entrada; en el diagrama cada flecha
  dice "entrada,salida". \(\lambda\) la cadena vacía; \(\Sigma^{*}\), \(\Sigma^{+}\), \(\Sigma^{n}\).
- Boole: complemento con barra (\(\overline{x}\)), \(+\) y \(\cdot\); f.n.d. y f.n.c.;
  mintérminos \(\sum m(\dots)\) y maxtérminos \(\prod M(\dots)\).
- Recurrencias: \(a_n^{(h)}\) la solución de la homogénea asociada, \(a_n^{(p)}\) la particular.
- Enteros: \(a \mid b\), \(mcd(a, b)\), \(mcm(a, b)\); \(\mathbb{Z}_n\), \(U_n\), \(\varphi(n)\).
- MathJax con `\( \)` y `\[ \]`, nunca `$`. Los "pesos" del enunciado se escriben con la palabra.

## Diagramas

- **MEF:** `<div class="pd-grafico af" data-g="nombre"></div>` y el dibujo descrito en
  `fuentes/md/diagramas/<unidad>.py`; `python fuentes/automatas.py fuentes/md/diagramas/u2.py
  app/contenido/md` mete el SVG. Las máquinas llevan `sep=" | "` (las etiquetas "0,0" se juntan
  como "0,0 | 1,0") y sin `finales`. Se miran después en el navegador: que no se pisen.
- Lo demás (diagramas de Hasse, árboles, tablas de grupos dibujadas) también por script en
  `fuentes/md/`, con las clases `.pd-grafico`; nunca a ojo.

## Evaluación

- Evaluación simple (`"evaluacion": {"tipo": "simple"}`), por ahora **sin banco de preguntas**:
  solo los parciales resueltos en `evaluacion/parciales/` (formato en `docs/evaluacion.md`).

## Pendientes e ideas

- Finales: cargarlos cuando lleguen y repasar las marcas ★ / ◈.
- Banco de autoevaluación (no está hecho).
- 3er parcial: no hay ninguno tomado; solo la guía complementaria.
- Lecturas dudosas, resueltas con una caja de aviso (confirmar con la cátedra si se puede):
  - Parcial 1 2026 ej. 5 con la barra continua \(\overline{xy}\); ej. 4b: 56 máquinas contando
    \(\omega(s_4, 1)\) (28 con solo transiciones).
  - Parcial 2 2026 ej. 2-II con \(p_0 = 100\).
  - Complementaria P2, TFA 2: sin solución tal como está escrita (se tomó \(d = 35\)).
  - Complementaria P1, CM-10c: 726.
  - Complementaria P3: U6 ej. 12 sin fórmula de \(f\) (se tomó \(f(n) = (n \bmod 4, n \bmod 6)\));
    U7 ej. 10c, clases laterales de los dos lados.
  - Diapositivas: U1 diap. 32 ("10 pelotas": exactamente 10, con la otra lectura); U6 diap. 48
    (Z325 debe ser Z315); U7 diap. 28 (la E se tomó como triple repetición); erratas U4 pág. 30
    y 31, U3 diap. 11.
- Las tablas "página → qué hay" de `fuentes/md/` de U6 y U7 están vacías; en U6 las páginas
  31–33, 37–38, 40, 42, 44, 48 y 50–51 salen rotas en el texto extraído (ver el PDF).
