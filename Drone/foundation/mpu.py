from mpu6050 import mpu6050
from time import sleep
import math

mpu = mpu6050.mpu6050(0x68)

def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_x_rotation(x,y,z):
    radians = 0
    try:
        radians = math.atan(x / dist(y,z))
    except ZeroDivisionError:
        pass
    finally:
        return math.degrees(radians)
 
def get_y_rotation(x,y,z):
    radians = 0
    try:
        radians = math.atan(y / dist(x,z))
    except ZeroDivisionError:
        pass
    finally:
        return math.degrees(radians)

class imu:
    def __init__(self):
        self.x_rot = 0
        self.y_rot = 0

    def update(self):
        data = mpu.get_all_data()

        accel = data[0]

        accel_Xout = accel['x'] / 16384.0
        accel_Yout = accel['y'] / 16384.0
        accel_Zout = accel['z'] / 16384.0

        self.x_rot = get_x_rotation(accel_Xout, accel_Yout, accel_Zout)
        self.y_rot = get_y_rotation(accel_Xout, accel_Yout, accel_Zout)

