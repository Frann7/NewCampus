# Guía_de_instalación_del_XAMPP

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/PA/CLASE 1/TEORIA/Guía_de_instalación_del_XAMPP.pdf` · 9 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 | Introducción: acrónimo XAMPP (X, Apache, MySQL, PHP, Perl), servidor local; versiones para Linux y Windows |
| 2 | Versiones para Mac OS X y Solaris; licencia (GPL de la compilación) |
| 3 | Pasos 1 a 3: descargar de apachefriends.org, ejecutar, bienvenida (captura sin datos extra) |
| 4 | Pasos 4 y 5: carpeta `C:\xampp`, componentes Apache y MySQL (la captura muestra la pantalla de idioma) |
| 5 | Pasos 6 y 7: Install y Finish (capturas sin datos extra) |
| 6 | Paso 8: panel de control (captura con PID y puertos: Apache 80/443, MySQL 3306, también en el texto); paso 10: probar `http://localhost/` (no hay paso 9) |
| 7 | ⚠ ver el PDF: captura de la bienvenida en `localhost/dashboard/` (XAMPP 7.2.32, "Apache + MariaDB + PHP + Perl"); paso 11 (dice `C:\wamp\`; la estructura está solo en la captura de la pág. 8) |
| 8 | ⚠ ver el PDF: capturas de las carpetas de `C:\xampp` y de `htdocs`; paso 12: htdocs es el directorio público; bibliografía |
| 9 | Nota: las imágenes son de una instalación local |

<!-- página 1 -->

Guía de Instalación del XAMPP
Este guía esta orientada a la instalación y puesta en marcha del XAMPP, como así también
los  conceptos básicos del mismo.
Objetivo: Comprender el funcionamiento básico del XAMP.
Sitio oficial: http://www.apachefriends.org
Introducción
XAMPP(X Sistema  Operativo,  Apache,  MySQL,  PHP,  Perl):  es  una  aplicación  para
cualquier sistema operativo que pone a disposición los servicios de Apache, PHP y MySQL de
manera  fácil  y  asistida.  XAMPP  contiene,  un  servidor  local  nos  permite  poner  a  prueba  la
aplicación en desarrollo, sin necesidad del Internet. Para realizar un localhost (servidor local) es
necesaria la instalación de los servicios mencionados.
Actualmente hay cuatro versiones de XAMPP:
XAMPP para Linux
La  versión  para  sistemas  Linux  (testeado  para  SuSE,  RedHat,  Mandrake  y
Debian)contiene: Apache, MySQL, PHP & PEAR, Perl, ProFTPD, phpMyAdmin, OpenSSL,
GD, Freetype2, libjpeg, libpng, gdbm, zlib, expat, Sablotron, libxml, Ming, Webalizer, pdf class,
ncurses, mod_perl, FreeTDS, gettext, mcrypt, mhash, eAccelerator, SQLite e IMAP C-Client.
XAMPP para Windows
Esta  versión  contiene:  Apache,  MySQL,  PHP +  PEAR,  Perl,  mod_php,  mod_perl,
mod_ssl, OpenSSL, phpMyAdmin, Webalizer, Mercury Mail Transport System para Win32 y
NetWare Systems v3.32, JpGraph, FileZilla FTP Server, mcrypt, eAccelerator, SQLite, y WEB-
DAV + mod_auth_mysql.

<!-- página 2 -->

XAMPP para Mac OS X
La versión para Mac OS X contiene: Apache, MySQL, PHP & PEAR, SQLite, Perl,
ProFTPD,  phpMyAdmin,  OpenSSL,  GD,  Freetype2,  libjpeg,  libpng,  zlib,  Ming,  Webalizer,
mod_perl, eAccelerator.
XAMPP para Solaris
La versión para Solaris (desarrollada y probada con Solaris 8, probada con Solaris 9)
contiene: Apache, MySQL, PHP & PEAR, Perl, ProFTPD, phpMyAdmin, OpenSSL, Freetype2,
libjpeg, libpng, zlib, expat, Ming, Webalizer, pdf class.
Licencia de XAMPP
XAMPP es una compilación de software libre (comparable a una distribución Linux), es
gratuito y libre para ser copiado conforme los términos de la licencia GNU General Public License.
Sin embargo, sólo la compilación de XAMPP está publicada bajo la licencia GPL. Por favor,
remítase a cada licencia contenida en los productos para saber qué es y qué no es permitido.
En el caso de uso comercial, por favor dé una mirada a las licencias de los productos
(especialmente MySQL), desde el punto de vista de XAMPP, el uso comercial es también libre.

<!-- página 3 -->

Comenzando la instalación
1)  -  El  primer  paso  es  obtener  el  instalador  de  XAMPP  desde  el  sitio  oficial:
https://www.apachefriends.org.
2) - Ejecutar el archivo que se descarga y hacer click en OK para continuar la instalación.
3) - Luego, se mostrara la siguiente ventana de bienvenida:

<!-- página 4 -->

4) - Selección del directorio de instalación, el programa será instalado por defecto en
c:\xampp, para cambiar el destino de instalación debe agregar la ubicación en la casilla, o
haciendo uso del Browser, para continuar click en Next.
5) - Creación del acceso directo, Creación de acceso en el menú Inicio, y sección de
servicios que vamos a instalar, en nuestro caso marcamos los servicios Apache y  Mysql, como
así también los accesos:

<!-- página 5 -->

6) - Luego realizar click en el botón “Install” y comenzara el proceso de instalación:
7) - Una vez que finaliza el proceso de instalación, haga click en “Finish”

<!-- página 6 -->

8)  Si  la  instalación  ha  concluido  satisfactoriamente  en  su  barra  de  herramientas  de
Windows encontrara el panel de administración:
realizando doble click en el icono naranja que se visualiza en la imagen anterior, se iniciaria el
Panel de administración:
Verifique que los servicios  Apache y MySQL se encuentren en ejecución, por lo tanto
tienen que tener un numero de PID(Identificador de Proceso) en la imagen anterior Apache posee
el 752 y  Mysql el 2032, estos varían en cada inicio, ademas verifique que que el puerto de
Apache sea el 80,443 y Mysql el 3306, lo cuales son los puertos por defecto.
10) Probando el servidor WEB local Apache, para esto ingrese al navegador web  y en la URL del
mismo ingrese:
http://localhost/
Esto automáticamente lo redirigirá a http://localhost/wampp y se visualizara lo siguiente:

<!-- página 7 -->

11)  Ubicación  del  directorio  XAMPP,  si  usted  instalo  en  la  ubicación  por  defecto  “C:\wamp\”
encontrara la siguiente estructura:

<!-- página 8 -->

12) El directorio publico donde se encuentran las aplicaciones WEB y las aplicaciones que usted a
partir de ahora valla programando es “ htdocs”, en este directorio encontrara la aplicaciones que
por defecto el aplicativo XAMPP instala, como el que accedió en el punto 10 de esta guía:
bibliografía:
Sitio oficial: http://www.apachefriends.org.

<!-- página 9 -->

Imágenes: Fueron capturadas de una instalación local del XAMPP.
