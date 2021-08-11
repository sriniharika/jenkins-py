# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:44:44 2021

@author: NiharikaSrivastava
"""

import socket

HOST = '127.0.0.1'

PORT = 4001

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen(2)

while True:
    clientsocket,address = server.accept()
    
    print(f"connected to client on address {address}")
    
    clientsocket.send('this is from server'.encode('utf-8'))
server.shutdown()
server.close()