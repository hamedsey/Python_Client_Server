import binascii
import socket
import struct
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address = ('192.168.0.1', 5001)
#server_address = ('128.61.18.161', 5001)
#server_address = ('130.207.122.162', 5001)
#server_address = ("130.207.125.115", 5099)
server_address = ('127.0.0.1', 5099)

#sock.connect(server_address)

#values = (2576980377, b'\0\0\0\0', 100, 0x000A)
values = (0x98999999, 0x0000, 5001, 0xBBAA, 100)
packer = struct.Struct('= I H I I I')

unpacker = struct.Struct('= I H I I I')

packed_data = packer.pack(*values)

print('values =', values)

file1 = open("client_time.txt","a") 

try:
    # Send data
    #print('sending {!r}'.format(binascii.hexlify(packed_data)))
    #sock.sendall(packed_data)
    #x = range(100)
    #for i in x:
    sent = sock.sendto(packed_data, server_address)
    start_time = time.time()

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(18)
    end_time = time.time()
    #print('received {!r}'.format(data))
    unpacked_data = unpacker.unpack(data)
    elapsed_time = (end_time - start_time)*1000000;
    print('Elapsed Time: ', elapsed_time)
    file1.write(str(elapsed_time))
    file1.write("\n")
    print('received unpacked:', unpacked_data)

finally:
    print('closing socket')
    sock.close()
    file1.close()