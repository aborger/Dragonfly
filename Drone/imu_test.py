import mpu

imu = mpu.imu()

while True:

    imu.update()

    print(imu.x_rot, imu.y_rot)
