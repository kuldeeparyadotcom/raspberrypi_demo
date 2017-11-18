#!/usr/bin/python3

"""
Purpose - Click picture using Raspberry pi 3 Camera module
Assumptions - 
1. Camera module is enabled
   If not, run command sudo raspi-config and enabled camera
2. python-picamera is installed
   If not, run the following command - sudo apt-get -y update && sudo apt-get install -y python3-picamera
Documentation - https://www.raspberrypi.org/documentation/usage/camera/python/README.md
"""

import picamera
import datetime
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG)

logging.debug("Starting program")
OUTPUT_DIR="/tmp/picamera_pics" #Directory where images would be stored

#Check if OPUTPUT_DIR exists
if not os.path.exists(OUTPUT_DIR):
    print("OUTPUT_DIR: ", OUTPUT_DIR, "does not exists so creating one")
    os.mkdir(OUTPUT_DIR)

#Check if OUTPUT_DIR is a directory
if not os.path.isdir(OUTPUT_DIR):
    print("OUTPUT_DIR: ", OUTPUT_DIR, "must be a directory to get images saved")
    print("Exiting.. ")
    sys.exit(1) #Exit with non-zero error code

#check if program does have write acces to the OUTPUT_DIR
if not os.access(OUTPUT_DIR, os.W_OK):
    print("It seems, program can not write images to: ", OUTPUT_DIR)
    print("Fix file permissions and try again! Exiting.. ")
    sys.exit(1) #Exit with non-zero error code

logging.debug("pictures will be saved to: %s" % OUTPUT_DIR)
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
logging.debug("timestamp captured: %s" % timestamp)
image_name="python_clicked_" + timestamp + ".jpg" #Dynamically generated name using timestamp
image_dest = os.path.join(OUTPUT_DIR, image_name)
logging.debug("image name would be: %s" % image_dest)

logging.debug("Making an attempt to click picture")
camera = picamera.PiCamera()
logging.debug("clicked")
camera.capture(image_dest) #Assumption - image is saved as test.jpg
logging.debug("Program completed")
