#!/bin/bash

#Purpose - 
#If you access your Raspberry Pi over SSH and felt a need to copy files from Raspi to local machine frequently,
#then this utility can save some time for you

#Assumptions -
#This utility is tested for Mac OS only
#Raspberry Pi SSH Server is enabled - On Raspberry Pi 3 it is disabled by default
#Documentation - https://www.raspberrypi.org/documentation/remote-access/ssh/

#Script requires another file to expose environment variables
#Create a regular file. Name it "set_envs.sh"
#Content - export KD_RASPI_USER="your_ssh_user_name" && export KD_RASPI_SERVER="ip_address_of_your_raspberry_pi"

function usage {
	echo "Usage: "
	echo "$0 /home/pi/test.jpg"
}

#Take file name as first argument
if [ $# -ne 1 ]; then
	usage
	exit 1
fi

function usage {
	echo "$0 /home/pi/test.jpg"
}

#Source env file
source ./set_envs.sh

if [ -z "$KD_RASPI_SERVER" ]; then
	echo "set environment variable KD_RASPI_SERVER"
	exit 1
fi

if [ -z "$KD_RASPI_USER" ]; then
	echo "set environment variable KD_RASPI_USER"
	exit 1
fi

file_name=$1 #File to copy from raspberry pi server
raspi_server=${KD_RASPI_SERVER} #Reads from environment variable
raspi_user=${KD_RASPI_USER} #Reads from environment variable
dest=/tmp/${basename}

scp ${raspi_user}@${raspi_server}:${file_name} ${dest} && \
	open ${dest}
