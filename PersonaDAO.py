from Persona import Persona 
from cursor import CursorDelPool
from logger_base import log

class PersonaDAO:
    _SELECCIONAR =  'select from persona order by idpersona'
    _INSERTAR =  'insert into persona(nombre,apellido,email,edad) VALUES (%s,%s,%s,%s)'
    _ACTUALIZAR = 'update persona set nombre= %s, apellido = %s, email = %s,edad = %s'
    _ELIMINAR = 'delete from persona where idpersona = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for r in registros:
                persona = Persona(r(0),r(1),r(2),r(3),r(4))
                personas.append(persona)
            return personas
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores =(persona.Nombre,persona.Apellido,persona.Email,persona.Edad)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores =(persona.Nombre,persona.Apellido,persona.Email,persona.Edad,persona.IdPerson)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
            valores =(persona.IdPerson)
            cursor.execute(cls._Eliminar,valores)
            return cursor.rowcount
        
if __name__ == '__main__':
        #insertar
        persona1 = Persona(nombre= 'Pedro',apellido = 'Pascal',email = 'pascal@gmail.com',edad=20)
        persona2 = Persona(nombre= 'Jordan',apellido = 'Diaz',email = 'jordan@gmail.com',edad=20)
        personasInsertadas = PersonaDAO.insertar(persona1)
        log.debug(f'Peronsas')
        personas = PersonaDAO.seleccionar
        