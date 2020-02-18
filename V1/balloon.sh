#!/bin/bash
chmod +x /etc/Moore_Flight_Computer/camera.sh #makes the file camera.sh executable
chmod +x /etc/Moore_Flight_Computer/data.sh #makes the file data.sh executable
/etc/Moore_Flight_Computer/camera.sh & 
disown
/etc/Moore_Flight_Computer/data.sh &
