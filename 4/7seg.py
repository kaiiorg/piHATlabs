#!/usr/bin/python
#Lab 4: Using a shift register
#Import the time and sys modules
import time, sys
#Import the RPi.GPIO module
import RPi.GPIO as GPIO
#Select the BCM mode
GPIO.setmode(GPIO.BCM)

#Pins for shift register
dataPin = 17
clockPin = 27
latchPin = 22

#Segment data to show the digit 0 to 9 on the 7 segment display
segments = [0xFC, 0x60, 0xDA, 0xF2, 0x66, 0xB6, 0x3E, 0xE0, 0xFE, 0xF6]

#function for driving the shift register
#assumes the dataPin and clockPin have already been setup
#Only does the 8 LSB of output
def	shiftOut(dataPin, clockPin, output, msbFirst):
	GPIO.output(dataPin, GPIO.LOW)
	GPIO.output(clockPin, GPIO.LOW)
	
	
	mask = 1
	if(msbFirst):
		mask <<= 7
		c = 7;
		print(output)
		while c >= 0:
			GPIO.output(dataPin, ((mask & output) >> c) == 1)
			GPIO.output(clockPin, GPIO.LOW)
			time.sleep(0.0001)
			GPIO.output(clockPin, GPIO.HIGH)
			time.sleep(0.0001)
			GPIO.output(clockPin, GPIO.LOW)
			mask >>= 1
			c-= 1
	else:
		c = 0
		while c < 8:
			GPIO.output(dataPin, ((mask & output) >> c) == 1)
			GPIO.output(clockPin, GPIO.LOW)
			time.sleep(0.0001)
			GPIO.output(clockPin, GPIO.HIGH)
			time.sleep(0.0001)
			GPIO.output(clockPin, GPIO.LOW)
			mask <<= 1
			c+= 1
	return

#toggle the latch line
#assumes it is already setup
def latch(latchPin):
	GPIO.output(latchPin, GPIO.LOW)
	time.sleep(0.0001)
	GPIO.output(latchPin, GPIO.HIGH)
	time.sleep(0.0001)
	GPIO.output(latchPin, GPIO.LOW)



#Setup the data, clock, and latch pins
GPIO.setup(dataPin, GPIO.OUT)
GPIO.output(dataPin, GPIO.LOW)
GPIO.setup(clockPin, GPIO.OUT)
GPIO.output(clockPin, GPIO.LOW)
GPIO.setup(latchPin, GPIO.OUT)
GPIO.output(latchPin, GPIO.LOW)


while True:
	try:
		for segment in segments:
			shiftOut(dataPin, clockPin, segment, False)
			latch(latchPin)
			time.sleep(0.25)
			shiftOut(dataPin, clockPin, segment | 1, False)
			latch(latchPin)
			time.sleep(0.25)
	except KeyboardInterrupt:
			shiftOut(dataPin, clockPin, 0, False)
			latch(latchPin)
			break
	
GPIO.cleanup()