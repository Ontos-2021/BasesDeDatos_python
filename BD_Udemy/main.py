import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="master_python"
)

# ¿La conexión ha sido correcta?
# print(database)


# Cursor
cursor = database.cursor()


# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS VEHICULOS(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
