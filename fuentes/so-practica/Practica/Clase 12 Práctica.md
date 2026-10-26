# Clase 12 Práctica

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Clase 12 Práctica.pdf` · 16 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
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

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
exequiel.aramburu@uader.edu.ar
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Algoritmos de compresión
● Empaquetar Archivos (TAR).
● Tabla de algoritmos de compresión / empaquetador.
● Compilar. Make. Configure. Gcc.
● Práctica de laboratorio. Compilar htop.
● Práctica de laboratorio. Compilar mc.

<!-- página 3 -->

¿Qué es GZIP?     (abreviatura de (abreviatura de GGNU NU ZIPZIP))
Es un reemplazo del programa compress de UNIX. Creado por Jean-
loup Gailly y Mark Adler en 1992 con la versión 0.1.
¿Qué es BZIP2?
● Es un aplicativo libre que comprime y descomprime archivos según
algoritmo de mayor porcentaje de compresión.
● Basado en una Licencia BSD.
● Comprime más pero consume más.
Extensión: .gz apt install gzip
apt install bzip2Extensión: .bz2

<!-- página 4 -->

¿Qué es XZ?     (abreviatura de (abreviatura de GGNU NU ZIPZIP))
XZ es el sucesor del formato de compresión del algoritmo de cadenas
de  MArkov/Lempel-Ziv, que proporciona una compresión potente (a
veces mejor que bzip2) pero devoradora de memoria y una rápida y
fácil descompresión.
Extensión: .xz
apt-get install xz-utils

<!-- página 5 -->

¿Qué es TAR?         ((TTape ape ArArchiever – Archivador de Cinta)chiever – Archivador de Cinta)
● Formato de archivos ampliamente usado en entornos UNIX.
● Identificados con la extensión tar.
● La principal función de tar es empaquetar los archivos.
ZIP no es compatible con GZIP
La principal diferencia entre estos formatos es que GZIP no empaqueta
los archivos, únicamente los comprime.

<!-- página 6 -->



<!-- página 7 -->

¿Qué es compilar en programación?
Ej: gcc

<!-- página 8 -->

apt-get install build-essential
Instala los paquetes necesarios para compilar un software. Incluyen el
depurador GNU, la colección de compiladores g++/GNU y algunas
herramientas y bibliotecas más que se requieren para compilar un programa.
Alguno de estos paquetes son: g++, gcc, libc6-dev, dpkg-dev y make.
BUILD-ESSENTIAL - Metapaquete

<!-- página 9 -->

Make es una herramienta de gestión de dependencias, típicamente, las que
existen entre los archivos que componen el código fuente de un programa,
para dirigir su recompilación o "generación" automáticamente.
Para prepararse para usar make, debe escribir un archivo llamado makefile
que describa las relaciones entre los archivos en su programa y establezca
los comandos para actualizar cada archivo
MAKE -  Utilidad para construir y mantener grupos de programas.

<!-- página 10 -->

Limpiar los archivos de una compilación anterior
  #make clean#make clean
Desinstalar los archivos compilados
  #make uninstall#make uninstall
Instalar los archivos compilados
#make install#make install
Compilar el código fuente
#make#make
MAKE -  Comandos.
Requiere el archivo:Requiere el archivo:
makefilemakefile

<!-- página 11 -->

Configure
Es  un script que generalmente se proporciona con el código fuente de la mayoría de los paquetes,
es responsable de prepararse para construir el software en su sistema específico.
Se asegura de que todas las dependencias para el resto del proceso de compilación e instalación
estén disponibles y descubre/obtiene las variables dependientes del sistema que necesita.
Finalmente crea el archivo Makefile, el cual es requerido por el comando make.

 Configure del MC
Configure del HTOP

<!-- página 12 -->

Instalación de paquetes tar.gz / tar.xz de código fuente
Descomprimir el código fuente
#gunzip nombre-del-paquete.tar.gz#gunzip nombre-del-paquete.tar.gz
oo
#xz -d nombre-del-paquete.tar.xz#xz -d nombre-del-paquete.tar.xz
Desempaquetar el código fuente
#tar xvf nombre-del-paquete.tar#tar xvf nombre-del-paquete.tar
Configurar los archivos para compilar el código fuente
#./configure#./configure
Compilar el código fuente
#make#make
1
2
3
4

<!-- página 13 -->

Práctica de Laboratorio
Descargue el código fuente de HTOP del sitio oficial:
Compile el código fuente y ejecútelo.
Liste la versión del compilado: ./htop -V
Liste la versión del sistema: htop -V
1
2
3 Liste las versiones de HTOP:
Compilar HTOP
*2) Nota: Resuelva dependencias con apt. (ej: apt install libssl-dev libncurses5
libncursesw5-dev)
https://htop.dev/

<!-- página 14 -->

Práctica de Laboratorio
Descargue el código fuente de MC del sitio oficial:
Compile el código fuente y ejecútelo.
Liste la versión del compilado: ./mc -V
Liste la versión del sistema: mc -V
1
2
3 Liste la versiones de MC:
Compilar MC
https://midnight-commander.org/
*2) Nota: Resuelva dependencias con apt. (ej: apt install libslang2-dev)

<!-- página 15 -->

Instale el navegador Microsoft Edge utilizando el .deb del sitio oficial:
Práctica de Laboratorio
https://www.microsoft.com/es-es/edge

<!-- página 16 -->

Examen Individual N°1 (EI1)
● Próxima clase.
● Se realiza en las computadores del laboratorio.
● Se utiliza el campus virtual.
● Incluye las clases: 3, 4, 5, 6, 7, 10, 11 y 12.
● Consta de 20 preguntas.
