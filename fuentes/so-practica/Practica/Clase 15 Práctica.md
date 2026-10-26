# Clase 15 Práctica

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Clase 15 Práctica.pdf` · 26 página(s) · texto extraído con pypdf.
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
| 9 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 10 |  |
| 11 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 12 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 13 |  |
| 14 |  |
| 15 |  |
| 16 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 17 |  |
| 18 |  |
| 19 |  |
| 20 |  |
| 21 |  |
| 22 |  |
| 23 |  |
| 24 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 25 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 26 |  |

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
exequiel.aramburu@uader.edu.ar
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Análisis de resultados del EI1.
● Presentación de la actividad extra aúlica de la clase pasada.
● Introducción al área de intercambio.
● Visualizar el tamaño/uso de swap con free/htop/top en GNU/Linux de consola.
● Visualizar el tamaño/uso de swap  en GNU/Linux con herramientas graficas.
● Visualizar y configurar de la swap utilizando swappines,swapoff, swapon y mkswap.
● Crear una swap de tipo archivo e incoporarla al S.O.
● Visualizar el tamaño/uso de swap  del S.O en Microsoft Windows.
● Actividad extra aúlica. Visualizar y administrar el área de intercambio
del S.O en Microsoft Windows.

<!-- página 3 -->

Análisis de resultados EI1

<!-- página 4 -->

Análisis de resultados EI1

<!-- página 5 -->

Análisis de resultados EI1

<!-- página 6 -->

Análisis de resultados EI1

<!-- página 7 -->

Análisis de resultados EI1

<!-- página 8 -->

https://wiki.debian.org/Swap Fuente:

<!-- página 9 -->

M2

<!-- página 10 -->

free – muestra la utilización de memoria del sistema
Sintaxis:
free <opciones>
Ejemplos:
$ free -tm
$ free -s 2
$ free -hw

<!-- página 11 -->

Htop
free

<!-- página 12 -->

GParted

<!-- página 13 -->

La cantidad recomendada de espacio de intercambio ha sido tradicionalmente el
doble de la cantidad de memoria del sistema. Esto ha cambiado con el tiempo a una
vez y media la memoria del sistema, ambas respuestas son líneas de base
decentes pero se están volviendo cada vez menos respuestas útiles a la pregunta a
medida que pasa el tiempo. Hay muchas variables sobre su sistema y el uso
previsto que determinarán el intercambio de sistema disponible que querrá tener.
Tamaño del Área de Intercambio
https://wiki.debian.org/Swap Fuente:

<!-- página 14 -->

● ¿Tiene la intención de utilizar las funciones de hibernación y suspensión?
Si tiene la intención de usar cualquiera de los dos, deberá asegurarse de que su espacio de intercambio disponible
sea lo suficientemente grande como para contener toda la información que su sistema en ejecución tendrá en la
RAM. Si tiene la intención de utilizar Hibernate, debe asegurarse de que su instalación de Debian tenga acceso a
una partición o archivo de intercambio que NO se comparta con otra instancia de GNU/Linux.
● ¿Cuánta memoria tiene tu máquina?
Si su máquina tiene una gran cantidad de RAM disponible y no necesita Hibernar o Suspender, entonces será más
seguro tener menos intercambio disponible para el sistema. Si su máquina tiene muy poca memoria RAM
disponible, como en el caso de las máquinas más antiguas y las netbooks, debe asegurarse de crear un espacio
de intercambio que sea lo suficientemente grande. Duplicar la memoria del sistema sería una buena sugerencia en
este caso.
● ¿Cuánta memoria ocuparán las aplicaciones que pretende ejecutar?
 El uso de memoria de un sistema Debian GNU/Linux variará mucho según las aplicaciones que elija ejecutar. Por
ejemplo, ejecutar un entorno de escritorio más ligero como Openbox o Xfce y sus aplicaciones asociadas utilizará
menos memoria que GNOME o KDE.
● ¿Cuánto disco duro tienes disponible?
Si usa un disco de estado sólido pequeño o una llave USB para la instalación de Debian, este espacio en el disco
duro puede ser escaso. En tales casos, podría tener más sentido instalar más memoria del sistema si es necesario
que usar un gran espacio de intercambio. Esto también tiene la ventaja de acelerar el sistema, ya que la velocidad
de lectura/escritura de los discos duros es mucho más lenta que la de la RAM.

<!-- página 15 -->

swappiness
Swappiness es una propiedad del Núcleo Linux que permite ajustar el equilibrio
entre el uso del Espacio de intercambio (swap en inglés, por eso el nombre de la
propiedad) y la Memoria de acceso aleatorio (RAM). El swappiness puede tomar
valores desde el 0 hasta el 100. Si se establece 0 el núcleo intentará no hacer
intercambio, mientras que si se establece 100 el sistema intentará mantener la
Memoria de acceso aleatorio lo más libre posible haciendo intercambio.
El valor por efecto en la mayoría de distribuciones suele ser de 60, pero si, por
ejemplo, se quisiera establecer su valor a 10, se puede lograr como administrador
con la siguiente orden:
echo 10 > /proc/sys/vm/swappiness
 Modificar el valor (Este efecto dura mientras el sistema esté activo. Para que el cambio sea
persistente entre reinicios, se establece el valor de la variable vm.swappiness en el archivo
/etc/sysctl.conf):

<!-- página 16 -->

Swappiness
0-100

<!-- página 17 -->

Para habilitar todas las áreas de intercambioswapon -a
Para deshabilitar todas las áreas de intercambioswapoff -a
swapon
 Lista  la swap disponibles con sus tamaños y prioridad

<!-- página 18 -->

Para habilitar todas las áreas de intercambioswapon -a
Para deshabilitar todas las áreas de intercambioswapoff -a
swapon
swapon -s
Lista  la swap disponibles con sus tamaños y prioridad
Lista  la swap disponibles y el tipo (archivo/partición)

<!-- página 19 -->

dd if=/dev/zero of=/var/swap bs=4096k count=256
Incorporamos otra swap de tipo archivo
Creamos el archivo de 1GB con el comando dd:
Establecemos permisos limitados (por seguridad):
chmod 600 /var/swap

<!-- página 20 -->

Incorporamos una swap de tipo archivo
Establecemos el formato con mkswap:
mkswap /var/swap
swapon /var/swap
Incorporamos el archivo a la swap

<!-- página 21 -->

Práctica de Laboratorio 1
Ejecute una terminal
Identifique y analice el tamaño de la memoria SWAP utilizando
estos 3 comandos:
* htop
* free -h
* swapon
1
2
Identificar el tamaño de la memoria SWAP:
3 Identifique la configuración del swappiness
cat /proc/sys/vm/swappiness

<!-- página 22 -->

Práctica de Laboratorio 2
Ejecute dos terminales(1 y 2)
Desactive la memoria swap desde terminal 2 y visualice e
identifique si deshabilito la swap en la terminal 1.
swapoff -a
1
2
Activando y desactivando la SWAP
3
Active la memoria swap utilizando la terminal 2 y visualice la
terminal 1.
swapon -a
4
Ejecute htop en la terminal 1

<!-- página 23 -->

Práctica de Laboratorio 3
Ejecute una terminal1
2
Incorporar una swap de tipo archivo al S.O
3
Listar las swap disponibles con el comando:
swapon
4
Cree un archivo de 1GB para ser utilizado como swap y asigne
permisos:
1) dd if=/dev/zero of=/var/swap bs=4096k count=256
2) chmod 600 /var/swap
1) mkswap /var/swap
2) swapon /var/swap
Establezca el formato e incorpore a la swap el archivo.

<!-- página 24 -->

Windows+R ->

<!-- página 25 -->

pagefile.sys

<!-- página 26 -->

Actividad extra aúlica
GRUPO  7
GRUPO 1
GRUPO 2
GRUPO 3
GRUPO 4
GRUPO 5
GRUPO 6
GRUPO 7
GRUPO 8
GRUPO 9
GRUPO 10
Aleatorio
1)Comentar las diferentes opciones existentes de
configuración de la Memoria Virtual.
2)Establecer sin archivo de paginación.
3)Forzar al S.O que agote la memoria RAM existente.
4)Mostrar lo que sucede y explicar el motivo.
