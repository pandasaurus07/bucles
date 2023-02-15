# Imports go at the top
from microbit import *
import random

vocales =["A", "E", "I", "O", "U"]


vocal_aleatoria = vocales[random.randint(0,len(vocales)-1)]
display.show(vocal_aleatoria)
