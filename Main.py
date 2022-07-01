from abc import abstractmethod

import pyautogui,pyaudio,speech_recognition as sr, time, pandas as pd

#Global Variables
screenwidth = 0
screenlength = 0


class Positions:
    xBoard = {} # 0 - 27, A = 0 - 6, B = 7 - 13, c = 14 - 20, d = 21 - 27
    yBoard = {}
    @abstractmethod
    def __init__(self):
       pass

    def addBoard(self, name, xValue, yValue):
        self.xBoard[name] = xValue
        self.yBoard[name] = yValue

class ItemClass(Positions): #28-37
    @classmethod

class BenchClass(Positions):#38 - 45
    @classmethod

class ShopClass(Positions):
    #Actions: Augement, Armory, Radiant Armory, Tome, Buy
    @classmethod

class ActionsClass(Positions):
    #Action: Lock, level, Roll, Sell,

def moveAndClick(xValue, yValue):

def dragAndClick(xInitial, yInitial, xFinal, yFinal):




def main():
    screenwidth, screenlength = pyautogui.size()
    data = pd.read_excel(r'TFTRatios.xlsx')
    df = pd.DataFrame(data, columns=['Position', 'X Ratio', 'Y Ratio'])  #Gets x and y ratios
    df["X Ratio"] = screenwidth * df["X Ratio"]
    df["Y Ratio"] = screenlength * df["Y Ratio"]
    print(df)
    item, bench, shop , actions = ItemClass(), BenchClass(), ShopClass(), ActionsClass()


if __name__ == "__main__":
    main()