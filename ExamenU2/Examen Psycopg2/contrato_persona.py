class contrato_Persona:
    def __init__(self, idPersona=None, idContrato=None):
        self.__idPersona = idPersona
        self.__idContrato = idContrato
    @property
    def idPersona(self):
        return self.__idPersona

    @idPersona.setter
    def idPersona(self, idPersona):
        self.__idPersona = idPersona
        
    @property
    def idContrato(self):
        return self.__idContrato

    @idContrato.setter
    def __idContrato(self, idContrato):
        self.__idContrato = idContrato
        
    def __str__(self):
        return f"ID contrato: {self.__idContrato}, idPersona: {self.__idPersona}"
