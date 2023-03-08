import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = '1234',
    host = '127.0.0.1',
    port = 5432,
    database = 'clase_db'
)

print(conexion)
cursor = conexion.cursor()
cursor.execute('select nombre from cliente')
resultados = cursor.fetchone()
print(resultados)