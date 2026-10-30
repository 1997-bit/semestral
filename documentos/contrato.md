# Contrato

## Pines

`wokwi/pines.py`, igual que `diagram.json`.

## Sensores

```python
leer_temperatura()  # grados
puerta_abierta()  # True / False, LDR
leer_bateria()  # 0 a 100, potenciómetro
boton  # Pin, interrupcion en main.py
```

## Actuadores

```python
establecer_color(rojo, verde, azul)  # LED RGB
encender_zumbador() / apagar_zumbador()
encender_frio() / apagar_frio()  # relay
mostrar(linea1, linea2="")  # LCD
```

## Estados

| Estado | Condición | Salida |
|---|---|---|
| Iniciando | Conectando | LED azul |
| `NORMAL` | 2 a 8 °C | LED verde |
| `ALARMA` | Fuera de rango | LED rojo y zumbador |

Comandos `encender_frio`, `apagar_frio` y `silenciar`. El botón envía `silenciar`.

`temperatura_alta` enciende el relay y `temperatura_baja` lo apaga.

## MQTT

Broker `broker.hivemq.com`

| Tema | Mensaje |
|---|---|
| `ds8/frio/datos` | `{"temperatura":5,"puerta":0,"bateria":90,"estado":"NORMAL"}` |
| `ds8/frio/eventos` | `{"tipo":"temperatura_alta"}`, `temperatura_baja`, `temperatura_normal` |
| `ds8/frio/comandos` | `encender_frio` |
| `ds8/frio/ack` | `{"accion":"encender_frio","origen":"mqtt","resultado":"ok"}` |

## MariaDB

| Tabla | Columnas |
|---|---|
| `lecturas` | id, temperatura, puerta, bateria, estado, fecha |
| `eventos` | id, tipo, fecha |
| `comandos` | id, accion, origen, resultado, fecha |

## Adafruit IO

Cuenta en `wokwi/secretos.py`, copiado de `secretos_ejemplo.py`.

| Feed | Dato |
|---|---|
| `temperatura` | grados |
| `puerta` | 0 cerrada, 1 abierta |
| `bateria` | 0 a 100 |
| `estado` | NORMAL / ALARMA |
| `comandos` | `encender_frio`, `apagar_frio`, `silenciar` |
