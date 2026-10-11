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

# ---------- Teoría: ejemplos con formato de parcial ----------

D["fm-editor-antes"] = dict(
    alt="Diagrama original: Editor crea directamente cada tipo de documento",
    clases=[
        dict(id="Editor", x=0, y=50, mets=["+ nuevoDocumento(tipo: string)"]),
        dict(id="DocumentoTexto", x=400, y=0, mets=["+ abrir()", "+ guardar()"]),
        dict(id="DocumentoPlanilla", x=400, y=120, mets=["+ abrir()", "+ guardar()"]),
    ],
    rel=[
        ("Editor", "DocumentoTexto", "dependencia", dict(sal="der", lle="izq", d1=-10, rot="crea")),
        ("Editor", "DocumentoPlanilla", "dependencia", dict(sal="der", lle="izq", d1=10)),
    ],
)

D["fm-editor"] = dict(
    alt="Factory Method aplicado al editor",
    clases=[
        dict(id="Editor", x=55, y=0, abstracta=True, destacada=True,
             mets=["+ nuevoDocumento(): void", "a:+ crearDocumento(): Documento"]),
        dict(id="EditorDeTexto", x=0, y=160, mets=["+ crearDocumento()"]),
        dict(id="EditorDePlanillas", x=185, y=160, mets=["+ crearDocumento()"]),
        dict(id="Documento", x=551, y=0, estereo="interface", mets=["+ abrir()", "+ guardar()"]),
        dict(id="DocumentoTexto", x=440, y=160, mets=["+ abrir()", "+ guardar()"]),
        dict(id="DocumentoPlanilla", x=600, y=160, mets=["+ abrir()", "+ guardar()"]),
    ],
    rel=[
        ("EditorDeTexto", "Editor", "herencia"),
        ("EditorDePlanillas", "Editor", "herencia"),
        ("DocumentoTexto", "Documento", "realiza"),
        ("DocumentoPlanilla", "Documento", "realiza"),
        ("Editor", "Documento", "dependencia", dict(rot="crea")),
    ],
)

D["af-comprobantes"] = dict(
    alt="Abstract Factory para los comprobantes de cada país",
    clases=[
        dict(id="Facturador", x=0, y=0, attrs=["- fabrica: FabricaFiscal"]),
        dict(id="FabricaFiscal", x=-4, y=150, estereo="interface", destacada=True,
             mets=["+ crearFactura(): Factura", "+ crearRecibo(): Recibo"]),
        dict(id="FabricaArgentina", x=-65, y=330, mets=["+ crearFactura()", "+ crearRecibo()"]),
        dict(id="FabricaChile", x=115, y=330, mets=["+ crearFactura()", "+ crearRecibo()"]),
        dict(id="Factura", x=465, y=0, estereo="interface", mets=["+ total(): double"]),
        dict(id="FacturaArgentina", x=380, y=130, mets=["+ total()"]),
        dict(id="FacturaChilena", x=560, y=130, mets=["+ total()"]),
        dict(id="Recibo", x=454, y=260, estereo="interface", mets=["+ imprimir(): string"]),
        dict(id="ReciboArgentino", x=385, y=390, mets=["+ imprimir()"]),
        dict(id="ReciboChileno", x=560, y=390, mets=["+ imprimir()"]),
    ],
    rel=[
        ("Facturador", "FabricaFiscal", "asociacion"),
        ("FabricaArgentina", "FabricaFiscal", "realiza"),
        ("FabricaChile", "FabricaFiscal", "realiza"),
        ("FacturaArgentina", "Factura", "realiza"),
        ("FacturaChilena", "Factura", "realiza"),
        ("ReciboArgentino", "Recibo", "realiza"),
        ("ReciboChileno", "Recibo", "realiza"),
        ("FabricaFiscal", "Factura", "dependencia", dict(sal="der", lle="izq", d1=-12, por=330, rot="crea")),
        ("FabricaFiscal", "Recibo", "dependencia", dict(sal="der", lle="izq", d1=12, por=330)),
    ],
)

