# Imports go at the top
from microbit import *

i=0
lista_nombres = ["Lucas","Pepe","Daniel","María","Alicia"]
while True:
    if button_a.was_pressed():
        i = i - 1
        sleep(500)
    elif button_b.was_pressed():
        i = i + 1

    if i>len(lista_nombres)-1:
        i=0
    elif i<0:
        i = len(lista_nombres)-1
    else:
        display.show(i)
        sleep(500)
        display.show(lista_nombres[i])
        sleep(500)
        
