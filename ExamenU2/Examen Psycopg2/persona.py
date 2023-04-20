class Persona:
    def __init__(self, id=None, nombre=None,edad=None, correo=None):
        self.__id = id
        self.__nombre = nombre
        self.__correo = correo
        self.__edad = edad

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def direccion(self, correo):
        self.__correo = correo
        
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f"ID persona: {self.__id}, Nombre: {self.__nombre}, Correo: {self.__correo}, Edad: {self.edad}"
