import pymssql

# Conectamos con el servidor de SQL Server
conexion = pymssql.connect(
    charset="UTF-8",
    server="localhost",
    user="sa",
    password="MiContraseña",
    database="master",
    port=1433,
    as_dict=True
)

# Ejecutamos una consulta SQL de ejemplo que nos 
# devolverá el nombre de la base de datos a la que estamos conectados
sql = "select DB_NAME() as BD;"
cursor = conexion.cursor()
cursor.execute(sql)
# Recorremos todos los registros devueltos por la consulta SQL (en este caso solo uno)
# Y mostramos el campo "BD"
registros = cursor.fetchall()
for registro in registros:
    print(f"{registro["BD"]}")
    
# Cerramos la conexión con el servidor SQL Server
cursor.close
conexion.close