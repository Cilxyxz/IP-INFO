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
                                                                              
       slowprint("\033[31m ════════════════════════════════════════════════════════")
       slowprint("\033[31m" + "\n IP          : \033[1;32m " + values['query'])
       slowprint("\033[31m" + " Status      : \033[1;32m " + values['status'])
       slowprint("\033[31m" + " Region      : \033[1;32m " + values['regionName'])
       slowprint("\033[31m" + " Country     : \033[1;32m " + values['country'])
       slowprint("\033[31m" + " Date & Time : \033[1;32m " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
       slowprint("\033[31m" + " City        : \033[1;32m " + values['city'])
       slowprint("\033[31m" + " ISP         : \033[1;32m " + values['isp'])
       slowprint("\033[31m" + " Lat,Lon     : \033[1;32m " + str(values['lat']) + "," + str(values['lon']))
       slowprint("\033[31m" + " ZIPCODE     : \033[1;32m " + values['zip'])
       slowprint("\033[31m" + " TimeZone    : \033[1;32m " + values['timezone'])
       slowprint("\033[31m" + " AS          : \033[1;32m " + values['as'] + "\n")
       slowprint("\033[31m ════════════════════════════════════════════════════════
       print (" ")
       slowprint("\033[31m ══════════════════════════════════════")
       slowprint("\033[31m         Coded By Pwnicated            ")
       slowprint("\033[31m══════════════════════════════════════ ")
       print (" ")
       slowprint("\033[1;91mPress\033[1;36m ENTER\033[1;91m To Continue")
       print (" ")
       vpp = input("\033[1;33m[+] IPInformation >>\033[1;32m")
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
       slowprint ("\033[31m ════════════════════════════════════════════════════════")
       slowprint ("\033[31m" + "         [+] Tool Name     =>\033[0;205" + " IP-Info")
       slowprint ("\033[31m" + "         [+] Autor         =>\033[0;205" + " Pwnicated")
       slowprint ("\033[31m" + "         [+] Github        =>\033[0;205" + " Cilxxyz")
       slowprint ("\033[31m ════════════════════════════════════════════════════════")
       magas = input("\033[31m [+] Press Enter To Continue [+]")
       if magas == " ":
           os.system("clear")
           return main()

       else:
           os.system("clear")
           return main()


def ext():

      exit()


def main():
      os.system("clear")
      print("\033[1;36m")
      slowprint(" ")
      slowprint ("\033[31m [ 1 ]\033[31m Scan IP Address")
      slowprint ("\033[31m [ 2 ]\033[31m About This Tool")
      slowprint ("\033[31m [ 0 ]\033[31m Exit")
      print("     ")
      option = input("\033[31m [+] IPInformation >> \033[31m")
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
          slowprint ("\033[31m Enter Corret Number!!!")
          time.sleep(2)
          os.system("clear")
          return main()

main()

