import mysql.connector

from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='test'
    )

    if conexion.is_connected():
        print("Conexión exitosa.")
except Error as ex:
    print("Ha ocurrido un error en la conexión a la base de datos |", ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexión ha finalizado")
