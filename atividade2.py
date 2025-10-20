class PneumaticActuator:
    def __init__(self, id: int):
        self._id = id
        self._position = 0.0  # posição inicial em %

    # Atualiza a posição com restrição 0–100%
    def set_position(self, value: float):
        if 0.0 <= value <= 100.0:
            self._position = value
        else:
            print(f"Valor inválido: {value}. Deve estar entre 0 e 100%.")

    # Retorna a posição atual
    def get_position(self) -> float:
        return self._position

    # Para o atuador (posição = 0)
    def stop(self):
        self._position = 0.0

    # Representação em string
    def __str__(self):
        return f"Atuador {self._id}: {self._position}%"


# ---------------------------
# Exemplo de uso
# ---------------------------
if __name__ == "__main__":
    actuator1 = PneumaticActuator(1)
    print(actuator1)  # Atuador 1: 0%

    actuator1.set_position(50.0)
    print(actuator1)  # Atuador 1: 50%

    actuator1.set_position(120.0)  # Valor inválido
    print(actuator1)

    actuator1.stop()
    print(actuator1)  # Atuador 1: 0%
