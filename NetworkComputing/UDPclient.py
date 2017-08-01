from socket import *
hostname = gethostname()
server_address = (hostname, 6789)
sock = socket(AF_INET, SOCK_DGRAM)


try:

    # Send data
    message = 'message'
    print('sending "%s"' % message)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendto(message.encode(), (server_address))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        # Data is read from the connection with recv()
        # decode() function returns string object
        data, addr = sock.recvfrom(1024)
        data = data.decode()
        amount_received += len(data)
        print('received "%s"' % data)
finally:
    sock.close()