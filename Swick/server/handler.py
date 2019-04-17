import socketserver
import json
from .classes import *

def writeServerMsg(file, text):
    tempmsg = Message(AnonUser("SYSTEM"), text)


class RequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        self.data = json.load(self.rfile)

        out = self.wfile 
        
        msgType = self.data["MSGTYPE"]
        
        if msgType == "usrSendMsg":
            self.msg = Message.fromDict(self.data)

        elif msgType == "usrJoin":
            joinedUsr = User.fromDict(self.data)
            with open("USRFILE.json", "r") as usrfile:
                try:
                    usr = json.load(usrfile)
                    for x in usr:
                        if joinedUsr.online:
                            raise RuntimeError("The requested user is already online.")
                        elif usr[x] == joinedUsr:
                            usr[x].online = True
                            usrFound = True
                            out.write(json.dumps({
                                "JOINSTATUS":"success"
                            }))
                        else:
                            usrFound = False
                    if not usrFound:
                        raise UserDoesNotExistError()

                except UserDoesNotExistError:
                    out.write(json.dumps({
                        "JOINSTATUS": "fail"
                    }))