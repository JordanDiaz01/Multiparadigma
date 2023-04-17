class Vendedor:
    def __init__(self, idvendedor=None, nombre=None, ciudad=None):
        self.__idvendedor = idvendedor
        self.__nombre = nombre
        self.__ciudad = ciudad

    @property
    def idvendedor(self):
        return self.__idvendedor

    @idvendedor.setter
    def idvendedor(self, idvendedor):
        self.__idvendedor = idvendedor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def ciudad(self):
        return self.__ciudad

    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad = ciudad

    def __str__(self):
        return f"ID Vendedor: {self.__idvendedor}, Nombre: {self.__nombre}, Ciudad: {self.__ciudad}"
