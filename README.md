## MAMDAU Flight Computer

This repository is for the storage and collaboration of the creation of the MAMDAU Flight computer that is used
for high altitude ballons.

### Devices and Sensors:
(More details on the parts to come later)

- Raspberry Pi Zero (Raspberry Pi 3 works as well
- 3 DS18B20 Temperature Sensors
- 1 Adafruit UV sensor
- Mighty Ohm Geiger Counter
- Adafruit Ozone Sensor
- Power bank that houses 4 double A batteries


##Quick Setup Guide Version 1
###Installation of code on Raspberry Pi:
1. Install Raspian OS on a micro-sd card and insert the micro-sd card into the raspberry pi zero
2. Put installation code for the Moore Flight computer on a flash drive
3. Insert flash drive into Raspberry Pi
4. Using file manager equivalent on Raspberry Pi to find directory containing the system code.
5. Once found on the flash drive, open current location with terminal
6. once in the terminal, unpack the folder using `sudo tar -xvzf MFP-0.3.tar.gz`
7. once unpacked, in terminal type `cd MFP-0.3/MFP-0.3-src` to get to the directory containing the install file
8. Type `./install.sh` to install the new version of Moore Flight Computer code

###Installation of code on Arduino:
1. Open up Arduino code in the arduino IDE program.
2. In Tools in the editor, you will need to Select the correct Port the Arduino is on.
3. Push the reset button on the Arduino and click the Upload button in the IDE
4. Unless an error pops up the code should have updated successfully.
5. If all else fails, google is your friend.


###How to start recording data:
1. Place the batteries in the pack
2. Make sure all components are properly connected
3. Make sure the micro-sd card is inserted into the raspberry pi zero
4. Switch on the battery pack and wait about a minute for the system to record data 


###How to retrieve data
1. Switch off the power from the battery back
2. Remove the micro-sd card from the raspberry pi zero
3. Open the micro-sd card on a linux device (the filesystem cannot be opened on a Windows
device)

**Insert Schematics Here**


