#!/bin/bash

function main {
  cd /home/pi/Mamdau2CODE

  screen -S UVdata -md sudo python3 uvsensor.py
  screen -S Temp -md sudo python3 temperatur.py
  screen -S Radiation -md sudo python3 geiger_new.py
  
}
#################
main
##########
