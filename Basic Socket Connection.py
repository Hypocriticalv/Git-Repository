import socket
import sys

#AF_INET refers to address-family ipv4, sock_stream refers to TCP protocol
try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   print('Socket successfully created.') 
except socket.error as err:
    print('Socket creation failed with error %s' %(err))
#error if socket is unable to be created
    
#default socket port
port = 80 

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print('There was an error resolving the host.')
    sys.exit

s.connect((host_ip,port))
#connection from socket to google

print('This socket has successfully connected to Google.')
        
