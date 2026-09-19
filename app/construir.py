# -*- coding: utf-8 -*-
"""
Junta todo el contenido en un solo archivo que lee index.html.

    python construir.py      (o el boton "Actualizar" de NewCampus)

Que junta en  generado/apuntes.js :
  contenido/<materia>/<unidad>/<pestania>/*.html            apuntes de cada unidad
  contenido/<materia>/evaluacion/parciales/<id>.html        parciales transcriptos
  contenido/<materia>/evaluacion/preguntas/<unidad>.html    banco de autoevaluacion

Cada apunte es una CARPETA con un archivo por bloque (la intro, cada ejercicio,
cada seccion de teoria). Se pegan en orden de nombre y se envuelven en el
<section class="pane"> que espera la pagina. Asi editar el ejercicio 12 abre
4 KB y no los 80 KB de la unidad entera; el nombre arranca con el numero de
ORDEN, que es lo unico que garantiza que queden como estaban.

Por que un .js y no leer los .html directamente:
  abriendo index.html con doble clic (file://) el navegador no deja leer otros
  archivos con fetch(), pero si deja cargar un <script>. El HTML viaja escapado
  con json.dumps, asi que las barras de las formulas (\\frac, \\leq) llegan intactas.

Para agregar una unidad o una materia nueva:
  - crear  contenido/<materia>/<unidad>/<teoria|practica>/00-intro.html  y un
    archivo por seccion o ejercicio (01-..., 02-...). Sin <section>: lo pone
    construir.py
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
NL = chr(10)


def revisar_formulas(texto):
    problemas = []
    for abre, cierra, etiqueta in (("\\(", "\\)", "en linea"), ("\\[", "\\]", "en bloque")):
        a, c = texto.count(abre), texto.count(cierra)
        if a != c:
            problemas.append("formulas %s: %d aperturas vs %d cierres" % (etiqueta, a, c))
    return problemas


def sangrar(trozo):
    """Los fragmentos se escriben al margen; adentro del <section> van a dos
    espacios, como estaba el HTML antes de partirlo."""
    return NL.join(("  " + l) if l.strip() else l for l in trozo.split(NL))


def armar_apunte(carpeta, vista):
    """Pega los fragmentos de una unidad y los envuelve en su <section>."""
    fragmentos = sorted(glob.glob(os.path.join(carpeta, "*.html")))
    if not fragmentos:
        return None, ["la carpeta esta vacia"]

    problemas = []
    partes = []
    for ruta in fragmentos:
        trozo = io.open(ruta, encoding="utf-8").read().strip()
        if not trozo:
            problemas.append("%s esta vacio" % os.path.basename(ruta))
            continue
        for p in revisar_formulas(trozo):
            problemas.append("%s: %s" % (os.path.basename(ruta), p))
        partes.append(sangrar(trozo))

    pestania = vista.rsplit("/", 1)[1]
    texto = ('<section class="pane" data-view="%s" data-tab-owner="%s">\n%s\n</section>'
             % (vista, pestania, "\n\n".join(partes)))
    return texto, problemas


def armar_parcial(carpeta):
    """Un parcial es una carpeta: meta.json con los datos de la tarjeta y un
    archivo por ejercicio."""
    problemas = []
    ruta_meta = os.path.join(carpeta, "meta.json")
    if not os.path.isfile(ruta_meta):
        return None, None, ["falta meta.json"]
    try:
        meta = json.loads(io.open(ruta_meta, encoding="utf-8").read())
    except ValueError as e:
        return None, None, ["meta.json no se entiende: %s" % e]

    for clave in ("titulo", "fecha", "detalle", "temas"):
        if not meta.get(clave):
            problemas.append("meta.json: falta %s" % clave)

    partes = []
    for ruta in sorted(glob.glob(os.path.join(carpeta, "*.html"))):
        trozo = io.open(ruta, encoding="utf-8").read().strip()
        for pr in revisar_formulas(trozo):
            problemas.append("%s: %s" % (os.path.basename(ruta), pr))
        partes.append(sangrar(trozo))
    if not partes:
        return None, None, problemas + ["la carpeta no tiene ejercicios"]

    atributos = "".join(NL + '  data-%s="%s"' % (k, meta[k])
                        for k in ("titulo", "fecha", "detalle", "temas") if meta.get(k))
    texto = ('<article class="parcial"%s>%s%s%s</article>'
             % (atributos, NL + NL, (NL + NL).join(partes), NL))
    return texto, meta, problemas


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

    # 1. Apuntes de cada unidad (una carpeta de fragmentos por pestania)
    apuntes = sorted(p for p in glob.glob(os.path.join(CONTENIDO, "*", "*", "*"))
                     if os.path.isdir(p) and os.path.basename(os.path.dirname(p)) != EVALUACION)
    if not apuntes:
        sys.exit("ERROR: no hay apuntes en %s" % CONTENIDO)

    for carpeta in apuntes:
        vista = os.path.relpath(carpeta, CONTENIDO).replace(os.sep, "/")
        texto, problemas = armar_apunte(carpeta, vista)
        if texto is None:
            hubo_problemas |= informar(vista, "", problemas)
            continue
        lineas.append("window.Apuntes.registrarPane(%s, %s);" % (json.dumps(vista), json.dumps(texto)))
        hubo_problemas |= informar(vista, texto, problemas)

    # 2. Evaluacion: parciales y bancos de preguntas de cada materia
    ids_vistos = set()

    # 2.a Parciales: una carpeta por parcial
    for carpeta in sorted(glob.glob(os.path.join(CONTENIDO, "*", EVALUACION, "parciales", "*"))):
        if not os.path.isdir(carpeta):
            continue
        rel = os.path.relpath(carpeta, CONTENIDO).replace(os.sep, "/")
        materia = rel.split("/")[0]
        clave = os.path.basename(carpeta)
        texto, meta, problemas = armar_parcial(carpeta)
        if texto is None:
            hubo_problemas |= informar(rel, "", problemas)
            continue
        lineas.append("window.Apuntes.registrarParcial(%s, %s, %s);"
                      % (json.dumps(materia), json.dumps(clave), json.dumps(texto)))
        hubo_problemas |= informar(rel, texto, problemas)

    # 2.b Bancos de preguntas
    for ruta in sorted(glob.glob(os.path.join(CONTENIDO, "*", EVALUACION, "*", "*.html"))):
        rel = os.path.relpath(ruta, CONTENIDO).replace(os.sep, "/")
        materia, _, clase, archivo = rel.split("/")
        clave = os.path.splitext(archivo)[0]
        texto = io.open(ruta, encoding="utf-8").read().strip()

        if clase == "preguntas":
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
