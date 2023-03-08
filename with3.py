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
            query = 'delete from cliente where idCliente = %s'
            valores = ('1')
            cursor.execute(query,valores)
            registrosinsert = cursor.rowcount
            log.debug(f'registros eliminados: {registrosinsert}')
except Exception as e:
    log.error(e)
finally: conn.close()