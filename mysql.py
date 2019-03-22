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
data_base = MySQLdb.connect(user=user, host=ip, password=password)
def run(order):    
    try:
        cur = data_base.cursor()
        cur.execute(order)
        hasil = []
        for i in cur.fetchall():
            hasil.append(i)
        return hasil
    except Exception as err:
        error(str(err))
        return str(err)

if __name__ == "__main__":
    while True:
        order = input("perintah: ")
        try:
            for i in run(order):
                print(i)
        except Exception as error:
            print(error)
def create_database():
    try:
        run("drop database %s" %(db_name))
    except:
        pass
    try:
        run("create database %s" %(db_name))
        run("use %s" %(db_name))
        run("create table conf (aturan varchar(100) primary key, nilai varchar(100))")
        print("[-INFO-] Done")
    except Exception as err:
        print("[-ERROR-] Cannot access mysql database\nplease make sure mysql is installed, running, and accessible:\n %s" %(str(err)))
        raise SystemExit
def check_database():
    try:
        run("use %s" %(db_name))
        temp = run("desc conf")
        if (temp[0][0]=='aturan' and temp[1][0] == "nilai"):
            return True
        raise ValueError
    except Exception as err:
        print("Database doesnt exist\nCreating the new one...")
        create_database()
def read_conf(key="ALL"):
    try:
        run("use %s" %(db_name))
        if (key=="ALL"):
            return dict(run('select * from conf'))
        else:
            return run('select nilai from conf where aturan="%s"' %(key))[0][0]
    except Exception as err:
        check_database()
def read_db(key, table):
    run("use %s" %(db_name))
    return run('select nilai from %s where aturan="%s"' %(table, key))[0][0]
    
    