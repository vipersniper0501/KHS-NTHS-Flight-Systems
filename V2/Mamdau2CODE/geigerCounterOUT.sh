#!/bin/bash

function start {
  sudo touch /home/pi/Mamdau2DATA/geigertest.txt
  while [ true ]; do
    cat /dev/ttyAMA0 > /home/pi/Mamdau2DATA/geigertest.txt
    sleep 5s
  done
}

function start2 {
	sudo touch /home/pi/Mamdau2DATA/geigertest.txt	
	while read line
	do
		echo "$lin2e" >> /home/pi/Mamdau2DATA/geigertest.txt
		echo >> /home/pi/Mamdau2DATA/geigertest.txt
		sleep 1s
	done
}

start

#start2
