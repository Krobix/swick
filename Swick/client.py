import socket
import threading

server = 0
outf = 0
inf = 0

def start():
    global server, outf, inf
    print("Welcome to the swick messenger.\n")
    address = input("Please enter the address of the server that you would like to join.\n")
    print("\n")
    port = input("Please enter the server port.\n")
    print("\n\n")
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((address, port))
    outf = server.makefile(mode="w")
    inf = server.makefile(mode="r")

    