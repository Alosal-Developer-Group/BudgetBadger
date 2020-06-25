from BudgetBadgerUpdated.api.engine import *


def ask_amount():
    """
    Asks the amount to either deduct or add to the user's budget.
    :return:
    """
    result = input('Amount to deduct/add: ')
    return int(result)


def editbudget():
    try:
        amount = ask_amount()
        MathEngine(amount)
    except Exception as e:
        print(e)
        print("Conversion failed, Please do not include anything but numerical characters (exclude $ or %, etc)")


def readbudget():
    path = dir_back() + "\\BudgetBadgerUpdated\\Budget\\currentbudget.dll"
    print(f'Your current budget is {read_file(path)}')

