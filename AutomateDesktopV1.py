from asyncio.windows_events import NULL
import pyautogui as pag
import sys
import pandas as pd
import os
import time
import pygetwindow
import keyboard
import re
from pynput import keyboard as pnpKey

# dirpath = os.path.dirname

# df = pd.read_excel(r'D:\PPDproj\SamplePPDSpreadsheet.xlsx',engine='openpyxl')

# emails = df.Email
# emailList = []
recCoordsList = []
continuesList = []

# for email in emails:
#     emailList.append(email)


hostQuestionOne = input("Press Y and then Enter to start recording.\n")


def CoordsRec(args):

    args = args.lower()
    if(args == "y" or args == "v"):
        print('Press Ctrl-C to end recording mouse coordinates.\n')
        print('Press X at any time to capture mouse position and click in that position on playback.\n')
        print("_______________________________________________________________________________")
        # if(args == "v"):
        #     time.sleep(2)
        #     pag.hotkey("ctrl", "c")
        try:
            while True:

                x, y = pag.position()
                positionStr = 'X: ' + \
                    str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr, end='')
                print('\b' * len(positionStr), end='', flush=True)
                rec = keyboard.is_pressed('x')

                if(rec):
                    print('x was pressed')
                    coords = str(pag.position())
                    newCoords = re.sub('[A-Za-z]', '', coords)
                    newCoords = re.sub('=', '', newCoords)
                    newCoords = newCoords.replace(" ", "")
                    newCoords = eval(newCoords)
                    x, y = newCoords
                    thisstring = 'Coordinates X:{x},Y:{y} were added to the playback list.'
                    print(thisstring.format(x=x, y=y))
                    time.sleep(1)
                    if(args == "v"):
                        continuesList.append((x, y))
                        time.sleep(1)

                    elif(args == "y"):
                        recCoordsList.append((x, y))
                        time.sleep(1)

        except KeyboardInterrupt:
            print("---Please Wait---")
            pag.click()
            pag.press('del')
            print('\n')
            if(args == "v"):
                return "v"
            elif(args == "y"):
                return "y"
    elif(args == 'n'):
        return NULL


CoordsRec(hostQuestionOne)


# ________________________________________________________________________________________________________________________________

hostQuestionTwo = input(
    "Would you like to enter typed keys into the playback sequence? Press Y if yes, pres N if no. Please delete the X's in the prompt... \n")

# -----------------------------------------------------------------------------------------------------------------------------
listenerList = []
formattedList = []


def startKeyLog():

    print("Your keystrokes are now being recorded... Press the ESC key at any time to stop recording your keystrokes.\n")

    def on_press(key):

        listenerList.append(str(key))

        if key:
            print(key)

        # Testing Key Presses----------------------------------------
        # try:
        #     print('alphanumeric key {0} pressed'.format(key.char))
        # except AttributeError:
        #     print('special key {0} pressed'.format(key))

    def on_release(key):
        # Testing key releases---------------------------------------
        # print('{0} released'.format(key))
        if key == pnpKey.Key.esc:
            # Stop listener
            return False

    # Collect events until released
    with pnpKey.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    # listener = pnpKey.Listener(on_press=on_press, on_release=on_release)
    # listener.start()

    # for item in listenerList:
    #     item = item.replace("'", "")
    #     item = item.replace("Key.space", " ")
    #     item = item.replace("Key.esc", "")
    #     formattedList.append(item)


def DecisionTree(args):
    while True:
        args = args.lower()
        if (args == "y"):
            startKeyLog()
        elif(args == "n"):
            print("You have chosen to end the program.")
            time.sleep(1)
            pag.press("esc")
            time.sleep(1)
            pag.hotkey("ctrl", "c")
            time.sleep(1)
            return NULL
        hostQuestionThree = input(
            "Would you like to continue recording the mouse position? Press Y if yes, press N if no.\n")
        if(hostQuestionThree.lower() == "y"):
            time.sleep(1)
            CoordsRec("v")
            time.sleep(1)
        elif(hostQuestionThree.lower() == "n"):
            break


DecisionTree(hostQuestionTwo)


# def playbackKeyboard(key):
#     time.sleep(1)
#     print(pag.press(key))
def PlayBack(arg, x, y):
    arg = arg.lower()
    time.sleep(1)
    pag.moveTo(x, y, duration=1)
    time.sleep(1)
    pag.click()
    time.sleep(1)
    print(x, y)
    if(arg == "y"):
        print(recCoordsList)
        time.sleep(1)
        for item in listenerList:
            time.sleep(1)
            item = item.replace("'", "")
            item = item.replace("Key.esc", "")
            item = item.replace("Key.space", " ")
            pag.write(item)
    elif(arg == "v"):
        print(continuesList)
        time.sleep(1)

        # playbackKeyboard(item)
        # newFormattedList = ('').join(formattedList)
        # print(newFormattedList)


for coord in recCoordsList:
    time.sleep(2)
    x, y = coord
    PlayBack("y", x, y)
    time.sleep(1)

for coord in continuesList:
    time.sleep(2)
    x, y = coord
    PlayBack("v", x, y)

# print(listenerList)
# combinedChars = []
# print(combinedChars)
# for item in listenerList:
#     combinedChars.append(' '.join(item))

# print(combinedChars)


# def Monitor(args):

    # if():
    # def OpenDB():
    #     os.startfile('D:\PPDproj\SampleRAMDatabase.xlsx')
    #     return True
    #     pag.click(1280,235)
    #     pag.moveTo(1120,445)
    #     pag.click(1120,445)
    # def DelayedGetData():
    #     time.sleep(5)
    #     pag.hotkey('ctrl','c')
    #     pag.hotkey('ctrl','z')
    #     time.sleep(5)
    # def DelayedMenuSpeadS():
    #     pag.moveTo(645,600)
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
    #             time.sleep(10)
    #             DelayedMenuSpeadS()
    #             DelayedPutData(email)
