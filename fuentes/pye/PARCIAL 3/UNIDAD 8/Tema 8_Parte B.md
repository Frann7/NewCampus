# Tema 8_Parte B

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PYE/PARCIAL 3/UNIDAD 8/Tema 8_Parte B.pdf` · 20 página(s) · texto extraído con pypdf.
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
| 17 |  |
| 18 |  |
| 19 |  |
| 20 |  |

<!-- página 1 -->

P x1 − x2 − Zα 2
σ1
n1
+ σ2
n2
 < μ1 −  μ2 < x1 − x2 + Zα 2
σ1
n1
+ σ2
n2
 = 1 − α
Diferencia de Medias Muestrales
a) Caso σ1 y σ2 son conocidos:
Se presenta el caso en que es necesario estimar la diferencia de las medias
poblacionales. Si se cuenta con dos muestras, se pueden presentar varios casos:
Se puede construir la variable normalizada Z:
~N(0,1) Z =
x1 − x2 − μx1−x2
σx1−x2
= x1 − x2 − μ1 − μ2
1
n1
σ1 + 1
n2
σ2

Visto anteriormente
Se puede plantear que las medias poblacionales sean iguales  μ1 − μ2 = 0  o que las
mismas difieran en una cantidad Y : μ1 − μ2 = Y
Para el método de estimación por IC:
2 2
2 2 2 2
P −Zα 2 < Z <  Zα 2 = 1 − α

<!-- página 2 -->

b) Caso σ1 y σ2 son desconocidos y se sabe que σ1 ≠ σ2:
T = x1 − x2 − μ1 − μ2
1
n1
S1 + 1
n2
S2

2 2 ~t(0, ν)
Para el método de estimación por IC:
El problema radica en elegir cuál de los  ν  utilizar ya que tenemos dos muestras:
                                                                  ν1 y ν2
Se utiliza un valor de grados de libertad ponderado entre ambas muestras:
νp =
S1 n1 + S2 n2
2
S1 n1
2
ν1
+
S2 n2
2
ν2

2 2
2 2
tomar el valor entero
más próximo
P x1 − x2 − tα 2
S1
n1
+ S2
n2
 < μ1 −  μ2 < x1 − x2 + tα 2
S1
n1
+ S2
n2
 = 1 − α
2 2 2 2

<!-- página 3 -->

c) Caso σ1 y σ2 son desconocidos pero σ1 = σ2:
También utilizamos la   ~t 0, ν : Construimos una variable T = x − μ
S
n
= Z
V ν

con V = ν. S2
σ2  Que sigue una  ~χ2 ν, α .  En este caso de diferencia de medias
V = ν1S1
σ1
+ ν2S2
σ2

2 2
2 2 y ν = ν1 + ν2 De esta forma:
T = x1 − x2 − μ1 − μ2
σ 1
n1
+ 1
n2

. 1
ν1S1
σ2 + ν2S2
σ2 . 1
ν1 + ν2
 2 2
Sp
T = x1 − x2 − μ1 − μ2
Sp
1
n1
+ 1
n2

 Con:  Sp = ν1S1 + ν2S2
ν1 + ν2

2 2
2

<!-- página 4 -->

Para el método de estimación por IC:
P x1 − x2 − tα 2 Sp
1
n1
+ 1
n2
 < μ1 −  μ2 < x1 − x2 + tα 2 Sp
1
n1
+ 1
n2
 = 1 − α
Ejemplo 2:  Dos muestras de la concentración de Fósforo en el río se toman en dos lugares
diferentes, uno corriente arriba y otro corriente debajo de una fábrica química.

a) Encontrar un intervalo de confianza del 95% para μ1 − μ2  suponiendo ~N μ, σ  y
σ1  ≠ σ2
b) Comparar la hipótesis μ1 = μ2 con un 95% de confianza.
n x  mg
l  S mg
l
M 1 Corriente
abajo
15 3,84 3,07
M 2 Corriente
arriba
12 1,49 0,80
M 1 M 2

<!-- página 5 -->

Corresponde al caso (b) σ1 y σ2 son desconocidos y se sabe que σ1 ≠ σ2
Calculo el grado de libertad ponderado:
νp =
S1 n1 + S2 n2
2
S1 n1
2
ν1
+
S2 n2
2
ν2
= 16,3 ≅ 16
x1 − x2 = 3,48 − 1,49 = 2,35 mg
l       ;
P x1 − x2 − tα 2
S1
n1
+ S2
n2
 < μ1 −  μ2 < x1 − x2 + tα 2
S1
n1
+ S2
n2
 = 1 − α
2 2 2 2
2 2
2 2
S1
n1
+ S2
n2
 = 0,826 mg
l
2 2
tα 2 = t0,025 = 2,12  con νp = 16
IC = 0,6 < μ1 − μ2 < 4,10  Con un 95% de confianza
¿ A qué caso de los vistos corresponde ?
Tabla A.4

<!-- página 6 -->

b) Comparar la hipótesis μ1 = μ2 con un 95% de confianza. Estimación puntual
T = x1 − x2 − μ1 − μ2
1
n1
S1 + 1
n2
S2

= 0
T = x1 − x2
1
n1
S1 + 1
n2
S2
= 2,35
0,826 = 2,845
P −tα 2 < T < tα 2 = 0,95
P −2,12 < 2,845 < 2,12 = 0,95 2,845 está fuera del intervalo
No puede afirmarse: μ1 = μ2
2,12 -2,12 T = 2,85 μ1 = μ2
2 2
2 2
CONTAMINA
Ahora vemos para qué sirve la estimación por IC y la Estimación Puntual

<!-- página 7 -->

Estimación de proporciones Muy utilizado en encuestas
Sea un experimento binomial  variable dicotómica Éxito
Fracaso
Un estimador puntual de V.A. x ~b x; n, p = n
x pxqn−x es: P = x
n
Con x = número de éxitos (o fracasos)  y  n = número de pruebas.
La proporción P = x n  de la muestra de V.A. x se utilizará como estimador
puntual de p que representa la proporción de la población.
Si no se espera que p (desconocida) esté demasiado cerca de 0 (fracaso) o 1
(éxito) se puede establecer un IC considerando la distribución muestral P .
¿ Por qué ponemos esta restricción ?

<!-- página 8 -->

Si n → ∞ vimos que ~b → ~N μ, σ :
μP = E P = E x
n = 1
n E x = 1
n . np = p
Z = P − μP
σP

σP = σx n =
2 2 1
n2 σx = npq
n2 = pq
n  2
V ax + b = a2V(x)
Usando la aproximación normal de la binomial:
P −Zα 2 < Z <  Zα 2 = 1 − α Con  Z = P − p
pq
n

<!-- página 9 -->

Para construir un estimador por IC:
P P − Zα 2
pq
n  < p < P + Zα 2
pq
n  = 1 − α
Problema !!! Los extremos del intervalo dependen de p (desconocida)
Si n → ∞ el error de sustituir P  por p es pequeño.
P P − Zα 2
P Q
n  < p < P + Zα 2
P Q
n  = 1 − α
Con las condiciones:      n   grande
                                           p ≫ 0   y   p ≪ 1

<!-- página 10 -->

Al igual que en los casos anteriores de estimación puntual de parámetros
poblacionales:  P ≠ p y por lo tanto se comete un error de estimación puntual.
Error = p − P
Con el método de estimación por IC se puede calcular el Error de Estimación
Puntual con un nivel de confianza 1 − α .
e = Zα 2
P Q
n
Determinemos ahora el tamaño de la muestra para asegurar, con un 1 − α %, un
determinado valor de e:
n =
Zα 2
e
2
P Q
Aquí el problema es que P  depende de n.
Se toma primeramente una muestra de n ≥ 30 para
calcular P , luego con P  se estima n para obtener un
error especificado.
P = x
n

<!-- página 11 -->

Dos muestras: Estimación de la diferencia de proporciones
Estimar la diferencia de dos proporciones   p1  y  p2
Se calcula P 1 =
x1
n1
    y P 2 =
x2
n2
  a partir de dos muestras de tamaño n1 y  n2
La diferencia de proporciones muestrales P 1 − P 2 se utilizará para estimar la
diferencia de proporciones poblacionales p1 − p2
Al ser P 1 y  P 2 independientes, es posible utilizar la ~N μ, σ  para la diferencia.
μP 1−P 2 = p1 − p2
σP 1−P 2 = p1q1
n1
+ p2q2
n2

2

<!-- página 12 -->

Por lo tanto:
P −Zα 2 < Z <  Zα 2 = 1 − α con Z = P 1 − P 2 − p1 − p2
p1q1
n1
+ p2q2
n2

Para construir   IC   se sustituye Z
P P 1 − P 2 − Zα 2
p1q1
n1
+ p2q2
n2
 < p1 − p2 < P 1 − P 2 + Zα 2
p1q1
n1
+ p2q2
n2
 = 1 − α
En las que p1, q1,  p2  y  q2  pueden ser sustituidas por  P 1 , Q 1,  P 2  y   Q 2   siempre que:
n   grande
                      y         p ≫ 0   y   p ≪ 1

<!-- página 13 -->

Estimación de la Varianza por IC
En el método de estimación puntual habíamos visto que para estimar σ2 a
partir de S2 se utiliza la ~χ2 con ν = (n − 1) grados de libertad.
La V.A.  V = ν. S2
σ2  tiene ~χ2
Si x ~N(μ, σ)
Para aceptar o rechazar la hipótesis de que la muestra de varianza S2 provenga
de una población de varianza σ2:
1. Elegimos α.
2. Calculamos V.
3. Encontramos Vα.
4. Comparamos V con Vα.
5. Decidimos aceptar o rechazar la hipótesis.

<!-- página 14 -->

Ahora nos proponemos estimar σ2 a partir de S2 con (1 − α) nivel de
confianza por IC:
Es decir, planteamos la probabilidad por IC
P V1−α 2 < V < Vα 2 = 1 − α Bilateral

<!-- página 15 -->

P V1−α 2 < ν. S2
σ2 < Vα 2 = 1 − α Dividiendo m.a.m. por ν. S2
P
V1−α 2
ν. S2 < 1
σ2 <
Vα 2
ν. S2 = 1 − α Invertimos las desigualdades
P ν. S2
Vα 2
< σ2 < ν. S2
 V1−α 2
= 1 − α
V
Tiene que quedar S2  al medio

<!-- página 16 -->

Ejemplo 3: Encuentre un IC del 95% para la varianza de todos los paquetes de
semillas que se distribuyen en una empresa agrícola suponiendo distribución
normal de los pesos de esos paquetes.
Pesos en Kg de una muestra de 10 paquetes:  464, 461, 458, 470, 461, 459, 458, 469, 452, 460
S2 = n.  xi
2 −  xi
n
1
2n
1
n. n − 1 = 10.2127312 − 46122
10.9 = 2576
90 = 28,62
Elegimos α = 0,05 y de la Tabla A.5 usando ν = 9 encontramos:
Vα 2 = V0,025 = 19,023 y V1−α 2 = V0,975 = 2,700
Por lo tanto el IC es:  IC = 9.28,62
19,023 ; 9.28,62
2,700  IC = ν. S2
Vα 2
; ν. S2
 V1−α 2

IC = 13,542 ;  95, 407
P 13,542 < σ2 < 95, 407 = 0.95

<!-- página 17 -->

Dos muestras: Estimación de la razón de Varianzas por IC
Como antes, hacemos uso de la ~f para estimar la razón de varianzas
F =
U ν1
V ν2

Con U y V dos V.A. independientes donde ambas tienen
~χ2 con ν1 grados de libertad para U y ν2 grados de libertad
para V.
Esta distribución nos ayuda a determinar con cierta probabilidad si S1
2 y S2
2
provenían de muestras de la misma población.
Ahora estamos interesados en estimar la razón de dos varianzas
poblacionales σ1
2 y σ2
2 a partir de muestras de varianzas S1
2 y S2
2 con (1 − α)
nivel de confianza utilizando IC
Se plantea entonces la Probabilidad de forma bilateral:
P f1−α 2 ν1, ν2 < F < fα 2 ν1, ν2 = 1 − α

<!-- página 18 -->

P f1−α 2 ν1, ν2 < F < fα 2 ν1, ν2 = 1 − α Con   F =
U ν1
V ν2
 =
S1
2
σ1
2
S2
2
σ2
2
= σ2
2. S1
2
σ1
2. S2
2
P f1−α 2 ν1, ν2 < σ2
2. S1
2
σ1
2. S2
2 < fα 2 ν1, ν2 = 1 − α Multiplicando m.a.m.S22
S12
P S2
2
S1
2 . f1−α 2 ν1, ν2 < σ2
2
σ1
2 < S2
2
S1
2 . fα 2 ν1, ν2 = 1 − α Invirtiendo las desigualdades
P S1
2
S2
2 . 1
fα 2 ν1, ν2
< σ1
2
σ2
2 < S1
2
S2
2 . 1
f1−α 2 ν1, ν2
= 1 − α

<!-- página 19 -->

P S1
2
S2
2 . 1
fα 2 ν1, ν2
< σ1
2
σ2
2 < S1
2
S2
2 . 1
f1−α 2 ν1, ν2
= 1 − α
Pero también puede ser expresada de otra forma sabiendo que:
f1−α ν1, ν2 =  1
fα ν2, ν1

P S1
2
S2
2 . 1
fα 2 ν1, ν2
< σ1
2
σ2
2 < S1
2
S2
2 . fα 2 ν2, ν1 = 1 − α

<!-- página 20 -->

Ejemplo 4:  Del Ejemplo 2 donde dos muestras de la concentración de Fósforo en el río se
toman en dos lugares diferentes, uno corriente arriba y otro corriente abajo de una fábrica
química. Suponiendo que las variables de concentración de fósforo en el río siguen
distribuciones normales, la razón de las varianzas muestrales S12
S22   es calculada y utilizada para
estimar la razón de las varianzas poblacionales de concentración de fósforo por IC. Con este
criterio mostrar que las varianzas poblacionales son distintas con un nivel de confianza del 98%
n x  mg
l  S mg
l
Muestra 1 Corriente abajo 15 3,84 3,07
Muestra 2 Corriente arriba 12 1,49 0,80
Solución: Con 1 − α = 0,98 → α = 0,02
De Tabla A.6: →
fα 2 ν1, ν2 = f0,01(14,11) = 4,30
fα 2 ν2, ν1 = f0,01 11,14 = 3,87
IC = 3,072
0,802 . 1
4,30 < σ1
2
σ2
2 < 3,072
0,802 . 3,87 = 1,851; 7,549
P S1
2
S2
2 . 1
fα 2 ν1, ν2
< σ1
2
σ2
2 < S1
2
S2
2 . fα 2 ν2, ν1 = 1 − α
Este IC  no
contiene el
cociente = 1
