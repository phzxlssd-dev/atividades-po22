#include <iostream>
#include <vector>
#include <memory>
#include <string>
using namespace std;


class AutomationDevice {
protected:
    int id;
    string name;

public:
    AutomationDevice(int idParam, string nameParam) {
        id = idParam;
        name = nameParam;
    }

    virtual void read() = 0;
    virtual void write(double value) = 0;
    virtual void display_status() const = 0;

    virtual ~AutomationDevice() {}
};


class Sensor : public AutomationDevice {
private:
    double value;

public:
    Sensor(int idParam, string nameParam) : AutomationDevice(idParam, nameParam) {
        value = 0.0;
    }

    void read() override {
        value += 1.0; 
    }

    void write(double val) override {
       
    }

    void display_status() const override {
        cout << "Sensor " << id << " (" << name << ") | Valor: " << value << endl;
    }
};


class Actuator : public AutomationDevice {
private:
    double state;

public:
    Actuator(int idParam, string nameParam) : AutomationDevice(idParam, nameParam) {
        state = 0.0;
    }

    void read() override {
       
    }

    void write(double val) override {
        state = val;
    }

    void display_status() const override {
        cout << "Actuator " << id << " (" << name << ") | Estado: " << state << endl;
    }
};

