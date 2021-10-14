import socket
import time
from random import randint

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

'''
  Streaming Server
  [27] Gera um número aleatório de 0 a 9 com o randint
  [28] Junta uma string com o número convertido para string
  [29] converte a string para seu valor em binário
  [30] Mostra a informação na tela
  [31] Envia os dados
  [32] Aguarda 1 segundo
'''

while True:
  conn, addr = s.accept()
  print('Client connection accepted ' + str(addr))
  while True:
    try:
      rand_num = randint(0, 9)
      raw_data = "O numero é: " + str(rand_num)
      data = raw_data.encode()
      print('Server sent:' + raw_data)
      conn.send(data)
      time.sleep(1)
    except(socket.error):
      print('Client connection closed ' + str(addr))
      break

conn.close()
