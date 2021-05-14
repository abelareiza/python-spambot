from idlelib.multicall import r

import pyautogui
import time

time.sleep(5)
f = open("cuarteto-de-nos.txt", "r")
t = time.time()
s = 3.0


for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(s - ((time.time() - t) % s))
