import RPi.GPIO as GPIO
import time
push_file_path = "button_file.txt"
pin_for_button_input = 18

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_for_button_input,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

x = 1
while x < 10:
    if GPIO.input(pin_for_button_input):
        push_file = open(push_file_path, "w")
        push_file.write("1")
        push_file.close()
        print("1")
    x = x+1
    time.sleep(0.1)