from cliente import Cliente
from cursor import CursorDelPool
from logger_base import log


class ClienteDAO():
     _SELECCIONAR =  'select * from clientes order by idcliente'
     _INSERTAR =  'insert into clientes(nombre,direccion) VALUES (%s,%s)'
     _ACTUALIZAR = 'update clientes set nombre= %s, direccion = %s where idcliente = %s'
     _ELIMINAR = 'delete from clientes where idcliente = %s'

     @classmethod
     def seleccionar(cls):
          with CursorDelPool() as cursor:
               cursor.execute(cls._SELECCIONAR)
               registros = cursor.fetchall()
               clientes = []
               for r in registros:
                    cliente = Cliente(r[0],r[1],r[2])
                    clientes.append(cliente)
               return clientes
     @classmethod
     def insertar(cls,cliente):
          with CursorDelPool() as cursor:
               valores =(cliente.nombre,cliente.direccion)
               cursor.execute(cls._INSERTAR,valores)
               return cursor.rowcount
     
     @classmethod
     def actualizar(cls,cliente):
          with CursorDelPool() as cursor:
               valores =(cliente.nombre,cliente.direccion,cliente.idcliente)
               cursor.execute(cls._ACTUALIZAR,valores)
               return cursor.rowcount
     @classmethod
     def eliminar(cls,cliente):
          with CursorDelPool() as cursor:
               valores =(cliente.idcliente)
               cursor.execute(cls._ELIMINAR,valores)
               return cursor.rowcount
          
if __name__ == '__main__':
        #seleccionar
        clientes_select = ClienteDAO.seleccionar()
        for p in clientes_select:
             log.debug(p)

     #     #insertar
        cliente1 = Cliente(nombre='Jafet',direccion='Arecas')
        clientesinserts = ClienteDAO.insertar(cliente1)
        log.debug(f'cliente insertado: {clientesinserts}')

     #    #editar
        cliente3 = Cliente(idcliente='7',nombre='Jafeteditado',direccion='Arecas')
        clienteupdate = ClienteDAO.actualizar(cliente3)
        log.debug(f'cliente actualizado: {clienteupdate}')

        #eliminar
        clienteDelete = ClienteDAO.eliminar(cliente3)
        log.debug(f'cliente eliminado: {clienteDelete}')
