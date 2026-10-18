# -*- coding: utf-8 -*-
"""Colorea los bloques de código al construir (lo llama construir.py).

En contenido/ el código se escribe plano, como siempre:
    <pre class="codigo"><code>...</code></pre>
y acá se convierte en renglones con sus palabras marcadas, para que
estilos.css los pinte (clases c-*). No hay nada que corra en el navegador.

Cada renglón queda en un <span class="cl">. Los bloques de 4 renglones o más
llevan número de línea (clase "num"). Atributos opcionales en el <pre>:
    data-lang="cpp|php|cs|html|git|sql|c|texto"   el lenguaje, si no se adivina bien
    data-desde="12"       número del primer renglón (un programa partido en partes)
    data-clave="3,7-9"    renglones resaltados, contados dentro del bloque

De paso marca los <h3> de ejemplos ("Ejemplo ...") y de errores ("Errores y
trampas") con su clase (h-ej, h-ojo), que es la que les da el color.
"""
import html
import re

PRE = re.compile(r'<pre class="codigo"([^>]*)><code>(.*?)</code></pre>', re.S)

CLAVES = set("""
class struct public private protected virtual override static const return if else elseif for
foreach while do switch case break continue default new delete this nullptr null NULL true false
TRUE FALSE namespace using function echo print extends implements interface abstract as var let
try catch throw include require include_once require_once global operator final self parent
typedef template typename friend inline explicit sizeof and or not instanceof use fn match
""".split())

TIPOS = set("""
int double float bool char void string long short unsigned auto std size_t array mixed object
String Long Boolean Date Character
""".split())

IDENT = re.compile(r'[^\W\d]\w*')
NUMERO = re.compile(r'\d+(?:\.\d+)?\b')
CADENA = re.compile(r'"(?:\\.|[^"\\\n])*"|\'(?:\\.|[^\'\\\n])*\'')
COM_BLOQUE = re.compile(r'/\*.*?\*/', re.S)
COM_LINEA = re.compile(r'//[^\n]*')
HASTA_FIN = re.compile(r'[^\n]*')
VAR_PHP = re.compile(r'\$[A-Za-z_]\w*')
DIR_PHP = re.compile(r'<\?php|<\?=|\?>')
LLAMADA = re.compile(r'[ \t]*\(')

# SQL (el de SQL Server, el de Bases de Datos): sin distinguir mayúsculas.
CLAVES_SQL = set("""
select from where and or not in is null like between order by asc desc group having top distinct as
join inner left right outer full on create table alter add drop constraint primary key foreign
references unique default check identity insert into values update set delete begin tran
transaction commit rollback use go case when then else end exists union all with grant revoke
truncate view index database if declare column
""".split())

TIPOS_SQL = set("""
int integer bigint smallint tinyint bit decimal numeric money smallmoney float real date datetime
datetime2 smalldatetime time char varchar nchar nvarchar text ntext
""".split())

SENTENCIA_SQL = re.compile(r'^\s*(select\s|create\s+(table|database|view)\b|insert\s+into\b|'
                           r'update\s+\w+\s+set\b|delete\s+from\b|alter\s+table\b|drop\s+table\b|'
                           r'begin\s+tran)', re.I | re.M)
COM_SQL = re.compile(r'--[^\n]*')
CADENA_SQL = re.compile(r"'(?:''|[^'\n])*'")
VAR_SQL = re.compile(r'@\w+')


def lenguaje(src, atributos):
    m = re.search(r'data-lang="([^"]+)"', atributos)
    if m:
        return m.group(1)
    if '<<<<<<<' in src and '>>>>>>>' in src:
        return 'conflicto'
    lineas = [l.strip() for l in src.split('\n') if l.strip()]
    if lineas and all(l.startswith(('git ', '$ git ')) for l in lineas):
        return 'git'
    if '<?php' in src or VAR_PHP.search(src):
        return 'php'
    if 'using System' in src or 'Console.' in src:
        return 'cs'
    if '#include' in src or 'std::' in src or re.search(r'\b(virtual|nullptr|override)\b', src):
        return 'cpp'
    if src.lstrip().startswith('<') and re.search(r'</?[a-zA-Z]', src):
        return 'html'
    if SENTENCIA_SQL.search(src):
        return 'sql'
    if re.search(r'[;{}]|\bclass\b', src):
        return 'c'
    return 'texto'


def tokens_c(src, lang):
    """Lenguajes con llaves (C++, PHP, C#, JS). Devuelve pares (clase, texto)."""
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        if c == '/':
            m = COM_BLOQUE.match(src, i) or COM_LINEA.match(src, i)
            if m:
                yield 'com', m.group(0)
                i = m.end()
                continue
        if c == '#':
            antes = src[src.rfind('\n', 0, i) + 1:i].strip()
            if lang == 'cpp' and not antes:                      # #include <...>
                m = HASTA_FIN.match(src, i)
                yield 'dir', m.group(0)
                i = m.end()
                continue
            if lang == 'php' and (not antes or antes[-1] in ';{}'):  # comentario con #
                m = HASTA_FIN.match(src, i)
                yield 'com', m.group(0)
                i = m.end()
                continue
        if c in '"\'':
            m = CADENA.match(src, i)
            if m:
                yield 'str', m.group(0)
                i = m.end()
                continue
        if lang == 'php':
            m = VAR_PHP.match(src, i) if c == '$' else (DIR_PHP.match(src, i) if c in '<?' else None)
            if m:
                yield ('var' if c == '$' else 'dir'), m.group(0)
                i = m.end()
                continue
        if c.isdigit():
            m = NUMERO.match(src, i)
            if m:
                yield 'num', m.group(0)
                i = m.end()
                continue
        if c.isalpha() or c == '_':
            m = IDENT.match(src, i)
            palabra = m.group(0)
            if palabra in CLAVES:
                clase = 'key'
            elif palabra in TIPOS:
                clase = 'tipo'
            elif LLAMADA.match(src, m.end()):
                clase = 'fn'
            elif palabra[0].isupper():
                clase = 'tipo'
            else:
                clase = None
            yield clase, palabra
            i = m.end()
            continue
        yield None, c
        i += 1


