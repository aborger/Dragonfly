import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

SERVO_PIN = 40

GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm=GPIO.PWM(SERVO_PIN, 50)

pwm.start(0)

def SetAngle(angle):
    duty = angle / 22 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    print('Setting angle to ' + str(angle))
    sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)
    
while True:
    SetAngle(0)
    sleep(2)
    SetAngle(110)
    sleep(2)