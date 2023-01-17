import socket
 
serverMACAddress = '98:D3:32:21:18:6D'
port = 4
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
s.send(bytes("F"))
s.close()