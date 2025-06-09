# Clase base que representa un vehículo
class Vehiculo:
    def mostrar_tipo(self):
        print("Este es un vehículo")

# Clase que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def mostrar_tipo(self):
        print("Esta es una bicicleta")

# Usamos las clases
vehiculo = Vehiculo()
vehiculo.mostrar_tipo()

bici = Bicicleta()
bici.mostrar_tipo()
