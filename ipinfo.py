#!/usr/bin/python

import os
import urllib.request
import json
from urllib import *
from platform import system
import sys
from datetime import datetime
import time


def slowprint(s):

    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 1000)
        
        def ipinfo():
       ip=input(" Enter IP Address : \033[1;32m ")
       url = ("http://ip-api.com/json/")
       response = urllib.request.urlopen(url + ip)
       data = response.read()
       values = json.loads(data)
       os.system("clear")
        
       print ("\033[0;205m\007\n")
       os.system("figlet IP-Info | lolcat")
       slowprint("\033[0;205 ════════════════════════════════════════════════════════")
       slowprint("\033[0;205" + "\n IP          : \033[1;32m " + values['query'])
       slowprint("\033[0;205" + " Status      : \033[0;205 " + values['status'])
       slowprint("\033[0;205" + " Region      : \033[0;205 " + values['regionName'])
       slowprint("\033[0;205" + " Country     : \033[0;205 " + values['country'])
       slowprint("\033[0;205" + " Date & Time : \033[0;205 " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
       slowprint("\033[0;205" + " City        : \033[0;205 " + values['city'])
       slowprint("\033[0;205" + " ISP         : \033[0;205 " + values['isp'])
       slowprint("\033[0;205" + " Lat,Lon     : \033[0;205 " + str(values['lat']) + "," + str(values['lon']))
       slowprint("\033[0;205" + " ZIPCODE     : \033[0;205 " + values['zip'])
       slowprint("\033[0;205" + " TimeZone    : \033[0;205 " + values['timezone'])
       slowprint("\033[0;205" + " AS          : \033[0;205 " + values['as'] + "\n")
       slowprint("\033[0;205 ════════════════════════════════════════════════════════") 
       print (" ")
       slowprint("\033[0;205        ══════════════════════════════════════")
       slowprint("\033[0;205                Coded By Pwnicated            ")
       slowprint("\033[0;205        ══════════════════════════════════════")
       print (" ")
       slowprint("\033[0;205Press\033[0;205 ENTER\033[0;205 To Continue")
       print (" ")
       vpp = input("\033[0;205m[+] IPInformation >>\033[0;2052m")
       if vpp == " ":
                os.system("clear")
                return main()
                else:
                os.system("clear")
                return main()
              def about():
       os.system("clear")
       print ("\033[1;32m\007\n")
       os.system("figlet IP-Info | lolcat")
       time.sleep(2)
        
       slowprint ("\033[0;205 ════════════════════════════════════════════════════════")
       slowprint ("\033[0;205" + "         [+] Tool Name     =>\033[0;205" + " IP-Info")
       slowprint ("\033[0;205" + "         [+] Autor         =>\033[0;205" + " Pwnicated")
       slowprint ("\033[0;205" + "         [+] Github        =>\033[0;205" + " Cilxxyz")
       slowprint ("\033[0;205 ════════════════════════════════════════════════════════")
       magas = input("\033[0;205m [+] Press Enter To Continue [+]")
       if magas == " ":
           os.system("clear")
           return main()          
           if magas == " ":
           os.system("clear")
           return main()

       else:
           os.system("clear")
           return main()


def ext():
      slowprint ("\033[1;36m ==============================================")
      slowprint ("\033[1;33m|      Thanks For Using IP-Information         |")
      slowprint ("\033[1;36m ==============================================")
      time.sleep(1)
      exit()


def main():
      os.system("clear")
      print("\033[1;36m")
      os.system("figlet IPInfo | lolcat")
      slowprint(" ")
      slowprint ("\033[1;33m [ 1 ]\033[1;91m Scan IP Address")
      slowprint ("\033[1;33m [ 2 ]\033[1;91m About This Tool")
      slowprint ("\033[1;33m [ 0 ]\033[1;91m Exit")
      print("     ")
      option = input("\033[1;36m [+] IPInformation >> \033[1;32m")
      if option == "1":
          os.system("clear")
          ipinfo()
          exit()

      elif option == "0":
          os.system("clear")
          ext()
          exit()

      elif option == "2":
          os.system("clear")
          about()
          exit()

      else:
          os.system("clear")
          slowprint ("\033[1;91m Enter Corret Number!!!")
          time.sleep(2)
          os.system("clear")
          return main()

main()

