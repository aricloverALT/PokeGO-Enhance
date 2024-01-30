import os, sys, time

parameters = sys.argv[1:]
platform = ""

openlimit = 0
giftlimit = 0

if (os.name == "nt"):
    platform = ".\\w-tools\\adb.exe"
elif (os.name == "posix"):
    platform = "./l-tools/adb"

if (len(parameters) >= 1):
    sys.exit()

if (len(parameters) == 1):
    if (parameters[0] == "show"):
        os.system(f"{platform} shell content insert --uri content://settings/system --bind name:s:show_touches --bind value:i:1")
    elif (parameters[0] == "hide"):
        os.system(f"{platform} shell content insert --uri content://settings/system --bind name:s:show_touches --bind value:i:0")
    elif (parameters[0] == "event"):
        os.system(f"{platform} shell getevent -l")
    else:
        sys.exit()

def opentap(x, y):
    os.popen(f"{platform} shell input tap $((16#{x})) $((16#{y}))")
    time.sleep(3)
    os.popen(f"{platform} shell input tap $((16#21c)) $((16#63f))")
    time.sleep(3)
    os.popen(f"{platform} shell input tap $((16#224)) $((16#7da))")
    time.sleep(1)
    os.popen(f"{platform} shell input tap $((16#221)) $((16#88f))")
    time.sleep(3)
    os.popen(f"{platform} shell input tap $((16#221)) $((16#88f))")
    time.sleep(3)

def sendtap(x, y, hasgift):
    os.popen(f"{platform} shell input tap $((16#{x})) $((16#{y}))")
    time.sleep(3)
    if (hasgift == "yes" or hasgift == "y"):
        os.popen(f"{platform} shell input tap $((16#221)) $((16#88f))")
        time.sleep(3)
    os.popen(f"{platform} shell input tap $((16#130)) $((16#6c9))")
    time.sleep(3)
    os.popen(f"{platform} shell input tap $((16#272)) $((16#34f))")
    time.sleep(3)
    os.popen(f"{platform} shell input tap $((16#220)) $((16#7c5))")
    time.sleep(1)
    os.popen(f"{platform} shell input tap $((16#221)) $((16#88f))")
    time.sleep(3)
    os.popen(f"{platform} shell input tap $((16#221)) $((16#88f))")
    time.sleep(3)

def scroll(open, gift, hasgift):
    os.popen(f"{platform} shell input touchscreen swipe 250 1000 250 500 400")
    time.sleep(1)
    friends(open, gift, hasgift)

def friends(open, gift, hasgift):
    if (open == 1):
        global openlimit
        # Friend 1
        opentap("2b0", "3ab")
        openlimit += 1
        if (openlimit == gift):
            sys.exit()
        # Friend 2
        opentap("20e", "510")
        openlimit += 1
        if (openlimit == gift):
            sys.exit()
        # Friend 3
        opentap("25a", "644")
        openlimit += 1
        if (openlimit == gift):
            sys.exit()
        # Friend 4
        opentap("239", "7c7")
        openlimit += 1
        if (openlimit == gift):
            sys.exit()
        else:
            scroll(open, gift, hasgift)
    else:
        global giftlimit
        # Friend 1
        sendtap("2b0", "3ab", hasgift)
        giftlimit += 1
        if (giftlimit == gift):
            sys.exit()
        # Friend 2
        sendtap("20e", "510", hasgift)
        giftlimit += 1
        if (giftlimit == gift):
            sys.exit()
        # Friend 3
        sendtap("25a", "644", hasgift)
        giftlimit += 1
        if (giftlimit == gift):
            sys.exit()
        # Friend 4
        sendtap("239", "7c7", hasgift)
        giftlimit += 1
        if (giftlimit == gift):
            sys.exit()
        else:
            scroll(open, gift, hasgift)

op1 = input("Would you to open gifts or sends gifts? Type open or o for opening gifts, type send or s for sending gifts: ")

if (op1 == "open" or op1 == "o"):
    op2 = input("How many gifts would you like to open? Please enter a number: ")
    friends(1, int(op2), None)

if (op1 == "send" or op1 == "s"):
    op2 = input("How many gifts would you like to send? Please enter a number: ")
    op3 = input("Does the top of the list have gifts? If yes type yes or y, if no type no or n: ")
    friends(0, int(op2), op3)