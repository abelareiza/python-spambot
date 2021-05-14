from idlelib.multicall import r

import pyautogui
import time

time.sleep(5)
f = open("shrek2.txt", "r")
s = time.time()

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(55.0 - ((time.time() - s) % 55.0))
