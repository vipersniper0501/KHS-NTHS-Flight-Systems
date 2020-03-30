import time
import board  # are required to connect to UV sensor. If there is an error saying cannot import, then you must manually install the modules to the pi
import busio  # are required to connect to UV sensor. If there is an error saying cannot import, then you must manually install the modules to the pi
import adafruit_veml6075  # are required to connect to UV sensor. If there is an error saying cannot import, then you must manually install the modules to the pi
import os
import sys
import datetime
import csv

i2c = busio.I2C(board.SCL, board.SDA)

veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)

#filepath = sys.argv[1]


def main():
    with open('/home/pi/Mamdau2DATA/UVsensorData.csv', 'a+') as f: # opens file UVsensorDATA.txt to add data

        f.write('UV Data')
        f.write(',')
        f.write('Hour Minute Second')
        f.write(' ')
        f.write('\n')
        f.close()

        while True:
            try:
                with open('/home/pi/Mamdau2DATA/UVsensorData.csv', 'a+') as f:
                    now = datetime.datetime.now()
                    f.write('%.5f' % veml.uv_index)
                    f.write(',')
                    f.write(now.strftime("%H:%M:%S"))
                    f.write(' ')
                    f.write('\n')  # writes data to the Hundred-Thouasandths place and outputs to file UVsensorDATA.txt and creates new line
                    print(veml.uv_index)
                    f.close()
                    time.sleep(1)  # time interval between data outputs
            except KeyboardInterrupt:
                f.close()
                print('File Closed')
                sys.exit(0)


if __name__ == '__main__':
    main()
