#!/bin/bash

function main {
  cd /home/pi/Mamdau2CODE

  sudo python3 uvsensor.py "/home/pi/Mamdau2DATA/UVsensorDATA.txt"
  sudo python3 temperatur.py
  sudo python3 geigerCounter.py
}
#################
main
##########
