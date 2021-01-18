# Dragon Fly Server
# Programmed by Aaron Borger

import pigpio
import motor as m
from time import sleep
import mpu
from math import e
from tf import TF

FL = m.Motor('FL',4)
FR = m.Motor('FR',22)
BL = m.Motor('BL',27)
BR = m.Motor('BR',17)

pc = TF(.1, .1)
pitchSP = 0
BIAS = 30

imu = mpu.imu()


def arm():
  pi = pigpio.pi()

  m.Motor.set_all_power(0) 
  sleep(1)
  m.Motor.set_all_power(2500)
  sleep(1)
  m.Motor.set_all_power(0)
  sleep(1)
  m.Motor.set_all_power(1000)
  sleep(3)
  m.Motor.set_all_power(2000)
  sleep(2)
  m.Motor.set_all_power(0)

def calibrate():
  m.Motor.set_all_power(0)
  print("Disconnect battery and press Enter")
  inp = input()
  if inp == '':
    m.Motor.set_all_power(2500)
    print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
    inp = input()
    if inp == '':
      print("Calibrating...")
      m.Motor.set_all_power(500)
      sleep(7)
      sleep(5)
      m.Motor.set_all_power(0)
      sleep(2)
      print("Arming...")
      m.Motor.set_all_power(500)
      sleep(1)
      print("Done")

# inputs[0] = LX, inputs[1] = LY, inputs[2] = RX, inputs[3] = RY
def convert(inputs):
    # Altitude/LY/inputs[1]
    #FL.val = inputs[1]
    #FR.val = inputs[1]
    #BL.val = inputs[1]
    #BR.val = inputs[1]
    # Yaw/LX/inputs[0]
    #FR.val -= inputs[0]
    #BL.val -= inputs[0]
    #FL.val += inputs[0]
    #BR.val += inputs[0]

    # Roll/RX/inputs[2]
    #pidX.setpoint = inputs[2]

    # Pitch/RY/inputs[3]
    #pidY.setpoint = inputs[3]
    pitchSP = 0


def test_pid():
    FL.val = 20
    FR.val = 20
    BL.val = 20
    BR.val = 20

def pid_update():
    imu.update()

    x = imu.x_rot
    y = imu.y_rot

    xControl = 0
    pitch_error = pitchSP - y
    yControl = pc.transfer(pitch_error)
    

    #FL.val += xControl * FL.val
    #BL.val += xControl * BL.val
    #FR.val -= xControl * FR.val
    #BR.val -= xControl * BR.val
    FL.val = -1 * yControl + BIAS
    FR.val = -1 * yControl + BIAS
    BL.val = yControl + BIAS
    BR.val = yControl + BIAS
    return x, y, xControl, yControl
def update_motors():
    m.Motor.setPower()

def reset_motors():
    m.Motor.reset_all_vals()
