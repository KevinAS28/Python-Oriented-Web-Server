import MySQLdb
from printt import *

db_name = "OWS"
if __name__ != "__main__":
    ip = "127.0.0.1"
    port=int("100")
    user = "root"
    password = ""
    
ip = "127.0.0.1"
port=int("100")
user = "root"
password = ""
"""
else:
    ip = input("ip: ")
    port = int(input("port: "))
    nama = input("nama database: ")
    user = input("username: ")
    password = input("password: ")
"""
try:
    data_base = MySQLdb.connect(user=user, host=ip, password=password)
except Exception as err:
    Error("Cannot connect to MYSQL database. the common problem is the MYSQL is not running or port is blocked")
def Run(order):    
    try:
        cur = data_base.cursor()
        cur.execute(order)
        hasil = []
        for i in cur.fetchall():
            hasil.append(i)
        return hasil
    except Exception as err:
        Error(str(err))
        return str(err)

if __name__ == "__main__":
    while True:
        order = input("perintah: ")
        try:
            for i in Run(order):
                print(i)
        except Exception as err:
            print(err)
def Create_Database():
    try:
        Run("drop database %s" %(db_name))
    except:
        pass
    try:
        Run("create database %s" %(db_name))
        Run("use %s" %(db_name))
        Run("create table conf (aturan varchar(100) primary key, nilai varchar(100))")
        Info("Done.")
    except Exception as err:
        Error("Cannot access mysql database\nplease make sure mysql is installed, Running, and accessible:\n %s" %(str(err)))
        raise SystemExit
def Check_Database():
    try:
        Run("use %s" %(db_name))
        temp = Run("desc conf")
        if (temp[0][0]=='aturan' and temp[1][0] == "nilai"):
            return True
        raise ValueError
    except Exception as err:
        print("Database doesnt exist\nCreating the new one...")
        Create_Database()
def Read_Conf(key="ALL"):
    try:
        Run("use %s" %(db_name))
        if (key=="ALL"):
            return dict(Run('select * from conf'))
        else:
            return Run('select nilai from conf where aturan="%s"' %(key))[0][0]
    except Exception as err:
        Check_Database()
def Read_Conf_List(key="ALL"):
    return list(map(lambda x: x.replace(" ", ""), Read_Conf(key).split(",")))
    
def Read_DB(key, table):
    Run("use %s" %(db_name))
    return Run('select nilai from %s where aturan="%s"' %(table, key))[0][0]

module_name = "MYSQL"

    