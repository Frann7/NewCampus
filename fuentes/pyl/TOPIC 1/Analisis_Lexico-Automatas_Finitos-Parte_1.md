# Analisis_Lexico-Automatas_Finitos-Parte_1

Fuente: `C:/Users/Fran/AppData/Local/Temp/claude/C--Users-Fran-Desktop-NewCampus/196b4912-5fa9-4a20-89f0-578e09e99c9b/scratchpad/pyl-pdf/TOPIC 1/Analisis_Lexico-Automatas_Finitos-Parte_1.pdf` · 12 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |
| 9 |  |
| 10 |  |
| 11 |  |
| 12 |  |

<!-- página 1 -->

1
Análisis Léxico, Lenguajes
Formales y Autómatas Finitos
Paradigmas y Lenguajes

<!-- página 2 -->

2
Análisis léxico - Introducción
◼ Primera fase del proceso de compilación
◼ Analizador léxico = Scanner
◼ Objetivos del Análisis Léxico
◼ Identificar Componentes Léxicos (y atributos)
◼ Detectar Errores Léxicos
Comportamiento:
Analizador
Léxico
Analizador
Sintáctico
Programa Fuente
(archivo de texto)
Obtener
siguiente
caracter
caracter
Obtener siguiente
Componente Léxico
Componente Léxico
y atributos (lexema, …)
Árbol de Análisis Sintáctico
Administrador de la
Tabla de Símbolos

<!-- página 3 -->

3
Análisis léxico - Introducción
◼ Definiciones:
◼ Componente léxico: conjunto de cadenas que tienen un
mismo significado desde el punto de vista sintáctico (es
decir que pueden encontrarse en los mismos lugares desde el
punto de vista de la sintaxis). Ejemplo: identificador
◼ Lexema: cada una de las cadenas pertenecientes a  un
componente léxico. Ejemplo: tot1
◼ Patrón: regla que define la estructura de los lexemas de un
componente léxico (ley de conformación interna del
conjunto). Ejemplo: una letra seguida de 0 o más letras o
dígitos.

<!-- página 4 -->

4
Introducción a los Lenguajes Formales
◼ La Teoría de Lenguajes y Autómatas sirve como base
para las tareas que deben realizarse dentro de las
distintas fases de la compilación.
◼ Definiciones:
◼ Símbolo: ente abstracto sin definición formal
◼ Alfabeto: conjunto finito (y no vacío) de símbolos
◼ Cadena (palabra/word): secuencia finita de 0 o más
símbolos de un alfabeto
◼ Longitud de una cadena: sea w una cadena, la longitud de
w se denota |w| y es la cantidad de símbolos que posee.
◼ Cadena vacía: se denota e (epsilon) y |e|=0

<!-- página 5 -->

5
Introducción a los Lenguajes Formales
◼ Operaciones sobre cadenas
◼ Concatenación: Sean w y x dos cadenas, su concatenación se escribe wx y es la
cadena compuesta por la secuencia de símbolos de w seguidos por la secuencia
de símbolos de x.
◼ Prefijo de una cadena w: es cualquier cadena s, donde w = sx |x| >=0
◼ Sufijo de una cadena w: es cualquier cadena s, donde w = xs |x| >=0
◼ Subcadena de w: es cualquier cadena s, donde w = xsy |x| >=0,  |y| >=0
◼ Prefijo propio, sufijo propio y subcadena propia: es un prefijo, sufijo,
subcadena distinta a la original
◼ Potencia: sea w una cadena e i >=0 un número natural, se escribe wi y es:
w0 = e
wi = w.wi-1 i > 0

<!-- página 6 -->

