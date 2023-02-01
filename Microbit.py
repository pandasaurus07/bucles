####################
# ¿Qué imprime? #
####################
from microbit import*

texto = "Microbit"
i=0
while(i<len(texto)):
    display.show(texto[i])
    i = i + 1
    sleep(500)
