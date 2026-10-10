# Diagramas de la unidad de patrones creacionales (teoría y práctica).
# Se regeneran con: python fuentes/uml.py fuentes/ing2/diagramas/crea.py

# ---------- Singleton ----------

D["singleton"] = dict(
    alt="Estructura del patrón Singleton",
    clases=[
        dict(id="Cliente", x=0, y=22),
        dict(id="Singleton", x=190, y=0, destacada=True,
             attrs=["s:- instancia: Singleton"],
             mets=["- Singleton()", "s:+ obtenerInstancia(): Singleton"]),
    ],
    rel=[("Cliente", "Singleton", "dependencia", dict(rot="usa"))],
)

D["singleton-config"] = dict(
    alt="La clase Configuracion como Singleton",
    clases=[dict(id="Configuracion", x=0, y=0, destacada=True,
                 attrs=["s:- instancia_: Configuracion*", "- idioma_: string"],
                 mets=["- Configuracion()", "s:+ obtenerInstancia(): Configuracion*",
                       "+ idioma(): string", "+ cambiarIdioma(idioma: string): void"])],
)

D["singleton-gestor"] = dict(
    alt="GestorUsuarios como Singleton",
    clases=[dict(id="GestorUsuarios", x=0, y=0, destacada=True,
                 attrs=["s:- instancia: GestorUsuarios"],
                 mets=["- GestorUsuarios()", "s:+ obtenerInstancia(): GestorUsuarios",
                       "+ login(usuario, clave): boolean", "+ cambiarContrasenia(usuario, nueva): void",
                       "+ darDeAlta(usuario): void", "+ darDeBaja(usuario): void"])],
)

# ---------- Factory Method ----------

D["factory"] = dict(
    alt="Estructura del patrón Factory Method",
    clases=[
        dict(id="Creador", x=49, y=0, abstracta=True, destacada=True,
             mets=["+ algunaOperacion(): void", "a:+ crearProducto(): Producto"]),
        dict(id="CreadorConcretoA", x=0, y=150, mets=["+ crearProducto()"]),
        dict(id="CreadorConcretoB", x=180, y=150, mets=["+ crearProducto()"]),
        dict(id="Producto", x=511, y=0, estereo="interface", mets=["+ hacerAlgo(): void"]),
        dict(id="ProductoConcretoA", x=420, y=150, mets=["+ hacerAlgo()"]),
        dict(id="ProductoConcretoB", x=600, y=150, mets=["+ hacerAlgo()"]),
    ],
    rel=[
        ("CreadorConcretoA", "Creador", "herencia"),
        ("CreadorConcretoB", "Creador", "herencia"),
        ("ProductoConcretoA", "Producto", "realiza"),
        ("ProductoConcretoB", "Producto", "realiza"),
        ("Creador", "Producto", "dependencia", dict(rot="crea")),
    ],
)

D["factory-logistica"] = dict(
    alt="Factory Method en el ejemplo de logística",
    clases=[
        dict(id="Logistica", x=50, y=0, abstracta=True, destacada=True,
             mets=["+ planificarEntrega(): string", "a:+ crearTransporte(): Transporte"]),
        dict(id="LogisticaTerrestre", x=0, y=150, mets=["+ crearTransporte()"]),
        dict(id="LogisticaMaritima", x=200, y=150, mets=["+ crearTransporte()"]),
        dict(id="Transporte", x=477, y=0, estereo="interface", mets=["+ entregar(): string"]),
        dict(id="Camion", x=440, y=150, mets=["+ entregar()"]),
        dict(id="Barco", x=575, y=150, mets=["+ entregar()"]),
    ],
    rel=[
        ("LogisticaTerrestre", "Logistica", "herencia"),
        ("LogisticaMaritima", "Logistica", "herencia"),
        ("Camion", "Transporte", "realiza"),
        ("Barco", "Transporte", "realiza"),
        ("Logistica", "Transporte", "dependencia", dict(rot="crea")),
    ],
)

# ---------- Abstract Factory ----------

