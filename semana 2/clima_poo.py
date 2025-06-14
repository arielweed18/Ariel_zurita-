class RegistroClima:
    def __init__(self):
        self._temperaturas = []  # Encapsulamiento con atributo protegido

    def ingresar_temperaturas(self):
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self._temperaturas.append(temp)

    def calcular_promedio(self):
        if not self._temperaturas:
            return 0
        return sum(self._temperaturas) / len(self._temperaturas)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

# Clase hija para demostrar herencia
class ClimaExtendido(RegistroClima):

    def mayor_temperatura(self):
        if not self._temperaturas:
            return None
        return max(self._temperaturas)

# Función principal
def main():
    print("Promedio semanal del clima - Programación Orientada a Objetos")
    clima = ClimaExtendido()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()
    print(f"La temperatura más alta registrada fue: {clima.mayor_temperatura()} °C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
