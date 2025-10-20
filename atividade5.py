from abc import ABC, abstractmethod

# ---------------------------
# Interface de comunicação
# ---------------------------
class CommunicationInterface(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self) -> str:
        pass

# ---------------------------
# Modbus
# ---------------------------
class ModbusInterface(CommunicationInterface):
    def __init__(self):
        self._last_message = ""

    def send(self, message: str):
        self._last_message = message
        print(f"[Modbus] Enviando: {message}")

    def receive(self) -> str:
        print("[Modbus] Recebendo mensagem")
        return self._last_message + "_reply"

# ---------------------------
# CAN
# ---------------------------
class CANInterface(CommunicationInterface):
    def __init__(self):
        self._last_message = ""

    def send(self, message: str):
        self._last_message = message
        print(f"[CAN] Enviando: {message}")

    def receive(self) -> str:
        print("[CAN] Recebendo mensagem")
        return self._last_message + "_reply"

# ---------------------------
# MQTT
# ---------------------------
class MQTTInterface(CommunicationInterface):
    def __init__(self):
        self._last_message = ""

    def send(self, message: str):
        self._last_message = message
        print(f"[MQTT] Enviando: {message}")

    def receive(self) -> str:
        print("[MQTT] Recebendo mensagem")
        return self._last_message + "_reply"

# ---------------------------
# Função fábrica
# ---------------------------
def create_interface(type: str) -> CommunicationInterface:
    if type == "Modbus":
        return ModbusInterface()
    elif type == "CAN":
        return CANInterface()
    elif type == "MQTT":
        return MQTTInterface()
    else:
        raise ValueError(f"Tipo de interface desconhecido: {type}")

# ---------------------------
# Teste
# ---------------------------
if __name__ == "__main__":
    interfaces = [
        create_interface("Modbus"),
        create_interface("CAN"),
        create_interface("MQTT")
    ]

    messages = ["Hello Modbus", "Hello CAN", "Hello MQTT"]

    for iface, msg in zip(interfaces, messages):
        iface.send(msg)
        reply = iface.receive()
        print(f"Resposta: {reply}\n")
