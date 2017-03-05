#!/usr/bin/python
#Lab 3: 

#import time.sleep
from time import sleep

#Import the RPi.GPIO module
import RPi.GPIO as GPIO
#Select the BCM mode
GPIO.setmode(GPIO.BCM)

#List of BCM pin number of the LEDs, in 0 to 7 order
LEDs = [13, 12, 19, 6, 5, 25, 24, 23]

#Setup the pins as outputs and make sure they're turned off
for LED in LEDs:
	GPIO.setup(LED, GPIO.OUT)
	GPIO.output(LED, GPIO.LOW)

#Counter variable
i = 0

#Loop indefinitely
while True:
	try:
		while i < 7:
			#Turn the current LED off
			GPIO.output(LEDs[i], GPIO.LOW)
			#Turn the next LED on
			GPIO.output(LEDs[i + 1], GPIO.HIGH)
			sleep(0.1)
			#Increment the counter
			i += 1
		
		while i > 0 :
			#Turn the current LED off
			GPIO.output(LEDs[i], GPIO.LOW)
			#Turn the next LED on
			GPIO.output(LEDs[i - 1], GPIO.HIGH)
			sleep(0.1)
			#Decrement the counter
			i -= 1
		
	except KeyboardInterrupt:
		for LED in LEDs:
			GPIO.output(LED, GPIO.LOW)
		break

GPIO.cleanup()
