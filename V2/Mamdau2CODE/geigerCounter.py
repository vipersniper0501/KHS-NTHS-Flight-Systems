import os
import serial
import time

filepath = "/home/pi/Mamdau2DATA/geigerCounterOutput.txt"
#ser = serial.Serial(port='/dev/ttyAMA0', baudrate=9600)
#data = ser.read(100)



def main():
  ser = serial.Serial(port='/dev/ttyAMA0', timeout=0, exclusive=True)
  with open(filepath, 'wb+') as f:
      print('file opened')
      while True:
        print('While loop starting')
        try:
            if not ser.is_open:
                ser.open()
                print('reopened port')
            data = ser.readline()
            print(data)
            f.write(data)
            print('wrote data')
        except serial.SerialException as e:
            ser.close()
            time.sleep(5)
            print('Error:')
            print(e)
       #time.sleep(1)
        print('repeat')



main()
