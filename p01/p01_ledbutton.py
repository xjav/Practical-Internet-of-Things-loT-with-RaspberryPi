# USER STORY: The user can operate a LED with a button.
#             The led will be off at startup and if the user presses the button the LED will blink three times and it will turn off.
# COURSE:     Practical Internet of Things (loT) with RaspberryPi
#             [https://miriadax.net/web/practical-internet-of-things-lot-with-raspberrypi]
# MODULE:     1. Introduction to Raspberry
# ACTIVITY:   Practical exercise (GITHUB????)
# BY:         Xavier Vidal
# PYTHON:     2.7


import RPi.GPIO as GPIO
import time

# CIRCUIT DIAGRAM ??????

# BOARD CONFIGURATION https://pinout.xyz/
GPIO_REFERENCE= GPIO.BCM
PINLED= 4       # 04 BCM (PIN BOARD 07)
PINBUTTON= 18   # 18 BCM (PIN BOARD 12)

# GPIO SETUP
GPIO.setmode(GPIO_REFERENCE)
GPIO.setup(PINLED, GPIO.OUT)
GPIO.setup(PINBUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP) # state true= DOWN BUTTON // false= UP BUTTON

# GPIO INITIAL STATE
GPIO.output(PINLED, False)  # PINLED off 

while True:
    input_state= GPIO.input(PINBUTTON)
    if input_state == False:
        for i in range(3):
            GPIO.output(PINLED, True)   # PINLED on
            time.sleep(0.7)
            GPIO.output(PINLED, False)  # PINLED off  
            time.sleep(0.7)

