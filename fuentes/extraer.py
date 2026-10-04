"""Pasa los PDFs de cátedra a texto, una sola vez, para leer menos.

Uso (desde la raíz del repo):
    python fuentes/extraer.py fuentes/pye "C:/Users/Fran/Desktop/SISTEMAS 3/PYE" "app/pdf/pye=app-pdf"

El primer argumento es la carpeta destino; los demás, carpetas con PDFs
(con "=subcarpeta" el resultado va a esa subcarpeta del destino). Se arma un
.md por PDF, con la misma ruta relativa, y un `<!-- página N -->` antes de
cada página. Las copias exactas (mismo contenido) se extraen una sola vez.

Si el .md ya existe, se conserva todo lo que está arriba de la página 1 (el
título y el índice "página → qué hay", que se escribe a mano) y solo se
regenera el texto. El PDF sigue siendo la fuente: esto es un atajo.

`<destino>/excluir.txt` (si existe): un nombre de PDF por renglón que no se
extrae nunca, p. ej. listas de alumnos u otros datos de personas: el repo es
público.
"""
import hashlib
import os
import sys
import unicodedata

from pypdf import PdfReader

MARCA = "<!-- página {} -->"


def normalizar(texto):
    # Las ecuaciones de Word usan letras itálicas matemáticas (𝑃, 𝑥, 𝟎):
    # se pasan a letras comunes para que se puedan leer y buscar.
    texto = "".join(unicodedata.normalize("NFKC", c) if 0x1D400 <= ord(c) <= 0x1D7FF else c
                    for c in texto)
    lineas, vacias = [], 0
    for linea in texto.splitlines():
        linea = linea.rstrip()
        vacias = vacias + 1 if not linea else 0
        if vacias <= 1:
            lineas.append(linea)
    return "\n".join(lineas).strip("\n")


def extraer(ruta):
    # pypdf sigue el orden de lectura: no mezcla las guías a dos columnas
    # (pdftotext -layout sí) y deja juntas las filas de las tablas simples.
    return [normalizar(p.extract_text() or "") for p in PdfReader(ruta).pages]


def encabezado_nuevo(nombre, fuente, paginas):
    filas = []
    for i, texto in enumerate(paginas, 1):
        nota = "⚠ ver el PDF (sin texto: escaneado o imagen)" if len(texto.strip()) < 20 else ""
        filas.append(f"| {i} | {nota} |")
    return "\n".join([
        f"# {nombre}",
        "",
        f"Fuente: `{fuente}` · {len(paginas)} página(s) · texto extraído con pypdf.",
        "Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.",
        "",
        "| Pág. | Qué hay |",
        "| :-- | :-- |",
        *filas,
        "",
    ])


def main():
    destino, origenes = sys.argv[1], sys.argv[2:]
    vistos = {}
    excluir = set()
    lista = os.path.join(destino, "excluir.txt")
    if os.path.exists(lista):
        with open(lista, encoding="utf-8") as f:
            excluir = {r.strip().lower() for r in f if r.strip() and not r.startswith("#")}
    for origen in origenes:
        origen, _, sub = origen.partition("=")
        for carpeta, _, archivos in os.walk(origen):
            for archivo in sorted(archivos):
                if not archivo.lower().endswith(".pdf") or archivo.lower() in excluir:
                    continue
                ruta = os.path.join(carpeta, archivo)
                rel = os.path.relpath(ruta, origen)
                with open(ruta, "rb") as f:
                    huella = hashlib.md5(f.read()).hexdigest()
                if huella in vistos:
                    print(f"copia: {rel}  =  {vistos[huella]}")
                    continue
                salida = os.path.join(destino, sub, os.path.splitext(rel)[0] + ".md")
                vistos[huella] = os.path.relpath(salida, destino)
                paginas = extraer(ruta)
                cabeza = None
                if os.path.exists(salida):
                    with open(salida, encoding="utf-8") as f:
                        viejo = f.read()
                    if MARCA.format(1) in viejo:
                        cabeza = viejo.split(MARCA.format(1))[0].rstrip("\n") + "\n"
                if cabeza is None:
                    fuente = os.path.abspath(ruta)
                    if not os.path.relpath(fuente).startswith(".."):
                        fuente = os.path.relpath(fuente)  # dentro del repo: ruta relativa
                    fuente = fuente.replace("\\", "/")
                    cabeza = encabezado_nuevo(os.path.splitext(archivo)[0], fuente, paginas)
                cuerpo = "\n\n".join(f"{MARCA.format(i)}\n\n{t}" for i, t in enumerate(paginas, 1))
                os.makedirs(os.path.dirname(salida), exist_ok=True)
                with open(salida, "w", encoding="utf-8", newline="\n") as f:
                    f.write(cabeza + "\n" + cuerpo + "\n")
                print(f"ok: {rel}  ({len(paginas)} pág.)")


if __name__ == "__main__":
    main()
