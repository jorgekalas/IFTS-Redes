import sqlite3
from datetime import datetime

# Nombre de la base de datos
DB_NAME = "chat.db"


def crear_base_de_datos():
    """
    Crea la base de datos y la tabla de mensajes si no existe.
    """
    conexion = None

    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        """)

        conexion.commit()
        print("Base de datos lista.")

    except sqlite3.Error as e:
        print(f"Error al crear la base de datos: {e}")
        raise

    finally:
        if conexion:
            conexion.close()


def guardar_mensaje(contenido, ip_cliente):
    """
    Guarda un mensaje en la base de datos y devuelve el timestamp.
    """
    conexion = None

    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?)
        """, (contenido, timestamp, ip_cliente))

        conexion.commit()
        return timestamp

    except sqlite3.Error as e:
        print(f"Error al guardar el mensaje: {e}")
        raise

    finally:
        if conexion:
            conexion.close()