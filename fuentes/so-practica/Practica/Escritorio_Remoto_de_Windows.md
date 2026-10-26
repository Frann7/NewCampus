# Escritorio_Remoto_de_Windows

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/SO PRACTICA/Practica/Escritorio_Remoto_de_Windows.pdf` · 8 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Escritorio Remoto de
Windows:
 Integrantes: (los nombres no se copian: el repo es público)

<!-- página 2 -->

1. Introducción al
Escritorio Remoto y su
Propósito
 ¿Qué es?
 Protocolo: Se basa en el RDP (Remote Desktop
Protocol) de Microsoft.
 Usos Principales:
- Soporte técnico a distancia.
- Administración de servidores.
- Trabajo remoto (Home Office).

<!-- página 3 -->

2. Arquitectura: ¿Cómo
Funciona?
 Modelo Cliente-Servidor:
 - Servidor: Escucha peticiones y comparte su
escritorio.
 - Cliente: Inicia la conexión para controlar al
servidor.
 Flujo de Datos: El servidor envía la imagen de su
pantalla; el cliente envía las acciones del teclado
y ratón.
 Puerto de Red: Utiliza el puerto TCP 3389 por
defecto.

<!-- página 4 -->

3. Requisitos y Ediciones
de Windows Compatibles
 Para ser Servidor (Anfitrión):
 SÍ: Windows 10/11 Pro, Enterprise, Education y
Windows Server.
 NO: Windows Home.
 Para ser Cliente:
 CUALQUIER edición de Windows.
 También disponible para macOS, iOS, Android y
Linux.

<!-- página 5 -->

4. Seguridad: Permisos y
Cifrado
 Autenticación a Nivel de Red (NLA): Verifica al
usuario ANTES de establecer la sesión completa.
Es la primera barrera de defensa.
 Grupo 'Usuarios de Escritorio remoto':
 Por defecto, solo Administradores pueden
conectar. Para dar acceso a otros, deben ser
añadidos a este grupo específico.
 Cifrado: Toda la comunicación entre cliente y
servidor viaja encriptada.

<!-- página 6 -->

5. El Cliente (mstsc.exe) y
sus Opciones
 Conexión simple: Solo se necesita la IP o el
nombre del equipo.
 Opciones Avanzadas:
 - Pantalla: Configurar resolución y usar múltiples
monitores.
 - Recursos locales: Compartir impresoras,
portapapeles y unidades de disco para transferir
archivos.
 - Rendimiento: Ajustar la calidad gráfica según la
velocidad de la red.

<!-- página 7 -->

6. Limitaciones de
Sesiones Concurrentes
 Windows de Escritorio (Pro):
- Política de una única sesión activa.
- Si te conectas remotamente, la sesión física en el
PC se bloquea.
- Si alguien inicia sesión físicamente, la sesión remota
se desconecta.
 Windows Server:
- Diseñado para múltiples usuarios simultáneos
usando Servicios de Escritorio Remoto (RDS) y
licencias CAL.

<!-- página 8 -->

7. Ventajas, Desventajas y
Alternativas
- Ventajas:
- Nativo de Windows (sin instalar nada extra).
- Centralización de datos y software.
- El cliente puede ser un equipo de bajos recursos.
- Desventajas:
- Dependencia total de una conexión de red
estable.
- Rendimiento deficiente en aplicaciones graficas
intensivas
- Alternativas Populares: TeamViewer, AnyDesk,
Chrome Remote Desktop, VNC.
