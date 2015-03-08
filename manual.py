#!/usr/bin/env python

import cv2, sys, time, os
import KeyboardPoller
from pantilt import *
from time import sleep
import RPi.GPIO as GPIO ## Import GPIO library

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setwarnings(False)

# Default Pan/Tilt for the camera in degrees.
# Camera range is from 0 to 180
cam_pan = 110
cam_tilt = 90

# Turn the camera to the default position
pan(cam_pan)
tilt(cam_tilt)

KeyboardPoller.WaitKey().thread.start()

while True:
   #key handler
   if KeyboardPoller.keypressed.isSet():  
      if KeyboardPoller.key=="a":
         print "A"
	 cam_pan=cam_pan+10
      if KeyboardPoller.key=="d": #quit
         print "D"
	 cam_pan=cam_pan-10
      if KeyboardPoller.key=="w": #quit
	 print "W"
         cam_tilt=cam_tilt+10
      if KeyboardPoller.key=="s": #quit
	 print "S"
         cam_tilt=cam_tilt-10
      if KeyboardPoller.key=="f": #quit
         print "firing" 
	 GPIO.setup(18, GPIO.OUT) ## Setup GPIO Pin 24 to OUT
	 GPIO.output(18,True) ## Turn on GPIO pin 24
	 sleep(2)
	 GPIO.output(18,False) ## Turn off GPIO pin 24
	 print "fired"
      if KeyboardPoller.key=="b": #spray
         print "firing left"
	 pan(5)
	 tilt(130)
	 GPIO.setup(18, GPIO.OUT) ## Setup GPIO Pin 24 to OUT
	 GPIO.output(18,True) ## Turn on GPIO pin 24
	 pan(170)
	 tilt(130)
	 sleep(2)
	 GPIO.output(18,False) ## Turn off GPIO pin 24
      if KeyboardPoller.key=="n": #spray
	 print "firing right"
         pan(90)
	 tilt(130)
	 GPIO.setup(18, GPIO.OUT) ## Setup GPIO Pin 24 to OUT
	 GPIO.output(18,True) ## Turn on GPIO pin 24
	 pan(35)
	 tilt(130)
	 sleep(2)
	 GPIO.output(18,False) ## Turn off GPIO pin 24

      if KeyboardPoller.key==" ": #reset all
         cam_pan=110
         cam_tilt=90
         print "Reset."
   KeyboardPoller.WaitKey().thread.start()
   pan(cam_pan)
   tilt(cam_tilt)
