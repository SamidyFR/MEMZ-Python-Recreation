import os
import time
import random
import webbrowser

sites = ["https://www.google.co.ck/search?q=how+2+remove+a+virus" "https://www.google.co.ck/search?q=how+to+get+money" "https://play.clubpenguin.com" "https://www.google.co.ck/search?q=batch+virus+download" "https://www.google.co.ck/search?q=what+happens+if+you+delete+system32" "https://www.google.co.ck/search?q=bonzi+buddy+download+free" "https://www.google.co.ck/search?q=how+2+buy+weed" ]


run = True

print("YOUR COMPUTER HAS BEEN FUCKED BY THE MEMZ TROJAN. Your computer won't boot up again, so use it as long as you can! :D Trying to kill MEMZ will cause your system to be destroyed instantly, so don't try it :D")
time.sleep(5)
while run == True:
    webbrowser.open(random.choice(sites))
    time.sleep(5)