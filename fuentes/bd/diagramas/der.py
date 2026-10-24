# Diagramas entidad-relación de Bases de Datos (formato arriba de fuentes/der.py).
# python fuentes/der.py fuentes/bd/diagramas/der.py

# ---------- 2do parcial 2025: clínica veterinaria (el DER que da el examen) ----------
D["p25-vet"] = dict(
    titulo="DER de la clínica veterinaria",
    ent=[
        dict(id="Propietario", x=200, y=60, lado="izq",
             attrs=["Nombre", "*Documento", "Teléfonos", "Dirección", "Ciudad", "Provincia", "País"]),
        dict(id="Animal", x=200, y=290, lado="izq",
             attrs=["*NúmeroHC", "Nombre", "Raza", "Sexo", "FechaNac", "Peso"]),
        dict(id="Servicios", x=460, y=60, lado="izq", attrs=["*Código", "Descripción"]),
        dict(id="Turno", x=460, y=290, lado="abajo", attrs=["*Número", "FechaHora", "Estado"]),
        dict(id="Veterinario", x=690, y=60, lado="der", attrs=["*NroMatricula", "Nombre"]),
        dict(id="Consulta", x=460, y=530, lado="izq",
             attrs=["*Número", "Diagnóstico", "Observaciones", "Fecha"]),
        dict(id="Tratamiento", x=760, y=530, lado="der", attrs=["*Código", "Nombre"]),
    ],
    rel=[
        dict(id="es dueño", x=200, y=175, une=[("Propietario", "(1,N)"), ("Animal", "(1,1)")]),
        dict(id="asigna", x=330, y=290, une=[("Animal", "(1,N)"), ("Turno", "(1,1)")]),
        dict(id="incluye", x=460, y=175, une=[("Servicios", "(1,N)"), ("Turno", "(1,N)")]),
        dict(id="atiende", x=690, y=175, une=[("Veterinario", "(1,N)"), ("Turno", "(1,1)")]),
        dict(id="realiza", x=460, y=420, une=[("Turno", "(1,1)", None, (-24, 0)), ("Consulta", "(1,1)")]),
        dict(id="aplica", x=610, y=530, une=[("Consulta", "(1,N)"), ("Tratamiento", "(1,N)")],
             attrs=["Costo"], lado="abajo"),
    ],
)

# ---------- Guía 9: zoológico ----------
D["g9-zoo"] = dict(
    titulo="DER del zoológico (Guía 9)",
    ent=[
        dict(id="Empleado", x=380, y=50, lado="der",
             attrs=["*Legajo", "Nombre", "Dirección", "Teléfono", "FechaIngreso"]),
        dict(id="Guía", x=280, y=150, w=90),
        dict(id="Cuidador", x=500, y=150),
        dict(id="Itinerario", x=150, y=280, lado="izq",
             attrs=["*Código", "Duración", "Longitud", "CantVisitantes"]),
        dict(id="Zona", x=410, y=280, lado="abajo", attrs=["*Código", "Nombre", "Extensión"]),
        dict(id="Especie", x=670, y=280, lado="der",
             attrs=["*Código", "Nombre", "NombreCientífico", "Descripción"]),
    ],
    gen=[dict(padre="Empleado", hijos=["Guía", "Cuidador"], rotulo="(p,s)")],
    rel=[
        dict(id="R1", x=150, y=150, une=[("Guía", "(1,n)"), ("Itinerario", "(1,n)")],
             attrs=["Hora"], lado="arriba"),
        dict(id="R2", x=620, y=180, une=[("Cuidador", "(1,n)"), ("Especie", "(1,n)")],
             attrs=["FechaDesde"], lado="der"),
        dict(id="R4", x=280, y=280, une=[("Itinerario", "(1,n)"), ("Zona", "(1,n)")]),
        dict(id="R3", x=540, y=280, une=[("Zona", "(1,n)"), ("Especie", "(1,1)")]),
    ],
)

# ---------- Guía 10: club náutico ----------
D["g10-nautico"] = dict(
    titulo="DER del club náutico (Guía 10)",
    ent=[
        dict(id="TipoEmbarcación", x=500, y=40, lado="der", attrs=["*Código", "Descripción"]),
        dict(id="Amarre", x=300, y=190, lado="arriba",
             attrs=["*Número", "LecturaAgua", "LecturaLuz", "Mantenimiento"]),
        dict(id="Embarcación", x=630, y=190, lado="der", attrs=["*Matrícula", "Nombre", "Dimensión"]),
        dict(id="Empleado", x=110, y=410, lado="izq", attrs=["*Código", "Nombre", "Teléfono"]),
        dict(id="Zona", x=450, y=410, lado="der", attrs=["*Letra", "Profundidad", "AnchoAmarres"]),
        dict(id="Socio", x=690, y=410, lado="der", attrs=["*DNI", "Nombre", "Dirección", "FechaIngreso"]),
    ],
    rel=[
        dict(id="R1", x=110, y=190, une=[("Amarre", "(1,n)"), ("Empleado", "(1,n)")]),
        dict(id="R6", x=500, y=115, une=[("TipoEmbarcación", "(1,n)"), ("Embarcación", "(1,1)")]),
        dict(id="R3", x=460, y=190, une=[("Amarre", "(1,1)"), ("Embarcación", "(1,1)")],
             attrs=["FechaDesde"], lado="abajo"),
        dict(id="R5", x=300, y=300, une=[("Amarre", "(1,1)"), ("Zona", "(1,n)")]),
        dict(id="R7", x=480, y=300, une=[("Amarre", "(1,1)"), ("Socio", "(1,n)")],
             attrs=["FechaDesde"], lado="der"),
        dict(id="R2", x=690, y=300, une=[("Embarcación", "(1,1)"), ("Socio", "(1,n)")]),
        dict(id="R4", x=280, y=410, une=[("Empleado", "(1,n)"), ("Zona", "(1,n)")]),
    ],
)

