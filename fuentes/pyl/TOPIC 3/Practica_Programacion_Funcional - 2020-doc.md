# Practica_Programacion_Funcional - 2020-doc

Fuente: `C:/Users/Fran/AppData/Local/Temp/claude/C--Users-Fran-Desktop-NewCampus/196b4912-5fa9-4a20-89f0-578e09e99c9b/scratchpad/pyl-pdf/TOPIC 3/Practica_Programacion_Funcional - 2020-doc.pdf` · 3 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |

<!-- página 1 -->

PARADIGMAS DE PROGRAMACION           Licenciatura en Sistemas de Información
UADER – Oro Verde

Página: 1 / 3
Trabajo Práctico
Programación Funcional

En los ejercicios siguientes escriba la/s función/es que se indican, en LISP.

Nivel 1
1. Defina una función que calcule el cuadrado de un número.
2. Defina una función que determine el valor absoluto de un número.
3. Defina una función que realice el siguiente cálculo, para el parámetro n: F(n) = n * (n - 1) / 2.

Nivel 2
4. Defina una función que calcule la enésima potencia de un número.
5. Escriba una función llamada “Cantidad” que devuelva la cantidad de elementos de una lista.
6. Escriba una función llamada “Sumatoria” que devuelva la suma de elementos de una lista.
7. Realice una función que devuelva el i-ésimo elemento de una lista.
8. Elimine el i-ésimo elemento de una lista.
9. Escriba una función llamada “Existe” que indique si un objeto se encuentra dentro de una lista determinada.
10. Escriba una función que determine la Media de una lista de números.
11. Agregue un elemento a una lista en una posición dada.
12. Agregue un elemento a una lista ordenada, en el lugar que le corresponda.
13. Realice un programa que calcule la sumatoria de las tres primeras potencias (es decir el número, el número al
cuadrado y al cubo) de un número dado.
14. Escriba una función que tome una lista y un elemento como argumentos, y devuelva la lista original con todas las
ocurrencias de dicho elemento eliminadas.
15. Escriba una función llamada "reemplazo", que tome una lista y dos elementos como argumentos, y devuelva la lista
original con todas las instancias del primer elemento reemplazadas por el segundo.
16. Escriba una función que devuelva el mínimo elemento de una lista.
17. Escriba una función que devuelva el máximo elemento de una lista.
18. Defina una función que tome una lista de números y devuelva una 3-upla formada por el promedio, el máximo y el
mínimo de la lista.

