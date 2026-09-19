/* ============================================================
   NEWCAMPUS - fechas academicas fijas
   ------------------------------------------------------------
   Feriados, mesas de examen y dias sin actividad. No las carga el
   usuario: vienen con el campus y se ven en el calendario junto a los
   parciales y trabajos practicos que agrega cada uno.

   Para sumar una fecha, copiar una linea de abajo:

     desde / hasta  "AAAA-MM-DD". Si dura un solo dia, van iguales.
     tipo           "feriado" | "mesas" | "sin-clases"
     titulo         como se lee en el detalle del dia
     corto          la etiqueta chiquita que entra en el cuadrito del dia
     detalle        opcional, una linea de aclaracion
   ============================================================ */

window.NC = window.NC || {};

window.NC.calFechas = [
  {
    desde: "2026-09-21", hasta: "2026-09-21",
    tipo: "sin-clases",
    titulo: "Día del estudiante",
    corto: "Día del estudiante",
    detalle: "Sin actividad académica."
  },
  {
    desde: "2026-09-22", hasta: "2026-09-26",
    tipo: "mesas",
    titulo: "Mesas de exámenes — turno Septiembre",
    corto: "Mesas de examen",
    detalle: "Con suspensión de clases."
  },
  {
    desde: "2026-09-29", hasta: "2026-09-29",
    tipo: "feriado",
    titulo: "San Miguel Arcángel, patrono de Entre Ríos",
    corto: "Feriado provincial",
    detalle: "Feriado provincial en Entre Ríos."
  }
];
