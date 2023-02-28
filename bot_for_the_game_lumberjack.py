import numpy as np
from mss import mss
import pyautogui
import time


while True:
    m = mss()

    """При условии параметров монитора Monitor(x=0, y=0, width=3840, height=2160, width_mm=607, height_mm=345, name=' DISPLAY1', is_primary=True)"""

    monitor = {
        "left": 1033,
        "top": 1626,
        "width": 1,
        "height": 1,
    }

    img = m.grab(monitor)

    img_arr = np.array(img)
    x = img_arr[0]
    y = x[0]
    z = y[0]
    print(f'1  {z}')

    if z == 127: #Персонаж слева
        # time.sleep(0.05)
        m = mss()
        monitor = {
            "left": 874,
            "top": 1450,
            "width": 1,
            "height": 1,
        }

        img = m.grab(monitor)

        img_arr = np.array(img)

        our_color = img_arr[0]
        x = img_arr[0]
        y = x[0]
        z = y[0]
        print(f'2  {z}')

        if z == 56 or z == 50:
            pyautogui.press(['right'])
        else:
            pyautogui.press(['left'])

    elif z == 148:  # Персонаж справа
        # time.sleep(0.05)
        m = mss()
        monitor = {
            "left": 1053,
            "top": 1450,
            "width": 1,
            "height": 1,
        }

        img = m.grab(monitor)
        img_arr = np.array(img)
        our_color = img_arr[0]
        x = img_arr[0]
        y = x[0]
        z = y[0]
        print(f'3  {z}')

        if z == 56 or z == 50:
            pyautogui.press(['left'])
        else:
            pyautogui.press(['right'])

