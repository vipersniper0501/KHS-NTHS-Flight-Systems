#!/bin/bash

# Make sure to place this in the Documents directory of your raspberry pi otherwise you will have to make some manual changes to the code.

IMGDIR='/home/pi/images'

while true; do
    TIME=$(date +%s)
    FILENAME=$IMGDIR/${TIME}.jpg
    raspistill -o $FILENAME -w 1024 -h 768 -n
    echo "Picture taken"
    sleep 60
done
