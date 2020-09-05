#!/usr/bin/python
import time
import board
import busio
import adafruit_veml6075
import datetime
import os
import sys
import csv
import threading
import asyncio
from threading import Timer,Thread,Event
from gps import *

filepath = "/home/pi/mamdau2data/mamdau_data_acquisition.csv"


timerInterval = 4 # Timerinterval in Sekunden


varTempA = 0 # DS1820-sensor 1 
varTempB = 0 # DS2018-sensor 2
varTempC = 0 # DS1820-sensor 3
varUVIndex = 0 # UX-index from veml6075
varUva = 0 # UVa from veml6075
varUvb = 0 # UVb from veml6075
varLat = 0 # GPS-data latitude (unit: decimal degree)
varLon = 0 # GPS-data longitude (unit: decimal degree)
varAlt = 0 # GPS-data altitude (unit: m)
varSpd = 0 # GPS-data speed (unit: m/s)
varCli = 0 # GPS-data climb (unit: m/min)
varUtc = 0 # GPS-data UTC-time
varCpm = 0 # Geiger-counter counts per minute
varCps = 0 # Geiger-counter counts per second
varUsv = 0 # Geiger-counter uSv/hr
gasPpb = 0 # Ozonconcentration in ppb
gasTmp = 0 # temperature from gas-sensor in Celsius
gasHum = 0 # relative humidity from gas-sensor

# Temperature-Sensors DS1820 (path)
TS_A = '/sys/bus/w1/devices/28-000004b8a26d/w1_slave'
TS_B = '/sys/bus/w1/devices/28-000004b8fb4c/w1_slave'
TS_C = '/sys/bus/w1/devices/28-000004b91a2d/w1_slave'


# Start GPS
gpsd = None #setting the global variable

class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd #bring in the scope
        gpsd = gps(mode=WATCH_ENABLE) #starting the stream
        self.current_value = None
        self.running = True
    
    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next()
            time.sleep(0.75)

# Timer for data acquisition
class perpetualTimer():
    def __init__(self,t,hFunction):
        self.t=t
        self.hFunction = hFunction
        self.thread = Timer(self.t,self.handle_function)
    
    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t,self.handle_function)
        self.thread.start()
        
    def start(self):
        self.thread.start()
        
    def cancel(self):
        self.thread.cancel()


    

def readTempSensor(sensorName):
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    return lines

def readTempLines(sensorName):
    
    lines = readTempSensor(sensorName)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.1)
        lines = readTempSensor(sensorName)
    temperaturStr = lines[1].find('t=')
    
    if temperaturStr != -1:
        tempData = lines[1][temperaturStr + 2:]
        tempCelsius = float(tempData) / 1000.0
        tempKelvin = 273 + float(tempData) /1000.0
        tempFahrenheit = float(tempData) / 1000.0 * 9.0 / 5.0 + 32.0
        return[tempCelsius, tempKelvin, tempFahrenheit]

def geiger_cpm():
    csv_path = "/home/pi/mamdau2data/geigerCounter.csv"
    csv_file = open(csv_path, 'r')
    csv_data = csv_file.read()
    csv_file.close()
    
    csv_data = csv_data.splitlines()
    csv_last_value = csv_data[-2].split(',')[4]
    return csv_last_value

def geiger_cps():
    csv_path = "/home/pi/mamdau2data/geigerCounter.csv"
    csv_file = open(csv_path, 'r')
    csv_data = csv_file.read()
    csv_file.close()
    
    csv_data = csv_data.splitlines()
    csv_last_value = csv_data[-2].split(',')[2]
    return csv_last_value

def geiger_usv():
    csv_path = "/home/pi/mamdau2data/geigerCounter.csv"
    csv_file = open(csv_path, 'r')
    csv_data = csv_file.read()
    csv_file.close()
    
    csv_data = csv_data.splitlines()
    csv_last_value = csv_data[-2].split(',')[6]
    return csv_last_value

def gas_ppb():
    csv_path = "/home/pi/mamdau2data/specOzone.csv"
    csv_file = open(csv_path, 'r')
    csv_data = csv_file.read()
    csv_file.close()
    
    csv_data = csv_data.splitlines()
    csv_last_value = csv_data[-2].split(',')[2]
    return csv_last_value

