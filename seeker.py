#!/usr/bin/python3
import socket
import os
import optparse
import sys
import subprocess as sub
import time
import platform
import requests
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
   os.system('sudo apt install python3-pip -y ') 
 else:
   dependencies_print(wi + gr + '[+]' + wi + 'No missing dependencies')
except ImportError:
 print('error')
def banner():
  first_slow_print(wi + '''
▒▒▒▒▒▒▐███████▌
▒▒▒▒▒▒▐░▀░▀░▀░▌
▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌
▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄
▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐
''')
  print(wi + gr + '[+]' + wi +'Seeker By FonderElite')
  print(wi + gr + '[+]' + wi + 'Github:https://github.com/FonderElite')
banner()

def banner(ip, port):
    ports = [80,443,21,22]
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(1.5)
    print(s.recv(1024))
    
def portScanner(host):
 try:
    for i in range(1024):
     connect = st.connect(host,i)
     print("port" + i + "is open")
 except:
        return False
def main():
 while True:
    try:
       domain = input(wi + yl + "[!]" + wi + "Please Enter Domain Name: " + wi)
       param = '-n' if platform.system().lower()=='linux' else '-c'
       ping_param = '-n' if platform.system() == 'linux' else 'C'.lower()
       ip = socket.gethostbyname(domain)
       command = ['ping', '-c', '1', domain]
       check = print(wi + yl + "[!]" + wi + "Checking if host is up...")
       time.sleep(0.5)
       #live = sub.call(command)
       if bool(ip) == True or request == "<Response [200]>":
           print(wi + gr + '[+]' + wi + "Host Is Up")
           print('Ip: ' + ip)
           first_slow_print(wi + yl + "[!]" + wi + "Scanning Open Ports...")
           sub.call(['nmap','-sV','-sC',ip,'-oN','scan.txt'])
           check_file = os.path.exists("scan.txt")
           if check_file == True:
            first_slow_print(wi + gr + "[+]" + wi + "File is saved as scan.txt")
            save = open("scan.txt","r")
            for i in save:
             vuln_ports = []
           else: 
            first_slow_print(wi + rd + "[-]" + wi + "File scan.txt Not Found Error")
           #sub.call(['nc ','-l',ip,port])
       else:
          print(wi +  rd + '[-]' + wi + "Host is down or blocking the tool's probes")
    except TypeError:
         print("Error Command")

    #print(ip)
    #print(wi + gr + '[+]' + wi + 'Banner Grabbing... + str(ip)')
    #port = input("Port: ")
    #

main()
          
