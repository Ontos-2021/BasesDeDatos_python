import mysql.connector

from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='world'
    )

    if conexion.is_connected():
        print("Conexión exitosa.")
        infoserver = conexion.get_server_info()
        print(f"Información del servidor: {infoserver}")
        cursor = conexion.cursor()
        cursor.execute("SELECT database();")
        registro = cursor.fetchone()
        print(f"Conectado a la base de datos: {registro}")

        cursor.execute("SELECT * FROM city WHERE CountryCode = 'ARG'")
        resultados = cursor.fetchall()

        for fila in resultados:
            # print(fila[1] + " - " + fila[2])
            print(f"Registro: {fila}")
        print(f"Total de registros: {cursor.rowcount}")

except Error as ex:
    print("Ha ocurrido un error en la conexión a la base de datos |", ex)

finally:

    if conexion.is_connected():
        conexion.close()
        print("La conexión ha finalizado")
