"""Pasa páginas de un PDF a PNG, para mirarlas cuando Read no puede abrir el PDF
(en esta PC falta pdftoppm).

Uso:  python fuentes/pagina.py "<ruta del PDF>" 3 7 8
Imprime la ruta de cada PNG (en la carpeta temporal); después, Read de esa ruta.
"""
import os
import sys
import tempfile

import pypdfium2 as pdfium


def main():
    ruta, paginas = sys.argv[1], [int(n) for n in sys.argv[2:]]
    pdf = pdfium.PdfDocument(ruta)
    base = os.path.splitext(os.path.basename(ruta))[0].replace(" ", "_")
    carpeta = os.path.join(tempfile.gettempdir(), "newcampus-paginas")
    os.makedirs(carpeta, exist_ok=True)
    for n in paginas:
        imagen = pdf[n - 1].render(scale=1.5).to_pil()
        salida = os.path.join(carpeta, f"{base}-p{n}.png")
        imagen.save(salida)
        print(salida)


if __name__ == "__main__":
    main()
