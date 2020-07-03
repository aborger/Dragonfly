# Dragon Fly Server
# Programmed by Aaron Borger

import pigpio
import motor as m
from time import sleep


FL = m.Motor('FL',4)
FR = m.Motor('FR',27)
BL = m.Motor('BL',17)
BR = m.Motor('BR',22)



def setup():
  pi = pigpio.pi()

  m.Motor.set_all_power(0) 
  sleep(1)
  m.Motor.set_all_power(99)
  sleep(1)
  m.Motor.set_all_power(0)
  sleep(1)

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
    FL.val += inputs[2]
    BL.val += inputs[2]
    FR.val -= inputs[2]
    BR.val -= inputs[2]

    # Pitch/RY/inputs[3]
    FL.val -= inputs[3]
    FR.val -= inputs[3]
    BL.val += inputs[3]
    BR.val += inputs[3]
        

  
def update_motors():
    m.Motor.setPower()

def reset_motors():
    m.Motor.reset_all_vals()
