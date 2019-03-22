import os
from threading import Thread
import socket
import time
from get_values_html import *
#object oriented protocol
#object oriented web page and web post / get
#fitur https?
#GUI?
#Label? OWS. Oriented Web Server
#jangan lupa nanti dikasih delete biar hemat ram
little_about = "Oriented Web Server\nby Kevin Agusto\n"
over_write_log_file = True
log_seperator = "\n\n"
#server_IP = "0.0.0.0" #akan berbeda dengan server lainnya jika ingin multiple
#server_PORT = 80
encoding = "utf-8"
list_file_log = [["OWS.log", 0], ["OWS_data_recv.data", 0]]#number is to mark its already used
post_page_dir = "OWS_POST_PAGE"
get_page_dir = "OWS_GET_PAGE"
default_web_page_extension = ".html"
post_page_list_ori = ["loginnet"] #folder inside post_page
get_page_list_ori = [] #folder inside get_page
server_dir =  os.getcwd()
post_page_list = [os.path.join(server_dir, post_page_dir, x) for x in post_page_list_ori]
get_page_list = [os.path.join(server_dir, get_page_dir, x) for x in get_page_list_ori]

#spab = lambda x: [print(" ") for i in range(x)]
def check_extensions(self, daftar, ext):
    for a in daftar:
        for i in ext:
            if (a==i):
                return True
    return False
def warn(text):
    print("[-WARNING-] %s" %(text))
def error(text):
    print("[-ERROR-] %s" %(text))
def spab(jumlah, sym=" "):
    for i in range(jumlah):
        print(sym)
def logg(text, angka=0, file_log=0):
    #check if file is exist
    if (not list_file_log[file_log][1]):
        if (not os.access(list_file_log[file_log][0], os.W_OK)):
            print("Creating log file (%s)..." %(list_file_log[file_log][0]))
            try:
                open(list_file_log[file_log][0], "w+")
                list_file_log[file_log][1] = 1
            except Exception as error:
                warn("Error while creating log file: %s" %(str(error)))
        else:
            if over_write_log_file:
                try:
                    os.remove(list_file_log[file_log][0])
                    open(list_file_log[file_log][0], "w+")
                    list_file_log[file_log][1] = 1
                except Exception as error:
                    warn("Error while recreating log file: %s" %(str(error)))                        
    with open(list_file_log[file_log][0], "a+") as tulis:
        try:
            text = text.decode("utf-8")
        except AttributeError:
            pass
        except Exception as err:
            warn("cannot decode text (logging): %s" %(str(err)))
        tulis.write(text)
        for i in range(angka):
            tulis.write(log_seperator)
def file_reader(name, mode="rb"):
    with open(name, mode) as baca:
        return baca.readlines()
logg("Start at %s" %(time.ctime()), 1)
def printt(text):
    logg(text)
    print("[INFO]", end="  ")
    print(text)
def keluar(status=0, extra=" "):
    printt("\nStopping Server...\n%s" %(extra)) if not status else printt("Server is Error\n%s"%(extra))
class TCP:
    protocol_name = "TCP"
    def __init__(self, status=None, *args):
        self.protocol = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.protocol.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if (status==0):
            self.bind()
        if (status==1):
            self.listen()
        if (status==2):
            self.connect(args[0], args1)
        if (status==3):
            self.send(args[0])
        if (status==4):
            self.accept()
        if (status==5):
            self.close(args[0])
    def listenserver(self, ip, port):
        self.protocol.bind((ip, port))
        self.protocol.listen()
    def send_data(self, data, ip, port=80):
        self.protocol.connect((ip, port))
    def bind(self):
        self.protocol.bind((server_IP, server_port))
    def listen(self, backlog=None):
        try:
            self.protocol.listen(backlog)
        except Exception as err:
            error(str(err))
    def accept(self):
        return self.protocol.accept()
    def connect(self, ip, port=80):
        self.protocol.connect((ip, port))
    def resend(self, data, client_socket):
        client_socket.send(data)
        client_socket.close()
    def send(self, data):
        try:
            data = data.encode(encoding)
        except AttributeError:
            pass
        except Exception as err:
            warn(str(err))
        self.protocol.send(data)
    def close(self, sock):
        sock.close()
    def shutdown(self):
        self.protocol.shutdown(socket.SHUT_RDWR)
    def recv_data(self, sock, buffersize=1024):
        return sock.recv(1024)
#pakai tcp status
protocol_list = [TCP]
class WEB_page:
    extensions = {"javascript": ["js"], "web_page": ["html"], "web_styles": ["css"], "picture": ["jpeg", "jpg", "png"]}
    def __init__(self, berkas):
        self.berkas = berkas
    def all_files(self):
        return os.listdir(berkas)
    def style_files(self):
        return list(filter(check_extensions, os.listdir(), self.extensions["web_styles"]))
    def picture_files(self):
        return list(filter(check_extensions, os.listdir(), self.extensions["picture"]))
    def web_page_files(self):
        return list(filter(check_extensions, os.listdir(), self.extensions["web_page"]))
    def javascript_files(self):
        return list(filter(check_extensions, os.listdir(), self.extensions["javascript"]))
class GET_page(WEB_page):
    def __init__(self, berkas):
        self.data = file_reader(berkas, "r")
    def data(self):
        return data;
    def file_reader(name, mode="rb"):
        with open(name, mode) as baca:
            return baca.readlines()
class POST_page:
    def __init__(self, berkas):
        #cuma ke init filenya kok...
        #self.init_page = os.path.split(berkas)[-1] + default_web_page_extension
        self.init_page = berkas
        #berkas = os.path.join(berkas, self.init_page)
        self.data = file_reader(berkas, "r")
        #auto detect variable in web page
        with open(self.init_page, "r") as oke:
            eko = oke.read().split("\n")
            oke = oke.readlines()
        line_post_characteristic = ["input", "name"]
        post_characteristic = ["form"]
        possibilty = 0
        #//##continue;
jumlah_server_jalan = [] #menggunakan list agar bisa diedit dari dalam class
class Server0:
    server_name = "Server0"
    server_start = True
    #post_page_list = [POST_page(x) for x in post_page_list]
    #get_page_list = [GET_page(x) for x in get_page_list]
    def client_handler(self, client_socket, info=["Unknown", "Unknown"]):
        try:
            printt("Received %s Connection from %s:%d" %(self.protocol.protocol_name, info[0], info[1]))
            printt(self.protocol.recv_data(client_socket))
        except KeyboardInterrupt:
            self.server_start = False
            keluar(0)
    def __init__(self, protocol=protocol_list[0], server_ip="0.0.0.0", server_port=80):
        self.protocol = protocol()
        self.server_ip = server_ip
        self.server_port = server_port
        jumlah_server_jalan.append(self.server_name)
    def prepareserver(self):
        self.protocol.listenserver(self.server_ip, self.server_port)
    def recv_data_loop(self):
        printt("%s is listening from %s:%d"%(self.server_name, self.server_ip, self.server_port)) 
        while (self.server_start):
            try:
                client, addr = self.protocol.accept()
                Thread(target=self.client_handler, args=[client, addr]).start()
            except KeyboardInterrupt:
                self.server_start = False
                self.protocol.shutdown()
                keluar(0)       
                
if __name__ == "__main__":
    server = Server0(TCP)
    server.prepareserver()
    server.recv_data_loop()
    