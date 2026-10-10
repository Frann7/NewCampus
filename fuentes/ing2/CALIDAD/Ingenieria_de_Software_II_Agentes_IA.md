# Ingenieria_de_Software_II_Agentes_IA

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/SEGUNDO CUATRIMESTRE/Calidad de software/Ingenieria_de_Software_II_Agentes_IA.pdf` · 9 página(s) · texto extraído con pypdf.
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

<!-- página 1 -->

Universidad Autónoma de Entre Ríos
Facultad de Ciencia y Tecnología
INGENIERÍA DE SOFTWARE II
AGENTES DE IA
PARA PROGRAMACIÓN
Del asistente conversacional a la ejecución de tareas sobre un proyecto
Lic. Paolo Orundés Cardinali
orundescardinali.paolo@uader.edu.ar
Lic. Damián Cian
cian.damian@uader.edu.ar
Lic. Pamela Bonadeo
bonadeo.pamela@uader.edu.ar
Codex · Claude Code · OpenCode

<!-- página 2 -->

¿Qué es un agente de IA para programación?
02
Es un sistema que interpreta un objetivo y actúa sobre un entorno de desarrollo para alcanzarlo.
PERCIBE
Lee consignas, archivos, estructura del
proyecto y resultados.
RAZONA
Analiza el problema, propone un plan y
decide el próximo paso.
ACTÚA
Edita código, ejecuta comandos, consulta
documentación y usa herramientas.
VERIFICA
Ejecuta pruebas, observa errores y ajusta
la solución.
Un chatbot sugiere código. Un agente puede intervenir directamente en el proyecto.
Modelo conceptual: agente que percibe su entorno y realiza acciones orientadas a objetivos.

<!-- página 3 -->

Del pedido a una solución verificada
03
El agente alterna razonamiento, acciones y observaciones del entorno.
1  OBJETIVO
“Corregir el error de autenticación”
→
2  PLAN
Localizar archivos, comprender el
flujo y definir cambios
→
3  ACCIÓN
Modificar código y ejecutar
comandos o herramientas
→
4  VALIDACIÓN
Correr pruebas, revisar resultados y
corregir
Si la validación falla, el resultado vuelve a alimentar el ciclo.
Razonar → actuar → observar → ajustar

<!-- página 4 -->

Codex
04
OPENAI Agente que trabaja directamente sobre proyectos de software.
Comprensión del proyecto
Explora archivos, dependencias e instrucciones del repositorio.
Implementación
Crea, modifica y refactoriza código en múltiples archivos.
Ejecución
Utiliza terminal, herramientas y entornos de desarrollo.
Verificación
Ejecuta pruebas y revisa los resultados antes de entregar.
Idea clave: convierte una consigna en cambios concretos y verificables.

<!-- página 5 -->

Claude Code
05
ANTHROPIC Agente de programación orientado al trabajo desde la terminal.
Análisis contextual
Comprende proyectos extensos y relaciones entre archivos.
Desarrollo
Implementa funcionalidades, refactoriza y corrige errores.
Herramientas
Ejecuta comandos e interactúa con flujos de desarrollo.
Instrucciones
Puede utilizar reglas y memoria contextual propias del proyecto.
Idea clave: colaboración en lenguaje natural con fuerte contexto del proyecto.

<!-- página 6 -->

OpenCode
06
CÓDIGO ABIERTO Plataforma abierta para utilizar distintos modelos de IA.
Elección del modelo
Permite conectarse con modelos de diferentes proveedores.
Modos de trabajo
Diferencia planificación, análisis y construcción.
Personalización
Admite agentes especializados, permisos, comandos y extensiones.
Entornos
Disponible para terminal, escritorio e integración con editores.
Idea clave: separa la herramienta de trabajo del modelo de IA elegido.

<!-- página 7 -->

Tres alternativas, una misma lógica de trabajo
07
CODEX
OpenAI
Ecosistema OpenAI
Proyecto + herramientas
Flujos locales y remotos
CLAUDE CODE
Anthropic
Modelos Claude
Terminal y contexto
Trabajo conversacional
OPENCODE
Código abierto
Múltiples proveedores
Terminal, IDE y escritorio
Alta personalización
La herramienta, el modelo, los permisos y el entorno determinan la experiencia final.

<!-- página 8 -->

El desarrollador conserva la responsabilidad
08
REVISAR
Leer y comprender los cambios antes de aceptarlos.
PROBAR
Ejecutar pruebas funcionales, unitarias y de integración.
PROTEGER
No exponer credenciales, datos personales ni información sensible.
LIMITAR
Configurar permisos y confirmar acciones de riesgo.
DOCUMENTAR
Registrar decisiones, supuestos y código generado.
VALIDAR
Comprobar seguridad, calidad y cumplimiento de requisitos.
Un agente acelera el trabajo; no reemplaza el criterio profesional.

<!-- página 9 -->

Referencias
09
Russell, S. J. y Norvig, P. (2021) Artificial Intelligence: A Modern Approach. 4.ª ed. Pearson.
Yao, S. et al. (2023) ReAct: Synergizing Reasoning and Acting in Language Models. ICLR 2023.
Jimenez, C. E. et al. (2024) SWE-bench: Can Language Models Resolve Real-World GitHub Issues? ICLR 2024.
Yang, J. et al. (2024) SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. NeurIPS 2024.
Wang, L. et al. (2024) A Survey on Large Language Model Based Autonomous Agents. Frontiers of Computer Science.
Huyen, C. (2025) AI Engineering: Building Applications with Foundation Models. O’Reilly Media.
Documentación oficial complementaria: OpenAI Codex · Anthropic Claude Code · OpenCode
