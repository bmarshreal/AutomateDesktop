from asyncio.windows_events import NULL
import pyautogui as pag, sys
import pandas as pd
import os
import time
import pygetwindow
import keyboard
import re

dirpath = os.path.dirname

df = pd.read_excel(r'D:\PPDproj\SamplePPDSpreadsheet.xlsx',engine='openpyxl')

emails = df.Email
emailList = []
recCoordsList = []

for email in emails:
    emailList.append(email)




hostQuestionOne = input("Would you like to record coordinates?")

def CoordsRec(args):

    if(args.lower() == "y"):
        print('Press Ctrl-C to quit.')
        print('Press x to capture mouse position.')

        try:
            while True:
                
                x, y = pag.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr, end='')
                print('\b' * len(positionStr), end='', flush=True)
                rec = keyboard.is_pressed('x')

                if(rec):
                    print('x was pressed')
                    coords = str(pag.position())
                    newCoords = re.sub('[A-Za-z]','',coords)#
                    newCoords = re.sub('=','',newCoords)
                    newCoords = newCoords.replace(" ","")
                    newCoords = eval(newCoords)
                    x,y = newCoords
                    thisstring = '{x} and {y} were appended.'
                    print(thisstring.format(x = x, y = y))
                    recCoordsList.append((x,y))
                    time.sleep(1)
                              
        except KeyboardInterrupt:
            pag.press('del')
            print('\n')
    elif(args.lower() == 'n'):
        return NULL


CoordsRec('y')
        
#                                                                                                                                   #
def PlayBack(x,y):
    time.sleep(1)
    pag.moveTo(x,y, duration=1)
    print(x,y)
    print(recCoordsList)
    time.sleep(1)


for coord in recCoordsList:
    time.sleep(2)
    x,y = coord
    print(PlayBack(x,y))                                  #

# def Monitor(args):

#     while args:
#         if(pynput.keyboard() == "x"):
#             CoordsRec("x")

# if():



# def OpenDB():
#     os.startfile('D:\PPDproj\SampleRAMDatabase.xlsx')
#     return True

# def OpenSpreadsheet():
#     os.startfile('D:\PPDproj\SamplePPDSpreadsheet.xlsx')
#     return True


# def DelayedMenuDB():
#     pag.moveTo(645,600)
#     pag.click()
#     pag.press('home')
#     pag.press('pgup')
#     time.sleep(7)
#     win = pygetwindow.getWindowsWithTitle('SampleRAMDatabase')[0]
#     win.maximize()
#     pag.moveTo(1280,235)
#     pag.click(1280,235)
#     pag.moveTo(1120,445)
#     pag.click(1120,445)
    

# def DelayedGetData():
#     time.sleep(5)
#     pag.click()
#     pag.press('home')
#     pag.moveTo(61,257)
#     pag.dragTo(167,257,2, button='left')
#     time.sleep(5)
#     pag.hotkey('ctrl','c')
#     pag.hotkey('ctrl','z')
#     time.sleep(5)
    

# def DelayedMenuSpeadS():
#     pag.moveTo(645,600)
#     pag.click()
#     time.sleep(5)
#     win2 = pygetwindow.getWindowsWithTitle('SamplePPDSpreadsheet')[0]
#     win2.maximize()
#     pag.click()
#     pag.moveTo(837,235)
#     pag.click(837,235)
#     pag.moveTo(700,447)
#     pag.click(700,447)
    

# def DelayedPutData(arg):
#     pag.moveTo(908,257)
#     time.sleep(5)
#     pag.write(arg)
#     pag.press('enter')    
#     pag.dragTo(1077, 257,2, button='left')
#     time.sleep(5)    
#     pag.hotkey('ctrl','v')
#     pag.press('enter')
#     pag.moveTo(457,48)
#     pag.click()
#     pag.moveTo(865,80)
#     pag.click()
#     time.sleep(5)

# for email in emailList:
#     if OpenDB() == False:
#         OpenDB()
#     else:
#         time.sleep(5)
#         DelayedMenuDB()
#         pag.write(email)
#         pag.press('enter')
#         DelayedGetData()

#         if OpenSpreadsheet() == False:
#             OpenSpreadsheet()
#         else:
#             time.sleep(10)
#             DelayedMenuSpeadS()
#             DelayedPutData(email)


    



