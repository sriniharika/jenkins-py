# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket
def resolve(host):
    return socket.gethostbyname(host)

print(resolve('ibm.com'))

