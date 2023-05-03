import random

def error() -> bool:
    return random.randint(0, 20) == 7

def sensorTemperatura() -> int:
    if error():
        return 1000
    temp = random.randint(0, 80) - 20
    return temp

def sensorHumedad() -> int:
    if error():
        return -213
    hum = random.randint(0, 950)
    return hum

def sensorLuz() -> int:
    if error():
        return -293871
    luz = random.randint(0, 1023)
    return luz