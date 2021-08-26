
try:
  import usocket as socket
except:
  import socket

from machine import Pin
from neopixel import NeoPixel
import time
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

#ssid = 'N300 N1zi'
#password = 'loragera1'

ssid = 'show'
password = 'ilia2002'

nameArduino = "Tello1"

n = 26

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)

pin = Pin(14, Pin.OUT)   # set GPIO14 to output to drive NeoPixels
np = NeoPixel(pin, n)   # create NeoPixel driver on GPIO14 for 8 pixels

led_state = "OFF"
def web_page(text:str):
    html = """<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">

</head>

<body>
    <h2>""" + text + """</h2>
</body>

</html>"""
    return html


for i in range(n):
  np[i] = (0, 0, 0)
np.write() 



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        #print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request_d = request.decode("utf-8")
        request = str(request)
        #print('GET Rquest Content = %s' % request)
        led_on = request.find('/?led_2_on')
        led_off = request.find('/?led_2_off')
        
        
        
        if led_on == 6:
            print('LED ON -> GPIO2')  #lose')            
            led_state = "OFF"
            led.on() 
            
            for i in range(n):
              np[i] = (0, 0, 0)
            np.write()    
        if led_off == 6:
            print('LED OFF -> GPIO2')
            print('Open')
            led_state = "ON"

            led.off()
            r, g, b = request_d[16:request_d.find(' HTTP')].split('_')
            r, g, b = int(r), int(g), int(b)
            print('red = {}, green = {}, blue = {}'.format(r, g, b))
            r = r if 0 <= r <= 255 else 0 if r < 0 else 255
            g = g if 0 <= g <= 255 else 0 if g < 0 else 255
            b = b if 0 <= b <= 255 else 0 if b < 0 else 255
            for i in range(n):
              np[i] = (r, g, b)
            np.write()    
        response = web_page(nameArduino)
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')

'''from machine import Pin


n = 26
pin = Pin(14, Pin.OUT)   # set GPIO14 to output to drive NeoPixels
np = NeoPixel(pin, n)   # create NeoPixel driver on GPIO14 for 8 pixels
# np[0] = (255, 0, 0) # set the first pixel to white
for i in range(n):
  np[i] = (0, 0, 255)
#np.fill((0, 0, 255))

np.write()              # write data to all pixels

time.sleep_ms(1000)
'''


