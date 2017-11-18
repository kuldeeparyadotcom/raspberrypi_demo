#!/usr/bin/python3

"""
Purpose - record video using Raspberry pi 3 Camera module
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
import time

logging.basicConfig(level=logging.DEBUG)

logging.debug("Starting program")
OUTPUT_DIR="/tmp/picamera_vidoes" #Directory where videos would be stored
DURATION=10 #Assumption - 10s video will be recorded

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

logging.debug("videos will be saved to: %s" % OUTPUT_DIR)
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
logging.debug("timestamp captured: %s" % timestamp)
video_name="python_recorded_" + timestamp + ".h264" #Dynamically generated name using timestamp
video_dest = os.path.join(OUTPUT_DIR, video_name)
logging.debug("image name would be: %s" % video_dest)

logging.debug("Making an attempt to shoot video")
camera = picamera.PiCamera()
logging.debug("Making attempt to start recording")
camera.start_recording(video_dest)
time.sleep(DURATION) #Capturing video for specified duration
camera.stop_recording()
logging.debug("recording finished")
logging.debug("Program completed")
