class PIDController:
    def __init__(self, Kp: float, Ki: float, Kd: float):
        self._Kp = Kp
        self._Ki = Ki
        self._Kd = Kd

        self._setpoint = 0.0
        self._integral = 0.0
        self._last_error = 0.0

    # Define o setpoint desejado
    def set_setpoint(self, sp: float):
        self._setpoint = sp

    # Atualiza a medição e retorna saída PID
    def update(self, measurement: float) -> float:
        error = self._setpoint - measurement
        self._integral += error
        derivative = error - self._last_error
        self._last_error = error

        output = self._Kp * error + self._Ki * self._integral + self._Kd * derivative
        return output

    # Representação em string mostrando os ganhos
    def __str__(self):
        return f"PID Gains -> Kp: {self._Kp}, Ki: {self._Ki}, Kd: {self._Kd}"


# ---------------------------
# Exemplo de uso / simulação
# ---------------------------
if __name__ == "__main__":
    pid = PIDController(Kp=1.0, Ki=0.1, Kd=0.05)
    print(pid)

    temperatura = 20.0
    pid.set_setpoint(25.0)  # desejamos 25°C

    print("Simulação PID:")
    for i in range(5):
        sinal = pid.update(temperatura)
        print(f"Leitura: {temperatura:.2f} | Sinal de controle: {sinal:.2f}")

        # Simula efeito do controle na temperatura
        temperatura += sinal * 0.1  # fator de ganho fictício
