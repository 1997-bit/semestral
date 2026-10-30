# Orientado a eventos. La interrupcion del boton y el temporizador solo marcan,
# el loop hace el trabajo porque MQTT no se puede usar dentro de una interrupcion

from machine import Pin, Timer
from time import sleep_ms
import sensores
import actuadores
import alarma
import mqtt
import adafruit

cliente = None
cliente_aio = None
boton_pendiente = False
lectura_pendiente = False


def al_presionar(pin):
    global boton_pendiente
    boton_pendiente = True


def al_tocar(timer):
    global lectura_pendiente
    lectura_pendiente = True


def procesar_comando(accion, origen):
    resultado = alarma.ejecutar_comando(accion)
    datos = {"accion": accion, "origen": origen, "resultado": resultado}
    print("[CMD]", datos)
    mqtt.publicar(cliente, mqtt.TOPIC_PUB_ACK, datos)


def recepcion_comandos(topic, msg):
    procesar_comando(msg.decode(), "mqtt")


def recepcion_adafruit(topic, msg):
    procesar_comando(msg.decode(), "adafruit")


def enviar_datos():
    temperatura = sensores.leer_temperatura()

    evento = alarma.revisar(temperatura)
    if evento:
        print("[EVENTO]", evento)
        mqtt.publicar(cliente, mqtt.TOPIC_PUB_EVENTOS, {"tipo": evento})

    datos = {
        "temperatura": temperatura,
        "puerta": int(sensores.puerta_abierta()),
        "bateria": sensores.leer_bateria(),
        "estado": alarma.estado,
    }
    print("[DATOS]", datos)
    mqtt.publicar(cliente, mqtt.TOPIC_PUB_DATOS, datos)
    actuadores.mostrar("Temp: {} C".format(temperatura), alarma.estado)
    return datos


def main():
    global cliente, cliente_aio, boton_pendiente, lectura_pendiente
    actuadores.iniciar()
    mqtt.conectar_wifi()
    cliente = mqtt.conectar_broker(recepcion_comandos)
    cliente_aio = adafruit.conectar(recepcion_adafruit)
    actuadores.actualizar_indicadores(alarma.estado)  # ya conectado, verde o rojo
    lecturas = 0

    while True:
        cliente.check_msg()
        cliente_aio.check_msg()

        if boton_pendiente:
            boton_pendiente = False
            procesar_comando("silenciar", "boton")

        if lectura_pendiente:
            lectura_pendiente = False
            datos = enviar_datos()
            lecturas += 1
            if lecturas % 5 == 0:  # Adafruit cada 10 s, limite 30 datos/min
                adafruit.publicar(cliente_aio, datos)

        sleep_ms(50)


sensores.boton.irq(trigger=Pin.IRQ_FALLING, handler=al_presionar)
Timer(period=2000, mode=Timer.PERIODIC, callback=al_tocar)  # DHT22 minimo 2 s

# Si se cae la red, reconecta todo
while True:
    try:
        main()
    except OSError as error:
        print("Conexion perdida:", error)
        sleep_ms(5000)
