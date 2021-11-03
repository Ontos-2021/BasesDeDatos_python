import mysql.connector

from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='recetapp'
    )

    if conexion.is_connected():
        print("Conexión exitosa.")
        print("")

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO recetas (nombre, tiempo, vegano) VALUES ('Pizza Napolitana', 15, 1);")

        conexion.commit() # Confirma la acción que estamos ejecutando

        print("Registro insertado con éxito")

except Error as ex:
    print("Ha ocurrido un error en la conexión a la base de datos |", ex)

finally:

    if conexion.is_connected():
        conexion.close()
        print("")
        print("La conexión ha finalizado")
