# Clase 14 Práctica

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Clase 14 Práctica.pdf` · 25 página(s) · texto extraído con pypdf.
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
| 10 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 11 |  |
| 12 |  |
| 13 |  |
| 14 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
| 15 |  |
| 16 |  |
| 17 |  |
| 18 |  |
| 19 | ⚠ ver el PDF (sin texto: escaneado o imagen) |
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
exequiel.aramburu@uader.edu.ar
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

<!-- página 2 -->

Práctica - SO -LSI – FCyT – UADER
Agenda
● Introducción a la administración de registros del sistema  (Logs).
● Registros locales de S.O y Servidores de Logs.
● Archivos de registros mas importantes del S.O en GNU/Linux.
● Rotación de registros del S.O en GNU/Linux.
● Visualizar y administrar los registros del S.O en GNU/Linux desde la terminal.
● Visualizar y administrar los registros del S.O en GNU/Linux con Herramientas Graficas.
● Actividad extra aúlica. Visualizar y administrar los registros
del S.O en Microsoft Windows.

<!-- página 3 -->

¿QUÉ SON LOS LOGS O REGISTROS?
Introducción
 Los logs son registros de los eventos que se generan en los servidores,
aplicaciones, redes y sistemas de una organización. Cada uno de estos archivos
contiene información relacionada a un evento específico que ocurrió dentro de un
equipo, sistema o red.(Vieda, 2013)
https://www.boletinoficial.gob.ar/detalleAviso/primera/216860/20190918
Glosario de Términos de Ciberseguridad establecida por la Resolución
1523/2019
Fuente:

<!-- página 4 -->

https://www.ccn-cert.cni.es/pdf/guias/glosario-determinos/22-401-descargar-glosario/file.html Fuente:
CENTRO CRIPTOGRÁFICO NACIONAL (ESPAÑA): GUÍA DE SEGURIDAD (CCN-STIC-
401) GLOSARIO Y ABREVIATURAS
Nota: Instituto Nacional de Tecnologías de la Comunicación (INTECO) su actividad se focalizó en el
ámbito de la ciberseguridad y en 2014 paso a denominarse Instituto Nacional de Ciberseguridad (INCIBE)

<!-- página 5 -->

Instituto Nacional de Ciberseguridad de España (Incibe)
https://www.incibe.es/sites/default/files/contenidos/guias/doc/guia_glosario_ciberseguridad_2021.pdf
Glosario de términos de ciberseguridad

<!-- página 6 -->

● El log es un registro oficial de eventos  que se guardan en un equipo por un periodo de
tiempo establecido.
● Cuando un evento ocurre el log generado debe responde las siguientes preguntas:
¿Quién?, ¿Qué?, ¿Cuándo?, ¿Dónde? y Por qué?
● Los logs son ficheros de texto o base de datos donde se guarda información de eventos.
Estos eventos pueden ser:
Logs de sistema : Generalmente generados por el demonio (ej:Rsyslogd). Registran
información relacionada con el funcionamiento del sistema operativo. Algunos ejemplos de
logs de sistema son los que registran información sobre los servicios, los que registran los
accesos al equipo, los mensajes del sistema, etc.
Logs de programas : Son aquellos que registran cronológicamente los eventos más
importantes mientras estamos usando una aplicación o programa. En este caso, los logs
pueden ser generados por la propia aplicación o por un demonio (ej:Rsyslogd).

<!-- página 7 -->

Logs Locales - Algunas ventajas:
● Detección de ataques e intrusos
● Detección de problemas de hardware/software
● Análisis forense de sistemas. Preservación de la
información.
● Evaluación de vulnerabilidad
● Cumplimiento de la normativa legal o log de eventos con
fines de auditoría.

<!-- página 8 -->

Syslog puede enviar información sobre TCP o UDP indistintamente. Por convención se
usa el puerto 514 UDP
Servidor de Logs

<!-- página 9 -->

Servidor de Logs – Algunas ventajas:
● Preservación de la información.
● Respaldo centralizado.
● Almacenamiento centralizado en base de datos.
● Exploración y visualización avanzada: gráficos, tablas, etc.
● Detección de anomalías integrales.
● Cumplir estándares  de seguridad.
● Trazabilidad de los eventos.
● Optimización de los análisis.
● Filtrado avanzado.

<!-- página 10 -->

Algunos ejemplos:

<!-- página 11 -->

Rotación de logs
Cuando hablamos de rotación de logs, nos referimos a lo siguiente:
● Determinar el tamaño máximo permitido para un archivo de log.
● Cuando se alcanza dicho tamaño, borrar el archivo, renombrarlo o
comprimirlo y crear uno nuevo.
● Especificar por cuánto tiempo deseamos mantener los registros, ya sea
comprimidos o no.

<!-- página 12 -->

En GNU/Linux → Logrotate
/etc/logrotate.conf
Logrotate es una utilidad de sistema que administra la compresión y rotación de archivos
de logs en sistemas Linux. Si los logs no se rotan, comprimen y depuran de manera
periódica, eventualmente pueden consumir todo el espacio en disco disponible en el
sistema.

<!-- página 13 -->

Archivos de registros mas importantes del S.O GNU/Linux.
 /var/log

<!-- página 14 -->

/var/log

<!-- página 15 -->

Comando dmesg
dmesg --level=alert,crit
dmesg -T
dmesg (diagnostic message, mensajes de diagnóstico) es un comando
presente en los sistemas operativos Unix que lista el buffer de mensajes
del núcleo. Este buffer contiene una gran variedad de mensajes
importantes generados durante el arranque del sistema y durante la
depuración de aplicaciones. La información ofrecida por dmesg puede
guardarse en el disco duro mediante un demonio de registro, como syslog.
Imprima marcas de tiempo legibles por humanos.
imprimirá mensajes de error y advertencia solamente.
dmesg --help imprimirá la ayuda.

<!-- página 16 -->

gnome-logs
 Herramientas Graficas
https://wiki.gnome.org/Apps/Logs

<!-- página 17 -->

ksystemlog
 Herramientas Graficas
https://apps.kde.org/es/ksystemlog

<!-- página 18 -->

KSystemLog muestra todos los registros del sistema, agrupados por servicios generales
(registro predeterminado del sistema, autenticación, kernel, X.org...) y opcionales (Apache,
Cups...). Incluye diversas funcionalidades para leer los archivos de registro de forma
agradable:
● Líneas de registro coloreadas según su severidad
● Vista en pestañas para poder mostrar varios registros a la vez
● Muestra de forma automática las nuevas líneas registradas
● Información detallada para las líneas de cada registro
Nota:  Los instaladores para Windows también se pueden descargar de la binary-factory.
https://binary-factory.kde.org/

<!-- página 19 -->

Visor de Eventos

<!-- página 20 -->

Visor de Eventos
msconfig→ Visor de Eventos
Ejecutar→ eventvws

<!-- página 21 -->

Visor de Eventos
El Visor de eventos puede gestionar registro de acontecimientos dentro de:
● Eventos reenviados. Aquellos registros que se reciben desde otra máquina.
● Eventos de software. Esto engloba registros como errores o avisos que proceden de nuestras
aplicaciones y programas. Los eventos referidos a errores son los más importantes, las advertencias
le precederían con un grado más bajo de riesgo.
● Eventos de seguridad. Este apartado está relacionado con los registros en relación con auditorías
dentro de los inicios de sesión pudiendo saber si un usuario ha podido logarse correctamente o no.
Puede darnos una idea de quién ha intentado usar nuestro equipo y cuándo.
● Eventos del sistema. Aquí se almacenan acontecimientos sobre el propio sistema y todo lo
relacionado a cómo funciona.
● Eventos de configuración. Registros en relación a máquinas establecidas como controladores de
dominio.
https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor

<!-- página 22 -->

Práctica de Laboratorio 1
Ejecute dos terminales (1 y 2).
En la terminal 1 monitorear el archivo de logs ejecutando el
siguiente comando:
1
2
3 En la terminal 2, intente autenticarse con el usuario root e
ingrese una contraseña incorrecta.
su root
Identificar intentos fallidos autenticación en el log auth.log
tail -f -n 18 /var/log/auth.log
4
Desde la terminal 1, identifique el intento fallido

<!-- página 23 -->

Práctica de Laboratorio 2
Ejecute una terminal
Cree un usuario con el comando:
1
2
3
Identificar usuario nuevos en el archivo de log:
adduser prueba
En el archivo de log auth.log identifique el usuario creado.

<!-- página 24 -->

Práctica de Laboratorio 3
Ejecute el visor de eventos grafico (ej: registros,
KsystemLog,etc)
Identifique los eventos de la práctica de laboratorio 1 y 2
1
2
Identificar usuario nuevos en el archivo de log:

<!-- página 25 -->

1)Realizar ambas pruebas de laboratorio (1 y 2) en Microsoft Windows e
identificar en el visor de sucesos los eventos cada una de ellas.
2) Crear un filtro con los eventos del punto 1.
3) Exportar los resultados del filtro personalizado.
4) Exponer en la clase próxima los 3 puntos anteriores.
Actividad extra aúlica
GRUPO  6
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