Nivel 3
19. Escriba una función que calcu le el i-ésimo número perfecto ( los números perfectos son aquellos que son iguales a la
suma de sus divisores.
20. Escriba una función que calcule los n primeros números primos y los devuelva en una lista.
21. Escriba una función que determine la Va rianza de una lista de números: Varianza = Sumatoria (Xi - Media)2 / (n - 1).
Siendo Xi cada uno de los n elementos de la lista.
22. Escriba una función que calcule la Moda de una lista de números (el número que más se repite).
23. Devuelva la cantidad de números que contiene una lista.
24. Realice una función que transforme un binario, expresado a través de una lista de {0,1}, en decimal.
25. Realice una función que sume dos números binarios, expresados a través de dos listas de {0,1}.
26. Realice una función que transforme un entero decimal a binario, expresado como lista de {0,1}.
27. Escriba una función llamada “Palíndromo” que indique si una lista es Palíndromo (capicúa).
28. Escriba una función que determine si una lista de {0,1}, donde cada 0 representa un paréntesis que abre y cada 1 un
paréntesis que cierra, está balanceada (es decir, que cada 0 tiene su 1 correspondiente de acuerdo a las reglas que
siguen los paréntesis). Ej: (001101) está balanceada y (1001010) no lo está.
29. Defina una función que tome como entrada una lista de números entre el 1 y el 3, y devuelva un par ordenado con el
número que mayor cantidad de veces aparece en la lista original y su frecuencia.
30. Realice un programa que, dado un número N, calcule el mayor valor de la serie de Fibonacci que sea menor que N. La
serie está dada por: 0, 1, 1, 2, 3, 5, 8, 13, ... ; donde los  primeros números son 0 y 1, y los demás se calculan como
la suma de los dos anteriores.
31. Escriba una función llamada “intercalar” que intercale dos listas ordenadas manteniendo el orden definido por las
mismas.
32. Escriba una función que tome una lista y elimine las repeticiones adyacentes de sus elementos.
33. Escriba una función que tome un número y una lista conteniendo los coeficientes de un polinomio y devuelva el
resultado del mismo reemplazando el número por la variable:
Ej. para (2 5 4 50 3) y 3 el polinomio en x es  2 + 5 x + 4 x2 + 50 x3 + 3 x4 ,  donde x=3.
34. Dadas dos listas de números defina una función devuelva una tercera, cuyos elementos sean resultado del siguiente
cálculo:
Parámetros: L1, L2 listas de números.

<!-- página 2 -->

PARADIGMAS DE PROGRAMACION           Licenciatura en Sistemas de Información
UADER – Oro Verde

Página: 2 / 3
Resultado: L3 lista de números
L3(1) = L1(1)*L2(1) + L1(1)*L2(2) + ... + L1(1)*L2(N)
L3(2) = L1(2)*L2(1) + L1(2)*L2(2) + ... + L1(2)*L2(N)
. . . .
L3(M) = L1(M)*L2(1) + L1(M)*L2(2) + ... + L1(M)*L2(N)
35. Considere que cada conjunto se representa mediante una lista. Defina funciones para simular:
a. Unión de conjuntos.
b. Intersección de conjuntos.
c. Diferencia de conjuntos.
d. Diferencia simétrica de conjuntos.
36. Escriba una función que tome una lista como entrada y genere una nueva lista con la primera mitad de la lista original
como segundo elemento y la segunda mitad como primer elemento.
(x1, x2, x3, x4, x5, x6)  -->  ( (x4, x5, x6), (x1, x2, x3) ).
37. Escriba una función que tome dos listas y determine si la secuencia de elementos de la primera se encuentra dentro
de la segunda.
38. Escriba una función que tome como entrada tres listas y determi ne si la tercera se puede formar a partir de los
elementos de las dos primeras.

Nivel 4
39. Escriba una función llamada "Cantidad -de" que toma como argumentos una lista y una condición (función), y
devuelve la cantidad de elementos de la lista que cumplen con dicha condición.
40. Defina una función que tome una lista de números y una condición (función) como parámetros y devuelva la
sumatoria de los elementos que cumplen dicha condición.
41. Defina una función llamada “Select” que devuelva la lista de elementos que cumplen con una determinada condición.
42. Defina una función llamada “Map” o “Collect” que devuelva la lista de los resultados de aplicar una función que se
pasa como parámetro a cada elemento de la lista de entrada.
43. Escriba una función llamada “intercalar-según” que tome dos listas y una función como entrada, y construya una
nueva lista resultado de intercalar las dos primeras en el orden establecido por la función (es decir, que la función se
aplica a los dos elementos que se comparan en cada momento para determinar cuál es el mayor).

Nivel 5
5.1 – Lógica compleja
44. Escriba una función que dada una lista de números y un número N, devuelva la lista resultante de eliminar los N
números más cercanos al promedio de la lista de entrada.
Ej: si la lista es (1 6 34 2 3 55 4 1 12) y N = 5, el promedio es 13.1,
por lo cual se deberán eliminar los números 12, 6, 4, 3 y 2, y el resultado será (1 34 55 1).
45. Realice una función que tome como parámetro una lista y devuelva otra lista con los elementos de la primera
ordenados de menor a mayor,  aplicando:
a. Ordenamiento elemental de selección.
b. Ordenamiento "burbujas" (intercalación).
c. QuickSort.
d. HeapSort.
46. Escriba una función que tome una lista de números y un número N, y devuelva la lista resulta do de eliminar los N
números mayores de la lista de entrada.
Ej: si la lista es  (1 6 34 2 3 55 4 1 12)  y N = 4, el resultado es (1 2 3 4 1).
47. Escriba una función que tome como entradas una lista L y un número N, y devuelve los N elementos del  centro de L.
Observación: si la cantidad de elementos de L es un número par, se considera que el número N ingresado también
será par, y viceversa.
Ej: para L = (3 2 4 7 11 2 3 4) y N = 4, el resultado será (4 7 11 2).
48. Escriba una función que tome una lista y devuelva una lista de pares (número frecuencia), ordenados de mayor a
menor de acuerdo a esta última. La frecuencia correspondiente a cada número es la cantidad de veces que el número
aparece en la lista.
49. Dada una lista de números y un número, escriba una función que divida a la lista en rangos de  acuerdo al número
ingresado.
Ej: para (8 5 7 13 2 21 16) y 4 se forman cuatro rangos y se crea la lista ( (2 5) (7 8) (13 16) (21) ).

5.2 – Procesamiento de listas con sublistas
50. Escriba una función que determine la cantidad de listas que contiene una lista con sublistas (incluyendo la principal).
51. Escriba una función “Evaluar” que tome una expresión aritmética en notación prefijo, representada mediante una lista
anidada, y devuelva su resultado. Solo se p ermiten los operadores +, - y *. Cada subexpresión contiene dos
operandos. Por ejemplo, (Evaluar '(* (+ 4 6) 4)) debería devolver 40.

<!-- página 3 -->

PARADIGMAS DE PROGRAMACION           Licenciatura en Sistemas de Información
UADER – Oro Verde

Página: 3 / 3
52. Escriba una función que transforme una lista con sublistas en una lista lineal.
53. Escriba una función que, dadas dos listas numéricas determine si todos los elementos de la primera se encuentran
dentro del rango de números de la segunda. Considere que esta última puede contener sublistas.
54. Escriba una función que, dadas dos listas determine cuantos elementos iguales tienen. Amba s listas pueden contener
sublistas.
