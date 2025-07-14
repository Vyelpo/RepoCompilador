import sqlite3

# Conectamos el .py a una base de datos
connection = sqlite3.connect('baseDeDatos.db') # En caso de que no exista se crea un nuevo .db
cursor = connection.cursor()

# Creamos una tabla para los usuarios
cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
               user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
               user_name TEXT, 
               user_password TEXT
               )
               """)

# Eliminar valores de la tabla
cursor.execute("DELETE FROM usuarios")

# Desde acá podemos añadir usuarios
cursor.execute("INSERT INTO usuarios (user_name, user_password) VALUES ('usuario0', '123')")
cursor.execute("INSERT INTO usuarios (user_name, user_password) VALUES ('usuario1', '123')")
cursor.execute("INSERT INTO usuarios (user_name, user_password) VALUES ('usuario2', '123')")

# Comprobamos los valores dentro de la base de datos
cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())

# Guardamos los cambios
connection.commit()
connection.close()