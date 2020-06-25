from BudgetBadgerUpdated.api import *

def UIfrontend():
    while True:
        print("1 - Edit Budget")
        print("2 - Read Budget")
        if input() == "1":
            editbudget()

        else:
            readbudget()
        print(' ') # This is to give some space between the UIFrontends


DirEngine()
UIfrontend()
