# Clase 4 Práctica

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/DIAPOS PARCIAL 1/Clase 4 Práctica.pdf` · 21 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional
.
aramburu.exequiel@uader.edu.ar

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Conversatorio de la actividad práctica Clase 3
● Arranque de una computadora Personal con BIOS y MBR
● Gestores de Arranque (bootloader)
● Arranque del sistema operativo GNU/Linux
● Definición de Grupos de TPG.

<!-- página 3 -->

Práctica - SO -LSI – FCyT – UADER
Conversatorio de la actividad práctica Clase 3
Instalación de Microsoft Windows 10/11 en VirtualBox

<!-- página 4 -->

Práctica - SO -LSI – FCyT – UADER

<!-- página 5 -->

Práctica - SO -LSI – FCyT – UADER
Arranque de una computadora personal con BIOS
● Los principales proveedores de BIOS son American Megatrends (AMI) y
Phoenix Technologies.
● Existen proyectos de BIOS bajo el esquema de Software libre, como Coreboot
o Libreboot, que ofrecen firmware alternativos para unas pocas referencias de
placas base.
dmidecode -t bios
dmidecode -t baseboard
https://doc.coreboot.org/mainboard/index.htm
l

https://www.coreboot.org
/

<!-- página 6 -->

Práctica - SO -LSI – FCyT – UADER
Arranque de una computadora personal con BIOS
● Etapa 1. Encendido de la computadora personal
● Etapa 2. Lectura del contenido de la memoria  (BIOS)
● Etapa 3. Pruebas de los dispositivos del sistema (POST)
● Etapa 4. Se muestra una pantalla de estado
● Etapa 5. Testeo de la memoria y de otros recursos de la computadora
● Etapa 6. Búsqueda del primer dispositivo para cargar un Sistema Operativo
El inicio de una computadora personal se compone de varias etapas.

<!-- página 7 -->

Práctica - SO -LSI – FCyT – UADER
Arranque de una computadora personal con BIOS
Antes de cargar un Sistema Operativo
Se busca un medio para iniciar el mismo (CD/DVD, disquete, dispositivo USB, red)
Se leen los primeros 512 bytes de ese dispositivo (Sector 0) para buscar un
programa cargador del Sistema Operativo (MBR – Master Boot Record o LILO)
Se selecciona un SO y se procede a la carga del mismo

<!-- página 8 -->

Práctica - SO -LSI – FCyT – UADER
Arranque de una computadora personal con BIOS
Gestor de Arranque

<!-- página 9 -->

Práctica - SO -LSI – FCyT – UADER

<!-- página 10 -->

Práctica - SO -LSI – FCyT – UADER

<!-- página 11 -->

● LILO (siglas de Linux Loader)
● ELILO (siglas de EFI Linux Loader).
● GRUB legacy.
● GRUB 2.
● systemd-boot. Antes llamado gummiboot.
● Shim.
● Preloader.
● SYSLINUX
● ISOLINUX.
● EXTLINUX.
● PXELINUX.
● MEMDISK.
● LOADLIN
● NTLDR
● BOOTMGR (siglas de BOOT ManaGeR)
● Otros...
Gestores de Arranque

<!-- página 12 -->

Gestores de Arranque

<!-- página 13 -->

Gestores de Arranque

<!-- página 14 -->

Práctica - SO -LSI – FCyT – UADER
Ahora inicia el Sistema Operativo

<!-- página 15 -->

Práctica - SO -LSI – FCyT – UADER
Sistemas de inicio en GNU/Linux
● BSD tradicional (Slackware y Gentoo)
● System V (Versiones viejas de Debian y Devuan)
● upstart (http://upstart.ubuntu.com/) (Versiones viejas de Ubuntu)
● systemd (https://www.freedesktop.org/wiki/Software/systemd/)
 (Versiones actuales de Debian)
Tipos
Es un sistema que controla la ejecución de los programas al inicio de una computadora
 personal.

<!-- página 16 -->

Práctica - SO -LSI – FCyT – UADER
Inicio de GNU/Linux con System V
Ahora es el turno del Sistema Operativo
El núcleo se descomprime y se carga en memoria para ser ejecutado
Se inicializan diversos dispositivos de hardware (controladores)
Se monta el sistema de archivos principal, la partición raíz (/)
Se ejecuta el proceso /sbin/init

<!-- página 17 -->

Práctica - SO -LSI – FCyT – UADER
Niveles de ejecución (runlevels) en System V
Son modos de ejecución de los sistemas operativos basados en Unix. Determinan formas en
 las que podemos iniciar nuestro sistema operativo y los servicios que podemos arrancar en
 cada uno de ellos. El demonio initinit es el encargado de llevar a cabo esta tarea.
● 0:  Apagado del equipo.
● 1:  Inicio en modo mono-usuario.
● 2-5: Inicio en modo multi-usuario y personalizables.
● 6: Reinicio del equipo.

<!-- página 18 -->

Práctica - SO -LSI – FCyT – UADER
Niveles de ejecución (runlevels) en System V
¿Qué es un scriptscript?
Un script es un guión o conjunto de instrucciones. Permiten la automatización
de tareas creando pequeñas utilidades. Cada nivel de ejecución contiene scripts
que usan para iniciar, detener y reiniciar los distintos demonios del sistema.
¿Qué es un demoniodemonio?
Un demonio o daemon (de sus siglas en inglés Disk And Execution Monitor),
es un tipo especial de proceso informático que se ejecuta en segundo plano en
vez de ser controlado directamente por el usuario (es un proceso no interactivo).

<!-- página 19 -->

Práctica - SO -LSI – FCyT – UADER
Niveles de ejecución (runlevels) en System V
En cada directorio
 encontramos los scripts
 de inicio de los distintos
 servicios.

<!-- página 20 -->

Práctica - SO -LSI – FCyT – UADER
Niveles de ejecución (runlevels) en System V
Para concluir, en cualquier sistema GNU/Linux se ejecutan 2 procesos más, getty y login.
● getty: abre un puerto tty (o terminal virtual), en el cual se puede ejecutar un
 proceso. En la mayoría se las terminales se ejecuta el proceso login.
● login: ofrece un prompt para que el usuario ingrese al sistema y abre una
 shell para que el mismo interactúe.
init
getty
login
shell

<!-- página 21 -->

Práctica - SO -LSI – FCyT – UADER
Definición de Grupos de TPG
● 6  / 7 personas por Grupo
● Selección del sistema operativo
(no puede repetirse)
● Instalación en VirtualBox / Nativo
● Exposición del S.O en clase 9
(Contenidos mínimos)
● 15 / 20 Minutos por grupo
● Mostrar en el proyector el S.O
● Sitio Oficial
● Introducción / historia
● Licencia
● Costos y versiones
● Última versión y ciclo de publicaciones.
● Segmento S.O (Escritorio o Servidor)
● Orientación del S.O (multimedia,
auditoria, juegos, programación, etc..)
● Documentación
● Soporte
