#!/bin/bash

#Only use this if the code is not already installed on the Pi

function install {
    sudo mkdir /home/pi/Mamdau2DATA
    sudo mkdir /home/pi/Mamdau2CODE

    sudo cp services_start.sh /home/pi/Mamdau2CODE/services_start.sh
    sudo cp uvsensor.py /home/pi/Mamdau2CODE/uvsensor.py
    sudo cp geiger_new.py /home/pi/Mamdau2CODE/geiger_new.py
    sudo cp temperatur.py /home/pi/Mamdau2CODE/temperatur.py

    sudo python3 -m pip install pyserial
    sudo python3 -m pip install asyncio
    sudo apt-get install python-smbus -y
    sudo apt-get install i2c-tools -y

}

install