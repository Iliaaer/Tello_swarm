import os
import platform
import threading
from time import sleep
from typing import Union
import netifaces
import socket
import requests 
import netaddr


class FlyArduino:

    def __init__(self, arduino_sn_list: list):
        self.session = requests.session()
        subnets, address = self._get_subnets()
        self.possible_addr = list()
        self.tello_arduino = {}
        first_ip=1
        last_ip=254

        oc = platform.system()
        if (oc == "Windows"):
            self.ping_com = "ping -n 1 "
        else:
            self.ping_com = "ping -c 1 "

        print("Scanning in Progress:")

        for subnet, netmask in subnets:
            if len(self.tello_arduino) == len(arduino_sn_list):
                break
            for ip in netaddr.IPNetwork('%s/%s' % (subnet, netmask)):
                if len(self.tello_arduino) == len(arduino_sn_list):
                    break
                if not (first_ip <= int(str(ip).split('.')[3]) <= last_ip):
                    continue
                if str(ip) in address:
                    continue
                potoc = threading.Thread(target=self._scan_Ip, args=[ip, arduino_sn_list])
                potoc.setName("Arduino=" + str(ip))
                potoc.start()
        potoc.join()
        
        print("Scanning completed")


    def _get_subnets(self):
        subnets = []
        addr_list = []
        ifaces = netifaces.interfaces()
        for this_iface in ifaces:
            addrs = netifaces.ifaddresses(this_iface)
            if socket.AF_INET not in addrs:
                continue
            ip_info = addrs[socket.AF_INET][0]
            address = ip_info['addr']
            netmask = ip_info['netmask']
            if netmask != '255.255.255.0':
                continue
            cidr = netaddr.IPNetwork('%s/%s' % (address, netmask))
            network = cidr.network
            subnets.append((network, netmask))
            addr_list.append(address)
        return subnets, addr_list

    def _scan_Ip(self, ip:str, arduino_sn_list) -> None:
        if len(self.tello_arduino) == len(arduino_sn_list):
            return
        addr = str(ip)
        comm = self.ping_com + addr
        response = os.popen(comm)
        data = response.readlines()
        for line in data:
            if 'TTL' in line:
                print(addr, "--> Ping Ok")
                url = 'http://' + addr + '/'
                try:
                    r = requests.get(url)
                    a = r.text.split('<h2>')[1].split('</h2>')[0]
                    print(a)
                    if a in arduino_sn_list:
                        self.tello_arduino[a] = addr
                except:
                    print('No')
                    pass
                break

    def led_on(self, arduino:Union[int, str]='All', red:int=255, green:int=255, blue:int=255) -> None:
        if type(arduino) == int:
            arduino = 'Tello' + str(arduino)
        try:
            if arduino == 'All':
                for ip in self.tello_arduino.values():
                    self.session.get('http://' + ip + '/?led_2_off_{}_{}_{}'.format(red, green, blue))
            else:
                ip = self.tello_arduino[arduino]
                self.session.get('http://' + ip + '/?led_2_off_{}_{}_{}'.format(red, green, blue))
        except:
            pass 
        sleep(0.1)


    def led_off(self, arduino:Union[int, str]='All') -> None:
        if type(arduino) == int:
            arduino = 'Tello' + arduino
        try:
            if arduino == 'All':
                for ip in self.tello_arduino.values():
                    self.session.get('http://' + ip + '/?led_2_on')
            else:
                ip = self.tello_arduino[arduino]
                self.session.get('http://' + ip + '/?led_2_on')
        except:
            pass
        sleep(0.1)