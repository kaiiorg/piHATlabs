#!/usr/bin/python
#Lab 3: 

#import time.sleep
from time import sleep

#Import the RPi.GPIO module
import RPi.GPIO as GPIO
#Select the BCM mode
GPIO.setmode(GPIO.BCM)

#The BCM pin number of LED0
LED0 = 13
#Setup the LED0 pin as an output
GPIO.setup(LED0, GPIO.OUT)

#Make sure that the LED0 is turned off
GPIO.output(LED0, GPIO.LOW)

#Loop indefinitely
while True:
	try:
		GPIO.output(LED0, GPIO.HIGH)
		sleep(0.5)
		GPIO.output(LED0, GPIO.LOW)
		sleep(0.5)
		
	except KeyboardInterrupt:
		GPIO.output(LED0, GPIO.LOW)
		break

GPIO.cleanup()