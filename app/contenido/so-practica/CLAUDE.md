# Sistemas Operativos — Práctica (so-practica) — cómo se escribe su contenido

Las reglas generales están en `docs/contenido.md` (raíz del repo); acá va solo lo propio de SO Práctica.

## Qué hay

- **Solo Evaluación** (pedido de Fran, 26/10/2026): sin unidades. En `materias.json` no tiene
  `unidades`; app.js la muestra igual porque tiene parciales, con una sola entrada "Evaluación".
  Si se suman apuntes, se cargan como clases (`"num": "Clase 14"`).
- **Parciales** (`evaluacion/parciales/`), uno por pregunta (`NN-pregunta-NN.html`):
  - `2026-primer-parcial`: el EI1 de Fran (16/06/2026), de 25 capturas en
    `SISTEMAS 3\SO PRACTICA\parcial 1 SO practica\` (dos no son del parcial: una de PyE y una del
    campus). El orden es el de las capturas. La 19 (qué SO no expuso ningún grupo) quedó como
    "Vailux OS, no confirmado": la lista de grupos no está en el material.
  - `2025-segundo-parcial`: `Parcial SO Practica 2.pdf` (cuestionario en blanco).
  - `2026-segundo-parcial-probable`: inventado, misma forma que el 2025, **sin repetir ninguna
    pregunta** del 2025 ni del primer parcial. Si aparece otro parcial real, revisar que no se pise.
- **Autoevaluación** (`evaluacion/preguntas/parcial-2025/`, ids `so-p2025-NN`, y
  `parcial-probable/`, ids `so-prob-NN`): las 20 de cada parcial en formato cuestionario. Cada
  carpeta es un tema del formulario, con el nombre de su `p-fuente` (`E.temas`, `banco.carpetas`). `data-etapa="1"`; emparejar =
  `completar` con desplegables.
  Las armó un script desde el parcial (no quedó en el repo): si se corrige una pregunta del parcial,
  corregirla también acá. Las opciones se mezclan al sortear, así que la explicación nombra cada
  opción por su texto, nunca por la letra.
- **Imágenes** en `app/img/so-practica/<parcial>/`, recortadas de las capturas sin las respuestas
  marcadas por Fran. En `cat.png` el hash de la contraseña del profe está difuminado (repo público).
  Los dibujos del probable (RAID y htop) son SVG en línea; los generó un script que no quedó en el
  repo: si hay que cambiarlos, se edita el SVG del fragmento.

## Fuentes y alcance

- Material en `C:\Users\Fran\Desktop\SISTEMAS 3\SO PRACTICA\`, en texto en `fuentes/so-practica/`.
  Muchas diapositivas son solo imagen (lista de `/var/log`, colores de htop, RAID, MBR/GPT): se miran
  con `python fuentes/pagina.py`.
- **Primer parcial (EI1):** clases 3, 4, 5, 6, 7, 10, 11 y 12 (y cayó una de hipervisores, clase 2).
- **Segundo parcial:** clases 14 a 20 (logs, swap, memoria y caché, sistemas de archivos y
  directorios, particiones MBR/GPT, RAID y Espacios de almacenamiento) y la exposición de
  Escritorio remoto. 20 preguntas de 5 puntos en el Aula Virtual: opción múltiple, V/F, emparejar
  y capturas para leer.
- En `fuentes/so-practica/Practica/Escritorio_Remoto_de_Windows.md` se sacaron a mano los nombres
  de los alumnos que la hicieron; si se vuelve a extraer, sacarlos otra vez.
- La cátedra no publica respuestas: son resoluciones propias, citando clase y diapositiva.

## Forma de cada pregunta

- Cabecera con `Pregunta N`, `5 pts` y la clase en `parcial-tema`; la indicación de Moodle en
  cursiva ("Seleccione una o más de una:"); opciones en `ol.parcial-incisos`; V/F en un `<p>`.
- Emparejar: tabla con "Elegir…" y la lista "Opciones del desplegable" (las frases de las
  diapositivas cuando la copia no las trae).
- Resultados: solo las letras correctas. Explicación: qué evalúa, la teoría en tabla, opción por
  opción (`¿Va?` y por qué) y trampas. En el probable, además "Por qué puede entrar".
