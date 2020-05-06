import picamera
from time import sleep
camera = picamera.PiCamera()

i=0
while True:
    print(i)
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Mamdau2DATA/pictures/photo(' + str(i) + ').jpg')
    camera.stop_preview()
    print('Picture ' + i + ' has been successfully taken.')
    i = i + 1
