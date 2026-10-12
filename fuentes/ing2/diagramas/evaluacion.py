# Diagramas propios del banco de autoevaluación (ejercicios de parcial).
# Se regeneran con: python fuentes/uml.py fuentes/ing2/diagramas/evaluacion.py
# Los ejercicios usan además los generales de cada patrón ("factory", "facade"...),
# que están en crea.py, estr.py y comp.py.

# ---------- Fundamental 04: agregar Singleton y Observer a un diagrama ----------

D["taller"] = dict(
    alt="El diagrama de la aplicación del taller mecánico",
    # angosto a propósito: en el ejercicio va en la columna fija del enunciado
    clases=[
        dict(id="Persona", x=30, y=0,
             attrs=["nombre", "telefono"],
             mets=["get nombre()", "get telefono()", "set telefono()"]),
        dict(id="OrdenDeTrabajo", x=200, y=0,
             attrs=["numero", "patente", "estado", "total"],
             mets=["agregarRepuesto()", "cambiarEstado()", "calcularTotal()"]),
        dict(id="Cliente", x=0, y=225,
             attrs=["DNI", "email"], mets=["get dni()", "get email()"]),
        dict(id="Mecanico", x=125, y=225,
             attrs=["legajo"], mets=["get legajo()"]),
    ],
    rel=[
        ("Cliente", "Persona", "herencia"),
        ("Mecanico", "Persona", "herencia"),
        ("Persona", "OrdenDeTrabajo", "enlace", dict(sal="der", lle="izq")),
    ],
)

D["taller-singleton"] = dict(
    alt="RegistroDeRepuestos como Singleton",
    clases=[dict(id="RegistroDeRepuestos", x=0, y=0, destacada=True,
                 attrs=["s:- instancia: RegistroDeRepuestos"],
                 mets=["- RegistroDeRepuestos()", "s:+ obtenerInstancia(): RegistroDeRepuestos",
                       "+ consultarStock(repuesto): int", "+ reservar(repuesto): void",
                       "+ reponer(repuesto, cantidad): void"])],
)

D["taller-observer"] = dict(
    alt="Observer sobre el diagrama del taller: el Cliente se suscribe a la OrdenDeTrabajo",
    # angosto a propósito: va en la columna de los pasos del ejercicio
    clases=[
        dict(id="Persona", x=40, y=0,
             attrs=["nombre", "telefono"],
             mets=["get nombre()", "get telefono()", "set telefono()"]),
        dict(id="OrdenDeTrabajo", x=220, y=0, destacada=True,
             attrs=["numero", "patente", "estado", "total", "observadores: Observador[]"],
             mets=["agregarRepuesto()", "cambiarEstado()", "calcularTotal()",
                   "suscribir(o: Observador)", "desuscribir(o: Observador)", "notificar()"]),
        dict(id="Mecanico", x=0, y=305,
             attrs=["legajo"], mets=["get legajo()"]),
        dict(id="Cliente", x=122, y=305, destacada=True,
             attrs=["DNI", "email"],
             mets=["get dni()", "get email()", "actualizar(orden)", "registrarAviso(aviso)"]),
        dict(id="Observador", x=255, y=505, estereo="interface", destacada=True, mets=["actualizar(orden)"]),
    ],
    rel=[
        ("Mecanico", "Persona", "herencia"),
        ("Cliente", "Persona", "herencia"),
        ("Persona", "OrdenDeTrabajo", "enlace", dict(sal="der", lle="izq")),
        ("OrdenDeTrabajo", "Observador", "agregacion", dict(m2="*")),
        ("Cliente", "Observador", "realiza", dict(sal="abajo", lle="izq")),
    ],
)
