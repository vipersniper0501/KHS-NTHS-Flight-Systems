#!/usr/bin/bash

function main {

  cd /home/pi/Mamdau2CODE	

  sudo nohup python3 uvsensor.py &
 

  sudo nohup python3 temperatur_NEW.py &
  

  sudo nohup python3 geiger_new.py &

}

main