D["af-cocina-antes"] = dict(
    alt="Diagrama original: Cocina crea directamente las cuatro clases",
    clases=[
        dict(id="Cocina", x=0, y=120, mets=["+ armarPedido(linea: string)"]),
        dict(id="EntradaVegana", x=420, y=0, mets=["+ servir()"]),
        dict(id="PlatoVegano", x=420, y=80, mets=["+ servir()"]),
        dict(id="EntradaClasica", x=420, y=160, mets=["+ servir()"]),
        dict(id="PlatoClasico", x=420, y=240, mets=["+ servir()"]),
    ],
    rel=[
        ("Cocina", "EntradaVegana", "dependencia", dict(sal="der", lle="izq", d1=-18, por=310, rot="crea")),
        ("Cocina", "PlatoVegano", "dependencia", dict(sal="der", lle="izq", d1=-6, por=350)),
        ("Cocina", "EntradaClasica", "dependencia", dict(sal="der", lle="izq", d1=6, por=350)),
        ("Cocina", "PlatoClasico", "dependencia", dict(sal="der", lle="izq", d1=18, por=310)),
    ],
)

D["af-cocina"] = dict(
    alt="Abstract Factory aplicado a la cocina",
    clases=[
        dict(id="Cocina", x=0, y=0, attrs=["- fabrica: FabricaDeMenu"]),
        dict(id="FabricaDeMenu", x=-4, y=150, estereo="interface", destacada=True,
             mets=["+ crearEntrada(): Entrada", "+ crearPlato(): Plato"]),
        dict(id="FabricaVegana", x=-50, y=330, mets=["+ crearEntrada()", "+ crearPlato()"]),
        dict(id="FabricaClasica", x=115, y=330, mets=["+ crearEntrada()", "+ crearPlato()"]),
        dict(id="Entrada", x=484, y=0, estereo="interface", mets=["+ servir()"]),
        dict(id="EntradaVegana", x=385, y=130, mets=["+ servir()"]),
        dict(id="EntradaClasica", x=540, y=130, mets=["+ servir()"]),
        dict(id="Plato", x=480, y=260, estereo="interface", mets=["+ servir()"]),
        dict(id="PlatoVegano", x=395, y=390, mets=["+ servir()"]),
        dict(id="PlatoClasico", x=540, y=390, mets=["+ servir()"]),
    ],
    rel=[
        ("Cocina", "FabricaDeMenu", "asociacion"),
        ("FabricaVegana", "FabricaDeMenu", "realiza"),
        ("FabricaClasica", "FabricaDeMenu", "realiza"),
        ("EntradaVegana", "Entrada", "realiza"),
        ("EntradaClasica", "Entrada", "realiza"),
        ("PlatoVegano", "Plato", "realiza"),
        ("PlatoClasico", "Plato", "realiza"),
        ("FabricaDeMenu", "Entrada", "dependencia", dict(sal="der", lle="izq", d1=-12, por=330, rot="crea")),
        ("FabricaDeMenu", "Plato", "dependencia", dict(sal="der", lle="izq", d1=12, por=330)),
    ],
)

D["singleton-adminbd"] = dict(
    alt="AdministradorBD como Singleton",
    clases=[dict(id="AdministradorBD", x=0, y=0, destacada=True,
                 attrs=["s:- instancia: AdministradorBD", "- host: string", "- usuario: string",
                        "- conexionAbierta: boolean"],
                 mets=["- AdministradorBD()", "s:+ obtenerInstancia(): AdministradorBD", "+ conectar(): void",
                       "+ ejecutar(consulta: string): Resultado", "+ desconectar(): void"])],
)

D["fm-conexiones"] = dict(
    alt="Factory Method para las conexiones a distintas bases de datos",
    clases=[
        dict(id="CreadorDeConexiones", x=135, y=40, abstracta=True, destacada=True,
             mets=["+ abrirConexion(): void", "a:+ crearConexion(): Conexion"]),
        dict(id="CreadorMySQL", x=0, y=230, mets=["+ crearConexion()"]),
        dict(id="CreadorPostgreSQL", x=168, y=230, mets=["+ crearConexion()"]),
        dict(id="CreadorMongoDB", x=353, y=230, mets=["+ crearConexion()"]),
        dict(id="Conexion", x=737, y=0, abstracta=True, estereo="abstract",
             attrs=["# nombreBD: string", "# host: string", "# puerto: int", "# usuario: string",
                    "# contrasenia: string"],
             mets=["a:+ conectar(): void"]),
        dict(id="ConexionMySQL", x=580, y=230, mets=["+ conectar()"]),
        dict(id="ConexionPostgreSQL", x=731, y=230, mets=["+ conectar()"]),
        dict(id="ConexionMongoDB", x=925, y=230, mets=["+ conectar()"]),
    ],
    rel=[
        ("CreadorMySQL", "CreadorDeConexiones", "herencia"),
        ("CreadorPostgreSQL", "CreadorDeConexiones", "herencia"),
        ("CreadorMongoDB", "CreadorDeConexiones", "herencia"),
        ("ConexionMySQL", "Conexion", "herencia"),
        ("ConexionPostgreSQL", "Conexion", "herencia"),
        ("ConexionMongoDB", "Conexion", "herencia"),
        ("CreadorDeConexiones", "Conexion", "dependencia", dict(rot="crea")),
    ],
)

