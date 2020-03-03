#!/bin/bash

UserName=$(whoami)

function main {
  cd /home/pi/mamdau2

  #echo "test!!!" > TEST.txt
#  sudo python3 mkdirs.py "/home/$(UserName)/Desktop/Mamdau2DATA"
  sudo python3 uvsensor.py "/home/$(UserName)/Mamdau2DATA/UVsensorDATA.txt"
}
#################
main
##########
