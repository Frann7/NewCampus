# Diagramas de la unidad de patrones de comportamiento (teoría y práctica).
# Se regeneran con: python fuentes/uml.py fuentes/ing2/diagramas/comp.py

# ---------- Observer ----------

D["observer"] = dict(
    alt="Estructura del patrón Observer",
    clases=[
        dict(id="Notificador", x=0, y=0, destacada=True,
             attrs=["- suscriptores: Suscriptor[]"],
             mets=["+ suscribir(s: Suscriptor)", "+ desuscribir(s: Suscriptor)", "+ notificar()"]),
        dict(id="Suscriptor", x=420, y=20, estereo="interface", mets=["+ actualizar(contexto)"]),
        dict(id="SuscriptorConcretoA", x=330, y=180, mets=["+ actualizar(contexto)"]),
        dict(id="SuscriptorConcretoB", x=540, y=180, mets=["+ actualizar(contexto)"]),
    ],
    rel=[
        ("Notificador", "Suscriptor", "agregacion", dict(m2="*")),
        ("SuscriptorConcretoA", "Suscriptor", "realiza"),
        ("SuscriptorConcretoB", "Suscriptor", "realiza"),
    ],
)

D["observer-tienda"] = dict(
    alt="Observer en el ejemplo de la tienda",
    clases=[
        dict(id="Tienda", x=0, y=0, destacada=True,
             attrs=["- suscriptores_: list<Suscriptor*>"],
             mets=["+ suscribir(s: Suscriptor*)", "+ desuscribir(s: Suscriptor*)",
                   "+ notificar(novedad: string)", "+ recibirProducto(producto: string)"]),
        dict(id="Suscriptor", x=440, y=30, estereo="interface", mets=["+ actualizar(novedad: string)"]),
        dict(id="Cliente", x=455, y=200, attrs=["- nombre_: string"], mets=["+ actualizar(novedad: string)"]),
    ],
    rel=[
        ("Tienda", "Suscriptor", "agregacion", dict(m2="*")),
        ("Cliente", "Suscriptor", "realiza"),
    ],
)

D["observer-farmacia"] = dict(
    alt="Observer sobre el diagrama de la aplicación farmacéutica",
    clases=[
        dict(id="Usuario", x=110, y=0,
             attrs=["nombre", "Telefono", "Direccion"],
             mets=["get nombre()", "get telefono()", "set telefono()"]),
        dict(id="Medicamento", x=420, y=0, destacada=True,
             attrs=["Serial", "Nombre", "Lote", "Posologia", "Presentacion", "observadores: Observador[]"],
             mets=["validarmedicacion()", "imprimirlote()", "imprimiretiqueta()",
                   "suscribir(o: Observador)", "desuscribir(o: Observador)", "notificar()"]),
        dict(id="Cliente", x=0, y=270,
             attrs=["CUIT", "Razon Social"], mets=["set razonsocial()", "get cuit()"]),
        dict(id="Farmaceutico", x=175, y=270, destacada=True,
             attrs=["Matricula"], mets=["get matricula()", "actualizar(lote)", "registrarEnTablaDeLotes(lote)"]),
        dict(id="Observador", x=470, y=360, estereo="interface", destacada=True, mets=["actualizar(lote)"]),
    ],
    rel=[
        ("Cliente", "Usuario", "herencia"),
        ("Farmaceutico", "Usuario", "herencia", dict(d1=-60)),
        ("Usuario", "Medicamento", "enlace", dict(sal="der", lle="izq", d1=-50, d2=-104)),
        ("Medicamento", "Observador", "agregacion", dict(m2="*")),
        ("Farmaceutico", "Observador", "realiza", dict(sal="der", lle="izq", d1=40)),
    ],
)

# ---------- Strategy ----------

