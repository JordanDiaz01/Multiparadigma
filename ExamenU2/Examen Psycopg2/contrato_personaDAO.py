from contrato_personaDAO import contrato_persona
from cursor import CursorDelPool
from logger_base import log


class contrato_personaDAO():
     _INSERTAR =  'insert into contrato(noContrato,Costo, fechaInicio, fechaFin) VALUES (%s,%s,%s,%s)'
     _ELIMINAR = 'delete from contrato where id = %s'

     @classmethod
     def seleccionar(cls):
          with CursorDelPool() as cursor:
               cursor.execute(cls._SELECCIONAR)
               registros = cursor.fetchall()
               contratos_personas = []
               for r in registros:
                    contratos_personas = contrato_persona(r[0],r[1],r[2])
                    contratos_personas.append(contrato_persona)
               return contratos_personas

     @classmethod
     def eliminar(cls,contrato):
          with CursorDelPool() as cursor:
               valores =(contrato.idPersona)
               cursor.execute(cls._ELIMINAR,valores)
               return cursor.rowcount
          
if __name__ == '__main__':

     #     #insertar
        contrato1 = contrato_persona()
        clientesinserts = contrato_persona.insertar(contrato1)
        log.debug(f'contrato insertado: {clientesinserts}')
        #eliminar
        clienteDelete = contrato_persona.eliminar(contrato1)
        log.debug(f'cliente eliminado: {clienteDelete}')
