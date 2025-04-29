from datetime import datetime

def obtener_timestamp():
    """
    Devuelve el timestamp actual en formato 'YYYY-MM-DD HH:MM:SS'.
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')