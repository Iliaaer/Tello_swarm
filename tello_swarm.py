import socket
import threading
import time


class Tello:
    host = ""
    port = 9000
    locaddr = (host, port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(locaddr)
    tello_address = ('', 8889)

    def __init__(self, ip_addres) -> None:
        self.tello_address = (ip_addres, 8889)
    
    def start(self, delay:int=5):
        self.sock.sendto('command'.encode(encoding="utf-8"), self.tello_address)
        time.sleep(delay)
    
    def takeoff(self, delay:int=10):
        self.sock.sendto('takeoff'.encode(encoding="utf-8"), self.tello_address)
        time.sleep(delay)
    
    def land(self, delay:int=5):
        self.sock.sendto('land'.encode(encoding="utf-8"), self.tello_address)
        time.sleep(delay)

    def get_battery(self, delay:int=2):
        order = "battery?"
        self.sock.sendto(order.encode(encoding="utf-8"), self.tello_address)
        time.sleep(delay)
