
f = open("./cache/consoleLog.txt", "w")
def logging(msg, params = ''):
    msg = msg + params
    f.writelines(msg)