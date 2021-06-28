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
    
    def start(self):
        self.sock.sendto('command'.encode(encoding="utf-8"), self.tello_address)
        time.sleep(5)
    
    def takeoff(self):
        self.sock.sendto('takeoff'.encode(encoding="utf-8"), self.tello_address)
        time.sleep(10)
    
    def land(self):
        self.sock.sendto('land'.encode(encoding="utf-8"), self.tello_address)
        time.sleep(5)

    def get_battery(self):
        """Gets the battery value
        Returns:
            int: The percentage of battery remaining
        """
        order = "battery?"
        self.sock.sendto(order.encode(encoding="utf-8"), self.tello_address)
        time.sleep(2)
        print(self.sock)
