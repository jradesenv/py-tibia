import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

class AnomObject(object):
    def __init__(self, **kwargs):
         self.__dict__.update(kwargs)

    def __str__(self):
        return str(self.__dict__)

battlePos = AnomObject(
    x=1738,
    y=124
)

def start():
    while True:
        print("rodando..." + str(battlePos))
        time.sleep(0.01)



start()