import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET refers to address-family ipv4, sock_stream refers to TCP protocol
list = ['y','Y','Yes','YES','yes']
while True:
    ip = input('Site name: ')
    try:
        result = socket.gethostbyname(ip)
        print(result)
    except socket.gaierror:
            print('Invalid site name, try again.')
    reuse = input('Run again? :')
    if reuse not in list:
        break
        
        