# Guía N°1, ejercicio 1: el diagrama que da la cátedra y sus dos soluciones
D["seguridad-antes"] = dict(
    alt="Diagrama de la Guía 1: Usuario, Sesion, ControladorSeguridad y Logger",
    clases=[
        dict(id="Usuario", x=0, y=0, attrs=["- nombre: String", "- password: String"], mets=["+ login()"]),
        dict(id="Sesion", x=240, y=0, attrs=["- id: Long", "- usuario: Usuario"],
             mets=["+ crearSesion()", "+ cerrarSesion()"]),
        dict(id="ControladorSeguridad", x=480, y=0, attrs=["- sesionesActivas: List<Sesion>"],
             mets=["+ registrarAcceso()"]),
        dict(id="Logger", x=541, y=180, mets=["+ escribirLog()"]),
    ],
    rel=[
        ("Usuario", "Sesion", "enlace"),
        ("Sesion", "ControladorSeguridad", "enlace"),
        ("ControladorSeguridad", "Logger", "enlace"),
    ],
)

D["seguridad-singleton"] = dict(
    alt="ControladorSeguridad convertido en Singleton",
    clases=[
        dict(id="Usuario", x=0, y=0, attrs=["- nombre: String", "- password: String"], mets=["+ login()"]),
        dict(id="Sesion", x=240, y=0, attrs=["- id: Long", "- usuario: Usuario"],
             mets=["+ crearSesion()", "+ cerrarSesion()"]),
        dict(id="ControladorSeguridad", x=480, y=0, destacada=True,
             attrs=["s:- instancia: ControladorSeguridad", "- sesionesActivas: List<Sesion>"],
             mets=["- ControladorSeguridad()", "s:+ obtenerInstancia(): ControladorSeguridad",
                   "+ registrarAcceso()"]),
        dict(id="Logger", x=582, y=230, mets=["+ escribirLog()"]),
    ],
    rel=[
        ("Usuario", "Sesion", "enlace"),
        ("Sesion", "ControladorSeguridad", "enlace"),
        ("ControladorSeguridad", "Logger", "enlace"),
    ],
)

D["seguridad-observer"] = dict(
    alt="Observer sobre el módulo de seguridad: el Logger se suscribe al ControladorSeguridad",
    clases=[
        dict(id="Usuario", x=0, y=0, attrs=["- nombre: String", "- password: String"], mets=["+ login()"]),
        dict(id="Sesion", x=240, y=0, attrs=["- id: Long", "- usuario: Usuario"],
             mets=["+ crearSesion()", "+ cerrarSesion()"]),
        dict(id="ControladorSeguridad", x=480, y=0, destacada=True,
             attrs=["- sesionesActivas: List<Sesion>", "- observadores: Observador[]"],
             mets=["+ registrarAcceso()", "+ suscribir(o: Observador)", "+ desuscribir(o: Observador)",
                   "+ notificar()"]),
        dict(id="Observador", x=522, y=250, estereo="interface", destacada=True, mets=["+ actualizar(acceso)"]),
        dict(id="Logger", x=240, y=250, destacada=True, mets=["+ escribirLog()", "+ actualizar(acceso)"]),
    ],
    rel=[
        ("Usuario", "Sesion", "enlace"),
        ("Sesion", "ControladorSeguridad", "enlace"),
        ("ControladorSeguridad", "Observador", "agregacion", dict(m2="*")),
        ("Logger", "Observador", "realiza"),
    ],
)

# ---------- Teoría, ejemplo 4: el diagrama del patrón de la sección ----------

