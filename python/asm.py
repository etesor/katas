# Resta dos números.
# Si el resultado es 0, se enciende un led. Si es diferente de 0 se encienden 2 leds.


def subs_led(a, b):
    total = a - b
    if total == 0:
        return True
    return False


print(subs_led(5,4))