D["abstract"] = dict(
    alt="Estructura del patrón Abstract Factory",
    clases=[
        dict(id="Cliente", x=8, y=0, attrs=["- fabrica: FabricaAbstracta"]),
        dict(id="FabricaAbstracta", x=0, y=150, estereo="interface", destacada=True,
             mets=["+ crearProductoA(): ProductoA", "+ crearProductoB(): ProductoB"]),
        dict(id="FabricaConcreta1", x=-50, y=330, mets=["+ crearProductoA()", "+ crearProductoB()"]),
        dict(id="FabricaConcreta2", x=130, y=330, mets=["+ crearProductoA()", "+ crearProductoB()"]),
        dict(id="ProductoA", x=430, y=0, estereo="interface", mets=["+ operacionA(): string"]),
        dict(id="ProductoA1", x=385, y=130, mets=["+ operacionA()"]),
        dict(id="ProductoA2", x=535, y=130, mets=["+ operacionA()"]),
        dict(id="ProductoB", x=430, y=260, estereo="interface", mets=["+ operacionB(): string"]),
        dict(id="ProductoB1", x=385, y=390, mets=["+ operacionB()"]),
        dict(id="ProductoB2", x=535, y=390, mets=["+ operacionB()"]),
    ],
    rel=[
        ("Cliente", "FabricaAbstracta", "asociacion"),
        ("FabricaConcreta1", "FabricaAbstracta", "realiza"),
        ("FabricaConcreta2", "FabricaAbstracta", "realiza"),
        ("ProductoA1", "ProductoA", "realiza"),
        ("ProductoA2", "ProductoA", "realiza"),
        ("ProductoB1", "ProductoB", "realiza"),
        ("ProductoB2", "ProductoB", "realiza"),
        ("FabricaAbstracta", "ProductoA", "dependencia", dict(sal="der", lle="izq", d1=-12, por=340, rot="crea")),
        ("FabricaAbstracta", "ProductoB", "dependencia", dict(sal="der", lle="izq", d1=12, por=340)),
    ],
)

D["abstract-muebles"] = dict(
    alt="Abstract Factory en el ejemplo de la mueblería",
    clases=[
        dict(id="Cliente", x=0, y=0, attrs=["- fabrica: FabricaDeMuebles"]),
        dict(id="FabricaDeMuebles", x=19, y=150, estereo="interface", destacada=True,
             mets=["+ crearSilla(): Silla", "+ crearSofa(): Sofa"]),
        dict(id="FabricaModerna", x=-55, y=330, mets=["+ crearSilla()", "+ crearSofa()"]),
        dict(id="FabricaVictoriana", x=115, y=330, mets=["+ crearSilla()", "+ crearSofa()"]),
        dict(id="Silla", x=442, y=0, estereo="interface", mets=["+ describir(): string"]),
        dict(id="SillaModerna", x=380, y=130, mets=["+ describir()"]),
        dict(id="SillaVictoriana", x=527, y=130, mets=["+ describir()"]),
        dict(id="Sofa", x=442, y=260, estereo="interface", mets=["+ describir(): string"]),
        dict(id="SofaModerno", x=380, y=390, mets=["+ describir()"]),
        dict(id="SofaVictoriano", x=527, y=390, mets=["+ describir()"]),
    ],
    rel=[
        ("Cliente", "FabricaDeMuebles", "asociacion"),
        ("FabricaModerna", "FabricaDeMuebles", "realiza"),
        ("FabricaVictoriana", "FabricaDeMuebles", "realiza"),
        ("SillaModerna", "Silla", "realiza"),
        ("SillaVictoriana", "Silla", "realiza"),
        ("SofaModerno", "Sofa", "realiza"),
        ("SofaVictoriano", "Sofa", "realiza"),
        ("FabricaDeMuebles", "Silla", "dependencia", dict(sal="der", lle="izq", d1=-12, por=330, rot="crea")),
        ("FabricaDeMuebles", "Sofa", "dependencia", dict(sal="der", lle="izq", d1=12, por=330)),
    ],
)

# ---------- Práctica ----------

D["p-inicio-serie"] = dict(
    alt="Diagrama de la clase Inicio_Serie",
    clases=[
        dict(id="Inicio_Serie", x=0, y=0, destacada=True,
             attrs=["s:# Inicio_Serie_: Inicio_Serie*", "# value_: string"],
             mets=["# Inicio_Serie(value: string)", "s:+ GetInstance(value: string): Inicio_Serie*",
                   "+ SomeBusinessLogic(): void", "+ value(): string"]),
    ],
)

D["p-conexion-antes"] = dict(
    alt="Diagrama original: Resultado, ConexionDB y Sentencia",
    clases=[
        dict(id="Resultado", x=0, y=10, attrs=["- cantidadFilas: Long"]),
        dict(id="ConexionDB", x=290, y=0,
             attrs=["- usuario: String", "- password: String", "- host: String"],
             mets=["+ obtenerResultado(Sentencia): Resultado"]),
        dict(id="Sentencia", x=720, y=10, attrs=["- consulta: String"]),
    ],
    rel=[("ConexionDB", "Resultado", "enlace"), ("ConexionDB", "Sentencia", "enlace")],
)

