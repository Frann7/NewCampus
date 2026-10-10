# Ingenieria_de_Software_II_Docker

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/SEGUNDO CUATRIMESTRE/Calidad de software/Ingenieria_de_Software_II_Docker.pdf` · 7 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Universidad Autónoma
de Entre Ríos
Facultad de Ciencia y Tecnología
INGENIERÍA DE SOFTWARE II
Calidad
Portabilidad
Docker
Contenedores, virtualización y orquestación
Lic. Paolo Orundés Cardinali
orundescardinali.paolo@uader.edu.ar
Lic. Damián Cian
cian.damian@uader.edu.ar
Lic. Pamela Bonadeo
bonadeo.pamela@uader.edu.ar
Cátedra · Ingeniería de Software II

<!-- página 2 -->

¿Qué es Docker?
02
Docker empaqueta una aplicación con todo lo que necesita para ejecutarse.
APLICACIÓN
Código fuente
DEPENDENCIAS
Librerías y paquetes
ENTORNO
Versión y configuración
El contenedor mantiene el mismo entorno en la notebook del desarrollador, en
el aula y en el servidor.
Ejemplos
Python + Flask
Node.js + Express
PHP + Apache
Java + Spring Boot
La portabilidad reduce diferencias entre ambientes.

<!-- página 3 -->

Conceptos principales
03
IMAGEN
Plantilla inmutable con la aplicación y sus dependencias.
python:3.13
CONTENEDOR
Instancia en ejecución de una imagen.
app-python
DOCKERFILE
Instrucciones para construir una imagen.
FROM python:3.13
COMPOSE
Define varios servicios relacionados.
web + base de datos
Una imagen puede crear muchos contenedores. Compose coordina el conjunto.

<!-- página 4 -->

Instalación tradicional y Docker
04
INSTALACIÓN TRADICIONAL DOCKER
× Lenguajes instalados en el sistema
× Posibles conflictos de versiones
× Configuración repetida en cada equipo
× Migración y limpieza más complejas
✓ Cada lenguaje vive en su contenedor
✓ Versiones y dependencias aisladas
✓ Entorno reproducible desde archivos
✓ Contenedores fáciles de recrear
Ejemplo: Python 3.13, Node.js 22, PHP 8.3 y Java 21 pueden convivir en un mismo equipo.

<!-- página 5 -->

Contenedores y máquinas virtuales
05
MÁQUINAS VIRTUALES CONTENEDORES
Aplicación Aplicación
Linux Windows
Hipervisor · Proxmox / VirtualBox
Hardware
Python Node PHP Java
Docker Engine
Sistema operativo + hardware
Cada VM incluye un sistema operativo completo. Los contenedores comparten el núcleo del host.
Uso combinado: una VM Linux en Proxmox puede alojar varios contenedores Docker.

<!-- página 6 -->

Ventajas de utilizar Docker
06
PORTABILIDAD
El mismo paquete viaja entre equipos.
CONSISTENCIA
Desarrollo y producción usan el mismo entorno.
AISLAMIENTO
Cada aplicación conserva sus versiones.
RAPIDEZ
Los contenedores arrancan en segundos.
REPRODUCIBILIDAD
Dockerfile y Compose documentan el entorno.
MANTENIMIENTO
Actualizar significa reemplazar y recrear.
Resultado: menos diferencias entre ambientes y despliegues más previsibles.

<!-- página 7 -->

Docker y Kubernetes
07
Docker construye y empaqueta. Kubernetes despliega y administra a escala.
1
Dockerfile
2
Imagen
3
Registro
4
Kubernetes
Kubernetes puede:
✓ crear varias instancias ✓ distribuir el tráfico ✓ reiniciar ante fallas
✓ escalar según la demanda ✓ actualizar sin detener el servicio
Actualmente Kubernetes suele ejecutar imágenes OCI mediante containerd, sin depender de Docker Engine.
