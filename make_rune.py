import pyautogui
import time
from util import log, AnomObject, rgbToHex, loadConfigFromJson, MAKE_RUNE_CONFIG_PATH

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

CONFIG = loadConfigFromJson(MAKE_RUNE_CONFIG_PATH)

#### START EXTRA CONFIG
extraConfig = AnomObject(
    logoutWhenNotAlone = True, 
    runeMagicSpell = 'adura vita',
    mlTrainingSpell = 'exevo pan',
    faceDirectionKey = 'a', #a,s,w,d
    loopsToHarlemShake = 100,
    _currentLoopsWithoutHarlemShake = 0,
    loopsToEatFood = 50,
    _currentLoopsWithoutEatFood = 0,
    maxRunes = 320,
    _currentRuneCount = 0,
    makeFood = True,
    runesToExevoPan = 4,
    _currentRuneToExevoPanCount = 0,
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
    if extraConfig._currentRuneCount < extraConfig.maxRunes:
        extraConfig._currentRuneCount += 1
        log("fazendo runa")
        pyautogui.press("enter")
        pyautogui.typewrite(extraConfig.runeMagicSpell)
        pyautogui.press("enter")
    else:
        log("treinando ml")
        pyautogui.press("enter")
        pyautogui.typewrite(extraConfig.mlTrainingSpell)
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

def shouldDoExevoPan():
    if extraConfig.makeFood:
        extraConfig._currentRuneToExevoPanCount += 1
        return extraConfig._currentRuneToExevoPanCount >= extraConfig.runesToExevoPan
    else:
        return False

def doExevoPan():
    log("fazendo food")
    pyautogui.press("enter")
    pyautogui.typewrite("exevo pan")
    pyautogui.press("enter")
    extraConfig._currentRuneToExevoPanCount = 0

def checkMakeRune():
    if hasMana():
        if shouldDoExevoPan():
            doExevoPan()
        else:
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
        time.sleep(0.05)

start()