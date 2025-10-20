#include <iostream>
using namespace std;

class PIDController {
private:
    double Kp;
    double Ki;
    double Kd;

    double setpoint = 0.0;
    double measurement = 0.0;
    double integral = 0.0;
    double previous_error = 0.0;

public:
    // Construtor
    PIDController(double Kp_param, double Ki_param, double Kd_param) {
        Kp = Kp_param;
        Ki = Ki_param;
        Kd = Kd_param;
        integral = 0.0;
        previous_error = 0.0;
    }

    // Define o setpoint desejado
    void set_setpoint(double sp) {
        setpoint = sp;
    }


    void update_measurement(double value) {
        measurement = value;
    }


    double compute_output() {
        double error = setpoint - measurement;
        integral += error;                      // erro acumulado
        double derivative = error - previous_error; // derivada
        previous_error = error;

        double output = Kp * error + Ki * integral + Kd * derivative;
        return output;
    }

    
    void display_gains() {
        cout << "Kp: " << Kp
             << " | Ki: " << Ki
             << " | Kd: " << Kd << endl;
    }
};

// Exemplo de uso no main
int main() {
    PIDController pid(1.0, 0.1, 0.05);  
    pid.display_gains();

    double temperatura = 20.0;
    pid.set_setpoint(25.0);             

    for (int i = 0; i < 5; i++) {
        pid.update_measurement(temperatura);

        double sinal = pid.compute_output();
        cout << "Leitura: " << temperatura << " | Sinal de controle: " << sinal << endl;

        
        temperatura += sinal * 0.1; }
