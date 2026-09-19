# -*- coding: utf-8 -*-
"""
Junta todo el contenido en un solo archivo que lee index.html.

    python construir.py      (o el boton "Actualizar" de NewCampus)

Que junta en  generado/apuntes.js :
  contenido/<materia>/<unidad>/<pestania>.html              apuntes de cada unidad
  contenido/<materia>/evaluacion/parciales/<id>.html        parciales transcriptos
  contenido/<materia>/evaluacion/preguntas/<unidad>.html    banco de autoevaluacion

Por que un .js y no leer los .html directamente:
  abriendo index.html con doble clic (file://) el navegador no deja leer otros
  archivos con fetch(), pero si deja cargar un <script>. El HTML viaja escapado
  con json.dumps, asi que las barras de las formulas (\\frac, \\leq) llegan intactas.

Para agregar una unidad o una materia nueva:
  - crear  contenido/<materia>/<unidad>/<teoria|practica>.html  con un
    <section class="pane" data-view="materia/unidad/pestania"> ... </section>
  - agregar la entrada en el menu lateral de  index.html
  - volver a correr  python construir.py
"""

import io
import os
import re
import sys
import json
import glob
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
CONTENIDO = os.path.join(AQUI, "contenido")
GENERADO = os.path.join(AQUI, "generado")
SALIDA = os.path.join(GENERADO, "apuntes.js")
EVALUACION = "evaluacion"


def revisar_formulas(texto):
    problemas = []
    for abre, cierra, etiqueta in (("\\(", "\\)", "en linea"), ("\\[", "\\]", "en bloque")):
        a, c = texto.count(abre), texto.count(cierra)
        if a != c:
            problemas.append("formulas %s: %d aperturas vs %d cierres" % (etiqueta, a, c))
    return problemas


def revisar_apunte(texto, vista):
    problemas = revisar_formulas(texto)
    esperado = 'data-view="%s"' % vista
    if esperado not in texto:
        problemas.append('la carpeta pide %s y no aparece en el <section class="pane">' % esperado)
    return problemas


def revisar_preguntas(texto, ids_vistos):
    """Cada <article class="preg"> necesita un data-id unico y un data-tipo valido."""
    problemas = revisar_formulas(texto)
    sin_comentarios = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
    for m in re.finditer(r'<article class="preg"([^>]*)>', sin_comentarios):
        pid = re.search(r'data-id="([^"]+)"', m.group(1))
        tipo = re.search(r'data-tipo="([^"]+)"', m.group(1))
        if not pid:
            problemas.append("hay una pregunta sin data-id")
            continue
        if pid.group(1) in ids_vistos:
            problemas.append("data-id repetido: %s" % pid.group(1))
        ids_vistos.add(pid.group(1))
        if not tipo or tipo.group(1) not in ("teoria", "practica"):
            problemas.append("%s: data-tipo tiene que ser teoria o practica" % pid.group(1))
    return problemas


def informar(nombre, texto, problemas):
    print("  [%-7s] %-38s %7d bytes" % ("OK" if not problemas else "REVISAR", nombre, len(texto)))
    for p in problemas:
        print("              %s" % p)
    return bool(problemas)


def main():
    lineas = ["/* GENERADO por construir.py - NO EDITAR. El contenido se edita en contenido/ */"]
    hubo_problemas = False

    print("Armando NewCampus\n")

    # 1. Apuntes de cada unidad
    apuntes = sorted(p for p in glob.glob(os.path.join(CONTENIDO, "*", "*", "*.html"))
                     if os.path.basename(os.path.dirname(p)) != EVALUACION)
    if not apuntes:
        sys.exit("ERROR: no hay apuntes en %s" % CONTENIDO)

    for ruta in apuntes:
        vista = os.path.relpath(ruta, CONTENIDO)[:-len(".html")].replace(os.sep, "/")
        texto = io.open(ruta, encoding="utf-8").read().strip()
        lineas.append("window.Apuntes.registrarPane(%s, %s);" % (json.dumps(vista), json.dumps(texto)))
        hubo_problemas |= informar(vista, texto, revisar_apunte(texto, vista))

    # 2. Evaluacion: parciales y bancos de preguntas de cada materia
    ids_vistos = set()
    for ruta in sorted(glob.glob(os.path.join(CONTENIDO, "*", EVALUACION, "*", "*.html"))):
        rel = os.path.relpath(ruta, CONTENIDO).replace(os.sep, "/")
        materia, _, clase, archivo = rel.split("/")
        clave = os.path.splitext(archivo)[0]
        texto = io.open(ruta, encoding="utf-8").read().strip()

        if clase == "parciales":
            funcion, problemas = "registrarParcial", revisar_formulas(texto)
        elif clase == "preguntas":
            funcion, problemas = "registrarPreguntas", revisar_preguntas(texto, ids_vistos)
        else:
            print("  [SALTEADO] %s  (la carpeta tiene que ser parciales o preguntas)" % rel)
            hubo_problemas = True
            continue

        lineas.append("window.Apuntes.%s(%s, %s, %s);"
                      % (funcion, json.dumps(materia), json.dumps(clave), json.dumps(texto)))
        hubo_problemas |= informar(rel[:-len(".html")], texto, problemas)

    # Marca de la construccion: el boton "Actualizar" espera a que cambie para recargar.
    lineas.append("window.Apuntes.construido = %s;" % json.dumps(time.strftime("%Y-%m-%d %H:%M:%S")))

    if not os.path.isdir(GENERADO):
        os.makedirs(GENERADO)

    # Se escribe aparte y se reemplaza de una vez: la pagina nunca lee un archivo a medias.
    temporal = SALIDA + ".tmp"
    io.open(temporal, "w", encoding="utf-8").write("\n".join(lineas) + "\n")
    os.replace(temporal, SALIDA)

    print("\n  generado/apuntes.js: %d bytes" % os.path.getsize(SALIDA))

    if hubo_problemas:
        print("\n  ATENCION: hay partes marcadas como REVISAR (ver arriba).")
        sys.exit(1)
    print("  Todo en orden.")


if __name__ == "__main__":
    main()
