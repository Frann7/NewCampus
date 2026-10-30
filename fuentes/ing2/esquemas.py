"""Dibuja los esquemas de Ing. II que no son diagramas de clases y los mete en los fragmentos.

Uso (desde la raíz del repo):
    python fuentes/ing2/esquemas.py

En cada fragmento de `app/contenido/ing2`, el contenido de
`<div class="pd-grafico esq" data-g="nombre">...</div>` se reemplaza por el SVG de
`D["nombre"]`. Los estilos (`.esq ...`) están en `app/assets/estilos.css`.

- `ciclo-metrica`: el ciclo de vida de las métricas (SWEBOK), seis fases en un anillo.
- `definir-procesos` y `elementos-proceso`: cómo se definen los procesos y sus tres elementos.
- `cmmi-diagnostico`: el método de las cuatro preguntas para ubicar el nivel.
- `grafo-par` y `grafo-tarifa`: grafos de control para la complejidad ciclomática.
- `git-comandos` y `git-ramas`: adónde mueve cada comando, y una rama con su merge.
- `vcs-svn` y `vcs-git`: dónde están el servidor, los repositorios y las copias de trabajo
  en un control de versiones centralizado (SVN) y en uno distribuido (Git).
"""
import glob
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENIDO = os.path.join(RAIZ, "app", "contenido", "ing2")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def flechas(nombre):
    """La punta de flecha, con un id propio para que dos esquemas en la misma página no choquen."""
    return (f'<defs><marker id="pta-{nombre}" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
            f'<path d="M1 1L9 5L1 9z" class="punta"/></marker></defs>')


def texto(x, y, s, clase):
    return f'<text class="{clase}" x="{x}" y="{y}">{esc(s)}</text>'


def svg(nombre, ancho, alto, alt, cuerpo):
    return (f'\n    <svg viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}" role="img" '
            f'aria-label="{esc(alt)}">{flechas(nombre)}{cuerpo}</svg>\n  ')


# ---------- Seis pasos en dos filas (ciclo de vida, cómo se definen los procesos) ----------

FASES = [
    ("1. Planificación", "de la medición", "objetivos y qué medir"),
    ("2. Definición", "de las métricas", "fórmula, unidad y criterio"),
    ("3. Recolección", "de datos", "capturar datos válidos"),
    ("4. Análisis e", "interpretación", "comparar con los límites"),
    ("5. Comunicación y", "uso de resultados", "informar y decidir acciones"),
    ("6. Revisión y", "retroalimentación", "¿la métrica sigue sirviendo?"),
]

PASOS_PROCESO = [
    ("1. Analizar la", "situación actual", "cómo se hace hoy (AS-IS)"),
    ("2. Establecer los", "objetivos de mejora", "qué se quiere lograr (TO-BE)"),
    ("3. Comprender", "la organización", "gente, estructura, cultura"),
    ("4. Diseñar el plan", "de proyecto", "para definir los procesos"),
    ("5. Implementar", "el proyecto", "definir, modelar y validar"),
    ("6. Monitorear y", "evaluar", "comparar con los objetivos"),
]


