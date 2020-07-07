# Dragon Fly Server
# Programmed by Aaron Borger

import pigpio
import motor as m
from time import sleep
from simple_pid import PID
import mpu
from math import e

FL = m.Motor('FL',4)
FR = m.Motor('FR',27)
BL = m.Motor('BL',17)
BR = m.Motor('BR',22)

imu = mpu.imu()

# Can fix tuning P, I, D
pidX = PID(0.002)
pidY = PID(0.002)

pidX.sample_time = 0.01
pidY.sample_time = 0.01
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
  m.Motor.set_all_power(-1)
  print("Disconnect battery and press Enter")
  inp = raw_input()
  if inp == '':
    m.Motor.set_all_power(100)
    print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
    inp = raw_input()
    if inp == '':
      print("Calibrating...")
      m.Motor.set_all_power(0)
      sleep(7)
      sleep(5)
      m.Motor.set_all_power(-1)
      sleep(2)
      print("Arming...")
      m.Motor.set_all_power(0)
      sleep(1)
      print("Done")

# inputs[0] = LX, inputs[1] = LY, inputs[2] = RX, inputs[3] = RY
def convert(inputs):
    # Altitude/LY/inputs[1]
    FL.val = inputs[1]
    FR.val = inputs[1]
    BL.val = inputs[1]
    BR.val = inputs[1]
    # Yaw/LX/inputs[0]
    FR.val -= inputs[0]
    BL.val -= inputs[0]
    FL.val += inputs[0]
    BR.val += inputs[0]

    # Roll/RX/inputs[2]
    pidX.setpoint = inputs[2]

    # Pitch/RY/inputs[3]
    pidY.setpoint = inputs[3]


def test_pid():
    FL.val = 20
    FR.val = 20
    BL.val = 20
    BR.val = 20

def pid_update():
    imu.update()

    x = imu.x_rot
    y = imu.y_rot

    xControl = pidX(x)
    yControl = pidY(y)


    FL.val += xControl * FL.val
    BL.val += xControl * BL.val
    FR.val -= xControl * FR.val
    BR.val -= xControl * BR.val
    FL.val -= yControl * FL.val
    FR.val -= yControl * FR.val
    BL.val += yControl * BL.val
    BR.val += yControl * BR.val

    return x_rot, y_rot, xControl, yControl
def update_motors():
    m.Motor.setPower()

def reset_motors():
    m.Motor.reset_all_vals()
