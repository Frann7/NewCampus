// NewCampus.exe - abre los apuntes en un servidor local.
//
//   Doble clic -> levanta un servidor en http://localhost:47800 (solo accesible
//   desde esta misma PC), abre el navegador y deja un icono junto al reloj.
//   Cuando se cierra la pestania el servidor se apaga solo: la pagina manda un
//   latido cada 10 segundos y, cuando dejan de llegar, NewCampus.exe termina.
//   Tambien se puede cerrar a mano: clic derecho en el icono -> Cerrar NewCampus.
//
// Que atiende el servidor:
//   GET  /...              los archivos de la carpeta app (y nada fuera de ella)
//   GET  /api/estado       quien es y que numero de corrida (para el contador de tiempo)
//   POST /api/ping         latido de la pagina abierta
//   POST /api/adios        la pestania se esta cerrando (apaga mas rapido)
//   GET  /api/datos        lo que guardo el usuario (calendario, autoevaluaciones...)
//   POST /api/datos        guardarlo
//
// Datos del usuario:
//   Se guardan en %LOCALAPPDATA%\NewCampus\datos.json, FUERA del repositorio:
//   un git pull o una actualizacion nunca los tocan, y no dependen del
//   navegador ni del puerto. Antes de reemplazarlo se deja la version anterior
//   en datos.anterior.json. La pagina los copia al navegador al abrir y los
//   manda de vuelta cada vez que cambian (assets/datos.js).
//
// Actualizaciones:
//   Si la carpeta es un repositorio de git (se bajo con git clone) y hay
//   internet, al abrir se fija si hay commits nuevos en GitHub. Si los hay,
//   pregunta con un cartel que lista los cambios; con "Si" hace git pull y,
//   si la actualizacion trae un NewCampus.exe nuevo, abre ese y se cierra.
//   Windows no deja reemplazar un .exe mientras corre, pero si renombrarlo:
//   antes del pull este .exe se renombra a NewCampus.exe.viejo y deja una
//   copia igual con su nombre, asi git lo reemplaza sin trabas. Si el pull
//   falla, todo vuelve a como estaba. El .viejo lo borra la version nueva.
//   No pregunta si ya hay un NewCampus abierto ni si no hay nada nuevo
//   (el que programa y sube los cambios nunca va a estar atrasado).
//   Los datos del usuario no estan en el repositorio: no se tocan.
//
// Requisitos:
//   Al arrancar revisa lo que el campus necesita y, si falta algo, lo dice en
//   un solo cartel con lo que hay que instalar: un navegador predeterminado,
//   conexion a internet (las formulas se cargan de internet) y, solo si faltan
//   los apuntes generados, Python 3 para armarlos. El .NET Framework 4 no se
//   puede revisar desde aca: es lo que hace correr este .exe, y si faltara
//   Windows avisa por su cuenta antes de abrirlo.
//   NewCampus.exe --diagnostico=archivo.txt escribe el resultado sin mostrar
//   nada (sirve para probarlo).
//
// Seguridad:
//   - Escucha en "localhost" y ademas rechaza todo pedido que no venga de esta
//     misma PC: no se puede entrar desde otra computadora de la red.
//   - Nunca sirve archivos fuera de app\ (se valida la ruta final).
//   - /api/datos exige el encabezado X-NewCampus y, si viene, el mismo origen:
//     otra pagina web abierta en el navegador no puede leer ni pisar los datos.
//   - No toca el registro de Windows. Si una version anterior dejo la clave
//     "newcampus", la borra al arrancar.
//
// Para recompilar (desde la carpeta NewCampus):
//   C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /nologo /target:winexe
//     /win32icon:app\lanzador\newcampus.ico /r:System.Windows.Forms.dll /r:System.Drawing.dll
//     /out:NewCampus.exe app\lanzador\NewCampus.cs

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Net;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using Microsoft.Win32;

