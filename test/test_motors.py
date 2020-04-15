import RPi.GPIO as GPIO
import time


IN_1 = 17
IN_2 = 22
IN_3 = 23
IN_4 = 24


def clean():
    GPIO.cleanup()


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IN_1, GPIO.OUT)
    GPIO.setup(IN_2, GPIO.OUT)
    GPIO.setup(IN_3, GPIO.OUT)
    GPIO.setup(IN_4, GPIO.OUT)


def forward(sec):
    GPIO.output(IN_1, True)
    GPIO.output(IN_2, False)
    GPIO.output(IN_3, True)
    GPIO.output(IN_4, False)
    time.sleep(sec)


def stop_all():
    GPIO.output(IN_1, GPIO.LOW)
    GPIO.output(IN_2, GPIO.LOW)
    GPIO.output(IN_3, GPIO.LOW)
    GPIO.output(IN_4, GPIO.LOW)


def reverse(sec):
    GPIO.output(IN_1, False)
    GPIO.output(IN_2, True)
    GPIO.output(IN_3, False)
    GPIO.output(IN_4, True)
    time.sleep(sec)


# noinspection PyBroadException
try:
    init()
    print("forward")
    forward(4)
    print("stop")
    time.sleep(10)
    print("reverse")
    reverse(2)
except:
    print("Cleaning GPIO...")

clean()
