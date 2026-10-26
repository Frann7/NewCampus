# Clase 6 Práctica

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/DIAPOS PARCIAL 1/Clase 6 Práctica.pdf` · 31 página(s) · texto extraído con pypdf.
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
| 28 |  |
| 29 |  |
| 30 |  |
| 31 |  |

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
exequiel.aramburu@uader.edu.ar
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Conversatorio de las herramientas Microsoft Windows(msconfig)
● Administración de Usuarios y Grupos GNU/Linux.
●  Administración de Permisos en el Sistema en GNU/Linux.
●  Practicas en laboratorio de usuarios, grupos y permisos en Debian GNU/Linux
o derivados.
● Actividad extra aúlica. Analizar los usuarios y grupos de Microsoft Windows.

<!-- página 3 -->

https://docs.microsoft.com/es-es/troubleshoot/windows-client/performance/system-configuration-utility-troubleshoot-configuration-errors

<!-- página 4 -->

2 a N usuarios trabajando en forma simultánea
característica heredada de Unix
utiliza ACL como mecanismo de control de acceso
define tipos de usuarios para el sistema
todo usuario pertenece a un grupo determinado

<!-- página 5 -->

Archivos de Configuración de Usuarios y Grupos
/etc/group/etc/group
/etc/passwd/etc/passwd
/etc/shadow/etc/shadow
contiene información de los usuarios del sistema
contiene información sobre la contraseña de los
usuarios
contiene información sobre los grupos del sistema

<!-- página 6 -->

Tipos de Usuarios en GNU/Linux
Usuarios especiales o del sistema
Usuarios normales
Súper Usuario o RootRoot

<!-- página 7 -->

Comandos básicos para el manejo de usuario:
Para mostrar información de los usuarios
Para manejo de usuario
who
w
finger
su
whoami
passwd

<!-- página 8 -->

Comandos básicos para el manejo de usuario:
who
w
finger
muestra información sobre los usuarios
logueados en el sistema
muestra información sobre los usuarios
logueados en el sistema y el comando que están
ejecutando
muestra información sobre los usuarios, su
directorio /home, su shell por defecto y su nombre
completo

<!-- página 9 -->

Comandos básicos para el manejo de usuario:
su
whoami
Permite cambiar de un usuario a otro, se utiliza
para cambiar a root o a súper usuario
Nos devuelve cual es el usuario con el que
estamos trabajando actualmente
passwd Permite cambiar nuestra contraseña o la de un
usuario determinado

<!-- página 10 -->

Todo archivo posee un usuario y un grupo determinados
Esto permite definir quien puede acceder a ese  y de que manera puede hacerlo
Para ello se utilizan reglas de control de acceso (ACL)
Dependiendo del tipo de archivo se pueden especificar distintos tipos de
permisos
ACLACL

<!-- página 11 -->

Administración de Usuarios:
Maneras de administrar usuarios Por línea de comandos
Editando archivos de configuración
Utilizando Herramientas gráficas

<!-- página 12 -->

Por línea de comandos
adduser
deluser
usermod
Administración de Usuarios:

<!-- página 13 -->

Comandos para la administración de usuarios:
adduser – agrega un usuario en el sistema
Sintaxis:
adduser <opciones> usuario
Opciones:
--home: permite especificar el directorio de inicio del usuario en el sistema.
--shell: permite especificar el interprete de comandos del usuario.
--no-create-home: no crea el directorio de inicio del usuario.
Ejemplos:
$adduser sistemas
$adduser --home /home/sistemas/juan juan

<!-- página 14 -->

Comandos para la administración de usuarios:
deluser – elimina un usuario del sistema
Sintaxis:
deluser <opciones> usuario
Opciones:
--backup: realiza un respaldo de los archivos que se encuentran en el home del usuario.
--backup-to: especifica el lugar donde se guardara el respaldo de la home del usuario.
--remove-all-files: remueve todos los archivos que sean propiedad del usuario a eliminar.
Ejemplos:
$deluser juan
$deluser --backup juan

<!-- página 15 -->

Comandos para la administración de usuarios:
usermod – modifica una cuenta de usuario del sistema
Sintaxis:
usermod <opciones> usuario
Opciones:
-e: se especifica la fecha en la cual se desactivará la cuenta de usuario.
-c: modifica el valor del campo de comentarios del archivo passwd del usuario.
-d: modifica la ubicación del directorio de inicio del usuario.
Ejemplos:
$usermod -d /home/usuarios/prog/juan juan
$usermod -c “Juan Perez”  juan

<!-- página 16 -->

Administración de Grupos:
Maneras de administrar grupos Por línea de comandos
Editando archivos de configuración
Utilizando Herramientas gráficas

<!-- página 17 -->

Por línea de comandos
Administración de Grupos:
addgroup
delgroup
groupmod

<!-- página 18 -->

Comandos para la administración de grupos:
addgroup – agrega un grupo en el sistema
Sintaxis:
addgroup <opciones> grupo
Opciones:
--version: muestra por pantalla la version del comando y copyright.
--help: muestra en pantalla ayuad del comando.
Ejemplos:
$addgroup sistemas
$addgroup --version

<!-- página 19 -->

Comandos para la administración de grupos:
delgroup – elimina un grupo del sistema
Sintaxis:
delgroup <opciones> grupo
Ejemplos:
$delgroup sistemas
$delgroup --backup juan
Opciones:
--version: muestra por pantalla la version del comando y copyright.
--help: muestra en pantalla ayuda del comando.

<!-- página 20 -->

Comandos para la administración de grupos:
groupmod – modifica una grupo de usuario del sistema
Sintaxis:
groupmod <opciones> grupo
Opciones:
-n: permite cambiar el nombre del grupo.
-g: permite cambiar el ID del grupo y debe ser un número entero positivo.
--help: muestra por pantalla la ayuda del comando.
Ejemplos:
$groupmod -n sistemas siste
$groupmod -g 767 sistemas

<!-- página 21 -->

Permisos
Establecen la forma en la que un usuario,
un grupo u otros usuarios pueden acceder
a un recurso

<!-- página 22 -->

Permisos
¿A quién?
¿Sobre qué?
UsuarioUsuario o Dueño
GrupoGrupo Asociado
Otros UsuariosOtros Usuarios
Archivos
Directorios

<!-- página 23 -->

Tipos de Permisos
Básicamente existen 3 tipos de
permisos
Lectura
Escritura
Ejecución
rr
ww
xx
ArchivoArchivo: ver su contenido
DirectorioDirectorio: listar su contenido
ArchivoArchivo: modificar su contenido
DirectorioDirectorio: borrar y renombrar
archivos contenidos en él
ArchivoArchivo: poder ejecutarlo
DirectorioDirectorio: poder acceder a él

<!-- página 24 -->

Entendiendo el esquema de permisos
- r w x r w x r w x
Archivo, Directorio o Enlace
Usuario
Grupo
Otros usuarios
d r w x r w - r - -
l r w x - - - - - -
- r w x r w x r w x
Algunos ejemplos

<!-- página 25 -->

Entendiendo el esquema de permisos
Octal Binario Significado
0 000 - - -
1 001 - - x
2 010 - w -
3 011 - w x
4 100 r - -
5 101 r - x
6 110 r w -
7 111 r w x
Permisos en forma numérica
Entonces: d r w x   r w -  r - -
7 6 4
-  r w -   r w -  r - -
6 6 4
l  r w x   - - -   - - -
7 0 0

<!-- página 26 -->

Por línea de comandos
Administración de Permisos
chmod
chown
chgrp

<!-- página 27 -->

Comandos para la administración de permisos:
chmod – modifica los permisos de un archivo
Sintaxis:
chmod <permisos> archivo
Opciones:
-R: permite que los permisos se apliquen a todos los subdirectorios de uno especificado
-v: muestra información sobre los cambios realizados
--help: muestra por pantalla la ayuda del comando.
Ejemplos:
$chmod +rwx /home/usuario -R
$chmod 750 miarchivo.dat

<!-- página 28 -->

Comandos para la administración de permisos:
chown – permite cambiar el dueño y/o grupo de un archivo
Sintaxis:
chown  usuario(:grupo) archivo
Opciones:
-R: permite que los permisos se apliquen a todos los subdirectorios de uno especificado
-v: muestra información sobre los cambios realizados
--help: muestra por pantalla la ayuda del comando.
Ejemplos:
$ chown usuario:usuario /home/usuario -R
$ chown root /root/ListadosUsuarios

<!-- página 29 -->

Comandos para la administración de permisos:
chgrp – permite cambiar el grupo de un archivo
Sintaxis:
chgrp  <grupo> archivo
Opciones:
-R: permite que los permisos se apliquen a todos los subdirectorios de uno especificado
-v: muestra información sobre los cambios realizados
--help: muestra por pantalla la ayuda del comando.Ejemplos:
$ chgrp www-data /var/www/sitios
$ chgrp ingenieria /home/jorge/ingenieria -R

<!-- página 30 -->

Analizar la administración de usuarios y grupos de Microsoft Windows
Actividad extra aúlica

<!-- página 31 -->

https://docs.microsoft.com/es-es/windows/security/identity-protection/access-control/local-accounts
Información oficial:
lusrmgr.msc
