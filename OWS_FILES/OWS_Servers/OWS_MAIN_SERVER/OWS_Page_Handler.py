
def Get_Data(data="", args=""):
    #special handling for method and file
    try:
        data = data.encode("utf-8")
    except:
        pass
    the_data = {}
    try:
        the_data[b"file"] = data.split(b" ")[1].strip(b"/")
    except Exception as error: 
        print("ERROR", data)

    the_data[b"method"] = data.split(b" ")[0]
    dat = data.split(b"\r\n")

    #clearing dat without ':'
    angka = 0
    for i in dat:
        if (not (b":"in i)):
            del dat[angka]
        else:
            dat[angka] = dat[angka].strip(b" ").rstrip(b" ")
            if (dat[angka]==b''):
                del dat[angka]
        angka+=1

    for i in dat:
        temp = i.split(b":")
        try:
            the_data[temp[0].rstrip(b" ").strip(b" ")] = temp[1].rstrip(b" ").strip(b" ")
        except:
            continue
    if (not(len(args))):
        return the_data
    else:
        return the_data[args]


def Main(data):
    print(data)

module_name = "OWS_Page_Handler"