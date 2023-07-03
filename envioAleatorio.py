import stomp
import json
import random
import time
import sensores

# Configura tus credenciales y dirección del servidor ActiveMQ

activemq_server = "b-1560683c-9b1e-4521-ae71-196c283796ac-1.mq.us-east-2.amazonaws.com"

activemq_port = 61614  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP

activemq_username = "tu_usuario"

activemq_password = "tu_contrasena"

queue_name = "/queue/sensores"

hosts = [(activemq_server, activemq_port)]

connection = stomp.Connection(hosts)

connection.set_ssl(hosts)

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