6
Introducción a los Lenguajes Formales
◼ Lenguaje (formal): conjunto de cadenas formadas a partir de un alfabeto
◼ Operaciones sobre lenguajes
◼ Unión: sean L y M dos lenguajes, la unión de L con M se escribe L  M y es:
L  M = {w | (w en L)  (w en M)}
◼ Concatenación: sean L y M dos lenguajes, su concatenación se escribe LM y es:
L.M = {wx | (w en L)  (x en M)}
◼ Potencia: sea L un lenguaje e i>= 0 un natural, la potencia se escribe Li y es:
L0 = {e}
Li = L.Li-1 i>0
◼ Clausura de Kleene o clausura transitiva: sea L un lenguaje, su clausura se
escribe L* y es:
L* = Ui=0.. Li
◼ Clausura positiva: sea L un lenguaje, su clausura se escribe L* y es:
L+ = Ui=1.. Li

<!-- página 7 -->

7
Lenguajes Formales y Autómatas Finitos
◼ Sistema de estados finitos: es un sistema que tiene las siguientes características:
◼ Posee entradas y salidas discretas
◼ Posee una cantidad finita de configuraciones llamadas “estados”
◼ El sistema en cada momento se encuentra en un estado determinado
◼ Cada estado resume la información de los anteriores, pero el sistema no
recuerda (registra) los estados en que estuvo
◼ Autómata finito: modela un sistema de estados finitos
◼ Es un modelo matemático definido por una 5-upla (Q, S, d , q0, F), donde:
Q: conjunto finito de estados
S: alfabeto de entrada
q0 en Q: estado inicial (nota: “en” se utiliza como “pertenece”)
FQ: conjunto de estados “Finales” o de “Aceptación”
d: Función de Transición
d: Q x S → Q

<!-- página 8 -->

8
Lenguajes Formales y Autómatas Finitos
Comportamiento de un Autómata finito:
1. Al inicio del reconocimiento el autómata se encuentra en su estado inicial y
el control está apuntando a la primer posición de la cadena.
2. Luego se utiliza la función de transición para calcular el nuevo estado (en
base al estado actual y al símbolo al que apunta el control).
3. Posteriormente se avanza el control, una posición a la derecha.
4. Si no se alcanzó el fin de la cadena, se vuelve al paso 2.
5. Al finalizar, si el estado en el que quedó pertenece al conjunto F de estados
finales, la cadena es aceptada (reconocida), y en caso contrario, es rechazada.

<!-- página 9 -->

9
Lenguajes Formales y Autómatas Finitos
◼ Un Autómata Finito define exactamente un Lenguaje (formal)
◼ Diagrama de transiciones: es una representación gráfica de un AF, a
través de un grafo dirigido y etiquetado, donde:
◼ Los nodos del grafo representan los estados del autómata
◼ Los arcos del grafo representan la función de transición, de tal
manera de que el arco (x, y) posee la etiqueta a si, y solo si, d(x, a)=y
◼ Los estados que se grafican con doble círculo son estados finales
◼ El estado inicial se indica mediante una flecha sin nodo de partida

<!-- página 10 -->

10
Lenguajes Formales y Autómatas Finitos
◼ Tabla de Transiciones: es una representación tabular de la función de transición, donde las
filas son estados, las columnas son los símbolos de entrada y las celdas definen el estado que
se alcanza desde el estado de la fila mediante el símbolo de la columna.
◼ Estado “Muerto”: es todo estado de un AF que no es de aceptación y en el cual todas las
transiciones de salida son ciclos hacia él mismo.
◼ En símbolos
q es estado “muerto” si, y solo si :   (q en (Q - F))  ("a en S (d(q, a) = q))

<!-- página 11 -->

11
Lenguajes Formales y Autómatas Finitos
◼ Lenguaje reconocido por un Autómata Finito
◼ Función de transición extendida: d
d: Q x S* → Q
◼ Definición:
d(q, e) = q
d(q, aw) = d( d(q, a), w)         a en S
w en S*
◼ Dado un AF M =(Q, S, d , q0, F), el lenguaje que reconoce se denota LM y es:
LM = {w | (w en S*) y (d(q0, w) en F)}
◼ La Clase de Lenguajes definidos por los Autómatas Finitos se denomina
“Clase de los Lenguajes Regulares”
^
^
^
^ ^
^

<!-- página 12 -->

12
Lenguajes Formales y Autómatas Finitos
Fin primera parte Análisis Léxico, Lenguajes
Formales y Autómatas Finitos
