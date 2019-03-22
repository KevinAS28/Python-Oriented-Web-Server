from logg import *
def Warn(text="Something went wrong"):
    banner = "[-WARNING-]"
    text = "%s %s" %(banner, text)
    print(text)
    Logg(text)
def Error(text="An error has been occurred."):
    banner = "[-ERROR-]"
    text = "%s %s" %(banner, text)
    print(text)
    Logg(text)
def Info(text):
    banner = "[-INFO-]"
    text = "%s %s" %(banner, text)
    print(text)
    Logg(text)
    
module_name = "printt"