import stomp



# Configura tus credenciales y dirección del servidor ActiveMQ

activemq_server = "localhost"

activemq_port = 61613  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP

activemq_username = "admin"

activemq_password = "admin"



# Función para determinar la cola basándose en el contenido del mensaje

def obtener_cola_destino(mensaje):

    if "importante" in mensaje:

        return "/queue/cola_importante"

    else:

        return "/queue/cola_normal"



# Conectar al servidor ActiveMQ

connection = stomp.Connection([(activemq_server, activemq_port)])

connection.set_listener("", stomp.PrintingListener())

#connection.start()

connection.connect(login=activemq_username, passcode=activemq_password, wait=True)



# Enviar mensaje a la cola basándose en su contenido

mensaje = "Hola, este es un mensaje importante para mi_cola"



cola_destino = obtener_cola_destino(mensaje)

connection.send(body=mensaje, destination=cola_destino, content_type="text/plain")

print(f"Mensaje enviado a la cola: {cola_destino}")



# Desconectar del servidor ActiveMQ

connection.disconnect()

