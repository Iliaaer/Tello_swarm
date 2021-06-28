from tello_swarm import Tello

tello1 = Tello('192.168.10.1')

tello1.start()
tello1.get_battery()