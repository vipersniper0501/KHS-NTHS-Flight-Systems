#!/bin/bash

# Starts up the raspberry pi cameras
# Make sure to have a cron job run this @reboot
# Example of cron setup: @reboot /home/pi/Documents/start_up.sh

screen -d -m sh /home/pi/Documents/take_picture.sh