# ---------- Unidad 2: las reglas de la cátedra (03-DERaRelacional) ----------
D["u2-multi"] = dict(
    titulo="Persona con un atributo multivaluado",
    ent=[dict(id="Persona", x=0, y=0, lado="der", attrs=["*DNI", "Nombre", "Apellido", "Teléfonos (varios)"])],
)
D["u2-1n"] = dict(
    titulo="Empleado trabaja en Departamento (1:N)",
    ent=[dict(id="Empleado", x=0, y=0, lado="izq", attrs=["*DNI", "Nombre", "Apellido"]),
         dict(id="Departamento", x=330, y=0, lado="der", attrs=["*Codigo", "Nombre"])],
    rel=[dict(id="Trabaja en", x=165, y=0, une=[("Empleado", "(1,1)"), ("Departamento", "(1,n)")])],
)
D["u2-nm"] = dict(
    titulo="Empleado trabaja en Proyecto (N:M) con horas",
    ent=[dict(id="Empleado", x=0, y=0, lado="izq", attrs=["*DNI", "Nombre", "Apellido"]),
         dict(id="Proyecto", x=330, y=0, lado="der", attrs=["*Codigo", "Nombre"])],
    rel=[dict(id="Trabaja en", x=165, y=0, une=[("Empleado", "(1,n)"), ("Proyecto", "(1,n)")],
              attrs=["Horas"], lado="abajo")],
)
D["u2-11"] = dict(
    titulo="Empleado dirige Departamento (1:1)",
    ent=[dict(id="Empleado", x=0, y=0, lado="izq", attrs=["*DNI", "Nombre", "Apellido"]),
         dict(id="Departamento", x=330, y=0, lado="der", attrs=["*Codigo", "Nombre"])],
    rel=[dict(id="Dirige", x=165, y=0, une=[("Empleado", "(0,1)"), ("Departamento", "(1,1)")])],
)
D["u2-debil"] = dict(
    titulo="Ejemplar, entidad débil de Libro",
    ent=[dict(id="Libro", x=0, y=0, lado="izq", attrs=["*ISBN", "Título", "Autor"]),
         dict(id="Ejemplar", x=330, y=0, lado="der", attrs=["*Número"])],
    rel=[dict(id="Pertenece", x=165, y=0, une=[("Libro", "(1,n)"), ("Ejemplar", "(1,1)")])],
)
D["u2-gen"] = dict(
    titulo="Persona generaliza a Empleado y Cliente",
    ent=[dict(id="Persona", x=150, y=0, lado="der", attrs=["*DNI", "Nombre", "Calle"]),
         dict(id="Empleado", x=40, y=110, lado="abajo", attrs=["Sueldo"]),
         dict(id="Cliente", x=260, y=110, lado="abajo", attrs=["LímiteCrédito"])],
    gen=[dict(padre="Persona", hijos=["Empleado", "Cliente"], rotulo="(t,s)")],
)

# ---------- Parcial de práctica 1: gimnasio (inventado) ----------
D["pp1-gimnasio"] = dict(
    titulo="DER del gimnasio",
    ent=[
        dict(id="Membresía", x=200, y=60, lado="izq", attrs=["*Código", "Descripción", "PrecioMensual"]),
        dict(id="Socio", x=200, y=290, lado="izq",
             attrs=["*DNI", "Nombre", "Teléfonos", "Dirección", "Ciudad", "Provincia", "País"]),
        dict(id="Clase", x=460, y=60, lado="arriba", attrs=["*Código", "Nombre", "Día", "Hora"]),
        dict(id="Profesor", x=720, y=60, lado="der", attrs=["*Legajo", "Nombre"]),
        dict(id="Reserva", x=460, y=290, lado="abajo", attrs=["*Número", "FechaHora", "Estado"]),
        dict(id="Pago", x=200, y=520, lado="izq", attrs=["*Número", "Fecha"]),
        dict(id="Concepto", x=520, y=520, lado="der", attrs=["*Código", "Descripción"]),
    ],
    rel=[
        dict(id="contrata", x=200, y=175, une=[("Membresía", "(1,N)"), ("Socio", "(1,1)")]),
        dict(id="dicta", x=590, y=60, une=[("Profesor", "(1,N)"), ("Clase", "(1,1)")]),
        dict(id="hace", x=330, y=290, une=[("Socio", "(1,N)"), ("Reserva", "(1,1)")]),
        dict(id="para", x=460, y=175, une=[("Clase", "(1,N)"), ("Reserva", "(1,1)")]),
        dict(id="realiza", x=200, y=410, une=[("Socio", "(1,N)"), ("Pago", "(1,1)")]),
        dict(id="incluye", x=360, y=520, une=[("Pago", "(1,N)"), ("Concepto", "(1,N)")],
             attrs=["Importe"], lado="abajo"),
    ],
)