static class NewCampus
{
    const string TITULO = "NewCampus";
    const int PUERTO_BASE = 47800;   // si esta ocupado prueba los 9 siguientes
    const int PUERTOS = 10;

    // 150 s y no 30: cuando la ventana queda en segundo plano Chrome frena los
    // temporizadores de la pagina hasta 1 latido por minuto. El cierre rapido al
    // cerrar la pestania lo da el aviso /api/adios, no este numero.
    const int SIN_LATIDO = 150;       // segundos sin latido -> se apaga
    const int TRAS_ADIOS = 5;         // segundos despues de un adios sin latido nuevo
    const int SIN_ABRIR = 120;        // si el navegador nunca abrio la pagina

    static string app;
    static string origen;             // http://localhost:47800
    static HttpListener servidor;
    static NotifyIcon icono;
    static DateTime arranque = DateTime.UtcNow;
    static DateTime ultimoLatido = DateTime.MinValue;
    static DateTime adios = DateTime.MinValue;
    // Numero de esta corrida: la pagina lo usa para saber si el contador de
    // tiempo que tiene guardado es de este NewCampus o de uno anterior.
    static readonly string corrida = Guid.NewGuid().ToString("N");

    [STAThread]
    static int Main(string[] args)
    {
        app = Path.GetFullPath(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "app"));
        if (!File.Exists(Path.Combine(app, "index.html")))
        {
            Aviso("No encuentro app\\index.html.\n\nNewCampus.exe tiene que estar al lado de la carpeta app.",
                  MessageBoxIcon.Error);
            return 1;
        }

        BorrarRegistroViejo();
        BorrarExeViejo();
        bool abrirNavegador = Array.IndexOf(args, "--sin-navegador") < 0;   // solo para pruebas

        // Internet se prueba en paralelo: si hay conexion tarda un instante,
        // y si no la hay no se quiere hacer esperar el arranque de mas.
        bool hayInternet = false;
        var pruebaInternet = new Thread(() => { hayInternet = HayInternet(); }) { IsBackground = true };
        pruebaInternet.Start();

        string diagnostico = null;
        foreach (string a in args) { if (a.StartsWith("--diagnostico=")) { diagnostico = a.Substring(14); } }
        if (diagnostico != null)
        {
            pruebaInternet.Join(5000);
            var falta = Faltantes(hayInternet, null, BuscarPython() != null);
            File.WriteAllText(diagnostico, falta.Count == 0 ? "OK" : string.Join(Environment.NewLine + Environment.NewLine, falta.ToArray()));
            return 0;
        }

        // Actualizaciones: antes de levantar nada, y solo si no hay otro
        // NewCampus abierto (ese es el que manda).
        if (Array.IndexOf(args, "--sin-actualizar") < 0 && BuscarAbierto() == null)
        {
            pruebaInternet.Join(5000);
            if (hayInternet && Actualizar(args)) { return 0; }   // se abrio la version nueva
        }

        // Sin los apuntes generados no hay nada que mostrar. Si esta Python,
        // se generan solos; si no, se avisa que hay que instalarlo.
        if (!File.Exists(Path.Combine(app, "generado", "indice.js")))
        {
            string python = BuscarPython();
            if (python != null) { Generar(python); }
            if (!File.Exists(Path.Combine(app, "generado", "indice.js")))
            {
                pruebaInternet.Join(5000);
                Aviso(Cartel(Faltantes(hayInternet, null, python != null)), MessageBoxIcon.Error);
                return 1;
            }
        }

