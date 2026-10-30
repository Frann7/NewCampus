"""Dibuja los esquemas de Ing. II que no son diagramas de clases y los mete en los fragmentos.

Uso (desde la raíz del repo):
    python fuentes/ing2/esquemas.py

En cada fragmento de `app/contenido/ing2`, el contenido de
`<div class="pd-grafico esq" data-g="nombre">...</div>` se reemplaza por el SVG de
`D["nombre"]` y, debajo, el rótulo de `ORIGEN["nombre"]`. Los estilos (`.esq ...`) están en
`app/assets/estilos.css`.

Hay dos clases de esquemas, y el rótulo dice cuál es cada uno (pedido de Fran, 29/10/2026):
- **Del apunte:** los diagramas que traen los apuntes de la cátedra, redibujados iguales (las
  mismas cajas, los mismos textos, las mismas flechas). El rótulo dice el apunte y la página
  impresa. Si el original está en inglés, el texto se deja y se agrega la traducción.
- **Propios:** los que no están en ningún apunte. El rótulo empieza con "No está en el apunte".

Del apunte: `cmmi-escalera`, `cmmi-progreso`, `elementos-proceso` (Calidad de software);
`metrica-ficha`, `metricas-contexto` (Métricas); `versionado`, `git-ramas`, `vcs-svn-git`,
`git-deltas`, `git-snapshots`, `git-tres-secciones` (Gestión de cambios).
Propios: `ciclo-metrica`, `definir-procesos`, `cmmi-diagnostico`, `grafo-par`, `grafo-tarifa`,
`git-comandos`.
"""
import glob
import math
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
    return f'<text class="{clase}" x="{x:g}" y="{y:g}">{esc(s)}</text>'


def lineas(x, y, renglones, clase, alto=17):
    """Varios renglones centrados en x; y es el del primero."""
    return "".join(texto(x, y + i * alto, r, clase) for i, r in enumerate(renglones))


def svg(nombre, ancho, alto, alt, cuerpo):
    return (f'\n    <svg viewBox="0 0 {ancho:g} {alto:g}" width="{ancho:g}" height="{alto:g}" role="img" '
            f'aria-label="{esc(alt)}">{flechas(nombre)}{cuerpo}</svg>')


def punta(nombre):
    return f'marker-end="url(#pta-{nombre})"'


# =====================================================================================
# DEL APUNTE: Calidad de software
# =====================================================================================

ESCALONES = [  # pág. 21, de abajo hacia arriba
    ("Pocos o ningún proceso definido,", "punto de arranque normal."),
    ("Procesos definidos, con sus recursos", "humanos y herramientas."),
    ("Procesos estandarizados, que todo", "el personal aplica y repite."),
    ("Medición de los procesos y observación", "del estatus de las operaciones."),
    ("Optimización de procesos y predicción", "con base en mediciones."),
]


def cmmi_escalera():
    nombre = "cmmi-escalera"
    W, h, gap, paso_x = 600, 58, 6, 44
    o = ""
    for i, (t1, t2) in enumerate(ESCALONES, 1):
        y = (5 - i) * (h + gap)
        x0 = 30 + (i - 1) * paso_x
        o += f'<rect class="nivel n{i}" x="{x0}" y="{y}" width="{W - x0}" height="{h}" rx="8"/>'
        o += f'<rect class="numniv n{i}" x="{W - 52}" y="{y}" width="52" height="{h}" rx="8"/>'
        o += texto(W - 26, y + h / 2 + 9, str(i), "num-t")
        o += texto(W - 64, y + 25, t1, "en der") + texto(W - 64, y + 43, t2, "en der")
        if i > 1:
            xa = x0 - 18
            o += (f'<path class="flecha" d="M{xa} {y + h - 2} L{xa} {y + 16} L{xa + 12} {y + 16}" '
                  f'fill="none" {punta(nombre)}/>')
    return svg(nombre, W, 5 * (h + gap) - gap, "Pirámide de los cinco niveles de madurez de CMMI", o)


PROGRESO = [
    ("1. Inicial",), ("2. Gestionado",), ("3. Definido",),
    ("4.Cuantitativa", "mente", "gestionado"), ("5.", "Optimización", "continua"),
]


