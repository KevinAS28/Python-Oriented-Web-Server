import os
import sys
import time
import imp
from threading import Thread
import re
#Naming rule:
#(Uppercase at first letter)_Uppercase at first letter
#each shorten of word, its capital
#module name, not capital except shorten of word

#Module prerequirement:
# module_name (at bottom)


#----------OWS-----------------
class OWS:
#----------PUBLIC-----------
    start_dir = os.getcwd()
    def Temp_Error(self, x):
        print("[-INTERNAL ERROR-] ", x)
#----------PUBLIC-----------    
    
#----------INTERNAL_SOURCE----------        
    over_write_file = True
    def __init__(self):
        print("", end="")
        

    def Remove_Ext(self=0, file_name="file.exe"):
        dot = list(file_name).index(".")
        to_return = ""
        for i in range(dot):
            to_return += file_name[i]
        return to_return    
    def Load_Module(self = 0, module="", dari="OWS_Tools", mode=0):
        #I DON'T WANT TO USE EXEC OR EVAL!!!
        #AND THIS METHOD NAME SHOULD BE Import_OWS
        #bisa pakai sys.path.insert(0, "OWS_FILES/OWS_Protocol")
        #ternyata ga bisa encrypt.
        try:        
            import_from = ["OWS_GUIs", "OWS_Protocols", "OWS_Servers", "OWS_Tools", "OWS_Pages"]
            the_module = os.path.join("OWS_FILES", import_from[import_from.index(dari)], module)
            if (mode==0):
                for i in os.listdir(the_module):
                    if (not i.endswith(".py")):
                        continue
                    to_exec = ["global {a}; {x} = imp.load_source('{y}', '{z}')".format(a=i.rstrip(".py"), x=i.rstrip(".py"), y=i, z=os.path.join(os.getcwd(), the_module, i))]
                    for a in to_exec:
                        try:
                            exec(a)
                        except BaseException as error:
                            print("Cannot Load %s: %s " %(i, str(error)))
                    
            if (mode==1):
                    return imp.load_source(module+".py", os.path.join(os.getcwd(), the_module, module+".py"))
        except Exception as err:
            print("[-ERROR-] Cannot load", module, "\n", str(err))
            
    Load_Module(module="printt", dari="OWS_Tools")
    Load_Module(module="logg", dari="OWS_Tools") 
    printt.Add_Function(  logg.Logg)
    to_load = {"MYSQL": "OWS_Tools", "backup": "OWS_Tools", "HTML": "OWS_Tools", "file_manager": "OWS_Tools"}
    printt.Info("Loading Modules...")
    for i in to_load:
        try:
            printt.Info("Loading module %s..." %(i))
            Load_Module(module=i, dari=to_load[i])
        except Exception as err:
            printt.Error(str(err))

    #------------------
    #SERVER DAN PROTOCOL di FOLDER
    #di gui, show availble server
    #developer mode...anjay
    #ntar di encrypt
    #daftar login
    #------------------
    #object oriented protocol
    #object oriented web page and web post / get
    #export servernya, pake lagi di ows lain (kalo bisa dengan cara install atau import)
    #library crypto (sekalian buat pribadi juga)
    #fitur https?
    #GUI?
    #rapihin nama function, dll
    #sebelum start, check dulu semua file, kelengkapannya
    #Label? OWS. Oriented Web Server
    #jangan lupa nanti dikasih delete biar hemat ram
    #Protocol harus ada Connect, send, recv, disconnect
    db_name = "OWS"
    MYSQL.db_name = db_name
    def Conf_Read(self=0, key="ALL", mode = 0, dari = 0):
        #mode (0=normal, 1=list)
        conf_sources = [MYSQL, logg]
        temp = conf_sources[dari]
        to_use = [temp.Read_Conf, temp.Read_Conf_List]
        #try default first
        try:
            return to_use[mode](key)
        except Exception as err:
            printt.Error("Cannot Read Conf from %s %s %s" %(temp.module_name, ":", str(err)))
            printt.Info("Try to read from another source...\n\n")            
            dari = 0
            for i in conf_sources:
                try:
                    temp = i
                    printt.Info("Trying from %s" %(temp.module_name))
                    to_use = [temp.Read_Conf, temp.Read_Conf_List]
                    hasil =  to_use[mode](key)
                    printt.Info("Success read configuration from %s" %(temp.module_name))
                    return hasil
                except:
                    continue                        
            printt.Error("Still cannot read from any source...\nProgram must be halted\nExitting...")
            raise SystemExit
        
    def Module_Lister(self=0, folder=""):
            return os.listdir(os.path.join(os.getcwd(), "OWS_FILES", folder))
    
        
    def Other_Files_Reader(self=0, file=""):
            addr = os.path.join("OWS_FILES", "Other_Files", file)
            with open(addr, "rb") as baca:
                return baca.read()
    def Other_Files_Lister(self=0, folder=""):
        addr = os.path.join("OWS_FILES", "Other_Files", folder)
        result = os.listdir(addr)
        for i in range(len(result)):
            result[i] = os.path.join("OWS_FILES", "Other_Files", folder, result[i])
        """
        for root, dirs, files in os.walk(top=addr, topdown="false"):
            for i in files:
                result.append(os.path.join(root, i))
        """
        
        return result
    def Get_Address_In_Other_Files(self=0, folder="", file=""):
        file = os.path.join("OWS_FILES", "Other_Files", folder, file)
        if (os.access(file, os.R_OK)):
            return os.path.join(os.getcwd(), file)
        return False
    #------ END_OF_INTERNAL_SOURCE------
    
    printt.Info("OWS Starting%s\n\n%s"%("", "-"*50))
    Server_List = Module_Lister(folder="OWS_Servers")
    GUI_List = Module_Lister(folder="OWS_GUIs")
    Protocol_List = Module_Lister(folder="OWS_Protocols")
    #Mencoba dengan GUI flexible, yang penting ada start, stop, restart, logo, status
    Running_Server = []
    Running_GUI = []
    #def Generate_Server
    #def Delete_Server 
    
    def Start_Server(self, server_name, protocol):
        printt.Info("Starting Server %s..." %(server_name))
        if True:   #try:
            #every server must have its own tools
            server = self.Load_Module(module=self.Server_List[self.Server_List.index(server_name)], dari="OWS_Servers", mode=1)    
            #prepare the tools...
            server_conf_reader = self.Load_Module(module="logg", dari="OWS_Tools", mode=1)
            server_conf_reader.conf_file = server.conf_file
            
            Server_Conf_Read = server_conf_reader.Read_Conf
            Server_Conf_Read_List = server_conf_reader.Read_Conf_List
            
            tools = [Server_Conf_Read, Server_Conf_Read_List, printt, HTML, printt, file_manager, self.Other_Files_Reader, self.Other_Files_Lister, self.Get_Address_In_Other_Files, MYSQL]
            
            protocol = self.Load_Module(module=self.Protocol_List[self.Protocol_List.index(protocol)], dari="OWS_Protocols", mode=1)
            #self.Running_Server[self.Empty_Running_Server_Id] = server.Server(protocol, tools)
            self.Running_Server.append(server.Server(protocol, tools))
            starter = Thread(target=self.Running_Server[-1].Start, args=[])
            starter.start()
            
            printt.Info("Server %s Started" %(server_name))
        #except Exception as err:
        #    printt.Error("Error while starting server %s: %s" %(server_name, str(err)))
    def Stop_Server(self):
        #try:
            ke = len(self.Running_Server)-1
            printt.Info("Stopping Server %s..." %(self.Running_Server[ke].Server_Name))
            self.Running_Server[ke].Stop()
            time.sleep(5)
            printt.Info("Server %s Stopped" %(self.Running_Server[ke].Server_Name))
            del self.Running_Server[ke]
        #except Exception as err:
        #    printt.Error(str(err))
        
    def Restart_Server(self, ke=len(Running_Server)-1):
        self.Stop_Server()
        self.Start_OWS_Server()
        
    def Start_OWS_Server(self):
        self.Start_Server("OWS_MAIN_SERVER", "TCP")
    def Start_GUI(self, gui_file, inputs=[]):
        try:
            #inputs is list of gui input function
            GUI = self.Load_Module(module=gui_file, dari="OWS_GUIs", mode=1)
            self.Running_GUI.append(GUI)
            Thread(target=self.Running_GUI[-1].Start_GUI, args=[inputs]).start()
            printt.Integrated_Function.append(self.Running_GUI[-1].GUI_Output)
        except Exception as err:
            printt.Error(str(err))
    def About(self, *args):
        printt.Info("Oriented Web Server\nWritten by Kevin Agusto\n")
        printt.Info("Server dengan konfigurasi, dengan c++?")
    def Start_OWS(self):
        self.Start_GUI(self.Conf_Read(key="GUI", mode=0, dari=0), [self.Start_OWS_Server, self.Stop_Server, self.Restart_Server, self.About])
    def Debug(self):
        while True:
            try:
                order = (input("order: "))
                if (order=="exit"):
                    break
                exec(order)
            except KeyboardInterrupt:
                break
            except Exception as err:
                printt.Error(str(err))
#--------END_OF_OWS----------

def User_Mode():
    OWS().Start_OWS()
    
def Dev_Mode():
    ows= OWS()
    Thread(target=ows.Debug).start()
    ows.Start_OWS()

if __name__ == "__main__":
    Dev_Mode()
    
    
    
    
    
