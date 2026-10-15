# Practica_I_-_AutomatasER

Fuente: `C:/Users/Fran/AppData/Local/Temp/claude/C--Users-Fran-Desktop-NewCampus/196b4912-5fa9-4a20-89f0-578e09e99c9b/scratchpad/pyl-pdf/TOPIC 1/Practica_I_-_AutomatasER.pdf` · 3 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |

<!-- página 1 -->

PPARADIGMASARADIGMAS  YY L LENGUAJESENGUAJES
Trabajo Práctico I
Autómatas finitos (AF) - Expresiones regulares (ER)
A. Definir reconocedores y expresiones regulares  para los siguientes lenguajes
1. Identificadores en Pascal.
2. Constante entera en Pascal.
3. Operadores relacionales del Pascal.
4. Constantes reales.
5. Conjunto de cadenas sobre {a, b} de longitud par.
6. Conjunto de cadenas sobre {a, b} que terminen con abb.
7. Conjunto de cadenas sobre {0, 1} que comiencen y terminen con 0.
8. Conjunto de cadenas sobre {0, 1} que contengan como subcadenas a 001 o 100.
9. Identificadores de cualquier longitud que comiencen con una letra y contengan letras, dígitos o guiones, que
no contengan dos guiones seguidos ni terminen con guión.
10. Comentarios acotados por (* *)  o { }.
11. Conjunto de cadenas que representen números reales sin notación exponencial considerando la coma para
separar los miles y el punto para los decimales.
12. Conjunto de cadenas sobre {0, 1} que contengan tres ceros consecutivos.
13. Conjunto de cadenas sobre {a, b, c} de la forma wcw, con w en {a, b}* y |w| = 2.
14. Conjunto de cadenas sobre {0, 1} que no contengan dos unos consecutivos.
15. Conjunto de cadenas sobre {0, 1} que no contengan la cadena 101.
16. Conjunto de cadenas sobre {0, 1} que sean, en binario, equivalentes a los múltiplos decimales de 4.
17. Conjunto de cadenas sobre {a, b, c} que no contengan como subcadenas a b ni a ac.
18. Conjunto de cadenas sobre {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} donde el 1, 3, 5, 7, si están en la cadena, aparezcan
en este orden.
19. Conjunto de cadenas sobre {0, 1} de longitud menor a 2 o mayor que 4.
20. Conjunto de cadenas sobre {a, b, c} de la forma wxz, donde w comienza y termina con a, x comienza y
termina con b y z comienza y termina con c; con w, x, z en {a, b, c}*.
21. Conjunto de cadenas sobre {0, 1} que no contengan las cadenas 101, 010, 000 y 111.
22. Conjunto de cadenas sobre {0, 1} que contengan las subcadenas 00 y 11, o que tengan longitud menor a 4.
23. Conjunto de cadenas sobre {r, s, t, u} donde toda s aparece antes que cualquier t.
24. Conjunto de cadenas de números binarios impares.
25. Conjunto de cadenas con el siguiente formato:
De 1 a 4 letras + símbolo @ + de 1 a 4 letras + punto + cadenas que contienen subcadenas de 1 hasta 4
dígitos o letras, separadas por punto.
26. Conjunto de cadenas sobre {x, y} de longitud múltiplo de 3 o de longitud 0.
27. Conjunto de cadenas sobre {a, s} que no posean dos s ni dos a consecutivas.
28. Conjunto de cadenas sobre {0, 1} con un número impar de 0s y un número par de 1s.
29. Conjunto de cadenas sobre {0, 1} donde en todo prefijo, la cantidad de 0 difiera de la cantidad de 1 en no
más de uno (|cantidad de 0 - cantidad de 1| <= 1).
30. Conjunto de cadenas sobre {0, 1} de la forma ww donde w está en {0, 1}2.
31. Lenguaje vacío sobre {0, 1}.
32. La cadena vacía sobre {a, b}.
33. Conjunto de cadenas sobre {0, 1} que no contengan como subcadena a la cadena vacía.
34. Conjunto de cadenas sobre {0, 1} que sean palíndromos.
35. Conjunto de cadenas sobre {0, 1} que sean palíndromos de longitud menor o igual a 4.
36. Conjunto de cadenas sobre {0, 1} que no contengan como prefijo a 0 ni a 1.
37. Conjunto de cadenas sobre {0, 1} de la forma 0n 12n.
38. Conjunto de cadenas sobre {a, b, c, d} de la forma  wn xm con n<>m, w en {a, b}* y x en {c, d}*.
39. Conjunto de cadenas sobre {a, b} de longitud menor o igual a 3 que no sean palíndromos.
40. Conjunto de cadenas sobre {0, 1, 2} de la forma w2w, donde w es una secuencia de ceros y unos.
41. Conjunto de cadenas sobre {a, b} donde por cada a existen dos o más b.
42. Conjunto de cadenas sobre {a, b, c, d} en las que no existan a y b adyacentes.
Año 2015 1

