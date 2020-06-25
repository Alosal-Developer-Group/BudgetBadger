import os
from outUI import *


# I added parameter "value". This parameter is to be edited.
def MathEngine(editstatus, value):
    if editstatus == "LOSS":

        # Basically what happens here is that, i create a variable named "path.
        # Then, i go ONE directory back than the current directory we're working in
        # And then, i go to budget.
        path = os.path.normpath(os.getcwd() + os.sep + os.pardir) + "\\Budget\\currentbudget.dll"
        f = open(path, "r")
        currentbudget = f.read()
        f.close()
        mathout = int(currentbudget) - value
        outUImath(mathout)
    else:
        path = os.path.normpath(os.getcwd() + os.sep + os.pardir) + "\\Budget\\currentbudget.dll"
        f = open(path, "r")
        currentbudget = f.read()
        f.close()

        mathout = int(currentbudget) + value
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
    os.mkdir("Budget")
    os.chdir("Budget")
    f = open("currentbudget.dll", "w")
    f.write(input("enter current budget"))
    f.close()
