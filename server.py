
import socket 

host = ''
port = 50000
backlog = 5
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

print "server listening..."

while True:
    client, address = s.accept()
    data = client.recv(size)

    if data:
        client.send(data)
    
    client.close()

print "server closed."
