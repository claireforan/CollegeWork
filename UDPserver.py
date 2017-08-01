from socket import *
import time
hostname = gethostname()
ip = gethostbyname(hostname)
sock = socket(AF_INET, SOCK_DGRAM)
server_address = (hostname, 6789)
sock.bind(server_address)

while True:

    try:
        while True:
            # decode() function returns string object
            print("waiting")
            data, addr = sock.recvfrom(1024)
            data = data.decode()
            if data:
                print('received "%s"' % data)
                print('sending data back to the client')
                # Create/Open the file to write logs into
                filehandle = open("filelog.txt", "a")
                # Set value to the current time
                receive_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
                info = "%s (%s) \n" % (data.upper(), receive_time)
                # Write the data 'info', into the file
                filehandle.write(info)
                filehandle.close()
                data = "%s, %s" % (data.upper(), receive_time)
                sock.sendto(data.encode(), (addr))

            else:
                print('no more data from %s', client_address)
                break
            
    finally:
        # Clean up the connection
        sock.close()
        
