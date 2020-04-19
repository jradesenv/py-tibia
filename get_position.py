import pyautogui
import time
import util

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def printConfig(configName, pos):
    print(configName + " = AnomObject(")
    print(str(pos).replace(":", "=").replace("'", "").replace("color= ", "color='").replace("}", "'").replace("{", ""))
    print(")")

def start():
    print("Posicione o mouse onde APARECERÁ PLAYER NO BATTLE..." )
    time.sleep(1)

    battlePos = util.waitGetMouseStopped()
    print("POSICAO E COR DO BATTLE VAZIO: " + str(battlePos))
    time.sleep(0.5)

    print("Posicione o mouse onde DEVE COMER FOOD..." )
    time.sleep(1)

    foodPos = util.waitGetMouseStopped()
    print("POSICAO DE ONDE COMER FOOD: " + str(foodPos))
    time.sleep(0.5)

    print("Posicione o mouse onde TEM MANA PRA FAZER A RUNA..." )
    time.sleep(1)

    manaPos = util.waitGetMouseStopped()
    print("POSICAO E COR DE ONDE TEM MANA PRA FAZER A RUNA: " + str(manaPos))
    time.sleep(0.5)

    configObject = util.Config(
        battlePos = battlePos,
        foodPos = foodPos,
        manaPos = manaPos,
        windowPos = None
    )
    util.writeConfigJson(configObject, util.MAKE_RUNE_CONFIG_PATH)
    savedConfig = util.loadConfigFromJson(util.MAKE_RUNE_CONFIG_PATH)

    print ("saved config: " + str(savedConfig))

start()