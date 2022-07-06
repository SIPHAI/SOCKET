import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('172.16.3.172',58083))
s.listen(s)
clientsocket,clientaddress = s.accept()
print(clientsocket)
clientaddess
('172.16.3.172',58083)
print('Got a connection from %s' %str(clientaddress))

