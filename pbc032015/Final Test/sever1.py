import threading
import redis 
import socket


sock  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("localhost",6379))
sock.listen(5)
connection, client_address = sock.accept()
