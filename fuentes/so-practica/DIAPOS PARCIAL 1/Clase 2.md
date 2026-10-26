# Clase 2

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/DIAPOS PARCIAL 1/Clase 2.pdf` · 18 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Sistemas Operativos
Práctica
Lic. Exequiel Aramburu
exequiel.aramburu@uader.edu.ar
Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

<!-- página 2 -->

Sistemas Operativos
Práctica
Virtualización

<!-- página 3 -->

Práctica - SO -LSI – FCyT – UADER
¿Qué es la Virtualización?
La virtualización es una tecnología informática que simula la funcionalidad
 del hardware para crear servicios de TI basados   en software, como aplicaciones,
 servidores, almacenamiento y redes.
(https://www.citrix.com/es-mx/glossary/what-is-virtualization.html)

<!-- página 4 -->

Práctica - SO -LSI – FCyT – UADER
¿Qué es una máquina virtual?
Una máquina virtual (VM) es un entorno virtual que funciona como una
 computadora dentro de una computadora. Se ejecuta en una partición aislada de su
 computadora host con sus propios recursos de potencia de CPU, memoria,
 un sistema operativo (por ejemplo, Windows, Linux, macOS) y otros recursos. Esto
 permite a los usuarios finales ejecutar aplicaciones en máquinas virtuales y
 utilizarlas como lo harían normalmente en su estación de trabajo.
(https://www.citrix.com/es-mx/glossary/what-is-a-virtual-machine.html)

<!-- página 5 -->

Práctica - SO -LSI – FCyT – UADER
¿Qué es un monitor de máquinas virtuales o hipervisor?
Un hipervisor, conocido también como monitor de máquinas virtuales, es un
 proceso que crea y ejecuta máquinas virtuales. Un hipervisor permite que un
 ordenador host preste soporte a varias máquinas virtuales invitadas mediante
 el uso compartido virtual de sus recursos, como la memoria y el procesamiento.
(https://www.vmware.com/latam/topics/glossary/content/hypervisor.html)

<!-- página 6 -->

Tipos de hipervisores

<!-- página 7 -->

Práctica - SO -LSI – FCyT – UADER
Tipos de hipervisores
En general, hay dos tipos de hipervisores. Los hipervisores de tipo 1, denominados
 «hipervisores bare metal», se ejecutan directamente en el hardware del host.
 Los hipervisores de tipo 2, denominados «alojados», se ejecutan como una capa
 de software sobre un sistema operativo, como otros programas informáticos.
(https://www.vmware.com/latam/topics/glossary/content/hypervisor.html)

<!-- página 8 -->

Práctica - SO -LSI – FCyT – UADER
Hipervisor tipo 1
Denominados “bare metal” (metal desnudo/metal básico), se ejecuta directamente
 sobre el hardware del host, es decir, en equipos sin sistemas operativos.
 Por lo tanto, los recursos de las VMs se programan directamente sobre el hardware.
Hipervisor de tipo 1
Windows Linux ...
Excel Word
Calc Writer

<!-- página 9 -->

Práctica - SO -LSI – FCyT – UADER
Hipervisor tipo 1 (Ventajas)
● Mejora el rendimiento.
● Mejor manejo de recursos.
● Estabilidad.

<!-- página 10 -->

Práctica - SO -LSI – FCyT – UADER
Hipervisor tipo 1 (Desventajas)
● Requiere de soporte en hardware a nivel del CPU.
● Dedicación exclusiva de hardware.
● Solo para entornos empresariales (desventaja de nuestro punto de vista).
● Se requieren 2 computadoras, una para virtualizar y otra para acceder.

<!-- página 11 -->

Práctica - SO -LSI – FCyT – UADER
Hipervisor tipo 1 (Demo)
Demostración de Citrix XenCenter
https://www.citrix.com/es-mx/downloads/citrix-hypervisor/
Otras alternativas: Proxmox, Red Hat Linux KVM, VMware ESXi y Microsoft Hyper-V Server.
Requisitos
RAM
2 GB Minimo
4 GB Recomendado
DISCO
46 GB Mínimo
70 GB Recomendado

<!-- página 12 -->

Práctica - SO -LSI – FCyT – UADER
Hipervisor tipo 2
Denominados “alojados”, se ejecutan como una capa de software sobre un sistema
 operativo de una computadora física “host”. Su ejecución es similar a un programa
 o aplicación.
Hipervisor de tipo 2
SO huésped
Proceso huésped del SO
Proceso
 anfitrión
 del SO
Sistema operativo anfitrión

<!-- página 13 -->

Práctica - SO -LSI – FCyT – UADER
Hipervisor tipo 2 (Ventajas)
● Encender y apagar máquinas virtuales a demanda.
● No requiere computadoras potentes.

<!-- página 14 -->

Práctica - SO -LSI – FCyT – UADER
Hipervisor tipo 2 (Desventajas)
● Recursos limitados.
● Funciona bajo S.O. host, por lo que si este falla, perjudica a las VMs.
● Compite por los recursos con otros procesos.
● Menor performance que las tipo 1.

<!-- página 15 -->

Práctica - SO -LSI – FCyT – UADER
Hipervisor tipo 2 (Demo)
Demostración Oracle VirtualBox
https://www.virtualbox.org/wiki/Downloads
Otras alternativas: Microsoft Virtual PC y VMware Workstation.

<!-- página 16 -->

Práctica - SO -LSI – FCyT – UADER
Ventajas de la virtualización
● Aislamiento.
● Seguridad.
● Flexibilidad.
● Agilidad.
● Portabilidad.
● Recuperación rápida en caso de fallo.
● Ahorro de energía.
● Ahorro de dinero.
● Administración centralizada.

<!-- página 17 -->

Práctica - SO -LSI – FCyT – UADER
Desventajas de la virtualización
● Necesidad de hardware de altas prestaciones (requiere de una inversión
grande).
● Dependencia de un S.O., muchos sistemas dependen de un solo equipo.
● Limitaciones en el hardware de las máquinas virtuales.
● Problemas de compatibilidad entre algunos hipervisores.

<!-- página 18 -->

Práctica - SO -LSI – FCyT – UADER
¿Para qué sirve virtualizar?
● Probar sistemas operativos nuevos.
● Experimentar migraciones a sistemas operativos nuevos.
● Testear aplicaciones o migración de aplicaciones.
● Mantener sistemas operativos obsoletos con aplicaciones antiguas.
● Ejecutar archivos infectados y probar comportamientos.
● Crear copias de seguridad.
