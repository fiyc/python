import socket

socket.setdefaulttimeout(10)
s = socket.socket()
s.connect(("103.229.127.100", 21))
ans = s.recv(1024)
print(ans)