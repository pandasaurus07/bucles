# Imports go at the top
from microbit import *

imagenes =[Image.HEART_SMALL,Image.HEART]

while True:
    display.show(Image.HEART_SMALL)
    sleep(500)
    display.show(Image.HEART)
    sleep(500)
