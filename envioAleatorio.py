import stomp
import json
import random
import time
import sensores

# Configura tus credenciales y dirección del servidor ActiveMQ

activemq_server = "localhost"

activemq_port = 61613  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP

activemq_username = "admin"

activemq_password = "admin"

queue_name = "/queue/sensores"


connection = stomp.Connection([(activemq_server, activemq_port)])

connection.set_listener("", stomp.PrintingListener())

connection.connect(login=activemq_username, passcode=activemq_password, wait=True)

try:
    while True:
        randomNumber = random.randint(0, 99)
        if randomNumber == 7:
            print('temperatura')
            msg = {
                "sensor": "temperatura",
                "valor": sensores.sensorTemperatura(),
                "error": False
            }
            msg_json = json.dumps(msg)
            connection.send(body=msg_json, destination=queue_name, content_type="application/json")
        elif randomNumber == 14:
            print('humedad')
            msg = {
                "sensor": "humedad",
                "valor": sensores.sensorHumedad(),
                "error": False
            }
            msg_json = json.dumps(msg)
            connection.send(body=msg_json, destination=queue_name, content_type="application/json")
        elif randomNumber == 21:
            print('luz')
            msg = {
                "sensor": "luz",
                "valor": sensores.sensorLuz(),
                "error": False
            }
            msg_json = json.dumps(msg)
            connection.send(body=msg_json, destination=queue_name, content_type="application/json")
        time.sleep(0.1)
        print('pass', randomNumber)
except KeyboardInterrupt:
    pass

connection.disconnect()