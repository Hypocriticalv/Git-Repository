#import all necessary modules
import pyfiglet
import sys
import socket
from datetime import datetime
#neat looking banner
def banner():
    ascii_banner = pyfiglet.figlet_format("Port Scanner")
    print(ascii_banner)
#defining a target for running script, one argument is the script name and the other is hostname/target IP, arguments for start/end port
def target_inputs():
    global target, start_port, end_port
    try:
        target = socket.gethostbyname(input('Target host/IP: '))
        start_port = int(input('Start Port (Enter number between 1 & 65534): '))
        end_port = int(input('End port (Enter number between 2 and 65535): '))
        if start_port < 1 or end_port > 65535:
            print('Invalid range, please select a port between 1 and 65535.')
            sys.exit()
        if start_port > end_port:
            print('End port cannot be greater than start port.')
            sys.exit()
        print(f'Thank you for selecting port range between {start_port} and {end_port}.')       
    except socket.gaierror:
        print('Hostname could not be resolved, exiting program.')
        sys.exit()
    except ValueError:
        print('Please select a port between 1 and 65535.')
    
#adding a banner notifying the user about target being scanned + time the scan was started
def start_scan():
    print('-' * 75)
    print('Scanning target: '  +  target)
    print('Scanning started at', str(datetime.now()))
    print('-' * 75)

global counter 
counter = 0
#adding in port range to be scanned and executing scan, ports can range from 1 - 65535
def port_scan():
    global counter
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
def end_scan():
    print('-' * 75)
    print('Scanning completed at', str(datetime.now()))
    print(f'Found {counter} open port(s).')
    print('-' * 75)
    
def again():
    global reuse
    while True:
        reuse = input('Would you like to start a new scan? (y/n) : ')
        if reuse not in ['y', 'n']:
            print('Invalid input, enter y or n.')
            continue
        elif reuse == 'y':
            main()
        else:
            print('Thanks for using the Network Port Scanner!')
            sys.exit()
             
def main():
    banner()
    target_inputs()
    start_scan()
    port_scan()
    end_scan()
    again()
    
if __name__ == "__main__":
    main()
    