#!/usr/bin/python3

"""
Purpose - To demonstrate how to perform some action when connected sound sensor detects sound
"""

import RPi.GPIO as GPIO
import time

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    print("Sound detected")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #Detect when pin goes high or low
GPIO.add_event_callback(channel, callback) #Assign function to GPIO Pin, Run function on change

#Infinite Loop
while True:
    time.sleep(1)
