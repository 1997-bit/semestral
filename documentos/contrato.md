# Contrato

## Pines

Los define Gloria en `wokwi/pines.py` junto con el circuito.

## Sensores

```python
leer_temperatura()  # grados
puerta_abierta()    # True / False (LDR)
leer_bateria()      # 0 a 100 (potenciómetro)
boton_presionado()  # True / False
```

## Actuadores

```python
encender_led() / apagar_led()
encender_zumbador() / apagar_zumbador()
encender_frio() / apagar_frio()   # relé
mostrar(texto)                    # LCD
```

## Estados

- `NORMAL`: temperatura entre 2 y 8 grados
- `ALARMA`: temperatura fuera de 2 a 8 grados

Comandos: `encender_frio`, `apagar_frio`, `silenciar`

## MQTT

Servidor: `broker.hivemq.com`

| Tema | Mensaje |
|---|---|
| `ds8/frio/datos` | `{"temperatura":5,"puerta":0,"bateria":90,"estado":"NORMAL"}` |
| `ds8/frio/comandos` | `{"accion":"encender_frio"}` |

## Base de datos (SQLite)

| Tabla | Columnas |
|---|---|
| `lecturas` | id, temperatura, puerta, bateria, estado, fecha |
| `eventos` | id, tipo, fecha |
| `comandos` | id, accion, fecha |

## ThingSpeak

| Campo | Dato |
|---|---|
| field1 | temperatura |
| field2 | puerta |
| field3 | bateria |
| field4 | estado (0 normal, 1 alarma) |
