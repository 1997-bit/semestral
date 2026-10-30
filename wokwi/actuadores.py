from machine import Pin, PWM, I2C
from i2c_lcd import I2cLcd
import pines

led_rojo = Pin(pines.LED_R_PIN, Pin.OUT)
led_verde = Pin(pines.LED_G_PIN, Pin.OUT)
led_azul = Pin(pines.LED_B_PIN, Pin.OUT)
rele = Pin(pines.RELE_PIN, Pin.OUT)

buzzer = PWM(Pin(pines.BUZZER_PIN))
buzzer.freq(2000)

i2c = I2C(0, sda=Pin(pines.LCD_SDA), scl=Pin(pines.LCD_SCL), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# LED RGB
def establecer_color(rojo, verde, azul):
    led_rojo.value(rojo)
    led_verde.value(verde)
    led_azul.value(azul)

# Zumbador
def encender_zumbador():
    buzzer.duty_u16(32768)


def apagar_zumbador():
    buzzer.duty_u16(0)

# Rele del equipo de frio
def encender_frio():
    rele.value(1)


def apagar_frio():
    rele.value(0)

# LCD
def mostrar(linea1, linea2=""):
    lcd.clear()
    lcd.putstr(linea1)
    lcd.move_to(0, 1)
    lcd.putstr(linea2)


def actualizar_indicadores(estado):
    if estado == "NORMAL":
        establecer_color(0, 1, 0)  # verde
        apagar_zumbador()
    elif estado == "ALARMA":
        establecer_color(1, 0, 0)  # rojo
        encender_zumbador()


def iniciar():
    establecer_color(0, 0, 1)  # azul mientras conecta
    apagar_zumbador()
    mostrar("Cadena de Frio", "Iniciando...")
