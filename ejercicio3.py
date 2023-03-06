# Imports go at the top
from microbit import *

imagenes =[Image.HEART_SMALL,Image.HEART]

while True:
    if button_a.was_pressed():
        display.show(Image.HEART_SMALL)
    elif button_b.was_pressed():
        display.show(Image.HEART)
