# Clase 19

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Clase 19.pdf` · 39 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 4 |  |
| 5 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 6 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 7 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 8 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 9 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 10 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 11 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 12 |  |
| 13 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 14 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 15 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 16 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 17 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 18 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 19 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 20 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 21 |  |
| 22 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 23 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 24 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 25 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 26 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 27 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 28 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 29 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 30 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 31 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 32 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 33 |  |
| 34 |  |
| 35 |  |
| 36 |  |
| 37 |  |
| 38 |  |
| 39 |  |

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.
aramburu.exequiel@uader.edu.ar

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Presentación de la actividad extra aúlica clase anterior.
● Introducción a RAID por Software y Hardware.
● Niveles estándares, anidados y propietarios. Ventajas y Desventajas.
● Análisis de Métodos de almacenamiento de datos en múltiples discos. En esta clase se analiza
RAID 0, RAID 1, RAID 4 y RAID 5.
● Espacios de almacenamiento en Microsoft Windows. Espacios simples, de reflejo y de paridad.
● Prácticas de laboratorio. Implementar RAID 0 por software instalando Debian GNU/Linux o derivado,
con RAID 0 desde el instalador del S.O.
● Actividad extra aúlica grupal N.º8. Métodos de espacios de almacenamiento de datos en múltiples
 discos en Microsoft Windows. Implementar espacios de paridad en Microsoft Windows Virtualizado.

<!-- página 3 -->



<!-- página 4 -->

FUENTE: https://www.debian.org/doc/manuals/debian-handbook/advanced-administration.es.html#sect.raid-soft

<!-- página 5 -->



<!-- página 6 -->



<!-- página 7 -->



<!-- página 8 -->



<!-- página 9 -->



<!-- página 10 -->



<!-- página 11 -->



<!-- página 12 -->

Instalación del S.O en RAID 0
Utilizando VirtualBox, creamos una VM con 2 discos de 10GB cada uno.

<!-- página 13 -->



<!-- página 14 -->



<!-- página 15 -->



<!-- página 16 -->



<!-- página 17 -->



<!-- página 18 -->



<!-- página 19 -->



<!-- página 20 -->



<!-- página 21 -->

Crear tabla de partición a cada dispositivo

<!-- página 22 -->



<!-- página 23 -->



<!-- página 24 -->



<!-- página 25 -->



<!-- página 26 -->



<!-- página 27 -->



<!-- página 28 -->



<!-- página 29 -->



<!-- página 30 -->



<!-- página 31 -->



<!-- página 32 -->



<!-- página 33 -->

Instalando el S.O en RAID 0

<!-- página 34 -->

cat /proc/mdstat
El archivo /proc/mdstat enumera los volúmenes existentes y sus estados.
mdstat

<!-- página 35 -->

mdadm --detail /dev/md0 mdadm -D /dev/md1

<!-- página 36 -->

Si un disco falla en RAID 0
¿Que sucede?
Vamos a simularlo en la VM ...

<!-- página 37 -->

PERDIDA DE UN DISCO EN RAID 0, LO DESCONECTAMOS DESDE VirtualBox

<!-- página 38 -->

Los espacios simples están diseñados para aumentar el rendimiento, pero no protegen los archivos en caso de
errores de la unidad. Son más indicados para datos temporales (como archivos de representación de vídeo), archivos
temporales de editores de imagen y archivos de objeto de compilador intermedios. Los espacios simples requieren al
menos dos unidades para ser útiles.
Los espacios de reflejo están diseñados para aumentar el rendimiento y proteger los archivos contra errores de la
unidad ya que guardan varias copias. Los espacios de reflejo doble realizan dos copias de los archivos y pueden tolerar
errores en una unidad, mientras que los espacios de reflejo triple pueden tolerar errores en dos unidades. Los espacios
de reflejo están indicados para almacenar una amplia variedad de datos, desde un recurso compartido de archivos de
uso general a una biblioteca de VHD. Cuando un espacio de reflejo se formatea con el Sistema de archivos resistente
(ReFS), Windows mantiene automáticamente la integridad de los datos, lo que hace que los archivos sean aún más
resistentes ante errores de la unidad. Los espacios simetría de dos vías requieren al menos dos unidades y los
espacios simetría de tres vías requieren al menos cinco.
Los espacios de paridad están diseñados para aumentar la eficiencia del almacenamiento y proteger los archivos en
caso de errores de la unidad ya que guardan varias copias de ellos. Los espacios de paridad están indicados para el
archivado de datos y para la retransmisión por streaming de medios, como música y vídeos. Este diseño de
almacenamiento requiere al menos tres unidades para protegerte en caso de error de una unidad, y al menos siete
unidades para protegerte en caso de error de dos unidades.
Espacios de almacenamiento en Windows
Fuenta: https://support.microsoft.com/es-es/windows/espacios-de-almacenamiento-en-windows-b6c8b540-b8d8-fb8a-e7ab-4a75ba11f9f2

<!-- página 39 -->

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
1) Identificar los métodos de espacios de almacenamiento de datos en
múltiples discos en Microsoft Windows.
2) Exponer en forma teórica los distintos métodos existentes.
3) Implementar espacios de paridad en Microsoft Windows Virtualizado, y
exponerlo en la presentación.
