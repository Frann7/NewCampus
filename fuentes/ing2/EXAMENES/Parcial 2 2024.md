# Modelo de parcial 2 2024

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/SEGUNDO CUATRIMESTRE/Ingeniería de software 2/Cuatrimestre 2/Parcial 2/Modelo de parcial 2 2024.pdf` · 2 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |

<!-- página 1 -->

Ruta Prov. 11, Km 10.5 - Oro Verde, Entre Ríos, Argentina - CP 3101 - fcyt.uader.edu.ar

23 de octubre del 2024

Parcial Nº2 Ing. de Software II

1- Qué patrones de diseño de los vistos en clase, usarían para el siguiente enunciado. Justifique.

En un sistema de alarma de un edificio se consideran detectores de humo, sensores de temperatura, sensores de presión, etc. Todos estos elementos
tienen un estado conectado/desconectado y en consecuencia se puede pasar de un estado a otro (cuando se crean, están desconectados). Todos ellos
son capaces de proporcionar una medida (un valor REAL) y tienen un valor umbral que se fija inicialmente al crear el elemento. El sistema recorre en
un bucle continuo todos sus elementos conectados. Cuando la medida de uno de ellos supera su valor umbral el sistema dispara la alarma. Para evitar
falsas alarmas, varios elementos se pueden unir formando arrays (y los arrays a su vez en otros arrays) y para este sensor complejo, la alarma sólo se
dispara si el valor medio de los elementos del array supera el umbral definido para ese elemento compuesto. Diseñar una solución con las clases
necesarias y sus características para este problema, implementando en Eiffel al menos todo lo relacionado con el disparo de la alarma.

2-  Realice el diagrama (mediante UML) el patrón Singleton, dar una breve descripción de su usabilidad y mencione 2 ejemplos.

3-  En el siguiente diagrama que pertenece a una aplicación farmacéutica, se solicita modelar:

- Se desea crear una clase para mantener la seguridad de los usuarios, llamada GestorUsuarios, dicha clase tendrá métodos para realizar el
login del sistema, cambiar la contraseña del usuario, dar de baja y dar de alta usuarios, por motivos de performance se desea crear una
sola instancia de dicha clase.
- Se necesita implementar mecanismos de para la emisión de lotes de medicamentos, para esto es necesario que cada vez que se imprima
un lote, se envíe una alerta al farmacéutico y este registra el suceso en una tabla de lotes.

<!-- página 2 -->

Ruta Prov. 11, Km 10.5 - Oro Verde, Entre Ríos, Argentina - CP 3101 - fcyt.uader.edu.ar

4- A partir del siguiente código identifique qué patrón es el que se utiliza.

class Facturacion {
 public:
  std::string Operation1() const {
    return "Facturacion: Ready!\n";
  }
  std::string OperationN() const {
    return "Facturacion: Go!\n";
  }};
class Compras {
 public:
  std::string Operation1() const {
    return "Compras: Get ready!\n";
  }
  std::string OperationZ() const {
    return "Compras: Fire!\n";
  }};
class Operador {
 protected:
  Facturacion *Facturacion_;
  Compras *Compras_;
 public:
  Operador(
      Facturacion *Facturacion = nullptr,
      Compras *Compras = nullptr) {
    this->Facturacion_ = Facturacion ?: new Facturacion;
    this->Compras_ = Compras ?: new Compras;
  }
  ~Operador() {
    delete Facturacion_;
    delete Compras_;
  }
  std::string Operation() {
    std::string result = "Operador initializes subsystems:\n";
    result += this->Facturacion_->Operation1();
    result += this->Compras_->Operation1();
