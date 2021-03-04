#!/usr/bin/python3
import socket
import os
import optparse
import sys
import subprocess as sub
import time
import platform
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
def first_slow_print(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
def dependencies_print(s):
    for c in s + '\n' : 
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
try:
 dependencies_print(wi + yl  + '[!]' + wi + 'Checking Dependencies...')
 check_pip = os.path.exists('/usr/bin/pip')
 if  check_pip == False:
   dependencies_print(wi + rd + '[-]'+ wi + 'pip not installed')
   dependencies_print(wi + gr + '[+]' + wi + 'Installing pip...') 
   os.system('sudo apt update -y')
   os.system('sudo apt install python3-pip') 
 else:
   dependencies_print(wi + gr + '[+]' + wi + 'No missing dependencies')
except ImportError:
 print('error')
def banner():
  first_slow_print(wi + gr + '''
▒▒▒▒▒▒▐███████▌
▒▒▒▒▒▒▐░▀░▀░▀░▌
▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌
▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄
▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐
''')
  print(wi + gr + '[+]' + wi +'Seeker By FonderElite')
  print(wi + gr + '[+]' + 'Github:https://github.com/FonderElite')
banner()

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(s.recv(1024))

def main():
    try:
       domain = input("Please Enter Domain Name: ")
       param = '-n' if platform.system().lower()=='linux' else '-c'
       command = ['ping', param, '1', domain]
       command[2]+=2
       print(wi + "Checkin If Host is Up")
       live = subprocess.call(command) == 0
       if live == True:
           print(wi + gr + '[+]' + "Host Is Up")
           get_ip = gethostbyname(domain)
    except:
       print("False")

    #print(ip)
    #print(wi + gr + '[+]' + wi + 'Banner Grabbing... + str(ip)')
    #port = input("Port: ")
    #banner(ip, port)

main()