<!-- página 2 -->

PPARADIGMASARADIGMAS  YY L LENGUAJESENGUAJES
43. Conjunto de cadenas sobre {0, 1} que contengan las subcadenas 01 y 10 a la vez, en cualquier lugar, o las
cadenas que no terminen en 11 y comiencen con 00 a la vez.
44. Conjunto de cadenas sobre {a, b} donde para cada a de la cadena exista una b posterior.
45. Conjunto de cadenas sobre {a, b, c} que no contengan más de dos símbolos iguales consecutivos.
46. Conjunto de cadenas sobre {a, b, c} que no posean ninguna b entre una a y una c consecutivas.
47. Conjunto de cadenas sobre {0, 1} que no contengan a 0 ni a 1 como subcadenas.
48. Conjunto de cadenas sobre {a, b} donde la cantidad de a más el doble de la cantidad de b sea igual a 5.
49. Conjunto de cadenas sobre {0, 1}, que contengan al menos un par de 1 consecutivos, y a lo sumo un par de
0 consecutivos.
50. Conjunto de cadenas sobre { a, b}, donde la paridad de la cantidad de b sea la misma que la paridad de la
longitud de la cadena.
51. Conjunto de cadenas sobre {0, 1, 2, 3} de la forma ws con w en {0, 2}n; s en {1, 3}*; n <3 y |ws| par.
52. Conjunto de cadenas sobre {a, b} que no contengan la subcadena abb o que sean de longitud múltiplo de 3.
53. Conjunto de cadenas sobre {0, 1} que no contengan la subcadena 101 y que tengan longitud par.
54. Conjunto de cadenas sobre {a, b, c, d}, de la forma xw con x en {a, b}n; w en {c, d}m; n impar y m<>2.
55. Conjunto de cadenas sobre {a, b, c}, que contengan no mas de dos b y no mas de dos c.
56. Conjunto de cadenas sobre { 0, 1, 2} que no contengan como subcadena a 012, y siempre contengan al
menos un 0 o dos 1 (en cualquier lugar).
57. Conjunto de cadenas sobre {0, 1} de la forma xwx, donde x y w en {0, 1}+.
58. Conjunto de cadenas sobre {0, 1, 2} en las cuales toda subcadena contenga al menos un 2.
59. Conjunto de cadenas sobre {a, b, c, d}, de la forma xwx con x en {a, b}2; w en {c, d}+.
60. Conjunto de cadenas sobre {a, b, c}, donde toda subcadena de longitud 3 contenga al menos una a.
61. Conjunto de cadenas sobre {a, b, c} que comiencen con ab o con c,  que contengan ca, que no contengan
cab y donde todo sufijo de longitud 3, posea al menos una b.
62. Conjunto de cadenas sobre {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} que representen números primos (en base diez).
63. Conjunto de cadenas sobre {0, 1} que representen potencias de 2 o números impares (en binario).
64. Conjunto de cadenas sobre {a, b, c, d}, de la forma xw con x en {a, b}n; w en {c, d}m; n impar y m<>2.
65. Conjunto de cadenas sobre {a, b, c}, que contengan no mas de dos b y no mas de dos c.
66. Conjunto de cadenas sobre { a, b}, que comiencen y terminen con a, con cantidad impar de a, y longitud
par.
67. Conjunto de cadenas sobre {a, b}, que contengan al menos una subcadena de la forma bnan con n>1.
68. Conjunto de cadenas sobre {a, b, c} que no contengan repeticiones consecutivas del mismo símbolo, ni la
subcadena bc.
69. Conjunto de cadenas sobre {0, 1} de la forma 0 n1m, donde n=(3x+1), con x>0, y m es impar.
70. Conjunto de cadenas sobre {0, 1} que no comiencen con 01 y que tengan longitud distinta de 3.
71. Conjunto de cadenas sobre { 0, 1}, que no contengan 01, que comiencen con 11 y donde todo prefijo de
longitud par tiene más 1 que 0.
72. Conjunto de cadenas sobre {a, b}, que no contengan ningún posfijo con mayor cantidad de b que de a.
73. Conjunto de cadenas sobre {a, b, c} con cantidad par de a, impar de b, y la cantidad de a más la cantidad
de b igual a la cantidad de c.
74. Conjunto de cadenas sobre {a, b} de longitud múltiplo de 3 pero no de 2, o de longitud múltiplo de 4.
75. Conjunto de cadenas sobre {a, b, c} que contengan ab o ca, y terminen en bc o aa.
76. Conjunto de cadenas sobre {a, b} que contengan menor cantidad de a que de b, o que comiencen con b.
77. Conjunto de cadenas sobre {0, 1, 2}, que no contengan 21 y que tengan más de un 0.
78. Conjunto de cadenas sobre {a, b, c} de longitud igual a (3n+2), con n>=0.
79. Conjunto de cadenas sobre {a, b} de la forma anbn (con n>0), o que comiencen con a y terminen con bbb.
80. Conjunto de cadenas sobre {a, b} que no contengan ni abba, ni baab.
B. Seleccionar diez AF del punto anterior y construir las ERs correspondientes utilizando el
procedimiento de transformación de ER a AF.
Año 2015 2

