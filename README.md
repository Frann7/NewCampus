# NewCampus

Campus de apuntes para la carrera **Analista en Sistemas de Información** (UADER, FCyT), por
ahora de tercer año. Corre en local: un ejecutable levanta un servidor en tu máquina y abre los
apuntes en el navegador. Sin nube ni cuentas.

> **Alpha.** Está en desarrollo y cambia seguido.

## Características

- **Apuntes por materia y unidad**, con teoría y práctica resuelta paso a paso.
- **Materias cargadas:** Probabilidad y Estadística, Programación Avanzada, Ingeniería de
  Software II, Paradigmas y Lenguajes, Bases de Datos y SO (Práctica).
- **Evaluación:** parciales y finales transcriptos y resueltos, y autoevaluaciones con informe.
- **Calendario y tareas** para anotar parciales, entregas y pendientes.
- Visor de PDFs de cátedra, cronómetro de estudio, modo claro/oscuro.

## Requisitos

- Windows con .NET Framework 4 (ya viene instalado).
- Conexión a internet (para las fórmulas y las tipografías).
- [Git](https://git-scm.com/download/win), para las actualizaciones automáticas.
- Python 3, solo para editar los apuntes.

## Instalación

```bash
git clone https://github.com/Frann7/NewCampus.git
```

Después, doble clic en `NewCampus.exe`. Abre el campus en `http://localhost:47800` y, cada vez
que arranca, se fija si hay una versión nueva y ofrece actualizar.

## Tus datos

Lo que cargás (calendario, tareas, autoevaluaciones) se guarda fuera del repo, en
`%LOCALAPPDATA%\NewCampus\datos.json`. Actualizar no lo toca.

## Editar los apuntes

El contenido se escribe en `app/contenido/<materia>/<unidad>/` y se arma con:

```bash
cd app
python construir.py
```

Eso genera `app/generado/`, que nunca se edita a mano.

## Material de cátedra

Los PDFs de `app/pdf/` son material de la facultad, subidos solo para estudiar.
