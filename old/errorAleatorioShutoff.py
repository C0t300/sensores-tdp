import stomp
import json
import random
import time
import sensores

isOn = {
    "luz": True,
    "temperatura": True,
    "humedad": True
}

class MyListener(stomp.ConnectionListener):

    def on_error(self, frame):
        print("ERR")
        print(frame.body)

    def on_message(self, frame):

        msg = json.loads(frame.body)
        try:
            isOn[msg["sensor"]] = not isOn[msg["sensor"]]
            print("El sensor " + msg["sensor"] + " está " + ("prendido" if isOn[msg["sensor"]] else "apagado"))
        except KeyError:
            print("ERR")
            print("El mensaje no tiene el formato correcto")
        
            

# Configura tus credenciales y dirección del servidor ActiveMQ

activemq_server = "localhost"

activemq_port = 61613  # Por defecto, ActiveMQ utiliza el puerto 61613 para STOMP

activemq_username = "admin"

activemq_password = "admin"

queue_name = "/queue/sensores"
queue_name_powered = "/queue/powered"

validValues = {
    "luz": [0,1023],
    "temperatura": [-20,60],
    "humedad": [0,950]
}

def checkValue(sensor, value):
    if value < validValues[sensor][0] or value > validValues[sensor][1]:
        print('ERR')
        return False
    return True


connection = stomp.Connection([(activemq_server, activemq_port)])

connection.set_listener("", MyListener())

connection.connect(login=activemq_username, passcode=activemq_password, wait=True)

connection.subscribe(destination=queue_name_powered, id=1, ack="auto")

try:
    while True:
        randomNumber = random.randint(0, 99)
        if randomNumber == 7 and isOn["temperatura"]:
            print('temperatura')
            msg = {
                "sensor": "temperatura",
                "valor": sensores.sensorTemperatura(),
                "error": False
            }
            if not checkValue(msg["sensor"], msg["valor"]):
                msg["error"] = True
            msg_json = json.dumps(msg)
            connection.send(body=msg_json, destination=queue_name, content_type="application/json")
        elif randomNumber == 14 and isOn["humedad"]:
            print('humedad')
            msg = {
                "sensor": "humedad",
                "valor": sensores.sensorHumedad(),
                "error": False
            }
            if not checkValue(msg["sensor"], msg["valor"]):
                msg["error"] = True
            msg_json = json.dumps(msg)
            connection.send(body=msg_json, destination=queue_name, content_type="application/json")
        elif randomNumber == 21 and isOn["luz"]:
            print('luz')
            msg = {
                "sensor": "luz",
                "valor": sensores.sensorLuz(),
                "error": False
            }
            if not checkValue(msg["sensor"], msg["valor"]):
                msg["error"] = True
            msg_json = json.dumps(msg)
            connection.send(body=msg_json, destination=queue_name, content_type="application/json")
        time.sleep(0.1)
        print('pass', randomNumber)
except KeyboardInterrupt:
    pass

connection.disconnect()