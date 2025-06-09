class Persona:
    def presentarse(self):
        print("Hola, soy una persona")

class Profesor(Persona):
    def presentarse(self):
        print("Hola, soy un profesor")

class Alumno(Persona):
    def presentarse(self):
        print("Hola, soy un alumno")

def saludar(persona):
    persona.presentarse()

# Uso
profesor = Profesor()
alumno = Alumno()

saludar(profesor)  # "Hola, soy un profesor"
saludar(alumno)    # "Hola, soy un alumno"
