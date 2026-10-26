# Clase 11 Práctica

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Clase 11 Práctica.pdf` · 23 página(s) · texto extraído con pypdf.
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
| 22 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 23 |  |

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
exequiel.aramburu@uader.edu.ar
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Actividad extra aúlica. Analizar las administración de tareas programadas
 de Microsoft Windows.
● Como podemos incorporar software/aplicativos a los S.O.
● GNU/Linux. Compilación y Dependencias.
● Paquetes y Sistemas de Paquetes.
● Aplicativos gráficos de instalación de software.

<!-- página 3 -->

Análisis de la Actividad extra aúlica de Clase 10.
Analizar las administración de tareas programadas de Microsoft Windows.

<!-- página 4 -->

Práctica - SO -LSI – FCyT – UADER
¿Como podemos incorporar un software/aplicación a nuestro S.O?
https://www.menti.com/zvvn1brnq6

<!-- página 5 -->

Práctica - SO -LSI – FCyT – UADER
¿Como podemos incorporar un software/aplicación a nuestro
S.O Microsoft Windows 11?

<!-- página 6 -->

Práctica - SO -LSI – FCyT – UADER
¿Como podemos incorporar un software/aplicación a nuestro
S.O Android?

<!-- página 7 -->

Práctica - SO -LSI – FCyT – UADER
¿Como podemos incorporar un software/aplicación a nuestro
S.O GNU/Linux?

<!-- página 8 -->

GNU/Linux. Compilación y Dependencias.
En el principio...
● En GNU/Linux era muy complicado instalar programas.
● Necesitábamos obligatoriamente compilarcompilar los programas
● Esto generaba muchos problemas de por las dependenciasdependencias
● Todo esto hacía que instalar problemas era sumamente complicado

<!-- página 9 -->

Para solucionar esto...
● Distintas comunidades de usuarios desarrollaron Sistemas de PaquetesSistemas de Paquetes
● Nace el concepto de paquete paquete
● Esto soluciona la gran mayoría de los problemas anteriores
● En la actualidad existen numerosas herramientas para realizar este proceso

<!-- página 10 -->

Ejemplo de paquetes de Debian GNU/Linux
Convención de un
paquete
binario .deb <númeroDeVersiónPaquete>
<nombreDelPaquete>
<númeroDeRevisiónDebian>
<nombre>_<NúmeroDeVersión>-<NúmeroDeRevisiónDebian>.deb<nombre>_<NúmeroDeVersión>-<NúmeroDeRevisiónDebian>.deb

<!-- página 11 -->

Paquetes
¿Qué es DPKG?
● Herramienta para el manejo de paquetes de bajo nivel.
● Creada por Ian Jackson en 1993.
● De características muy similares al rpm.
Algunas funciones de DPKG
La principal función es la instalación, eliminación y configuración de los paquetes Debian
junto con su información.
Configuración básica de DPKG
Se realiza desde el archivo  /etc/dpkg/dpkg.cfg/etc/dpkg/dpkg.cfg

<!-- página 12 -->

Paquetes
dpkg -i <paquete>
Para instalar paquetes deb. No resuelve dependencias.
Ejemplo: dpkg -i htop_3.2.0-1_amd64.debEjemplo: dpkg -i htop_3.2.0-1_amd64.deb
dpkg -r <paquete>
Para desinstalar paquetes. No borra los archivos de
configuración.
Ejemplo: dpkg -r htopEjemplo: dpkg -r htop

<!-- página 13 -->

Herramienta Grafica de paquetes deb (Gdebi)
Gdebi es una herramienta que puede instalar paquetes deb. La cual permite instalar paquetes deb de forma
local, es decir, sin necesidad de repositorios ni una conexión a Internet

<!-- página 14 -->

Sistemas de paquetes

<!-- página 15 -->

Sistemas de paquetes
Un sistema de gestión de paquetes , también conocido como gestor de paquetes, es una colección de
herramientas que sirven para automatizar el proceso de instalación, actualización, configuración y eliminación
de paquetes de software.
En estos sistemas, el software se distribuye en forma de paquetes, frecuentemente encapsulado en un solo
fichero. Estos paquetes incluyen otra información importante, además del software mismo, como por ejemplo:
● Nombre completo
● Descripción de su funcionalidad
● Número de versión
● El distribuidor del software
● Suma de verificación
● Dependencia de otros paquetes.
Esta información se introduce normalmente en una base de datos de paquetes local.

<!-- página 16 -->

Sistemas de paquetes
Oficial
o
No oficial
Linux
Admin/User
Sistema de Paquetes Repositorio
Paquetes Dependencias

<!-- página 17 -->

Ejemplos de sistemas de paquetes

<!-- página 18 -->

Sistema de paquetes APT
¿Qué es APT?
● Herramienta avanzada para el manejo de paquetes.
● Basada el uso de DPKG.
Algunas funciones de APT
● Resolución de complejas dependencias.
● Traer paquetes de servidores remotos para instalar en nuestro
equipo.
Configuración básica de APT
Se realiza desde el archivo   /etc/apt/sources.list./etc/apt/sources.list.

<!-- página 19 -->

Configuración de APT
El archivo /etc/apt/sources.list/etc/apt/sources.list posee una lista de las fuentes en
donde encontraremos los paquetes.
Estructura de /etc/apt/sources.list
debdeb  http://host/debianhttp://host/debian  distribución sección1 sección2 sección3  distribución sección1 sección2 sección3
deb-src deb-src http://host/debianhttp://host/debian  distribución sección1 sección2 sección3  distribución sección1 sección2 sección3
Ejemplo:
debdeb  http://http.us.debian.org/debianhttp://http.us.debian.org/debian  stable main contrib non-free  stable main contrib non-free
deb-srcdeb-src  http://http.us.debian.org/http://http.us.debian.org/ debian stable main contrib non-free debian stable main contrib non-free

<!-- página 20 -->

Comandos
APT
apt-get update
apt-get upgrade
apt-get dist-upgrade
apt-get install
apt-get remove
apt-get clean
apt-cache search
apt-cache show
apt-cdrom add
man apt

<!-- página 21 -->

Kpackage
 Shaman
Herramienta Grafica de sistemas de paquetes

<!-- página 22 -->

Synaptic

<!-- página 23 -->

Instalación de software utilizando distintas alternativas:
Libreoffice https://es.libreoffice.org/
Htop https://htop.dev/
