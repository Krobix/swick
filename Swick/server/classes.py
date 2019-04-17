import json

class UserDoesNotExistError(Exception):
    pass

class AnonUser:
    @staticmethod
    def fromDict(dicte):
        tempusr = AnonUser("temp")
        tempusr.__dict__ = dicte
        return tempusr

    
    def __init__(self, name):
        self.name = name
        self.__secret = "0"
        self.online = True
        self.banned = False
        self.muted = False

    def __eq__(self, other):
        return self.__secret == other.__secret

class User(AnonUser):
    @staticmethod
    def fromDict(dicte):
        tempusr = User("temp", "temp")
        tempusr.__dict__ = dicte
        return tempusr
    
    def __init__(self, name, secret):
        self.name = name
        super().__init__(name)

        with open("USRFILE.json", "r") as usrfile:
            tempDict = json.load(usrfile)
            try:
                self.__dict__ = tempDict[self.name]
            except KeyError:
                self.isAdmin = False
                self.banned = False
                self.muted = False
                self.__secret = secret
                self.online = False


                with open("USRFILE.json", "w") as wfile:
                    tempDict[self.name] = self.__dict__
                    json.dump(tempDict, wfile)

    


class Message:
    @staticmethod
    def fromDict(dicte):
        tempmsg = Message(dicte["author"], dicte["channel"])
        tempmsg.__dict__ = dicte
        return tempmsg
    
    def __init__(self, author, content):
        self.author = author
        self.content = content