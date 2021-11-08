import sqlite3


# Definir conección y el cursor
def main():
    connection = sqlite3.connect('BaseDeDatos.db')
    cursor = connection.cursor()

    comando1 = """
    CREATE TABLE IF NOT EXISTS
    stores(id_store INTEGER PRIMARY KEY, location TEXT)
    """
    cursor.execute(comando1)


if __name__ == '__main__':
    main()
