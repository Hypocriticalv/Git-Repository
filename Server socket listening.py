import socket

s = socket.socket() #Create empty socket object
print('Socket created.')

#reserve a port on pc 1 - 65535
port = 15503

# Next bind to the port we have not typed any ip in the ip field 
# instead we have inputted an empty string this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('',port))
print('Socket binded to %s' %(port))

#put socket into listening mode, number has to do with max requests before denying connection
s.listen(5)
print('socket is listening')

# a forever loop until we interrupt it or an error occurs 
while True:
    c, addr = s.accept()  #establishing connection with client
    print('Got connection from',addr)
    # send a thank you message to the client. encoding to send byte type. 
    c.send('Thank you for connecting'.encode()) 
    # Close the connection with the client
    c.close()
    break