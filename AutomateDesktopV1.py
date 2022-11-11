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

# combine the mouse.move and keyboard.write into the same source via tuple and enumeration. Feed source into seperate functions that will act upon the source differently from eachother.

# dirpath = os.path.dirname

# df = pd.read_excel(r'D:\PPDproj\SamplePPDSpreadsheet.xlsx',engine='openpyxl')

# emails = df.Email
# emailList = []
recCoordsList = []
continuesList = []
formattedList = []
listenerList = []
listenerList2 = []

# for email in emails:
#     emailList.append(email)


def startKeyLog(arg):
    arg = arg.lower()

    command = input(
        "Please enter keys that you wish to be played back in the sequence.")
    if(arg == "y"):
        listenerList.append(command)
    elif(arg == "v"):
        listenerList2.append(command)


hostQuestionOne = input("Press Y and then Enter to start recording.\n")


def CoordsRec(args):

    args = args.lower()
    if(args == "y" or args == "v"):
        print('Press Ctrl-C to end recording mouse coordinates.\n')
        print('Press X at any time to capture mouse position and click in that position on playback.\n')
        print("_______________________________________________________________________________")

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
                        startKeyLog("v")

                    elif(args == "y"):
                        recCoordsList.append((x, y))
                        time.sleep(1)
                        # startKeyLog("y")

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


#     print("Your keystrokes are now being recorded... Press the ESC key at any time to stop recording your keystrokes.\n")

#     def on_press(key):

#         listenerList.append(str(key))

#         if key:
#             print(key)

#         # Testing Key Presses----------------------------------------
#         # try:
#         #     print('alphanumeric key {0} pressed'.format(key.char))
#         # except AttributeError:
#         #     print('special key {0} pressed'.format(key))

#     def on_release(key):
#         # Testing key releases---------------------------------------
#         # print('{0} released'.format(key))
#         if key == pnpKey.Key.esc:
#             # Stop listener
#             return False

#     # Collect events until released
#     with pnpKey.Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()

#     # ...or, in a non-blocking fashion:
#     # listener = pnpKey.Listener(on_press=on_press, on_release=on_release)
#     # listener.start()

#     # for item in listenerList:
#     #     item = item.replace("'", "")
#     #     item = item.replace("Key.space", " ")
#     #     item = item.replace("Key.esc", "")
#     #     formattedList.append(item)


def DecisionTree(args):
    while True:
        args = args.lower()
        if (args == "y"):
            startKeyLog(args)
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
def PlayBack(arg, x, y, item):
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
        # for item in listenerList:
        #     time.sleep(1)
        # item = item.replace("'", "")
        # item = item.replace("Key.esc", "")
        # item = item.replace("Key.space", " ")
        pag.write(item)
    elif(arg == "v"):
        print(continuesList)
        time.sleep(1)
        pag.write(item)

        # playbackKeyboard(item)
        # newFormattedList = ('').join(formattedList)
        # print(newFormattedList)


for iter, (item1, item2) in enumerate(zip(recCoordsList, listenerList)):
    a, b = item1
    PlayBack("y", a, b, item2)

for iter, (item1, item2) in enumerate(zip(continuesList, listenerList2)):
    a, b = item1
    PlayBack("v", a, b, item2)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