def cmmi_progreso():
    nombre = "cmmi-progreso"
    o = ('<polygon class="flechon" points="20,42 650,42 650,6 738,76 650,146 650,110 20,110"/>')
    w, h = 118, 70
    for i, renglones in enumerate(PROGRESO):
        x = 8 + i * 130
        o += f'<rect class="nivel n{i + 1}" x="{x}" y="41" width="{w}" height="{h}" rx="10"/>'
        y0 = 76 + 5 - (len(renglones) - 1) * 8.5
        o += lineas(x + w / 2, y0, renglones, "en")
    return svg(nombre, 740, 152, "Diagrama de progreso lineal: los cinco niveles de CMMI como etapas", o)


def elementos_proceso():
    nombre = "elementos-proceso"
    cx, cy, r = 300, 200, 85
    o = f'<circle class="circulo" cx="{cx}" cy="{cy}" r="{r}"/>'
    angulos = [-90, 30, 150]                 # los tres puntos sobre el círculo
    for a, b in zip(angulos, angulos[1:] + [angulos[0] + 360]):
        a1, b1 = math.radians(a + 13), math.radians(b - 13)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(b1), cy + r * math.sin(b1)
        o += (f'<path class="flecha" d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" '
              f'fill="none" {punta(nombre)}/>')
    for a in angulos:
        o += f'<circle class="punto" cx="{cx + r * math.cos(math.radians(a)):.1f}" cy="{cy + r * math.sin(math.radians(a)):.1f}" r="11"/>'
    o += texto(cx, cy + 6, "PROCESS", "tit") + texto(cx, cy + 24, "(proceso)", "desc")
    # arriba, los procedimientos: un flujo A, B, C, D
    o += '<rect class="punteado" x="232" y="8" width="150" height="80" rx="4"/>'
    letras = {"A": (250, 52), "B": (300, 22), "C": (300, 70), "D": (360, 46)}
    for k, (x, y) in letras.items():
        o += texto(x, y + 5, k, "cid")
    for a, b in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("B", "C")]:
        (x1, y1), (x2, y2) = letras[a], letras[b]
        dx, dy = x2 - x1, y2 - y1
        n = math.hypot(dx, dy)
        o += (f'<line class="flecha" x1="{x1 + dx / n * 9:.1f}" y1="{y1 + dy / n * 9:.1f}" '
              f'x2="{x2 - dx / n * 11:.1f}" y2="{y2 - dy / n * 11:.1f}" {punta(nombre)}/>')
    o += f'<line class="flecha" x1="300" y1="92" x2="300" y2="{cy - r - 14}" {punta(nombre)}/>'
    o += lineas(392, 40, ["Procedures and methods", "(métodos y procedimientos)"], "desc izq")
    # abajo a la izquierda, las personas; a la derecha, las herramientas
    for k in range(3):
        x = 118 + k * 30
        o += f'<circle class="icono" cx="{x}" cy="262" r="8"/><rect class="icono" x="{x - 10}" y="273" width="20" height="30" rx="3"/>'
    o += lineas(150, 326, ["People with skills, training,", "and motivation", "(personas capacitadas y motivadas)"], "desc")
    for k in range(4):
        x = 400 + k * 22
        o += f'<rect class="icono" x="{x}" y="258" width="16" height="7"/><rect class="icono" x="{x + 5}" y="265" width="6" height="38"/>'
    o += lineas(444, 326, ["Tools and equipment", "(herramientas y equipos)"], "desc")
    return svg(nombre, 600, 368, "Los procesos integran las tres dimensiones: personas, métodos y procedimientos, herramientas", o)


# =====================================================================================
# DEL APUNTE: Métricas
# =====================================================================================

FICHA = [  # pág. 4: (título, color, renglones)
    ("Atributo", "warn", ["Calidad", "del código"]),
    ("Medida", "dato", ["50 errores", "encontrados"]),
    ("Unidad de medida", "ok", ["errores por", "revisión"]),
    ("Métrica", "teoria", ["errores por cada 1.000", "líneas de código"]),
]


