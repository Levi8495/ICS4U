import pyautogui as pg
import keyboard as kb

#   r'C:\Users\Benoit family\Desktop\program practice\***\images\'

path = r'D:\azurelaneauto\images\azur'
file_name = pg.prompt("Enter the name fool", "Enter file name")

if file_name == None:
    quit()

cordList = []

def getcord():

    for i in range(2):

        kb.wait("space")
        x, y = pg.position()

        cordList.append(x)
        cordList.append(y)

getcord()

#   The last arguments of region are relative to the first cordinates

relx = cordList[2] - cordList[0]
rely = cordList[3] - cordList[1]

pg.screenshot(path + file_name + ".png", region=(cordList[0], cordList[1], relx, rely))
