import socket
from db import crear_tabla_mensajes, guardar_mensaje
from utils import obtener_timestamp

# Configuración del servidor
HOST = '127.0.0.1'  # Equivale a localhost
PORT = 5000         # Puerto en escucha

def inicializar_socket():
    """
    Inicializa y configura el socket del servidor.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    server_socket.bind((HOST, PORT))  # Enlaza el socket al host y puerto
    server_socket.listen()  # Escucha conexiones entrantes
    print(f"Servidor escuchando en {HOST}:{PORT}")
    return server_socket

def aceptar_conexiones(server_socket):
    """
    Acepta conexiones entrantes y procesa los mensajes de los clientes.
    """
    while True:
        conn, addr = server_socket.accept()
        print(f"Conexión establecida desde {addr}")

        with conn:
            while True:
                data = conn.recv(1024)  # Se recibe datos del cliente
                if not data:
                    break  # Se corta la conexión

                mensaje = data.decode('utf-8')
                print(f"Mensaje recibido: {mensaje}")

                # Guardar mensaje en la base de datos
                guardar_mensaje(mensaje, addr[0])

                # Enviar confirmación al cliente
                timestamp = obtener_timestamp()
                respuesta = f"Mensaje recibido: {timestamp}"
                conn.sendall(respuesta.encode('utf-8'))

def main():
    try:
        # Crear la tabla de mensajes si no existe
        crear_tabla_mensajes()

        # Inicializar el socket del servidor
        server_socket = inicializar_socket()

        # Aceptar y manejar conexiones
        aceptar_conexiones(server_socket)

    except Exception as e:
        print(f"Error en el servidor: {e}")

if __name__ == "__main__":
    main()