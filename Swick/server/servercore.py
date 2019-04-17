import socketserver
import threading
import json
from .handler import RequestHandler

class SwickServer:
    def __init_(self):
        try:
            with open("SWICKSERVCONF.json", "r") as configFile:
                config = json.load(configFile)
        except:
            raise RuntimeError("SWICKSERVCONF.json is not formatted properly, or could not be read.")

        self._server = mainServer = socketserver.TCPServer((config["address"], config["port"]), RequestHandler)



