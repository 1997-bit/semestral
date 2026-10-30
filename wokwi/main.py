# Loop principal: boton, temperatura, LCD, datos, MQTT y Adafruit

from time import sleep_ms
import ujson
import sensores
import actuadores
import alarma
import mqtt
import adafruit

cliente = None
cliente_aio = None


def procesar_comando(accion, origen):
    resultado = alarma.ejecutar_comando(accion)
    datos = {"accion": accion, "origen": origen, "resultado": resultado}
    print("[CMD]", datos)
    mqtt.publicar(cliente, mqtt.TOPIC_PUB_ACK, datos)
    return resultado


def recepcion_comandos(topic, msg):
    # HiveMQ manda JSON: {"accion": "encender_frio"}
    try:
        accion = ujson.loads(msg)["accion"]
    except (ValueError, KeyError):
        print("[CMD] mensaje invalido:", msg)
        return
    procesar_comando(accion, "mqtt")


def recepcion_adafruit(topic, msg):
    # Adafruit manda el texto solo: encender_frio
    procesar_comando(msg.decode(), "adafruit")


def enviar_datos():
    temperatura = sensores.leer_temperatura()

    evento = alarma.revisar(temperatura)
    if evento:
        datos_evento = {"tipo": evento}
        print("[EVENTO]", datos_evento)
        mqtt.publicar(cliente, mqtt.TOPIC_PUB_EVENTOS, datos_evento)

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
    global cliente, cliente_aio
    actuadores.iniciar()
    mqtt.conectar_wifi()
    cliente = mqtt.conectar_broker(recepcion_comandos)
    cliente_aio = adafruit.conectar(recepcion_adafruit)
    actuadores.actualizar_indicadores(alarma.estado)  # ya conectado: verde o rojo

    boton_antes = False
    vueltas = 0

    while True:
        # Comandos de HiveMQ y Adafruit
        cliente.check_msg()
        cliente_aio.check_msg()

        # Boton: solo al presionar, silencia la alarma
        boton = sensores.boton_presionado()
        if boton and not boton_antes:
            procesar_comando("silenciar", "boton")
        boton_antes = boton

        # Datos cada 2 s (el DHT22 no lee mas rapido), Adafruit cada 10 s (limite 30 datos/min)
        vueltas += 1
        if vueltas % 20 == 0:
            datos = enviar_datos()
        if vueltas == 100:
            adafruit.publicar(cliente_aio, datos)
            vueltas = 0

        sleep_ms(100)


# Si se cae la red, reconecta todo
while True:
    try:
        main()
    except OSError as error:
        print("Conexion perdida:", error)
        sleep_ms(5000)
