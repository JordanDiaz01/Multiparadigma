#coloca un bloque y te lo cierra
import psycopg2
from logger_base import log

conn = psycopg2.connect(
    user = 'postgres',
    password = '1234',
    host = '127.0.0.1',
    port = 5432,
    database = 'clase_db'
)

log.debug(conn)

#with son como bloques de un if o trycatch

try:
    with conn:
        with conn.cursor() as cursor:
            query = 'insert into cliente(nombre,apellido,email) values (%s,%s,%s)'
            valores = (('Juan','Perez','juan@gmail.com'),('jordan','diaz','jordadiaz@gmail.com'))
            cursor.executemany(query,valores)
            registrosinsert = cursor.rowcount
            log.debug(f'registros insertados: {registrosinsert}')
except Exception as e:
    log.error(e)
finally: conn.close()