def tokens_html(src):
    pos = 0
    for m in re.finditer(r'(?P<com><!--.*?-->)|(?P<key></?[A-Za-z][\w-]*|/?>)|(?P<str>"[^"\n]*"|\'[^\'\n]*\')',
                         src, re.S):
        if m.start() > pos:
            yield None, src[pos:m.start()]
        yield m.lastgroup, m.group(0)
        pos = m.end()
    if pos < len(src):
        yield None, src[pos:]


def tokens_git(src):
    for k, linea in enumerate(src.split('\n')):
        if k:
            yield None, '\n'
        resto = linea
        if resto.startswith('$ '):
            yield 'com', '$ '
            resto = resto[2:]
        palabras = re.split(r'(\s+|"[^"]*")', resto)
        vistos = 0
        for p in palabras:
            if not p:
                continue
            if p.isspace():
                yield None, p
                continue
            vistos += 1
            if p.startswith('"'):
                yield 'str', p
            elif vistos == 1 and p == 'git':
                yield 'key', p
            elif vistos == 2:
                yield 'fn', p
            elif p.startswith('-'):
                yield 'num', p
            else:
                yield None, p


def tokens_sql(src):
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        m = None
        if c == '-':
            m, clase = COM_SQL.match(src, i), 'com'
        elif c == '/':
            m, clase = COM_BLOQUE.match(src, i), 'com'
        elif c == "'":
            m, clase = CADENA_SQL.match(src, i), 'str'
        elif c == '@':
            m, clase = VAR_SQL.match(src, i), 'var'
        elif c.isdigit():
            m, clase = NUMERO.match(src, i), 'num'
        if m:
            yield clase, m.group(0)
            i = m.end()
            continue
        if c.isalpha() or c == '_':
            m = IDENT.match(src, i)
            palabra = m.group(0)
            baja = palabra.lower()
            if baja in CLAVES_SQL:
                clase = 'key'
            elif baja in TIPOS_SQL:
                clase = 'tipo'
            elif LLAMADA.match(src, m.end()):
                clase = 'fn'
            else:
                clase = None
            yield clase, palabra
            i = m.end()
            continue
        yield None, c
        i += 1


def tokens_conflicto(src):
    for k, linea in enumerate(src.split('\n')):
        if k:
            yield None, '\n'
        yield ('key' if linea.startswith(('<<<<<<<', '=======', '>>>>>>>')) else None), linea


def tokens(src, lang):
    if lang == 'texto':
        return [(None, src)]
    if lang == 'html':
        return tokens_html(src)
    if lang == 'git':
        return tokens_git(src)
    if lang == 'conflicto':
        return tokens_conflicto(src)
    if lang == 'sql':
        return tokens_sql(src)
    return tokens_c(src, lang)


def numeros(texto):
    """'3,7-9' -> {3, 7, 8, 9}"""
    fuera = set()
    for parte in texto.split(','):
        parte = parte.strip()
        if '-' in parte:
            a, b = parte.split('-')
            fuera.update(range(int(a), int(b) + 1))
        elif parte:
            fuera.add(int(parte))
    return fuera


def un_bloque(m):
    atributos, adentro = m.group(1), m.group(2)
    if re.search(r'<[a-zA-Z/!]', adentro):       # ya trae etiquetas: no se toca
        return m.group(0)
    src = html.unescape(adentro)
    renglones = [[]]
    for clase, texto in tokens(src, lenguaje(src, atributos)):
        for k, trozo in enumerate(texto.split('\n')):
            if k:
                renglones.append([])
            if trozo:
                t = html.escape(trozo, quote=False)
                renglones[-1].append('<span class="c-%s">%s</span>' % (clase, t) if clase else t)

    clave = re.search(r'data-clave="([^"]*)"', atributos)
    clave = numeros(clave.group(1)) if clave else set()
    desde = re.search(r'data-desde="(\d+)"', atributos)
    cuerpo = ''.join('<span class="cl%s">%s\n</span>' % (' clave' if k in clave else '', ''.join(r))
                     for k, r in enumerate(renglones, 1))
    extra = ''
    if len(renglones) >= 4 or desde:
        extra = ' num'
    estilo = ' style="counter-reset:linea %d"' % (int(desde.group(1)) - 1) if desde else ''
    return '<pre class="codigo%s"%s%s><code>%s</code></pre>' % (extra, atributos, estilo, cuerpo)


TITULO = re.compile(r'<h3>(Ejemplo\b|Errores y trampas)')


def un_titulo(m):
    """Los h3 de ejemplos y de errores llevan su color (estilos.css)."""
    return '<h3 class="%s">%s' % ('h-ej' if m.group(1) == 'Ejemplo' else 'h-ojo', m.group(1))


def colorear(texto):
    return TITULO.sub(un_titulo, PRE.sub(un_bloque, texto))
