import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm = GPIO.PWM(11, 50)
pwm.start(7.5)

try:
	while True:
		pwm.ChangeDutyCycle(12.5)
		time.sleep(5)
		pwm.ChangeDutyCycle(7.5)
		time.sleep(5)

except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()


