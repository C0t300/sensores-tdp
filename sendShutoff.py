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

timeOff = {
    "luz": 0,
    "temperatura": 0,
    "humedad": 0
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

def shutOffRandom(posibility: float = 0.1) -> int:
    if random.random() < posibility:
        sensor = random.randint(1, 3)
        return sensor
    else:
        return 0

try:
    while True:
        sensor = shutOffRandom() #0,1,2,3
        if sensor == 1 and isOn["luz"]:
            isOn["luz"] = not isOn["luz"]
            msg = {
                "sensor": "luz",
            }
            timeOff["luz"] += 1
            msg_json = json.dumps(msg)
            connection.send(body=msg_json, destination=queue_name, content_type="application/json")
            print("Apagando sensor luz.")

        elif sensor == 2 and isOn["temperatura"]:
            isOn["temperatura"] = not isOn["temperatura"]
            msg = {
                "sensor": "temperatura",
            }
            timeOff["temperatura"] += 1
            msg_json = json.dumps(msg)
            connection.send(body=msg_json, destination=queue_name, content_type="application/json")
            print("Apagando sensor temperatura.")
        elif sensor == 3 and isOn["humedad"]:
            isOn["humedad"] = not isOn["humedad"]
            msg = {
                "sensor": "humedad",
            }
            timeOff["humedad"] += 1
            msg_json = json.dumps(msg)
            connection.send(body=msg_json, destination=queue_name, content_type="application/json")
            print("Apagando sensor humedad.")
        else:
            print('No se apagó nada.')

            for sensor in timeOff:

                if not isOn[sensor]:
                    timeOff[sensor] += 1

                if timeOff[sensor] >= 10:
                    timeOff[sensor] = 0
                    isOn[sensor] = not isOn[sensor]
                    msg = {
                        "sensor": sensor,
                    }
                    msg_json = json.dumps(msg)
                    connection.send(body=msg_json, destination=queue_name, content_type="application/json")
                    print("Reiniciando sensor " + sensor)
        time.sleep(1)
except KeyboardInterrupt:
    pass

connection.disconnect()