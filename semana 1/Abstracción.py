# Vamos a crear una clase para representar un dispositivo electrónico

class Dispositivo:
    def encender(self):
        print("El dispositivo se está encendiendo...")

# Ahora creamos una clase que representa un teléfono que es un dispositivo
class Telefono(Dispositivo):
    def encender(self):
        print("El teléfono está encendido.")

# Usamos las clases
mi_telefono = Telefono()
mi_telefono.encender()  # Muestra el mensaje del teléfono
