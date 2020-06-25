from api.engine import *


def editbudget(editstatus):
    if editstatus == "GAIN":
        GAIN = input('How much did you make?')
        def gaintry():
            global GAIN
            try:
                VARCHECK = int(GAIN)

                # Here, I pass in the value of "Gain" to MathEngine
                MathEngine("GAIN", int(GAIN))
            except:
                print("Conversion failed, Please do not include anything but numerical characters (exclude $ or %, etc)")
                input()
                gaintry()


    else:
        LOSS = input('How much did you lose/spend?')
        def losstry():
            global LOSS
            try:
                VARCHECK = int(LOSS)

                # Here, I pass in the value of "Loss" to MathEngine
                MathEngine("LOSS", int(LOSS))
            except:
                print("Conversion failed, Please do not include anything but numerical characters (exclude $ or %, etc)")
                losstry()


def readbudget():
    pass
