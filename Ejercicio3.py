# Imports go at the top
from microbit import *
import random
import music

imagenes =[Image.HEART_SMALL,Image.HEART,Image.GHOST,Image.GIRAFFE,Image.TRIANGLE]
musica=[music.BADDY,music.CHASE,music.BIRTHDAY,music.DADADADUM]
while True:
    if button_a.was_pressed():
        imagenes_aleatoria = imagenes[random.randint(0,len(imagenes)-1)]
        display.show(imagenes_aleatoria)
    if button_b.was_pressed():
        musica_aleatoria = musica[random.randint(0,len(musica)-1)]
        music.play(musica_aleatoria)    

