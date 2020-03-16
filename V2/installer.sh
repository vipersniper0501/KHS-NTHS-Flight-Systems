#!/bin/bash

#Only use this if the code is not already installed on the Pi

function install {
    sudo mkdir /home/pi/Mamdau2DATA
    sudo mkdir /home/pi/Mamdau2CODE
    sudo cp services_start.sh /home/pi/Mamdau2CODE/services_start.sh
    sudo cp uvsensor.py /home/pi/Mamdau2CODE/uvsensor.py
    suod cp geigerCounter.py /home/pi/Mamdau2CODE/geigerCounter.py
}

install