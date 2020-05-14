


____________________________________________________________________

# MAMDAU Flight Computer 

____________________________________________________________________

## Info/Description:

This repository is for the storage and collaboration of the creation of the MAMDAU Flight computer that is used
for high altitude ballons.

____________________________________________________________________

## Prerequisits:

#### Devices and Sensors for Version 2:

- 1x Raspberry Pi Zero (Raspberry Pi 3 works as well)
- 3x DS18B20 Temperature Sensors
- 1x VEML 6075 UV sensor
- 1x Mighty Ohm Geiger Counter
- 1x DGS-O3 968-042 Ozone Sensor
- 1x Adafruit Real Time Clock
- 1x USB-A to Micro-USB
- 1x Power bank that houses 4 double A batteries

#### Devices and Sensors for Version 1:

- 1x Raspberry Pi Zero
- 1x Arduino UNO
- 3x TMP 36 Temperature Sensors
- 1x Raspberry Pi Camera
- 1x VEML 6075 UV Sensor

____________________________________________________________________

## Warnings:

1. Ensure that the schematics have been followed properly
2. Be careful running commands as root on the Raspberry Pi
3. Follow installation instructions carefully 
4. **IMPORTANT! DO NOT TOUCH THE UNDERSIDE OF THE GEIGER COUNTER WHILE IT IS TURNED ON!** If the underside of the Geiger Counter is touched while it is turned on you will short circuit it and damage the capacitors and resitors!

____________________________________________________________________

## Installations:

### Quick Setup Guide Version 2

#### Installation of code on Raspberry Pi:

1. Install Raspian OS on a micro-sd card
2. Put Micro-SD card into a flash drive and open it on a Raspbery Pi that you can easily access the OS on.
3. Create the following directories in `/home/pi/`: `/Mamdau2DATA` and `/Mamdau2CODE`
4. Once those are made copy the `V2` source code and place into `/home/pi/Mamdau2CODE`
5. After those have been succesfully placed open the Terminal
6. In the Terminal type the following: `sudo crontab -e` and choose the editor of your choice
7. Once you have typed the command you should have gotten something that says at the top: `Edit this file to introduce tasks to be run by cron.` In here type the following: `@reboot sudo bash /home/pi/Mamdau2CODE/services_start.sh`
8. Save
9. Now unplug the Micro-SD card that you have been working on from the Raspberry Pi and now plug it into the Pi that you will be using for the launch.
10. Plug in the power and the Pi will automatically start collecting data. 

#### How to start recording data:

1. Place batteries inside Geiger Counter
2. Make sure all components are properly connected
3. Make sure the micro-sd card is inserted into the raspberry pi zero
4. Turn on Geiger Counter first
5. Switch on the battery pack and wait about a minute for the system to start recording data 

#### How to retrieve data

1. Switch off the power from the battery back
2. Switch off the power on the Geiger Counter
3. Remove the micro-sd card from the raspberry pi zero
4. Open the micro-sd card on a linux device (the filesystem cannot be opened on a Windows device)
5. The location of data should be under `/home/pi/Mamdau2DATA/`

____________________________________________________________________

### Quick Setup Guide Version 1

#### Installation of code on Raspberry Pi:

1. Install Raspian OS on a micro-sd card and insert the micro-sd card into the raspberry pi zero
2. Put installation code for the Moore Flight computer on a flash drive
3. Insert flash drive into Raspberry Pi
4. Using file manager equivalent on Raspberry Pi to find directory containing the system code.
5. Once found on the flash drive, open current location with terminal
6. once in the terminal, unpack the folder using `sudo tar -xvzf MFP-0.3.tar.gz`
7. once unpacked, in terminal type `cd MFP-0.3/MFP-0.3-src` to get to the directory containing the install file
8. Type `./install.sh` to install the new version of Moore Flight Computer code

#### Installation of code on Arduino:

1. Open up Arduino code in the arduino IDE program.
2. In Tools in the editor, you will need to Select the correct Port the Arduino is on.
3. Push the reset button on the Arduino and click the Upload button in the IDE
4. Unless an error pops up the code should have updated successfully.
5. If all else fails, google is your friend.

#### How to start recording data:

1. Place the batteries in the pack
2. Make sure all components are properly connected
3. Make sure the micro-sd card is inserted into the raspberry pi zero
4. Switch on the battery pack and wait about a minute for the system to record data 

#### How to retrieve data

1. Switch off the power from the battery back
2. Remove the micro-sd card from the raspberry pi zero
3. Open the micro-sd card on a linux device (the filesystem cannot be opened on a Windows device)
4. The location of data should be around where the systems code is













