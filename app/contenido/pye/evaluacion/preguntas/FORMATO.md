# Formato del banco de preguntas

Cada pregunta es un archivo de `preguntas/<unidad>/` y su nombre es el `data-id`.
`construir.py` los pega en orden de nombre.

```htmlBANCO DE PREGUNTAS - Unidad 4
  El nombre del archivo (u4) es la unidad. Formato de cada pregunta:

  <article class="preg" data-id="unico" data-tipo="teoria|practica">
    <div class="p-enunciado">   enunciado (en practica: el ejercicio completo)
    <div class="p-pregunta">    solo practica: lo que se pregunta en modo NORMAL
    <ul class="p-opciones">     opciones; la correcta lleva data-correcta
    <div class="p-pista">       pista de la lamparita (modo INTERACTIVO)
    <div class="p-explicacion"> se muestra al corregir y en el informe
    <ol class="p-pasos">        solo practica: los pasos del modo INTERACTIVO
      <li data-nivel="..." data-respuesta="0,88">   paso con respuesta numerica
      <li data-nivel="...">  + <ul class="p-opciones">   paso con opciones

  data-nivel = el nivel MAS AVANZADO en el que todavia aparece el paso:
    avanzado     -> aparece en los tres niveles (partes principales)
    medio        -> aparece en medio y principiante
    principiante -> aparece solo en principiante (las cuentas mas chicas)
  data-tolerancia (opcional): margen aceptado. Si no esta, se acepta un 1 %.
```
