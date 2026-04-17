import socket

# Configuración del cliente
HOST = "127.0.0.1"
PORT = 5000


def iniciar_cliente():
    """
    Se conecta al servidor y permite enviar varios mensajes
    hasta que el usuario escriba 'éxito'.
    """
    cliente_socket = None

    try:
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect((HOST, PORT))

        print("Conectado al servidor.")
        print("Escribí tus mensajes. Para salir, escribí 'éxito'.")

        while True:
            mensaje = input("Ingresá un mensaje: ")

            if mensaje.lower() == "éxito":
                print("Cerrando conexión con el servidor...")
                break

            cliente_socket.send(mensaje.encode("utf-8"))

            respuesta = cliente_socket.recv(1024).decode("utf-8")
            print(f"Respuesta del servidor: {respuesta}")

    except ConnectionRefusedError:
        print("No se pudo conectar con el servidor. Verificá que esté en ejecución.")

    except ConnectionResetError:
        print("La conexión fue cerrada inesperadamente por el servidor.")

    except Exception as e:
        print(f"Ocurrió un error en el cliente: {e}")

    finally:
        if cliente_socket:
            cliente_socket.close()


if __name__ == "__main__":
    iniciar_cliente()