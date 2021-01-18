import control as mc
from time import sleep
from os import system

mc.calibrate()
mc.arm()
while True:
  #system('clear')
  #mc.test_pid()
  x_rot, y_rot, xControl, yControl = mc.pid_update()
  
  ROUND = 2
  x_rot = str(round(x_rot, ROUND))
  y_rot = str(round(y_rot, ROUND))
  xControl = str(round(xControl, ROUND))
  yControl = str(round(yControl, ROUND))
        
  print('X rot: ' + x_rot + ' Y rot: ' + y_rot + ' X C(S): ' + xControl + ' Y C(S): ' + yControl)
  mc.update_motors()
  mc.reset_motors()
  sleep(.5)
