import pyautogui
import time
from util import log, AnomObject, CompleteConfig, rgbToHex, loadConfigFromJson, MULTI_CLIENT_1_CONFIG_PATH, MULTI_CLIENT_2_CONFIG_PATH

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

CONFIG1 = loadConfigFromJson(MULTI_CLIENT_1_CONFIG_PATH)
CONFIG2 = loadConfigFromJson(MULTI_CLIENT_2_CONFIG_PATH)

#### START EXTRA CONFIG
extraConfig1 = AnomObject(
    runeMagicSpell = 'adori gran',
    mlTrainingSpell = 'exura vita',
    faceDirectionKey = 's', #a,s,w,d
    loopsToHarlemShake = 15,
    _currentLoopsWithoutHarlemShake = 0,
    loopsToEatFood = 5,
    _currentLoopsWithoutEatFood = 0,
    maxRunes = 320,
    _currentRuneCount = 0
)

extraConfig2 = AnomObject(
    runeMagicSpell = 'adura vita',
    mlTrainingSpell = 'exura vita',
    faceDirectionKey = 's', #a,s,w,d
    loopsToHarlemShake = 15,
    _currentLoopsWithoutHarlemShake = 0,
    loopsToEatFood = 5,
    _currentLoopsWithoutEatFood = 0,
    maxRunes = 320,
    _currentRuneCount = 0
)
#### END EXTRA CONFIG

multiConfigs = [
    CompleteConfig(
        config=CONFIG1, extraConfig=extraConfig1
    ),
    CompleteConfig(
        config=CONFIG2, extraConfig=extraConfig2
    )
]

def hasMana(config):
    manaColor = rgbToHex(pyautogui.pixel(config.manaPos.x,config.manaPos.y))
    mana = manaColor == config.manaPos.color
    return mana

def makeRune(extraConfig):
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


def doHarlemShake(extraConfig):
    log("fazendo harlemShake")
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.press('d')
    pyautogui.press(extraConfig.faceDirectionKey)
    pyautogui.keyUp('ctrl')

def eatFood(config):
    log("fazendo eatFood")
    pyautogui.rightClick(config.foodPos.x, config.foodPos.y)

def selectWindow(config):
    pyautogui.leftClick(config.windowPos.x, config.windowPos.y)

def checkMakeRune(config, extraConfig):
    if hasMana(config):
            makeRune(extraConfig)

def checkHarlemShake(extraConfig):
    extraConfig._currentLoopsWithoutHarlemShake += 1
    if extraConfig._currentLoopsWithoutHarlemShake >= extraConfig.loopsToHarlemShake:
        doHarlemShake(extraConfig)
        extraConfig._currentLoopsWithoutHarlemShake = 0

def checkEatFood(config, extraConfig):
    extraConfig._currentLoopsWithoutEatFood += 1
    if extraConfig._currentLoopsWithoutEatFood >= extraConfig.loopsToEatFood:
        eatFood(config)
        extraConfig._currentLoopsWithoutEatFood = 0

def start():
    time.sleep(3)
    
    while True:
        for completeConfig in multiConfigs:
            selectWindow(completeConfig.config)
            time.sleep(0.05)
            checkMakeRune(completeConfig.config, completeConfig.extraConfig)
            checkHarlemShake(completeConfig.extraConfig)
            checkEatFood(completeConfig.config, completeConfig.extraConfig)
            time.sleep(2)

start()