# Programacion Funcional - Teoría

Fuente: `C:/Users/Fran/AppData/Local/Temp/claude/C--Users-Fran-Desktop-NewCampus/196b4912-5fa9-4a20-89f0-578e09e99c9b/scratchpad/pyl-pdf/TOPIC 3/Programacion Funcional - Teoría.pdf` · 16 página(s) · texto extraído con pypdf.
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
| 13 |  |
| 14 |  |
| 15 |  |
| 16 |  |

<!-- página 1 -->

Click to add Text
Programación Funcional
UADER

<!-- página 2 -->

1. Introducción
◼ Modelos genéricos de programación:
◼ Imperativa: explica paso a paso COMO
resolver un problema, es decir que provee un
algoritmo para su resolución.
◼ Declarativa: define reglas QUE
DESCRIBEN o DEFINEN la solución al
problema.

<!-- página 3 -->

1. Introducción
◼ Ejemplo Programación Imperativa, y Programación Funcional (cálculo del factorial de un número)
Forma Imperativa: (Especificación de los pasos del cálculo)
Dado el número N:
1 - Asignar a una variable I el valor de N
2 - Poner en 1 una variable FAC
3 - Mientras  I>0
2.1 - Asignar a FAC el resultado de FAC * I.
2.2 - Disminuir I en 1.
4 - Devolver el valor de FAC.
Forma Declarativa: (Definición de lo que ES el factorial)
Factorial(N)
- Si N=0, Factorial de N es 1.
- Si N>0, Factorial de N es N * Factorial (N-1).

<!-- página 4 -->

2 Programación Funcional
◼ Está basada en la evaluación de expresiones construidas mediante aplicaciones de
FUNCIONES (lambda calculus, Church, 1932).
◼ Se aplica el concepto matemático de Función:
FUNCIÓN: Transformación de un elemento (que puede ser una n-upla) tomado de un
conjunto llamado Dominio, en un y sólo un, valor tomado de otro conjunto (que puede
ser el mismo); el Codominio.
f(x) : X → Y

<!-- página 5 -->

2 Programación Funcional
◼ TRANSPARENCIA REFERENCIAL: Es la propiedad más importante de la Programación Funcional. Se
define de la siguiente manera: “una función siempre devuelve el mismo resultado si se le pasan los mismos
argumentos” En otras palabras, el valor de una expresión depende solo de los valores de sus subexpresiones,
y no del momento ni la forma en la cuál es llamada.
f(x) + f(x) es lo mismo que 2 * f(x)
◼ EFECTOS LATERALES: si una subrutina, además de cumplir con su objetivo, realiza alguna otra tarea,
se dice que posee Efectos Laterales. En la práctica, esto se produce normalmente cuando se modifican sus
parámetros o alguna variable global, o cuando se guardan datos en un archivo o se imprime en pantalla. La
Programación Funcional NO posee efectos laterales, es decir que una Función calcula su resultado y no
realiza nada más.
◼ Inmutabilidad: la Programación Funcional pura NO posee asignaciones, ya que van en contra los
postulados anteriores. Las variables toman un valor y no lo cambian dentro de su ámbito léxico.
◼ Tampoco existe la iteración. Ésta se reemplaza por la recursividad.

<!-- página 6 -->

2 Lisp (List Processor)
◼ Es el lenguaje más conocido de Programación Funcional. Aún así, no es un lenguaje funcional puro ya que posee asignación (SETF) e
iteración (DO).
◼ Se utiliza la notación prefijo para cualquier función, inclusive para las expresiones aritméticas
◼ Funciones y constantes más importantes
(DEFUN  nombreFuncion (parámetros)  resultado)   //define una función
(COND  (condición1  resultado1)  (condición2  resultado2) ... )
Listas
(FIRST lista)    o      (CAR lista)    //devuelve el primer elemento de lista
(REST lista)     o      (CDR lista)    //devuelve la lista resultante de quitar el primer elemento a lista
(NULL lista) //determina si una lista está vacía
(CONS elemento lista) //construye una nueva lista con elemento como primero y lista como resto
NIL // constante Lista Vacía y constante False
’(4 3 5 6)        // constante Lista
T          // constante True

<!-- página 7 -->

Programación Funcional
Pensamiento Funcional
⚫ Definir claramente en el lenguaje natural qué es lo que debe hacer la función
⚫ Definir su Dominio, para saber a cuales valores de los parámetros debe responder
⚫ Definir su Codominio, principalmente para saber el tipo de dato que debe devolver, y qué
características deben tener los valores de retorno
⚫ Analizar si alcanza con plantear una sola respuesta para todos los valores de entrada
posible, o si el conjunto de entrada se debe particionar en clases de valores que posean la
misma respuesta
⚫ Si hubiese clases, comenzar a plantear los casos más simples o de solución trivial.
⚫ Para cada caso, pensar cual es la solución Completa (las soluciones parciales deben formar
parte de la solución completa para dichos casos)
⚫ Si el planteamiento o la solución para un caso es compleja, pensar en cómo dividir el
problema en más de una función

<!-- página 8 -->

