class Contrato:
    def __init__(self, id=None, noContrato=None,Costo=None, fechaInicio=None,fechaFin=None):
        self.__id = id
        self.__noContrato = noContrato
        self.__Costo = Costo
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def noContrato(self):
        return self.__noContrato

    @noContrato.setter
    def noContrato(self, noContrato):
        self.__noContrato = noContrato

    @property
    def Costo(self):
        return self.__Costo

    @Costo.setter
    def Costo(self, Costo):
        self.__Costo = Costo
        
    @property
    def fechaInicio(self):
        return self.__fechaInicio
    @fechaInicio.setter
    def fechaInicio(self, fechaInicio):
        self.__fechaInicio = fechaInicio
        
    @property
    def fechaFin(self):
        return self.__fechaFin
    @fechaFin.setter
    def fechaFin(self, fechaFin):
        self.__fechaFin = fechaFin

    def __str__(self):
        return f"ID contrato: {self.__id}, no.Contrato: {self.__noContrato}, costo: {self.__Costo}, Fecha inicio: {self.__fechaInicio}, Fecha final: {self.fechaFin}"
