import sqlite3

def conectar_db():
    try:
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print(f"Error al conectarse con la base de datos {e}")
        return None, None
        
def create_table(cursor):
    try:
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL
                    )
                    """)
    except Exception as e:
        print(f"Error al crear table {e}")
        return None, None
        
def new_user(cursor, conn, name, lastname, username, password_hash):
    if not name or not lastname or not username or not password_hash:
        return False
    try:
        cursor.execute("""
    INSERT INTO users (name, lastname, username, password_hash)
                    VALUES(?, ?, ?, ?)
                    """, (name, lastname, username, password_hash))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al guardar el usuario {e}")
        return False

def find_user(cursor, user):        
    try:
        cursor.execute("""
    SELECT * FROM users 
                    WHERE username = ?
                    """, (user,))
        user_db = cursor.fetchone()
        return user_db
    except Exception as e:
        print(f"Error al buscar usuario {e}")
        return None
