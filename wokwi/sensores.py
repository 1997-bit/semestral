from machine import Pin
import pines

boton = Pin(pines.BOTON_PIN, Pin.IN, Pin.PULL_UP)  # 0 presionado

# Faltan leer_temperatura, puerta_abierta y leer_bateria (ver contrato)


def boton_presionado():
    return boton.value() == 0
