#!/bin/bash

lxterminal -e python3 /home/pi/Documents/uvsensor.py
sleep 1

while true
	do
		sleep 60
		pkill -f uvsensor.py
		sleep 1
		lxterminal -e python3 /home/pi/Documents/uvsensor.py
	done 
