# Imports go at the top
from microbit import *
import music

lstNotas = ['g:1', 'g:1', 'a:2', 'g:2', 'c:2', 'b:3', 'g:1', 'g:1', 'a:2', 'g:2', 'D:2']

music.play(lstNotas, wait=False, loop=True)

while True:
    display.show(Image.ANGRY)
    sleep(1000)
    display.show(Image.SNAKE)
    sleep(1000)
