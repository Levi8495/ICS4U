import pyautogui as pg
import time
import keyboard as kb

path = r'D:\azurelaneauto\images\battleimages\azur'

#x, y = pg.locateCenterOnScreen(path + 'battlebutton.png', confidence=0.7)
#pg.click(x, y)
#time.sleep(1)

def pgcheck(picture):
    while pg.locateCenterOnScreen(path + picture + '.png', confidence=0.5) is None:
        pg.click(860, 540)
        time.sleep(5)

def pglocate(picture):
    x = 0
    y = 0

    x, y = pg.locateCenterOnScreen(path + picture +'.png', confidence=0.6)
    #time.sleep(0.5)
    pg.moveTo(x, y)
    pg.click(x, y)
    time.sleep(1)

    return x, y

def pglocatec(picture, conf):
    x = 0
    y = 0

    x, y = pg.locateCenterOnScreen(path + picture +'.png', confidence=conf)
    #time.sleep(0.5)
    pg.moveTo(x, y)
    pg.click(x, y)
    time.sleep(0.5)

    return x, y

def pglocateB(picture):

    x = 0
    y = 0

    x, y = pg.locateCenterOnScreen(picture, confidence=0.6)
    #time.sleep(0.5)
    pg.moveTo(x, y)
    pg.click(x, y)
    time.sleep(0.5)

def pglocateC(picture, path):

    x = 0
    y = 0

    x, y = pg.locateCenterOnScreen(path + picture + '.png', confidence=0.6)
    #time.sleep(0.5)
    pg.moveTo(x, y)
    pg.click(x, y)
    time.sleep(0.8)

def pglocateCC(picture, path, conf):

    x = 0
    y = 0

    x, y = pg.locateCenterOnScreen(path + picture + '.png', confidence=conf)
    #time.sleep(0.5)
    pg.moveTo(x, y)
    pg.click(x, y)
    time.sleep(0.5)

#kb.wait("space")
#x, y = pglocate('battlebutton')
#x, y = pglocate('campaign')
#x, y = pglocatec('3-4picture', .9)
#x, y = pglocate('clickgo')
#x, y = pglocate('inbattlego')

#time.sleep(5)

#pgcheck('exit')
#
#x, y = pglocatec('exit', 0.5)
#x, y = pglocate('home')
#x, y = pglocate('')
#x, y = pglocate('')
