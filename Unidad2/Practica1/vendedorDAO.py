from vendedor import Vendedor
from cursor import CursorDelPool
from logger_base import log


class VendedorDAO:
     _SELECCIONAR =  'select * from vendedores order by idvendedor'
     _INSERTAR =  'insert into vendedores(nombre,ciudad) VALUES (%s,%s)'
     _ACTUALIZAR = 'update vendedores set nombre= %s, ciudad = %s where idvendedor = %s'
     _ELIMINAR = 'delete from vendedores where idvendedor = %s'

     @classmethod
     def seleccionar(cls):
          with CursorDelPool() as cursor:
               cursor.execute(cls._SELECCIONAR)
               registros = cursor.fetchall()
               vendedores = []
               for r in registros:
                    vendedor = Vendedor(r[0],r[1],r[2])
                    vendedores.append(vendedor)
               return vendedores
     @classmethod
     def insertar(cls,vendedor):
          with CursorDelPool() as cursor:
               valores =(vendedor.nombre,vendedor.ciudad)
               cursor.execute(cls._INSERTAR,valores)
               return cursor.rowcount
     
     @classmethod
     def actualizar(cls,vendedor):
          with CursorDelPool() as cursor:
               valores =(vendedor.nombre,vendedor.ciudad,vendedor.idvendedor)
               cursor.execute(cls._ACTUALIZAR,valores)
               return cursor.rowcount
     @classmethod
     def eliminar(cls,vendedor):
          with CursorDelPool() as cursor:
               valores =(vendedor.idvendedor,)
               cursor.execute(cls._ELIMINAR,valores)
               return cursor.rowcount
          
if __name__ == '__main__':
        #seleccionar
        vendedores_select = VendedorDAO.seleccionar()
        for p in vendedores_select:
             log.debug(p)
             
         #insertar
        vendedor1 = Vendedor(nombre='Jordan',ciudad='NL')
        vendedoresinserts = VendedorDAO.insertar(vendedor1)
        log.debug(f'vendedor insertado: {vendedoresinserts}')
        vendedor3 = Vendedor(nombre='Rafael',ciudad='NL')
        vendedoresinserts = VendedorDAO.insertar(vendedor3)
        log.debug(f'vendedor insertado: {vendedoresinserts}')

        #editar
        vendedor2 = Vendedor(idvendedor='15',nombre='jordaneditado',ciudad='NL')
        vendedorupdate = VendedorDAO.actualizar(vendedor2)
        log.debug(f'vendedor actualizado: {vendedorupdate}')

        #eliminar
        vendedor3 = Vendedor(idvendedor="16")
        vendedordelete = VendedorDAO.eliminar(vendedor3)
        log.debug(f'vendedor eliminado: {vendedordelete}')
