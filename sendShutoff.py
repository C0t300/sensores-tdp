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

queue_name = "/queue/powered"

isOn = {
    "luz": True,
    "temperatura": True,
    "humedad": True
}


connection = stomp.Connection([(activemq_server, activemq_port)])

connection.set_listener("", stomp.PrintingListener())

connection.connect(login=activemq_username, passcode=activemq_password, wait=True)

def ask() -> int:
    print("¿Qué sensor quieres apagar/prender?")
    print("1. Luz")
    print("2. Temperatura")
    print("3. Humedad")
    print("4. Salir")
    sensor = int(input("-> "))
    return sensor

try:
    while True:
        sensor = ask()
        if sensor == 1:
            msg = {
                "sensor": "luz",
            }
        elif sensor == 2:
            msg = {
                "sensor": "temperatura",
            }
        elif sensor == 3:
            msg = {
                "sensor": "humedad",
            }
        else:
            break
        msg_json = json.dumps(msg)
        connection.send(body=msg_json, destination=queue_name, content_type="application/json")
        print("Mensaje enviado")
except KeyboardInterrupt:
    pass

connection.disconnect()