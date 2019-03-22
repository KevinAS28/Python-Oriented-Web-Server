from threading import Thread
import time
import os
import imp
import MySQLdb
#from urllib import request, parse, response

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
imp.load_source("OWS_Page_Handler.py", os.path.join(dir_path, "OWS_Page_Handler.py"))
conf_file = os.path.join(dir_path, "OWS_MAIN_SERVER.conf")

def No_Tools(*x):
    print("No tools...")
tools = []
#Server_Conf_Read, Server_Conf_Read_List, Page_Lister

class Server:
    def Debug_Server(self):
        while (True):
            try:
                inp = input("Server %s command: " %(self.Server_Name))
                if (inp=="exit"):
                    break
                exec(inp)
            except KeyboardInterrupt:
                break
    
    def Add_Tools(self, tools=[]):
        for i in tools:
            to_exec = ["self.{x} = i".format(x=i.__name__.rstrip(".py") if (i.__name__).endswith(".py") else i.__name__) ]
            for a in to_exec:
                exec(a)
    
    
    def __init__(self, protocol, tools=[]):
        self.Add_Tools(tools)
        self.name = "OWS_MAIN_SERVER"
        self.protocol = protocol.Protocol(port=int(self.Read_Conf("port")))
        
        self.running = False
        self.source_folder = self.Read_Conf("source_folder")
        self.all_files = self.Other_Files_Lister(self.source_folder)
        self.default_page = self.Read_Conf("default_page")
    
    def Login(data):
        return "OWS.jpg"
    list_action = {b"Login": Login}
    def Client_Handler(self, *data):
        web_data = self.HTML.Get_Data(data[0])
        connection_id = data[1]
        address_dynamic = data[2]
        address_static = data[3]
        to_send = self.default_page
        if (web_data[b"method"]==b"GET"):
            try:
                if (web_data["file"]==b""):
                    to_send = self.default_page
            except KeyError:
                to_send = self.default_page
        else:
                to_send = web_data[b"file"]
        if (web_data[b"method"]==b"POST"):
            to_send = self.list_action[web_data[b"button"]](web_data)
        to_send = self.Get_Address_In_Other_Files(folder=self.source_folder, file=to_send)
        to_send = self.file_manager.File_Reader(to_send)
        self.protocol.Send_By_ID(connection_id, to_send)
    def Start(self):
        
        if (not self.running):
            self.running = True
            #self.Server = Thread(target=self.protocol.Start_Listen, args=[[self.Client_Handler]])
            #self.Server.start()
            self.protocol.Start_Listen([self.Client_Handler])
    def Stop(self):
        
        self.protocol.Stop_Listen()
        self.running=False
        
    def Restart(self):
        self.Stop()
        self.Start()
        
    @property
    def Server_Name(self):
        return self.name    
    
module_name = "OWS_MAIN_SERVER"