def seis_pasos(nombre, pasos, ciclo, centro, alt):
    """Arriba los pasos 1, 2 y 3 de izquierda a derecha; abajo 4, 5 y 6 de derecha a izquierda.
    Con `ciclo`, una flecha del 6 al 1 dice que vuelve a empezar."""
    w, h, gap, fila2 = 210, 92, 45, 180
    pos = [(0, 0), (w + gap, 0), (2 * (w + gap), 0),
           (2 * (w + gap), fila2), (w + gap, fila2), (0, fila2)]
    o = ""
    for (t1, t2, d), (x, y) in zip(pasos, pos):
        cx = x + w / 2
        o += (f'<g class="fase"><rect class="caja" x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>'
              + texto(cx, y + 26, t1, "tit") + texto(cx, y + 45, t2, "tit")
              + texto(cx, y + 71, d, "desc") + "</g>")
    m = f'marker-end="url(#pta-{nombre})"'
    yc = h / 2
    for x in (w, 2 * w + gap):                      # 1 -> 2 y 2 -> 3
        o += f'<line class="flecha" x1="{x + 4}" y1="{yc}" x2="{x + gap - 4}" y2="{yc}" {m}/>'
    xd = 2 * (w + gap) + w / 2                       # 3 -> 4
    o += f'<line class="flecha" x1="{xd}" y1="{h + 4}" x2="{xd}" y2="{fila2 - 4}" {m}/>'
    for x in (2 * (w + gap), w + gap):              # 4 -> 5 y 5 -> 6
        o += f'<line class="flecha" x1="{x - 4}" y1="{fila2 + yc}" x2="{x - gap + 4}" y2="{fila2 + yc}" {m}/>'
    if ciclo:                                        # 6 -> 1: vuelve a empezar
        xi = w / 2
        o += f'<line class="flecha vuelta" x1="{xi}" y1="{fila2 - 4}" x2="{xi}" y2="{h + 4}" {m}/>'
        o += texto(xi + 12, (h + fila2) / 2 + 4, "vuelve a empezar", "nota izq")
    o += texto(w + gap + w / 2, (h + fila2) / 2 + 4, centro, "centro")
    return svg(nombre, 3 * w + 2 * gap, fila2 + h + 2, alt, o)


# ---------- SVN y Git ----------

def caja(x, y, w, h, clase, tit=None):
    o = f'<rect class="{clase}" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>'
    if tit:
        o += texto(x + w / 2, y + 20, tit, "tit")
    return o


def interior(x, y, w, h, clase, t1, t2):
    return (caja(x, y, w, h, clase) + texto(x + w / 2, y + h / 2 - 3, t1, "en")
            + texto(x + w / 2, y + h / 2 + 13, t2, "en2"))


def vcs(nombre, distribuido):
    wd, gap = 200, 45
    xs = [0, wd + gap, 2 * (wd + gap)]
    ancho = 3 * wd + 2 * gap
    ws, xs0 = 300, (ancho - 300) / 2
    if distribuido:
        o = caja(xs0, 0, ws, 82, "servidor", "Servidor remoto (GitHub)")
        o += interior(xs0 + 30, 30, ws - 60, 42, "repo", "Repositorio remoto", "lo que comparte el equipo")
        yd, hd = 160, 150
    else:
        o = caja(xs0, 0, ws, 82, "servidor", "Servidor central")
        o += interior(xs0 + 30, 30, ws - 60, 42, "repo", "Repositorio único", "con todo el historial")
        yd, hd = 160, 92
    m = f'marker-end="url(#pta-{nombre})" marker-start="url(#pta-{nombre})"'
    for i, x in enumerate(xs):
        o += caja(x, yd, wd, hd, "dev", f"Desarrollador {i + 1}")
        if distribuido:
            o += interior(x + 15, yd + 32, wd - 30, 46, "repo", "Repositorio local", "historial completo")
            o += interior(x + 15, yd + 92, wd - 30, 46, "copia", "Copia de trabajo", "los archivos que edita")
        else:
            o += interior(x + 15, yd + 32, wd - 30, 46, "copia", "Copia de trabajo", "sin el historial")
        # cada desarrollador se conecta con el servidor
        xa = xs0 + ws / 2 + (i - 1) * 90
        o += f'<line class="flecha" x1="{xa}" y1="86" x2="{x + wd / 2}" y2="{yd - 4}" {m}/>'
    rot = ("push sube los commits · pull los baja" if distribuido
           else "commit sube los cambios · update los baja")
    o += texto(ancho / 2, yd + hd + 24, rot, "centro")
    alt = ("Git: servidor remoto y, en cada desarrollador, repositorio local y copia de trabajo"
           if distribuido else "SVN: un servidor central con el repositorio y copias de trabajo en cada desarrollador")
    return svg(nombre, ancho, yd + hd + 32, alt, o)


# ---------- Los tres elementos de un proceso ----------

