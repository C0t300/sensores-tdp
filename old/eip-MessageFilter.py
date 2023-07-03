import stomp

import json



# Configura tus credenciales y dirección del servidor ActiveMQ

activemq_server = "localhost"

activemq_port = 61613  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP

activemq_username = "admin"

activemq_password = "admin"

queue_name = "/queue/mi_cola"



# Función para aplicar el filtro

def mensaje_valido(mensaje):

    # Aquí puedes implementar la lógica de tu filtro. Por ejemplo:

    return len(mensaje["texto"]) > 5



# Conectar al servidor ActiveMQ

connection = stomp.Connection([(activemq_server, activemq_port)])

connection.set_listener("", stomp.PrintingListener())

#connection.start()

connection.connect(login=activemq_username, passcode=activemq_password, wait=True)



# Enviar mensaje JSON a la cola si cumple con el criterio del filtro

mensaje = {

    "texto": "Hola, este es un mensaje para mi_cola",

    "prioridad": "alta"

}



if mensaje_valido(mensaje):

    mensaje_json = json.dumps(mensaje)  # Convertir el objeto Python en una cadena JSON

    connection.send(body=mensaje_json, destination=queue_name, content_type="application/json")

    print("Mensaje JSON enviado a la cola.")

else:

    print("El mensaje no cumple con el criterio del filtro y no se envía.")



# Desconectar del servidor ActiveMQ

connection.disconnect()