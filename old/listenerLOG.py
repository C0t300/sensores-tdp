import stomp
import time
import datetime
import json
from pathlib import Path


logDirectory = "logs/"
if not Path(logDirectory).exists():
    Path(logDirectory).mkdir()

class MyListener(stomp.ConnectionListener):

    def on_error(self, frame):

        print(frame.body)

    def on_message(self, frame):

        print(frame.body)
        msg = json.loads(frame.body)
        sensor = msg["sensor"]
        path = Path(logDirectory + sensor + ".txt")
        with open(path, "a") as fp:
            newdict = {"fecha": str(datetime.datetime.now())}
            for key in msg:
                newdict[key] = msg[key]
            fp.write(str(newdict) + "\n")

        

# Configura tus credenciales y dirección del servidor ActiveMQ

activemq_server = "localhost"

activemq_port = 61613  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP

activemq_username = "tu_usuario"

activemq_password = "tu_contraseña"

queue_name = "/queue/sensores"

# Conectar al servidor ActiveMQ

connection = stomp.Connection([(activemq_server, activemq_port)])

connection.set_listener("", MyListener())

connection.connect(login=activemq_username, passcode=activemq_password, wait=True)

# Suscribirse a la cola

connection.subscribe(destination=queue_name, id=1, ack="auto")

# Esperar mensajes

print("Esperando mensajes... presiona Ctrl+C para salir")

try:

    while True:

        time.sleep(1)

except KeyboardInterrupt:

    pass

# Desconectar del servidor ActiveMQ

connection.disconnect()
