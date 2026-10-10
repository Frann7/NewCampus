# Diagramas de la unidad de patrones estructurales (teoría y práctica).
# Se regeneran con: python fuentes/uml.py fuentes/ing2/diagramas/estr.py

# ---------- Adapter ----------

D["adapter"] = dict(
    alt="Estructura del patrón Adapter (adaptador de objetos)",
    clases=[
        dict(id="Cliente", x=0, y=10),
        dict(id="InterfazCliente", x=190, y=0, estereo="interface", mets=["+ metodo(datos)"]),
        dict(id="Adaptador", x=170, y=150, destacada=True,
             attrs=["- adaptado: Servicio"], mets=["+ metodo(datos)"]),
        dict(id="Servicio", x=470, y=160, mets=["+ metodoServicio(datosEspeciales)"]),
    ],
    rel=[
        ("Cliente", "InterfazCliente", "asociacion"),
        ("Adaptador", "InterfazCliente", "realiza"),
        ("Adaptador", "Servicio", "asociacion"),
    ],
)

D["adapter-termometro"] = dict(
    alt="Adapter en el ejemplo del termómetro",
    clases=[
        dict(id="Termometro", x=110, y=0, estereo="interface", mets=["+ celsius(): double"]),
        dict(id="TermometroDigital", x=0, y=150, mets=["+ celsius()"]),
        dict(id="AdaptadorSensor", x=210, y=150, destacada=True,
             attrs=["- sensor_: SensorAmericano*"], mets=["+ celsius()"]),
        dict(id="SensorAmericano", x=540, y=160, mets=["+ leerFahrenheit(): double"]),
    ],
    rel=[
        ("TermometroDigital", "Termometro", "realiza"),
        ("AdaptadorSensor", "Termometro", "realiza"),
        ("AdaptadorSensor", "SensorAmericano", "asociacion"),
    ],
)

# ---------- Composite ----------

D["composite"] = dict(
    alt="Estructura del patrón Composite",
    clases=[
        dict(id="Cliente", x=0, y=10),
        dict(id="Componente", x=235, y=0, estereo="interface", mets=["+ ejecutar()"]),
        dict(id="Hoja", x=140, y=150, mets=["+ ejecutar()"]),
        dict(id="Compuesto", x=300, y=150, destacada=True,
             attrs=["- hijos: Componente[]"],
             mets=["+ agregar(c: Componente)", "+ eliminar(c: Componente)", "+ ejecutar()"]),
    ],
    rel=[
        ("Cliente", "Componente", "asociacion"),
        ("Hoja", "Componente", "realiza"),
        ("Compuesto", "Componente", "realiza"),
        ("Compuesto", "Componente", "agregacion", dict(sal="der", lle="der", por=570, rot="hijos", m2="*")),
    ],
)

D["composite-cajas"] = dict(
    alt="Composite en el ejemplo de productos y cajas",
    clases=[
        dict(id="Articulo", x=170, y=0, estereo="interface", mets=["+ precio(): double"]),
        dict(id="Producto", x=0, y=150,
             attrs=["- nombre_: string", "- precio_: double"], mets=["+ precio()"]),
        dict(id="Caja", x=230, y=150, destacada=True,
             attrs=["- contenido_: vector<Articulo*>"],
             mets=["+ agregar(articulo: Articulo*)", "+ precio()"]),
    ],
    rel=[
        ("Producto", "Articulo", "realiza"),
        ("Caja", "Articulo", "realiza"),
        ("Caja", "Articulo", "agregacion", dict(sal="der", lle="der", por=540, rot="contenido_", m2="*")),
    ],
)

