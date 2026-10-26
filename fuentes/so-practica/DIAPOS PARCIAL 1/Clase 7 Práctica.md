# Clase 7 Práctica

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/DIAPOS PARCIAL 1/Clase 7 Práctica.pdf` · 23 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
exequiel.aramburu@uader.edu.ar
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

<!-- página 2 -->

Proceso
Programa Proceso!=

<!-- página 3 -->

GNU/Linux como Sistema Operativo Multitarea
● Múltiples procesos pueden ejecutarse “simultáneamente” sin interferir entre sí.
● Cada proceso “cree” que se está ejecutando solo en el sistema y que tiene       acceso a todos los
recursos del mismo.
● Todos los procesos tienen siempre un determinado estado en el tiempo.
● El sistema operativo mantiene información de todos sus procesos y de su estado.
●  Para cada proceso deben reservarse recursos y asignarse prioridades.

<!-- página 4 -->

Procesos en GNU/Linux
● Init es el primer proceso a ejecutarse por el núcleo. Corre con un identificador de proceso (PID) igual a
1.
● Debe encontrarse siempre en ejecución ya que es el “Padre” de todos los  demás procesos.
● Este proceso realiza varias acciones como vimos anteriormente y finalmente ejecuta varias instancias
(forks) del proceso getty.
init
getty
cron
klogd
...
login bash

<!-- página 5 -->

Gestión de Procesos
Constantemente el núcleo y las aplicaciones de usuarios envían señales a los procesos para modificar su estado.
Usuarios
Aplicaciones
Núcleo
Proceso 1Proceso 1
Proceso 2Proceso 2
Proceso 3Proceso 3
Señal 2
Señal 15
Señal 9
Para enviar señales utilizaremos el comando kill

<!-- página 6 -->

Gestión de Procesos
Señales
15 – SIGTERM: Solicita la terminación del proceso
que la recibe.
9 – SIGKILL: Termina el proceso que la recibe en
forma inmediata.
2 – SIGINT: Es la misma señal que se produce
cuando un usuario presiona las teclas “Control + C”
para solicitar su terminación
20 – SIGSTP: Es la misma señal que se produce
cuando un usuario presiona las teclas “Control + Z”
para mandar un proceso a segundo plano.
19 – SIGCONT: Reanuda un proceso suspendido
con SIGSTP.

<!-- página 7 -->

Gestión de Procesos
Información
sobre
procesos
Identificador de Proceso (PID)
Identificador de Proceso Padre (PPID)
Valor de los Registros
Información sobre Usuarios y Grupos
Prioridad con respecto a otros
Recursos consumidos por el proceso
Estado del proceso

<!-- página 8 -->

Herramientas para trabajar con procesos
Para visualizar procesos
Para enviar señales a procesos
ps
top
htop
pstree
kill
nice
renice
killall

<!-- página 9 -->

Herramientas para la administración de procesos
Examinando la salida del comando ps
● Usuario con el que se ejecuta el proceso.
● Identificador de Proceso (PID)
●% de uso de CPU y de Memoria
● Terminal en la que se ejecuta el comando.
●Fecha de Inicio
● Comando que se ejecuta

<!-- página 10 -->

Herramientas para la administración de procesos
top – muestra la lista de procesos que consumen más recursos en el sistema
Sintaxis:
top <opciones>
Opciones:
-s:deshabilita el modo interactivo.
-c: muestra el path absoluto con el que fue llamado cada comando de la lista.
-d <segundos>:permite especificar los segundos de espera entre muestreos.
Ejemplos:
$top -c
$top -d 1

<!-- página 11 -->

Herramientas para la administración de procesos
htop – muestra la lista de procesos y nos permite gestionarlos.
Sintaxis:
htop
Comandos en modo interactivo:
F1 – Muestra la ayuda
F6 – Permite ordenar los procesos por consumo de memoria, consumo de cpu, usuario o
        PID.
F10 – Sale de htop.
Ejemplos:
htop

<!-- página 12 -->

Herramientas para la administración de procesos
kill – permite enviar señales a un proceso
Sintaxis:
kill <opciones> <señal> PID
Opciones:
-l: muestra una tabla con las señales disponibles y sus respectivos números.
-s señal: permite especificar una señal por su nombre para enviar a un proceso.
-n señal: permite especificar una señal por su número para enviar a un proceso.
Ejemplos:
kill -9 9873
kill -SIGKILL 3482

<!-- página 13 -->

Herramientas para la administración de procesos
killall – permite enviar señales a un proceso usando su nombre
Sintaxis:
killall <opciones> <señal> nombre
Opciones:
-l: muestra una tabla con las señales disponibles y sus respectivos números.
-s señal: permite especificar una señal por su nombre para enviar a un proceso.
-n señal: permite especificar una señal por su número para enviar a un proceso.
Ejemplos:
killall -9 kde
killall -SIGKILL amsn

<!-- página 14 -->

Herramientas para la administración de procesos
nice – cambia la prioridad de un proceso a la hora de ejecutarlo.
Sintaxis:
nice <opciones> <proceso> argumento del proceso
Opciones:
-n: permite especificar un número entero para definir la prioridad del proceso.
--version: permite mostrar la versión actual del comando.
--help: muestra la ayuda del comando
Ejemplos:
# nice -n -20 apt-get update

<!-- página 15 -->

Herramientas para la administración de procesos
renice – cambia la prioridad de un proceso en ejecución
Sintaxis:
renice prioridad <-p pid> <-g grupo> <-u usuario>
Opciones:
-p pid: espeficica el PID del proceso al cual queremos modificar la prioridad
-g grupo: permite cambiar el ID del grupo asociado al proceso.
-u usuario: permite cambiar el ID del usuario asociado al proceso.
Ejemplos:
$renice +1 -p 897
$renice +2 2308 -u usuario

<!-- página 16 -->

Herramientas para la administración de procesos
free – muestra la utilización de memoria del sistema
Sintaxis:
free <opciones>
Opciones:
-m: muestra la memoria en megabytes.
-t: muestra totales de memoria en las columnas de total, usada y libre.
-s intervalo: muestra el uso de la memoria y se actualiza pasado un intervalo de tiempo.
Ejemplos:
$ free -tm
$ free -s 2

<!-- página 17 -->

Herramientas para la administración de procesos
uptime – indica el tiempo que lleva el sistema encendido.
Sintaxis:
uptime <opciones>
Opciones:
-V: muestra la versión del programa
Ejemplos:
$ uptime
$ uptime -V

<!-- página 18 -->

Herramientas para la administración de procesos
watch – permite ejecutar un comando periódicamente
Sintaxis:
watch <opciones> comando
Opciones:
-n: permite especificar un intervalo de tiempo para ejecutar un comando.
-t: permite no mostrar en la salida el comando que se utiliza
--help: muestra la ayuda del comando
Ejemplos:
$ watch -n 5 date
$ watch -t date

<!-- página 19 -->

Herramientas para la administración de procesos
pgrep – busca los procesos que tienen atributos determinados.
Sintaxis:
pgrep <opciones> <patrón>
Opciones:
-G: permite especificar el nombre de un grupo para poder buscar procesos.
-I: muestra la salida del comando en formato largo agregando el nombre del proceso.
-U intervalo: permite especificar el nombre de un usuario para poder buscar procesos.
Ejemplos:
$ pgrep -G usuario
$ pgrep -L apache2

<!-- página 20 -->

Herramientas para la administración de procesos
pstree – muestra los procesos en forma de árbol.
Sintaxis:
pstree <opciones>
Opciones:
-u: permite mostrar el nombre del usuario propietario del proceso.
-p: permite mostrar el PID del proceso.
Ejemplos:
$ pstree
$ pstree -U

<!-- página 21 -->

Herramientas para la administración de procesos
fg, bg – permiten manipular y enviar procesos a primer y a segundo plano
Sintaxis:
fg, bg %número de trabajo
Ejemplos:
$ bg -
$ fg %1

<!-- página 22 -->

Herramientas para la administración de procesos
nohup – ejecuta un comando y no permite que reciba más señales de hup, term y
kill del sistema.
& - le indica a la shell que un proceso se ejecute en segundo plano
Sintaxis:
nohup comando <argumentos>
Opciones:
--version: muestra la versión del comando nohup.
--help: muestra la ayuda del comando
Ejemplos:
$ nohup sleep 60 &
$ yes > /dev/null &

<!-- página 23 -->

Herramientas para la administración de procesos
jobs – permite ver los procesos detenidos o en segundo plano en una shell
Sintaxis:
jobs <opciones>
Opciones:
-l: permite ver el PID de las tareas
-p: muestra únicamente el PID de las tareas
Ejemplos:
$ jobs
$ jobs -l
