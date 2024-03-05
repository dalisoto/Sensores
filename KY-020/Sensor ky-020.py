from machine import Pin, I2C
import ssd1306
import time

# Definir el pin al que está conectado el sensor de vibración
PIN_SENSOR_VIBRACION = 14  

# Configuración de la pantalla OLED
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))  # Configura la comunicación I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # Inicializa la pantalla OLED

# Configurar el pin del sensor de vibración
sensor_vibracion = Pin(PIN_SENSOR_VIBRACION, Pin.IN)

def mostrar_estado_sensor():
    valor_vibracion = sensor_vibracion.value()
    estado = "DETECTADO" if sensor_vibracion.value() else "NO DETECTADO"
    oled.fill(0)  # Borra la pantalla
    oled.text("Vibracion", 0, 0)  # Texto fijo
    oled.text("Valor: {}".format(valor_vibracion), 0, 20)  # Mostrar el valor de la vibración
    oled.show()  # Actualiza la pantalla

# Ciclo principal
while True:
    mostrar_estado_sensor()
    time.sleep(0.5)  # Espera medio segundo antes de volver a leer el sensor