        bool primero;
        using (var unico = new Mutex(true, "Local\\NewCampus", out primero))
        {
            if (!primero)
            {
                // Ya hay uno corriendo: se abre el navegador en ese y listo.
                string abierto = BuscarAbierto();
                if (abierto != null) { if (abrirNavegador) { Abrir(abierto); } }
                else { Aviso("NewCampus ya se esta abriendo. Espera unos segundos.", MessageBoxIcon.Information); }
                return 0;
            }

            if (!Iniciar())
            {
                Aviso("No se pudo iniciar el servidor local: los puertos " + PUERTO_BASE + " a " +
                      (PUERTO_BASE + PUERTOS - 1) + " estan ocupados.", MessageBoxIcon.Error);
                return 1;
            }

            pruebaInternet.Join(5000);
            var faltan = Faltantes(hayInternet, origen, true);
            if (faltan.Count > 0) { Aviso(Cartel(faltan), MessageBoxIcon.Warning); }

            if (abrirNavegador && !Abrir(origen + "/") && faltan.Count == 0)
            {
                // habia navegador configurado, pero no se dejo abrir
                Aviso("No se pudo abrir el navegador.\n\nPodes abrir el campus a mano escribiendo esta " +
                      "direccion en Edge, Chrome o Firefox:\n\n" + origen + "/", MessageBoxIcon.Warning);
            }
            using (icono = CrearIcono())
            using (new System.Threading.Timer(_ => Vigilar(), null, 2000, 2000))
            {
                string actualizado = null;
                foreach (string a in args) { if (a.StartsWith("--actualizado=")) { actualizado = a.Substring(14); } }
                if (actualizado != null) { avisoActualizado = actualizado; }
                if (avisoActualizado != null)
                {
                    icono.ShowBalloonTip(6000, TITULO, "NewCampus se actualiz\u00f3: " + avisoActualizado + ".", ToolTipIcon.Info);
                }
                Application.Run();
                icono.Visible = false;
            }
            servidor.Close();
        }
        return 0;
    }

    /* ---------------- actualizaciones ----------------
       Se pregunta a GitHub (git fetch) si hay commits nuevos. Todo git corre
       sin ventana, sin pedir nada por consola y con tiempo maximo. */

    static string avisoActualizado;   // para el globito del icono al terminar

    static bool Actualizar(string[] args)
    {
        string raiz = Path.GetFullPath(AppDomain.CurrentDomain.BaseDirectory).TrimEnd('\\');
        if (!Directory.Exists(Path.Combine(raiz, ".git"))) { return false; }   // bajado sin git
        int c;
        if (Git(raiz, "--version", 5000, out c) == null || c != 0) { return false; }   // git no instalado

        Git(raiz, "fetch --quiet", 20000, out c);
        if (c != 0) { return false; }
        string cuenta = Git(raiz, "rev-list --count HEAD..@{u}", 5000, out c);
        int nuevas;
        if (c != 0 || !int.TryParse((cuenta ?? "").Trim(), out nuevas) || nuevas <= 0) { return false; }

        string lista = Git(raiz, "-c i18n.logOutputEncoding=UTF-8 log -n 8 \"--format=- %s\" HEAD..@{u}", 5000, out c) ?? "";
        string texto = (nuevas == 1 ? "Hay 1 actualizaci\u00f3n nueva" : "Hay " + nuevas + " actualizaciones nuevas") +
                       " de NewCampus:\n\n" + lista.Trim() +
                       (nuevas > 8 ? "\n(y " + (nuevas - 8) + " m\u00e1s)" : "") +
                       "\n\n\u00bfQuer\u00e9s actualizar ahora? Tus datos (calendario, autoevaluaciones, la ruta...) no se tocan.";
        bool sinPreguntar = Array.IndexOf(args, "--actualizar-sin-preguntar") >= 0;   // solo para pruebas
        if (!sinPreguntar &&
            MessageBox.Show(texto, TITULO + " - actualizaci\u00f3n", MessageBoxButtons.YesNo, MessageBoxIcon.Question) != DialogResult.Yes)
        {
            return false;
        }

        // Si la actualizacion trae un NewCampus.exe nuevo, este (que esta
        // corriendo) se corre de lugar y deja una copia igual con su nombre.
        string exe = Application.ExecutablePath;
        string viejo = exe + ".viejo";
        string cambiaExe = Git(raiz, "diff --name-only HEAD @{u} -- \"" + Path.GetFileName(exe) + "\"", 5000, out c);
        bool tocaExe = c == 0 && !string.IsNullOrEmpty((cambiaExe ?? "").Trim());
        bool movido = false;
        if (tocaExe)
        {
            try
            {
                if (File.Exists(viejo)) { File.Delete(viejo); }
                File.Move(exe, viejo);
                movido = true;
                File.Copy(viejo, exe);
            }
            catch
            {
                if (movido && !File.Exists(exe)) { try { File.Move(viejo, exe); } catch { } }
                Aviso("No se pudo preparar la actualizaci\u00f3n (no se pudo mover NewCampus.exe). " +
                      "Se abre la versi\u00f3n que ten\u00e9s.", MessageBoxIcon.Warning);
                return false;
            }
        }

        string salida = Git(raiz, "pull --ff-only --quiet", 90000, out c);
        if (c != 0)
        {
            if (movido) { try { File.Delete(exe); File.Move(viejo, exe); } catch { } }
            string detalle = (salida ?? "no respondi\u00f3 a tiempo").Trim();
            if (detalle.Length > 600) { detalle = detalle.Substring(0, 600) + "..."; }
            Aviso("No se pudo actualizar NewCampus. Se abre la versi\u00f3n que ten\u00e9s.\n\n" +
                  "Lo m\u00e1s com\u00fan: hay archivos del campus cambiados a mano en esta carpeta. " +
                  "Lo que dijo git:\n\n" + detalle, MessageBoxIcon.Warning);
            return false;
        }

        string resumen = nuevas == 1 ? "1 cambio nuevo" : nuevas + " cambios nuevos";
        if (!tocaExe)
        {
            // el .exe es el mismo: se sigue abriendo este, ya con los apuntes nuevos
            avisoActualizado = resumen;
            return false;
        }

        // Abrir la version nueva (con los mismos argumentos) y cerrar esta.
        var nuevos = new List<string>();
        foreach (string a in args)
        {
            if (a != "--actualizar-sin-preguntar" && !a.StartsWith("--actualizado=")) { nuevos.Add(Comillas(a)); }
        }
        nuevos.Add("--sin-actualizar");
        nuevos.Add(Comillas("--actualizado=" + resumen));
        try
        {
            Process.Start(new ProcessStartInfo(exe, string.Join(" ", nuevos.ToArray()))
            {
                UseShellExecute = false, WorkingDirectory = raiz
            });
            return true;
        }
        catch
        {
            Aviso("NewCampus se actualiz\u00f3, pero no se pudo abrir la versi\u00f3n nueva. Abrilo de nuevo con doble clic.",
                  MessageBoxIcon.Warning);
            return true;
        }
    }

    static string Comillas(string a) { return a.IndexOf(' ') >= 0 ? "\"" + a + "\"" : a; }

    // Corre git sin ventana. Devuelve lo que escribio (salida y errores), o
    // null si no se pudo correr o no termino a tiempo.
    static string Git(string carpeta, string argumentos, int espera, out int codigo)
    {
        codigo = -1;
        try
        {
            var inicio = new ProcessStartInfo("git", argumentos)
            {
                UseShellExecute = false, CreateNoWindow = true, WorkingDirectory = carpeta,
                RedirectStandardOutput = true, RedirectStandardError = true,
                StandardOutputEncoding = Encoding.UTF8, StandardErrorEncoding = Encoding.UTF8
            };
            // nunca pedir usuario, clave ni confirmaciones por consola
            inicio.EnvironmentVariables["GIT_TERMINAL_PROMPT"] = "0";
            inicio.EnvironmentVariables["GCM_INTERACTIVE"] = "never";
            var texto = new StringBuilder();
            using (var p = new Process { StartInfo = inicio })
            {
                p.OutputDataReceived += (s, e) => { if (e.Data != null) { lock (texto) { texto.AppendLine(e.Data); } } };
                p.ErrorDataReceived += (s, e) => { if (e.Data != null) { lock (texto) { texto.AppendLine(e.Data); } } };
                p.Start();
                p.BeginOutputReadLine();
                p.BeginErrorReadLine();
                if (!p.WaitForExit(espera)) { try { p.Kill(); } catch { } return null; }
                p.WaitForExit();
                codigo = p.ExitCode;
            }
            lock (texto) { return texto.ToString(); }
        }
        catch { return null; }
    }

    // El .exe anterior a una actualizacion queda como NewCampus.exe.viejo.
    // Se borra al arrancar; puede tardar un momento en soltarse, asi que se
    // reintenta un rato en segundo plano.
    static void BorrarExeViejo()
    {
        string viejo = Application.ExecutablePath + ".viejo";
        if (!File.Exists(viejo)) { return; }
        new Thread(() =>
        {
            for (int i = 0; i < 20 && File.Exists(viejo); i++)
            {
                try { File.Delete(viejo); } catch { Thread.Sleep(500); }
            }
        }) { IsBackground = true }.Start();
    }

    /* ---------------- servidor ---------------- */

    static bool Iniciar()
    {
        for (int p = PUERTO_BASE; p < PUERTO_BASE + PUERTOS; p++)
        {
            var intento = new HttpListener();
            intento.Prefixes.Add("http://localhost:" + p + "/");
            try { intento.Start(); }
            catch (HttpListenerException) { intento.Close(); continue; }

            servidor = intento;
            origen = "http://localhost:" + p;
            var hilo = new Thread(Escuchar) { IsBackground = true };
            hilo.Start();
            return true;
        }
        return false;
    }

    static void Escuchar()
    {
        while (servidor.IsListening)
        {
            HttpListenerContext ctx;
            try { ctx = servidor.GetContext(); }
            catch { return; }   // se cerro el servidor
            ThreadPool.QueueUserWorkItem(_ => Atender(ctx));
        }
    }

    static void Atender(HttpListenerContext ctx)
    {
        var req = ctx.Request;
        var res = ctx.Response;
        try
        {
            // doble candado: aunque http.sys ya filtra por "localhost",
            // se rechaza cualquier pedido que no venga de esta misma PC
            if (!req.IsLocal) { res.StatusCode = 403; return; }

            res.Headers["X-Content-Type-Options"] = "nosniff";
            string ruta = Uri.UnescapeDataString(req.Url.AbsolutePath);

            if (ruta == "/api/estado")
            {
                Json(res, 200, "{\"app\":\"NewCampus\",\"instancia\":\"" + corrida + "\"}");
            }
            else if (ruta == "/api/ping")
            {
                ultimoLatido = DateTime.UtcNow;
                Json(res, 200, "{\"ok\":true}");
            }
            else if (ruta == "/api/adios")
            {
                adios = DateTime.UtcNow;
                Json(res, 200, "{\"ok\":true}");
            }
            else if (ruta == "/api/datos")
            {
                Datos(req, res);
            }
            else if (req.HttpMethod == "GET" || req.HttpMethod == "HEAD")
            {
                Archivo(req, res, ruta);
            }
            else
            {
                res.StatusCode = 405;
            }
        }
        catch { try { res.StatusCode = 500; } catch { } }
        finally { try { res.Close(); } catch { } }
    }

    static void Archivo(HttpListenerRequest req, HttpListenerResponse res, string ruta)
    {
        if (ruta.EndsWith("/")) { ruta += "index.html"; }
        string completo;
        try { completo = Path.GetFullPath(Path.Combine(app, ruta.TrimStart('/').Replace('/', '\\'))); }
        catch { res.StatusCode = 400; return; }

        // nada fuera de app\ (evita ..\ y rutas absolutas)
        if (!completo.StartsWith(app + "\\", StringComparison.OrdinalIgnoreCase) || !File.Exists(completo))
        {
            res.StatusCode = 404;
            return;
        }

        res.ContentType = TipoDe(completo);
        res.Headers["Cache-Control"] = "no-cache";   // siempre la ultima version de los apuntes
        // FileShare.Delete: construir.py puede reemplazar el archivo mientras se lee
        using (var fs = new FileStream(completo, FileMode.Open, FileAccess.Read,
                                       FileShare.ReadWrite | FileShare.Delete))
        {
            res.ContentLength64 = fs.Length;
            if (req.HttpMethod == "GET") { fs.CopyTo(res.OutputStream); }
        }
    }

    static string TipoDe(string archivo)
    {
        switch (Path.GetExtension(archivo).ToLowerInvariant())
        {
            case ".html": return "text/html; charset=utf-8";
            case ".js":   return "text/javascript; charset=utf-8";
            case ".css":  return "text/css; charset=utf-8";
            case ".json": return "application/json; charset=utf-8";
            case ".svg":  return "image/svg+xml";
            case ".png":  return "image/png";
            case ".jpg":
            case ".jpeg": return "image/jpeg";
            case ".ico":  return "image/x-icon";
            case ".pdf":  return "application/pdf";
            case ".md":
            case ".txt":  return "text/plain; charset=utf-8";
            default:      return "application/octet-stream";
        }
    }

    /* ---------------- datos del usuario ----------------
       Un solo archivo JSON por PC, fuera de la carpeta del repositorio. */

    const int MAX_DATOS = 10 * 1024 * 1024;   // 10 MB: de sobra para texto
    static readonly object candadoDatos = new object();

    static string CarpetaDatos()
    {
        return Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "NewCampus");
    }

    static void Datos(HttpListenerRequest req, HttpListenerResponse res)
    {
        // Solo la propia pagina: se exige un encabezado que otra pagina web no
        // puede mandar sin permiso, y si viene el origen tiene que ser este.
        string origenPedido = req.Headers["Origin"];
        if (req.Headers["X-NewCampus"] != "1" || (origenPedido != null && origenPedido != origen))
        {
            res.StatusCode = 403;
            return;
        }

        string archivo = Path.Combine(CarpetaDatos(), "datos.json");

        if (req.HttpMethod == "GET")
        {
            string contenido = null;
            lock (candadoDatos)
            {
                if (File.Exists(archivo)) { contenido = File.ReadAllText(archivo, Encoding.UTF8); }
            }
            if (contenido == null || contenido.Trim().Length == 0)
            {
                Json(res, 200, "{\"app\":\"NewCampus\",\"existe\":false}");
            }
            else
            {
                Json(res, 200, "{\"app\":\"NewCampus\",\"existe\":true,\"contenido\":" + contenido + "}");
            }
            return;
        }

        if (req.HttpMethod != "POST") { res.StatusCode = 405; return; }
        if (req.ContentLength64 > MAX_DATOS) { res.StatusCode = 413; return; }

        string cuerpo;
        using (var lector = new StreamReader(req.InputStream, Encoding.UTF8)) { cuerpo = lector.ReadToEnd(); }
        cuerpo = cuerpo.Trim();
        // lo minimo para no guardar basura: un objeto JSON y de un tamanio razonable
        if (cuerpo.Length == 0 || cuerpo.Length > MAX_DATOS || cuerpo[0] != '{' || cuerpo[cuerpo.Length - 1] != '}')
        {
            res.StatusCode = 400;
            return;
        }

        lock (candadoDatos)
        {
            Directory.CreateDirectory(CarpetaDatos());
            // se escribe aparte y se reemplaza de una vez; la version anterior queda de respaldo
            string temporal = archivo + ".tmp";
            File.WriteAllText(temporal, cuerpo, new UTF8Encoding(false));
            if (File.Exists(archivo))
            {
                File.Replace(temporal, archivo, Path.Combine(CarpetaDatos(), "datos.anterior.json"));
            }
            else
            {
                File.Move(temporal, archivo);
            }
        }
        Json(res, 200, "{\"ok\":true}");
    }

    static void Json(HttpListenerResponse res, int estado, string cuerpo)
    {
        byte[] datos = Encoding.UTF8.GetBytes(cuerpo);
        res.StatusCode = estado;
        res.ContentType = "application/json; charset=utf-8";
        res.Headers["Cache-Control"] = "no-store";
        res.ContentLength64 = datos.Length;
        res.OutputStream.Write(datos, 0, datos.Length);
    }

    /* ---------------- apagado automatico ----------------
       La pagina late cada 10 segundos. Si deja de latir es que se cerro la
       pestania (o el navegador), asi que no tiene sentido seguir escuchando. */

    static void Vigilar()
    {
        var ahora = DateTime.UtcNow;
        bool hubo = ultimoLatido != DateTime.MinValue;

        bool cerrar =
            (!hubo && (ahora - arranque).TotalSeconds > SIN_ABRIR) ||
            (hubo && (ahora - ultimoLatido).TotalSeconds > SIN_LATIDO) ||
            (adios != DateTime.MinValue && ultimoLatido < adios &&
             (ahora - adios).TotalSeconds > TRAS_ADIOS);

        if (cerrar) { Salir(); }
    }

    static void Salir()
    {
        if (icono != null) { icono.Visible = false; }
        Application.Exit();
    }

    /* ---------------- icono junto al reloj ---------------- */

    static NotifyIcon CrearIcono()
    {
        var n = new NotifyIcon
        {
            Icon = Icon.ExtractAssociatedIcon(Application.ExecutablePath),
            Text = "NewCampus (" + origen.Replace("http://", "") + ")",
            Visible = true
        };
        n.ContextMenu = new ContextMenu(new[]
        {
            new MenuItem("Abrir NewCampus", (s, e) => Abrir(origen + "/")),
            new MenuItem("-"),
            new MenuItem("Cerrar NewCampus", (s, e) => Salir())
        });
        n.DoubleClick += (s, e) => Abrir(origen + "/");
        return n;
    }

    /* ---------------- varios ---------------- */

    static string BuscarAbierto()
    {
        for (int p = PUERTO_BASE; p < PUERTO_BASE + PUERTOS; p++)
        {
            try
            {
                var pedido = (HttpWebRequest)WebRequest.Create("http://localhost:" + p + "/api/estado");
                pedido.Timeout = 800;
                using (var r = pedido.GetResponse())
                using (var lector = new StreamReader(r.GetResponseStream()))
                {
                    if (lector.ReadToEnd().Contains("NewCampus")) { return "http://localhost:" + p + "/"; }
                }
            }
            catch { }
        }
        return null;
    }

    // Las versiones anteriores registraban el enlace newcampus: en Windows. Ya no hace falta.
    static void BorrarRegistroViejo()
    {
        try { Registry.CurrentUser.DeleteSubKeyTree(@"Software\Classes\newcampus", false); } catch { }
    }

    static bool Abrir(string url)
    {
        try { Process.Start(url); return true; } catch { return false; }
    }

    /* ---------------- requisitos ----------------
       Lo que el campus necesita ademas de este .exe. Todo lo que falte se
       junta en una sola lista, cada cosa con que es y como conseguirla. */

    static List<string> Faltantes(bool hayInternet, string direccion, bool hayPython)
    {
        var falta = new List<string>();

        if (!File.Exists(Path.Combine(app, "generado", "indice.js")) && hayPython)
        {
            falta.Add("LOS APUNTES GENERADOS - falta la carpeta app\\generado y no se pudo armar sola. " +
                      "Abri una consola en la carpeta app y corre: python construir.py (ahi se ve el error).");
        }
        else if (!File.Exists(Path.Combine(app, "generado", "indice.js")))
        {
            falta.Add("PYTHON 3 - faltan los apuntes generados (la carpeta app\\generado) y para " +
                      "armarlos hace falta Python 3. Instalalo desde https://www.python.org/downloads/ " +
                      "marcando la opcion \"Add python.exe to PATH\", y volve a abrir NewCampus: " +
                      "los apuntes se generan solos.");
        }
        if (!HayNavegador())
        {
            falta.Add("UN NAVEGADOR WEB - no hay ninguno elegido como predeterminado. Instala Microsoft " +
                      "Edge, Google Chrome o Firefox, o elegi uno en Configuracion > Aplicaciones > " +
                      "Aplicaciones predeterminadas." +
                      (direccion != null ? " Mientras tanto, el campus se abre escribiendo " + direccion +
                       "/ en cualquier navegador." : ""));
        }
        if (!hayInternet)
        {
            falta.Add("CONEXION A INTERNET - las formulas matematicas se cargan de internet. Sin " +
                      "conexion el campus abre igual, pero las formulas se ven como texto (por ejemplo " +
                      "\\frac{1}{2}) hasta que vuelva la conexion.");
        }
        return falta;
    }

    static string Cartel(List<string> falta)
    {
        return "Para que NewCampus funcione bien falta:\n\n- " + string.Join("\n\n- ", falta.ToArray());
    }

    // Navegador predeterminado: el que eligio el usuario para los enlaces http,
    // o en su defecto el que tenga registrado Windows.
    static bool HayNavegador()
    {
        try
        {
            using (var k = Registry.CurrentUser.OpenSubKey(
                @"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice"))
            {
                string prog = k == null ? null : k.GetValue("ProgId") as string;
                if (!string.IsNullOrEmpty(prog))
                {
                    using (var c = Registry.ClassesRoot.OpenSubKey(prog + @"\shell\open\command"))
                    {
                        if (c != null) { return true; }
                    }
                }
            }
            using (var c = Registry.ClassesRoot.OpenSubKey(@"http\shell\open\command"))
            {
                return c != null;
            }
        }
        catch { return true; }   // si no se puede leer el registro, no se asusta a nadie
    }

    // Se prueba contra el mismo lugar del que la pagina carga MathJax.
    static bool HayInternet()
    {
        try
        {
            ServicePointManager.SecurityProtocol |= (SecurityProtocolType)3072;   // TLS 1.2
            var pedido = (HttpWebRequest)WebRequest.Create("https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js");
            pedido.Method = "HEAD";
            pedido.Timeout = 4000;
            using (pedido.GetResponse()) { return true; }
        }
        catch { return false; }
    }

    // "py" es el lanzador oficial de Python en Windows; "python" puede ser el
    // atajo de la Microsoft Store que no tiene Python instalado: por eso se
    // pide la version y se exige que diga "Python 3".
    static string BuscarPython()
    {
        foreach (string comando in new[] { "py", "python" })
        {
            try
            {
                var inicio = new ProcessStartInfo(comando, "--version")
                {
                    UseShellExecute = false, CreateNoWindow = true,
                    RedirectStandardOutput = true, RedirectStandardError = true
                };
                using (var p = Process.Start(inicio))
                {
                    string salida = p.StandardOutput.ReadToEnd() + p.StandardError.ReadToEnd();
                    p.WaitForExit(5000);
                    if (salida.Contains("Python 3")) { return comando; }
                }
            }
            catch { }
        }
        return null;
    }

    static void Generar(string python)
    {
        try
        {
            var inicio = new ProcessStartInfo(python, "construir.py")
            {
                UseShellExecute = false, CreateNoWindow = true, WorkingDirectory = app
            };
            using (var p = Process.Start(inicio)) { p.WaitForExit(120000); }
        }
        catch { }
    }

    static void Aviso(string texto, MessageBoxIcon icono)
    {
        MessageBox.Show(texto, TITULO, MessageBoxButtons.OK, icono);
    }
}
