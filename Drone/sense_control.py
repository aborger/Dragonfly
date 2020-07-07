import mpu
from simple_pid import PID

imu = mpu.imu()

while True:

    imu.update()

    print(imu.x_rot, imu.y_rot)
