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
        # sentencia = INSERT INTO recetas (nombre, tiempo, vegano) VALUES ('Pizza Napolitana', 15, 1)"
        # sentencia = "UPDATE recetas SET nombre = 'Pizza Muzzarella', tiempo = 50 WHERE idReceta = 13"
        # sentencia = "DELETE FROM recetas WHERE nombre = 'Pizza Muzzarella' AND tiempo = 50"
        sentencia = "INSERT INTO recetas (nombre, tiempo, vegano) VALUES ('Pizza Calabresa', 35, 0)"

        cursor.execute(sentencia)

        conexion.commit()  # Confirma la acción que estamos ejecutando

        print("Registro insertado con éxito")

        # Mostrar las filas
        sentencia = "SELECT * FROM recetas"
        cursor.execute(sentencia)
        registros = cursor.fetchall()

        for registro in registros:
            print(registro)

except Error as ex:
    print("Ha ocurrido un error en la conexión a la base de datos |", ex)

finally:

    if conexion.is_connected():
        conexion.close()
        print("")
        print("La conexión ha finalizado")