def gas_tmp():
    csv_path = "/home/pi/mamdau2data/specOzone.csv"
    csv_file = open(csv_path, 'r')
    csv_data = csv_file.read()
    csv_file.close()
    
    csv_data = csv_data.splitlines()
    csv_last_value = csv_data[-2].split(',')[3]
    return csv_last_value

def gas_hum():
    csv_path = "/home/pi/mamdau2data/specOzone.csv"
    csv_file = open(csv_path, 'r')
    csv_data = csv_file.read()
    csv_file.close()
    
    csv_data = csv_data.splitlines()
    csv_last_value = csv_data[-2].split(',')[4]
    return csv_last_value

def uv_index():
    csv_path = "/home/pi/mamdau2data/UVsensor.csv"
    csv_file = open(csv_path, 'r')
    csv_data = csv_file.read()
    csv_file.close()
    
    csv_data = csv_data.splitlines()
    csv_last_value = csv_data[-2].split(',')[0]
    return csv_last_value

def uv_a():
    csv_path = "/home/pi/mamdau2data/UVsensor.csv"
    csv_file = open(csv_path, 'r')
    csv_data = csv_file.read()
    csv_file.close()
    
    csv_data = csv_data.splitlines()
    csv_last_value = csv_data[-2].split(',')[1]
    return csv_last_value

def uv_b():
    csv_path = "/home/pi/mamdau2data/UVsensor.csv"
    csv_file = open(csv_path, 'r')
    csv_data = csv_file.read()
    csv_file.close()
    
    csv_data = csv_data.splitlines()
    csv_last_value = csv_data[-2].split(',')[2]
    return csv_last_value

 #write the csv and print on screen
def fileWriter():
    print ("UV-Index: "'%.5f' %varUVIndex )
    print ("UVA: "'%.5f' % varUva)
    print ("UVB: "'%.5f' % varUvb)
    print ("latitude: " , varLat)
    print ("longitude: " , varLon)
    print ("altitude in m: " , varAlt)
    print ("speed in m/s " , varSpd)
    print ("climb in m/min" , varCli)
    print (varUtc)

    
    
    with open (filepath, 'a') as f:
        f.write(str(varUtc))
        f.write(',')
        f.write('{0:0.8f}'.format(varLat))
        f.write(',')
        f.write('{0:0.8f}'.format(varLon))
        f.write(',')
        f.write('{0:0.2f}'.format(varAlt))
        f.write(',')
        f.write('{0:0.2f}'.format(varSpd))
        f.write(',')
        f.write('{0:0.2f}'.format(varCli))
        f.write(',')
        f.write('{0:0.2f}'.format(readTempLines(TS_A)[0]))
        f.write(',')
        f.write('{0:0.2f}'.format(readTempLines(TS_B)[0]))
        f.write(',')
        f.write('{0:0.2f}'.format(readTempLines(TS_C)[0]))
        f.write(',')
        f.write(uv_index())
        f.write(',')
        f.write(uv_a())
        f.write(',')
        f.write(uv_b())
        f.write(',')
        f.write(geiger_cps())
        f.write(',')
        f.write(geiger_cpm())
        f.write(',')
        f.write(geiger_usv())
        f.write(',')
        f.write(gas_ppb())
        f.write(',')
        f.write(gas_tmp())
        f.write(',')
        f.write(gas_hum())
        f.write(' ')
        f.write('\n')
        f.close() 


varUsv = geiger_usv()
varCpm = geiger_cpm()
varCps = geiger_cps()

gpsp = GpsPoller()
gpsp.start()
t = perpetualTimer(timerInterval,fileWriter)
t.start()


    
while True:
    try:
        varLat = gpsd.fix.latitude
        varLon = gpsd.fix.longitude
        varAlt = gpsd.fix.altitude
        varSpd = gpsd.fix.speed
        varCli = gpsd.fix.climb
        varUtc = gpsd.utc
        varUtc = varUtc[11:19]
        time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("Program has ended.")
        sys.exit(0)


  
    