D["strategy"] = dict(
    alt="Estructura del patrón Strategy",
    clases=[
        dict(id="Contexto", x=0, y=0, destacada=True,
             attrs=["- estrategia: Estrategia"],
             mets=["+ cambiarEstrategia(e: Estrategia)", "+ hacerAlgo()"]),
        dict(id="Estrategia", x=420, y=12, estereo="interface", mets=["+ ejecutar(datos)"]),
        dict(id="EstrategiaConcretaA", x=330, y=170, mets=["+ ejecutar(datos)"]),
        dict(id="EstrategiaConcretaB", x=540, y=170, mets=["+ ejecutar(datos)"]),
    ],
    rel=[
        ("Contexto", "Estrategia", "agregacion"),
        ("EstrategiaConcretaA", "Estrategia", "realiza"),
        ("EstrategiaConcretaB", "Estrategia", "realiza"),
    ],
)

D["strategy-navegador"] = dict(
    alt="Strategy en el ejemplo del navegador",
    clases=[
        dict(id="Navegador", x=0, y=0, destacada=True,
             attrs=["- estrategia_: EstrategiaRuta*"],
             mets=["+ cambiarEstrategia(e: EstrategiaRuta*)", "+ mostrarRuta(origen, destino)"]),
        dict(id="EstrategiaRuta", x=450, y=10, estereo="interface",
             mets=["+ calcularRuta(origen, destino): string"]),
        dict(id="RutaEnAuto", x=430, y=170, mets=["+ calcularRuta(...)"]),
        dict(id="RutaAPie", x=640, y=170, mets=["+ calcularRuta(...)"]),
    ],
    rel=[
        ("Navegador", "EstrategiaRuta", "agregacion"),
        ("RutaEnAuto", "EstrategiaRuta", "realiza"),
        ("RutaAPie", "EstrategiaRuta", "realiza"),
    ],
)

# ---------- Práctica ----------

D["p-dispositivo"] = dict(
    alt="Diagrama del código de la Guía 3, ejercicio 3",
    clases=[
        dict(id="Context", x=0, y=0, destacada=True,
             attrs=["- dispositivo: dispositivo"],
             mets=["+ setdispositivo(d: dispositivo)", "+ doSomeBusinessLogic(): void"]),
        dict(id="dispositivo", x=400, y=12, estereo="interface",
             mets=["+ doAlgorithm(data: array): array"]),
        dict(id="ConcretedispositivoA", x=330, y=170, mets=["+ doAlgorithm(data)"]),
        dict(id="ConcretedispositivoB", x=550, y=170, mets=["+ doAlgorithm(data)"]),
    ],
    rel=[
        ("Context", "dispositivo", "agregacion"),
        ("ConcretedispositivoA", "dispositivo", "realiza"),
        ("ConcretedispositivoB", "dispositivo", "realiza"),
    ],
)

D["p-alarma"] = dict(
    alt="Diagrama del código de la Guía 3, ejercicio 4",
    clases=[
        dict(id="ISubject", x=30, y=0, estereo="interface",
             mets=["+ Attach(alarma: Ialarma*)", "+ Detach(alarma: Ialarma*)", "+ Notify()"]),
        dict(id="Subject", x=0, y=190, destacada=True,
             attrs=["- list_alarma_: list<Ialarma*>", "- message_: string"],
             mets=["+ Attach(alarma: Ialarma*)", "+ Detach(alarma: Ialarma*)", "+ Notify()",
                   "+ CreateMessage(message: string)", "+ HowManyalarma()", "+ SomeBusinessLogic()"]),
        dict(id="Ialarma", x=470, y=20, estereo="interface", mets=["+ Update(message: string)"]),
        dict(id="alarma", x=450, y=220,
             attrs=["- subject_: Subject&", "- message_from_subject_: string", "- number_: int",
                    "s:- static_number_: int"],
             mets=["+ Update(message: string)", "+ RemoveMeFromTheList()", "+ PrintInfo()"]),
    ],
    rel=[
        ("Subject", "ISubject", "realiza"),
        ("alarma", "Ialarma", "realiza"),
        ("Subject", "Ialarma", "agregacion", dict(sal="der", lle="izq", d1=-90, d2=10, por=380, m2="*")),
        ("alarma", "Subject", "asociacion", dict(d1=40, d2=40)),
    ],
)

