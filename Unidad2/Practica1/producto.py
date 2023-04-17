
class Producto:
    def __init__(self, idproducto  =None, nombre  =None, precio  =None):
        self.__idproducto = idproducto
        self.__nombre = nombre
        self.__precio = precio

    @property
    def idproducto(self):
        return self.__idproducto

    @idproducto.setter
    def idproducto(self, idproducto):
        self.__idproducto = idproducto

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID Producto: {self.__idproducto}, Nombre: {self.__nombre}, Precio: {self.__precio}"
