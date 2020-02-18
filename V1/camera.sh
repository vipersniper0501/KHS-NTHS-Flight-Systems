#!/bin/bash
PICSDIR=/etc/Moore_Flight_Coomputer/Pictures  #sends pictures to the folder pictures on Pi
while true; do #creates 
	#DATE=`date +%Y%m%d`
	#HOUR=`date +%H%M%S`
	raspistill -o $PICSDIR/`date +%s`.jpg
	sleep 30 #waits 30 seconds before continuing
done
