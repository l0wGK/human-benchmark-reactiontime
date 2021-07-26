from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while True:
    while keyboard.is_pressed('c') == False:
        x, y = pyautogui.position()
        if pyautogui.pixel(x,y)[1] == 218:
            click()
