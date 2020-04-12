import pyautogui
import time
from util import log, AnomObject, rgbToHex

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

##### START CONFIG

battlePos = AnomObject(
x= 1744, y= 122, color='#151617'
)

foodPos = AnomObject(
x= 1436, y= 486, color='#5c4538'
)

manaPos = AnomObject(
x= 1490, y= 94, color='#3535c8'
)
##### END CONFIG

#### START EXTRA CONFIG

logoutWhenNotAlone = False

#### END EXTRA CONFIG

def isAlone():
    battleColor = rgbToHex(pyautogui.pixel(battlePos.x,battlePos.y))
    alone = battleColor == battlePos.color
    return alone

def doLogout():
    pyautogui.hotkey('ctrl', 'l')

def checkIsAlone():
    if not isAlone():
        log("não está mais sozinho!!!")
        if logoutWhenNotAlone:
            print("fazendo logout!")
            doLogout()
            exit()

def start():
    while True:
        checkIsAlone()
        time.sleep(0.5)

start()