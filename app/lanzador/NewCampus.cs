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
                Application.Run();
                icono.Visible = false;
            }
            servidor.Close();
        }
        return 0;
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
