import socket
#module import for parsing url links
from urllib.parse import urlparse 

#list of accepted inputs
list = ['y','Y','Yes','YES','yes'] 

#AF_INET refers to address-family ipv4, sock_stream refers to TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


while True:
    url = input('Site name: ')
    try:
        #urlparse gets hostname from ip input
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname or url
        #Result gets the argument returned by parsed_url or ip
        result = socket.gethostbyname(hostname)
        print(f'The IP located at {hostname} is {result}.')
    except socket.gaierror:
            print('Invalid site name, try again.')
            
    reuse = input('Run again? :')
    if reuse not in list:
        break
        
        
