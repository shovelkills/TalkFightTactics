from abc import abstractmethod

import pyautogui as pygui,pyaudio,speech_recognition as sr, time, pandas as pd

#Global Variables
screenwidth, screenlength = pygui.size()


class Positions:

    @abstractmethod
    def __init__(self):
        self.xPosition = {}
        self.yPosition = {}
    @classmethod
    def addPosition(self, name, xvalue, yvalue):#Adds to position dictionaries
        self.xPosition[name] = xvalue
        self.yPosition[name] = yvalue
    def showPosition(self):
        print(self.yPosition)
        print(self.xPosition)

class BoardClass(Positions):# 0 - 27, A = 0 - 6, B = 7 - 13, c = 14 - 20, d = 21 - 27
    #Actions: Move from board to board and bench
    #Action:Move item from bench to unit - bench and board
    #Action: Move from bench to board and bench
    xPosition = {}
    yPosition = {}
    @abstractmethod
    def __init__(self):
        super()
    def addPosition(self, name, xvalue, yvalue):
        super().addPosition(name, xvalue, yvalue)

class ShopClass(Positions):
    #Actions: Pick Augement, Armory, Radiant Armory, Tome, Buy
    #Action: Lock, level, Roll, Sell,
    xPosition = {}
    yPosition = {}
    @abstractmethod
    def __init__(self):
        super()
    def addPosition(self, name, xvalue, yvalue):
        super().addPosition(name, xvalue, yvalue)

def moveAndClick(xvalue, yvalue):
    pygui.click(x=xvalue, y=yvalue, button ='left')

def dragAndClick(xinitial, yinitial, xfinal, yfinal):
    pygui.mouseDown(x = xinitial, y = yinitial)
    pygui.mouseUp(x = xfinal, y = yfinal)



def main():
    data = pd.read_excel(r'TFTRatios.xlsx')
    df = pd.DataFrame(data, columns=['Position', 'X Ratio', 'Y Ratio'])  #Gets x and y ratios
    df["X Ratio"] = screenwidth * df["X Ratio"]
    df["Y Ratio"] = screenlength * df["Y Ratio"]
    board, shop = BoardClass(), ShopClass()
    for i in range(len(df)):
        temp = df.iloc[i]
        if ("Item" in temp['Position'] or "Bench" in temp['Position'] or len(temp['Position']) == 2):
            board.addPosition(temp['Position'], temp['X Ratio'], temp['Y Ratio'])
        else:
            shop.addPosition(temp['Position'], temp['X Ratio'], temp['Y Ratio'])
    board.showPosition()
    shop.showPosition()
if __name__ == "__main__":
    main()