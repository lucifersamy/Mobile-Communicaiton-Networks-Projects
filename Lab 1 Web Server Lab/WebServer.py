# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The web server is up on the port:', serverPort)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send(bytes('\n\nHTTP/1.1 200 OK\r\n\r\n', 'UTF-8'))
        connectionSocket.send(bytes(outputdata, 'UTF-8'))
        # Fill in end
        # Send the content of the requested file to the client
        #If this loop run Hello World writes 2 times I dont know why so I change it
        for i in range(0, 0):
            connectionSocket.send(bytes(outputdata[i], 'UTF-8'))
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send(bytes('\nHTTP/1.1 404 Not Found\n\n', 'UTF-8'))
        connectionSocket.send(bytes('\n404 Not Found\n\n', 'UTF-8'))
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
