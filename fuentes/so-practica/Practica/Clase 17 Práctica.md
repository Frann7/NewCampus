# Clase 17 Práctica

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Clase 17 Práctica.pdf` · 33 página(s) · texto extraído con pypdf.
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
| 21 |  |
| 22 |  |
| 23 |  |
| 24 |  |
| 25 |  |
| 26 |  |
| 27 |  |
| 28 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 29 |  |
| 30 |  |
| 31 |  |
| 32 |  |
| 33 |  |

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
aramburu.exequiel@uader.edu.ar
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Estructura de Directorios.
● Estructura de directorio en GNU/Linux.
● Introducción a Sistemas de archivos con y sin Journaling. Tipos de Archivos.
● Analizando algunos sistemas de archivos. Ventajas y Desventajas
● Operaciones de archivos en Debian GNU/Linux o derivados.
Prácticas en laboratorio en Debian GNU/Linux:Comandos mkdir, ls, rm, cp, mv, pwd.
● Montado y desmontado de un sistema de archivos en Debian GNU/Linux o derivados.
Prácticas en laboratorio en Debian GNU/Linux:Comandos mount y umount.
● Actividad extra aúlica. Explicar la estructura de directorio y sistemas de archivos que soporta el S.O
Microsoft Windows. Mostrar comandos básicos para manipular archivos:copiar, mover, modificar y crear.

<!-- página 3 -->

Estructura de Directorios

<!-- página 4 -->

D:
E:
Jerarquía/Estructura del sistema de archivos

<!-- página 5 -->

Estándar de jerarquía del sistema de archivos
(Filesystem Hierarchy Standard - FHS)
https://refspecs.linuxfoundation.org/fhs.shtml
El estándar de jerarquía del sistema de archivos (en inglés Filesystem Hierarchy Standard,
también conocido por sus siglas FHS) es una norma que define los directorios principales y
sus contenidos en el sistema operativo GNU/Linux y otros sistemas de la familia Unix.
Se diseñó originalmente en 1994 para estandarizar el sistema de archivos de las
distribuciones de Linux, basándose en la tradicional organización de directorios de los
sistemas Unix. En 1995 se amplió el ámbito del estándar a cualquier Unix que sea
voluntariamente.
El 3 de junio de 2015 fue lanzada FHS 3.0.

<!-- página 6 -->

Estructura de directorios en GNU/Linux
Fuente: https://www.debian.org/releases/stable/amd64/apcs02.en.html

<!-- página 7 -->

Estructura de directorios en GNU/Linux
Directorio raíz del sistema. De aquí “cuelgan” todos los directorios del
sistema./
Es una abreviatura de binarios o ejecutables. Aquí se encuentran la
mayoría de los programas esenciales del sistema operativo./bin
/sbin
En este directorio encontraremos archivos que representan los diferentes
dispositivos del sistema.
/etc
Contiene todos los archivos de configuración del sistema y de cada uno de sus
programas.
/dev
Aquí encontraremos utilidades para la administración del sistema. Estas
utilidades son accesibles solamente para el root o superusuario.
Este directorio contiene los subdirectorios personales de los usuarios del
sistema. Cada usuario posee su propio directorio en el que puede almacenar
archivos personales, documentos, programas y archivos de configuración.
/home

<!-- página 8 -->

Estructura de directorios en GNU/Linux
/lib
/proc
El directorio lib posee librerías compartidas utilizadas por el sistema a la hora
de arrancar y correr comandos propios.
Los archivos que contiene residen en memoria, hacen referencia a procesos e
información del sistema.
Es la segunda mayor sección del sistema de archivo. Contiene archivos de
documentación, librerías, código fuente, binarios usados por programas que no
son del sistema.
/usr
En este directorio encontraremos datos variables como pueden ser: archivos de
logs, temporales, spool de impresión, etc.
/var
/tmp
Contiene archivos temporales del sistema. Los programas pueden escribir en
este directorio datos que necesiten mientras estén en ejecución.
/root Éste es el directorio personal de usuario root.

<!-- página 9 -->

¿Qué es un Sistema de archivos?
Es un modelo abstracto que permite manipular los
datos almacenados en un espacio de disco de una
forma determinada.
Un tratamiento consistente de la información almacenada físicamente en disco. Una jerarquía
de archivos y protección de los archivos.
¿Qué nos permite hacer un Sistema de archivos?
Es un sistema que sirve para dar mayor seguridad a la integridad de los datos que
contenemos en nuestros discos rígidos. Se recomienda para sistemas de alta disponibilidad.
¿Qué es un Sistema de archivos con Journaling?

<!-- página 10 -->

Algunos Sistema de archivos sin Journaling
FAT (12/16/32)
Diseñado por Bill Gates y Marc McDowland en 1977. Desarrollado para DOS/Windows. El
tamaño máximo de un archivo en FAT32 es 4 GB.
Ext2
Diseñado originalmente por Rémy Card. Desarrollado para GNU/Linux. Los límites son un
máximo de 2 TB de archivo, y de 4 TB de partición.

<!-- página 11 -->

Algunos  Sistema de archivos con Journaling
ext3
Diseñado por la Comunidad de Software Libre. Desarrollado para GNU/Linux. Los límites son
un máximo de 2 TB de archivo, y de 16 TB de partición.
ReiserFS
Diseñado por la empresa Namesys, liderado por Hans Reiser. Desarrollado para GNU/Linux.
Los límites son un máximo de 8 TB de archivo, y de 16 TB de partición.
XFS
Diseñado por la empresa SGI. Desarrollado para Unix IRIX y GNU/Linux. Los límites son un
máximo de 8 EB de archivo, y de 9 EB de partición.
JFS
Diseñado por por la empresa IBM. Desarrollado para Unix AIX y GNU/Linux. El tamaño
máximo de partición va de 512 TB hasta 4 PB (en función del block size).
NTFS
Diseñado por Microsoft. Desarrollado para Windows NT/2000/XP/Vista. Los límites son un
máximo de 16 TB de archivo, y de 256 TB de partición.

<!-- página 12 -->

Algunos  Sistema de archivos con Journaling
ext4
Diseñado por Mingming Cao, Dave Kleikamp, Alex Tomas, Andrew Morton y otros
programadores. Desarrollado para GNU/Linux. Los límites son un máximo de 16 TB de
archivo, y de 1 EB de partición. Deja de ser experimental en la versión de Kernel 2.6.28.

<!-- página 13 -->

https://en.wikipedia.org/wiki/Comparison_of_file_systems
https://docs.microsoft.com/es-es/windows/win32/fileio/filesystem-functionality-comparison
Otros  sistemas de archivos:
Wikipedia:
Microsoft:

<!-- página 14 -->

Gparted
Soporte para sistemas de archivos

<!-- página 15 -->

 apt install reiser4progs
Incorporando Soporte
  para el FS → reiser4

<!-- página 16 -->

GNU/Linux no trabaja con unidades
Entonces, para poder acceder a un dispositivo (disco rígido, cdrom,
pendrive) necesitamos incorporarlo a nuestro sistema de archivos.
Para esto nos valemos de los comandos mount y umount.
Ellos se encargan de poder acceder a un dispositivo, a través de un
directorio en nuestro sistema (normalmente ubicados en /media).
Montado de Sistemas de Archivos

<!-- página 17 -->

● Archivos o ficheros ordinarios: estos pueden ser archivos de textos, documentos,
ejecutables, etc.
● Directorios: también conocidos como carpetas y son tipos de archivos especiales que
agrupan otros ficheros de forma estructurada.
● Archivos de dispositivos: representan dispositivos conectados al sistema. Se dividen en
tres clases:
Seriales: se lee o escribe carácter por carácter, ejemplos:
teclados, mouses y MODEM's.
Bloque: permiten leer y/o escribir datos por bloques en forma
aleatoria, ejemplo: discos rígidos, disquetes, memorias, etc.
Especiales: se utilizan en pantallas, dispositivos gráficos, etc.
Tipos de archivo en GNU/Linux

<!-- página 18 -->

Tipos de dispositivos en GNU/Linux
/dev/hdXX
(hard device)
Dispositivos IDEIDE
/dev/fdXX
(floppy device)
/dev/sdXX
(scsi device)
Dispositivos IDE o SCSIIDE o SCSI
Dispositivos USBUSB
/dev/plipXX
(parallel interface port)
Puertos SerieSerie
/dev/ttySXX
(terminal teletype serial)
Puertos ParalelosParalelos
/dev/nvme0nX Dispositivos M2M2

<!-- página 19 -->

Comandos para el manejo de archivos:
mkdir
rm
cp
mv
ln

<!-- página 20 -->

Comandos para el manejo de archivos:
mkdir – crea directorios
Sintaxis:
mkdir <opciones> <directorios>
Opciones:
-p: crea la estructura completa de directorio
-v: imprime un mensaje por pantalla de cada directorio creado
Ejemplos:
$mkdir -p /home/usuario/dir1/subdir1
$mkdir -v /home/usuario/dir2

<!-- página 21 -->

Comandos para el manejo de archivos:
rm – remueve archivos o directorios
Sintaxis:
rm <opciones> <archivos>
Opciones:
-r: remueve un directorio en forma recursiva, eliminando todo su contenido
-i: pide confirmación antes de remover el archivo
-f: no pide confirmación para remover
Ejemplos:
$rm -r /home/usuario/dir1
$rm -i /home/usuario/dir2

<!-- página 22 -->

Comandos para el manejo de archivos:
cp – copia archivos y directorios
Sintaxis:
cp <opciones> origen destino
Opciones:
-v: imprime por pantalla los archivos copiados
-r: permite copiar recursivamente el contenido de un directorio
-i: pide confirmación antes de sobreescribir un archivo
Ejemplos:
$cp -v /etc/hosts /home/usuario/
$cp -i /etc/hosts /home/usuario/

<!-- página 23 -->

Comandos para el manejo de archivos:
mv – mueve (renombra) archivos y directorios
Sintaxis:
mv <opciones> origen destino
Opciones:
-v: imprime por pantalla los archivos movidos
-f: borra los archivos existentes sin pedir confirmación
-i: pide confirmación al usuario antes de sobreescribir archivos
Ejemplos:
$mv -i /home/usuario/hosts /home/usuario/archivo-hosts
$mv -v /home/usuario/archivo-hosts /home/usuario/hosts

<!-- página 24 -->

Comandos para el manejo de archivos:
ln – crea enlaces entre archivos
Sintaxis:
ln <opciones> destino nombre-enlace
Opciones:
-v: imprime por pantalla los archivos enlazados
-s: crea un enlace simbólico
-i: pide confirmación al usuario antes de sobreescribir archivos
Ejemplos:
$ln -s /home/usuario/hosts /home/usuario/enlace-hosts
$ln -v /home/usuario/hosts /home/usuario/otro-enlace-hosts

<!-- página 25 -->

Comandos para el manejo de archivos:
mount
umount

<!-- página 26 -->

Comandos para el manejo de sistemas de archivos:
mount – monta un sistema de archivos
Sintaxis:
mount <opciones> <dispositivo> <directorio>
Opciones:
-o: permite especificar opciones de montado (solo lectura, lectura/escritura)
-a: monta todo los sistemas de archivos mencioados en fstab
-t: permite especificar el tipo de sistema de archivos (vfat, ext2, ext3, reiserfs)
Ejemplos:
$mount
$mount -t iso9660 /dev/hdc /mnt

<!-- página 27 -->

Comandos para el manejo de sistemas de archivos:
umount – desmonta un sistema de archivos
Sintaxis:
umount <opciones> <dispositivo> <directorio>
Opciones:
-n: desmonta un sistema de archivos sin modificar /etc/mtab
-a: desmonta todos los sistemas de archivos mencioados en mtab
-t: permite especificar el tipo de sistema de archivos (vfat, ext2, ext3, reiserfs)
Ejemplos:
$umount -a
$umount /mnt

<!-- página 28 -->



<!-- página 29 -->

Cómo Linux maneja el montado de sistemas de archivos
Utiliza el archivo /etc/fstab (filesystem table)
En el se especifica la ubicación de cada sistema de archivos y sus opciones
de montado.
Se usa principalmente en la carga del sistema operativo para el montado de
particiones en el árbol de directorio de Linux.
Sirve como atajo a la hora de montar dispositivos o sistemas de archivos

<!-- página 30 -->

Práctica de Laboratorio 1
Ejecute una terminal
Crear un directorio, en el home del usuario.
* mkdir /home/usuario/prueba
* cd /home/usuario/prueba
1
2
Crear un directorio y un archivo, con el contenido hola mundo.
3 Crear un archivo, y completarlo con el texto “hola mundo”,
guardar y mostrar su contenido, con los siguientes comandos:
* nano prueba.txt
* cat prueba.txt

<!-- página 31 -->

Práctica de Laboratorio 2
Ejecute una terminal
Identifique el dispositivo, con el comando dmesg.
1
2
Montar un dispositivo, en esta práctica un pendrive.
3 Cree un directorio llamado Pendrive y monte el
dispositivo:
* mkdir /media/pendrive
* mount /dev/xxx1 /media/pendrive
* ls /media/pendrive

<!-- página 32 -->

Práctica de Laboratorio 3
Ejecute una terminal1
2
Desmontar el dispositivo.
Desmonte la unidad con el siguiente comando:
* unmount /media/pendrive

<!-- página 33 -->

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
1) Explicar la estructura de directorio y las unidades del S.O
Microsoft Windows.
2) Explicar los sistemas de archivos que soporta por defecto.
3) Mostrar comandos básicos para manipular archivos:copiar,
mover, modificar y crear.
