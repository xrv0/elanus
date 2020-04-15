from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)

while True:
    sleep(1)
    print(sensor.get_gyro_data())