D["p-exportadores-antes"] = dict(
    alt="Diagrama original: Archivo suelto y Exportador con tres hijas",
    clases=[
        dict(id="Archivo", x=0, y=30),
        dict(id="Exportador", x=430, y=0, abstracta=True, mets=["+ exportar()"]),
        dict(id="ExportadorCSV", x=270, y=130),
        dict(id="ExportadorXLS", x=425, y=130),
        dict(id="ExportadorPDF", x=580, y=130),
    ],
    rel=[("ExportadorCSV", "Exportador", "herencia"), ("ExportadorXLS", "Exportador", "herencia"),
         ("ExportadorPDF", "Exportador", "herencia")],
)

D["p-exportadores"] = dict(
    alt="Observer para que el Archivo avise a los exportadores",
    clases=[
        dict(id="Archivo", x=0, y=0, destacada=True,
             attrs=["- nombre", "- tamanio", "- contenido", "- exportadores: Exportador[]"],
             mets=["+ modificarContenido(nuevo)", "+ suscribir(e: Exportador)",
                   "+ desuscribir(e: Exportador)", "+ notificar()"]),
        dict(id="Exportador", x=500, y=50, abstracta=True, mets=["+ exportar()"]),
        dict(id="ExportadorCSV", x=340, y=230),
        dict(id="ExportadorXLS", x=495, y=230),
        dict(id="ExportadorPDF", x=650, y=230),
    ],
    rel=[
        ("Archivo", "Exportador", "agregacion", dict(m2="*")),
        ("ExportadorCSV", "Exportador", "herencia"),
        ("ExportadorXLS", "Exportador", "herencia"),
        ("ExportadorPDF", "Exportador", "herencia"),
    ],
)

D["p-coche"] = dict(
    alt="Diagrama de la guía: Coche y IComportamientoFrenos",
    clases=[
        dict(id="Coche", x=60, y=0, attrs=["- largo", "- ancho", "- color"], mets=["+ Frenado()"]),
        dict(id="IComportamientoFrenos", x=380, y=15, estereo="Interface", mets=["+ Frenar()"]),
        dict(id="CocheAntiguo", x=0, y=200),
        dict(id="CocheNuevo", x=150, y=200),
        dict(id="FrenadoNormal", x=350, y=200),
        dict(id="FrenadoABS", x=510, y=200),
    ],
    rel=[
        ("Coche", "IComportamientoFrenos", "agregacion"),
        ("CocheAntiguo", "Coche", "herencia"),
        ("CocheNuevo", "Coche", "herencia"),
        ("FrenadoNormal", "IComportamientoFrenos", "realiza"),
        ("FrenadoABS", "IComportamientoFrenos", "realiza"),
    ],
)

D["p-organismos"] = dict(
    alt="Composite para la jerarquía de organismos",
    clases=[
        dict(id="Organismo", x=150, y=0, abstracta=True,
             attrs=["# nombre: String", "# esMesaEntrada: Boolean", "# direccion: String", "# padre: Organismo"],
             mets=["a:+ puedeRecibirExpedientes(): Boolean"]),
        dict(id="OrganismoSimple", x=0, y=220, mets=["+ puedeRecibirExpedientes()"]),
        dict(id="OrganismoCompuesto", x=280, y=220, destacada=True,
             attrs=["- hijos: Organismo[]"],
             mets=["+ agregarHijo(o: Organismo)", "+ eliminarHijo(o: Organismo)", "+ puedeRecibirExpedientes()"]),
    ],
    rel=[
        ("OrganismoSimple", "Organismo", "herencia"),
        ("OrganismoCompuesto", "Organismo", "herencia"),
        ("OrganismoCompuesto", "Organismo", "agregacion", dict(sal="der", lle="der", por=590, rot="hijos", m2="*")),
    ],
)

