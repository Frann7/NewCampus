# Clase 16 Práctica

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Clase 16 Práctica.pdf` · 20 página(s) · texto extraído con pypdf.
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

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
exequiel.aramburu@uader.edu.ar
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Presentación de la actividad extra aúlica de la clase pasada.
● Jerarquía de memoria.
● Introducción a la Memoria cache. Identificar la memoria cache L1, L2, L3.
Práctica de laboratorio utilizando el comando lscpu.
● Introducción a la Memoria RAM y los conceptos de Bufferd, shared y cache.
● Comandos para identificar la memoria RAM y su consumo.
Práctica de laboratorio utilizando los comandos: htop, free y syns.
● Liberar memoria cache. Práctica de laboratorio con ejemplo de memoria cache.
● Introducción a RAMDisk. Práctica de laboratorio Crear RAM Disk con tmpfs.
● Actividad extra aúlica. Visualizar las memorias L1,L2,L3 y cache en el S.O en Microsoft Windows.

<!-- página 3 -->

JERARQUÍA DE MEMORIA
El sistema de memoria está construido como una jerarquía de capas. Las capas superiores
tienen mayor velocidad, menor capacidad y mayor costo por bit que las capas inferiores, a
menudo por factores de mil millones o más.
Fuente: Tanenbaum, A., Stallings, W., & Kerrish, M. (2009). Sistemas Operativos modernos., 3ra edición.

<!-- página 4 -->

                    MEMORIA RAM (DDR3 / DDR4 / DDR 5)
Discos  (HDD / SDD / M2)
Cintas
SWAP
Disk
Cache
C
A
P
A
C
I
D
A
D
 V
E
L
O
C
I
D
A
D
C
O
S
T
O
JERARQUÍA DE MEMORIA

<!-- página 5 -->

L1/L2
Por Nucleo
L3: Compartida
MEMORIA CACHE L1, L2 y L3

<!-- página 6 -->

MEMORIA CACHE L1, L2 y L3 – Velocidades y Latencia

<!-- página 7 -->

lscpu
12Mb CompartidaTotal
6 (núcleos) x256kb = 1,5 Mb
6 (núcleos) x 32kb = 192 kb
6 (núcleos) x 32kb = 192 kb
384 kb
L1
L2
L3

<!-- página 8 -->

HTOP – Análisis de la Memoria RAM
¿Que significan los colores?

<!-- página 9 -->

Buffer/Shared/cache
Cache: El almacenamiento en caché es el proceso de almacenar temporalmente una copia de un recurso determinado
para que las solicitudes posteriores al mismo recurso se procesen más rápido
Buffer: es un área de almacenamiento temporal en la memoria principal (RAM) que almacena la transferencia de datos entre dos
o más dispositivos o entre una aplicación y un dispositivo. El almacenamiento en búfer compensa la diferencia en las velocidades
de transferencia entre el remitente y el receptor de los datos.
Shared: La memoria compartida, permite que dos o más procesos compartan una zona común de memoria, representa
la forma más rápida de IPC , debido a que no hay ningún tráfico entre cliente/servidor, si no que todo el acceso es
directo a la memoria.

<!-- página 10 -->

Buffer/Shared/cache
cache UsadoBufferd SharedUsado

<!-- página 11 -->

CPU-X – Memoria RAM
Cache Antes Cache Después

<!-- página 12 -->

De forma predeterminada, el kernel de Linux escribe datos en el disco de forma asíncrona.
Las escrituras se almacenan en búfer (caché) en la memoria y se escriben en el dispositivo
de almacenamiento en el momento óptimo. El comando de sincronización fuerza una
escritura inmediata de todos los datos almacenados en caché en el disco.
Ejecute la sincronización si prevé que el sistema sea inestable o que el dispositivo de
almacenamiento deje de estar disponible repentinamente y desea asegurarse de que todos
los datos se escriban en el disco.
Se pueden sincronizar archivos individuales o todo el sistema de archivos que contiene los
archivos especificados. Si no se proporcionan argumentos , se sincronizan todos los
sistemas de archivos montados.
# sync
Comando sync

<!-- página 13 -->

Cada sistema Linux tiene tres opciones para borrar el caché sin interrumpir ningún proceso o
servicio.
1. Borre PageCache únicamente.
# sync; echo 1 > /proc/sys/vm/drop_caches
2. Borrar Dentries e inodos.
# sync; echo 2 > /proc/sys/vm/drop_caches
3. Borrar caché de página, dentries e inodos.
# sync; echo 3 > /proc/sys/vm/drop_caches
¿Cómo borrar el caché en Linux?

<!-- página 14 -->

RAM Disk – Utilizando tmpfs
mkdir /tmp/ramdisk
mount -t tmpfs -o size=16G tmpfs /tmp/ramdisk
IMPORTANTE: Los datos desaparecerán cuando reinicies o apagues el equipo, puesto que la RAM es una
memoria volátil. Por eso, lo que quieras conservar, hazle una copia en una partición del disco duro.
Crear un directorio vació
Directorio de montado
de la RAM Disk
FileSystem Tamaño
1
2
Tmpfs es un sistema de archivos que guarda todos sus archivos en la memoria virtual. Dado que tmpfs vive
completamente en la memoria caché de la página y en el intercambio, todas las páginas de tmpfs se mostrarán
como "Shmem" en /proc/meminfo y shared (compartido en español) en free.

<!-- página 15 -->

Práctica de Laboratorio 1
Ejecute una terminal
Identifique y anote el tamaño de la memoria cache del CPU
(L1,L2 y L3) utilizando el comando:
* lscpu
1
2
Identificar el tamaño de la memoria L1,L2,L3:
Nota: Complete la tabla expuesta en la diapositiva 18, con el
resultado.

<!-- página 16 -->

Práctica de Laboratorio 2
Ejecute una terminal.
Copie algunos archivos y luego identifique el tamaño de la
memoria RAM: Total, Usada, Shared,B uffer,Cache y
Disponible. Utilizando el siguiente comando:
# free -wm
1
2
Identificar la RAM utilizada:
Nota: Complete la tabla expuesta en la diapositiva 18, con el
resultado.

<!-- página 17 -->

Práctica de Laboratorio 3
Ejecute una terminal
Borre la cache de la RAM utilizando el siguiente comando
como root:
# sync; echo 1 > /proc/sys/vm/drop_caches
1
2
Identificar la RAM Utilizada, luego del borrado de la cache.
Liste nuevamente el tamaño de la memoria RAM: Total,
Usada,  Shared, Buffer, Cache y Disponible. Anote el
resultado la tabla diapositiva 18:
3

<!-- página 18 -->

Práctica de Laboratorio 1/2/3
L1
L2 L3
D I
Tamaño 192Kb
6*32kb
192Kb
6*32kb
1,5 Mb
6*256kb
12Mb
Total Usada Libre Compartida Búfer Cache Disponible
Tamaño
(Mb)
ANTES
31912 1367 16439 61 91 14013 30020
Tamaño
(Mb)
DESPUES
31912 1344 30167 61 1 399 30114

<!-- página 19 -->

Práctica de Laboratorio 4
Ejecute una terminal
Cree un directorio y monte la RAM Disk utilizando los
siguientes comandos como root:
#mkdir /tmp/ramdisk
#mount -t tmpfs -o size=16G tmpfs /tmp/ramdisk
1
2
Crear un RAM disk con tmpfs.
Copie archivos a la RAM disk y verifique el estado de la
memoria RAM, identificando el consumo y su tipo:
# free -wm
3

<!-- página 20 -->

Actividad extra aúlica
GRUPO  X
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
1) Explicar la solapa “Rendimiento->memoria” del administrador
de tareas de S.O Microsoft Windows.
2) Visualizar la memoria cache del CPU L1,L2 y L3.
3) Luego copiar archivos grandes, y visualizar en la memoria la
cache.
4)Explicar lo que sucede.
