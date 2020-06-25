import os
from outUI import *


# I added parameter "value". This parameter is to be edited.
def MathEngine(editstatus, value):
    os.chdir("Budget")
    if editstatus == "LOSS":
        f = open("currentbudget.dll", "r")
        currentbudget = f.read()
        f.close()
        mathout = int(currentbudget) - value
        outUImath(mathout)
    else:
        f = open("currentbudget.dll", "r")
        currentbudget = f.read()
        f.close()

        mathout = currentbudget + value
        outUImath(mathout)


def DirEngine():
    try:
        os.chdir("Budget")
        f = open("currentbudget.dll", "r")
        budget = f.read()
        f.close()
    except:
        setup()


def setup():
    os.chdir("api")
    os.mkdir("Budget")
    os.chdir("Budget")
    f = open("currentbudget.dll", "w")
    f.write(input("enter current budget"))
    f.close()
