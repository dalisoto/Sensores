from machine import Pin, SoftI2C, PWM
from time import sleep
import ssd1306

# Crear objeto buzzer
buzzer = PWM(Pin(2), freq=440, duty=512)

# Declarar pines para la interfaz I2C
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Declarar objeto del tipo display OLED con la interfaz I2C
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Lista de mensajes asociados a cada frecuencia
messages = {
    659: "Mi",
    698: "Fa",
    783: "Sol",
    880: "La",
    987: "Si",
    523: "Do",
    587: "Re"
}

# Función para emitir sonido y mostrar mensaje en OLED
def sonido(frecuencia, duracion):
    buzzer.freq(frecuencia)
    buzzer.duty(512)
    mensaje = messages.get(frecuencia, "")
    display.fill(0)
    display.text(mensaje, 2, 2, 2)
    display.show()
    sleep(duracion)
    display.fill(0)
    display.show()

# Ciclo infinito para reproducir la canción
while True:
    sonido(659, 0.5)  # Mi
    sonido(698, 0.5)  # Fa
    sonido(783, 1.0)  # Sol
    sonido(698, 0.5)  # Fa
    sonido(783, 0.5)  # Sol
    sonido(880, 0.5)  # La
    sonido(783, 1.0)  # Sol
    # Continuar con el resto de las notas de la canción...