D["composite-alarma"] = dict(
    alt="Composite para el sistema de alarma del parcial 2024",
    clases=[
        dict(id="SistemaAlarma", x=0, y=20,
             mets=["+ recorrer(): void", "+ dispararAlarma(): void"]),
        dict(id="Elemento", x=330, y=0, abstracta=True,
             attrs=["# conectado: BOOLEAN", "# umbral: REAL"],
             mets=["+ conectar()", "+ desconectar()", "a:+ medida(): REAL", "+ superaUmbral(): BOOLEAN"]),
        dict(id="DetectorHumo", x=60, y=260, mets=["+ medida()"]),
        dict(id="SensorTemperatura", x=200, y=260, mets=["+ medida()"]),
        dict(id="SensorPresion", x=380, y=260, mets=["+ medida()"]),
        dict(id="ArrayElementos", x=530, y=260, destacada=True,
             attrs=["- elementos: Elemento[]"],
             mets=["+ agregar(e: Elemento)", "+ medida()"]),
    ],
    rel=[
        ("SistemaAlarma", "Elemento", "agregacion", dict(m2="*")),
        ("DetectorHumo", "Elemento", "herencia"),
        ("SensorTemperatura", "Elemento", "herencia"),
        ("SensorPresion", "Elemento", "herencia"),
        ("ArrayElementos", "Elemento", "herencia"),
        ("ArrayElementos", "Elemento", "agregacion", dict(sal="der", lle="der", por=780, rot="elementos", m2="*")),
    ],
)

# ---------- Facade ----------

D["facade"] = dict(
    alt="Estructura del patrón Facade",
    clases=[
        dict(id="Cliente", x=0, y=85),
        dict(id="Fachada", x=170, y=45, destacada=True,
             attrs=["- a: ClaseA", "- b: ClaseB", "- c: ClaseC"], mets=["+ operacionSimple()"]),
        dict(id="ClaseA", x=470, y=0, mets=["+ operacionA()"]),
        dict(id="ClaseB", x=470, y=85, mets=["+ operacionB()"]),
        dict(id="ClaseC", x=470, y=170, mets=["+ operacionC()"]),
    ],
    rel=[
        ("Cliente", "Fachada", "asociacion"),
        ("Fachada", "ClaseA", "asociacion", dict(d1=-30, d2=0)),
        ("Fachada", "ClaseB", "asociacion"),
        ("Fachada", "ClaseC", "asociacion", dict(d1=30, d2=0)),
    ],
)

D["facade-tienda"] = dict(
    alt="Facade en el ejemplo de la tienda",
    clases=[
        dict(id="Tienda", x=0, y=45, destacada=True,
             attrs=["- inventario_: Inventario*", "- pagos_: Pagos*", "- envios_: Envios*"],
             mets=["+ comprar(producto: string, monto: double): void"]),
        dict(id="Inventario", x=500, y=0, mets=["+ hayStock(producto: string): bool"]),
        dict(id="Pagos", x=500, y=85, mets=["+ cobrar(monto: double): void"]),
        dict(id="Envios", x=500, y=170, mets=["+ despachar(producto: string): void"]),
    ],
    rel=[
        ("Tienda", "Inventario", "asociacion", dict(d1=-30, d2=0)),
        ("Tienda", "Pagos", "asociacion"),
        ("Tienda", "Envios", "asociacion", dict(d1=30, d2=0)),
    ],
)

D["facade-operador"] = dict(
    alt="Diagrama del código del parcial 2024: Operador, Facturacion y Compras",
    clases=[
        dict(id="Operador", x=0, y=20, destacada=True,
             attrs=["# Facturacion_: Facturacion*", "# Compras_: Compras*"],
             mets=["+ Operador(Facturacion*, Compras*)", "+ Operation(): string"]),
        dict(id="Facturacion", x=400, y=0, mets=["+ Operation1(): string", "+ OperationN(): string"]),
        dict(id="Compras", x=400, y=110, mets=["+ Operation1(): string", "+ OperationZ(): string"]),
    ],
    rel=[
        ("Operador", "Facturacion", "asociacion", dict(d1=-25, d2=0)),
        ("Operador", "Compras", "asociacion", dict(d1=25, d2=0)),
    ],
)

# ---------- Práctica ----------

D["p-conversor"] = dict(
    alt="Diagrama del código de la Guía 2, ejercicio 1",
    clases=[
        dict(id="Target", x=60, y=0, mets=["+ Request(): string"]),
        dict(id="conversor", x=40, y=140, destacada=True,
             attrs=["- convierte_: convierte*"], mets=["+ Request(): string"]),
        dict(id="convierte", x=360, y=150, mets=["+ SpecificRequest(): string"]),
    ],
    rel=[
        ("conversor", "Target", "herencia"),
        ("conversor", "convierte", "asociacion"),
    ],
)