def elementos_proceso():
    nombre = "elementos-proceso"
    W = 600
    cajas = [  # (x, y, w, título, descripción)
        ((W - 220) / 2, 0, 220, "Personas", "ejecutan y mejoran el proceso"),
        (0, 196, 230, "Métodos y procedimientos", "cómo se hacen las actividades"),
        (W - 230, 196, 230, "Herramientas", "soportan, miden y controlan"),
    ]
    cx, cy, rx, ry = W / 2, 150, 70, 30
    o = ""
    for x, y, w, t, d in cajas:
        o += (f'<g class="fase"><rect class="caja" x="{x}" y="{y}" width="{w}" height="62" rx="10"/>'
              + texto(x + w / 2, y + 26, t, "tit") + texto(x + w / 2, y + 47, d, "desc") + "</g>")
    # líneas del centro a cada elemento
    o += f'<line class="flecha" x1="{cx}" y1="{cy - ry}" x2="{cx}" y2="62"/>'
    o += f'<line class="flecha" x1="{cx - rx + 8}" y1="{cy + 16}" x2="{170}" y2="196"/>'
    o += f'<line class="flecha" x1="{cx + rx - 8}" y1="{cy + 16}" x2="{W - 170}" y2="196"/>'
    o += f'<ellipse class="centro-el" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/>'
    o += texto(cx, cy + 5, "Proceso", "tit")
    o += texto(cx, 290, "El proceso integra los tres: si falla uno, la mejora no funciona", "centro")
    return svg(nombre, W, 298, "Los tres elementos de un proceso: personas, métodos y procedimientos, herramientas", o)


# ---------- CMMI: el método de las cuatro preguntas ----------

PREGUNTAS = [
    ("1. ¿Los proyectos se planifican y se siguen?", "Nivel 1 · Inicial", "n1"),
    ("2. ¿Hay un proceso común para todos los equipos?", "Nivel 2 · Gestionado", "n2"),
    ("3. ¿Se miden los procesos para controlar y predecir?", "Nivel 3 · Definido", "n3"),
    ("4. ¿Se usan los datos para mejorar e innovar?", "Nivel 4 · Cuantitativamente gestionado", "n4"),
]


def cmmi_diagnostico():
    nombre = "cmmi-diagnostico"
    wq, hq, paso, xn, wn = 390, 50, 90, 450, 290
    m = f'marker-end="url(#pta-{nombre})"'
    o = ""
    for i, (q, nivel, k) in enumerate(PREGUNTAS):
        y = i * paso
        o += (f'<rect class="pregunta" x="0" y="{y}" width="{wq}" height="{hq}" rx="8"/>'
              + texto(wq / 2, y + 30, q, "en"))
        o += f'<line class="flecha" x1="{wq + 4}" y1="{y + hq / 2}" x2="{xn - 4}" y2="{y + hq / 2}" {m}/>'
        o += texto((wq + xn) / 2, y + hq / 2 - 7, "no", "rot")
        o += (f'<rect class="nivel {k}" x="{xn}" y="{y + 5}" width="{wn}" height="{hq - 10}" rx="8"/>'
              + texto(xn + wn / 2, y + 30, nivel, "en"))
        ya = y + hq
        o += f'<line class="flecha" x1="{wq / 2}" y1="{ya + 4}" x2="{wq / 2}" y2="{ya + paso - hq - 4}" {m}/>'
        o += texto(wq / 2 + 12, ya + (paso - hq) / 2 + 4, "sí", "rot izq")
    y5 = 4 * paso
    o += (f'<rect class="nivel n5" x="0" y="{y5}" width="{wq}" height="{hq - 10}" rx="8"/>'
          + texto(wq / 2, y5 + 25, "Nivel 5 · En optimización continua", "en"))
    o += texto(xn + wn / 2, y5 + 25, "El nivel es el del primer «no»", "centro")
    return svg(nombre, xn + wn, y5 + hq, "Diagnóstico del nivel de CMMI con cuatro preguntas en orden", o)


# ---------- Complejidad ciclomática: el grafo del par o impar ----------

