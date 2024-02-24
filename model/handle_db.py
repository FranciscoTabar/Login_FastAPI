import sqlite3

conn = sqlite3.connect("./usuarios.db")
cursor = conn.cursor()

# Crear la tabla users
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        username TEXT NOT NULL,
        pais TEXT NOT NULL,
        password_user TEXT NOT NULL
    )
""")

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()


class Handle_DB():
    def __init__(self):
        self._con = sqlite3.connect("./usuarios.db")
        self._cur = self._con.cursor()

    def get_all(self):
        data = self._cur.execute("SELECT * FROM users")
        return data.fetchall()

    def get_only(self, data_user):
        data = self._cur.execute("SELECT * FROM users WHERE username = ?", (data_user,))
        return data.fetchone()

    def insert(self, data_user):
        self._cur.execute("INSERT INTO users (nombre, apellido, username, pais, password_user) VALUES (?, ?, ?, ?, ?)", (
            data_user["nombre"],
            data_user["apellido"],
            data_user["username"],
            data_user["pais"],
            data_user["password_user"]
        ))
        self._con.commit()

    def __del__(self):
        self._con.close()


db = Handle_DB()
 