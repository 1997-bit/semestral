import pines
import actuadores

NORMAL = "NORMAL"
ALARMA = "ALARMA"

estado = NORMAL


def cambiar_estado(nuevo):
    global estado
    print("[ALARMA]", estado, "->", nuevo)
    estado = nuevo
    actuadores.actualizar_indicadores(estado)


def revisar(temperatura):
    """Cambia de estado si la temperatura sale o vuelve al rango. Evento o None"""
    if temperatura is None:
        return None
    if estado == NORMAL and temperatura > pines.TEMP_MAX:
        cambiar_estado(ALARMA)
        actuadores.encender_frio()
        return "temperatura_alta"
    if estado == NORMAL and temperatura < pines.TEMP_MIN:
        cambiar_estado(ALARMA)
        actuadores.apagar_frio()
        return "temperatura_baja"
    if estado == ALARMA and pines.TEMP_MIN <= temperatura <= pines.TEMP_MAX:
        cambiar_estado(NORMAL)
        return "temperatura_normal"
    return None


def ejecutar_comando(accion):
    if accion == "encender_frio":
        actuadores.encender_frio()
    elif accion == "apagar_frio":
        actuadores.apagar_frio()
    elif accion == "silenciar" and estado == ALARMA:
        # Solo apaga zumbador, sigue en ALARMA
        actuadores.apagar_zumbador()
    else:
        return "error"
    return "ok"
