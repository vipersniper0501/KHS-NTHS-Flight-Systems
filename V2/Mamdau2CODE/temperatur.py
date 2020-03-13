
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time, sys
import datetime
import csv
 
# Systempfad zum den Sensor, weitere Systempfade könnten über ein Array
# oder weiteren Variablen hier hinzugefügt werden.
# 28-02161f5a48ee müsst ihr durch die eures Sensors ersetzen!

# System path to the sensor, further system paths could be via an array
# or other variables can be added here.
# 28-02161f5a48ee you have to replace with your sensor!
sensor_1 = '/sys/bus/w1/devices/28-000004b91a2d/w1_slave'
sensor_2 = '/sys/bus/w1/devices/'
sensor_3 = '/sys/bus/w1/devices/'
sensor_4 = '/sys/bus/w1/devices/'
 
def readTempSensor(sensorName) :
    """Aus dem Systembus lese ich die Temperatur der DS18B20 aus."""
    """I read the temperature of the DS18B20 from the system bus."""
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def readTempLines(sensorName) :
    lines = readTempSensor(sensorName)
    # Solange nicht die Daten gelesen werden konnten, bin ich hier in einer Endlosschleife
    # As long as the data could not be read, I am in an endless loop
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readTempSensor(sensorName)
    temperaturStr = lines[1].find('t=')
    # Ich überprüfe ob die Temperatur gefunden wurde.
    # I check if the temperature was found.
    if temperaturStr != -1 :
        tempData = lines[1][temperaturStr+2:]
        tempCelsius = float(tempData) / 1000.0
        tempKelvin = 273 + float(tempData) / 1000
        tempFahrenheit = float(tempData) / 1000 * 9.0 / 5.0 + 32.0
        # Rückgabe als Array - [0] tempCelsius => Celsius...
        # Return as an array - [0] tempCelsius => Celsius ...
        return [tempCelsius, tempKelvin, tempFahrenheit]
 
try:
    while True :
        # Mit einem Timestamp versehe ich meine Messung und lasse mir diese in der Console ausgeben.
        # I provide my measurement with a timestamp and have it displayed in the console.
        print("Temperatur um " + time.strftime('%H:%M:%S') +" drinnen: " + str(readTempLines(sensor_1)[0]) + " °C")
        temperature_1 = readTempLines(sensor_1)[0]
        # Nach 10 Sekunden erfolgt die nächste Messung
        # The next measurement takes place after 10 seconds
        

        # Datenlogger
        f= open('logger.txt', 'a')
        f.write(time.strftime('%Y-%m-%d %H:%M:%S'))
        f.write(',')  
        f.write('{0:0.2f}'.format(temperature_1))                                   # Temperatur 
        f.write(' ')                                                                # Abstand/Leerzeichen
        f.write('\n')                                                               # Neue Zeile
        f.close()
        

        # und so weiter
        # and so on
        
        time.sleep(1)
except KeyboardInterrupt:
    # Programm wird beendet wenn CTRL+C gedrückt wird.
    # Program ends when CTRL + C is pressed.
    print('Temperaturmessung wird beendet')
except Exception as e:
    print(str(e))
    sys.exit(1)
finally:
    # Das Programm wird hier beendet, sodass kein Fehler in die Console geschrieben wird.
    # The program ends here so that no error is written to the console.
    print('Programm wird beendet.')
    sys.exit(0)
