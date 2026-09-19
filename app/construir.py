# -*- coding: utf-8 -*-
"""
Junta todo el contenido en un solo archivo que lee index.html.

    python construir.py      (o el boton "Actualizar" de NewCampus)

Que deja en  generado/ :
  indice.js                  que hay y en que archivo esta (es lo unico
                             que carga index.html al arrancar)
  panes/<materia>-<unidad>-<pestania>.js
  examenes/<materia>-<id>.js
  preguntas/<materia>-<unidad>.js
                             cada uno se carga recien cuando se abre

De donde lo saca:
  contenido/materias.json                                   el menu lateral y el
                                                            material de catedra
  contenido/<materia>/<unidad>/<pestania>/*.html            apuntes de cada unidad
  contenido/<materia>/evaluacion/parciales/<id>/           parciales transcriptos
  contenido/<materia>/evaluacion/finales/<id>/              finales transcriptos
  contenido/<materia>/evaluacion/preguntas/<unidad>/*.html  banco de autoevaluacion,
                                                            un archivo por pregunta

Cada apunte es una CARPETA con un archivo por bloque (la intro, cada ejercicio,
cada seccion de teoria). Se pegan en orden de nombre y se envuelven en el
<section class="pane"> que espera la pagina. Asi editar el ejercicio 12 abre
4 KB y no los 80 KB de la unidad entera; el nombre arranca con el numero de
ORDEN, que es lo unico que garantiza que queden como estaban.

Por que un .js y no leer los .html directamente:
  abriendo index.html con doble clic (file://) el navegador no deja leer otros
  archivos con fetch(), pero si deja cargar un <script>. El HTML viaja escapado
  con json.dumps, asi que las barras de las formulas (\\frac, \\leq) llegan intactas.

Por que una pieza por unidad y no todo junto:
  con todo junto el navegador se traga TODAS las materias antes de mostrar
  la primera linea. Asi se carga solo lo que abris.

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
SALIDA = os.path.join(GENERADO, "indice.js")
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


def armar_examen(carpeta, tipo):
    """Un examen (parcial o final) es una carpeta: meta.json con los datos de la
    tarjeta y un archivo por ejercicio. El tipo sale de la carpeta que lo
    contiene, asi no hay que repetirlo en cada meta.json."""
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

    meta["tipo"] = tipo
    atributos = "".join(NL + '  data-%s="%s"' % (k, meta[k])
                        for k in ("tipo", "titulo", "fecha", "detalle", "temas") if meta.get(k))
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


CABECERA = "/* GENERADO por construir.py - NO EDITAR. El contenido se edita en contenido/ */"


def escribir(ruta, texto):
    """Se escribe aparte y se reemplaza de una vez: la pagina nunca lee un
    archivo a medias."""
    carpeta = os.path.dirname(ruta)
    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    temporal = ruta + ".tmp"
    io.open(temporal, "w", encoding="utf-8", newline=NL).write(texto)
    os.replace(temporal, ruta)


def limpiar_generado():
    """Se borra lo de la vuelta anterior: si se renombra o se saca una unidad,
    no queda el archivo viejo dando vueltas."""
    for patron in ("*.js", os.path.join("*", "*.js")):
        for ruta in glob.glob(os.path.join(GENERADO, patron)):
            os.remove(ruta)


def guardar_pieza(carpeta, clave, llamada):
    """Cada pieza va en su propio .js, que la pagina carga solo cuando hace
    falta. Devuelve la ruta relativa que se anota en el indice."""
    archivo = "%s/%s.js" % (carpeta, clave.replace("/", "-"))
    escribir(os.path.join(GENERADO, archivo.replace("/", os.sep)), CABECERA + NL + llamada + NL)
    return archivo


def armar_materias(panes):
    """El menu lateral y el material de catedra salen de contenido/materias.json.
    Una materia se muestra completa si tiene unidades con contenido; si no,
    aparece como 'pronto'. Una unidad sin contenido no se lista."""
    problemas = []
    ruta = os.path.join(CONTENIDO, "materias.json")
    if not os.path.isfile(ruta):
        return [], ["falta contenido/materias.json"]
    try:
        datos = json.loads(io.open(ruta, encoding="utf-8").read())
    except ValueError as e:
        return [], ["materias.json no se entiende: %s" % e]

    con_contenido = {}
    for vista in panes:
        materia, unidad, _ = vista.split("/")
        con_contenido.setdefault(materia, set()).add(unidad)

    salida = []
    listadas = set()
    for m in datos.get("materias", []):
        clave = m.get("clave")
        if not clave or not m.get("nombre"):
            problemas.append("hay una materia sin clave o sin nombre")
            continue
        listadas.add(clave)
        tiene = con_contenido.get(clave, set())

        unidades = []
        for u in m.get("unidades", []):
            if u.get("clave") not in tiene:
                continue          # todavia no tiene apuntes: no se muestra
            unidades.append({"clave": u["clave"],
                             "num": u.get("num", u["clave"]),
                             "nombre": u.get("nombre", "")})

        sin_listar = tiene - set(u["clave"] for u in unidades)
        for u in sorted(sin_listar):
            problemas.append("%s/%s tiene apuntes pero no esta en materias.json" % (clave, u))

        ficha = {"clave": clave, "nombre": m["nombre"],
                 "corto": m.get("corto", m["nombre"][:6]), "unidades": unidades}
        if m.get("pdf"):
            ficha["pdf"] = m["pdf"]
        if m.get("material"):
            ficha["material"] = m["material"]
        salida.append(ficha)

    for clave in sorted(set(con_contenido) - listadas):
        problemas.append("la materia %s tiene apuntes pero no esta en materias.json" % clave)

    return salida, problemas


def main():
    print("Armando NewCampus\n")
    hubo_problemas = False
    indice = {"panes": {}, "examenes": {}, "preguntas": {}}

    limpiar_generado()

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
        indice["panes"][vista] = guardar_pieza(
            "panes", vista,
            "window.Apuntes.registrarPane(%s, %s);" % (json.dumps(vista), json.dumps(texto)))
        hubo_problemas |= informar(vista, texto, problemas)

    # 2. Evaluacion: parciales y bancos de preguntas de cada materia
    ids_vistos = set()

    # 2.a Examenes: una carpeta por examen, adentro de parciales/ o de finales/.
    # Lo que muestra la tarjeta va en el indice, asi la lista se dibuja sin
    # cargar ningun examen.
    for carpeta_tipo, tipo in (("parciales", "parcial"), ("finales", "final")):
        for carpeta in sorted(glob.glob(os.path.join(CONTENIDO, "*", EVALUACION, carpeta_tipo, "*"))):
            if not os.path.isdir(carpeta):
                continue
            rel = os.path.relpath(carpeta, CONTENIDO).replace(os.sep, "/")
            materia = rel.split("/")[0]
            clave = os.path.basename(carpeta)
            texto, meta, problemas = armar_examen(carpeta, tipo)
            if texto is None:
                hubo_problemas |= informar(rel, "", problemas)
                continue

            ficha = {"id": clave, "archivo": guardar_pieza(
                "examenes", materia + "/" + clave,
                "window.Apuntes.registrarExamen(%s, %s, %s);"
                % (json.dumps(materia), json.dumps(clave), json.dumps(texto)))}
            ficha.update(meta)
            indice["examenes"].setdefault(materia, []).append(ficha)
            hubo_problemas |= informar(rel, texto, problemas)

    # 2.b Bancos de preguntas: una carpeta por unidad, un archivo por pregunta
    for carpeta in sorted(glob.glob(os.path.join(CONTENIDO, "*", EVALUACION, "preguntas", "*"))):
        if not os.path.isdir(carpeta):
            continue
        rel = os.path.relpath(carpeta, CONTENIDO).replace(os.sep, "/")
        materia = rel.split("/")[0]
        clave = os.path.basename(carpeta)

        partes = []
        problemas = []
        for ruta in sorted(glob.glob(os.path.join(carpeta, "*.html"))):
            pregunta = io.open(ruta, encoding="utf-8").read().strip()
            for pr in revisar_preguntas(pregunta, ids_vistos):
                problemas.append("%s: %s" % (os.path.basename(ruta), pr))
            partes.append(pregunta)
        if not partes:
            hubo_problemas |= informar(rel, "", ["la carpeta esta vacia"])
            continue
        texto = (NL + NL).join(partes)
        indice["preguntas"].setdefault(materia, {})[clave] = guardar_pieza(
            "preguntas", materia + "/" + clave,
            "window.Apuntes.registrarPreguntas(%s, %s, %s);"
            % (json.dumps(materia), json.dumps(clave), json.dumps(texto)))
        hubo_problemas |= informar(rel, texto, problemas)

    # 3. El indice: lo unico que carga index.html de entrada
    indice["materias"], problemas_menu = armar_materias(indice["panes"])
    if problemas_menu:
        hubo_problemas |= informar("menu (contenido/materias.json)", "", problemas_menu)
    else:
        print("  [OK     ] %-38s %7d materias" % ("menu (contenido/materias.json)",
                                                  len(indice["materias"])))
    indice["construido"] = time.strftime("%Y-%m-%d %H:%M:%S")
    escribir(SALIDA, CABECERA + NL +
             "window.Apuntes.registrarIndice(" + json.dumps(indice, indent=2) + ");" + NL)

    piezas = glob.glob(os.path.join(GENERADO, "*", "*.js"))
    pesado = max(piezas, key=os.path.getsize) if piezas else None
    print("\n  generado/indice.js: %d bytes  (lo unico que se carga al arrancar)"
          % os.path.getsize(SALIDA))
    print("  %d piezas que se cargan cuando se abren; la mas grande: %s con %d bytes"
          % (len(piezas), os.path.basename(pesado), os.path.getsize(pesado)))

    if hubo_problemas:
        print("\n  ATENCION: hay partes marcadas como REVISAR (ver arriba).")
        sys.exit(1)
    print("  Todo en orden.")


if __name__ == "__main__":
    main()
