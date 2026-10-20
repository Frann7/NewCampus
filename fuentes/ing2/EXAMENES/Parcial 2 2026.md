# Parcial N°2 — Ingeniería del Software II — 14 de octubre de 2026

Fuente: `C:/Users/Fran/Desktop/SISTEMAS 3/ING 2/PARCIAL 2026/` (tres fotos de WhatsApp de la hoja
de un compañero) · transcripto a mano, sin el nombre ni el DNI de la hoja. Suma 100 puntos:
Práctica 60 (35 + 10 + 15) y Teoría 40 (10 cada pregunta).

## Práctica

1- Dado el siguiente código identificar cual es el patrón que se está implementando, mencionar
cuales fueron los elementos que te ayudaron a identificar el mismo y armar el diagrama en UML del
mismo. (35 puntos)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
class Graphic {
public:
    virtual ~Graphic() {}
    virtual void Move(int x, int y) = 0;
    virtual void Draw() const = 0; };
class Dot : public Graphic {
protected:
    int x_;
    int y_;
public:
    Dot(int x, int y) : x_(x), y_(y) {}
    void Move(int x, int y) override {
        x_ += x;
        y_ += y;      }
    void Draw() const override {
        std::cout << "Dibujando punto en ("
        << x_ << ", " << y_ << ")\n";     }};

class Circle : public Dot {
private:
    int radius_;
public:
    Circle(int x, int y, int radius)
      : Dot(x, y), radius_(radius) {}
    void Draw() const override {
        std::cout << "Dibujando circulo en ("
        << x_ << ", " << y_
        << ") con radio " << radius_ << "\n";
}};

class CompoundGraphic : public Graphic {
private:
    std::vector<Graphic*> children_;
public:
    void Add(Graphic* graphic) {
        children_.push_back(graphic);     }
    void Remove(Graphic* graphic) {
        auto it = std::find(
            children_.begin(),
            children_.end(),
            graphic          );
        if (it != children_.end()) {
            children_.erase(it);     }     }

    void Move(int x, int y) override {
        for (Graphic* graphic : children_) {
            graphic->Move(x, y);      }     }

    void Draw() const override {
        std::cout << "Dibujando grupo:\n";
        for (const Graphic* graphic : children_) {
            graphic->Draw();       }
        std::cout << "Fin del grupo\n";     }};

class ImageEditor {
private:
    CompoundGraphic* all_;
public:
    ImageEditor() : all_(nullptr) {}
    ~ImageEditor() {
        delete all_;     }
    void Load() {
        all_ = new CompoundGraphic();
        all_->Add(new Dot(1, 2));
        all_->Add(new Circle(5, 3, 10));
        std::cout << "Imagen cargada.\n";     }
    void DrawAll() {
        if (all_ != nullptr) {
            all_->Draw();     }     }

    void MoveAll(int x, int y) {
        if (all_ != nullptr) {
            all_->Move(x, y);     }     }};

int main() {
    ImageEditor editor;
    editor.Load();
    std::cout << "\nImagen original:\n";
    editor.DrawAll();
    std::cout << "\nMoviendo todos los elementos...\n";
    editor.MoveAll(10, 5);
    std::cout << "\nImagen después del movimiento:\n";
    editor.DrawAll();
    return 0;
}
```

2- Dado el siguiente enunciado identificar en qué nivel de madurez se encuentra la empresa y
explicar cómo se llevaría al siguiente nivel.

Una empresa de ciberseguridad dedicada al desarrollo de soluciones para la protección de sistemas y
redes cuenta con procesos de trabajo definidos y documentados que son utilizados por los diferentes
equipos de la organización. Para cada proyecto se establecen procedimientos, responsabilidades,
estándares y criterios de trabajo que sirven como guía para el desarrollo de las actividades.
Además, la empresa capacita a sus empleados en estos procedimientos y adapta las prácticas
generales de la organización a las necesidades particulares de cada proyecto, manteniendo una
metodología común para gestionar el desarrollo, las pruebas y la implementación de sus soluciones
de seguridad.

Antes de comenzar cada proyecto, los equipos utilizan las prácticas establecidas por la
organización para planificar las actividades y definir la forma en que se llevarán a cabo. Aunque
cada proyecto puede presentar diferentes necesidades o requerimientos de seguridad, los equipos
parten de una metodología común y realizan las adaptaciones necesarias sin dejar de seguir los
lineamientos generales establecidos. La empresa también mantiene documentación sobre sus procesos
y proporciona herramientas y conocimientos compartidos para que los distintos equipos puedan
desarrollar sus actividades de manera consistente. (10 puntos)

3- Defina métricas y describa cada uno de los elementos que la componen. (15 puntos)

## Teoría

10 puntos cada pregunta

1. Realice un cuadro comparativo entre Process Improvement (PI) y Software Process Improvement
   (SPI) que contemple objetivo, ámbito de aplicación y un ejemplo concreto.
2. Realice un Diagrama de ciclo del ciclo de vida de una métrica.
3. Represente la estructura de un patrón Strategy. Defina su propósito.
4. Represente gráficamente la arquitectura de control de versiones de **SVN y Git**, indicando los
   servidores centrales, los repositorios y la ubicación de las copias de trabajo de los
   desarrolladores en cada caso.
