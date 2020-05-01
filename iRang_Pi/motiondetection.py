from gpiozero import MotionSensor
from picamera import Picamera
from picamera import datetime

pir  = MotionSensor(4)
camera = Picamera()
while True:
	pir.wait_for_motion()
	print(“no motion”)