D["p-auditoria"] = dict(
    alt="Observer para la auditoría de movimientos",
    clases=[
        dict(id="Movimiento", x=0, y=0, destacada=True,
             attrs=["- expediente: Expediente", "- organismoOrigen: Organismo",
                    "- organismoDestino: Organismo", "- usuario: Usuario",
                    "- observadores: ObservadorMovimiento[]"],
             mets=["+ realizarMovimiento()", "+ consultarMovimiento()",
                   "+ suscribir(o: ObservadorMovimiento)", "+ desuscribir(o: ObservadorMovimiento)",
                   "+ notificar()"]),
        dict(id="ObservadorMovimiento", x=470, y=70, estereo="interface",
             mets=["+ actualizar(m: Movimiento)"]),
        dict(id="AlertaAdministrador", x=400, y=280, mets=["+ actualizar(m: Movimiento)"]),
        dict(id="RegistroAuditoria", x=640, y=280, mets=["+ actualizar(m: Movimiento)"]),
    ],
    rel=[
        ("Movimiento", "ObservadorMovimiento", "agregacion", dict(m2="*")),
        ("AlertaAdministrador", "ObservadorMovimiento", "realiza"),
        ("RegistroAuditoria", "ObservadorMovimiento", "realiza"),
    ],
)

D["p-archivos-fabrica"] = dict(
    alt="Factory Method para los tipos de archivo adjunto",
    clases=[
        dict(id="CreadorArchivo", x=190, y=0, abstracta=True, destacada=True,
             mets=["a:+ crearArchivo(): Archivo"]),
        dict(id="CreadorPDF", x=0, y=120, destacada=True, mets=["+ crearArchivo()"]),
        dict(id="CreadorPNG", x=165, y=120, destacada=True, mets=["+ crearArchivo()"]),
        dict(id="CreadorJPG", x=330, y=120, destacada=True, mets=["+ crearArchivo()"]),
        dict(id="CreadorTXT", x=495, y=120, destacada=True, mets=["+ crearArchivo()"]),
        dict(id="Archivo", x=175, y=260, abstracta=True,
             attrs=["# nombre: String", "# contenido: String"],
             mets=["a:+ obtenerTamanioMaximo(): long", "a:+ visualizar()"]),
        dict(id="ArchivoPDF", x=30, y=450),
        dict(id="ArchivoPNG", x=180, y=450),
        dict(id="ArchivoJPG", x=330, y=450, destacada=True),
        dict(id="ArchivoTXT", x=480, y=450, destacada=True),
    ],
    rel=[
        ("CreadorPDF", "CreadorArchivo", "herencia"),
        ("CreadorPNG", "CreadorArchivo", "herencia"),
        ("CreadorJPG", "CreadorArchivo", "herencia"),
        ("CreadorTXT", "CreadorArchivo", "herencia"),
        ("ArchivoPDF", "Archivo", "herencia"),
        ("ArchivoPNG", "Archivo", "herencia"),
        ("ArchivoJPG", "Archivo", "herencia"),
        ("ArchivoTXT", "Archivo", "herencia"),
        ("CreadorArchivo", "Archivo", "dependencia", dict(sal="der", lle="der", por=690, rot="crea")),
    ],
)

D["p-carpetas"] = dict(
    alt="Composite para organizar los archivos en carpetas",
    clases=[
        dict(id="Archivo", x=160, y=0, abstracta=True,
             attrs=["# nombre: String", "# contenido: String"],
             mets=["a:+ obtenerTamanioMaximo(): long", "a:+ visualizar()"]),
        dict(id="ArchivoPDF", x=0, y=190),
        dict(id="ArchivoPNG", x=140, y=190),
        dict(id="Carpeta", x=290, y=190, destacada=True,
             attrs=["- archivos: Archivo[]"],
             mets=["+ agregar(a: Archivo)", "+ eliminar(a: Archivo)", "+ visualizar()"]),
    ],
    rel=[
        ("ArchivoPDF", "Archivo", "herencia"),
        ("ArchivoPNG", "Archivo", "herencia"),
        ("Carpeta", "Archivo", "herencia"),
        ("Carpeta", "Archivo", "agregacion", dict(sal="der", lle="der", por=540, rot="archivos", m2="*")),
    ],
)

