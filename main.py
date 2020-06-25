import os
import time
# 3Debatable_Impeach_caiman_Mince7_Queasy_Sedge
#efsghzsfgh

def UIfrontend():
    print("1 - Edit Budget")
    print("2 - Read Budget")
    if input() == "1":
        print("1 - I received money")
        print("2 - I spent or lost money")
        if input == "1":
            editbudget("GAIN")
        else:
            editbudget("LOSS")
    else:
        readbudget()


def editbudget(editstatus):
    if editstatus ==


def MathEngine():



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
