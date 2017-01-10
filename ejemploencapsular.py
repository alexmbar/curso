from abc import ABCMeta, abstractmethod
class Persona:
    __metaclass__ = ABCMeta


class Deportista(Persona):

    def __init__(self, edad, nombre);
        self.edad = edad
        self.nombre = nombre
            print "Se ha creado a", self.nombre, " de ", self.edad
    @abstractmethod
    def hablar(self):

class Deportista(Persona):

    def __init__(self,edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.__deporte = deporte
            print "Se ha creado a", self.nombre, " de ", self.edad

    def practicarDeporte(self):
        print self.nombre ": voy a practicar"

    def verMiDeporte(self):
        return self.__deporte


juan = Persona(30,"Juan")
juan.hablar("Hola,estoy hablando","Este soy yo")
luis = Deportista(18,"Luis","natacion")
luis.hablar("Hola,estoy hablando","Este soy yo")
luis.practicarDeporte()
print "Luis practica", luis.verMiDeporte()