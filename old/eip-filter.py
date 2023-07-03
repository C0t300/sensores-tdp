import stomp

# Configura tus credenciales y dirección del servidor ActiveMQ

activemq_server = "localhost"

activemq_port = 61613  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP

activemq_username = "admin"

activemq_password = "admin"

queue_name = "/queue/mi_cola"



# Función para aplicar el filtro

def mensaje_valido(mensaje):

    # Aquí puedes implementar la lógica de tu filtro. Por ejemplo:

    return len(mensaje) > 5



# Conectar al servidor ActiveMQ

connection = stomp.Connection([(activemq_server, activemq_port)])

connection.set_listener("", stomp.PrintingListener())

#connection.start()

connection.connect(login=activemq_username, passcode=activemq_password, wait=True)



# Enviar mensaje a la cola si cumple con el criterio del filtro

mensaje = "Hola, este es un mensaje para mi_cola"



if mensaje_valido(mensaje):

    connection.send(body=mensaje, destination=queue_name, content_type="text/plain")

    print("Mensaje enviado a la cola.")

else:

    print("El mensaje no cumple con el criterio del filtro y no se envía.")



# Desconectar del servidor ActiveMQ

connection.disconnect()