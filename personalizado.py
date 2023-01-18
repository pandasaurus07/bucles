from microbit import *
n = 1
borde = Image("95059:95059:98089:95059:95059")
interior = Image("05950:05950:00900:05950:05950")
while n <= 10:
    if n %2 == 0:
        display.show(borde)
    else:
        display.show(interior)
    sleep(500)
    n += 1
