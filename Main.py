import pyautogui,pyaudio,speech_recognition as sr, time, pandas as pd
screenwidth, screenlength = pyautogui.size()
print(screenwidth, screenlength)


# class ItemPositions:
#     xItem = []
#     yItem = []
#     @classmethod
#     def
#
# class boardPositions:
#     xBoard = []
#     yBoard = []
#     @classmethod
#
# class buyPositions:
#     xBuy = []
#     yBuy = []
#     @classmethod
#
# class benchPositions:
#     xBench = []
#     yBench = []
#     @classmethod
#
# class actions:
#
#
# #def Carousel():
#
# def Buy():
#
# def Sell():
#
# #def Place():
#
# #def Orb():
#
# def Item():
#
# def Augement():
#
# def Level():
#
# def Roll():
#
# #def Scout():
#
# def Lock():



def main():
    data = pd.read_excel(r'TFTRatios.xlsx')
    df = pd.DataFrame(data, columns=['X Ratio', 'Y Ratio'])
    print (df)

if __name__ == "__main__":
    main()