D["p-conexion"] = dict(
    alt="ConexionDB convertida en Singleton",
    clases=[
        dict(id="Resultado", x=0, y=40, attrs=["- cantidadFilas: Long"]),
        dict(id="ConexionDB", x=290, y=0, destacada=True,
             attrs=["s:- instancia: ConexionDB", "- usuario: String", "- password: String", "- host: String"],
             mets=["- ConexionDB()", "s:+ obtenerInstancia(): ConexionDB",
                   "+ obtenerResultado(Sentencia): Resultado"]),
        dict(id="Sentencia", x=720, y=40, attrs=["- consulta: String"]),
    ],
    rel=[("ConexionDB", "Resultado", "enlace"), ("ConexionDB", "Sentencia", "enlace")],
)

D["p-registro"] = dict(
    alt="RegistroEventos como Singleton, usado desde varias partes",
    clases=[
        dict(id="ModuloVentas", x=0, y=0),
        dict(id="ModuloStock", x=0, y=70),
        dict(id="ModuloUsuarios", x=0, y=140),
        dict(id="RegistroEventos", x=290, y=20, destacada=True,
             attrs=["s:- instancia: RegistroEventos", "- eventos: List<String>"],
             mets=["- RegistroEventos()", "s:+ obtenerInstancia(): RegistroEventos",
                   "+ registrar(mensaje: String): void", "+ mostrar(): void"]),
    ],
    rel=[
        ("ModuloVentas", "RegistroEventos", "dependencia", dict(d2=-40)),
        ("ModuloStock", "RegistroEventos", "dependencia", dict(d2=0)),
        ("ModuloUsuarios", "RegistroEventos", "dependencia", dict(d2=40)),
    ],
)

D["p-vehiculos-antes"] = dict(
    alt="Diagrama original: Vehículo con Auto, Camioneta y Motocicleta",
    clases=[
        dict(id="Vehiculo", x=95, y=0, attrs=["- nombre: String", "- fechaCreacion: Date", "- marca: String"]),
        dict(id="Motocicleta", x=0, y=170),
        dict(id="Auto", x=140, y=170),
        dict(id="Camioneta", x=250, y=170),
    ],
    rel=[("Auto", "Vehiculo", "herencia"), ("Camioneta", "Vehiculo", "herencia"),
         ("Motocicleta", "Vehiculo", "herencia")],
)

D["p-vehiculos"] = dict(
    alt="Factory Method para crear vehículos",
    clases=[
        dict(id="FabricaVehiculo", x=165, y=0, abstracta=True, destacada=True,
             mets=["+ registrarVehiculo(): void", "a:+ crearVehiculo(): Vehiculo"]),
        dict(id="FabricaAuto", x=0, y=150, destacada=True, mets=["+ crearVehiculo()"]),
        dict(id="FabricaCamioneta", x=190, y=150, destacada=True, mets=["+ crearVehiculo()"]),
        dict(id="FabricaMotocicleta", x=385, y=150, destacada=True, mets=["+ crearVehiculo()"]),
        dict(id="Vehiculo", x=190, y=300, attrs=["- nombre: String", "- fechaCreacion: Date", "- marca: String"]),
        dict(id="Auto", x=95, y=470),
        dict(id="Camioneta", x=232, y=470),
        dict(id="Motocicleta", x=370, y=470),
    ],
    rel=[
        ("FabricaAuto", "FabricaVehiculo", "herencia"),
        ("FabricaCamioneta", "FabricaVehiculo", "herencia"),
        ("FabricaMotocicleta", "FabricaVehiculo", "herencia"),
        ("Auto", "Vehiculo", "herencia"),
        ("Camioneta", "Vehiculo", "herencia"),
        ("Motocicleta", "Vehiculo", "herencia"),
        ("FabricaVehiculo", "Vehiculo", "dependencia", dict(sal="der", lle="der", por=600, rot="crea")),
    ],
)

D["p-enemigos"] = dict(
    alt="Factory Method para crear enemigos",
    clases=[
        dict(id="CreadorEnemigo", x=120, y=0, abstracta=True, destacada=True,
             mets=["+ aparecer(): void", "a:+ crearEnemigo(): Enemigo"]),
        dict(id="CreadorOrco", x=0, y=150, destacada=True, mets=["+ crearEnemigo()"]),
        dict(id="CreadorTroll", x=165, y=150, destacada=True, mets=["+ crearEnemigo()"]),
        dict(id="CreadorGoblin", x=330, y=150, destacada=True, mets=["+ crearEnemigo()"]),
        dict(id="Enemigo", x=140, y=300, abstracta=True,
             attrs=["# nombre: String", "# puntosDeVida: int", "# danio: int", "# velocidad: int"],
             mets=["a:+ atacar(): void"]),
        dict(id="Orco", x=80, y=510, mets=["+ atacar()"]),
        dict(id="Troll", x=200, y=510, mets=["+ atacar()"]),
        dict(id="Goblin", x=320, y=510, mets=["+ atacar()"]),
    ],
    rel=[
        ("CreadorOrco", "CreadorEnemigo", "herencia"),
        ("CreadorTroll", "CreadorEnemigo", "herencia"),
        ("CreadorGoblin", "CreadorEnemigo", "herencia"),
        ("Orco", "Enemigo", "herencia"),
        ("Troll", "Enemigo", "herencia"),
        ("Goblin", "Enemigo", "herencia"),
        ("CreadorEnemigo", "Enemigo", "dependencia", dict(sal="der", lle="der", por=530, rot="crea")),
    ],
)

