from fly_tello import FlyTello
from fly_arduino import FlyArduino
from time import sleep

my_tellos = list()
my_arduino = list()

# my_tellos.append('0TQZHBRED0113W') # tello=1       Главный
my_tellos.append('0TQZHARED00ZWY') # tello=2       Запасной

my_arduino.append('Tello1')
my_arduino.append('Tello2')

arduino = FlyArduino(my_arduino)
fly = FlyTello(my_tellos)

print('============================================')
input('Go?')

fly.takeoff()
arduino.led_on()
fly.forward(dist=50)
fly.get_battery()
arduino.led_off()
arduino.led_on()
arduino.led_off()
arduino.led_on()
arduino.led_off()
arduino.led_on()
arduino.led_off()
arduino.led_on()
arduino.led_off()
fly.land()
arduino.led_on()

'''arduino.led_on()
sleep(2)
arduino.led_off()
sleep(2)
arduino.led_on(arduino=1)
sleep(2)
arduino.led_on(arduino=2)
sleep(2)
arduino.led_off()
sleep(2)
arduino.led_on()'''


