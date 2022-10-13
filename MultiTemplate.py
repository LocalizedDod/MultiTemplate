from colorama import Fore
import ctypes
from dhooks import Webhook
import sys
import time
import os
from colorama import Fore
import sys

def slowprint(s): #for slowprint
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

ctypes.windll.kernel32.SetConsoleTitleW("Loading _MULTITOOL NAME HERE_...") #title 
os.system("cls") #loader
print(Fore.GREEN + "Loading _MULTITOOL NAME HERE_../")
time.sleep(2)
os.system("cls")
print(Fore.GREEN + "Loading _MULTITOOL NAME HERE_..|")
time.sleep(2)
os.system("cls")
print(Fore.GREEN + "Loading _MULTITOOL NAME HERE_..\ ")
time.sleep(2)
os.system("cls")        

def banner():
    ctypes.windll.kernel32.SetConsoleTitleW("_MULTITOOL NAME HERE_ | _something random here like link for discord or anything_") # title of console
    os.system('mode con: cols=180 lines=40') # put the config you like just change numbers and find perfect one.
    print(Fore.MAGENTA + '''     
███▄ ▄███▓ █    ██  ██▓  ▄▄▄█████▓ ██▓▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██    ▓██░▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▒██    ▒██ ▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██▒   ░██▒▒▒█████▓ ░██████▒▒██▒ ░ ░██░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓    ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░  ░      ░░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░      ░    ░░░ ░ ░   ░ ░   ░       ▒ ░  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
       ░      ░         ░  ░        ░               ░ ░      ░ ░      ░  ░
                                                                        ''' ) 
                                                                      

banner()
print(Fore.LIGHTBLUE_EX + "───────────────────────────────────────────────────────────────────────────")  
number = input(Fore.LIGHTBLUE_EX + '''
    -----------------------------------
    | 1 ] Option          | 4 ] ?     |     
    | 2 ] Credits         | 5 ] ?     |      
    | 3 ] Webhook Spammer | 6 ] ?     |    
    -----------------------------------                  
->''') #you can expand the menu

if str(number) == "1":
    os.system("cls")
    slowprint(Fore.LIGHTBLUE_EX + "This is an Option! Edit it to anything you like [option 2/3 for a example")
    time.sleep(5)

if str(number) == "2":
    os.system("cls")
    slowprint(Fore.LIGHTBLUE_EX + "Credits to D0V4 / 0V4Team")
    time.sleep(5)

if str(number) == "3":
    os.system("cls")
    slowprint(Fore.LIGHTBLUE_EX + "Enter URL: ")
    URLWebhook = input()
    slowprint(Fore.LIGHTBLUE_EX + "Enter Message: ")
    Message = input()
    URLw = Webhook(URLWebhook)
while True:    
    URLw.send(f"{Message}") 
   