D["p-libro-antes"] = dict(
    alt="Diagrama original: Administrable, Libro y Libro digital",
    clases=[
        dict(id="Administrable", x=0, y=10, estereo="interface",
             mets=["+ agregarstock()", "+ eliminarstock()", "+ vender()"]),
        dict(id="Libro", x=230, y=0, attrs=["+ nombre", "+ isbn"],
             mets=["+ agregarstock()", "+ eliminarstock()", "+ vender()"]),
        dict(id="LibroDigital", x=430, y=10, nombre="Libro digital", mets=["+ vender()"]),
    ],
)

D["p-libro"] = dict(
    alt="Adapter para vincular el libro digital",
    clases=[
        dict(id="Administrable", x=120, y=0, estereo="interface",
             mets=["+ agregarstock()", "+ eliminarstock()", "+ vender()"]),
        dict(id="Libro", x=0, y=190, attrs=["+ nombre", "+ isbn"],
             mets=["+ agregarstock()", "+ eliminarstock()", "+ vender()"]),
        dict(id="AdaptadorLibroDigital", x=200, y=190, destacada=True,
             attrs=["- libroDigital: LibroDigital"],
             mets=["+ agregarstock()", "+ eliminarstock()", "+ vender()"]),
        dict(id="LibroDigital", x=540, y=225, nombre="Libro digital", mets=["+ vender()"]),
    ],
    rel=[
        ("Libro", "Administrable", "realiza"),
        ("AdaptadorLibroDigital", "Administrable", "realiza"),
        ("AdaptadorLibroDigital", "LibroDigital", "asociacion"),
    ],
)

D["p-tpv"] = dict(
    alt="Adapter para los servicios de autorización de pago del TPV",
    clases=[
        dict(id="TPV", x=0, y=10, mets=["+ cobrar(tarjeta, importe)"]),
        dict(id="AutorizadorPago", x=300, y=0, estereo="interface",
             mets=["+ autorizar(tarjeta, importe, idComercio): boolean"]),
        dict(id="AdaptadorVisa", x=180, y=160, destacada=True,
             attrs=["- servicio: ServicioVisa"], mets=["+ autorizar(...)"]),
        dict(id="AdaptadorMasterCard", x=470, y=160, destacada=True,
             attrs=["- servicio: ServicioMasterCard"], mets=["+ autorizar(...)"]),
        dict(id="ServicioVisa", x=190, y=330, mets=["+ (su propia API)"]),
        dict(id="ServicioMasterCard", x=495, y=330, mets=["+ (su propia API)"]),
    ],
    rel=[
        ("TPV", "AutorizadorPago", "asociacion"),
        ("AdaptadorVisa", "AutorizadorPago", "realiza"),
        ("AdaptadorMasterCard", "AutorizadorPago", "realiza"),
        ("AdaptadorVisa", "ServicioVisa", "asociacion"),
        ("AdaptadorMasterCard", "ServicioMasterCard", "asociacion"),
    ],
)

D["p-molecula"] = dict(
    alt="Diagrama del código de la Guía 2, ejercicio 2",
    clases=[
        dict(id="Component", x=120, y=0, abstracta=True,
             attrs=["# parent: Component"],
             mets=["+ setParent(parent: Component)", "+ getParent(): Component",
                   "+ add(component: Component)", "+ remove(component: Component)",
                   "+ ismolecula(): bool", "a:+ operation(): string"]),
        dict(id="atomo", x=40, y=260, mets=["+ operation(): string"]),
        dict(id="molecula", x=250, y=260, destacada=True,
             attrs=["# children"],
             mets=["+ add(component: Component)", "+ remove(component: Component)",
                   "+ ismolecula(): bool", "+ operation(): string"]),
    ],
    rel=[
        ("atomo", "Component", "herencia"),
        ("molecula", "Component", "herencia"),
        ("molecula", "Component", "agregacion", dict(sal="der", lle="der", por=560, rot="children", m2="*")),
    ],
)

D["p-directorio"] = dict(
    alt="Composite para archivos y directorios",
    clases=[
        dict(id="Archivo", x=110, y=0, abstracta=True,
             attrs=["# nombre: String"], mets=["a:+ tamanio(): Long"]),
        dict(id="ArchivoSimple", x=0, y=150,
             attrs=["- tamanio: Long", "- contenido: String"], mets=["+ tamanio(): Long"]),
        dict(id="Directorio", x=230, y=150, destacada=True,
             attrs=["- archivos: Archivo[]"],
             mets=["+ agregar(a: Archivo)", "+ eliminar(a: Archivo)", "+ tamanio(): Long"]),
    ],
    rel=[
        ("ArchivoSimple", "Archivo", "herencia"),
        ("Directorio", "Archivo", "herencia"),
        ("Directorio", "Archivo", "agregacion", dict(sal="der", lle="der", por=470, rot="archivos", m2="*")),
    ],
)

