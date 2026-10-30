from machine import Pin, ADC
import dht
import pines

sensor_dht = dht.DHT22(Pin(pines.DHT_PIN))
ldr = ADC(Pin(pines.LDR_PIN))
pot = ADC(Pin(pines.POT_PIN))
boton = Pin(pines.BOTON_PIN, Pin.IN, Pin.PULL_UP)  # 0 presionado


def leer_temperatura():
    """grados o None"""
    try:
        sensor_dht.measure()
        return sensor_dht.temperature()
    except OSError:
        return None


def puerta_abierta():
    # AO baja con mas luz, calibrar LDR_UMBRAL en Wokwi
    return ldr.read_u16() < pines.LDR_UMBRAL


def leer_bateria():
    """0 a 100"""
    return pot.read_u16() * 100 // 65535
