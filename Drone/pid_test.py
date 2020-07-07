import control as mc
from time import sleep
from os import system

#mc.calibrate()
mc.arm()
while True:
  system('clear')
  mc.test_pid()
  mc.pid_update()
  mc.update_motors()
  mc.reset_motors()
  sleep(.5)
