#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import sys
from datetime import datetime
import csv


# Systempfad zum den Sensor, weitere Systempfade könnten über ein Array
# oder weiteren Variablen hier hinzugefügt werden.
# 28-02161f5a48ee müsst ihr durch die eures Sensors ersetzen!

# System path to the sensor, further system paths could be via an array
# or other variables can be added here.
# 28-02161f5a48ee you have to replace with your sensor!
sensor_1 = '/sys/bus/w1/devices/28-000004b91a2d/w1_slave'
sensor_2 = '/sys/bus/w1/devices/28-000004b8a26d/w1_slave'
sensor_3 = '/sys/bus/w1/devices/28-000004b8fb4c/w1_slave'



def readTempSensor(sensorName):
    """Aus dem Systembus lese ich die Temperatur der DS18B20 aus."""
    """I read the temperature of the DS18B20 from the system bus."""
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    return lines


def readTempLines(sensorName):
    lines = readTempSensor(sensorName)
    # Solange nicht die Daten gelesen werden konnten, bin ich hier in einer Endlosschleife
    # As long as the data could not be read, I am in an endless loop
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readTempSensor(sensorName)
    temperaturStr = lines[1].find('t=')
    # Ich überprüfe ob die Temperatur gefunden wurde.
    # I check if the temperature was found.
    if temperaturStr != -1:
        tempData = lines[1][temperaturStr + 2:]
        tempCelsius = float(tempData) / 1000.0
        tempKelvin = 273 + float(tempData) / 1000
        tempFahrenheit = float(tempData) / 1000 * 9.0 / 5.0 + 32.0
        # Rückgabe als Array - [0] tempCelsius => Celsius...
        # Return as an array - [0] tempCelsius => Celsius ...
        return [tempCelsius, tempKelvin, tempFahrenheit]


# where the script starts
def main():
    # creates header for CSV file
    f = open('/home/pi/Mamdau2DATA/TempDATA.csv', 'a')
    f.write('Date and Time')
    f.write(',')
    f.write('Temperature Sensor 1')
    f.write(',')
    f.write('Temperature Sensor 2')
    f.write(',')
    f.write('Temperature Sensor 3')
    f.write(' ')
    f.write('\n')
    f.close()

    try:
        while True:
            # Mit einem Timestamp versehe ich meine Messung und lasse mir diese in der Console ausgeben.
            # I provide my measurement with a timestamp and have it displayed in the console.
            print("Temperature Sensor 1 at " + time.strftime('%H:%M:%S') + "   Temp. : " + str(readTempLines(sensor_1)[0]) + " °C")
            print("Temperature Sensor 2 at " + time.strftime('%H:%M:%S') + "   Temp. : " + str(readTempLines(sensor_2)[0]) + " °C")
            print("Temperature Sensor 3 at " + time.strftime('%H:%M:%S') + "   Temp. : " + str(readTempLines(sensor_3)[0]) + " °C")
            temperature_1 = readTempLines(sensor_1)[0]
            temperature_2 = readTempLines(sensor_2)[0]
            temperature_3 = readTempLines(sensor_3)[0]
            # Nach 10 Sekunden erfolgt die nächste Messung
            # The next measurement takes place after 10 seconds

            # Datenlogger
            f = open('/home/pi/Mamdau2DATA/TempDATA.csv', 'a')
            #f.write(now)
            f.write(time.strftime('%Y-%m-%d  %H:%M:%S'))
            f.write(',')
            f.write('{0:0.2f}'.format(temperature_1))  # Temperature
            f.write(',')
            f.write('{0:0.2f}'.format(temperature_2))
            f.write(',')
            f.write('{0:0.2f}'.format(temperature_3))
            f.write(' ')  # Abstand/Leerzeichen
            f.write('\n')  # Neue Zeile
            f.close()

            # und so weiter
            # and so on

    except KeyboardInterrupt:
        # Programm wird beendet wenn CTRL+C gedrückt wird.
        # Program ends when CTRL + C is pressed.
        print('Temperature measurement is ended')
    except Exception as e:
        print(str(e))
        sys.exit(1)
    finally:
        # Das Programm wird hier beendet, sodass kein Fehler in die Console geschrieben wird.
        # The program ends here so that no error is written to the console.
        print('Program has ended.')
        sys.exit(0)


if __name__ == '__main__':
    main()
