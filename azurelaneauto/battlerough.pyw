import pyautogui as pg
import time
import keyboard as kb

path = r'D:\azurelaneauto\images\battleimages\azur'

#x, y = pg.locateCenterOnScreen(path + 'battlebutton.png', confidence=0.7)
#pg.click(x, y)
#time.sleep(1)

def pgcheck(picture):
    while pg.locateCenterOnScreen(path + picture + '.png', confidence=0.5) is None:
        time.sleep(5)

def pglocate(picture):
    x = 0
    y = 0

    x, y = pg.locateCenterOnScreen(path + picture +'.png', confidence=0.6)
    pg.click(x, y)
    time.sleep(1.75)

    return x, y

def pglocatec(picture, conf):
    x = 0
    y = 0

    x, y = pg.locateCenterOnScreen(path + picture +'.png', confidence=conf)
    pg.click(x, y)
    time.sleep(1.75)

    return x, y


kb.wait("space")

x, y = pglocate('battlebutton')
x, y = pglocate('campaign')
x, y = pglocatec('3-4picture', .9)
x, y = pglocate('clickgo')
x, y = pglocate('inbattlego')

time.sleep(5)

pgcheck('exit')

x, y = pglocatec('exit', 0.5)
x, y = pglocate('home')
#x, y = pglocate('')
#x, y = pglocate('')
