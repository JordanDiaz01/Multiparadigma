from contrato import Contrato
from cursor import CursorDelPool
from logger_base import log


class contratoDAO():
     _SELECCIONAR =  'select * from contrato'
     _INSERTAR =  'insert into contrato(id, nocontrato,costo, fechainicio, fechafin) VALUES (%s,%s,%s,%s,%s)'
     _ACTUALIZAR = 'update contrato set nocontrato= %s, costo = %s, fechainicio = %s,fechafin = %s where id = %s'
     _ELIMINAR = 'delete from contrato where id = %s'

     @classmethod
     def seleccionar(cls):
          with CursorDelPool() as cursor:
               cursor.execute(cls._SELECCIONAR)
               registros = cursor.fetchall()
               contratos = []
               for r in registros:
                    contratos = Contrato(r[0],r[1],r[2])
                    contratos.append(Contrato)
               return contratos
     @classmethod
     def insertar(cls,contrato):
          with CursorDelPool() as cursor:
               valores =(contrato.id,contrato.noContrato,contrato.Costo,contrato.fechaInicio,contrato.fechaFin)
               cursor.execute(cls._INSERTAR,valores)
               return cursor.rowcount
     
     @classmethod
     def actualizar(cls,contrato):
          with CursorDelPool() as cursor:
               valores =(contrato.noContrato,contrato.Costo,contrato.fechaInicio,contrato.fechaFin,contrato.id)
               cursor.execute(cls._ACTUALIZAR,valores)
               return cursor.rowcount
     @classmethod
     def eliminar(cls,contrato):
          with CursorDelPool() as cursor:
               valores =(contrato.id)
               cursor.execute(cls._ELIMINAR,valores)
               return cursor.rowcount
          
if __name__ == '__main__':
        #seleccionar
        personas_select = contratoDAO.seleccionar()
        for p in personas_select:
             log.debug(p)

     #     #insertar
        contrato1 = Contrato(id=1,noContrato=11231230,Costo=500, fechaInicio='2023/04/05', fechaFin='2024/05/05')
        clientesinserts = contratoDAO.insertar(contrato1)
        log.debug(f'contrato insertado: {clientesinserts}')

     #    #editar
        contrato2 = Contrato(id='1',noContrato=11231230,Costo=1000, fechaInicio="2023/04/05", fechaFin="2024/05/05")
        clienteupdate = contratoDAO.actualizar(contrato2)
        log.debug(f'cliente actualizado: {clienteupdate}')

        #eliminar
      #  clienteDelete = contratoDAO.eliminar(contrato2)
      #  log.debug(f'cliente eliminado: {clienteDelete}')