<!-- página 3 -->

PPARADIGMASARADIGMAS  YY L LENGUAJESENGUAJES
C. Transformar las siguientes Expresiones Regulares en AFN- y graficar sus tablas de transición
1)  0 (0 | 1) * 0
2)  (( | 0 ) 1 *)*
3)  ( c* )*
4)  0* 1 0* 1 0* 1 0*
5)  a* (b | c )*
6)  (((a | b ) | c ) | d )
7)  u(( n ( it | til )) | ses)
8)  (0 | 1 ) 0 (0 | 1) (0 | 1)
9)  (a | (b | )* a*a | b(ba)* )*
D. Construir a partir de las expresiones regulares, el AFD mínimo
1)  ( ab | b) | a*
2)  a ( cd )* ( bc | b) ca
3)  (a | b ) (ba | ca )* | (cd | db)
4)  (( aa ) | (bb) | ( ca ) | (cb))*
5)  dd* ( ddd* | e ( mir ) d* )
6)  a ( b | c ) | b | c ( b | a)
7)  (( a* | b*) *) *
8)  ((( ab* |  b) * (b ( a | )) * ) * a)
E. Construir una ER, transformar en AFN-e, transformar en AF y minimizar los siguientes lenguajes
1. Conjunto de cadenas de longitud mayor a 0 sobre {x, y} tales que, si comienzan con y, deben terminar con
x.
2. Conjunto de cadenas sobre {a, s} que no posean dos s o dos a consecutivas.
3. Conjunto de cadenas sobre {e, b} que contenga como subcadena a bee o a beb.
4. Conjunto de cadenas sobre {a, b}  que comiencen y terminen con el mismo símbolo, de longitud mayor o
igual a 3.
5. Conjunto de cadenas sobre {a, b, c} que comienzan con ab o terminan con ba.
6. Conjunto de cadenas sobre {a, b} de longitud mayor o igual a 2 o igual a 0.
Año 2015 3
