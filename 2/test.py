#!/usr/bin/python
#Lab 2: Test the HAT
#Import the time and sys modules
import time, sys
#Import the RPi.GPIO module
import RPi.GPIO as GPIO
#Select the BCM mode
GPIO.setmode(GPIO.BCM)

#List of BCM pin number of the LEDs, in 0 to 7 order
LEDs = [13, 12, 19, 6, 5, 25, 24, 23]

#Pins for shift register
dataPin = 17
clockPin = 27
latchPin = 22

#Segment data to show the digit 0 to 9 on the 7 segment display
segments = [0xFC, 0x60, 0xDA, 0xF2, 0x66, 0xB6, 0x3E, 0xE0, 0xFE, 0xF6]

#List of BCM pin numbers of the buttons
buttons = [16, 26, 20, 21]

#function for driving the shift register
#assumes the dataPin and clockPin have already been setup
#Only does the 8 LSB of output
def	shiftOut(dataPin, clockPin, output):
	GPIO.output(dataPin, GPIO.LOW)
	GPIO.output(clockPin, GPIO.LOW)
	
	msbFirst = False
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

#Setup the button pins
for button in buttons:
	GPIO.setup(button, GPIO.IN)

#Setup the data, clock, and latch pins
GPIO.setup(dataPin, GPIO.OUT)
GPIO.output(dataPin, GPIO.LOW)
GPIO.setup(clockPin, GPIO.OUT)
GPIO.output(clockPin, GPIO.LOW)
GPIO.setup(latchPin, GPIO.OUT)
GPIO.output(latchPin, GPIO.LOW)

#Setup the pins as outputs and make sure they're turned off
for LED in LEDs:
	GPIO.setup(LED, GPIO.OUT)
	GPIO.output(LED, GPIO.LOW)

#Turn all the LEDs on, wait, then turn them back off.
print("Turning LEDs on")
for LED in LEDs:
	GPIO.output(LED, GPIO.HIGH)
	time.sleep(0.1)
time.sleep(1)
print("Turning LEDs off")
for LED in LEDs:
	GPIO.output(LED, GPIO.LOW)
	time.sleep(0.1)

print("Testing PWM on LED0 and LED1")
#Test PWM
pwm0 = GPIO.PWM(13, 1000)
pwm1 = GPIO.PWM(12, 1000)
pwm0.start(0)
pwm1.start(0)
i = 0
while i <= 100:
	pwm0.ChangeDutyCycle(i)
	pwm1.ChangeDutyCycle(i)
	i += 10
	time.sleep(0.25)
pwm0.stop()
pwm1.stop()

print("Testing shift register and 7 segment display")
c = 0
for segment in segments:
	print("\t" + str(c))
	shiftOut(dataPin, clockPin, segment)
	latch(latchPin)
	time.sleep(0.5)
	shiftOut(dataPin, clockPin, segment | 1)
	latch(latchPin)
	c+=1
	time.sleep(0.5)

#Turn all segments off
time.sleep(1)
shiftOut(dataPin, clockPin, 0)
latch(latchPin)


#Test the buttons
c = 0
while c < 4:
	print("Press button " + str(c) + " (press ctrl+c if it doesn't respond.)")
	#Keep checking for a button press
	try:
		while GPIO.input(buttons[c]) != GPIO.LOW:
			#debounce
			time.sleep(0.01)
	except KeyboardInterrupt:
		print("Skipping button " + str(c))
	c+= 1

GPIO.cleanup()