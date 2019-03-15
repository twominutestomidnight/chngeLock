class Camera:
    def __init__(self,ip,port,login,password):
        self.ip = ip
        self.port = port
        self.login = login
        self.password = password


    def __str__(self):
        return "ip : " + self.ip + ", port : " + str(self.port) + ", login : " + self.login + ", password : " \
               + self.password