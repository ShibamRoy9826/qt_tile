#!/usr/bin/python3

import pyautogui as pg
import sys

pg.FAILSAFE=False

try:
    if sys.argv[1]=="right":
        pg.hotkey('win','right')
    else:
        pg.hotkey('win','left')
except:
    pass

