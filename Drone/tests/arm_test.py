import pigpio
import motor as m
from time import sleep

FL = m.Motor('FL',4)
#FR = m.Motor('FR', 27)
BL = m.Motor('BL', 17)
BR = m.Motor('BR', 22)

pi = pigpio.pi()

def arm():
  print(m.Motor.objs)
  m.Motor.set_all_power(0)
  sleep(1)
  m.Motor.set_all_power(2500)
  sleep(1)
  m.Motor.set_all_power(0)
  sleep(1)

arm()
m.Motor.set_all_power(1000)
sleep(3)
m.Motor.set_all_power(2000)
sleep(2)
m.Motor.set_all_power(500)
sleep(2)
m.Motor.set_all_power(1500)
sleep(3)
m.Motor.set_all_power(0)
