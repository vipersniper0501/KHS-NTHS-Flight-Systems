#!/bin/bash

function main {
  cd /home/pi/Mamdau2CODE

  sudo nohup python3 uvsensor.py &
  sudo nohup python3 temperatur.py &
  sudo nohup python3 geiger_new.py &

}
#################
main
##########
