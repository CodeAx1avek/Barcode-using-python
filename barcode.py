#!/bin/python
import os
try:
    import image
except:
    os.system('pip install image')
try:
    import qrcode    
except:
    os.system('pip install qrcode')
try:
    import pyfiglet
except:
    os.system('pip install pyfiglet')
try:
    import requests
except:
    os.system('pip install requests')
import time
os.system('clear')

rs = requests.session()
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
nu = 0
n = 0
br = pyfiglet.figlet_format("CodeAx1")
print(B+br)
print('''
[Make Own Barcode]
Coded By : CodeAX1
________________________________________
''')

avek = input(Y+"Enter Your Barcode Words: ")
try:
    img = qrcode.make(avek)
    location = input(Y+'enter of your barcode file name :')
    print(B+'[+] we are processing your barcode')
    time.sleep(10)
    
    saved = img.save(location+".jpg")
    print(G+'[+] We have Succesfully printed your barcod')
    print(G+'[+]Check Your file we saved')
    
    
except:
    print(B+'Something is wrong')
    print(B+'Contact Owner of Script - insta: codeax1')
    print(B+"Please report this to debug error")