D["p-expresion"] = dict(
    alt="Composite para expresiones matemáticas",
    clases=[
        dict(id="Expresion", x=195, y=0, estereo="interface", mets=["+ evaluar(): double"]),
        dict(id="Numero", x=40, y=150, attrs=["- valor: double"], mets=["+ evaluar()"]),
        dict(id="Operacion", x=270, y=150, abstracta=True, destacada=True,
             attrs=["# izquierda: Expresion", "# derecha: Expresion"]),
        dict(id="Suma", x=110, y=320, mets=["+ evaluar()"]),
        dict(id="Resta", x=245, y=320, mets=["+ evaluar()"]),
        dict(id="Multiplicacion", x=380, y=320, mets=["+ evaluar()"]),
        dict(id="Division", x=540, y=320, mets=["+ evaluar()"]),
    ],
    rel=[
        ("Numero", "Expresion", "realiza"),
        ("Operacion", "Expresion", "realiza"),
        ("Suma", "Operacion", "herencia"),
        ("Resta", "Operacion", "herencia"),
        ("Multiplicacion", "Operacion", "herencia"),
        ("Division", "Operacion", "herencia"),
        ("Operacion", "Expresion", "agregacion", dict(sal="der", lle="der", por=540, m2="2")),
    ],
)

D["p-pantalla"] = dict(
    alt="Diagrama del código de la Guía 2, ejercicio 3",
    clases=[
        dict(id="Client", x=0, y=50),
        dict(id="Pantalla", x=150, y=20, destacada=True,
             attrs=["# _subsystem1: Subsystem1", "# _subsystem2: Subsystem2"],
             mets=["+ Operation(): string"]),
        dict(id="Subsystem1", x=500, y=0, mets=["+ operation1(): string", "+ operationN(): string"]),
        dict(id="Subsystem2", x=500, y=110, mets=["+ operation1(): string", "+ operationZ(): string"]),
    ],
    rel=[
        ("Client", "Pantalla", "dependencia"),
        ("Pantalla", "Subsystem1", "asociacion", dict(d1=-25, d2=0)),
        ("Pantalla", "Subsystem2", "asociacion", dict(d1=25, d2=0)),
    ],
)

D["p-tienda-antes"] = dict(
    alt="Diagrama original: Cliente suelto y Producto con Revista, CD y Libro",
    clases=[
        dict(id="Cliente", x=0, y=60),
        dict(id="Producto", x=305, y=0),
        dict(id="Revista", x=190, y=110),
        dict(id="CD", x=305, y=110),
        dict(id="Libro", x=420, y=110),
    ],
    rel=[("Revista", "Producto", "herencia"), ("CD", "Producto", "herencia"), ("Libro", "Producto", "herencia")],
)

D["p-tienda"] = dict(
    alt="Facade para que el Cliente compre y reclame",
    clases=[
        dict(id="Cliente", x=0, y=30),
        dict(id="FachadaTienda", x=150, y=0, destacada=True,
             mets=["+ comprar(p: Producto): void", "+ reclamar(p: Producto): void"]),
        dict(id="GestorCompras", x=480, y=-55, mets=["+ registrarCompra(p)", "+ cobrar(p)"]),
        dict(id="GestorReclamos", x=480, y=45, mets=["+ registrarReclamo(p)"]),
        dict(id="Producto", x=305, y=170),
        dict(id="Revista", x=190, y=270),
        dict(id="CD", x=305, y=270),
        dict(id="Libro", x=420, y=270),
    ],
    rel=[
        ("Cliente", "FachadaTienda", "asociacion"),
        ("FachadaTienda", "GestorCompras", "asociacion", dict(d1=-15, d2=0)),
        ("FachadaTienda", "GestorReclamos", "asociacion", dict(d1=15, d2=0)),
        ("FachadaTienda", "Producto", "dependencia", dict(sal="abajo", lle="arriba", d1=60)),
        ("Revista", "Producto", "herencia"),
        ("CD", "Producto", "herencia"),
        ("Libro", "Producto", "herencia"),
    ],
)
