# Guia Nº2 Ejercicios - Patrones estructurales

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/SEGUNDO CUATRIMESTRE/PATRONES DE DISEÑO/PRACTICA/Guia Nº2 Ejercicios - Patrones estructurales.docx` · texto sacado del .docx.
⚠ El ej. 4 trae un diagrama UML (imagen) que no está en el texto: el mismo de Libro / Libro digital / Administrable de `practica 2 patrones.md`, ej. 1.

Guia Nº2 de Patrones - Patrones estructurales

Ejercicio 1:
Según el siguiente diagrama en C++, identifique que de qué patrón se trata, y que elementos ayudaron a detectar el patrón mencionado 

class Target {
 public:
  virtual ~Target() = default;

  virtual std::string Request() const {
    return "Target: The default target's behavior.";
  }
};
class convierte {
 public:
  std::string SpecificRequest() const {
    return ".eetpadA eht fo roivaheb laicepS";
  }
};
class conversor : public Target {
 private:
  convierte *convierte_;

 public:
  conversor(convierte *convierte) : convierte_(convierte) {}
  std::string Request() const override {
    std::string to_reverse = this->convierte_->SpecificRequest();
    std::reverse(to_reverse.begin(), to_reverse.end());
    return "conversor: (TRANSLATED) " + to_reverse;
  }
};
void ClientCode(const Target *target) {
  std::cout << target->Request();
}

int main() {
  std::cout << "Client: I can work just fine with the Target objects:\n";
  Target *target = new Target;
  ClientCode(target);
  std::cout << "\n\n";
  convierte *convierte = new convierte;
  std::cout << "Client: The convierte class has a weird interface. See, I don't understand it:\n";
  std::cout << "convierte: " << convierte->SpecificRequest();
  std::cout << "\n\n";
  std::cout << "Client: But I can work with it via the conversor:\n";
  conversor *conversor = new conversor(convierte);
  ClientCode(conversor);
  std::cout << "\n";
  delete target;
  delete convierte;
  delete conversor;
  return 0;
}
Ejercicio 2
Dado el siguiente código identifique el lenguaje de programación que en que se está implementado,  que tipo de patrón se implementa y realice el diagrama correspondiente.

<?php
namespace Git\ZZZZ\Conceptual;
abstract class Component
{
    protected $parent; 
    public function setParent(?Component $parent)
    {
        $this->parent = $parent;
    }
    public function getParent(): Component
    {
        return $this->parent;
    }

    public function add(Component $component): void { }
    public function remove(Component $component): void { }
    public function ismolecula(): bool
    {
        return false;
    }

    abstract public function operation(): string;
}

class atomo extends Component
{
    public function operation(): string
    {
        return "atomo";
    }
}

class molecula extends Component
{
    protected $children;
    public function __construct()
    {
        $this->children = new \SplObjectStorage();
    }

    public function add(Component $component): void
    {
        $this->children->attach($component);
        $component->setParent($this);
    }
    public function remove(Component $component): void
    {
        $this->children->detach($component);
        $component->setParent(null);
    }

    public function ismolecula(): bool
    {
        return true;
    }

    public function operation(): string
    {
        $results = [];
        foreach ($this->children as $child) {
            $results[] = $child->operation();
        }
        return "Branch(" . implode("+", $results) . ")";
    }
}

function clientCode(Component $component)
{
    // ...

    echo "RESULT: " . $component->operation();

    // ...
}

$simple = new atomo();
echo "Client: I've got a simple component:\n";
clientCode($simple);
echo "\n\n";

$tree = new molecula();
$branch1 = new molecula();
$branch1->add(new atomo());
$branch1->add(new atomo());
$branch2 = new molecula();
$branch2->add(new atomo());
$tree->add($branch1);
$tree->add($branch2);
echo "Client: Now I've got a subject:\n";
clientCode($tree);
echo "\n\n";

function clientCode2(Component $component1, Component $component2)
{
    // ...

    if ($component1->ismolecula()) {
        $component1->add($component2);
    }
    echo "RESULT: " . $component1->operation();

    // ...
}

echo "Client: I don't need to check the components classes even when managing the tree:\n";
clientCode2($tree, $simple);

Ejercicio 3

Dado el siguiente código identifique el lenguaje de programación que en que se está implementado,  que tipo de patrón se implementa y realice el diagrama correspondiente.

using System;

namespace git.QQQQ.Conceptual
{

    public class Pantalla
    {
        protected Subsystem1 _subsystem1;
        protected Subsystem2 _subsystem2;

        public pantalla(Subsystem1 subsystem1, Subsystem2 subsystem2)
        {
            this._subsystem1 = subsystem1;
            this._subsystem2 = subsystem2;
        }
        
        public string Operation()
        {
            string result = "pantallainitializes subsystems:\n";
            result += this._subsystem1.operation1();
            result += this._subsystem2.operation1();
            result += "pantallaorders subsystems to perform the action:\n";
            result += this._subsystem1.operationN();
            result += this._subsystem2.operationZ();
            return result;
        }
    }

    public class Subsystem1
    {
        public string operation1()
        {
            return "Subsystem1: Ready!\n";
        }

        public string operationN()
        {
            return "Subsystem1: Go!\n";
        }
    }

    public class Subsystem2
    {
        public string operation1()
        {
            return "Subsystem2: Get ready!\n";
        }

        public string operationZ()
        {
            return "Subsystem2: Fire!\n";
        }
    }

    class Client
    {
        public static void ClientCode(pantallapantalla)
        {
            Console.Write(pantalla.Operation());
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            Subsystem1 subsystem1 = new Subsystem1();
            Subsystem2 subsystem2 = new Subsystem2();
            pantallapantalla= new pantalla(subsystem1, subsystem2);
            Client.ClientCode(pantalla);
        }
    }
}

Ejercicio 4
Supongamos que tenemos un sistema que vende libros. Se desea vincular al sistema una clase de tipo libro digital con un funcionamiento diferente al que se está manejando. Se debe adaptar la nueva clase sin que afecte la lógica de la aplicación. Se adjunta una parte del diagrama de UML:

Ejercicio 5
Dado el siguiente enunciado identifique qué patrones se pueden implementar. Una vez identificado, represente el patrón mediante el diagrama de clases implementando los mismos para cada caso.

Una empresa de gestión de contenidos multimedia desea desarrollar una plataforma que permita a sus usuarios organizar, editar y publicar diferentes tipos de archivos digitales (imágenes, videos, documentos, audios). Los usuarios pueden crear colecciones de archivos que a su vez pueden contener otras colecciones, formando una estructura jerárquica que facilita la organización y manejo de grandes cantidades de contenido.
Para simplificar la interacción con el sistema, se requiere una interfaz única que permita realizar operaciones comunes como reproducir, pausar, renombrar o eliminar archivos, sin importar si el usuario está trabajando con un solo archivo o con una colección completa. Además, esta interfaz debe manejar internamente las particularidades de cada tipo de archivo y gestionar la estructura jerárquica de colecciones.
Por otro lado, la plataforma debe integrarse con varias bibliotecas externas para procesamiento y conversión de formatos multimedia (por ejemplo, una biblioteca para edición de imágenes, otra para edición de video y otra para procesamiento de audio). Cada biblioteca tiene una interfaz diferente e incompatible con la del sistema principal.
Finalmente, la empresa quiere que el sistema sea fácil de mantener y ampliar en el futuro, permitiendo agregar nuevos tipos de archivos y servicios externos sin impactar la experiencia del usuario ni la estructura general del código.
