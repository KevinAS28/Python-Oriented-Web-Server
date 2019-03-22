log_file = ["OWS.log"]
over_write_log_file = True
conf_file = "OWS.conf"
import time
def Del_Space(x):
    return x.rstrip(" ").strip(" ")

def Read_Conf_File(key="ALL"):
    with open(conf_file, "r") as oke:
        oke = oke.read()
        conf = {}
        temp0 = oke.split("\n")
        #remove space and seperate "="    
        temp0 = list(filter(lambda x: not "#" in x, map(lambda x: x.rstrip(" ").strip(" "), temp0))) 
        for i in temp0:
            if (not "=" in i):
                continue
            a = i.split("=")
            conf[Del_Space(a[0])] = Del_Space(a[1])
        if (key=="ALL"):
            return conf
        else:
            try:
                return conf[key]
            except Exception as err:
                import printt
                printt.error(str(err))
def Read_Conf_File_List(key="ALL"):
    return list(map(lambda x: x.replace(" ", ""), Read_Conf_File(key).split(",")))
def Check_Logg():
    #check file
    if (os.access(log_file[0], os.R_OK)):
        print("Log file exist")
        if over_write_log_file:
            print("Recreating...")
            os.remove(log_file[0])
            open(log_file[0], "w+")
def Logg(text, mode_log=0):
    with open(log_file[0], "a+") as tulis:
        tulis.write(str(time.ctime()))
        tulis.write(text)
        tulis.write("\n")
module_name = "logg"