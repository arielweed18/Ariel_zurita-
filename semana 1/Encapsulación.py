# Clase para manejar la información de un estudiante
class futbolista :
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # atributo privado con '__'


    def obtener_edad(self):
        return self.__edad

    # Método para cambiar la edad (setter)
    def cambiar_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad inválida")

# Usamos la clase
futbolista1 = futbolista("Leo Messi", 37)
print(futbolista1.nombre)  # Acceso directo
print(futbolista1.obtener_edad())  # Acceso indirecto a la edad privada

futbolista1.cambiar_edad(37)  # Cambiamos edad
print(futbolista1.obtener_edad())