# ---------- Parcial de práctica 2: hotel (inventado) ----------
D["pp2-hotel"] = dict(
    titulo="DER del hotel",
    ent=[
        dict(id="Huésped", x=200, y=60, lado="izq",
             attrs=["*Documento", "Nombre", "Emails", "Ciudad", "Provincia", "País"]),
        dict(id="Reserva", x=200, y=290, lado="izq",
             attrs=["*Número", "FechaIngreso", "FechaEgreso", "Estado"]),
        dict(id="Habitación", x=540, y=290, lado="abajo", attrs=["*Número", "Piso"]),
        dict(id="TipoHabitación", x=540, y=60, lado="der", attrs=["*Código", "Descripción", "PrecioNoche"]),
        dict(id="Factura", x=200, y=530, lado="izq", attrs=["*Número", "Tipo", "Fecha"]),
        dict(id="Servicio", x=540, y=530, lado="der", attrs=["*Código", "Descripción"]),
    ],
    rel=[
        dict(id="hace", x=200, y=175, une=[("Huésped", "(1,N)"), ("Reserva", "(1,1)")]),
        dict(id="ocupa", x=370, y=290, une=[("Reserva", "(1,N)"), ("Habitación", "(1,N)")]),
        dict(id="es de", x=540, y=175, une=[("TipoHabitación", "(1,N)"), ("Habitación", "(1,1)")]),
        dict(id="genera", x=200, y=410, une=[("Reserva", "(1,1)"), ("Factura", "(1,1)")]),
        dict(id="detalla", x=370, y=530, une=[("Factura", "(1,N)"), ("Servicio", "(1,N)")],
             attrs=["Importe"], lado="abajo"),
    ],
)

# ---------- Guía 5, ejercicio 1: biblioteca (resuelto en la clase del 02/06) ----------
D["g5-biblioteca"] = dict(
    titulo="DER de la biblioteca (Guía 5)",
    ent=[
        dict(id="Editorial", x=150, y=60, lado="izq", attrs=["*Código", "Nombre", "Dirección", "Teléfono"]),
        dict(id="Género", x=560, y=60, lado="der", attrs=["*Código", "Descripción"]),
        dict(id="Autor", x=110, y=290, lado="izq", attrs=["*Código", "Nombre", "Nacionalidad"]),
        dict(id="Libro", x=360, y=290, lado="der", attrs=["*IdLibro", "Título"]),
        dict(id="Ejemplar", x=360, y=520, lado="izq", attrs=["*Número"]),
        dict(id="Sucursal", x=620, y=520, lado="der", attrs=["*IdSucursal", "Nombre", "Dirección"]),
        dict(id="Préstamo", x=360, y=750, lado="izq", attrs=["*Código", "FechaPréstamo", "FechaDevolución"]),
        dict(id="Socio", x=640, y=750, lado="der", attrs=["*NroTarjeta", "Nombre", "Dirección", "Teléfono"]),
    ],
    rel=[
        dict(id="publica", x=250, y=175, une=[("Editorial", "(1,n)"), ("Libro", "(1,1)")]),
        dict(id="pertenece", x=470, y=175, une=[("Género", "(1,n)"), ("Libro", "(1,1)")]),
        dict(id="escribe", x=235, y=290, une=[("Autor", "(1,n)"), ("Libro", "(1,n)")]),
        dict(id="tiene", x=360, y=405, une=[("Libro", "(1,n)"), ("Ejemplar", "(1,1)")]),
        dict(id="asignado", x=490, y=520, une=[("Sucursal", "(1,n)"), ("Ejemplar", "(1,1)")]),
        dict(id="incluye", x=360, y=635, une=[("Ejemplar", "(0,n)"), ("Préstamo", "(1,n)")]),
        dict(id="pide", x=500, y=750, une=[("Socio", "(0,n)"), ("Préstamo", "(1,1)")]),
    ],
)

# ---------- Los tipos de atributo, como los dibuja la cátedra (02-DER_Extendido) ----------
D["atributos"] = dict(
    titulo="Persona con un atributo multivaluado y uno compuesto",
    ent=[dict(id="Persona", x=0, y=0, lado="der",
              attrs=["*DNI", "Nombre", "+Teléfonos", ("Dirección", ["Calle", "Número", "Dpto."])])],
)
