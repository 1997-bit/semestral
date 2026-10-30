# Wi-Fi y MQTT del Lab 7

import network
import time
import ujson
from umqttsimple import MQTTClient

SSID = 'Wokwi-GUEST'
PASSWORD = ''

MQTT_BROKER = "broker.hivemq.com"
CLIENT_ID = "ds8_frio_pico1"

TOPIC_PUB_DATOS = b"ds8/frio/datos"
TOPIC_PUB_EVENTOS = b"ds8/frio/eventos"
TOPIC_PUB_ACK = b"ds8/frio/ack"
TOPIC_SUB_COMANDOS = b"ds8/frio/comandos"


def conectar_wifi():
    print("Conectando a Wi-Fi...")
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)
    while not wifi.isconnected():
        time.sleep(0.5)
    print("Wi-Fi conectado")


def conectar_broker(recepcion_comandos):
    print("Conectando a", MQTT_BROKER)
    cliente = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    cliente.set_callback(recepcion_comandos)
    cliente.connect()
    cliente.subscribe(TOPIC_SUB_COMANDOS)
    print("MQTT conectado")
    return cliente


def publicar(cliente, topic, datos):
    cliente.publish(topic, ujson.dumps(datos))