def grafo_par():
    nombre = "grafo-par"
    m = f'marker-end="url(#pta-{nombre})"'
    nodos = {  # id: (x, y, w, texto)
        "q": (210, 0, 140, "¿es par?"),
        "p": (40, 100, 140, "decir par"),
        "i": (380, 100, 140, "decir impar"),
        "f": (230, 200, 100, "fin"),
    }
    o = ""
    for x, y, w, t in nodos.values():
        o += f'<rect class="nodo" x="{x}" y="{y}" width="{w}" height="40" rx="20"/>' + texto(x + w / 2, y + 25, t, "en")
    o += f'<line class="flecha" x1="245" y1="42" x2="125" y2="96" {m}/>'
    o += f'<line class="flecha" x1="315" y1="42" x2="435" y2="96" {m}/>'
    o += f'<line class="flecha" x1="125" y1="142" x2="250" y2="196" {m}/>'
    o += f'<line class="flecha" x1="435" y1="142" x2="310" y2="196" {m}/>'
    o += texto(165, 62, "sí", "rot") + texto(395, 62, "no", "rot")
    o += texto(280, 120, "N = 4 nodos · E = 4 aristas", "centro")
    return svg(nombre, 560, 242, "Grafo de control de una función con un if: cuatro nodos y cuatro aristas", o)


def grafo_tarifa():
    nombre = "grafo-tarifa"
    m = f'marker-end="url(#pta-{nombre})"'
    nodos = [(200, 0, 170, "¿más de 20 kg?"), (20, 90, 150, "tarifa pesada"), (330, 90, 170, "¿más de 5 kg?"),
             (230, 180, 140, "tarifa media"), (430, 180, 140, "tarifa común"), (180, 280, 180, "mostrar el precio")]
    o = ""
    for x, y, w, t in nodos:
        o += f'<rect class="nodo" x="{x}" y="{y}" width="{w}" height="40" rx="20"/>' + texto(x + w / 2, y + 25, t, "en")
    for x1, y1, x2, y2 in [(255, 42, 95, 86), (315, 42, 415, 86), (395, 132, 300, 176), (435, 132, 500, 176),
                           (95, 132, 220, 276), (300, 222, 270, 276), (500, 222, 320, 276)]:
        o += f'<line class="flecha" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {m}/>'
    o += texto(165, 60, "sí", "rot") + texto(375, 60, "no", "rot")
    o += texto(330, 150, "sí", "rot") + texto(485, 150, "no", "rot")
    o += texto(270, 345, "N = 6 nodos · E = 7 aristas", "centro")
    return svg(nombre, 590, 352, "Grafo de control de la función de la tarifa: seis nodos y siete aristas", o)


# ---------- Git: adónde mueve cada comando ----------

LUGARES = [
    ("Directorio", "de trabajo", "mal"),
    ("Área de", "preparación", "ojo"),
    ("Repositorio", "local", "ok"),
    ("Repositorio", "remoto (origin)", "rem"),
]
COMANDOS = [(0, 1, "git add"), (1, 2, "git commit"), (2, 3, "git push"), (3, 0, "git pull")]


def git_comandos():
    nombre = "git-comandos"
    w, gap, hc = 150, 40, 56
    m = f'marker-end="url(#pta-{nombre})"'
    xs = [i * (w + gap) for i in range(4)]
    o = ""
    for (t1, t2, k), x in zip(LUGARES, xs):
        o += (f'<rect class="lugar {k}" x="{x}" y="0" width="{w}" height="{hc}" rx="10"/>'
              + texto(x + w / 2, 24, t1, "en") + texto(x + w / 2, 42, t2, "en"))
        o += f'<line class="guia" x1="{x + w / 2}" y1="{hc}" x2="{x + w / 2}" y2="{hc + 4 * 34 + 10}"/>'
    for j, (a, b, c) in enumerate(COMANDOS):
        y = hc + 34 * (j + 1)
        xa, xb = xs[a] + w / 2, xs[b] + w / 2
        d = 1 if xb > xa else -1
        o += f'<line class="flecha" x1="{xa + 4 * d}" y1="{y}" x2="{xb - 4 * d}" y2="{y}" {m}/>'
        o += texto((xa + xb) / 2, y - 6, c, "cmd")
    return svg(nombre, 4 * w + 3 * gap, hc + 4 * 34 + 14, "Adónde mueve los cambios cada comando de Git", o)


