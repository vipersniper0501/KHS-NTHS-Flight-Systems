#!/bin/bash
sudo killall gpsd
sleep 1
sudo systemctl stop gpsd.socket
sleep 2
sudo systemctl disable gpsd.socket
sleep 2
sudo gpsd /dev/ttyUSB1 -F /var/run/gpsd.socket
sleep 3
lxterminal -e cgps
sleep 3

lxterminal -e python3 /home/pi/Documents/geiger.py
sleep 1
lxterminal -e python3 /home/pi/Documents/specOzone.py
sleep 5
pkill -f specOzone.py
sleep 3
lxterminal -e python3 /home/pi/Documents/specOzone.py 
sleep 3
lxterminal -e python3 /home/pi/Documents/uvsensor.py
sleep 3
lxterminal -e python3 /home/pi/Documents/mamdau_V4.py

while true
	do
		sleep 60
		pkill -f uvsensor.py
		sleep 1
		lxterminal -e python3 /home/pi/Documents/uvsensor.py
	done 
