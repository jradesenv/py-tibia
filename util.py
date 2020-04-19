import pyautogui
import time
from datetime import datetime
import json
import jsonpickle

MAKE_RUNE_CONFIG_PATH = './config.json'
MULTI_CLIENT_1_CONFIG_PATH = './client1_config.json'
MULTI_CLIENT_2_CONFIG_PATH = './client2_config.json'

class AnomObject(object):
    def __init__(self, **kwargs):
         self.__dict__.update(kwargs)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self is not None and other is not None and self.__dict__ == other.__dict__

class Position(object):
    def __init__(self, x: int, y: int, color: str):
        self.x  = x
        self.y = y
        self.color = color

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self is not None and other is not None and self.__dict__ == other.__dict__

class Config(object):
    def __init__(self, battlePos: Position, foodPos: Position, manaPos: Position, windowPos: Position):
        self.windowPos = windowPos
        self.battlePos = battlePos
        self.foodPos = foodPos
        self.manaPos = manaPos

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self is not None and other is not None and self.__dict__ == other.__dict__

class CompleteConfig(object):
    def __init__(self, config: Config, extraConfig: AnomObject):
        self.config = config
        self.extraConfig = extraConfig

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
    oldPosition = Position(x=0, y=0, color="")
    newPosition = None
    while newPosition is None or oldPosition != newPosition:
        print("continue parado...")
        oldPosition = newPosition
        pos = pyautogui.position()
        newPosition = Position(x=pos.x, y=pos.y, color=rgbToHex(pyautogui.pixel(pos.x,pos.y)))
        time.sleep(3)

    print("posição identificada!")
    return newPosition

def writeConfigJson(config, path):
    jsonStr = jsonpickle.encode(config)
    with open(path, 'w') as f:
        f.write(jsonStr)

def loadConfigFromJson(path):
    jsonStr = open(path).read()
    return jsonpickle.decode(jsonStr)