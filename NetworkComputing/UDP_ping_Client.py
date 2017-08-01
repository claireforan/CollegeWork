from socket import *
import time
hostname = gethostname()
server_address = (hostname, 12000)
# Create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)


try:
    # Send message 10 times
    i = 1
    while i <= 10:
        # Start time of RTT
        start = time.time()
        # Data is transmitted to the server with sendall()
        # encode() function returns bytes object
        message = 'Ping %i %i' % (i, time.time())
        print('sending "%s"' % message)
        sock.sendto(message.encode(), (server_address))
        # Start time out timer
        sock.settimeout(1)
        # if received in time
        try:  
            # Receiving message from server
            amount_received = 0
            amount_expected = len(message)
            
            while amount_received < amount_expected:
                # Data is read from the connection with recv()
                # decode() function returns string object
                data, addr = sock.recvfrom(1024)
                data = data.decode()
                amount_received += len(data)
                print('received "%s"' % data)
                finish = time.time()
                # calculate RTT and print it
                rtt = finish - start
                print("RTT: %f" % rtt)
                i += 1
        # if timed out
        except timeout:
            print("Request timed out")
# Close socket      
finally:
    print("closing socket")
    sock.close()