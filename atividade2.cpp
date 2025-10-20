#include <iostream>
#include <stdexcept>
using namespace std;

class Motor {
private:
    int id;
    double speed = 0.0;
    double max_speed = 0.0;

public:
    
    Motor(int startId, double maxSpeedParam) {
        id = startId;
        max_speed = maxSpeedParam;
        speed = 0.0;
    }

  
    void set_speed(double valor) {
        if (valor <= max_speed) {
            speed = valor;
        } else {
            throw runtime_error("Velocidade excede o limite de seguranca!");
        }
    }

   
    double get_speed() {
        return speed;
    }

    
    void stop() {
        speed = 0.0;
    }

   
    void display_info() {
        cout << "Motor " << id
             << " | Speed: " << speed
             << " / MaxSpeed: " << max_speed
             << endl;
    }
};
