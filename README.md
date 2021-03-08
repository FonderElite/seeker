#!/usr/bin/python3
import mechanize
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
            vp = ['ftp','ssh','telnet','netbios-ssn','dns','pop3','windows-rpc','mysql','http','https','smtp','msrpc']
            if vp[0] or vp[1] or vp[2] or vp[3] or vp[4] or vp[5] or vp[6] or vp[7] or vp[8] or vp[9] or vp[10] or vp[11] in save:
             first_slow_print(wi + gr + "[+]" + wi + "Vulnerable Port(s) found!")
            else: 
             first_slow_print(wi + rd + "[-]" + wi + "No Vulnerable Ports are present!")
           else: 
            first_slow_print(wi + rd + "[-]" + wi + "File scan.txt Not Found Error")
           #sub.call(['nc ','-l',ip,port])
           try:
            first_slow_print(wi + yl + '[!]' + wi  + 'Testing Blind Sql Injection on the target')
            url = "http://" + ip
            sqlw = input('SQLi_Payload location: ')
            openw = open(sqlw,'r')
            for i in openw:
             i = i.strip()
             blindsql = requests.post(url + "/" + i)
             print(blindsql)
           except:
            print(wi + rd + '[-]' + wi + "Error, most likely the target is not vulnerable")
       else:
          print(wi +  rd + '[-]' + wi + "Host is down or blocking the tool's probes")
    except TypeError:
         print("Error Command")

    #print(ip)
    #print(wi + gr + '[+]' + wi + 'Banner Grabbing... + str(ip)')
    #port = input("Port: ")
    #

main()
          
                
