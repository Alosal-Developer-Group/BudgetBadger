from api import *


def UIfrontend():
    print("1 - Edit Budget")
    print("2 - Read Budget")
    if input() == "1":
        print("1 - I received money")
        print("2 - I spent or lost money")
        if input() == "1":
            editbudget("GAIN")
        else:
            editbudget("LOSS")
    else:
        readbudget()


DirEngine()
UIfrontend()
