#!/usr/bin/python
#Lab 3: 

#import time.sleep
from time import sleep

#Import the RPi.GPIO module
import RPi.GPIO as GPIO
#Select the BCM mode
GPIO.setmode(GPIO.BCM)

#List of BCM pin numbers of the buttons
buttons = [16, 26, 20, 21]
#Setup the button pins
for button in buttons:
	GPIO.setup(button, GPIO.IN)

#Counter variable
i = 0

#Loop indefinitely
while True:
	try:
		#Check to see if each button has been pressed, output the number of button that was pressed.
		while i < 4
			if GPIO.input(buttons[i]) != GPIO.LOW:
				print(str.format("You pressed button {0}!", i))
				#Debounce
				time.sleep(0.01)
			i += 1
		i = 0
	except KeyboardInterrupt:
		break

GPIO.cleanup()