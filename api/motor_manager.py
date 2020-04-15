from gpiozero import Motor

IN_1 = 17
IN_2 = 22
IN_3 = 23
IN_4 = 24

right_motor = Motor(forward=IN_1, backward=IN_2)
left_motor = Motor(forward=IN_3, backward=IN_4)


def forward():
    right_motor.forward()
    left_motor.forward()


def backward():
    right_motor.backward()
    left_motor.backward()


def left():
    right_motor.forward()
    left_motor.backward()


def right():
    right_motor.backward()
    left_motor.forward()


def stop():
    right_motor.stop()
    left_motor.stop()
