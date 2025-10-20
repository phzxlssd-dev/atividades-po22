class PressureSensor:
    def __init__(self, id: int):
        self._id = id
        self._pressure = 0.0  # leitura inicial

    # Retorna a leitura atual
    def get_pressure(self) -> float:
        return self._pressure

    # Atualiza a leitura
    def set_pressure(self, value: float):
        self._pressure = value

    # Representação em string
    def __str__(self):
        return f"Sensor {self._id}: {self._pressure} Pa"


# ---------------------------
# Exemplo de uso
# ---------------------------
if __name__ == "__main__":
    sensor1 = PressureSensor(1)
    print(sensor1)  # Sensor 1: 0.0 Pa

    sensor1.set_pressure(101325.0)
    print(sensor1)  # Sensor 1: 101325.0 Pa

    print("Leitura atual:", sensor1.get_pressure())
