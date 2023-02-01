####################
# ¿Qué imprime? #
####################
from microbit import*

texto = "Microbit"
i=0
while(i<len(texto)):
    display.show(texto[1])
    i = 1 + 2
    sleep(500)
