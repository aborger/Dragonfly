# Dragon Fly Server
# Programmed by Aaron Borger

import socket
import control as mc
import os



#os.system("sudo pigpiod")

#mc.calibrate()
mc.arm()

# Create socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get this machine name
host = '192.168.137.94'
print(host)
port = 9999

# bind to the port
serversocket.bind((host, port))

# que up to 5 requests
serversocket.listen(5)

def parse(vals):
  valList = vals.split()
  mapped = list(map(int, valList))
  while len(mapped) < 4:
    mapped.append(0)
  return mapped


while True:
    # establish connection
    clientsocket,addr = serversocket.accept()
    while True:

        message = clientsocket.recv(11)
        inputs = parse(message)
        inputs[0] -= 10
        inputs[2] -= 50
        inputs[3] -= 50

        mc.convert(inputs)
        x_rot, y_rot, xControl, yControl = mc.pid_update()

        ROUND = 2
        x_rot = round(x_rot, ROUND)
        y_rot = round(y_rot, ROUND)
        xControl = round(xControl, ROUND)
        yControl = round(yControl, ROUND)
        # Clears screen
        print(chr(27) + "[2J")

        mc.update_motors()
        print(' ')
        print('x_rot = ' + str(x_rot))
        print('y_rot = ' + str(y_rot))
        print('xControl = ' + str(xControl))
        print('yControl = ' + str(yControl))

        mc.reset_motors()

