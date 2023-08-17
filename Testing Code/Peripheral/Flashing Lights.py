from RPi import GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)

while True:
    GPIO.output(19, 1)
    time.sleep(0.06)
    GPIO.output(19,0)
    time.sleep(0.6)
GPIO.cleanup()
    