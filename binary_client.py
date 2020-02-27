import binascii
import socket
import struct

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
#sock.connect(server_address)

#values = (2576980377, b'\0\0\0\0', 100, 0x000A)
values = (0x98999999, 0x0000, 100, 0x000A)
packer = struct.Struct('I I I I')

unpacker = struct.Struct('I I I I')

packed_data = packer.pack(*values)

print('values =', values)

try:
    # Send data
    #print('sending {!r}'.format(binascii.hexlify(packed_data)))
    #sock.sendall(packed_data)

    sent = sock.sendto(packed_data, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(16)
    #print('received {!r}'.format(data))
    unpacked_data = unpacker.unpack(data)
    print('received unpacked:', unpacked_data)

finally:
    print('closing socket')
    sock.close()