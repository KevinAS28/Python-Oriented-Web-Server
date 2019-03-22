if (True):
    def Padding(self, data):
        if (type(data)!=bytes):
            try:
                data = data.encode("utf-8")
            except:
                pass
        while ((len(data)%16)!=0):
            data += b"\0"
        return data
    @property
    def AES_PASSWORD():
        return """F<{Z[C?AY)L7!Yc@"""
    @property
    def AES_IV():
        return """nrB27PNZTnn-N^dR"""
    def Encrypt_AES(self, data):
        aes = AES.new(self.AES_PASSWORD, AES.MODE_CBC, self.AES_IV)
        return aes.encrypt(self.Padding(data))
    
    def Decrypt_AES(self, data):
        aes = AES.new(self.AES_PASSWORD, AES.MODE_CBC, self.AES_IV)
        return aes.decrypt(self.Depadding(data))
    
    def AFD(self, file, result=""): #AES File Decrypt
        if not (len(result)):
            result=file.rstrip(self.Enc_Extension)
        self.Check_File_Internal(result)
        with open(file, "rb") as baca:
            with open(result, "wb") as tulis:
                tulis.write(self.Decrypt_AES(baca.read()))
    
    def AFE(self, file, result=""): #AES File Encrypt
        if not len(result):
            result=file+self.Enc_Extension
        self.Check_File_Internal(result)
        with open(file, "rb") as baca:
            with open(result, "wb") as tulis:         
                tulis.write(self.Encrypt_AES(baca.read()))

