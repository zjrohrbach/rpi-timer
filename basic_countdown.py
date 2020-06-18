import digit_handling_functions as dh
import RPi.GPIO as GPIO


x = 0
while x < 30:
    dh.iterate_digit_down(0)
    dh.output()
    x = x + 1
    dh.time.sleep(1)

GPIO.cleanup()