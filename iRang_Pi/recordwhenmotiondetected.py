
		from gpiozero import MotionSensor  #for the motion

		from picamera import PiCamera    # for the camera
		from datetime import datetime    # to change the video file name

		pir = MotionSensor(4)
		camera = PiCamera()
		filename = "{0:%Y}-{0:%m}-{0:%d}".format(datetime.now())

		while True:    # while motion detected
		pir.wait_for_motion()
		print("Motion detected!")
		camera.start_recording(filename)   # record video
		pir.wait_for_no_motion()
		camera.stop_preview()       #when motion off stop recording
