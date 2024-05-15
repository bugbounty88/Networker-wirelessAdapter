import os
ip = input("Enter ip target: ")
os.system("nmap -sV " + ip)