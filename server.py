import socket
from database import crear_base_de_datos, guardar_mensaje

# Configuración del servidor
HOST = "127.0.0.1"
PORT = 5000


def inicializar_servidor():
    """
    Crea y configura el socket del servidor.
    """
    try:
        servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Permite reutilizar el puerto si se reinicia el servidor
        servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        servidor_socket.bind((HOST, PORT))
        servidor_socket.listen(5)

        print(f"Servidor escuchando en {HOST}:{PORT}")
        return servidor_socket

    except OSError as e:
        print(f"Error al iniciar el servidor: {e}")
        return None


def atender_cliente(cliente_socket, direccion_cliente):
    """
    Atiende al cliente, recibe mensajes, los guarda en SQLite
    y envía una respuesta de confirmación.
    """
    try:
        while True:
            mensaje = cliente_socket.recv(1024).decode("utf-8")

            if not mensaje:
                break

            if mensaje.strip() == "":
                respuesta = "No se puede enviar un mensaje vacío."
                cliente_socket.send(respuesta.encode("utf-8"))
                continue

            print(f"Mensaje recibido de {direccion_cliente[0]}: {mensaje}")

            timestamp = guardar_mensaje(mensaje, direccion_cliente[0])
            respuesta = f"Mensaje recibido: {timestamp}"

            cliente_socket.send(respuesta.encode("utf-8"))

    except Exception as e:
        print(f"Error con el cliente {direccion_cliente}: {e}")

    finally:
        cliente_socket.close()
        print(f"Cliente desconectado: {direccion_cliente}")


def iniciar_servidor():
    """
    Función principal del servidor.
    """
    try:
        crear_base_de_datos()
    except Exception as e:
        print(f"No se pudo preparar la base de datos: {e}")
        return

    servidor_socket = inicializar_servidor()

    if servidor_socket is None:
        return

    try:
        while True:
            print("Esperando una conexión...")
            cliente_socket, direccion_cliente = servidor_socket.accept()
            print(f"Cliente conectado desde {direccion_cliente}")

            atender_cliente(cliente_socket, direccion_cliente)

    except KeyboardInterrupt:
        print("\nServidor detenido manualmente.")

    finally:
        servidor_socket.close()
        print("Servidor cerrado correctamente.")


if __name__ == "__main__":
    iniciar_servidor()