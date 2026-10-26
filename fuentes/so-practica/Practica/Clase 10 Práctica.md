# Clase 10 Práctica

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Clase 10 Práctica.pdf` · 19 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |
| 9 |  |
| 10 |  |
| 11 |  |
| 12 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 13 |  |
| 14 |  |
| 15 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 16 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 17 |  |
| 18 |  |
| 19 |  |

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
exequiel.aramburu@uader.edu.ar
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Hilos en POSIX.
● Hilos. Práctica de Laboratorio utilizando el lenguaje C.
● Condición de carrera. Práctica de Laboratorio utilizando el lenguaje C.
● Administración de tareas GNU/Linux (Crontab).
● Prácticas de administración de tareas programadas en GNU/Linux.
● Actividad extra aúlica. Analizar las administración de tareas programadas
 de Microsoft Windows.

<!-- página 3 -->

Hilos en POSIX

<!-- página 4 -->

● Para poder utilizar la interfaz de los hilos es necesario incluir la cabecera a pthread.h.
Además, a la hora de compilar hay que enlazar el código con la opcion -pthread.
  gcc hilos.c -o hilos -pthread
● La creación de un hilo se hace mediante  pthread_create. A partir de este punto, si la función
no produce error, hay dos hilos de ejecución: el del programa invocante y otro cuyo nombre
de función se pasa por parámetro y en nuestro caso se corresponde con  primos_h. Dicha
función recibe un puntero a datos y devuelve otro, en nuestro caso &tdata. Típicamente, el
hilo invocante usa el ultimo parámetro de hilo para enviar datos de entrada al nuevo hilo.
   pthread_create (&h1 , NULL , (void *) primos_h, (void *) &tdata1);
● El resultado del hilo se devuelve cuando la función con la que se crea el hilo finaliza. El hilo
devuelve un puntero cuyos resultados se pueden recoger, mas tarde,
con pthread_join desde el hilo padre que lo ha creado.
pthread_join (h1 , NULL );

<!-- página 5 -->

EJEMPLO DE HILOS
Calculando números primos
MONONUCLEO
1 Proceso
*MULTINUCLEO
X Hilos

<!-- página 6 -->

DESCARGAR EL CÓDIGO FUENTE
COMPILAR EL CÓDIGO FUENTE
  gcc hilos.c -o hilos -pthread
Práctica de hilos
EJECUTAR EL PROGRAMA
       ./hilos
Del campus -->

<!-- página 7 -->

2 Terminales
Ejecutando el programa
Ejecutando htop

<!-- página 8 -->

Práctica
Ejecute el programa hilos y registre los resultados en la siguiente tabla:
Hilos/Buscar Primos
encontrados 1 2 4 6 8 10 12
200.000
   X X segundos
500.000
1.000.000
Procesador:  X
Núcleos/hilos:   X/X
cat /proc/cpuinfo

<!-- página 9 -->

Práctica
Resultado en mi PC.
Hilos/Buscar Primos
encontrados 1 2 4   6 8 10 12
200.000 17.984  4,36 3,17 1,972 1,45 1,26 1,12 1,12
500.000 41.538   23,99 17,79 10,62 7,54 6,32 5,53 5,32
1.000.000 78.498 90,31 66,87 39,25 27,57 23,03 20,15 18,63
Procesador: Intel(R) Core(TM) i5-10400F CPU @ 2.90GHz
Núcleos/hilos:   6 núcleos / 12 hilos

<!-- página 10 -->

Práctica de condición de carrera
Depurar programas que contienen condiciones de carrera no es nada divertido. Los resultados de la
mayoría de las ejecuciones de prueba están bien, pero en algún momento poco frecuente ocurrirá algo
extraño e inexplicable.
Tanenbaum, A., Stallings, W., & Kerrish, M. Sistemas Operativos modernos., 3ra edición.
Stallings, W., Aguilar, L. J., Dodero, J. M., Torres, E., & Mora, M. K. (1997).Â Sistemas operativos (Vol. 732). Prentice Hall.

<!-- página 11 -->

  gcc carrera_condicion.c -o carrera_condicion -pthread
Práctica de condición de carrera
Del campus -->
DESCARGAR EL CÓDIGO FUENTE
COMPILAR EL CÓDIGO FUENTE
EJECUTAR EL PROGRAMA
       ./carrera_condicion

<!-- página 12 -->



<!-- página 13 -->

Configuración del Crontab

<!-- página 14 -->

Configuración del Crontab

<!-- página 15 -->

Comandos crontab

<!-- página 16 -->



<!-- página 17 -->

 cada minuto.
 cada hora, en el minuto 0.
diaria a las 4 de la mañana.
 cada 10 minutos.
cada hora entre las 9 de la
mañana y las 20 de la
tarde de lunes a viernes.
cada hora desde las 9 de la
mañana hasta las 20 de la
tarde.
 A las 9 de la mañana y a las
20 de la tarde (2 veces al día).
EJEMPLOS DETALLE
* * * * * /home/aramburu/scripts/script.sh
0 * * * * /home/aramburu/scripts/script.sh
0 4 * * * /home/aramburu/scripts/script.sh
0 9,20 * * * /home/aramburu/scripts/script.sh
0 9-20 * * * /home/aramburu/scripts/script.sh
0 9-20 * * 1-5 /home/aramburu/scripts/script.sh
*/10 * * * * /home/aramburu/scripts/script.sh

<!-- página 18 -->

ACTIVIDAD DE LABORATORIO
Programe un cron para que se ejecute cada minuto y borre el archivo llamado prueba.txt si existe
en el directorio antes creado.
Cree un directorio llamado Clase10 en su home.
Cree un archivo llamado prueba.txt  y verifique el correcto funcionamiento del cron.

<!-- página 19 -->

Analizar la administración de tareas programadas en Microsoft Windows
Actividad extra aúlica
