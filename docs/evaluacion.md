# Pestaña Evaluación

> Las rutas de este documento son relativas a `app/` (salvo que digan otra cosa).

**Pestaña Evaluación** (una por materia, no depende de la unidad):

* **Qué evaluación tiene cada materia:** la clave `evaluacion` de `contenido/materias.json`. Sin
  ella, la de PyE (todo lo de abajo). `{"tipo": "simple", "minutos": 40}` (PA) es la **simple**:
  lista de parciales (finales solo si hay) y Autoevaluaciones como en PyE, pero el formulario es
  solo nombre (opcional) y minutos. Corre en `cuestionario.js` (`config.tipo = "simple"`,
  `etapa = "1"`, formato virtual): **todas** las preguntas del banco de la materia, ordenadas por
  id, reloj de cuenta regresiva, nota sobre 100 y revisión con explicación; sin la condición
  30/60 ni nada de etapas. El banco de PA está en `preguntas/parcial-php/` (no es una clase, así
  que sus preguntas no llevan chip de unidad). `E.configMateria`, `E.esSimple` en `nucleo.js`.

* **Parciales y finales:** cada examen es una carpeta con `meta.json` (titulo, fecha, detalle,
  temas: lo que muestra la tarjeta sin abrir el examen) y un archivo por ejercicio. El
  `<article class="parcial">` lo arma `construir.py`, que también le pone el `data-tipo` según la
  carpeta que lo contiene: `parciales/` o `finales/`. Son dos listas separadas en la pantalla de
  Evaluación, pero se escriben y se estilan igual.
  Se transcribe respetando la estructura del original (cabecera, ejercicios con `<h2>` y puntaje,
  `ol.parcial-incisos` para a) b) c), `ol.parcial-sub-incisos` para I) II) III), fórmula y tabla en `.parcial-dos`).
  No se transcriben nombres ni notas de alumnos.
  Un examen puede quedar **solo transcripto**, sin resolver: en ese caso no lleva los desplegables
  y la nota de arriba usa `class="parcial-nota parcial-nota-crudo"` para avisarlo. Cuando se
  resuelve, debajo de los incisos de **cada ejercicio** van dos desplegables dentro de
  `<div class="parcial-extras">`:

  1. `<details class="parcial-desp pd-resultados">` — solo las respuestas, como la hoja de resultados
     de una guía. Sin procedimiento.
  2. `<details class="parcial-desp pd-explicacion">` — la explicación completa, y tiene que alcanzar
     **sin leer las guías**: el enunciado repetido, de qué tema es, los conceptos y fórmulas desde cero,
     el desarme del enunciado, la resolución inciso por inciso con la fórmula repetida, una tabla
     *"Parecido en la guía"* (qué ejercicio se le parece, qué tiene igual y qué cambia) y las trampas.
     Si ayuda un gráfico, va como SVG con las clases de `.pd-grafico` (usan los tokens del tema).

  Dentro de los desplegables se usa `<h4>` y `<span class="paso">`, nunca `<h2>` ni `<h3>`: así el
  índice lateral muestra solo los ejercicios mientras están cerradas. Al **abrir** una explicación,
  sus incisos (`.paso`) y subtítulos (`h4`) se suman al índice de la derecha, debajo de su ejercicio,
  y desaparecen al cerrarla.
* **Banco de preguntas:** una carpeta por unidad y **un archivo por pregunta**, cuyo nombre es el
  `data-id`. El formato completo está en `preguntas/FORMATO.md`. Hay preguntas para las **dos
  etapas del parcial**, porque la cátedra toma cada parcial en dos instancias:
  * **1ra etapa** (`u4-c-...`, `data-etapa="1"`): el cuestionario del Aula Virtual, respuesta corta.
    `data-formato="opcion|multiple|completar"`; en `completar` los huecos son `span.p-hueco`
    (numérico con `data-respuesta="0,20"`, que se acepta **solo con coma y 2 decimales**, o
    desplegable con sus opciones adentro). Sin modo interactivo ni pistas.
  * **2da etapa** (`u4-t-...` / `u4-p-...`): el escrito. `data-tipo="teoria|practica"`, con
    enunciado, opciones (`data-correcta`), pista y explicación; las de práctica además
    `p-pregunta` (modo normal) y `ol.p-pasos` (modo interactivo), con `data-nivel` en cada paso
    (`avanzado` = aparece siempre, `medio` = medio y principiante, `principiante` = solo principiante).

  **Toda pregunta está orientada a los exámenes:** lleva `data-origen="parcial|final"` (se ve como
  ★ dorado o ◈ violeta, con la misma regla que las marcas: si el tema lo tomaron en un parcial, es
  dorado) y un `p-fuente` que dice de qué examen sale. Al sortear, las de parcial salen el doble de
  seguido. `construir.py` rechaza una pregunta sin origen.
  **Toda respuesta numérica se verifica con una cuenta antes de cargarla.**
