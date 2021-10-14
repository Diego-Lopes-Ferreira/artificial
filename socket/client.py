'''
    Streaming Client
'''
import socket

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
  data = s.recv(1024)
  # print("" + repr(data))
  print("Data [ ", end="")
  print(repr(data), end="")
  print(" ]")
  ''' Print mais bonito "Data [b'O número é 20']"
  print("Data [ ", end="")
  print(repr(data), end="")
  print(" ]")
  '''

s.close()
