import socket
import time

HOST = '127.0.0.1' #IP Adress of the Server

PORT = 30000

s = socket.socket()
s.connect((HOST, PORT))
print("It's connected")
while True:
	dataIn = input('Send: ')
	s.send(bytes(dataIn, 'utf-8'))
	dataOut = s.recv(4)
	print(dataOut)
	time.sleep(0.1)
