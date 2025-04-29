import sqlite3
from datetime import datetime

# Nombre del archivo de la base de datos
DB_NAME = 'chat.db'

def crear_tabla_mensajes():
    """
    Crea la tabla de mensajes si no existe.
    """
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        # Crear la tabla
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        ''')

        conexion.commit()
        conexion.close()
        print("Tabla 'mensajes' lista en la base de datos.")
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")

def guardar_mensaje(contenido, ip_cliente):
    """
    Guarda un mensaje en la base de datos.
    """
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        fecha_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute('''
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?)
        ''', (contenido, fecha_envio, ip_cliente))

        conexion.commit()
        conexion.close()
        print("Mensaje guardado en la base de datos.")
    except sqlite3.Error as e:
        print(f"Error al guardar el mensaje: {e}")