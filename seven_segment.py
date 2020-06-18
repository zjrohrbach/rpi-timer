import RPi.GPIO as GPIO
import time

segment_pins  = [20,  21,  26,  19,  13,  12,  16]
segment_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
GPIO.setmode(GPIO.BCM)


digits = [
    'abcdef',   #0 
    'bc',       #1
    'abdeg',    #2
    'abcdg',    #3
    'bcfg',     #4
    'acdfg',    #5
    'acdefg',   #6
    'abc',      #7
    'abcdefg',  #8
    'abcfg',    #9
]

def clear_all_segments():
    for x in segment_pins:
        GPIO.output(x, GPIO.LOW)

def set_digit(x):
    clear_all_segments()
    segments_to_light = digits[x]
    i = 0
    while i < len(segment_names):
        if segments_to_light.find(segment_names[i]) != -1:
            GPIO.output(segment_pins[i], GPIO.HIGH)
        i = i + 1
    


for x in segment_pins:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x, GPIO.LOW)

for x in segment_pins:
    GPIO.output(x, GPIO.HIGH)
    time.sleep(.1)

j = 0
while j < 10:
    set_digit(j)
    time.sleep(1)
    j = j+1

GPIO.cleanup()