# ---------- Git: una rama y su merge ----------

def git_ramas():
    nombre = "git-ramas"
    m = f'marker-end="url(#pta-{nombre})"'
    yM, yF, r = 40, 130, 14
    nodos = {"C1": (90, yM), "C2": (190, yM), "C3": (340, yM), "F1": (270, yF), "F2": (380, yF), "M": (480, yM)}
    aristas = [("C1", "C2"), ("C2", "C3"), ("C3", "M"), ("C2", "F1"), ("F1", "F2"), ("F2", "M")]
    o = ""
    for a, b in aristas:
        (x1, y1), (x2, y2) = nodos[a], nodos[b]
        dx, dy = x2 - x1, y2 - y1
        n = (dx * dx + dy * dy) ** 0.5
        ux, uy = dx / n, dy / n
        clase = "flecha rama" if "F" in a + b else "flecha"
        o += (f'<line class="{clase}" x1="{x1 + ux * r:.1f}" y1="{y1 + uy * r:.1f}" '
              f'x2="{x2 - ux * (r + 3):.1f}" y2="{y2 - uy * (r + 3):.1f}" {m}/>')
    for k, (x, y) in nodos.items():
        clase = "commit rama" if k.startswith("F") else ("commit merge" if k == "M" else "commit")
        o += f'<circle class="{clase}" cx="{x}" cy="{y}" r="{r}"/>' + texto(x, y + 4, k, "cid")
    o += texto(20, yM + 5, "main", "rama-n izq")
    o += texto(250, yF + 5, "funcion", "rama-n der")
    o += texto(125, 100, "git checkout -b funcion", "cmd")
    o += texto(445, 100, "git merge funcion", "cmd izq")
    return svg(nombre, 600, 160, "Una rama que sale de main, suma dos commits y vuelve con un merge", o)


D = {
    "ciclo-metrica": seis_pasos("ciclo-metrica", FASES, True, "Un ciclo continuo: se repite siempre",
                                "Ciclo de vida de las métricas: seis fases en un ciclo"),
    "definir-procesos": seis_pasos("definir-procesos", PASOS_PROCESO, False, "De cómo está (AS-IS) a cómo va a ser (TO-BE)",
                                   "Los seis pasos para definir los procesos"),
    "elementos-proceso": elementos_proceso(),
    "cmmi-diagnostico": cmmi_diagnostico(),
    "grafo-par": grafo_par(),
    "grafo-tarifa": grafo_tarifa(),
    "git-comandos": git_comandos(),
    "git-ramas": git_ramas(),
    "vcs-svn": vcs("vcs-svn", False),
    "vcs-git": vcs("vcs-git", True),
}

PATRON = re.compile(r'(<div class="pd-grafico esq" data-g="([\w-]+)">)(.*?)(</div>)', re.S)


def main():
    usados = set()
    for ruta in glob.glob(os.path.join(CONTENIDO, "**", "*.html"), recursive=True):
        s = open(ruta, encoding="utf-8").read()

        def poner(mt):
            usados.add(mt.group(2))
            if mt.group(2) not in D:
                raise SystemExit(f"{ruta}: no hay esquema '{mt.group(2)}'")
            return mt.group(1) + D[mt.group(2)] + mt.group(4)

        nuevo = PATRON.sub(poner, s)
        if nuevo != s:
            open(ruta, "w", encoding="utf-8", newline="\n").write(nuevo)
            print("  " + os.path.relpath(ruta, RAIZ))
    for falta in sorted(set(D) - usados):
        print(f"  (sin usar: {falta})")


if __name__ == "__main__":
    main()
