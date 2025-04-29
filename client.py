import socket

# Configuración del cliente
HOST = '127.0.0.1'  # IP del servidor (localhost)
PORT = 5000         # Puerto del servidor

def main():
    try:
        # Crear el socket del cliente
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectarse al servidor
        client_socket.connect((HOST, PORT))
        print(f"Conectado al servidor en {HOST}:{PORT}")

        while True:
            # Pedir mensaje al usuario
            mensaje = input("Escribí un mensaje (o 'éxito' para salir): ")

            if mensaje.lower() == 'éxito':
                print("Cerrando conexión...")
                break

            # Enviar mensaje al servidor
            client_socket.sendall(mensaje.encode('utf-8'))

            # Recibir y mostrar respuesta del servidor
            respuesta = client_socket.recv(1024)
            print(f"Respuesta del servidor: {respuesta.decode('utf-8')}")

        # Cerrar el socket del cliente
        client_socket.close()

    except Exception as e:
        print(f"Error en el cliente: {e}")

if __name__ == "__main__":
    main()
