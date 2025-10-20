 #include <iostream>
#include <stdexcept>
#include <iomanip>
using namespace std;

class TemperatureSensor {
private:
    int id;
    double temperature = 0.0;

public:
    TemperatureSensor(int idStart, double temperaturestart = 0.0) {
        id = idStart;
        temperature = temperaturestart;
    }

    double gettemperature() {
        return temperature;
    }

    void set_temperature(double valor) {   // corrigido: tipo de retorno void
        temperature = valor;
    }

    void display_info() {                  // corrigido: cout estava invertido
        cout << "idstart " << id
             << " temperaturestart " << temperature
             << " valor" << endl;
    }
};
