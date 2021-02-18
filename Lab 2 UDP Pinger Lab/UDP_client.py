import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ('localhost', 12000)
sock.settimeout(1)
arr = []
total = 0
max = -2
min = 3
try:
    for i in range(1, 11):
        start = time.time()
        message = 'Ping ------ #' + str(i) + " " + time.ctime(start)
        try:
            sent = sock.sendto(bytes(message, 'UTF-8'), server_addr)
            print("Sent " + message)
            data, server = sock.recvfrom(4096)
            print(bytes("Received ", 'UTF-8') + data)
            end = time.time();
            elapsed = end - start
            print("RTT: " + str(elapsed) + " seconds\n")
            arr.append(elapsed)
            total = total + elapsed
            if(elapsed < min):
                min = elapsed
            if(elapsed > max):
                max = elapsed
        except socket.timeout:
            print("#" + str(i) + " Requested Time out\n")

finally:
    print("----Closing Socket")
    sock.close()


average = total/10
print("Average: ")
print(average)
print("Max: ")
print(max)
print("Min: ")
print(min)
