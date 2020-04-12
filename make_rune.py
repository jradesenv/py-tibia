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
extraConfig = AnomObject(
    logoutWhenNotAlone = False, 
    magicSpell = 'adura vita',
    faceDirectionKey = 's', #a,s,w,d
    loopsToHarlemShake = 100,
    _currentLoopsWithoutHarlemShake = 0,
    loopsToEatFood = 50,
    _currentLoopsWithoutEatFood = 0
)
#### END EXTRA CONFIG

def isAlone():
    battleColor = rgbToHex(pyautogui.pixel(battlePos.x,battlePos.y))
    alone = battleColor == battlePos.color
    return alone

def hasMana():
    manaColor = rgbToHex(pyautogui.pixel(manaPos.x,manaPos.y))
    mana = manaColor == manaPos.color
    return mana

def doLogout():
    pyautogui.hotkey('ctrl', 'l')

def makeRune():
    pyautogui.press("enter")
    pyautogui.typewrite(extraConfig.magicSpell)
    pyautogui.press("enter")

def doHarlemShake():
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.press('d')
    pyautogui.press(extraConfig.faceDirectionKey)
    pyautogui.keyUp('ctrl')

def eatFood():
    pyautogui.rightClick(foodPos.x, foodPos.y)

def checkIsAlone():
    if not isAlone():
        log("não está mais sozinho!!!")
        if extraConfig.logoutWhenNotAlone:
            print("fazendo logout!")
            doLogout()
            exit()

def checkMakeRune():
    if hasMana():
        log("fazendo runa")
        makeRune()

def checkHarlemShake():
    extraConfig._currentLoopsWithoutHarlemShake += 1
    if extraConfig._currentLoopsWithoutHarlemShake >= extraConfig.loopsToHarlemShake:
        doHarlemShake()
        extraConfig._currentLoopsWithoutHarlemShake = 0

def checkEatFood():
    extraConfig._currentLoopsWithoutEatFood += 1
    if extraConfig._currentLoopsWithoutEatFood >= extraConfig.loopsToEatFood:
        eatFood()
        extraConfig._currentLoopsWithoutEatFood = 0

def start():
    time.sleep(3)
    log("jogando! extraConfig: " + str(extraConfig))
    
    while True:
        checkIsAlone()
        checkMakeRune()
        checkHarlemShake()
        checkEatFood()
        time.sleep(0.1)

start()