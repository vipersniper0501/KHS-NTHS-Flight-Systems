import time
import board
import busio
import adafruit_veml6075
import os
import sys

i2c = busio.I2C(board.SCL, board.SDA)

veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)

filepath = sys.argv[1]

def start_script():
    file=open(filepath, 'w+')

    while True:
        file.write(str(veml.uv_index))
        time.sleep(1)
    else:
        file.close()

start_script()
