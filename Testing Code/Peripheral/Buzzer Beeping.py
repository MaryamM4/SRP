from RPi import GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT) 

while True:
    GPIO.output(21, 1)
    time.sleep(.06)
    GPIO.output(21,0)
    time.sleep(.6)
GPIO.cleanup()
    