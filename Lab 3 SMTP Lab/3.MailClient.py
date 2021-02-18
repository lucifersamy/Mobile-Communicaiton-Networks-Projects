from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose Google mail server gmail and calling it mailserver
mailserver = ('smtp.gmail.com', 587)#Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Sending STARTTLS command
command="STARTTLS\r\n"
clientSocket.send(command.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
tls_socket=ssl.wrap_socket(clientSocket)


#Info for username and password
username =  "semadilber7@gmail.com"
password = "sample" #this is not my original password you can change username and password if you want
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)


authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
tls_socket.send(authMsg)
recv_auth = tls_socket.recv(1024).decode()
print(recv_auth.decode())
if recv_auth[:3] != '235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <semadilber7@gmail.com> \r\n"
tls_socket.send(mailFrom.encode())
recv2 = tls_socket.recv(1024).decode()
print("After MAIL FROM command: "+recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptTo = "RCPT TO: <sema.dilber2016@gtu.edu.tr> \r\n"
tls_socket.send(rcptTo.encode())
recv3 = tls_socket.recv(1024).decode()
print("After RCPT TO command: "+recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
tls_socket.send(data.encode())
recv4 = tls_socket.recv(1024).decode()
print("After DATA command: "+recv4)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end


# Send message data.
# Fill in start
subject = "Subject: SMTP mail client testing \r\n\r\n"
tls_socket.send(subject.encode())
tls_socket.send(msg.encode() + '\n')
#message = raw_input("Please write your message: \r\n")
#tls_socket.send(message.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
tls_socket.send(endmsg.encode())
recv_msg = tls_socket.recv(1024).decode()
print("Response after sending message body:"+recv_msg.decode())
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
tls_socket.send("QUIT\r\n".encode())
message=tls_socket.recv(1024).decode()
print (message)
tls_socket.close()
# Fill in end
