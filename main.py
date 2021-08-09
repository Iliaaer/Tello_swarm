
# For more details and step by step guide visit: Microcontrollerslab.com

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'N300 N1zi'
password = 'loragera1'
nameArduino = "Tello1"

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)


led_state = "OFF"
def web_page(text:str):
    html = """<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }
    </style>
</head>

<body>
    <h2>""" + text + """</h2>
</body>

</html>"""
    return html




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
        led_on = request.find('/?led_2_on')
        led_off = request.find('/?led_2_off')
        
      
        if led_on == 6:
            print('LED ON -> GPIO2')  # Выключение
            print('Close')            
            led_state = "OFF"
            led.on() 
        if led_off == 6:
            print('LED OFF -> GPIO2') # Включение
            print('Open')
            led_state = "ON"

            led.off()
            r, g, b = request_d[16:request_d.find(' HTTP')].split('_')
            print('red = {}, green = {}, blue = {}'.format(r, g, b))  
        response = web_page(nameArduino)
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')
