from api.engine import *


def editbudget(editstatus):
    if editstatus == "GAIN":
        def gaintry():
            GAIN = input('How much did you make?')
            try:
                VARCHECK = int(GAIN)

                # Here, I pass in the value of "Gain" to MathEngine
                MathEngine("GAIN", int(GAIN))
            except Exception as e:
                print("Conversion failed, Please do not include anything but numerical characters (exclude $ or %, etc)")
                input()
                gaintry()
        gaintry()


    else:
        def losstry():
            LOSS = input('How much did you lose/spend?')
            try:
                VARCHECK = int(LOSS)

                # Here, I pass in the value of "Loss" to MathEngine
                MathEngine("LOSS", int(LOSS))
            except:
                print("Conversion failed, Please do not include anything but numerical characters (exclude $ or %, etc)")
                input()
                losstry()
        losstry()


def readbudget():
    pass
