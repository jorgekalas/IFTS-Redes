# PFO 1 - Programación sobre Redes

## Implementación de un chat básico cliente-servidor con sockets y base de datos

Este trabajo práctico consiste en desarrollar una aplicación simple de chat utilizando sockets en Python, con una arquitectura cliente-servidor. Además, cada mensaje enviado por el cliente se almacena en una base de datos SQLite.

## Objetivo del proyecto

Aprender a:
- configurar un servidor de sockets en Python
- permitir la conexión de clientes
- recibir mensajes desde el cliente
- almacenar esos mensajes en una base de datos SQLite
- responder al cliente con una confirmación
- aplicar modularización y manejo de errores

## Archivos del proyecto

- `server.py`: contiene la lógica del servidor
- `client.py`: contiene la lógica del cliente
- `database.py`: contiene las funciones relacionadas con SQLite
- `chat.db`: base de datos generada automáticamente al ejecutar el servidor

## Funcionamiento general

### Servidor

El servidor:
- escucha en `localhost:5000`
- acepta conexiones entrantes
- recibe mensajes enviados por el cliente
- guarda cada mensaje en la base de datos
- responde con la fecha y hora en la que recibió el mensaje

### Cliente

El cliente:
- se conecta al servidor
- permite enviar múltiples mensajes
- muestra en pantalla la respuesta del servidor
- termina cuando el usuario escribe `éxito`

## Base de datos

Se utiliza SQLite y se crea una tabla llamada `mensajes` con los siguientes campos:
- `id`
- `contenido`
- `fecha_envio`
- `ip_cliente`

## Cómo ejecutar el proyecto

### 1. Ejecutar el servidor

    python server.py

### 2. Ejecutar el cliente en otra terminal

    python client.py

## Ejemplo de uso

Cliente:

    Conectado al servidor.
    Escribí tus mensajes. Para salir, escribí 'éxito'.
    Ingresá un mensaje: Hola
    Respuesta del servidor: Mensaje recibido: 2026-04-17 15:10:20

## Validaciones agregadas

- Si el usuario envía un mensaje vacío, el servidor responde que no se puede enviar un mensaje vacío.