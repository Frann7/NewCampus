# Diagramas de la unidad Base de Ing. de Software II.
# Se regeneran con: python fuentes/uml.py fuentes/ing2/diagramas/base.py

D["cuenta"] = dict(
    alt="La clase Cuenta dibujada en tres pisos",
    clases=[dict(id="Cuenta", x=0, y=0,
                 attrs=["- titular: string", "- saldo: double"],
                 mets=["+ depositar(monto: double): void", "+ saldo(): double"])],
)

D["marcas"] = dict(
    alt="Una clase con miembros estáticos, una clase abstracta y una interfaz",
    clases=[
        dict(id="Alumno", x=0, y=0,
             attrs=["- nombre: string", "s:- cantidad: int"],
             mets=["+ Alumno(nombre: string)", "s:+ cantidad(): int"]),
        dict(id="Animal", x=250, y=0, estereo="abstract", abstracta=True,
             attrs=["# nombre: string"], mets=["a:+ hablar(): string"]),
        dict(id="Imprimible", x=460, y=0, estereo="interface",
             mets=["+ imprimir(): void"]),
    ],
)

D["medicamento"] = dict(
    alt="La clase Medicamento del parcial 2024",
    clases=[dict(id="Medicamento", x=0, y=0,
                 attrs=["Serial", "Nombre", "Lote", "Posologia", "Presentacion"],
                 mets=["validarmedicacion()", "imprimirlote()", "imprimiretiqueta()"])],
)

D["herencia"] = dict(
    alt="Perro y Gato heredan de Animal",
    clases=[
        dict(id="Animal", x=95, y=0, attrs=["# nombre: string"], mets=["+ hablar(): string"]),
        dict(id="Perro", x=0, y=140, mets=["+ hablar(): string"]),
        dict(id="Gato", x=200, y=140, mets=["+ hablar(): string"]),
    ],
    rel=[("Perro", "Animal", "herencia"), ("Gato", "Animal", "herencia")],
)

D["realiza"] = dict(
    alt="Avion y Pajaro realizan la interfaz Volador",
    clases=[
        dict(id="Volador", x=85, y=0, estereo="interface", mets=["+ volar(): void"]),
        dict(id="Avion", x=0, y=130, mets=["+ volar(): void"]),
        dict(id="Pajaro", x=180, y=130, mets=["+ volar(): void"]),
    ],
    rel=[("Avion", "Volador", "realiza"), ("Pajaro", "Volador", "realiza")],
)

D["asociacion"] = dict(
    alt="Duenio conoce a un Animal",
    clases=[
        dict(id="Duenio", x=0, y=0, attrs=["- mascota: Animal"], mets=["+ saludar(): void"]),
        dict(id="Animal", x=320, y=0, mets=["+ hablar(): string"]),
    ],
    rel=[("Duenio", "Animal", "asociacion", dict(rot="mascota", m2="1"))],
)

D["agregacion"] = dict(
    alt="Un Equipo tiene muchos Jugadores",
    clases=[
        dict(id="Equipo", x=0, y=0, attrs=["- nombre: string"], mets=["+ agregar(j: Jugador): void"]),
        dict(id="Jugador", x=360, y=14, attrs=["- nombre: string"]),
    ],
    rel=[("Equipo", "Jugador", "agregacion", dict(m2="*"))],
)

D["composicion"] = dict(
    alt="Una Casa está hecha de Habitaciones",
    clases=[
        dict(id="Casa", x=0, y=0, attrs=["- direccion: string"]),
        dict(id="Habitacion", x=300, y=0, attrs=["- metros: double"]),
    ],
    rel=[("Casa", "Habitacion", "composicion", dict(m2="1..*"))],
)

D["dependencia"] = dict(
    alt="Impresora usa un Documento",
    clases=[
        dict(id="Impresora", x=0, y=0, mets=["+ imprimir(d: Documento): void"]),
        dict(id="Documento", x=380, y=0, mets=["+ texto(): string"]),
    ],
    rel=[("Impresora", "Documento", "dependencia", dict(rot="usa"))],
)

D["farmacia"] = dict(
    alt="El diagrama de la aplicación farmacéutica del parcial 2024",
    clases=[
        dict(id="Usuario", x=110, y=0,
             attrs=["nombre", "Telefono", "Direccion"],
             mets=["get nombre()", "get telefono()", "set telefono()"]),
        dict(id="Medicamento", x=420, y=0,
             attrs=["Serial", "Nombre", "Lote", "Posologia", "Presentacion"],
             mets=["validarmedicacion()", "imprimirlote()", "imprimiretiqueta()"]),
        dict(id="Cliente", x=0, y=270,
             attrs=["CUIT", "Razon Social"], mets=["set razonsocial()", "get cuit()"]),
        dict(id="Farmaceutico", x=210, y=270,
             attrs=["Matricula"], mets=["get matricula()"]),
    ],
    rel=[
        ("Cliente", "Usuario", "herencia"),
        ("Farmaceutico", "Usuario", "herencia"),
        ("Usuario", "Medicamento", "enlace", dict(sal="der", lle="izq")),
    ],
)

D["duenio"] = dict(
    alt="Duenio guarda un puntero a Animal; Perro y Gato heredan de Animal",
    clases=[
        dict(id="Duenio", x=0, y=0,
             attrs=["- mascota_: Animal*"],
             mets=["+ Duenio(mascota: Animal*)", "+ cambiarMascota(mascota: Animal*): void", "+ saludar(): void"]),
        dict(id="Animal", x=470, y=25, estereo="abstract", abstracta=True,
             mets=["a:+ hablar(): string"]),
        dict(id="Perro", x=380, y=170, mets=["+ hablar(): string"]),
        dict(id="Gato", x=580, y=170, mets=["+ hablar(): string"]),
    ],
    rel=[
        ("Duenio", "Animal", "asociacion", dict(rot="mascota_", sal="der", lle="izq")),
        ("Perro", "Animal", "herencia"),
        ("Gato", "Animal", "herencia"),
    ],
)
