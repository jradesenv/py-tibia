import pyautogui
import time
import util

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def start(clientName, clientConfigPath):
    print(clientName + " Posicione o mouse onde seleciono a Janela..." )
    time.sleep(1)

    windowPos = util.waitGetMouseStopped()
    print(clientName + " POSICAO SELECIONAR JANELA: " + str(windowPos))
    time.sleep(0.5)

    print(clientName + " Posicione o mouse onde DEVE COMER FOOD..." )
    time.sleep(1)

    foodPos = util.waitGetMouseStopped()
    print(clientName + " POSICAO DE ONDE COMER FOOD: " + str(foodPos))
    time.sleep(0.5)

    print(clientName + " Posicione o mouse onde TEM MANA PRA FAZER A RUNA..." )
    time.sleep(1)

    manaPos = util.waitGetMouseStopped()
    print(clientName + " POSICAO E COR DE ONDE TEM MANA PRA FAZER A RUNA: " + str(manaPos))
    time.sleep(0.5)

    configObject = util.Config(
        battlePos = None,
        foodPos = foodPos,
        manaPos = manaPos,
        windowPos = windowPos
    )
    util.writeConfigJson(configObject, clientConfigPath)
    savedConfig = util.loadConfigFromJson(clientConfigPath)

    print ("saved config: " + str(savedConfig))

start("client 1", util.MULTI_CLIENT_1_CONFIG_PATH)
time.sleep(1)
start("client 2", util.MULTI_CLIENT_2_CONFIG_PATH)