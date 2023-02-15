# Imports go at the top
from microbit import *
import random

vocales =["A", "E", "I", "O", "U"]
consonantes =["F", "R", "T", "V", "P", "G", "M", "B", "C", "S", "L"]
total_palabras = 9



while total_palabras>0:
    if button_a.was_pressed():
        vocal_aleatoria = vocales[random.randint(0,len(vocales)-1)]
        display.show(vocal_aleatoria)
        total_palabras = total_palabras -1
        sleep(1000)
    elif button_b.was_pressed():
        consonante_aleatoria = consonantes[random.randint(0,len(consonantes)-1)]
        display.show(consonante_aleatoria)
        total_palabras = total_palabras- 1
        sleep(1000)
    else:
        display.show("?")

display.scroll("Fin")
cuenta = 20
while True:
    cuenta = cuenta - 1
    display.scroll(cuenta,delay=30)
    sleep(500)



