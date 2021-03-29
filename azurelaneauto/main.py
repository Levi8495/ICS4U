import pyautogui as pg
import keyboard as kb
import time
import battlemod as battleM
import menumod as menuM
import pghelpfunctions2 as pghelp


kb.wait("space")

while True:


x, y = battleM.pglocate('battlebutton')
x, y = battleM.pglocate('campaign')
x, y = battleM.pglocatec('3-4picture', .9)
x, y = battleM.pglocate('clickgo')
x, y = battleM.pglocate('inbattlego')

time.sleep(5)

battleM.pgcheck('exit')

x, y = battleM.pglocatec('exit', 0.5)
x, y = battleM.pglocate('home')

menuM.retire()
menuM.shipOnScreen()
menuM.scrollRetire()
menuM.shipOnScreen()
