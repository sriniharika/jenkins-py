# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:45:02 2021

@author: NiharikaSrivastava

Modes

'r' read
'w' write
'a' append

selector

'b' binary mode
't' text mode

'wb' write binary
'at' append text

open() returns file object
"""

import sys
#print(sys.getfilesystemencoding())
f = open('data.txt',mode='rt',encoding='utf-8')

#f.write("Python3 popularly used for machine learning")
#f.writelines(['python is used for Ml,\n','javascript is for web based'])

for line in f:
    sys.stdout.write(line)
       
f.close()
