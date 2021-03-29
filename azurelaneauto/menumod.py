import keyboard as kb
import pyautogui as pg
import pghelpfunctions2 as pghelp
import battlemod as battleM


counterList = pghelp.counterList                                    #       Just putting these lists in here
battleList = pghelp.battleList                                      #       Ill run a for loop to find the picture on screen using
dockList = pghelp.dockList                                          #       battlemod.pglocate()


def shipOnScreen():

    path = r'D:\azurelaneauto\images\dockimages\azur'

    for i in range(len(counterList.longlist)):

        try:
            battleM.pglocateB(counterList.longlist[i])
            continue

        except TypeError:
            continue

    if pg.locateCenterOnScreen(path + 'selected.png') is not None:
        battleM.pglocateC('home', path)
        return

    battleM.pglocateC('retireconfirm', path)
    battleM.pglocateC('retireconfirm', path)

    battleM.pglocateC('tapto', path)
    battleM.pglocateC('retireconfirm', path)
    battleM.pglocateC('disa', path)
    battleM.pglocateC('tapto', path)
    battleM.pglocateC('home', path)




def retire():

    path = r'D:\azurelaneauto\images\dockimages\azur'

    battleM.pglocateC('build', path)
    battleM.pglocateC('retire', path)
    #battleM.pglocateC('filter', path)
    #battleM.pglocateCC('common', path, .7)
    #battleM.pglocateCC('rare', path, .9)
    #battleM.pglocateCC('retireconfirm', path, .6)

#kb.wait("space")

def scrollRetire():

    path = r'D:\azurelaneauto\images\dockimages\azur'

    try:
        battleM.pglocateC('scroll', path)
        pg.drag(0, 500, 1, button='left')
    except TypeError:
        return



#retire()
#shipOnScreen()
#scrollRetire()

#shipOnScreen()
