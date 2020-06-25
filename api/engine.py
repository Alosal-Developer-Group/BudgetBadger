import os


def MathEngine(editstatus):
    if editstatus == "LOSS":
        f = open("currentbudget.dll", "r")
        currentbudget = f.read()
        f.close()
        mathout = currentbudget - LOSS
        outUImath(mathout)
    else:
        f = open("currentbudget.dll", "r")
        currentbudget = f.read()
        f.close()
        mathout = currentbudget + GAIN
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