Programación Funcional
Las funciones son Valores de Primera Clase. Esto significa que se pueden utilizar en
cualquier lugar en el cuál esté permitido poner un valor, ya que tienen su misma jerarquía.
Funciones de Orden Superior, que son funciones que tienen otras funciones como
argumentos o como resultado, aumentando la flexibilidad y generalidad del lenguaje.
Ej: se necesita definir funciones que calculen:
• La cantidad de números pares que contiene una lista
• La cantidad de valores negativos que contiene una lista
• La cantidad de números perfectos que contiene una lista
◼ Una primer solución podría ser escribir tres funciones, una para cada problema
◼ Pero… ya que el proceso de resolución de los tres casos es similar, un mejor enfoque es
Generalizar la solución parametrizando la función que decide si un elemento se cuenta o no.
(defun contarSi(L seCuenta)
(cond
( (null L) 0 )
( (funcall seCuenta (first L)) (+ 1 (contarSi (rest L) seCuenta)) )
( T (contarSi (rest L) seCuenta)) ) )
Variable que contiene la función que se pasó como parámetro

<!-- página 9 -->

Programación Funcional
Llamada a una Función de Orden Superior
(contarSi  ‘(1 2 3 -2 -5 -3)  #’par)
Funciones Anónimas: en programación funcional se permite definir y
utilizar una función sin asignarle un nombre. Estas funciones se
denominan Funciones Anónimas, y se expresan siguiendo la sintaxis del
Cálculo Lambda:  (lambda (parámetros) resultado) [ Lx.M].
Ejemplo:   (Lambda (X) (* X X))
Uso de una Función Anónima como parámetro de una Función de
Orden Superior
(ContarSi     ‘(2 -4 3 0 56 -34 2 8)   (Lambda (n) (< n 0)))

<!-- página 10 -->

Programación Funcional
Otras características importantes
Normalmente los lenguajes funcionales poseen manejo implícito de memoria, por lo tanto
no se tiene necesidad de crear y destruir variables en forma explícita.
La estructura de datos principal de un lenguaje funcional es la Lista, ya que por ser
lenguaje de 4ta generación, con un nivel de abstracción mayor, se orienta hacia la
resolución de problemas de la realidad, donde dicha estructura es mucho más común que
otras, tales como el arreglo.
Normalmente los lenguajes funcionales tienen Tipado Dinámico.
La programación funcional soporta Polimorfismo.

<!-- página 11 -->

Programación Funcional
Otras características importantes
Evaluación Tardía (Lazy evaluation): es una característica de algunos lenguajes funcionales
por la cual cuando se ejecuta una función, las expresiones que se le pasan como parámetros son
evaluadas en el momento en el que se las necesita, y no antes. Esto hace que no sea necesario
perder tiempo de ejecución para calcular valores que no se utilizan
Ejemplo:
(defun algo(X Y Z)
(cond
((= X 1) 0)
((> X 10) Y)
(t Z)))
(algo 1 (minimo (pares (ordenar '(…))) (frecuencias '(…) )

<!-- página 12 -->

Programación Funcional
Otras características importantes
Currying: el nombre proviene de su creador Haskell Curry. Consiste en interpretar una función
de n parámetros, como una función de 1 parámetro que devuelve una función de n-1
parámetros, con el primer parámetro como valor fijo, y así sucesivamente. Se puede utilizar
internamente para la ejecución de funciones y también como soporte para la aplicación parcial
de funciones.
Cálculo Lambda: En lógica matemática y ciencias de la computación, el cálculo lambda,
también cálculo λ, es un sistema formal. Fue diseñado para investigar la definición de funciones
y cómo aplicarlas. También es una herramienta para analizar la recursividad. Fue introducido
por Alonzo Church y Stephen Cole Kleene en la década de 1930. Church utilizó el cálculo
lambda en 1936 para dar una respuesta negativa al problema de la decisión (Entscheidung
problema). El cálculo de Lambda constituye la base formal de los lenguajes de programación
funcionales.
En el cálculo lambda, una expresión o término se define recursivamente a través de las siguientes
reglas de formación:
1. Toda variable es un término: x, y, z, u, v, w, x1, x2, x3,...
2. Si t es un término y x es una variable, entonces (λx.t) es un término (llamado una
abstracción lambda).
3. Si t y s son términos, entonces (ts) es un término (llamado una aplicación lambda).

<!-- página 13 -->

Programación Funcional
Beneficios
◼ Los Programas son más fáciles de escribir porque el sistema libera al
usuario de las consideraciones de implementación, tales como manejo de
memoria, declaración de variables, etc.
◼ Los Programas son concisos (mucho más cortos que en la programación
imperativa).
◼ Los Programas son más fáciles de comprender porque poseen
propiedades matemáticas que permiten razonar acerca de ellos.
◼ La PF induce a la división de problema en subproblemas pequeños, lo que
ayuda al reuso de código.
◼ La PF ayuda a mejorar la calidad del código incluso en otros paradigmas
(razonamiento acerca del Dominio y Codominio, por ejemplo)

<!-- página 14 -->

Programación Funcional
Desventajas
⚫ La expresión de la Entrada/Salida no es funcional.
⚫ Read → no es función
⚫ Write → efectos laterales
⚫ Archivos
⚫ Actualización de las estructuras de datos
⚫ Dificultad para obtener una implementación eficiente

<!-- página 15 -->

Lenguajes Funcionales
◼ Lisp (1960, el primer lenguaje funcional)
◼ Hope (1970s)
◼ ML (1970s introduce sistemas de tipos polimórficos)
◼ Scheme (1975)
◼ Miranda (1980s)
◼ Haskell (1990, uno de los lenguajes funcionales más
importantes actualmente)
◼ Erlang (1995, de propósito general y concurrente)

<!-- página 16 -->

Programación Funcional
Fin PF
