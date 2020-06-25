import os
from BudgetBadgerUpdated.outUI import *


def MathEngine(value):
    path = dir_back() + "\\BudgetBadgerUpdated\\Budget\\currentbudget.dll"
    currentbudget = read_file(path)

    mathout = int(currentbudget) + value
    edit_file(path, str(mathout))
    outUImath(mathout)


def DirEngine():
    try:
        path = dir_back() + "\\BudgetBadgerUpdated\\Budget\\currentbudget.dll"
        read_file(path)
    except:
        setup()


def dir_back(current_directory=os.getcwd()):
    """
    Goes one directory back from a specified path.
    The default setting for "current_directory" is os.getcwd()
    :param current_directory:
    :return:
    """
    return os.path.normpath(current_directory + os.sep + os.pardir)


def read_file(path):
    """
    Opens a file, and returns what ever is inside.
    :param path:
    :return:
    """
    with open(path, 'r') as f:
        return f.read()


def edit_file(path, data, mode='w'):
    """
    Edits a file
    :param path:
    :param data:
    :param mode:
    :return:
    """
    with open(path, mode) as f:
        f.write(data)


def setup():
    path = dir_back() + "\\BudgetBadgerUpdated\\Budget\\currentbudget.dll"
    f = open(path, "w")
    f.write(input("enter current budget"))
    f.close()
