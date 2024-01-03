#Simple python obfuscator

from time import sleep
import os

def starter():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
   ____  ____  ______ _    _  _____  _____       _______ ____  _____  
  / __ \|  _ \|  ____| |  | |/ ____|/ ____|   /\|__   __/ __ \|  __ \ 
 | |  | | |_) | |__  | |  | | (___ | |       /  \  | | | |  | | |__) |
 | |  | |  _ <|  __| | |  | |\___ \| |      / /\ \ | | | |  | |  _  / 
 | |__| | |_) | |    | |__| |____) | |____ / ____ \| | | |__| | | \ \ 
  \____/|____/|_|     \____/|_____/ \_____/_/    \_\_|  \____/|_|  \_\
      
    Coded by Ven
    Encrypt your python code
    Date Created: January 2, 2024""")
def obs():
    starter()
    f = input("Enter the filename you want to encrypt(e.g main.py): ")
    print("Please  wait...")
    sleep(1)
    print("Encrypting your python code....")
    os.system('python3 -m py_compile ' + f)
    sleep(1)
    print("Done. your file is saved in __pycache__")
    print("Thank you for using this tool Have a great day! :) ")
obs()
