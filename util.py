import pyautogui
import time
from datetime import datetime

class AnomObject(object):
    def __init__(self, **kwargs):
         self.__dict__.update(kwargs)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self is not None and other is not None and self.__dict__ == other.__dict__

def rgbToHex(rgb):
    return str('#%02x%02x%02x' % rgb)

def dateTimeStr():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]

def log(msg):
    print(dateTimeStr() + " " + msg)

def waitGetMouseStopped():
    oldPosition = AnomObject(x=0, y=0, color="")
    newPosition = None
    while newPosition is None or oldPosition != newPosition:
        print("continue parado...")
        oldPosition = newPosition
        pos = pyautogui.position()
        newPosition = AnomObject(x=pos.x, y=pos.y, color=rgbToHex(pyautogui.pixel(pos.x,pos.y)))
        time.sleep(3)

    print("posição identificada!")
    return newPosition