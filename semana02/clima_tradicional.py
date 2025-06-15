# Función para solicitar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de cada día de la semana:")
    for i in range(7):
        temp = float(input(f"Día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    datos_clima = ingresar_temperaturas()
    promedio = calcular_promedio(datos_clima)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
