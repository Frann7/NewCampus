# Teoria_Funcional-doc

Fuente: `C:/Users/Fran/AppData/Local/Temp/claude/C--Users-Fran-Desktop-NewCampus/196b4912-5fa9-4a20-89f0-578e09e99c9b/scratchpad/pyl-pdf/TOPIC 3/Teoria_Funcional-doc.pdf` · 3 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |

<!-- página 1 -->

 1
Fundamentos de la Programación Funcional

Modelos genéricos de programación:

 - Imperativa: explican paso a paso COMO resolver un problema, es decir que proveen un
                                    algoritmo para su resolución.

 - Declarativa: definen reglas QUE DESCRIBEN o DEFINEN la solución del problema.

 La programación Funcional es DECLARATIVA, aunque en la práctica existen muchos lenguajes
“funcionales” impuros, tales como LISP, que permiten especificar algoritmos. De todos modos, la mayor
parte de la programación en estos lenguajes se hace de manera declarativa.

Ejemplo que muestra la diferencia entre Programación Imperativa, y Programación Funcional
(cálculo del factorial de un número)

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

PROGRAMACION FUNCIONAL

• Está basada en la evaluación de expresiones construidas mediante llamadas a FUNCIONES.

• Se aplica el concepto matemático de Función:

FUNCIÓN: Transformación de un elemento (que puede ser una n-upla) tomado de un conjunto llamado
Dominio, en un y sólo un, valor tomado de otro conjunto (que puede ser el mismo); el Codominio.

• TRANSPARENCIA REFERENCIAL: Es la propiedad más importante de la Programación Funcional.
Se define de la siguiente manera: “una función siempre devuelve el mismo resultado si se le pasan los
mismos argumentos ” En otras palabras, el valor de una expresión depende solo de l os valores de sus
subexpresiones, y no del momento ni la forma en la cuál es llamada.

Debido a esto, por ejemplo,  f(x) + f(x)  es lo mismo que 2 * f(x)

• EFECTOS LATERALES: si una rutina, además de cumplir con su objetivo, realiza alguna otra tarea,
se dice que posee Efectos Laterales. En la práctica, esto se produce cuando se modifican los parámetros
de la rutina, o alguna variable global . La Programación Funcional NO posee efectos laterales, es decir
que una Función calcula su resultado y no hace nada más.

<!-- página 2 -->

 2
• La programación funcional pura NO posee asignaciones, ya que van en contra los postulados anteriores.

• Tampoco existe la iteración. Ésta se reemplaza por la recursividad.

• Las funciones son Valores de Primera Clase. Esto significa que se pueden utilizar en cualquier lugar en
el cuál esté permitido poner un valor, ya que tienen su misma jerarquía.

• En consecuencia, se permite definir Funciones de Orden Superior, que son funciones que tienen otras
funciones como argumentos o como resultado, aumentando la flexibilidad y generalidad del lenguaje.

• Normalmente los lenguajes funcionales poseen manejo implícito de memoria, por lo tanto no  se tiene
necesidad de crear y destruir variables en forma explícita.

• La estructura de datos principal de un lenguaje fun cional es la Lista, ya que por ser lenguaje de 4ta
generación, con un nivel de abstracción mayor, se orienta hacia la resolución de problemas de la
realidad, donde dicha estructura es mucho más común que otras, tales como el arreglo.

• Funciones Anónimas: en programación funcional se permite definir y utilizar una función sin asignarle
un nombre. Estas funciones se denominan Funciones Anónimas, y se expresan siguiendo la sintaxis del
Cálculo Lambda:  (lambda (parámetros) resultado) [ Lx.M].

Ejemplo en LISP:
 (LAMBDA (X) (* X X))

Uso de una Función Anónima como parámetro de una Función de Orden Superior
  (CONTARSI   (LAMBDA (E) (>= E 0))   ‘(2 -4 3 0 56 -34 2 8))

• Funciones que se ejecutan sobre una lista completa: (map funcion lista)  {devuelve la lista re sultante de
aplicar la función a cada uno de los elementos de lista}

• Normalmente los lenguajes funcionales tienen Tipado Dinámico.

• La programación funcional soporta Polimorfismo paramétrico y sobrecarga

• Evaluación Tardía: es una característica de algunos lenguajes funcionales por la cuál cuando se ejecuta
una función, las expresiones que se le pasan como parámetros son evaluadas en el momento en el que se
las necesita, y no antes. Esto hace que no sea necesario perder tiempo de ejecución para calcular va lores
que no se utilizan

• Las desventajas de los lenguajes funcionales son:
• Expresión de la Entrada/Salida
• Dificultad para obtener una implementación eficiente
• Actualización de estructuras de datos.

Ejemplos de lenguajes Funcionales:

   Lisp
   FP
   Haskell
   Hope
   ISWIM
   Miranda
   Scheme
   Standard ML

<!-- página 3 -->

 3
LISP  (LISt Processing)
• Es el lenguaje más conocido de Programación Funcional. Aún así, n o es un lenguaje funcional puro ya
que posee asignación (SETF) e iteración (DO).
• Se utiliza la notación prefijo para cualquier función, inclusive para las expresiones aritméticas
• Funciones y constantes más importantes
• (FIRST lista)    o      (CAR lista)    //devuelve el primer elemento de lista
• (REST lista)     o      (CDR lista)    //devuelve la lista resultante de quitar el primer elemento a lista
• (NULL lista)         //determina si una lista está vacía
• (CONS elemento lista)    //construye una nueva lista con elemento como primero y lista como resto
• (DEFUN  nombreFuncion (parámetros)  resultado)   //define una función
• (COND  (condición1  resultado1)  (condición2  resultado2) ... )
//devuelve el i-ésimo resultado si la i-ésima condición es verdadera, partiendo por i=1
• NIL // constante Lista Vacía y constante False
• T          // constante True
• ’()        // constante Lista Vacía
• (FUNCALL  variableFuncion  Parámetro1 Parámetro2 ... ParámetroN)
//ejecuta la función asociada a la variableFuncion, normalmente pasada como parámetro, con
los    parámetros indicados
• (LISTP  objeto)     //verdadero si objeto es una lista
• (NUMBERP objeto)     //verdadero si objeto es un número
• (AND  condicion1 condicion2 ...)   //verdadero si todas las condiciones son verdaderas
• (OR condicion1 condicion2 ...)    //verdadero si al menos una condición es verdadera
• (+ num1 num2 … numN)  // suma
• (- num1 num2)    // resta
• (<  expr1  expr2)   // verdadero si expr1 es menor que expr2
• (=  expr1  expr2)   // verdadero si expr1 es igual a expr2
