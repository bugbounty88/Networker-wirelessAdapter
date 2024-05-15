from os import system
import time
Y = "\033[2;33m"
G = "\033[2;32m"
R = "\033[2;31m"
B = "\033[2;30m"
print(R+"You must connect your device by wireless adapter.")
time.sleep(7)
print(Y + "Networker Search for devices...")
system("netdiscover")