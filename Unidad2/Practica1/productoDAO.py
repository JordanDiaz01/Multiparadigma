from producto import Producto
from cursor import CursorDelPool
from logger_base import log


class ProductoDAO:
     _SELECCIONAR =  'select * from productos order by idproducto'
     _INSERTAR =  'insert into productos(nombre,precio) VALUES (%s,%s)'
     _ACTUALIZAR = 'update productos set nombre= %s, precio = %s where idproducto = %s'
     _ELIMINAR = 'delete from productos where idproducto = %s'

     @classmethod
     def seleccionar(cls):
          with CursorDelPool() as cursor:
               cursor.execute(cls._SELECCIONAR)
               registros = cursor.fetchall()
               productos = []
               for r in registros:
                    producto = Producto(r[0],r[1],r[2])
                    productos.append(producto)
               return productos
     @classmethod
     def insertar(cls,producto):
          with CursorDelPool() as cursor:
               valores =(producto.nombre,producto.precio)
               cursor.execute(cls._INSERTAR,valores)
               return cursor.rowcount
     
     @classmethod
     def actualizar(cls,producto):
          with CursorDelPool() as cursor:
               valores =(producto.nombre,producto.precio,producto.idproducto)
               cursor.execute(cls._ACTUALIZAR,valores)
               return cursor.rowcount
     @classmethod
     def eliminar(cls,producto):
          with CursorDelPool() as cursor:
               valores =(producto.idproducto)
               cursor.execute(cls._ELIMINAR,valores)
               return cursor.rowcount
          
if __name__ == '__main__':
        #seleccionar
        productos_select = ProductoDAO.seleccionar()
        for p in productos_select:
             log.debug(p)
             
         #insertar
        producto1 = Producto(nombre='figura1',precio='500')
        productosinserts = ProductoDAO.insertar(producto1)
        log.debug(f'producto insertado: {productosinserts}')
        producto3 = Producto(nombre='figura2',precio='300')
        productosinserts = ProductoDAO.insertar(producto3)
        log.debug(f'producto insertado: {productosinserts}')

        #editar
        producto2 = Producto(idproducto='4',nombre='figuraeditada',precio='100')
        vendedorupdate = ProductoDAO.actualizar(producto2)
        log.debug(f'producto actualizado: {vendedorupdate}')

     #    #eliminar
        producto3 = Producto(idproducto='6',nombre='figura2',precio='300')
        vendedordelete = ProductoDAO.eliminar(producto3)
        log.debug(f'producto eliminado: {vendedordelete}')
