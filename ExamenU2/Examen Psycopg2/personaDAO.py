from persona import Persona
from cursor import CursorDelPool
from logger_base import log


class personaDAO():
     _SELECCIONAR =  'select * from persona'
     _INSERTAR =  'insert into persona(id, nombre,correo,edad) VALUES (%s,%s,%s,%s)'
     _ACTUALIZAR = 'update persona set nombre= %s, correo = %s, edad = %s where id = %s'
     _ELIMINAR = 'delete from clientes where persona = %s'
     _obtenerContratosFecha = ''

     @classmethod
     def seleccionar(cls):
          with CursorDelPool() as cursor:
               cursor.execute(cls._SELECCIONAR)
               registros = cursor.fetchall()
               persona = []
               for r in registros:
                    persona = Persona(r[0],r[1],r[2])
                    persona.append(Persona)
               return persona
     @classmethod
     def insertar(cls,persona):
          with CursorDelPool() as cursor:
               valores =(persona.id,persona.nombre,persona.correo,persona.edad)
               cursor.execute(cls._INSERTAR,valores)
               return cursor.rowcount
     
     @classmethod
     def actualizar(cls,persona):
          with CursorDelPool() as cursor:
               valores =(persona.nombre,persona.correo,persona.edad,persona.id)
               cursor.execute(cls._ACTUALIZAR,valores)
               return cursor.rowcount
     @classmethod
     def eliminar(cls,persona):
          with CursorDelPool() as cursor:
               valores =(persona.id)
               cursor.execute(cls._ELIMINAR,valores)
               return cursor.rowcount
          
if __name__ == '__main__':
        #seleccionar
        personas_select = personaDAO.seleccionar()
        for p in personas_select:
             log.debug(p)

     #     #insertar
        persona1 = Persona(id=1,nombre='JordanDiaz',correo='jordanDIaz@gmail.com', edad=18)
        clientesinserts = personaDAO.insertar(persona1)
        log.debug(f'cliente insertado: {clientesinserts}')

     #    #editar
        persona2 = Persona(id='1',nombre='JordanEditado',edad=22,correo='jordanDiaz@hotmail.com')
        clienteupdate = personaDAO.actualizar(persona2)
        log.debug(f'persona actualizada: {clienteupdate}')

        #eliminar
    #    clienteDelete = personaDAO.eliminar(persona2)
        #log.debug(f'persona eliminada: {clienteDelete}')
