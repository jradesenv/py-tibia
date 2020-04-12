import pyautogui
import time
from util import log, AnomObject, rgbToHex, loadConfigFromJson

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = False

CONFIG = loadConfigFromJson()

#### START EXTRA CONFIG
extraConfig = AnomObject(
    logoutWhenNotAlone = True, 
    magicSpell = 'exevo pan',
    faceDirectionKey = 'd', #a,s,w,d
    loopsToHarlemShake = 100,
    _currentLoopsWithoutHarlemShake = 0,
    loopsToEatFood = 50,
    _currentLoopsWithoutEatFood = 0
)
#### END EXTRA CONFIG

def isAlone():
    battleColor = rgbToHex(pyautogui.pixel(CONFIG.battlePos.x,CONFIG.battlePos.y))
    alone = battleColor == CONFIG.battlePos.color
    return alone

def hasMana():
    manaColor = rgbToHex(pyautogui.pixel(CONFIG.manaPos.x,CONFIG.manaPos.y))
    mana = manaColor == CONFIG.manaPos.color
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
    pyautogui.rightClick(CONFIG.foodPos.x, CONFIG.foodPos.y)

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
    log("config carregada: " + str(CONFIG))
    time.sleep(3)
    log("jogando! extraConfig: " + str(extraConfig))
    
    while True:
        checkIsAlone()
        checkMakeRune()
        checkHarlemShake()
        checkEatFood()
        time.sleep(0.1)

start()