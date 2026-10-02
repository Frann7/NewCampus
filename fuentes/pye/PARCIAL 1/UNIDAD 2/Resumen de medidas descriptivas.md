# Resumen de medidas descriptivas

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 1/UNIDAD 2/Resumen de medidas descriptivas.pdf` · 1 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Resumen de fórmulas del Tema 2: NIC, media, cuartiles, moda, percentiles, varianza, CV, asimetría, curtosis; datos sin agrupar y agrupados. ⚠ ver el PDF: fracciones y sumatorias rotas, columnas mezcladas, y el teorema de Chebyshev (imagen) no está en el texto |

<!-- página 1 -->

Licenciatura en Sistemas de Información
Resumen de fórmulas de Tema 2

Datos sin agrupar
Datos agrupados
NIC = log10 n    o   NIC = √n, 5 ≤ NIC ≤ 15
Ancho del IC: A =
R
NIC
Medidas de posición o tendencia central
Media: X̅ =
1
n ∑ Xi
n
i=1
*Se puede obtener con Alcula. X̅ = ∑(XPMi. fri)
k
i=1

Mediana/cuartiles:
n impar:  Qk = Xk
4(n+1)  con k=1,2,3.
n par: Qk =
1
2 [X(k
4 n) + X(k
4 n+1)] con k=1,2,3
Se determina a cuál intervalo de clase pertenece el
cuartil. Es el primero que tenga Fr ≥
k
4.
Qk = Li +
k
4   −   Fr(i−1)
Fri −  Fr(i−1)
. A
con k=1,2,3
Moda: Valor de mayor frecuencia.
Se determina a cuál intervalo de clase pertenece la
moda. Es aquél con mayor fr.
Mo = Li + A
fi − f(i+1)
fi − f(i−1)
+ 1

Percentiles:
Pk = X( k
100n) con k=1,…,99
Se determina a cuál intervalo de clase pertenece el
percentil. Es el primero que tenga Fr ≥
k
100.
Pk = Li +
k
100  −  Fr(i−1)
Fri− Fr(i−1)
. A   con k=1,…,99

Medidas de dispersión
Varianza:
S2 = n ∑ Xi
2n
i=1 − (∑ Xi
n
i=1 )2
n (n − 1)
Desvío estándar: S = √S2
*Se puede obtener con Alcula.
S2 =
n ∑ XPMi
2k
i=1 . fai   − [∑ (XPMi. fai)k
i=1 ]
2
n (n − 1)

   S = √S2

Rango:
R = Xmáx − Xmín R = Xmáx − Xmín
Rango intercuartil:
IQ = Q3 − Q1 IQ = Q3 − Q1
Coeficiente de variación:
CV = S/X̅ CV = S/X̅
Medidas de forma
Asimetría:
SK = 3( X̅ − X̃)
S

SK = 3( X̅ − X̃)
S
Curtosis:
Cu = 1
n
∑ (xi − X̅ )4n
i=1
S4 − 3
