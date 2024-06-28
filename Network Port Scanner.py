#import all necessary modules
import pyfiglet
import sys
import socket
from datetime import datetime
#neat looking banner
ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)
#defining a target for running script, one argument is the script name and the other is hostname/target IP
if len(sys.argv) == 4:
    try:
        target = socket.gethostbyname(sys.argv[1])
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
        if start_port < 1 or end_port > 65535:
            print('Invalid range, please select a port between 1 and 65535.')
            sys.exit()
        if start_port > end_port:
            print('End port cannot be greater than start port.')
            sys.exit()
        elif start_port and end_port == int():
            print(f'Thank you for selecting port range between {start_port} and {end_port}.')       
    except socket.gaierror:
        print('Hostname could not be resolved, exiting program.')
        sys.exit()
    except ValueError:
        print('Please select a port between 1 and 65535.')
else:
    print('Invalid amount of arguments.')
    print('You can use this script with the following command: python "Network Port Scanner.py" <hostname> <port 1> <port 2>')
    sys.exit()
    
#adding a banner notifying the user about target being scanned + time the scan was started
print('-' * 75)
print('Scanning target: '  +  target)
print('Scanning started at', str(datetime.now()))
print('-' * 75)

counter = 0
#adding in port range to be scanned and executing scan, ports can range from 1 - 65535
try:
    
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        
        if result == 0:
            counter += 1
            print(f'Port {port} is open.')
        s.close()
except socket.gaierror:
    print('Hostname could be resolved, exiting program.')
    sys.exit()
except KeyboardInterrupt:
    print('Scanning interrupted, exiting program.')
    sys.exit()
except socket.error:
    print('Server not responding, exiting program.')
    sys.exit()

print('-' * 75)
print('Scanning completed at' + str(datetime.now()))
print(f'Found {counter} open port(s).')
print('-' * 75)
        