* **Autoevaluaciones:** lo primero que se elige es la **etapa** que se simula, y hasta elegirla el
  resto del formulario queda bloqueado. La 1ra etapa corre en `cuestionario.js` (todas las
  preguntas en una página, se entrega al final, nota sobre 100 con puntaje parcial y lo que
  significa según el reglamento: 30 regulariza, 60 pasa a la 2da instancia). La 2da corre en
  `examen.js` e `informe.js` y tiene tres maneras (`config.modo` + `config.estilo`): **normal /
  parcial** (opciones), **normal / guiado** (pistas y todos los pasos, sin vidas ni nivel:
  lo que antes se llamaba interactivo) e **interactivo** (ejercicios `-e-` completos, reales e inventados, con los pasos
  agrupados por `data-inciso` y un botón para saltear el ejercicio entero). `E.guiado(c)` dice si
  hay pistas y pasos; `E.conVidas(c)` y `E.nivelDe(c)`, que vidas y nivel son solo del interactivo
  (el guiado usa siempre el nivel principiante). En normal, `config.navLibre` agrega casillas, Anterior/Saltear y Terminar.
  Las que se guardaron antes de existir las etapas se toman como de 2da etapa, y las viejas en
  modo interactivo (sin `config.v`) se migran a normal / guiado, que es lo que eran.
* Las autoevaluaciones que arma el usuario se guardan en el `localStorage` del navegador.

## Estado actual (lo más trabajado)

- **1ra instancia** (preguntas `uN-c-*`, `data-etapa="1"`): ahora es **en hoja**: 10 preguntas de
  opción múltiple (puede haber varias correctas) o V/F, sin completar. Formato "virtual" (Aula
  Virtual, con completar) sigue disponible. Opciones: **modo urgente** (las `uN-c-urgente-*` con
  `data-fundamental`, de la más probable a la menos), **corregir al responder** (botón Comprobar)
  y **📖 Resolver** en cada pregunta (muestra respuesta y explicación; vale 0).
- **2da instancia, interactivo** (ejercicios `uN-e-*`): pasos por nivel (`data-nivel`:
  principiante ⊃ medio ⊃ avanzado), cada paso con `p-consigna`, `p-pista`, `p-explicacion`,
  `p-resolucion`, `p-anotar` ("En la hoja"); por artículo `p-datos` (cuadro de datos, con
  "Planteo en la hoja" en los fundamentales) y `p-rta[data-inciso]`. Botón Resolver, Saltear =
  posponer, revisar ejercicios anteriores, enunciado siempre visible (columna fija).
  Casillas: "Solo tal cual del parcial" (+ elegir Parcial 2025/2023 entero en orden) y
  **"Ejercicios fundamentales"** (`uN-e-fundamental-*`, `data-fundamental` = orden de
  probabilidad; el número del archivo no es el orden).
- **Consignas de pasos:** cada cuenta parcial dice de qué fórmula es y qué parte calcula, con los
  números ("Para estandarizar el 90 se usa z = (x − μ)/σ. Primero el numerador..."). Los pasos
  `medio` se entienden solos (no empiezan con "Ahora..."). La consigna no muestra su resultado.
- Contenido grande del banco se suele escribir con **agentes en paralelo** (uno por unidad), cada
  uno con instrucciones de formato, fuentes, verificación con Python y `construir.py`; después se
  verifica todo junto en el navegador y se hace un solo commit. Como modelo de formato, cada agente
  lee **un** ejercicio parecido, no la unidad entera.
