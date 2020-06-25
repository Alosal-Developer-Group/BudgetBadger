def editbudget(editstatus):
    if editstatus == "GAIN":
        GAIN = input('How much did you make?')
        def gaintry():
            global GAIN
            try:
                VARCHECK = int(GAIN)
                MathEngine("GAIN")
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
                MathEngine("LOSS")
            except:
                print("Conversion failed, Please do not include anything but numerical characters (exclude $ or %, etc)")
                losstry()


def readbudget():
    pass
