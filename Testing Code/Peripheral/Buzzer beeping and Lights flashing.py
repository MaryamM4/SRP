from RPi import GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT) 

while True:
    GPIO.output(19, 1)
    GPIO.output(21, 1)
    time.sleep(1)
    GPIO.output(19,0)
    GPIO.output(21,0)
    time.sleep(1)
GPIO.cleanup()
    