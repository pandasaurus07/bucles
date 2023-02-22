# Imports go at the top
from microbit import *
import radio

radio.on()
radio.config(channel=42)

while True:
    if button_a.was_pressed():
        mensaje="malote"
        radio.send(mensaje)
        display.show(mensaje)
        sleep(1000)
    elif button_b.was_pressed():
        mensaje="chiquitin"
        radio.send(mensaje)
        display.show(mensaje)
        sleep(1000)
    else:
        display.show("?")
        sleep(1000)