D["id-singleton"] = dict(
    alt="Singleton para la configuración de la biblioteca",
    clases=[
        dict(id="Prestamos", x=0, y=20),
        dict(id="Socios", x=0, y=96),
        dict(id="Catalogo", x=0, y=172),
        dict(id="Configuracion", x=270, y=0, destacada=True,
             attrs=["s:- instancia: Configuracion", "- diasDePrestamo: int", "- multaDiaria: double",
                    "- horario: string"],
             mets=["- Configuracion()", "s:+ obtenerInstancia(): Configuracion", "+ diasDePrestamo(): int",
                   "+ multaDiaria(): double", "+ horario(): string"]),
    ],
    rel=[
        ("Prestamos", "Configuracion", "dependencia", dict(sal="der", lle="izq", d2=-76, rot="usa")),
        ("Socios", "Configuracion", "dependencia", dict(sal="der", lle="izq", d2=0)),
        ("Catalogo", "Configuracion", "dependencia", dict(sal="der", lle="izq", d2=76)),
    ],
)

D["id-factory"] = dict(
    alt="Factory Method para los documentos de cada trámite",
    clases=[
        dict(id="MesaDeEntradas", x=-10, y=72),
        dict(id="Oficina", x=187, y=40, abstracta=True, destacada=True,
             mets=["+ atenderTramite(): void", "a:+ crearDocumento(): Documento"]),
        dict(id="OficinaDeSolicitudes", x=0, y=240, mets=["+ crearDocumento()"]),
        dict(id="OficinaDeReclamos", x=211, y=240, mets=["+ crearDocumento()"]),
        dict(id="OficinaDeHabilitaciones", x=396, y=240, mets=["+ crearDocumento()"]),
        dict(id="Documento", x=836, y=50, estereo="interface", mets=["+ imprimir()"]),
        dict(id="Solicitud", x=700, y=240, mets=["+ imprimir()"]),
        dict(id="Reclamo", x=830, y=240, mets=["+ imprimir()"]),
        dict(id="Habilitacion", x=960, y=240, mets=["+ imprimir()"]),
    ],
    rel=[
        ("MesaDeEntradas", "Oficina", "asociacion"),
        ("OficinaDeSolicitudes", "Oficina", "herencia"),
        ("OficinaDeReclamos", "Oficina", "herencia"),
        ("OficinaDeHabilitaciones", "Oficina", "herencia"),
        ("Solicitud", "Documento", "realiza"),
        ("Reclamo", "Documento", "realiza"),
        ("Habilitacion", "Documento", "realiza"),
        ("Oficina", "Documento", "dependencia", dict(rot="crea")),
    ],
)

D["id-abstract"] = dict(
    alt="Abstract Factory para las líneas de iluminación",
    clases=[
        dict(id="Instalador", x=-10, y=0, attrs=["- fabrica: FabricaDeLinea"]),
        dict(id="FabricaDeLinea", x=-3, y=150, estereo="interface", destacada=True,
             mets=["+ crearPanel(): Panel", "+ crearSensor(): Sensor"]),
        dict(id="FabricaHogar", x=-60, y=330, mets=["+ crearPanel()", "+ crearSensor()"]),
        dict(id="FabricaProfesional", x=95, y=330, mets=["+ crearPanel()", "+ crearSensor()"]),
        dict(id="Panel", x=493, y=0, estereo="interface", mets=["+ mostrar()"]),
        dict(id="PanelHogar", x=400, y=130, mets=["+ mostrar()"]),
        dict(id="PanelProfesional", x=525, y=130, mets=["+ mostrar()"]),
        dict(id="Sensor", x=490, y=260, estereo="interface", mets=["+ detectar()"]),
        dict(id="SensorHogar", x=395, y=390, mets=["+ detectar()"]),
        dict(id="SensorProfesional", x=529, y=390, mets=["+ detectar()"]),
    ],
    rel=[
        ("Instalador", "FabricaDeLinea", "asociacion"),
        ("FabricaHogar", "FabricaDeLinea", "realiza"),
        ("FabricaProfesional", "FabricaDeLinea", "realiza"),
        ("PanelHogar", "Panel", "realiza"),
        ("PanelProfesional", "Panel", "realiza"),
        ("SensorHogar", "Sensor", "realiza"),
        ("SensorProfesional", "Sensor", "realiza"),
        ("FabricaDeLinea", "Panel", "dependencia", dict(sal="der", lle="izq", d1=-12, por=340, rot="crea")),
        ("FabricaDeLinea", "Sensor", "dependencia", dict(sal="der", lle="izq", d1=12, por=340)),
    ],
)
