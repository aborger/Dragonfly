# Contains class for motors
import pigpio

pi = pigpio.pi()
MIN = 500
MAX = 2500

class Motor:
  objs = []

  def __init__(self, name, pin):
    Motor.objs.append(self)
    self.name = name
    self.GPIO_PIN = pin
    self.val = 0

  def __map(self, x, in_min, in_max, out_min, out_max):
    if x == -1:
      return 0
    else:
      return (x - in_min) * (out_max) / (in_max - in_min) + out_min

  def check_power(self, power):
    power = self.__map(power, 0, 100, MIN, MAX)
    if power <= MIN:
      power = MIN
    if power > MAX:
      power = MAX
    return power

  @classmethod
  def setPower(cls):
    for obj in cls.objs:
      power = obj.check_power(obj.val)
      pi.set_servo_pulsewidth(obj.GPIO_PIN, power)
      power = round(power, 2)
      print(obj.name + ': ' + str(power))

  @classmethod
  def set_all_power(cls, power):
    for obj in cls.objs:
      #power = obj.check_power(power)
      pi.set_servo_pulsewidth(obj.GPIO_PIN, power)
      print(obj.name + str(power))

  @classmethod
  def reset_all_vals(cls):
    for obj in cls.objs:
      obj.val = 0
