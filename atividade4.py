from abc import ABC, abstractmethod
import random

# ---------------------------
# Classe base abstrata
# ---------------------------
class AutomationDevice(ABC):
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, value):
        pass

    @abstractmethod
    def status(self):
        pass

# ---------------------------
# Sensor
# ---------------------------
class Sensor(AutomationDevice):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self._value = 0.0

    def read(self):
        self._value = random.uniform(20.0, 30.0)  # valor aleatório
        return self._value

    def write(self, value):
        # Sensor não faz nada ao escrever
        pass

    def status(self):
        print(f"Sensor {self._id} ({self._name}) | Valor: {self._value:.2f}")

# ---------------------------
# Actuator
# ---------------------------
class Actuator(AutomationDevice):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self._state = 0.0

    def read(self):
