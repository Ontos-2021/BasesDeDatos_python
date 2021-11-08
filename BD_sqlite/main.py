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
    def recibir_resultados():
        cursor.execute("SELECT * FROM purchases")

        resultados = cursor.fetchall()

        print("Purchases:")
        for purchase in resultados:
            print(f"ID: {purchase[0]} - ID store: {purchase[1]} - Total Cost: {purchase[2]}")
        print("")

    recibir_resultados()

    # Actualizar

    cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE id_purchase = 54")

    recibir_resultados()

    # Borrar

    cursor.execute("DELETE FROM purchases WHERE id_purchase = 54")

    recibir_resultados()


if __name__ == '__main__':
    main()
