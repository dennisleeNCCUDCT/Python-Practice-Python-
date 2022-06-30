import time;
import webbrowser;
import os;
from random import randrange

url="https://www.youtube.com/watch?v=UQ1P33qc5tg"

for e in range(1000):
     # TODO: write code...
     for i in range(10):
         webbrowser.open(url)
         time.sleep(randrange(15))
         i=i+1

         webbrowser.open(url)
         time.sleep(randrange(15))
         i=i+1

         webbrowser.open(url)
         time.sleep(randrange(15))
         i=i+1

         webbrowser.open(url)
         time.sleep(randrange(15))
         i=i+1

         webbrowser.open(url)
         time.sleep(randrange(15))
         i=i+1


         webbrowser.open(url)
         time.sleep(randrange(15))
         i=i+1

         webbrowser.open(url)
         time.sleep(randrange(15))
         i=i+1

         webbrowser.open(url)
         time.sleep(randrange(15))
         i=i+1

         webbrowser.open(url)
         time.sleep(randrange(15))
         i=i+1

         webbrowser.open(url)
         time.sleep(randrange(15))
         i=i+1

         webbrowser.open(url)
         time.sleep(120)
         i=i+1
         
        
         os.system("taskkill /im chrome.exe /f")
         print("for windows to kill chrome")
         os.system("killall -9 'Google Chrome'")
         print("for mac to kill chrome")
         e=e+1




         
