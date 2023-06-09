import stomp
import time
import datetime
import json
import http.client
from pathlib import Path


logDirectory = "logs/"
if not Path(logDirectory).exists():
    Path(logDirectory).mkdir()

class MyListener(stomp.ConnectionListener):

    def on_error(self, frame):

        print(frame.body)

    def on_message(self, frame):

        msg = json.loads(frame.body)
        print(msg)
        sensor = msg["sensor"]
        conn = http.client.HTTPSConnection("ati2y37q462q7v2kknbmkacu7u0iwtrw.lambda-url.us-east-2.on.aws")
        payload = json.dumps({
            "date": datetime.datetime.now(),
            "sensor": sensor,
            "value": msg["valor"]
        }, default=str)
        headers = {
        'usm': 'TallerDeProgra',
        'Content-Type': 'application/json'
        }
        conn.request("POST", "/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

        

# Configura tus credenciales y dirección del servidor ActiveMQ

activemq_server = "b-1560683c-9b1e-4521-ae71-196c283796ac-1.mq.us-east-2.amazonaws.com"

activemq_port = 61614  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP

activemq_username = "tu_usuario"

activemq_password = "tu_contrasena"

queue_name = "/queue/sensores"

hosts = [(activemq_server, activemq_port)]

connection = stomp.Connection(hosts)

connection.set_ssl(hosts)

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
