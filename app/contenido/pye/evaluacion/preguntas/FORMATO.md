# Formato del banco de preguntas

Cada pregunta es un archivo de `preguntas/<unidad>/` y su nombre es el `data-id`.
`construir.py` los pega en orden de nombre.

El parcial tiene **dos etapas**, y el banco tiene preguntas para cada una:

| Etapa | Cómo es en la cátedra | Prefijo del archivo |
| :--- | :--- | :--- |
| 1ra (virtual) | Cuestionario del Aula Virtual: respuesta corta, rápida | `u4-c-...` |
| 2da (escrito) | Problemas y teoría a desarrollar | `u4-t-...` (teoría) · `u4-p-...` (práctica) |

## Regla para todas: orientadas a los exámenes

Toda pregunta sale de algo que **ya tomaron** o de un tema marcado ★ / ◈ en la teoría o la
práctica. Lo dice con dos cosas:

* `data-origen="parcial"` si ese tema lo tomaron en un parcial (se ve como ★), o
  `data-origen="final"` si solo lo tomaron en finales (se ve como ◈). Es obligatorio.
* `<p class="p-fuente">` al final del enunciado, con el examen y el ejercicio.

Al armar una autoevaluación, las de parcial salen el doble de seguido que las de final.

## 2da etapa (escrito)

```html
<article class="preg" data-id="unico" data-tipo="teoria|practica" data-origen="parcial|final">
  <div class="p-enunciado">   enunciado (en practica: el ejercicio completo) + p-fuente
  <div class="p-pregunta">    solo practica: lo que se pregunta en modo NORMAL
  <ul class="p-opciones">     opciones; la correcta lleva data-correcta
  <div class="p-pista">       pista de la lamparita (modo INTERACTIVO)
  <div class="p-explicacion"> se muestra al corregir y en el informe
  <ol class="p-pasos">        solo practica: los pasos del modo INTERACTIVO
    <li data-nivel="..." data-respuesta="0,88">   paso con respuesta numerica
    <li data-nivel="...">  + <ul class="p-opciones">   paso con opciones
```

`data-nivel` = el nivel MAS AVANZADO en el que todavia aparece el paso:
`avanzado` aparece en los tres niveles (partes principales), `medio` en medio y principiante,
`principiante` solo en principiante (las cuentas mas chicas).
`data-tolerancia` (opcional): margen aceptado. Si no esta, se acepta un 1 %.

## 1ra etapa (cuestionario virtual)

Imita el cuestionario del Aula Virtual: no hay modo interactivo ni pistas, se contesta todo y se
corrige al final sobre 100 puntos. Tres formatos:

```html
<article class="preg" data-id="u5-c-..." data-etapa="1" data-formato="opcion|multiple|completar"
         data-origen="parcial|final">
  <div class="p-enunciado">   enunciado + p-fuente (en completar, con los huecos adentro)
  <ul class="p-opciones">     solo opcion y multiple
  <div class="p-explicacion"> se muestra en la revisión final
</article>
```

* **`opcion`** — "Seleccione una". Una sola `li` con `data-correcta`. Verdadero/Falso es una
  `opcion` con dos `li`: `Verdadero` y `Falso`. Vale poner "Ninguna opción es correcta", y a
  veces que sea la correcta. Puntaje: todo o nada.
* **`multiple`** — "Seleccione una o más de una". Una o varias `li` con `data-correcta`.
  Puntaje: cada correcta marcada suma su parte (1 / cantidad de correctas) y cada incorrecta
  marcada resta lo mismo; nunca baja de 0.
* **`completar`** — "Complete". Los huecos van dentro del enunciado. Puntaje: la parte
  proporcional de huecos bien.
  * Hueco numérico: `<span class="p-hueco" data-respuesta="0,20"></span>`. Como en el Aula
    Virtual, **se acepta solo con coma y 2 decimales** (`0,20`; `0,2` o `0.20` cuentan mal).
    Con `data-decimales="4"` pide 4. El enunciado dice la regla una vez, como el Aula Virtual:
    *"Ingrese el resultado utilizando coma como separador decimal y 2 cifras decimales.
    Ejemplo: 0,10"*.
  * Hueco desplegable: `<span class="p-hueco"><span data-correcta>cuantitativa discreta</span><span>cuantitativa continua</span><span>cualitativa</span></span>`.
    Solo texto: un desplegable no muestra fórmulas. Para elegir entre fórmulas, se listan con
    letra en el enunciado (`a)`, `b)`...) y el desplegable ofrece las letras.
