# Funcional

Fuente: `C:/Users/Fran/AppData/Local/Temp/claude/C--Users-Fran-Desktop-NewCampus/196b4912-5fa9-4a20-89f0-578e09e99c9b/scratchpad/pyl-pdf/TOPIC 3/Funcional.pdf` · 13 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Programación Funcional.

<!-- página 2 -->

¿Que es la programación funcional?
La programación funcional es un paradigma de
programación declarativa basado en la
utilización de funciones aritméticas que no
maneja datos mutables o de estado. Enfatiza la
aplicación de funciones, en contraste con el
estilo de programación imperativa, que
enfatiza los cambios de estado

<!-- página 3 -->

Programación funcional
● No mantiene estados.
● Enfatiza la aplicación de funciones
● Las funciones no tienen efecto
secundario
● Uso de recurrencia

<!-- página 4 -->

Ventajas de usar un paradigma
funcional
• Ausencia de efectos colaterales (
transparencia referencial )
• Proceso de depuración menos problemático
• Pruebas de unidades más confiables
• Mayor facilidad para la ejecución concurrente

<!-- página 5 -->

Lenguajes funcionales
Entre los lenguajes funcionales puros, cabe destacar a Haskell y
Miranda.
Los lenguajes funcionales híbridos más conocidos son Scala, Lisp,
Clojure, Scheme, Ocaml, SAP y Standard ML (estos dos últimos,
descendientes del lenguaje ML). Erlang es otro lenguaje funcional de
programación concurrente.
Mathematica permite la programación en múltiples estilos, pero
promueve la programación funcional. R también es un lenguaje
funcional dedicado a la estadística.
Microsoft Research está trabajando en el lenguaje F# (Functional#).

<!-- página 6 -->

Funciones
Una función es una relación entre un set de inputs y un
set de outputs permisibles...
...con la propiedad de que cada input está relacionado
con exactamente un output.

<!-- página 7 -->

Funciones
Haskell
Java
PHP
1987
1995
Lenguaje -> Año
2003Scala

<!-- página 8 -->

Lisp
• Lisp (LISt Processing)
• Es el lenguaje más conocido de Programación
Funcional. Aún así, no es un lenguaje
funcional puro ya que posee asignación
(SETF) e iteración (DO).
• Se utiliza la notación prefijo para cualquier
función, inclusive para las expresiones
aritméticas
• (defun cuadrado(n) (* n n))

<!-- página 9 -->

Scala
• Scala es multiparadigma.
• Se puede utilizar el Paradigma Funcional y el
orientado a Objetos
• Es de tipado estático
• Tiene genéricos similar a Java
• Todo es un Objeto (casi todo)
• Fue influenciado por Java, Ruby, Haskell,
Erlang,
• etc...

<!-- página 10 -->

Elixir
• Orientado a Concurrencia: Diseñado sobre la máquina virtual de Erlang (BEAM), Elixir es altamente
eficiente para crear aplicaciones concurrentes y distribuidas, facilitando el manejo de procesos en
paralelo sin bloqueos.
• Funcional: Utiliza el paradigma de programación funcional, promoviendo inmutabilidad y expresiones
puras. Esto ayuda a reducir errores y facilita el razonamiento sobre el código.
• Escalabilidad: Es ideal para sistemas distribuidos y escalables, permitiendo que las aplicaciones
crezcan tanto en complejidad como en volumen sin pérdida de rendimiento.
• Resiliencia: Su diseño se centra en la tolerancia a fallos. Gracias a la infraestructura de supervisión de
procesos, Elixir permite que los sistemas manejen errores sin afectar la estabilidad general.
• Sintaxis Intuitiva y Moderna: Inspirada en Ruby, la sintaxis de Elixir es clara y fácil de leer, lo que hace
que los desarrolladores la aprendan rápidamente.
• Excelente Soporte para Web y APIs: Gracias al framework Phoenix, que es rápido y escalable, es una
opción muy popular para desarrollar aplicaciones web en tiempo real.
• Interoperabilidad: Elixir puede interactuar con bibliotecas y código escrito en Erlang, lo que amplía
enormemente las posibilidades de su ecosistema.
• Sistema de Metaprogramación: Utiliza macros para manipular y transformar el código en tiempo de
compilación, lo que permite crear DSLs y realizar transformaciones avanzadas del código.

<!-- página 11 -->

Elixir
• Definir Funciones
• defmodule Math do
• def suma(a, b) do
• a + b
• end
• end
•
• Funciones Anónimas
• suma = fn (a, b) -> a + b end
• suma.(3, 4) # Llama a la función y devuelve 7
•
• Pattern matching
• defmodule Factorial do
• def calcular(0), do: 1
• def calcular(n), do: n * calcular(n - 1)
• end

<!-- página 12 -->

Sentencias Elixir
• Condicionales
• if condicion do
• # código si la condición es verdadera
• else
• # código si es falsa
• end
•
• unless condicion do
• # código si la condición es falsa
• end
•
•
case variable do
valor1 -> # código si es valor1
valor2 -> # código si es valor2
_ -> # valor por defecto
end
cond do
condicion1 -> # código si es verdadera
condicion2 -> # código si es verdadera
true -> # valor por defecto
end

<!-- página 13 -->

Listas Elixir
⚫ lista = [1, 2, 3, 4, 5]
⚫ Concatenar: [1, 2, 3] ++ [4, 5]  # Resultado: [1, 2, 3, 4, 5]
⚫ Restar: [1, 2, 3, 4] -- [2, 4]  # Resultado: [1, 3]
⚫ Patter matching : [head | tail] = [1, 2, 3]  # head = 1, tail = [2, 3]
⚫ Agregar elemento : nueva_lista = [nuevo_elemento | lista_existente]
