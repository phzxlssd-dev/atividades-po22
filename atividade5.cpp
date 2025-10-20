#include <iostream>
#include <string>
#include <memory>
using namespace std;

class CommunicationInterface {
public:
    virtual void send(string message) = 0;
    virtual string receive() = 0;
    virtual ~CommunicationInterface() {}
};

class ModbusInterface : public CommunicationInterface {
private:
    string lastMessage;

public:
    ModbusInterface() {
        lastMessage = "";
    }

    void send(string message) override {
        lastMessage = message;
        cout << "[Modbus] Enviando: " << message << endl;
    }

    string receive() override {
        cout << "[Modbus] Recebendo mensagem" << endl;
        return lastMessage + "_reply";
    }
};

class CANInterface : public CommunicationInterface {
private:
    string lastMessage;

public:
    CANInterface() {
        lastMessage = "";
    }

    void send(string message) override {
        lastMessage = message;
        cout << "[CAN] Enviando: " << message << endl;
    }

    string receive() override {
        cout << "[CAN] Recebendo mensagem" << endl;
        return lastMessage + "_reply";
    }
};

class MQTTInterface : public CommunicationInterface {
private:
    string lastMessage;

public:
    MQTTInterface() {
        lastMessage = "";
    }

    void send(string message) override {
        lastMessage = message;
        cout << "[MQTT] Enviando: " << message << endl;
    }

    string receive() override {
        cout << "[MQTT] Recebendo mensagem" << endl;
        return lastMessage + "_reply";
    }
};


unique_ptr<CommunicationInterface> create_interface(string type) {
    if (type == "Modbus") {
        return make_unique<ModbusInterface>();
    } else if (type == "CAN") {
        return make_unique<CANInterface>();
    } else if (type == "MQTT") {
        return make_unique<MQTTInterface>();
    } else {
        return nullptr;
    }
}


int main() {
    auto iface1 = create_interface("Modbus");
    auto iface2 = create_interface("CAN");
    auto iface3 = create_interface("MQTT");

    iface1->send("Hello Modbus");
    cout << "Resposta: " << iface1->receive() << endl;

    iface2->send("Hello CAN");
    cout << "Resposta: " << iface2->receive() << endl;

    iface3->send("Hello MQTT");
    cout << "Resposta: " << iface3->receive() << endl;

    return 0;
}
