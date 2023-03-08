from logger_base import log

class Persona:
    def init(self,idPersona = None, Nombre= None, Apellido = None,Email=None, Edad=None) -> None:
        self._idPersona = idPersona
        self._Nombre = Nombre
        self._Apellido = Apellido
        self._Email = Email
        self._Edad = Edad

    def str(self) -> str:
        return f"""
                Id Persona: {self._idPersona}
                Nombre: {self._Nombre}
                Apellido: {self._Apellido}
                Email: {self._Email}
                Edad: {self._Edad}
                """
    @property
    def idPerson(self):
        return self._idPersona
    @idPerson.setter
    def idPerson(self,idPersona):
        self._idPersona=idPersona

    @property
    def Nombre(self):
        return self._idPersona
    @idPerson.setter
    def idPerson(self,idPersona):
        self._idPersona=idPersona

    @property
    def Apellido(self):
        return self._Apellido
    @Apellido.setter
    def Apellido(self,Apellido):
        self._Apellido= Apellido

    @property
    def Apellido(self):
        return self._Apellido
    @Apellido.setter
    def Apellido(self,Apellido):
        self._Apellido= Apellido
    @property
    def Email(self):
        return self._Email
    @Email.setter
    def Email(self,Email):
        self._Email=Email

    @property
    def Edad(self):
        return self._Edad
    @Edad.setter
    def Edad(self,Edad):
        self._Edad=Edad