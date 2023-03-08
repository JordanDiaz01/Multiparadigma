import psycopg2
from logger_base import log 

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = 5432,
    database = 'clase_db'
)

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    query = 'INSERT INTO cliente(nombre) VALUES(%s)'
    nombre = 'Juan'
    valores = (nombre,)
    cursor.execute(query,valores)
    log.debug('insert')
    query = 'UPDATE cliente SET nombre=%s WHERE idCliente = %s'
    valores = ('juan','5')
    cursor.execute(query,valores)
    log.debug('update')
    conexion.commit()
except Exception as e:
    conexion.rollback()
    log.error(e)