D["p-ui"] = dict(
    alt="Abstract Factory para la interfaz de escritorio y web",
    clases=[
        dict(id="Aplicacion", x=22, y=0, attrs=["- fabrica: FabricaUI"]),
        dict(id="FabricaUI", x=0, y=150, estereo="interface", destacada=True,
             mets=["+ crearBoton(): Boton", "+ crearCuadroTexto(): CuadroTexto"]),
        dict(id="FabricaEscritorio", x=-70, y=330, mets=["+ crearBoton()", "+ crearCuadroTexto()"]),
        dict(id="FabricaWeb", x=130, y=330, mets=["+ crearBoton()", "+ crearCuadroTexto()"]),
        dict(id="Boton", x=500, y=0, abstracta=True,
             attrs=["# ancho: int", "# alto: int", "# texto: String", "# colorFondo: String"],
             mets=["a:+ dibujar(): void"]),
        dict(id="BotonEscritorio", x=420, y=200, mets=["+ dibujar()"]),
        dict(id="BotonWeb", x=600, y=200, mets=["+ dibujar()"]),
        dict(id="CuadroTexto", x=500, y=320, abstracta=True,
             attrs=["# ancho: int", "# alto: int", "# texto: String", "# colorFondo: String"],
             mets=["a:+ dibujar(): void"]),
        dict(id="CuadroTextoEscritorio", x=395, y=520, mets=["+ dibujar()"]),
        dict(id="CuadroTextoWeb", x=620, y=520, mets=["+ dibujar()"]),
    ],
    rel=[
        ("Aplicacion", "FabricaUI", "asociacion"),
        ("FabricaEscritorio", "FabricaUI", "realiza"),
        ("FabricaWeb", "FabricaUI", "realiza"),
        ("BotonEscritorio", "Boton", "herencia"),
        ("BotonWeb", "Boton", "herencia"),
        ("CuadroTextoEscritorio", "CuadroTexto", "herencia"),
        ("CuadroTextoWeb", "CuadroTexto", "herencia"),
        ("FabricaUI", "Boton", "dependencia", dict(sal="der", lle="izq", d1=-12, por=360, rot="crea")),
        ("FabricaUI", "CuadroTexto", "dependencia", dict(sal="der", lle="izq", d1=12, por=360)),
    ],
)

D["p-stock"] = dict(
    alt="Abstract Factory para las familias de productos de música y computación",
    clases=[
        dict(id="GestorStock", x=145, y=0, attrs=["- fabrica: FabricaDeProductos"]),
        dict(id="FabricaDeProductos", x=100, y=130, estereo="interface", destacada=True,
             mets=["+ crearProducto(tipo: String): Producto"]),
        dict(id="FabricaMusica", x=70, y=280, mets=["+ crearProducto(tipo)"]),
        dict(id="FabricaComputacion", x=290, y=280, mets=["+ crearProducto(tipo)"]),
        dict(id="Producto", x=185, y=420, abstracta=True,
             attrs=["# nombre: String", "# precio: double", "# stock: int"]),
        dict(id="ProductoMusica", x=45, y=590, abstracta=True),
        dict(id="ProductoComputacion", x=310, y=590, abstracta=True),
        dict(id="CD", x=10, y=690),
        dict(id="DVD", x=120, y=690),
        dict(id="PC", x=250, y=690),
        dict(id="Notebook", x=355, y=690),
        dict(id="Tablet", x=465, y=690),
    ],
    rel=[
        ("GestorStock", "FabricaDeProductos", "asociacion"),
        ("FabricaMusica", "FabricaDeProductos", "realiza"),
        ("FabricaComputacion", "FabricaDeProductos", "realiza"),
        ("ProductoMusica", "Producto", "herencia"),
        ("ProductoComputacion", "Producto", "herencia"),
        ("CD", "ProductoMusica", "herencia"),
        ("DVD", "ProductoMusica", "herencia"),
        ("PC", "ProductoComputacion", "herencia"),
        ("Notebook", "ProductoComputacion", "herencia"),
        ("Tablet", "ProductoComputacion", "herencia"),
        ("FabricaDeProductos", "Producto", "dependencia", dict(sal="der", lle="der", por=580, rot="crea")),
    ],
)
