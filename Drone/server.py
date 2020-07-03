# Dragon Fly Server
# Programmed by Aaron Borger

import socket
import control as mc
import os

#os.system("sudo pigpiod")

#mc.calibrate()
mc.setup()

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
  mapped = map(int, valList)
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
        inputs[2] -= 10
	inputs[3] -= 10
	for i in inputs:
	    i = i/100
        mc.convert(inputs)
        mc.update_motors()
        mc.reset_motors()

