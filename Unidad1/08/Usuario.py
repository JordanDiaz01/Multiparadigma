
class Usuario:
    def __init__(self, usuario, contrasena, nombre, curp, ciudad, rol='cliente') -> None:
        self._usuario = usuario
        self._contrasena = contrasena
        self._rol = rol
        self._nombre = nombre
        self._curp = curp
        self._ciudad = ciudad

    # Getters
    @property
    def getUsuario(self):
        return self._usuario
    @property
    def getContrasena(self):
        return self._contrasena
    @property
    def getRol(self):
        return self._rol
    @property
    def getNombre(self):
        return self._nombre
    @property
    def getCurp(self):
        return self._curp
    @property
    def getCiudad(self):
        return self._ciudad

    # Setters
    @getUsuario.setter
    def setUsuario(self, usuario):
        self._usuario = usuario
    @getContrasena.setter
    def setContrasena(self, contrasena):
        self._contrasena = contrasena
    @getRol.setter
    def setRol(self, rol):
        self._rol = rol
    @getNombre.setter
    def setNombre(self, nombre):
        self._nombre = nombre
    @getCurp.setter
    def setCurp(self, curp):
        self._curp = curp
    @getCiudad.setter
    def setCiudad(self, ciudad):
        self._ciudad = ciudad

    def __str__(self) -> str:
        return f"Usuario:{self._usuario}\nContraseña:{self._contrasena}\n Rol:{self._rol}\n Nombre:{self._nombre}\n CURP:{self._curp}\n Ciudad:{self._ciudad}"
