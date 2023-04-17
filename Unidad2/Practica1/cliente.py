class Cliente:
    def __init__(self, idcliente=None, nombre=None, direccion=None):
        self.__idcliente = idcliente
        self.__nombre = nombre
        self.__direccion = direccion

    @property
    def idcliente(self):
        return self.__idcliente

    @idcliente.setter
    def idcliente(self, idcliente):
        self.__idcliente = idcliente

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    def __str__(self):
        return f"ID Cliente: {self.__idcliente}, Nombre: {self.__nombre}, Dirección: {self.__direccion}"