def metrica_ficha():
    nombre = "metrica-ficha"
    w, h, hc = 215, 112, 34
    o = ""
    for i, (t, k, rr) in enumerate(FICHA):
        x, y = (i % 2) * (w + 12), (i // 2) * (h + 12)
        o += (f'<rect class="cuerpo-f" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>'
              f'<rect class="hf {k}" x="{x}" y="{y}" width="{w}" height="{hc}" rx="8"/>'
              + texto(x + w / 2, y + 23, t, "num-t chico") + lineas(x + w / 2, y + 66, rr, "en", 19))
    y = 2 * (h + 12)
    W = 2 * w + 12
    o += (f'<rect class="cuerpo-f" x="0" y="{y}" width="{W}" height="92" rx="8"/>'
          f'<rect class="hf mal" x="0" y="{y}" width="{W}" height="{hc}" rx="8"/>'
          + texto(W / 2, y + 23, "Indicador", "num-t chico")
          + lineas(W / 2, y + 60, ["Si hay más de 10 errores/KLOC,", "el código se considera defectuoso"], "en", 19))
    return svg(nombre, W, y + 94, "Atributo, medida, unidad de medida, métrica e indicador con el ejemplo del apunte", o)


def metricas_contexto():
    nombre = "metricas-contexto"
    cx, cy = 310, 150
    o = f'<ellipse class="centro-el" cx="{cx}" cy="{cy}" rx="78" ry="34"/>' + texto(cx, cy + 6, "Metrics", "num-t")
    cajas = [  # (x, y, w, título, renglones, punto de llegada)
        (10, 4, 230, "Process (proceso)", ["Used to improve SDLC efficiency", "(mejorar la eficiencia del SDLC)"], (150, 80)),
        (380, 4, 230, "Product (producto)", ["For software product quality", "(calidad del producto de software)"], (470, 80)),
        (10, 212, 260, "Project (proyecto)", ["To measure project team efficiency", "and testing tools (eficiencia del", "equipo y de sus herramientas de prueba)"], (150, 208)),
    ]
    for x, y, w, t, rr, (ex, ey) in cajas:
        hh = 30 + 17 * len(rr)
        o += f'<g class="fase"><rect class="caja" x="{x}" y="{y}" width="{w}" height="{hh}" rx="10"/>'
        o += texto(x + w / 2, y + 22, t, "tit") + lineas(x + w / 2, y + 42, rr, "desc") + "</g>"
        sx = cx - 60 if ex < cx else cx + 60
        sy = cy - 22 if ey < cy else cy + 22
        o += f'<line class="flecha" x1="{sx}" y1="{sy}" x2="{ex}" y2="{ey}" {punta(nombre)}/>'
    return svg(nombre, 620, 296, "Las métricas se aplican al proceso, al producto y al proyecto", o)


# =====================================================================================
# DEL APUNTE: Gestión de cambios
# =====================================================================================

def archivo(x, y):
    """El ícono de un PDF: una hoja con la esquina doblada."""
    return (f'<path class="hoja" d="M{x} {y} h24 l10 10 v32 h-34 z"/>'
            + f'<rect class="hoja-et" x="{x + 3}" y="{y + 20}" width="28" height="11" rx="2"/>'
            + texto(x + 17, y + 29, "PDF", "pdf-t"))


def versionado():
    nombre = "versionado"
    o = lineas(300, 26, ["Versionado"], "tit grande") + texto(300, 48, "explicado de forma sencilla", "en")
    o += '<line class="guia" x1="330" y1="66" x2="330" y2="262"/>'
    o += texto(165, 84, "Sin versionado:", "en") + texto(465, 84, "Con versionado:", "en")
    for (x, y), n in zip([(88, 98), (210, 98), (88, 176), (210, 176)],
                         [["Invoice-V1.pdf"], ["V2-final.pdf"], ["V2-final2.0.pdf"], ["V3-this-is-the-", "true-final.pdf"]]):
        o += archivo(x, y) + lineas(x + 17, y + 58, n, "desc", 15)
    o += archivo(448, 98) + texto(465, 156, "The-one-and-only-invoice.pdf", "desc")
    o += lineas(465, 178, ["...but with a version history", "(...pero con historial de versiones)"], "desc")
    return svg(nombre, 600, 266, "Versionado explicado de forma sencilla: sin versionado y con versionado", o)


def git_ramas():
    nombre = "git-ramas"
    r, yM, yF = 13, 84, 150
    main = [60, 170, 260]
    rama = [240, 330, 420]
    merge = 530
    o = ""
    for a, b in zip(main, main[1:]):
        o += f'<line class="linea-c" x1="{a + r}" y1="{yM}" x2="{b - r}" y2="{yM}"/>'
    o += f'<line class="linea-c" x1="{main[-1] + r}" y1="{yM}" x2="{merge - r}" y2="{yM}"/>'
    o += f'<path class="linea-c" d="M{main[0] + r} {yM} C140 {yM} 150 {yF} {rama[0] - r} {yF}" fill="none"/>'
    for a, b in zip(rama, rama[1:]):
        o += f'<line class="linea-c" x1="{a + r}" y1="{yF}" x2="{b - r}" y2="{yF}"/>'
    o += f'<path class="linea-c" d="M{rama[-1] + r} {yF} C490 {yF} 480 {yM} {merge - r} {yM}" fill="none"/>'
    for x in main + [merge]:
        o += f'<circle class="commit" cx="{x}" cy="{yM}" r="{r}"/>'
    for x in rama:
        o += f'<circle class="commit verde" cx="{x}" cy="{yF}" r="{r}"/>'

    def rotulo(x, y, w, t1, t2, clase, ax, ay1, ay2):
        return (f'<rect class="rotulo-c {clase}" x="{x}" y="{y}" width="{w}" height="38" rx="3"/>'
                + texto(x + w / 2, y + 16, t1, "en") + texto(x + w / 2, y + 31, t2, "desc")
                + f'<line class="flecha" x1="{ax}" y1="{ay1}" x2="{ax}" y2="{ay2}" {punta(nombre)}/>')
    o += rotulo(205, 4, 110, "Main tip", "(punta de main)", "", 260, 44, yM - r - 3)
    o += rotulo(455, 4, 150, "New merge commit", "(nuevo commit de merge)", "", merge, 44, yM - r - 3)
    o += rotulo(5, 186, 110, "Common base", "(base común)", "", 60, 184, yM + r + 3)
    o += rotulo(365, 186, 110, "Feature tip", "(punta de la rama)", "verde", 420, 184, yF + r + 3)
    return svg(nombre, 610, 228, "Una rama que sale de una base común y vuelve a la principal con un commit de merge", o)


def cilindro(x, y, w, h, clase, etiqueta):
    e = 7
    return (f'<path class="{clase}" d="M{x} {y + e} A{w / 2} {e} 0 0 0 {x + w} {y + e} V{y + h - e} '
            f'A{w / 2} {e} 0 0 1 {x} {y + h - e} Z"/>'
            f'<ellipse class="{clase}" cx="{x + w / 2}" cy="{y + e}" rx="{w / 2}" ry="{e}"/>'
            + texto(x + w / 2, y + h / 2 + 8, etiqueta, "cil-t"))


def vcs_svn_git():
    nombre = "vcs-svn-git"
    o = ""
    for ox, titulo, local in [(0, "SVN", False), (380, "GIT", True)]:
        o += texto(ox + 160, 24, titulo, "tit grande rojo")
        o += f'<rect class="servidor-a" x="{ox + 40}" y="42" width="190" height="72"/>'
        o += texto(ox + 115, 76, "Central Server", "en") + texto(ox + 115, 94, "(servidor central)", "desc")
        o += cilindro(ox + 205, 66, 86, 58, "repo-c", "Repository")
        for k, dx in enumerate([30, 135, 240]):
            x = ox + dx
            o += f'<rect class="dev-a" x="{x}" y="196" width="56" height="46"/>' + texto(x + 28, 224, f"D{k + 1}", "en")
            sx = ox + 85 + k * 50
            o += (f'<path class="flecha gruesa" d="M{x + 28} 192 V160 H{sx} V120" fill="none" {punta(nombre)}/>')
            if local:
                o += cilindro(x + 34, 230, 42, 36, "lr-c", "LR")
    o += '<rect class="leyenda" x="40" y="286" width="440" height="56" rx="10"/>'
    o += texto(56, 309, ". D1, D2, D3 --> Developers (desarrolladores)", "en izq")
    o += texto(56, 331, ". LR --> Local Repository (repositorio local)", "en izq")
    return svg(nombre, 720, 348, "SVN y Git: servidor central con su repositorio; en Git, además, un repositorio local en cada desarrollador", o)


VERSIONES = ["Version 1", "Version 2", "Version 3", "Version 4", "Version 5"]


def checkins(nombre, filas, pie, alt, conectar_columnas):
    """La cabecera "Checkins Over Time" con las cinco versiones; `filas` es, por cada archivo,
    una lista de (columna, texto, tenue)."""
    w, h, paso = 106, 32, 136
    xs = [10 + i * paso for i in range(5)]
    o = texto(350, 16, "Checkins Over Time", "cmd")
    o += f'<line class="flecha" x1="10" y1="26" x2="690" y2="26" {punta(nombre)}/>'
    for x, v in zip(xs, VERSIONES):
        o += f'<rect class="ver" x="{x}" y="38" width="{w}" height="{h}" rx="16"/>' + texto(x + w / 2, 59, v, "num-t mono")
    for j, fila in enumerate(filas):
        y = 96 + j * 58
        for c, t, tenue in fila:
            clase = "arch tenue" if tenue else "arch"
            o += f'<rect class="{clase}" x="{xs[c]}" y="{y}" width="{w}" height="{h}" rx="16"/>' + texto(xs[c] + w / 2, y + 21, t, "cmd")
        if not conectar_columnas:
            for (c1, _, _), (c2, _, _) in zip(fila, fila[1:]):
                o += f'<line class="flecha" x1="{xs[c1] + w + 3}" y1="{y + h / 2}" x2="{xs[c2] - 3}" y2="{y + h / 2}" {punta(nombre)}/>'
    if conectar_columnas:
        for x in xs:
            for y1 in (70, 128, 186):
                o += f'<line class="linea-c fina" x1="{x + w / 2}" y1="{y1}" x2="{x + w / 2}" y2="{y1 + 26}"/>'
    o += texto(350, 290, pie, "centro")
    return svg(nombre, 700, 298, alt, o)


def git_deltas():
    filas = [
        [(0, "File A", False), (1, "Δ1", False), (3, "Δ2", False)],
        [(0, "File B", False), (3, "Δ1", False), (4, "Δ2", False)],
        [(0, "File C", False), (1, "Δ1", False), (2, "Δ2", False), (4, "Δ3", False)],
    ]
    return checkins("git-deltas", filas,
                    "Almacenamiento de datos como cambios en una versión de la base de cada archivo.",
                    "Otros sistemas guardan los cambios (deltas) de cada archivo", False)


def git_snapshots():
    filas = [
        [(0, "File A", False), (1, "A1", False), (2, "A1", True), (3, "A2", False), (4, "A2", True)],
        [(0, "File B", False), (1, "B", True), (2, "B", True), (3, "B1", False), (4, "B2", False)],
        [(0, "File C", False), (1, "C1", False), (2, "C2", False), (3, "C2", True), (4, "C3", False)],
    ]
    return checkins("git-snapshots", filas,
                    "Almacenamiento de datos como instantáneas del proyecto a través del tiempo.",
                    "Git guarda instantáneas de todo el proyecto en cada versión", True)


def git_tres_secciones():
    nombre = "git-tres-secciones"
    cols = [(0, "Working", "Directory", "mal"), (230, "Staging", "Area", "ojo"), (460, ".git directory", "(Repository)", "gris")]
    o = ""
    for x, t1, t2, k in cols:
        o += f'<rect class="lugar {k}" x="{x}" y="0" width="180" height="58"/>' + lineas(x + 90, 25, [t1, t2], "num-t mono2", 19)
        o += f'<line class="linea-c" x1="{x + 90}" y1="58" x2="{x + 90}" y2="300"/>'
    m = punta(nombre)
    for y, x1, x2, t in [(110, 550, 90, "Checkout the project"), (190, 90, 320, "Stage Fixes"), (262, 320, 550, "Commit")]:
        d = 1 if x2 > x1 else -1
        o += f'<line class="flecha ancha" x1="{x1}" y1="{y}" x2="{x2 - 8 * d}" y2="{y}" {m}/>'
        o += texto((x1 + x2) / 2, y - 10, t, "cmd fondo")
    o += lineas(320, 324, ["Directorio de trabajo, área de almacenamiento y el directorio Git."], "centro")
    return svg(nombre, 640, 332, "Las tres secciones de un proyecto de Git y lo que mueve cada operación", o)


# =====================================================================================
# PROPIOS (no están en ningún apunte)
# =====================================================================================

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
    m = punta(nombre)
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


PREGUNTAS = [
    ("1. ¿Los proyectos se planifican y se siguen?", "Nivel 1 · Inicial", "n1"),
    ("2. ¿Hay un proceso común para todos los equipos?", "Nivel 2 · Gestionado", "n2"),
    ("3. ¿Se miden los procesos para controlar y predecir?", "Nivel 3 · Definido", "n3"),
    ("4. ¿Se usan los datos para mejorar e innovar?", "Nivel 4 · Cuantitativamente gestionado", "n4"),
]


def cmmi_diagnostico():
    nombre = "cmmi-diagnostico"
    wq, hq, paso, xn, wn = 390, 50, 90, 450, 290
    m = punta(nombre)
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


def grafo(nombre, nodos, aristas, rotulos, pie, ancho, alto, alt):
    m = punta(nombre)
    o = ""
    for x, y, w, t in nodos:
        o += f'<rect class="nodo" x="{x}" y="{y}" width="{w}" height="40" rx="20"/>' + texto(x + w / 2, y + 25, t, "en")
    for x1, y1, x2, y2 in aristas:
        o += f'<line class="flecha" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {m}/>'
    for x, y, t in rotulos:
        o += texto(x, y, t, "rot")
    o += texto(pie[0], pie[1], pie[2], "centro")
    return svg(nombre, ancho, alto, alt, o)


def grafo_par():
    return grafo("grafo-par",
                 [(210, 0, 140, "¿es par?"), (40, 100, 140, "decir par"), (380, 100, 140, "decir impar"), (230, 200, 100, "fin")],
                 [(245, 42, 125, 96), (315, 42, 435, 96), (125, 142, 250, 196), (435, 142, 310, 196)],
                 [(165, 62, "sí"), (395, 62, "no")], (280, 120, "N = 4 nodos · E = 4 aristas"),
                 560, 242, "Grafo de control de una función con un if: cuatro nodos y cuatro aristas")


def grafo_tarifa():
    return grafo("grafo-tarifa",
                 [(200, 0, 170, "¿más de 20 kg?"), (20, 90, 150, "tarifa pesada"), (330, 90, 170, "¿más de 5 kg?"),
                  (230, 180, 140, "tarifa media"), (430, 180, 140, "tarifa común"), (180, 280, 180, "mostrar el precio")],
                 [(255, 42, 95, 86), (315, 42, 415, 86), (395, 132, 300, 176), (435, 132, 500, 176),
                  (95, 132, 220, 276), (300, 222, 270, 276), (500, 222, 320, 276)],
                 [(165, 60, "sí"), (375, 60, "no"), (330, 150, "sí"), (485, 150, "no")],
                 (270, 345, "N = 6 nodos · E = 7 aristas"),
                 590, 352, "Grafo de control de la función de la tarifa: seis nodos y siete aristas")


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
    m = punta(nombre)
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


# =====================================================================================

D = {
    "cmmi-escalera": cmmi_escalera(),
    "cmmi-progreso": cmmi_progreso(),
    "elementos-proceso": elementos_proceso(),
    "metrica-ficha": metrica_ficha(),
    "metricas-contexto": metricas_contexto(),
    "versionado": versionado(),
    "git-ramas": git_ramas(),
    "vcs-svn-git": vcs_svn_git(),
    "git-deltas": git_deltas(),
    "git-snapshots": git_snapshots(),
    "git-tres-secciones": git_tres_secciones(),
    "ciclo-metrica": seis_pasos("ciclo-metrica", FASES, True, "Un ciclo continuo: se repite siempre",
                                "Ciclo de vida de las métricas: seis fases en un ciclo"),
    "definir-procesos": seis_pasos("definir-procesos", PASOS_PROCESO, False, "De cómo está (AS-IS) a cómo va a ser (TO-BE)",
                                   "Los seis pasos para definir los procesos"),
    "cmmi-diagnostico": cmmi_diagnostico(),
    "grafo-par": grafo_par(),
    "grafo-tarifa": grafo_tarifa(),
    "git-comandos": git_comandos(),
}

CALIDAD, METRICAS, CAMBIOS = "Calidad de software", "Métricas", "Gestión de cambios"
ORIGEN = {
    "cmmi-escalera": f"Diagrama del apunte de {CALIDAD}, pág. 21 (redibujado).",
    "cmmi-progreso": f"Diagrama del apunte de {CALIDAD}, pág. 21 (redibujado).",
    "elementos-proceso": f"Diagrama del apunte de {CALIDAD}, pág. 12 (redibujado): «Los procesos integran las tres dimensiones».",
    "metrica-ficha": f"Diagrama del apunte de {METRICAS}, pág. 4 (redibujado).",
    "metricas-contexto": f"Diagrama del apunte de {METRICAS}, pág. 4 (redibujado; entre paréntesis, la traducción).",
    "versionado": f"Diagrama del apunte de {CAMBIOS}, pág. 5 (redibujado).",
    "git-ramas": f"Diagrama del apunte de {CAMBIOS}, pág. 5 (redibujado; entre paréntesis, la traducción).",
    "vcs-svn-git": f"Diagrama del apunte de {CAMBIOS}, pág. 9 (redibujado).",
    "git-deltas": f"Diagrama del apunte de {CAMBIOS}, pág. 12 (redibujado).",
    "git-snapshots": f"Diagrama del apunte de {CAMBIOS}, pág. 12 (redibujado).",
    "git-tres-secciones": f"Diagrama del apunte de {CAMBIOS}, pág. 14 (redibujado).",
    "ciclo-metrica": f"No está dibujado en el apunte: son las seis fases de {METRICAS}, pág. 5, puestas en un ciclo.",
    "definir-procesos": f"No está dibujado en el apunte: son los seis pasos de {CALIDAD}, pág. 10.",
    "cmmi-diagnostico": "No está en el apunte: es un método para ordenar el diagnóstico con las definiciones de los niveles.",
    "grafo-par": f"No está dibujado en el apunte: {METRICAS}, pág. 13, nombra el grafo de control pero no lo dibuja.",
    "grafo-tarifa": f"No está dibujado en el apunte: {METRICAS}, pág. 13, nombra el grafo de control pero no lo dibuja.",
    "git-comandos": f"No está en el apunte: es el diagrama de {CAMBIOS}, pág. 14, con el repositorio remoto agregado.",
}
assert set(D) == set(ORIGEN)

PATRON = re.compile(r'(<div class="pd-grafico esq" data-g="([\w-]+)">)(.*?)(</div>)', re.S)


def main():
    usados = set()
    for ruta in glob.glob(os.path.join(CONTENIDO, "**", "*.html"), recursive=True):
        s = open(ruta, encoding="utf-8").read()

        def poner(mt):
            g = mt.group(2)
            usados.add(g)
            if g not in D:
                raise SystemExit(f"{ruta}: no hay esquema '{g}'")
            origen = ORIGEN[g]
            clase = "propio" if origen.startswith("No está") else "apunte"
            return (mt.group(1) + D[g] + f'\n    <p class="pd-pie esq-origen {clase}">{esc(origen)}</p>\n  '
                    + mt.group(4))

        nuevo = PATRON.sub(poner, s)
        if nuevo != s:
            open(ruta, "w", encoding="utf-8", newline="\n").write(nuevo)
            print("  " + os.path.relpath(ruta, RAIZ))
    for falta in sorted(set(D) - usados):
        print(f"  (sin usar: {falta})")


if __name__ == "__main__":
    main()
