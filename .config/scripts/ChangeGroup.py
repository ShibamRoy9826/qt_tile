#!/usr/bin/python3

import pyautogui as pg
import sys
pg.FAILSAFE=False

a=0
with open("/home/shibam/Addons/CustomScripts/logs.txt","r") as f:
    a=int(f.read())
with open("/home/shibam/Addons/CustomScripts/logs.txt","w") as f:
    a+=1
    f.write(str(a))
try:
    if sys.argv[1]=="right":
        pg.hotkey('win','right')
    else:
        pg.hotkey('win','left')
except Exception as e:
    with open("/home/shibam/Addons/CustomScripts/logs.txt","w") as f:
        f.write(str(e))

