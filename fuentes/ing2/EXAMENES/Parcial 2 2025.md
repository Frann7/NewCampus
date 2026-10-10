# Parcial N°2 — Ingeniería del Software II — 8 de octubre de 2025

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/SEGUNDO CUATRIMESTRE/EXAMENES/Parcial 2a/2b/2c 8-10-2025.png`
(tres fotos) · transcripto a mano. El puntaje de la Práctica no figura en las fotos (la Teoría suma 50).

## Teoría

La empresa SoftMetrics desarrolla soluciones web y aplicaciones empresariales bajo un enfoque de
Programación Orientada a Objetos (POO).

En la actualidad presenta las siguientes características:

- Utiliza herramientas de control de versiones (Git) y gestión de proyectos (Jira).
- Los equipos siguen un proceso de desarrollo documentado, pero no todos lo aplican con la misma
  rigurosidad.
- No realiza mediciones cuantitativas del desempeño ni del cumplimiento de los procesos.
- Las revisiones de código son manuales y dependen de la experiencia del revisor.
- La empresa quiere incorporar Inteligencia Artificial (IA) para mejorar la calidad y la
  productividad, por ejemplo, usando herramientas como Codex o Copilot para sugerir código y
  detectar errores.
- No posee aún un sistema formal de análisis predictivo ni de optimización automática de procesos.
- El equipo de desarrollo trabaja con Programación Orientada a Objetos (POO) y planea incorporar
  dos patrones de diseño en su solución empresarial, la creación flexible de familias de objetos y
  otro para conectar módulos con interfaces incompatibles con los existentes del sistema.

Responder:

1. **5 Puntos.** ¿En qué nivel de madurez del modelo CMMI se encuentra actualmente SoftMetrics?
   Justifique brevemente. ¿Qué riesgos o limitaciones enfrenta la empresa si no avanza al siguiente
   nivel?
2. **10 Puntos.** Proponga tres acciones concretas que podrían ayudarla a llegar al Nivel 5,
   integrando el uso de herramientas de Inteligencia Artificial.
3. **5 Puntos.** Indique los pasos que debe seguir el equipo de desarrollo para registrar todos los
   cambios del código desde el Working Directory hacia la rama develop, y luego integrarlos en main,
   asegurando que ambas ramas estén actualizadas en el remoto (*Git Workflow*).
4. **20 Puntos.** Represente mediante un diagrama UML la estructura de los patrones de diseño que
   quiere incorporar SoftMetrics. Explique el propósito de cada uno dentro del sistema.
5. **10 Puntos.** Defina un ejemplo de métrica de calidad del software que la empresa podría
   implementar. Para ello, complete: Atributo, Medida, Unidad de medida, Indicador, Métrica.

## Práctica

**1-** A partir del siguiente enunciado identifique cuáles serían los patrones de diseño que
utilizaría y justifique por qué eligió los mismos.

La empresa **Muebles Express S.A.** se dedica a la fabricación y comercialización de muebles
personalizados a través de su plataforma web. Los clientes pueden ingresar al sitio, navegar por el
catálogo de productos y seleccionar los muebles que desean comprar, teniendo la posibilidad de
personalizar cada artículo según diferentes parámetros: tipo de material, color, tamaño y estilo de
ensamblaje. Cada cliente debe poder elegir su combinación preferida de estas opciones, de manera que
el sistema aplique automáticamente la estrategia de configuración más adecuada según sus elecciones
y genere un presupuesto final.

Una vez realizada la compra, el pedido se envía al área de producción de la empresa, donde un
sistema interno se encarga de crear los muebles según las especificaciones del cliente. Para cada
tipo de mueble —como sillas, mesas, estanterías o escritorios— existe un procedimiento de
fabricación específico que permite instanciar los objetos correspondientes sin que el área de ventas
tenga que conocer los detalles internos de la producción. Esto asegura que la creación de los
muebles sea flexible y escalable, permitiendo agregar nuevos tipos de productos sin afectar la
lógica de compra.

Cuando la fabricación del mueble se completa, el sistema notifica automáticamente al cliente a
través de correo electrónico o mensajes en la plataforma web, informándole que su pedido está listo
para ser enviado o retirado. Además, el cliente puede suscribirse para recibir actualizaciones sobre
el estado de su pedido en tiempo real, de manera que cualquier cambio relevante —como retrasos,
avances en la producción o confirmación de despacho— se comunique de forma inmediata y automática.

**2-** Dado el siguiente código en PHP identifique el patrón que se implementa en el mismo y explique
qué elementos ayudaron a identificarlo.

```php
<?php
namespace ...\api\RealWorld;

class YouTubeDownloader
{   protected $youtube;
    protected $ffmpeg;
    public function __construct(string $youtubeApiKey)
    {   $this->youtube = new YouTube($youtubeApiKey);
        $this->ffmpeg = new FFMpeg();
    }
    public function downloadVideo(string $url): void
    {
        echo "Fetching video metadata from youtube...\n";
        // $title = $this->youtube->fetchVideo($url)->getTitle();
        echo "Saving video file to a temporary file...\n";
        // $this->youtube->saveAs($url, "video.mpg");

        echo "Processing source video...\n";
        // $video = $this->ffmpeg->open('video.mpg');
        echo "Normalizing and resizing the video to smaller dimensions...\n";
        // $video
        //     ->filters()
        //     ->resize(new FFMpeg\Coordinate\Dimension(320, 240))
        //     ->synchronize();
        echo "Capturing preview image...\n";
        // $video
        //     ->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(10))
        //     ->save($title . 'frame.jpg');
        echo "Saving video in target formats...\n";
        // $video
        //     ->save(new FFMpeg\Format\Video\X264(), $title . '.mp4')
        //     ->save(new FFMpeg\Format\Video\WMV(), $title . '.wmv')
        //     ->save(new FFMpeg\Format\Video\WebM(), $title . '.webm');
        echo "Done!\n";
    }
}
class YouTube
{   public function fetchVideo(): string
    {   }
    public function saveAs(string $path): void
    {   }
}
class FFMpeg
{   public static function create(): FFMpeg
    {   }
    public function open(string $video): void
    {   }
}
class FFMpegVideo
{   public function filters(): self
    {   }
    public function resize(): self
    {   }
    public function synchronize(): self
    {   }
    public function frame(): self
    {   }
    public function save(string $path): self
    {   }
}
function clientCode(YouTubeDownloader $api)
{   $api->downloadVideo("https://www.youtube.com/watch?v=QH2-TGUlwu4"); }
$api = new YouTubeDownloader("APIKEY-XXXXXXXXX");
clientCode($api);
?>
```