D["p-gestor-contenido"] = dict(
    alt="GestorContenido como Singleton",
    clases=[dict(id="GestorContenido", x=0, y=0, destacada=True,
                 attrs=["s:- instancia: GestorContenido"],
                 mets=["- GestorContenido()", "s:+ obtenerInstancia(): GestorContenido",
                       "+ publicar(p: Publicacion)", "+ editar(p: Publicacion)", "+ borrar(p: Publicacion)"])],
)

D["p-multimedia-arbol"] = dict(
    alt="Composite para archivos y colecciones multimedia",
    clases=[
        dict(id="ElementoMultimedia", x=250, y=0, estereo="interface",
             mets=["+ reproducir()", "+ pausar()", "+ renombrar(nombre)", "+ eliminar()"]),
        dict(id="Imagen", x=0, y=190),
        dict(id="Video", x=105, y=190),
        dict(id="Documento", x=210, y=190),
        dict(id="Audio", x=330, y=190),
        dict(id="Coleccion", x=440, y=190, destacada=True,
             attrs=["- elementos: ElementoMultimedia[]"],
             mets=["+ agregar(e: ElementoMultimedia)", "+ quitar(e: ElementoMultimedia)", "+ reproducir()"]),
    ],
    rel=[
        ("Imagen", "ElementoMultimedia", "realiza"),
        ("Video", "ElementoMultimedia", "realiza"),
        ("Documento", "ElementoMultimedia", "realiza"),
        ("Audio", "ElementoMultimedia", "realiza"),
        ("Coleccion", "ElementoMultimedia", "realiza"),
        ("Coleccion", "ElementoMultimedia", "agregacion", dict(sal="der", lle="der", por=760, rot="elementos", m2="*")),
    ],
)

D["p-multimedia-fachada"] = dict(
    alt="Facade y Adapter para las bibliotecas externas",
    clases=[
        dict(id="Usuario", x=0, y=30),
        dict(id="PlataformaMultimedia", x=140, y=0, destacada=True,
             mets=["+ reproducir(e)", "+ pausar(e)", "+ renombrar(e, nombre)", "+ eliminar(e)", "+ convertir(e, formato)"]),
        dict(id="Conversor", x=470, y=20, estereo="interface", mets=["+ convertir(e, formato)"]),
        dict(id="AdaptadorImagen", x=260, y=220, destacada=True, mets=["+ convertir(e, formato)"]),
        dict(id="AdaptadorVideo", x=500, y=220, destacada=True, mets=["+ convertir(e, formato)"]),
        dict(id="AdaptadorAudio", x=740, y=220, destacada=True, mets=["+ convertir(e, formato)"]),
        dict(id="BibliotecaImagenes", x=255, y=350),
        dict(id="BibliotecaVideo", x=510, y=350),
        dict(id="BibliotecaAudio", x=750, y=350),
    ],
    rel=[
        ("Usuario", "PlataformaMultimedia", "asociacion"),
        ("PlataformaMultimedia", "Conversor", "asociacion"),
        ("AdaptadorImagen", "Conversor", "realiza"),
        ("AdaptadorVideo", "Conversor", "realiza"),
        ("AdaptadorAudio", "Conversor", "realiza"),
        ("AdaptadorImagen", "BibliotecaImagenes", "asociacion"),
        ("AdaptadorVideo", "BibliotecaVideo", "asociacion"),
        ("AdaptadorAudio", "BibliotecaAudio", "asociacion"),
    ],
)
