import sqlite3


# Definir conección y el cursor
def main():
    connection = sqlite3.connect('BaseDeDatos.db')
    cursor = connection.cursor()

    comando = """
    CREATE TABLE IF NOT EXISTS
    stores(id_store INTEGER PRIMARY KEY, location TEXT)
    """
    cursor.execute(comando)

    comando = """
    CREATE TABLE IF NOT EXISTS
    purchases(id_purchase INTEGER PRIMARY KEY, id_store INTEGER, total_cost FLOAT,
    FOREIGN KEY(id_store) REFERENCES stores(id_store))
    """

    cursor.execute(comando)

    # Agregar tiendas

    cursor.execute("INSERT INTO stores VALUES (21, 'Minneapolis, MN')")
    cursor.execute("INSERT INTO stores VALUES (95, 'Chicago, IL')")
    cursor.execute("INSERT INTO stores VALUES (64, 'Iowa City, IA')")

    # Agregar compras

    cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
    cursor.execute("INSERT INTO purchases VALUES (23, 64, 21.12)")

    # Recibir resultados

    cursor.execute("SELECT * FROM purchases")

    resultados = cursor.fetchall()

    print(f"Resultados: {resultados}")


if __name__ == '__main__':
    main()
