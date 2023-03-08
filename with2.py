
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
            query = 'UPDATE cliente SET nombre=%s, apellido = %s, email = %s WHERE idCliente = %s'
            valores = (('Pedro','Pascal','pedro@gmail.com',1),('Joel','Sanchez','joel@gmail.com',2))
            cursor.executemany(query,valores)
            registrosinsert = cursor.rowcount
            log.debug(f'registros actualizados: {registrosinsert}')
except Exception as e:
    log.error(e)
finally: conn.close()