from logger_base import log
from conexion2 import Conexion

class CursorDelPool:
    def __init__(self) -> None:
        self._conexion =  None
        self._cursor = None
    
    def _enter_(self):
        log.debug('Entra with')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
    
    def exit(self,tipoExcepcion,mensajeExcepcion,detalleExcepcion):
        log.debug("sale with")
        if mensajeExcepcion:
            log.error("error",mensajeExcepcion)
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.LiberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as  cursor:
        cursor.execute('select* from persona')
    