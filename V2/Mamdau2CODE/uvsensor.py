import time
import board #are required to connect to UV sensor. If there is an error saying cannot import, then you must manually install the modules to the pi
import busio #are required to connect to UV sensor. If there is an error saying cannot import, then you must manually install the modules to the pi
import adafruit_veml6075 #are required to connect to UV sensor. If there is an error saying cannot import, then you must manually install the modules to the pi
import os
import sys
import datetime


i2c = busio.I2C(board.SCL, board.SDA)

veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)



filepath = sys.argv[1]

def start_script():
    file=open(filepath, 'w+') #opens file UVsensorDATA.txt to add data

    file.write('UV Data          H  M  S\n')

    while True:
        now = datetime.datetime.now()
        file.write('%.5f' % veml.uv_index + "          " + now.strftime("%H:%M:%S") + "\n") #writes data to the Hundred-Thouasandths place and outputs to file UVsensorDATA.txt and creates new line
        time.sleep(1) #time interval between data outputs
    else:
        file.close() #"Closes" file

start_script() 
