# Guardar en MariaDB

import pymysql


def conectar():
    return pymysql.connect(host="localhost", user="ds8", password="ds8", database="frio", autocommit=True)


def ejecutar(sql, valores):
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(sql, valores)


def guardar_lectura(datos):
    ejecutar(
        "INSERT INTO lecturas (temperatura, puerta, bateria, estado) VALUES (%s, %s, %s, %s)",
        (datos["temperatura"], datos["puerta"], datos["bateria"], datos["estado"]),
    )


def guardar_evento(datos):
    ejecutar("INSERT INTO eventos (tipo) VALUES (%s)", (datos["tipo"],))


def guardar_comando(datos):
    ejecutar(
        "INSERT INTO comandos (accion, origen, resultado) VALUES (%s, %s, %s)",
        (datos["accion"], datos["origen"], datos["resultado"]),
    )
