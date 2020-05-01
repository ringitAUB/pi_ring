from picamera import Picamera
from time import sleep
camera = Picamera()
camera.start_preview()
sleep(5)
camera.capture(‘/home/pi/Desktop/image1.jpg’)
camera.stop_preview()
