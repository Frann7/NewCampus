# Guia Nº3 Ejercicios - Patrones de comportamiento

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/SEGUNDO CUATRIMESTRE/PATRONES DE DISEÑO/PRACTICA/Guia Nº3 Ejercicios - Patrones de comportamiento.docx` · texto sacado del .docx.
Sin imágenes.

Guia Nº3 de Patrones - Patrones de comportamiento

Ejercicio 1:
Mencione 3 ejemplos donde implementaría el patrón de comportamiento Observer y 3 ejemplos para el patrón de comportamiento Strategy.

Ejercicio 2:
Realice el diagrama correspondiente para representar el patrón observer, identifique cada elemento del patrón y mencione cuales son las ventajas de implementar dicho patrón.

Ejercicio 3:
Identifique el patrón que aparece en el siguiente código en PHP. Realice el diagrama del mismo. Mencione ventajas y desventajas.

<?php
namespace RefactoringGuru\123\Conceptual;
class Context
{
    private $dispositivo;
    public function __construct(dispositivo $dispositivo)
    {
        $this->dispositivo = $dispositivo;
    }
    public function setdispositivo(dispositivo $dispositivo)
    {
        $this->dispositivo = $dispositivo;
    }
    public function doSomeBusinessLogic(): void
    {
        echo "Context: Sorting data using the dispositivo (not sure how it'll do it)\n";
        $result = $this->dispositivo->doAlgorithm(["a", "b", "c", "d", "e"]);
        echo implode(",", $result) . "\n";
    }
}
interface dispositivo
{
    public function doAlgorithm(array $data): array;
}
class ConcretedispositivoA implements dispositivo
{
    public function doAlgorithm(array $data): array
    {
        sort($data);
        return $data;
    }
}
class ConcretedispositivoB implements dispositivo
{
    public function doAlgorithm(array $data): array
    {
        rsort($data);
        return $data;
    }
}
$context = new Context(new ConcretedispositivoA());
echo "Client: dispositivo is set to normal sorting.\n";
$context->doSomeBusinessLogic();
echo "\n";
echo "Client: dispositivo is set to reverse sorting.\n";
$context->setdispositivo(new ConcretedispositivoB());
$context->doSomeBusinessLogic();

Ejercicio 4 Identifique qué patrón de comportamiento se está siendo implementado en el siguiente código en C++ mencione ventajas y desventajas del mismo, y realice el diagrama correspondiente:

#include <iostream>
#include <list>
#include <string>

class Ialarma {
 public:
  virtual ~Ialarma(){};
  virtual void Update(const std::string &message_from_subject) = 0;
};
class ISubject {
 public:
  virtual ~ISubject(){};
  virtual void Attach(Ialarma *alarma) = 0;
  virtual void Detach(Ialarma *alarma) = 0;
  virtual void Notify() = 0;
};
class Subject : public ISubject {
 public:
  virtual ~Subject() {
    std::cout << "Goodbye, I was the Subject.\n";
  }
    void Attach(Ialarma *alarma) override {
    list_alarma_.push_back(alarma);
  }
  void Detach(Ialarma *alarma) override {
    list_alarma_.remove(alarma);
  }
  void Notify() override {
    std::list<Ialarma *>::iterator iterator = list_alarma_.begin();
    HowManyalarma();
    while (iterator != list_alarma_.end()) {
      (*iterator)->Update(message_);
      ++iterator;
    }
  }
  void CreateMessage(std::string message = "Empty") {
    this->message_ = message;
    Notify();
  }
  void HowManyalarma() {
    std::cout << "There are " << list_alarma_.size() << " alarmas in the list.\n";
  }
  void SomeBusinessLogic() {
    this->message_ = "change message message";
    Notify();
    std::cout << "I'm about to do some thing important\n";
  }
 private:
  std::list<Ialarma *> list_alarma_;
  std::string message_;
};
class alarma : public Ialarma {
 public:
  alarma(Subject &subject) : subject_(subject) {
    this->subject_.Attach(this);
    std::cout << "Hi, I'm the alarma \"" << ++alarma::static_number_ << "\".\n";
    this->number_ = alarma::static_number_;
  }
  virtual ~alarma() {
    std::cout << "Goodbye, I was the alarma \"" << this->number_ << "\".\n";
  }
  void Update(const std::string &message_from_subject) override {
    message_from_subject_ = message_from_subject;
    PrintInfo();
  }
  void RemoveMeFromTheList() {
    subject_.Detach(this);
    std::cout << "alarma \"" << number_ << "\" removed from the list.\n";
  }
  void PrintInfo() {
    std::cout << "alarma \"" << this->number_ << "\": a new message is available --> " << this->message_from_subject_ << "\n";
  }
 private:
  std::string message_from_subject_;
  Subject &subject_;
  static int static_number_;
  int number_;
};
int alarma::static_number_ = 0;
void ClientCode() {
  Subject *subject = new Subject;
  alarma *alarma1 = new alarma(*subject);
  alarma *alarma2 = new alarma(*subject);
  alarma *alarma3 = new alarma(*subject);
  alarma *alarma4;
  alarma *alarma5;
  subject->CreateMessage("Hello World! :D");
  alarma3->RemoveMeFromTheList();
  subject->CreateMessage("The weather is hot today! :p");
  alarma4 = new alarma(*subject);
  alarma2->RemoveMeFromTheList();
  alarma5 = new alarma(*subject);
  subject->CreateMessage("My new car is great! ;)");
  alarma5->RemoveMeFromTheList();
  alarma4->RemoveMeFromTheList();
  alarma1->RemoveMeFromTheList();
  delete alarma5;
  delete alarma4;
  delete alarma3;
  delete alarma2;
  delete alarma1;
  delete subject;
}
int main() {
  ClientCode();
  return 0;
}
