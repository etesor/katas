# Substraction.
# If the result is 0, turn on 2 leds, if not, turn on 1 led.
# This migh seem simple, but the idea was to re-write assembly code into python to prove the abismal difference between that technology.


def subs_led(a, b):
    total = a - b
    if total == 0:
        return True
        # Turn on 2 leds
    return False
    # Turn on 1 led


print(subs_led(5,4))