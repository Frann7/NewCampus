# Clase 20

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Clase 20.pdf` · 38 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 4 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 5 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 6 |  |
| 7 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 8 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 9 |  |
| 10 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 11 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 12 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 13 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 14 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 15 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 16 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 17 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 18 |  |
| 19 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 20 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 21 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 22 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 23 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 24 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 25 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 26 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 27 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 28 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 29 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 30 |  |
| 31 |  |
| 32 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 33 |  |
| 34 |  |
| 35 |  |
| 36 |  |
| 37 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 38 |  |

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
● Análisis de Métodos de almacenamiento de datos en múltiples discos. En esta clase se analiza
RAID 2,RAID 3 y RAID 6.
●  Análisis de  RAID 10, RAID 5E y 6E. Variantes de RAID 10, 5E y RAID 6E que incluyen discos de reserva.
● Prácticas de laboratorio. Implementar RAID | por software instalando Debian GNU/Linux o derivado,
con RAID | desde el instalador del S.O.
● Actividad extra aúlica grupal N.º8. Métodos de espacios de almacenamiento de datos en múltiples
 discos en Microsoft Windows. Implementar espacios de reflejo en Microsoft Windows Virtualizado.

<!-- página 3 -->



<!-- página 4 -->



<!-- página 5 -->



<!-- página 6 -->

RAID 5E y RAID 6E
Se puede llamar RAID 5E y RAID 6E a las variantes de RAID 5 y RAID 6 que incluyen disco de
reserva (RAID). Estos discos pueden estar conectados y preparados (hot spare) o en espera
(standby spare). En los RAID 5E y RAID 6E, los discos de reserva están disponibles para
cualquiera de las unidades miembro. No suponen mejora alguna del rendimiento, pero sí se
minimiza el tiempo de reconstrucción (en el caso de los discos hot spare) y las labores de
administración cuando se producen fallos. Un disco de reserva no es realmente parte del conjunto
hasta que un disco falla y el conjunto se reconstruye sobre el de reserva.

<!-- página 7 -->



<!-- página 8 -->



<!-- página 9 -->

Instalación del S.O en RAID 0
Utilizando VirtualBox, creamos una VM con 2 discos de 10GB cada uno.

<!-- página 10 -->



<!-- página 11 -->



<!-- página 12 -->



<!-- página 13 -->



<!-- página 14 -->



<!-- página 15 -->



<!-- página 16 -->



<!-- página 17 -->



<!-- página 18 -->

Crear tabla de partición a cada dispositivo

<!-- página 19 -->



<!-- página 20 -->



<!-- página 21 -->



<!-- página 22 -->



<!-- página 23 -->



<!-- página 24 -->



<!-- página 25 -->



<!-- página 26 -->



<!-- página 27 -->



<!-- página 28 -->



<!-- página 29 -->



<!-- página 30 -->

Instalando el S.O en RAID 0
* Es Importante instalar el Gestor de arranque(ej: GRUB) en ambas particiones.

<!-- página 31 -->

cat /proc/mdstat
El archivo /proc/mdstat enumera los volúmenes existentes y sus estados.
mdstat

<!-- página 32 -->

Gráficamente

<!-- página 33 -->

mdadm --detail /dev/md0 mdadm -D /dev/md1

<!-- página 34 -->

Si un disco falla en RAID 1
¿Que sucede?
Vamos a simularlo en la VM ...

<!-- página 35 -->

PERDIDA DE UN DISCO EN RAID 1, LO DESCONECTAMOS DESDE VirtualBox
RAID 1
RAID 0

<!-- página 36 -->

PERDIDA DE UN DISCO EN RAID 1, LO DESCONECTAMOS DESDE VirtualBox
Lo incorporar al RAID al nuevo disco:
mdadm /dev/md0 --add /dev/sdb1

<!-- página 37 -->

REBUILD RAID 1

<!-- página 38 -->

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
1) Identificar el métodos de espacios de almacenamiento de datos en
múltiples discos en Microsoft Windows específicamente el de de reflejo.
2) Implementar espacios de reflejo en Microsoft Windows Virtualizado, y
exponerlo en la presentación.
