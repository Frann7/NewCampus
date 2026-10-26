# Clase 18

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Clase 18.pdf` · 25 página(s) · texto extraído con pypdf.
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
| 12 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 13 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 14 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
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

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.
aramburu.exequiel@uader.edu.ar

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Presentación de la actividad extra aúlica clase anterior. Explicar la estructura de directorio
y sistemas de archivos que soporta el S.O Microsoft Windows. Mostrar comandos básicos para manipular
archivos:copiar, mover, modificar y crear.
● Tabla de particiones. Tipos de tablas, estructura y ventajas.
● Introducción a particiones. Definición y utilización.
● Esquemas de Particionado. Definición y Ejemplos.
● Herramientas de particiones graficas y de consola. Gparted, gnome-disk-utility, fdisk, cfdisk, lsblk,
blkid, parted y df.
● Práctica de laboratorio. Identificar el esquema de particionado y debate grupal.
● Actividad extra aúlica. Esquemas de particionado Microsoft Windows. Identificar, analizar
 y exponer las herramientas de particionado nativas/externas. MBR y GPT.

<!-- página 3 -->

Una partición de disco, es el nombre genérico que recibe cada división presente en una sola
unidad física de almacenamiento de datos. Los dispositivos de almacenamiento se pueden
dividir en una o más particiones, con sistemas de archivos independientes en cada
partición.
Existen distintas tablas de partición (ej:MBR y GPT), y distintos tipos de particiones según la
tabla.
Las particiones pueden utilizarse para varios fines, puedes tener una dedicada a guardar
datos sensibles con medidas de seguridad que no interfieran en el resto del sistema, como
copias de seguridad, o utilizarla para instalar diferentes sistemas operativos o dividirlo.
Introducción a Particiones

<!-- página 4 -->

Preguntas:
¿Cuantas particiones podemos crear?
¿Cual es el tamaño máximo de una partición?
¿Que tipos de particiones existen?
¿Que tipos de tabla de particiones existen?

<!-- página 5 -->

TABLA DE PARTICIONES
MBR
GPT

<!-- página 6 -->

Tabla de particiones

<!-- página 7 -->

MBR (Master Boot Record)
Gestor de Arranque

<!-- página 8 -->

Práctica - SO -LSI – FCyT – UADER

<!-- página 9 -->

Completo(pfd): https://uefi.org/sites/default/files/resources/UEFI_Spec_2_10_Aug29.pdf
GUID Partition Table (html): https://uefi.org/specs/UEFI/2.10/05_GUID_Partition_Table_Format.html
Tabla de Particiones GUID (GPT)

<!-- página 10 -->

Tabla de Particiones GUID (GPT)
La tabla de partición GUID (GPT) es un esquema de partición basado en el uso de un identificador único
global (GUID). La GPT se desarrolló para hacer frente a las limitaciones de la tabla de partición MBR,
especialmente con el limitado espacio de almacenamiento máximo direccionable de un disco. A diferencia
de MBR, que no puede direccionar un almacenamiento mayor de 2 TiB (equivalente a unos 2,2 TB), GPT
se utiliza con discos duros de mayor tamaño; el tamaño máximo direccionable del disco es de 2,2 ZiB.
Además, GPT, por defecto, permite crear hasta 128 particiones primarias. Este número puede ampliarse
asignando más espacio a la tabla de particiones.
Fuente:https://access.redhat.com/documentation/es-es/red_hat_enterprise_linux/8/html/managing_storage_devices/guid-partition-table_assembly_creating-a-partition-table-on-a-disk

<!-- página 11 -->

Los discos GPT utilizan el Direccionamiento Lógico de Bloques (LBA - Logical Block Addressing) y la
disposición de las particiones es la siguiente:
● Para mantener la compatibilidad con los discos MBR, el primer sector (LBA 0) de GPT está reservado para
los datos de MBR y se llama "MBR protector".
● La cabecera GPT primaria comienza en el segundo bloque lógico (LBA 1) del dispositivo. La cabecera
contiene el GUID del disco, la ubicación de la tabla de particiones primaria, la ubicación de la cabecera GPT
secundaria, y las sumas de comprobación CRC32 de sí misma y de la tabla de particiones primaria. También
especifica el número de entradas de partición en la tabla.
● La GPT primaria incluye comienza en bloque LBA 2 hasta LBA 33, por defecto 128 entradas de partición,
cada una con un tamaño de entrada de 128 bytes, su GUID de tipo de partición y su GUID de partición única.
● La GPT secundaria es idéntica a la GPT primaria. Se utiliza principalmente como una tabla de respaldo para la
recuperación en caso de que la tabla de partición primaria se corrompa.
● La cabecera secundaria de GPT se encuentra en el último sector lógico del disco y puede utilizarse para
recuperar la información de GPT en caso de que la cabecera primaria esté dañada. Contiene el GUID del disco,
la ubicación de la tabla de particiones secundarias y la cabecera GPT primaria, las sumas de comprobación
CRC32 de sí mismo y de la tabla de particiones secundarias, y el número de posibles entradas de partición.

<!-- página 12 -->



<!-- página 13 -->



<!-- página 14 -->



<!-- página 15 -->

No ocupa todos los sectores

<!-- página 16 -->

Total Ultimo
Backup GPT
Al final del dispositivo
Del almacenamiento
2014
LBA 34
2048 500117503
464844800
500118182
655
5001181580

<!-- página 17 -->

Fuente: https://www.seagate.com/la/es/support/kb/storage-capacity-measurement-standards-002046en/

<!-- página 18 -->

Fuente: https://www.adata.com/ar/consumer/662?tab=faq
256GB *0,93 = 238,08 GB aprox.

<!-- página 19 -->

Fuente: https://access.redhat.com/documentation/es-es/red_hat_enterprise_linux/6/html/installation_guide/s2-diskpartrecommend-x86

<!-- página 20 -->

Algunas herramientas Gráficas y de consola
● Gparted
● gnome-disk-utility
● KDE Partition Manager
● fdisk
● cfdisk
● lsblk
● parted
● blkid
● df
Gráficas Consola
A continuación se muestran y analizan  todas las herramientas mencionadas en el proyector….
fdisk -l
cfdisk /dev/sda
lsblk -fm
parted -l
blkid
Un ejemplo
df -hT

<!-- página 21 -->

Práctica de Laboratorio 1
Identificar la tabla de partición, las particiones definida en su
equipo y sus sistemas de archivos.
1
2
Identificar el esquema de particionado
Completar la tabla que expone a continuación.
3 Debate grupal sobre los esquemas de particionado.

<!-- página 22 -->

Práctica de Laboratorio 1
 Discos y
tecnología Tamaño Tabla de
partición
Partición Swap
Tamaño
Partición 1
Tamaño
Filesystem
Montado
Partición 2
Tamaño
Filesystem
Montado
...
Partición N
Tamaño
 Filesystem
Montado
1 1 M2 256 GB GPT 18 GB
238 GB
Ext4
/
2
3

<!-- página 23 -->

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
1) Identificar las herramientas de particionado del sistema Microsoft Windows
nativas como mínimo.
2) Explicar y exponer las diferentes opciones de la herramienta nativa.
3) Comentar los esquemas de particionado del S.O

<!-- página 24 -->

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
1) Realizar una copia de la tabla de partición de dispositivo con tabla particiones MBR y al
menos una partición definida, utilizando el comando dd.
   Ej: dd if=/dev/xxx of=backupMBR bs=512 count=1
2) Utilizar un lector de Hexadecimal para abrir el archivo generado, identificar cada campos de
la tabla (utilizando la estructura antes expuesta) y su valor.
3) Por otro lado, capturar visualmente la tabla de particiones con una herramienta gráfica
(ej:gparted).
4) Exponer y explicar ambos resultados relacionando cada valor.

<!-- página 25 -->

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
1) Realizar una copia de la tabla de partición de dispositivo con tabla particiones GPT y al
menos una partición definida, exceptuando el LBA0 y la GPT Secundaria,  utilizando el
comando dd.
1) Ej: dd if=/dev/xxx of=BackupGPT bs=512  skip=1 count=33
2) Utilizar un lector de Hexadecimal para abrir el archivo generado, identificar cada campos de
la tabla (utilizando la estructura antes expuesta) y su valor.
3) Por otro lado, capturar visualmente la tabla de particiones con una herramienta gráfica
(ej:gparted).
4) Exponer y explicar ambos resultados relacionando cada valor.
